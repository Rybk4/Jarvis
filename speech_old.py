# speech_processing.py

import argparse
import queue
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from word2numberi18n import w2n
import json

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status, q, model, dump_fn):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def extract_and_process_result(result):
    # Extract the value of the "text" field from JSON
    text_value = result.get("text", "")

    # Преобразование слов в цифры в итоговом результате
    words = text_value.split()
    for i, word in enumerate(words):
        try:
            numeric_value = w2n.word_to_num(word)
            words[i] = str(numeric_value)
        except ValueError:
            pass  # Не удалось преобразовать, оставляем слово без изменений

    updated_result = ' '.join(words)
    print(updated_result)
    return updated_result

def process_audio_input(device=None, samplerate=None, model=None):
    q = queue.Queue()
    updated_result = None  # Устанавливаем значение по умолчанию

    try:
        if samplerate is None:
            # Получаем информацию об устройстве, если значение не указано
            device_info = sd.query_devices(device, "input")
            samplerate = int(device_info["default_samplerate"])

        if model is None:
            # Используем языковую модель по умолчанию, если не указано другое значение
            model = Model(lang="ru")
        else:
            model = Model(lang=model)

        with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device,
                dtype="int16", channels=1, callback=lambda indata, frames, time, status: callback(indata, frames, time, status, q, model, None)):

            rec = KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()

                if rec.AcceptWaveform(data):
                    final_result = json.loads(rec.Result())

                    updated_result = extract_and_process_result(final_result)
                    if updated_result !="":

                        return updated_result

    except KeyboardInterrupt:
        print("\nDone")
    except Exception as e:
        print(type(e).__name__ + ": " + str(e))
    finally:
        return updated_result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-l", "--list-devices", action="store_true",
        help="show list of audio devices and exit")
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        sys.exit(0)

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        "-f", "--filename", type=str, metavar="FILENAME",
        help="audio file to store recording to")
    parser.add_argument(
        "-d", "--device", type=int_or_str,
        help="input device (numeric ID or substring)")
    parser.add_argument(
        "-r", "--samplerate", type=int, help="sampling rate")
    parser.add_argument(
        "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
    args = parser.parse_args(remaining)

    process_audio_input(args.device, args.samplerate, args.model)

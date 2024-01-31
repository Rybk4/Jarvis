import requests
import sounddevice as sd
import numpy as np
import io
import soundfile as sf

def record_audio(filename='recorded_audio.wav', duration=5, samplerate=16000):
    print("Recording...")
    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    sf.write(filename, audio_data, samplerate)

def recognize_speech_yandex(api_key, audio_file):
    with open(audio_file, 'rb') as file:
        audio_data = file.read()

    url = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"
    headers = {
        'Authorization': f"Api-Key {api_key}",
        'Content-Type': 'audio/x-wav',
    }

    params = {
        'format': 'lpcm',
        'sampleRateHertz': 16000,
    }

    response = requests.post(url, headers=headers, params=params, data=audio_data)

    if response.status_code == 200:
        result = response.json()
        if 'result' in result:
            print("Распознавание речи (Yandex SpeechKit):", result['result'])
        else:
            print("Ошибка распознавания:", result)
    else:
        print("Ошибка запроса к Yandex SpeechKit:", response.status_code, response.text)

if __name__ == "__main__":
    API_KEY = 'ВАШ_API_КЛЮЧ_YANDEX_SPEECHKIT'
    audio_filename = 'recorded_audio.wav'

    record_audio(audio_filename)
    recognize_speech_yandex(API_KEY, audio_filename)

import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    print("Голосовой помощник активирован. Говорите...")

    while True:
        with sr.Microphone() as source:
            try:
                audio_data = recognizer.listen(source, timeout=5)  # запись аудио с микрофона

                print("Распознавание речи:")
                text = recognizer.recognize_google(audio_data, language="en-US")  # Распознавание на английском
                print("Текст (английский):", text)

                russian_text = recognizer.recognize_google(audio_data, language="ru-RU")  # Распознавание на русском
                print("Текст (русский):", russian_text)

            except sr.UnknownValueError:
                print("Не удалось распознать речь.")
            except sr.RequestError as e:
                print(f"Ошибка при запросе к Google Web Speech API; {e}")

if __name__ == "__main__":
    recognize_speech()

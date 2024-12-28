import speech_recognition as sr

from lamp import Lamp


class Voice:
    """Декоратор голоса
    """

    def __init__(self, lamp: Lamp):
        self.lamp = lamp

    def functional(self):
        # Инициализация распознавателя
        recognizer = sr.Recognizer()

        # Использование микрофона для захвата речи
        with sr.Microphone() as source:
            print("Дайте команду...")
            audio = recognizer.listen(source)

        # Распознавание речи с использованием Google Web Speech API
        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {text}")
            if "включить" in text:
                self.lamp = 100
                print("Лампа включена")

            elif "выключить" in text:
                self.lamp = 0
                print("Лампа выключена")

            else:
                print("Команда не найдена")

        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса; {e}")


class Automation:
    """Автоматизация
    """

    def __init__(self, lamp: Lamp):
        self.lamp = lamp
    
    def functional(self):
        start = int(input("Начало работы:"))
        end = int(input("Конец работы:"))
        if start > end:
            print("Ошибка времени")
        else:
            self.lamp.brightness = 0
            print(f"Лампа будет работать с {start} по {end}")


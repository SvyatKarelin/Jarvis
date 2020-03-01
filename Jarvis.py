# Для распознавания речи требуются библиотеки SpeechRecognition и Pocket Sphinx
# установка на raspberry:
# pip3 install SpeechRecognition
# pip3 install pocketsphinx

# для Windows/Anaconda:
# conda install -c conda-forge speechrecognition

# редактируем словарь известных системе произношений
# sudo nano /home/pi/.local/lib/python3.7/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict
# оставляем только ключевое слово для активации Джарвиса - jarvis JH AA R V AH S


import os
import speech_recognition as sr


class Jarvis:
    def __init__(self):
        # конструктор
        self.r = sr.Recognizer()

    def checkActive(self):
        with sr.WavFile("send.wav") as source:
            audio = self.r.record(source)

        try:
            # используем возможности библиотеки Spinx
            t = self.r.recognize_sphinx(audio)
            print(t)
        except LookupError:
            print("Не могу распознать аудио-поток")

        return t == "jarvis"

    def playHiBeep(self):
        # todo проигрываем сигнал активности
        print('hi beep!')

    def listen(self):
        # записываем 3 секунды эфира с микрофона
        #os.system('arecord -B --buffer-time=1000000 -f dat -r 16000 -d 3 -D plughw:1,0 send.wav')
        with self.r.Microphone() as source:
            audio = self.r.listen(source)

    def say(self, words):
        # todo text-to-speech
        print(words)

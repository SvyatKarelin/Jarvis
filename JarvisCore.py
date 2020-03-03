# Для распознавания речи требуются библиотеки SpeechRecognition и Pocket Sphinx
# установка на raspberry:
# pip3 install SpeechRecognition
# pip3 install pocketsphinx

# для Windows/Anaconda:
# conda install -c conda-forge speechrecognition

# редактируем словарь известных системе произношений
# sudo nano /home/pi/.local/lib/python3.7/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict
# оставляем только ключевые слова для активации Джарвиса
# - jarvis JH AA R V AH S
# - stop S T AO P


import os
import time
import speech_recognition as sr
from YandexCloud import YandexStuff

class Jarvis:

    def __init__(self):
        # конструктор
        self.yandexStuff = YandexStuff()
        self.r = sr.Recognizer()
        self.iamToken, self.iamTokenExpires = self.yandexStuff.create_token()
        #self.yandexStuff.createSynthAudio(self.iamToken, "Привет, я Джарвис. Готов к работе.")
        self.play('audio/powerup.wav')
        time.sleep(0.5)
        self.play('audio/jarvisHi.wav')
        time.sleep(0.5)
        self.playLowBeep()

    def destroy(self):
        self.play('audio/powerdown.wav')
        time.sleep(1)
        self.play('audio/jarvisBye.wav')

    def checkActive(self):
        # 0 - неактивен
        # 1 - активация по слову Jarvis
        # 2 - стоп-слово Stop
        result = 0
        t = ""

        with sr.WavFile("audio/tmp/send.wav") as source:
            audio = self.r.record(source)

        # используем возможности библиотеки Spinx
        try:
            t = self.r.recognize_sphinx(audio)
            print("Sphinx thinks you said: [" + t + "]")
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        if t == "jarvis":
            result = 1
        elif t == "stop":
            result = 2

        if result == 1:
            self.playHiBeep()

        return result

    def playHiBeep(self):
        os.system("aplay audio/beep_hi.wav")

    def playLowBeep(self):
        os.system("aplay audio/beep_lo.wav")

    def listen(self, n, useOgg = False):
        # записываем n секунд эфира с микрофона
        os.system('arecord -fcd -d' + str(n) + ' audio/tmp/send.wav')

        if useOgg:
            os.system('opusenc --bitrate 48 audio/tmp/send.wav audio/tmp/send.ogg')

        # with self.r.Microphone() as source:
        #    audio = self.r.listen(source)

    def play(self, file):
        os.system('aplay ' + file)

    def say(self, words):
        # todo text-to-speech
        print(words)

    def yandexRecognize(self):
        # speech-to-text от старины Яндекса
        recognizedText = self.yandexStuff.recognize(self.iamToken)
        print(recognizedText)


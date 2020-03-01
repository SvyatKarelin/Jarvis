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
from YandexCloud import YandexStuff

class Jarvis:

    def __init__(self):
        # конструктор
        self.yandexStuff = YandexStuff()
        self.r = sr.Recognizer()
        self.iamToken, self.iamTokenExpires = self.yandexStuff.create_token()

    def checkActive(self):
        result = False
        t = ""
        """
        with self.r.Microphone() as source:
            audio = self.r.listen(source)

        try:
            t = self.r.recognize_sphinx(audio)
            print("Sphinx thinks you said " + t)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        """

        with sr.WavFile("send.wav") as source:
            audio = self.r.record(source)


        # используем возможности библиотеки Spinx
        try:
            t = self.r.recognize_sphinx(audio)
            print("Sphinx thinks you said: [" + t + "]")
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        result = t == "jarvis"
        if result:
            self.playHiBeep()

        return result

    def playHiBeep(self):
        os.system("aplay audio/beep_hi.wav")

    def playLowBeep(self):
        os.system("aplay audio/beep_lo.wav")

    def listen(self, n, useOgg = False):
        # записываем n секунд эфира с микрофона
        os.system('arecord -fcd -d' + str(n) + ' send.wav')

        if useOgg:
            os.system('opusenc --bitrate 48 send.wav send.ogg')

        # with self.r.Microphone() as source:
        #    audio = self.r.listen(source)

    def say(self, words):
        # todo text-to-speech
        print(words)

    def yandexRecognize(self):
        # speech-to-text от старины Яндекса
        recognizedText = self.yandexStuff.recognize(self.iamToken)
        print(recognizedText)


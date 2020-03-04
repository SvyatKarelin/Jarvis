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


import os
import time
import subprocess
import speech_recognition as sr
from YandexCloud import YandexStuff

class Jarvis:

    def __init__(self, logAll = False):
        # конструктор
        self.logAll = logAll
        self.yandexStuff = YandexStuff()

        self.r = sr.Recognizer()
        self.iamToken, self.iamTokenExpires = self.yandexStuff.create_token()
        #self.yandexStuff.createSynthAudio(self.iamToken, "Привет, я Джарвис. Готов к работе.")

        self.play('audio/powerup.wav')
        time.sleep(0.5)
        # todo uncomment
        self.play('audio/jarvisHi.wav')
        time.sleep(0.5)
        self.playLowBeep()

    def destroy(self):
        # todo uncomment self.play('audio/jarvisBye.wav')
        time.sleep(1)
        self.play('audio/powerdown.wav')

    def checkActive(self):

        result = False
        t = ""

        with sr.WavFile("audio/tmp/send.wav") as source:
            audio = self.r.record(source)

        # используем возможности библиотеки Spinx
        try:
            t = self.r.recognize_sphinx(audio)# todo check, language='ru-RU/cmusphinx-ru-5.2')
            if t != "" or self.logAll:
                print("Sphinx thinks you said: [" + t + "]")
        except sr.UnknownValueError:
            result = 0
            if self.logAll:
                print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        if t == "jarvis":
            result = True

        if result:
            self.playHiBeep()

        return result

    def playHiBeep(self):
        Jarvis.sysCommand("aplay audio/beep_hi.wav", self.logAll)

    def playLowBeep(self):
        Jarvis.sysCommand("aplay audio/beep_lo.wav", self.logAll)

    def listen(self, n, useOgg = False):
        # записываем n секунд эфира с микрофона
        Jarvis.sysCommand('arecord -fcd -d' + str(n) + ' audio/tmp/send.wav', self.logAll)

        if useOgg:
            Jarvis.sysCommand('opusenc --bitrate 48 audio/tmp/send.wav audio/tmp/send.ogg', self.logAll)

        # with self.r.Microphone() as source:
        #    audio = self.r.listen(source)

    @staticmethod
    def sysCommand(command, logAll = False):
        #c = "{}{}".format(command, self.devNull)
        #os.system(c)
        subprocess.run(
            command,
            shell = True,
            capture_output = not logAll)

    @staticmethod
    def play(file):
        Jarvis.sysCommand('aplay ' + file)

    @staticmethod
    def say(self, words):
        # todo text-to-speech
        print(words)

    def yandexRecognize(self):
        # speech-to-text от старины Яндекса
        recognizedText = self.yandexStuff.recognize(self.iamToken)
        result = recognizedText['result']
        print(result)
        return result


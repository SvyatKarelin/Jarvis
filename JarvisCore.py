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
import speech_recognition as speech

import CommandChecker
from YandexCloud import YandexStuff
from modules.radio import Radio
from modules.anekdot import Anekdot
from modules.game import Game
from modules.weather import Weather
from modules.city import city_game

class Jarvis:

    def __init__(self, logAll = True):
        # конструктор
        self.logAll = logAll
        self.yandexStuff = YandexStuff()
        self.loop = True

        # создаем модули
        self.radio = Radio()
        self.anekdot = Anekdot()
        self.game = Game()
        self.weather = Weather()
        self.citygame = city_game()


        self.recognizer = speech.Recognizer()
        self.iamToken, self.iamTokenExpires = self.yandexStuff.create_token()

        self.play('audio/powerup.wav')
        time.sleep(0.5)
        # todo uncomment
        self.play('audio/jarvisHi.wav')
        time.sleep(0.5)
        self.playLowBeep()

    def destroy(self):
        self.play('audio/jarvisBye.wav')
        time.sleep(1)
        self.play('audio/powerdown.wav')
        self.loop = False

    def checkActive(self):

        result = False
        t = ""

        with speech.WavFile("audio/tmp/send.wav") as source:
            audio = self.recognizer.record(source)

        # используем возможности библиотеки Spinx
        try:
            t = self.recognizer.recognize_sphinx(audio)# todo check, language='ru-RU/cmusphinx-ru-5.2')
            if t != "" or self.logAll:
                print("Sphinx thinks you said: [" + t + "]")
        except speech.UnknownValueError:
            result = 0
            if self.logAll:
                print("Sphinx could not understand audio")
        except speech.RequestError as e:
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

    def mainLoop(self):
        try:
            while self.loop:
                self.listen(2)
                res = self.checkActive()
                if res:
                    # записываем основной запрос пользователя
                    self.listen(3, True)
                    self.playLowBeep()

                    time.sleep(0.5)

                    words = self.yandexRecognize()
                    command = CommandChecker.checkForCommand(words.lower())

                    print('команда: ' + command)
                    if (command == "exit"):
                        loop = False
                        self.destroy()

                    elif (command == "game"):
                        self.game.GameLoop()

                    elif (command == "weather"):
                        self.weather.getWeather()

                    elif (command == "radio"):
                        self.radio.listen()

                    elif (command == "radiostop"):
                        self.radio.stop()

                    elif command == "cities":
                        self.citygame.citi_function()

                    elif (command == "anekdot"):
                        try:
                            joke = self.anekdot.getJoke()
                            print(joke)
                            self.say(joke)
                        except:
                            self.say("Что-то я не в настроении шутить")

        except Exception as e:
            print("Глобальная ошибка; {0}".format(e))
            self.play('audio/error.wav')

    # статические функции для использования в других классах
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
    def playmp3(file):
        Jarvis.sysCommand('mpg123  ' + file)

    def say(self, text):
        # print(text)
        self.yandexStuff.createSynthAudio(self.iamToken, text, "tts.wav")
        Jarvis.play("audio/tmp/tts.wav")

    def yandexRecognize(self):
        # speech-to-text от старины Яндекса
        #print('token: ' + self.iamToken);
        recognizedText = self.yandexStuff.recognize(self.iamToken)
        result = recognizedText['result']
        print(result)
        return result


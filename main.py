from JarvisCore import Jarvis
import CommandChecker
from modules import game, weather
from modules.radio import Radio
import time


loop = True
# создаем Джарвиса
jarvis = Jarvis()
radio = Radio()

try:
    while loop:
        jarvis.listen(2)
        res = jarvis.checkActive()
        if res:
            # записываем основной запрос пользователя
            jarvis.listen(3, True)

            jarvis.playLowBeep()
            time.sleep(0.5)
            words = jarvis.yandexRecognize()
            command = CommandChecker.checkForCommand(words)

            if (command == "exit"):
                loop = False
                jarvis.destroy()

            elif (command == "game"):
                game.GameLoop()

            elif (command == "weather"):
                weather.weather()

            elif (command == "radio"):
                radio.listen()

            elif (command == "radiostop"):
                radio.stop()

        """
        command = input(">введите комманду:")
        if command == "/help":
            print("/game играть")
            print("/speak разговаривать")
        elif command == "/game":
            game.GameLoop()
        elif command == "/speak":
            speaker.speaker()
        """
except Exception as e:
    print("Глобальная ошибка; {0}".format(e))
    jarvis.play('audio/error.wav')


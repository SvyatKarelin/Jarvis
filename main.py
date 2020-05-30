from JarvisCore import Jarvis
import CommandChecker
from modules import game, weather, anekdot
from modules.radio import Radio
import time


loop = True
# создаем Джарвиса
jarvis = Jarvis()
radio = Radio()

#joke = anekdot.getJoke()
#jarvis.say(joke)

try:
    while loop:
        jarvis.listen(2)
        res = jarvis.checkActive()
        if res:
            # записываем основной запрос пользователя
            jarvis.listen(3, True)

            jarvis.playLowBeep()
            time.sleep(0.5)
            #print('yandex token:' + jarvis.iamToken)
            words = jarvis.yandexRecognize()
            command = CommandChecker.checkForCommand(words.lower())

            print('команда: ' + command)
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

            elif (command == "anekdot"):
                try:
                    joke = anekdot.getJoke()
                    print(joke)
                    jarvis.say(joke)
                except:
                    jarvis.say("Что-то я не в настроении шутить")

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


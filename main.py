from JarvisCore import Jarvis
import time

loop = True
# создаем Джарвиса
jarvis = Jarvis()

try:
    while loop:
        jarvis.listen(2)
        res = jarvis.checkActive()
        if res == 1:
            jarvis.listen(3, True)
            # записываем основной запрос пользователя
            jarvis.playLowBeep()
            jarvis.yandexRecognize()
        elif res == 2:
            loop = False
            jarvis.destroy()

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


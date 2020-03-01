import speaker
import game
from JarvisCore import Jarvis

# создаем Джарвиса
jarvis = Jarvis()

try:
    while True:
        jarvis.listen(2)
        if jarvis.checkActive():
            jarvis.listen(3, True)
            # записываем основной запрос пользователя
            jarvis.playLowBeep()
            jarvis.yandexRecognize()

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


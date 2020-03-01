import speaker
import game
import Jarvis

# создаем Джарвиса
jarvis = Jarvis()

try:
    while True:
        jarvis.listen()
        if jarvis.checkActive():
            jarvis.listen()

        command = input(">введите комманду:")
        if command == "/help":
            print("/game играть")
            print("/speak разговаривать")
        elif command == "/game":
            game.GameLoop()
        elif command == "/speak":
            speaker.speaker()
except Exception:
    jarvis.say("Ошибка")


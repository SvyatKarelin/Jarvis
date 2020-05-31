import random
import strings
from modules.baseModule import BaseModule

class Game(BaseModule):

    # конструктор
    def __init__(self):
        self.name = strings.game_s1
        super().__init__()

    #self.game_speech_1 = 'game_1.wav'  # Добро пожаловать в игру 'Угадай число'
    #self.game_speech_2 = 'game_2.wav'  # Для выхода из игры используйте команду 'стоп'


    def GameLoop(self):
        count = 8  # todo использовать random
        print(game_s2)
        print(game_s3)
        Jarvis.play("audio/game/game_1.wav")
        g_c = ""
        counter = 0
        while g_c != "/exit":
            g_c = input(game_s4)
            try:
                g_c = int(g_c)

                if count < g_c:
                    print(game_s5)
                elif count > g_c:
                    print(game_s6)
                elif count == g_c:
                    print("Вы угадали c " + str(counter) + " попытки")
                counter += 1
            except:
                if g_c != "/exit":
                    g_c = ""

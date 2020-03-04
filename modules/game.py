import random

# звуковые файлы
from JarvisCore import Jarvis

game_speech_1 = 'game_1.wav'  # Добро пожаловать в игру 'Угадай число'
game_speech_2 = 'game_2.wav'  # Для выхода из игры используйте команду 'стоп'


def GameLoop():
    count = 8  # todo использовать random
    print("Добро пожаловать в игру 'Угадай число'")
    print("Для выхода из игры используйте команду 'exit'")
    Jarvis.play("audio/game/game_1.wav")
    g_c = ""
    counter = 0
    while g_c != "/exit":
        g_c = input("введите число: ")
        try:
            g_c = int(g_c)

            if count < g_c:
                print("Веденное вами число больше загаданного , попробуйте снова")
            elif count > g_c:
                print("Веденное вами число меньше загаданного , попробуйте снова")
            elif count == g_c:
                print("Вы угадали c " + str(counter) + " попытки")
            counter += 1
        except:
            if g_c != "/exit":
                g_c = ""

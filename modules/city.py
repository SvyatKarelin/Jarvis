import random
from modules.baseModule import BaseModule
#import main
from modules import citi_list


class city_game(BaseModule):

    def __init__(self):
        self.name = "city"
        super().__init__()

    def citi_function(self):

        u_chek = []
        print("Добро пожаловать в игру 'города'")
        print("Для выхода из игры используйте комманду 'exit'")
        city = citi_list.cities
        city_str = random.choice(city)
        city.remove(city_str)
        print(city_str)
        u_i = input("")
        if u_i in city:
            city.remove(u_i)
        u_chek.append(u_i)
        #if u_i == "exit":todo сделать
            #main.main_logic()
        one_eliment_u_i = u_i[0]
        g = city_str[len(city_str)-1:]
        if one_eliment_u_i == g:
            self.program_logic(u_i,city,u_chek)
        else:
            print("вы играете нечестно")


    def  program_logic (self,y,o,u_chek):
        c = ""
        format_list = []
        while c != "exit":
            list = []
            last_eliment_u_i =  y[len(y)-1:].capitalize()

            for i in o:
              if i[0] == last_eliment_u_i:
                  list.append(i)

            if len(list) > 0:
                format_list = random.choice(list)
                o.remove(format_list)
                print(format_list)
            elif len(list) == 0:
                print("произошла ошибка ввода попробуйте ввести другое слово")
            list.clear()
            y = input("")
            if y in o:
                o.remove(y)
            if y in u_chek:
                print("вы уже использовали это слово")
                y = input("")
            u_chek.append(y)
            last_eliment_u_c = y[0]
            j =  last_eliment_u_c.split()
            if y != "exit":
                b = "".join(j)
                if format_list != []:
                    if b != format_list[len(format_list) - 1:]:
                        print("вы играете нечестно")
                        c = "exit"
            elif y == "exit":
                c = "exit"

a = city_game()
j = a.citi_function()
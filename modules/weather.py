import requests
from modules.baseModule import BaseModule

class Weather(BaseModule):

    # конструктор
    def __init__(self):
        self.name = "Погода"
        super().__init__()

    def getWeather(self):
        url = 'https://wttr.in/Veliky Novgorod'

        weather_parameters = {
            '0': '',
            #'T': '',
            'M': '',
            '1': ''
        }

        request_headers = {
            'Accept-Language': 'ru'
        }

        # https://wttr.in/Veliky Novgorod?0&T&M
        # ?0                      # только текущая погода
        # ?1                      # погода сегодня + 1 день
        # ?2                      # погода сегодня + 2 дня
        # ?n                      # узкая версия (только день и ночь)
        # ?q                      # тихая версия (без текста "Прогноз погоды")
        # ?Q                      # сверхтихая версия (без "Прогноз погоды", нет названия города)
        # ?T                      # отключить терминальные последовательности (без цветов)

        response = requests.get(url, params=weather_parameters, headers=request_headers)
        print(response.text)

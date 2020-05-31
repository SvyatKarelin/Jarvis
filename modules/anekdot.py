import requests
import json
import baseModule


class Anekdot(BaseModule):

    # конструктор
    def __init__(self):
        self.name = "Анекдоты"
        self.listening = False
        super().__init__(self)

    def getJoke(jokeType = 1):

        # joke types
        # 1 - Анекдот;
        # 2 - Рассказы;
        # 3 - Стишки;
        # 4 - Афоризмы;
        # 5 - Цитаты;
        # 6 - Тосты;
        # 8 - Статусы;

        url = "http://rzhunemogu.ru/RandJSON.aspx?CType={}"
        response = requests.get(url.format(jokeType))

        decode_resp = response.text.encode('UTF-8')
        text = json.loads(decode_resp, strict=False)
        return text['content']
import requests
import json


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

#print(getJoke())
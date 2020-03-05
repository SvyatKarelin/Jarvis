import requests
import json


def getJoke(jokeType = 1):

    url = "http://rzhunemogu.ru/RandJSON.aspx?CType={}"
    response = requests.get(url.format(jokeType))

    decode_resp = response.text.encode('UTF-8')
    text = json.loads(decode_resp, strict=False)
    return text['content']

#print(getJoke())
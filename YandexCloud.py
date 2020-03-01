import json
import requests

class YandexStuff:

    def __init__(self):
        # oauth-токен для доступа к облачным функциям
        self.oauth_token = "AgAAAAAAI7q8AATuwdo1O3xPcEnEgasUoV4yTM4"
        # id каталога Yandex-облака
        self.folderId = "b1gg9qm2acr83gf1lcss"

    def create_token(self):
        params = {'yandexPassportOauthToken': self.oauth_token}
        response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', params=params)
        decode_response = response.content.decode('UTF-8')
        text = json.loads(decode_response)
        iam_token = text.get('iamToken')
        expires_iam_token = text.get('expiresAt')

        return iam_token, expires_iam_token


    def recognize(self, IAM_TOKEN):
        # распознаём речь
        url = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"
        headers = {'Authorization': f'Bearer {IAM_TOKEN}'}

        with open("send.ogg", "rb") as f:
            data_sound = f.read()

        # остальные параметры:
        params = {
            'lang': 'ru-RU',
            'folderId': self.folderId,
            'sampleRateHertz': 48000,
        }

        response = requests.post(url, params=params, headers=headers, data=data_sound)

        # декодируем ответ:
        decode_resp = response.content.decode('UTF-8')
        # и загрузим в json, чтобы получить текст из аудио:
        text = json.loads(decode_resp)

        return text
import os
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


    def recognize(self, iam_token):
        # распознаём речь
        url = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"
        #headers = {'Authorization': f'Bearer {iam_token}'}
        headers = {
            'Authorization': 'Bearer ' + iam_token,
        }

        with open("audio/tmp/send.ogg", "rb") as f:
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

    def synthesize(self, iam_token, text):
        url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
        headers = {
            'Authorization': 'Bearer ' + iam_token,
        }

        data = {
            'text': text,
            'lang': 'ru-RU',
            'voice': 'zahar',
            'folderId': self.folderId,
            'format': 'lpcm',
            'sampleRateHertz': 48000,
        }

        with requests.post(url, headers=headers, data=data, stream=True) as resp:
            if resp.status_code != 200:
                raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

            for chunk in resp.iter_content(chunk_size=None):
                yield chunk

    def createSynthAudio(self, iam_token, text, outFile = ""):
        with open("audio/tmp/synth.raw", "wb") as f:
            for audio_content in self.synthesize(iam_token, text):
                f.write(audio_content)

        output = "speech.wav"
        if outFile != "":
            output = outFile

        # lpcm в wav-формат при помощи SoX-утилиты
        os.system('sox -r 48000 -b 16 -e signed-integer -c 1 audio/tmp/synth.raw audio/tmp/' + output)

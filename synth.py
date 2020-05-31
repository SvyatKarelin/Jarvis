# только для тестов
import argparse
from YandexCloud import YandexStuff

parser = argparse.ArgumentParser()
parser.add_argument("--t")
parser.add_argument("--f")
args = parser.parse_args()

text = args.t
outfile = args.f

yandexStuff = YandexStuff()
iamToken, iamTokenExpires = yandexStuff.create_token()
yandexStuff.createSyntеуhAudio(iamToken, text, outfile)

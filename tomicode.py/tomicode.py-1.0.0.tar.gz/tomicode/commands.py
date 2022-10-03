import random as r
import requests

class random():
    def number(od = int, do = int):
        return r.randint(od, do)
    def meme():
        r = requests.get('https://ivall.pl/memy')
        json_data = r.json()
        image_url = json_data['url']

        return image_url

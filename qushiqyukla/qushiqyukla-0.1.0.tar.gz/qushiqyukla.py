from playsound import playsound
import os
from random import randint
rn = randint(1, 100)
class sound():
    class uz(): 
        def man(text):
            os.system(f'edge-tts -v uz-UZ-SardorNeural -t "{text}" --write-media "{rn}.mp3"')
            playsound(f"{rn}.mp3")
            os.remove(f"{rn}.mp3")
        def woman(text):
            os.system(f'edge-tts -v uz-UZ-MadinaNeural -t "{text}" --write-media "{rn}.mp3"')
            playsound(f"{rn}.mp3")
            os.remove(f"{rn}.mp3")
    class en():
        def man(text):
            os.system(f'edge-tts -v en-EN-AriaNeural -t "{text}" --write-media "{rn}.mp3"')
            playsound(f"{rn}.mp3")
            os.remove(f"{rn}.mp3")
        def woman(text):
            os.system(f'edge-tts -v en-EN-AriaNeural -t "{text}" --write-media "{rn}.mp3"')
            playsound(f"{rn}.mp3")
            os.remove(f"{rn}.mp3")
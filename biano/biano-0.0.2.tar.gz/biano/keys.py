#coding=utf-8

import pynput
from pynput.keyboard import Listener, Key
from biano import sound
s = "qwertyuiop[]"+"asdfghjkl;"+"zxcvbnm,."
maps = {k:i+40 for k,i in zip(s, range(len(s)))}

arr = []
pressed = set()
def press(key):
    if hasattr(key, "char") and key.char in maps:
        vc = maps[key.char]
        if vc in pressed:
            return
        pressed.add(vc)
        sound.sd.play(vc)
    global lst
    if key == Key.esc:
        lst.stop()
        sound.sd.close()
        sound.release()

pass

def release(key):
    if hasattr(key, "char") and key.char in maps:
        vc = maps[key.char]
        if vc in pressed:
            pressed.remove(vc)

pass
lst = None
def run():
    global lst
    print("press esc to exit")
    with Listener(on_press=press, on_release=release) as lst:
        lst.join()

pass
if __name__=="__main__":
    run()

pass
"""
python keys.py
"""
#coding=utf-8

import pyaudio
import numpy as np
import math
fps = 4096
p = pyaudio.PyAudio()

# stream = p.open(format=p.get_format_from_width(1),
#                 channels=1,
#                 rate=fps,
#                 output=True)
# pass

def f(rate, sec = 1.0):
    #print("f:"+str(rate))
    global fps
    size = int(fps * sec)
    data = np.zeros(size, dtype = np.uint8)
    for i in range(size):
        x = i*2*math.pi*rate/fps
        y = math.sin(x)*128
        y = y * (size-i)/size
        y += 128
        y = min(255, y)
        data[i] = y
    return bytes(list(data))

pass

class CacheFc:
    def __init__(self):
        self.cache = {}
    def __call__(self, rate):
        if rate not in self.cache:
            self.cache[rate] = f(rate, 1.0)
        return self.cache[rate]

pass
def create():
    return p.open(format=p.get_format_from_width(1), channels=1, rate=fps, output=True)

pass

def close(stream):
    stream.stop_stream()
    stream.close()

pass
import threading

def fn(n):
    return 27.5*(2**(1/12))**(n-1)

pass

class Sound:
    def __init__(self):
        self.fc = CacheFc()
        self.frees = [create() for i in range(20)]
        self.index = 0
        self.lock = threading.Lock()
    def _play(self, data, id):
        self.frees[id].write(data)
    def play(self, rate):
        rate = fn(rate)
        data = self.fc(rate)
        with self.lock:
            id = self.index
            self.index = (self.index+1)%20
        th = threading.Thread(target = self._play, args =(data, id))
        th.setDaemon(True)
        th.start()
    def close(self):
        for st in self.frees:
            close(st)

pass
sd = Sound()
def release():
    p.terminate()

pass

import datetime
import random
import time

# import RPi.GPIO as GPIO

GPIO_signal = True

def get_signal():
    global GPIO_signal
    r_num = random.random()
    if r_num > .7:
        return not GPIO_signal
    return GPIO_signal

def record():
    with open("water_recordings.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S:%f')}\n")

if __name__ == "__main__":
    f = open("water_recordings.txt", "w")
    f.close()
    try:
        while True:
            if GPIO_signal != get_signal():
                GPIO_signal = not GPIO_signal
                record()
            time.sleep(1)
    except KeyboardInterrupt:
        exit()
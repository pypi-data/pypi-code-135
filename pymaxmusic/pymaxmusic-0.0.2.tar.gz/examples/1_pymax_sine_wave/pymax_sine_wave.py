#
# pymax_sine_wave.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_sine_wave.maxpat"

import math

def sine_wave():
    ontime_in_ms = 0
    while True:
        yield [ontime_in_ms, ontime_in_ms, math.sin(2 * math.pi * ontime_in_ms/1000)]
        ontime_in_ms += 12


if __name__ == "__main__":

    from pymaxmusic import pymax

    pymax.open_pymax()
    pymax.add_generator("sine_wave", sine_wave)
    pymax.run_pymax()


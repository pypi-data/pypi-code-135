#
# pymax_stochastic_texture.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_stochastic_texture.maxpat"

import numpy as np

# HELPER FUNCTIONS -----------------------------------------------------------

def find_closest_in_list(keyValue, values):
  diffs = [abs(keyValue - value) for value in values]
  return values[diffs.index(min(diffs))]

def make_pitch_field(pitchClasses):
  return [12 * octave + pc for octave in range(11) for pc in pitchClasses]

def linear_map(value, source_range : list, target_range : list):
  x = value
  x_min = source_range[0]
  x_max = source_range[1]
  y_min = target_range[0]
  y_max = target_range[1]
  return ((y_max - y_min)/(x_max - x_min)) * (x - x_min) + y_min


# PYMAX OBJECT AND GENERATOR ------------------------------------------------

class StochasticTexture():
    def __init__(self):

        self.pitch_field = []

        self.iotime_mean = 1
        self.iotime_std = 1

        self.duration_mean = 1
        self.duration_std = 1

        self.pitch_mean = 60
        self.pitch_std = 0

        self.volume_mean = 60
        self.volume_std = 0

        self.ontime = 0
        self.channel = 1

    def set_pitch_field(self, *pitch_classes):
        self.pitch_field = make_pitch_field(pitch_classes)

    def set_iotime(self, mean, std):
        self.iotime_mean = linear_map(mean, [0,127], [-4, 2])
        self.iotime_std = linear_map(std, [0,127], [0, 1.33])

    def set_duration(self, mean, std):
        self.duration_mean = linear_map(mean, [0,127], [-4, 2])
        self.duration_std = linear_map(std, [0,127], [0, 1.33])

    def set_pitch(self, mean, std):
        self.pitch_mean = linear_map(mean, [0,127], [57, 72])
        self.pitch_std = linear_map(std, [0, 127], [0, 12])

    def set_volume(self, mean, std):
        self.volume_mean = linear_map(mean, [0,127], [12, 115])
        self.volume_std = linear_map(std, [0,127], [0, 4])

    def get_duration(self):
        return 2**np.random.normal(self.duration_mean, self.duration_std)

    def get_pitch(self):
        pitch = int(np.random.normal(self.pitch_mean, self.pitch_std))
        pitch = find_closest_in_list(pitch, self.pitch_field)
        return pitch

    def get_volume(self):
        return int(np.random.normal(self.volume_mean, self.volume_std))


def texture_generator(texture : StochasticTexture):
    ontime = 0
    while True:
        yield [ontime, texture.get_pitch(), texture.get_volume(), texture.get_duration(), 1]
        iotime = 2**np.random.normal(texture.iotime_mean, texture.iotime_std)
        ontime += iotime

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    from pymaxmusic import pymax
    pymax.open_pymax()
    pymax.add_class("texture", StochasticTexture)
    pymax.add_generator("texture_gen", texture_generator, "texture")
    pymax.run_pymax()
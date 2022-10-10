#
# pymax_order_to_randomness.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_order_to_randomness.maxpat"

import numpy as np

# HELPER FUNCTIONS --------------------------------------------------

def markov_step(current, choices, matrix):
    try:
        row_index = choices.index(current)
        weights   = matrix[row_index]
        step      = random_weighted_choice(choices, weights)
        return step
    except ValueError:
        return


def random_weighted_choice(choices, weights):

  prob        = np.random.random()
  weight_sum  = sum([weight for weight in weights])

  if weight_sum != 1.0:
    normalized_weights = [weight/weight_sum for weight in weights]
  else:
    normalized_weights = weights

  partial_sum = 0
  for (choice, weight) in zip(choices, normalized_weights):
    partial_sum += weight
    if prob < partial_sum:
      return choice

  return None


def linear_map(value, source_range : list, target_range : list):
  x = value
  x_min = source_range[0]
  x_max = source_range[1]
  y_min = target_range[0]
  y_max = target_range[1]
  return ((y_max - y_min)/(x_max - x_min)) * (x - x_min) + y_min


# PYMAX OBJECTS ----------------------------------------------------------------

class Melody(object):

    def __init__(self):

        self.octave             = 4
        self.velocity_mean      = 60
        self.velocity_std       = 10
        self.iotime_mean        = 1.0
        self.iotime_std         = 0.5
        self.duration_mean      = 4.0
        self.duration_std       = 1.0
        self.melodic_randomness = 0.0

        self.melody_notes = {
                'c1' : 0,
                'e1' : 4,
                'g1' : 7,
                'c2' : 12,
                'e2' : 16,
                            }

        self.states = ['c1', 'e1', 'g1', 'c2', 'e2']

        self.state_matrix = [[0.0, 1.0, 0.0, 0.0, 0.0], 
                             [0.0, 0.0, 1.0, 0.0, 0.0], 
                             [0.0, 0.0, 0.0, 1.0, 0.0], 
                             [0.0, 0.0, 0.0, 0.0, 1.0], 
                             [1.0, 0.0, 0.0, 0.0, 0.0]]

        self.state = 'c1'
        self.ontime = 0


    def set_octave(self, octave : int):
        self.octave = octave


    def set_velocity_mean(self, mean):
        self.velocity_mean = linear_map(mean, [0,127], [12, 115])


    def set_velocity_std(self, std):
        self.velocity_std = linear_map(std, [0,127], [0, 4])


    def set_iotime_mean(self, mean):
        self.iotime_mean = linear_map(mean, [0,127], [-4, 2])


    def set_iotime_std(self, std):
        self.iotime_std = linear_map(std, [0,127], [0, 1.33])


    def set_duration_mean(self, mean):
        self.duration_mean = linear_map(mean, [0, 127], [0.5, 4.0])


    def set_duration_mean(self, mean):
        self.duration_std = linear_map(mean, [0, 127], [0.5, 4.0])


    def set_melodic_randomness(self, melodic_randomness):
        n = len(self.state_matrix)
        r = linear_map(melodic_randomness, [0, 127], [0.0, 1.0]) / n
        self.state_matrix = [[1.0 - (n - 1 ) * r if i == (j + 1) % n else r for i in range(n)] for j in range(n)]


    def get_pitch(self):
       return self.melody_notes[self.state] + 12 * self.octave


    def get_velocity(self):
       return int(np.random.normal(self.velocity_mean, self.velocity_std))


    def get_duration(self):
       return 2**np.random.normal(self.duration_mean, self.duration_std)


    def get_iotime(self):
       return 2**np.random.normal(self.iotime_mean, self.iotime_std)


    def advance(self):
        self.state = markov_step(self.state, self.states, self.state_matrix)



def melody_generator(melody : Melody):
    ontime = 0
    while True:
        pitch       = melody.get_pitch()
        velocity    = melody.get_velocity()
        duration    = melody.get_duration()
        yield [ontime, pitch, velocity, duration, 1]

        melody.advance()           
        ontime += melody.get_iotime()


# ----------------------------------------------------------------------

if __name__ == "__main__":

    from pymaxmusic import pymax

    pymax.open_pymax()
    pymax.add_class("m1", Melody)
    pymax.add_class("m2", Melody)
    pymax.add_class("m3", Melody)
    pymax.add_class("m4", Melody)
    
    pymax.add_generator("gen1", melody_generator, "m1")
    pymax.add_generator("gen2", melody_generator, "m2")
    pymax.add_generator("gen3", melody_generator, "m3")
    pymax.add_generator("gen4", melody_generator, "m4")

    pymax.run_pymax()

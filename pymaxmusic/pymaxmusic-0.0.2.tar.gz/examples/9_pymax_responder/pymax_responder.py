#
# pymax_responder.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_responder.maxpat"

import numpy as np

# HELPER FUNCTIONS -------------------------

def make_markov_transition_matrix(random_walk : list):

  choices  = list(set(random_walk))
  matrix  = [[0 for choice in choices] for choice in choices]

  for i, step in enumerate(random_walk[1:]):
    prev  = random_walk[i]
    i     = choices.index(prev)
    j     = choices.index(step)
    matrix[i][j] += 1

  for i in range(len(matrix)):
    row = matrix[i]
    row_sum = sum(row)
    if row_sum == 0.0:
      row[i] = 1.0
    else:
      for j in range(len(row)):
        row[j] /= row_sum

  return (choices, matrix)


# MAKE MARKOV STEP --------------------------------------

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




# PYMAX OBJECTS ---------------------------------------------------------

class Analyzer():

    def __init__(self):

        self.first_note      = True
        self.has_input      = False
        self.last_ontime    = 0

        self.pitch_chain    = []
        self.pitches        = []
        self.pitch_matrix   = []

        self.iotime_chain   = []
        self.iotime_min     = 0
        self.iotime_mean    = 0
        self.iotime_std     = 0

        self.velocity_chain = []
        self.velocity_mean  = 0
        self.velocity_std   = 0


    def input_note(self, pitch, velocity, ontime_in_ticks):
        def ticks_to_beats(ticks):
            return ticks / 480
        self.pitch_chain.append(pitch)
        self.velocity_chain.append(velocity)
        # iotime - only if an event has already occurred before this event:
        ontime_in_beats = ticks_to_beats(ontime_in_ticks)
        if not self.first_note:
            self.iotime_chain.append(ontime_in_beats - self.last_ontime)
        self.last_ontime = ontime_in_beats
        self.first_note = False
        self.has_input = True


    def analyze_input(self):
        def get_list_statistics(l : list):
            mean        = sum(l) / len(l)
            variance    = sum([((x - mean) ** 2) for x in l]) / len(l)
            std         = variance ** 0.5
            return (mean, std)
        self.iotime_min                         = min(self.iotime_chain)
        self.iotime_mean, self.iotime_std       = get_list_statistics(self.iotime_chain)
        self.velocity_mean, self.velocity_std   = get_list_statistics(self.velocity_chain)
        self.pitches, self.pitch_matrix         = make_markov_transition_matrix(self.pitch_chain)
        self.iotime_chain                       = []
        self.velocity_chain                     = []
        self.pitch_chain                        = []
        self.first_note                          = True



def responder(analyzer : Analyzer):

    ontime  = 0
    pitch   = np.random.choice(analyzer.pitches)
    channel = 1

    while True:
        if analyzer.has_input:

            velocity    = np.random.normal(analyzer.velocity_mean, analyzer.velocity_std)
            iotime      = np.random.normal(analyzer.iotime_mean, analyzer.iotime_std) 

            yield [ontime, pitch, velocity, iotime, channel]

            ontime  += iotime
            pitch   = markov_step(pitch, analyzer.pitches, analyzer.pitch_matrix)
            if not pitch:
                pitch = np.random.choice(analyzer.pitches)



# --------------------------------------------------------------------------------

if __name__ == "__main__":
    from pymaxmusic import pymax
    pymax.open_pymax()
    pymax.add_class("analyzer", Analyzer)
    pymax.add_generator('responder', responder, "analyzer")
    pymax.run_pymax()

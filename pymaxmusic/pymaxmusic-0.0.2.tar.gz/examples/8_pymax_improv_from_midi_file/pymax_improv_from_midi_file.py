#
# pymax_improv_from_midi_file.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_improv_from_midi_file.maxpat"



import mido # download from https://github.com/mido/mido
import numpy as np
from random import choice

# HELPER FUNCTIONS FOR MARKOV CHAINS AND FOR CONVERTING MIDI TO NOTES:

def midi_file_to_notes(midi_file_name : str):
    mid = mido.MidiFile(midi_file_name)
    tracks = []
    for i, track in enumerate(mid.tracks):
        notes = []
        ontime = 0
        for msg in track:
            if msg.type == 'note_on':
                iotime = msg.time / 480
                ontime += iotime
                note = [ontime, msg.note, iotime, msg.velocity, msg.channel + 1]
                notes.append(note)
        tracks.append(notes)
    return tracks


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


def find_closest_in_list(keyValue, values):
  diffs = [abs(keyValue - value) for value in values]
  return values[diffs.index(min(diffs))]
  
def make_pitch_field(pitchClasses):
  return [12 * octave + pc for octave in range(11) for pc in pitchClasses]


# PYMAX OBJECT AND GENERATOR ---------------------------------------------------------

class MarkovPitchContour():

    def __init__(self):
        self.pitch_diff_choices = [] 
        self.pitch_diff_matrix  = []

    def load_midi_file(self, midi_file_name : str, track_number = 0):
        notes                       = midi_file_to_notes(midi_file_name)[track_number]
        pitch_chain                 = [note[1] for note in notes]
        pitch_diff_chain            = [pitch_chain[i] - pitch_chain[i-1] for i in range(1, len(pitch_chain))]
        markov_info                 = make_markov_transition_matrix(pitch_diff_chain)
        self.pitch_diff_choices     = markov_info[0]
        self.pitch_diff_matrix      = markov_info[1]
        self.midi_file              = midi_file_name
        self.track_number           = track_number
        print("MIDI file " + midi_file_name + " , track " + str(track_number) + " loaded.")
        return self.midi_file

    def step(self, pitch_diff):
        return markov_step(pitch_diff, self.pitch_diff_choices, self.pitch_diff_matrix)


class PitchField():
    def __init__(self):
        self.pitches = []

    def find_closest(self, pitch):
        return find_closest_in_list(pitch, self.pitches)

    def set_field(self, *pitch_classes):
        self.pitches = make_pitch_field(pitch_classes)


def improviser(contour : MarkovPitchContour, field : PitchField):
    swing_counter   = 0
    ontime          = 0
    pitch           = field.find_closest(72)
    pitch_diff      = choice(contour.pitch_diff_choices)
    while True:
        yield [ontime, pitch, 100, .5, 1]
        ontime        += (.6 if swing_counter else .4)
        swing_counter = (swing_counter + 1) % 2
        pitch_diff    = contour.step(pitch_diff)
        pitch         = field.find_closest(pitch + pitch_diff)
        while pitch > 108:
            pitch -= 12
        while pitch < 24:
            pitch += 12


#----------------------------------------------------------------------------

if __name__ == "__main__":

    from pymaxmusic import pymax
    
    contour     = MarkovPitchContour()
    pitch_field = PitchField()

    pymax.open_pymax()
    pymax.add_object("midi_loader", contour)
    pymax.add_object("pitch_field", pitch_field)
    pymax.add_generator("improviser", improviser, "midi_loader", "pitch_field")
    pymax.run_pymax()
#
# pymax_arpeggiator.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_arpeggiator.maxpat"


# HELPER FUNCTIONS -------------------------------------------------------------

def find_closest_in_list(target, values):
  diffs = [abs(target - value) for value in values]
  return values[diffs.index(min(diffs))]
  
def make_pitch_field(pitch_classes):
  return [12 * octave + pc for octave in range(11) for pc in pitch_classes]




# PYMAX OBJECTS AND GENERATORS -------------------------------------------------

class Arpeggio():

    def __init__(self):
        self.pitch_field    = make_pitch_field([0, 4, 7])
        self.contour        = [0, 4, 7, 12, 16, 12, 7, 4]
        self.step           = .25
        self.start_pitch    = 60
        self.duration       = .25
        self.volume         = 100

    def set_pitch_field(self, *pitch_classes):
        self.pitch_field = make_pitch_field(pitch_classes)

    def get_pitch(self, index):
        pitch_class     = self.contour[index]
        pitch           = pitch_class + self.start_pitch
        closest_pitch   = find_closest_in_list(pitch, self.pitch_field)
        return closest_pitch

# ARPEGGIATOR GENERATOR

def arpeggiator(arp):

    ontime   = 0
    i        = 0

    while True:
        yield [ontime, arp.get_pitch(i), arp.volume, arp.duration, 1]
        ontime  += arp.step
        i       = (i + 1) % len(arp.contour)


# ------------------------------------------------------------------------------

if __name__ == "__main__":

    from pymaxmusic import pymax

    arp = Arpeggio()

    pymax.open_pymax()
    pymax.add_object("arp", arp)
    pymax.add_generator("arp_gen", arpeggiator, "arp")
    pymax.run_pymax()
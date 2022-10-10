#
# pymax_melody.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_melody.maxpat"


class Melody():
    def __init__(self, pitch_classes, ontimes, total_duration):

        self.pitch_classes      = pitch_classes
        self.ontimes            = ontimes
        self.total_duration     = total_duration

        self.speed          = 1
        self.note_duration  = 1
        self.tonic          = 0
        self.octave         = 4
        self.volume         = 60

        self.loop           = False

    def get_pitch(self, i):
        return self.pitch_classes[i] + self.tonic + 12 * self.octave

    def get_ontime(self, i):
        if i == self.get_length():
            return self.total_duration * self.speed
        else:
            return self.ontimes[i] * self.speed
        
    def get_length(self):
        return len(self.pitch_classes)

    def reverse(self):
        time_to_last_ontime = sum(self.interonset_times)
        self.interonset_times.reverse()
        self.interonset_times[0] = self.total_duration - time_to_last_ontime
        self.pitch_classes.reverse()


def melody_generator(melody):

    ontime = 0
    i = 0
    time_to_next_note = melody.get_ontime(i)

    while i < melody.get_length():

        ontime += time_to_next_note
        pitch = melody.get_pitch(i)

        yield [ontime, pitch, melody.volume, melody.note_duration, 1]

        i += 1
        time_to_next_note = melody.get_ontime(i) - melody.get_ontime(i-1)

        if melody.loop and i == melody.get_length():
            i = 0


# ------------------------------------------------------------------------------

if __name__ == "__main__":

    from pymaxmusic import pymax

    melody = Melody(    [0,   7,   8,   5,   7,   3,   2,   3,   5],
                        [0.0, 1.0, 2.0, 3.0, 4.0, 4.5, 5.0, 5.5, 6.0], 
                        8.0
                    )

    pymax.open_pymax()
    pymax.add_object("melody", melody)
    pymax.add_generator("gen", melody_generator, "melody")
    pymax.run_pymax()

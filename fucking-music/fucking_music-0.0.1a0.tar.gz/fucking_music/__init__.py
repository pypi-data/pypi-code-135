nBase = {
    #   C   C#  D   D#  E   F   F#  G   G#  A   A#  B
    #   0   1   2   3   4   5   6   7   8   9   10  11

    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11
}

intNameBase = {
    'ч.1': 0,
    'м.2': 1,
    'б.2': 2,
    'м.3': 3,
    'б.3': 4,
    'ч.4': 5,
    'тритон': 6,
    'ч.5': 7,
    'м.6': 8,
    'б.6': 9,
    'м.7': 10,
    'б.7': 11,
    'ч.8': 12,
    'м.9': 13,
    'б.9': 14,
    'м.10': 15,
    'б.10': 16,
    'ч.11': 17,
    'ув.11': 18,
    'ум.12': 18,
    'ч.12': 19,
    'м.13': 20,
    'б.13': 21,
    'м.14': 22,
    'б.14': 23,
    'ч.15': 24
}

accIntervalBase = {
    'major': [2, 2, 1, 2, 2, 2],
    'minor': [2, 1, 2, 2, 1, 2]
}


def isInTheRange(var, rangeBase):
    """
    Возвращает True или False в зависимости от того, входит ли var в
    rangeBase = {'min': min_val, 'max': max_val}
    :param var:
    :param rangeBase:
    :return:
    """
    return rangeBase['min'] <= var <= rangeBase['max']


class Note:
    #           C#3
    # {
    #     'name': 'C#3',
    #     'alt': '#',
    #     'octave_position': '2',
    #     'octave': '3'
    # }

    errorBase = {
        'inputError': 'В названии ноты допущена ошибка',
        'octaveRangeError': 'Нота находится за пределами пианино',
        'addError': 'Ошибка в добавлении ноты'
    }

    octaveRange = {
        'min': 0,
        'max': 8
    }

    def __init__(self, name: str):
        self.name = name
        self.alt = None
        self.octave_position = None
        self.__octave = None

        characters = len(name)

        if characters == 0 or not name[0].upper() in nBase:
            raise ValueError(Note.errorBase['inputError'])

        if characters == 1:
            pass
        elif characters == 2:
            if name[1] == 'b' or name[1] == '#':
                self.alt = name[1]
            else:
                try:
                    self.__octave = int(name[1])
                except ValueError:
                    raise ValueError(Note.errorBase['inputError'])
        elif characters == 3:
            if name[1] == 'b' or name[1] == '#':
                self.alt = name[1]
            else:
                raise ValueError(Note.errorBase['inputError'])
            try:
                self.__octave = int(name[2])
            except ValueError:
                raise ValueError(Note.errorBase['inputError'])
        else:
            raise ValueError(Note.errorBase['inputError'])

        self.__alteration()

        if isinstance(self.octave, int) and isinstance(self.octave_position, int):
            self.global_position = self.octave * 12 + self.octave_position
        else:
            self.global_position = None

    def __abs__(self):
        return self.global_position

    def __add__(self, other):
        if isinstance(other, int):
            octave_position = (self.octave_position + other) % 12
            if isinstance(self.octave, int):
                octave = self.octave + (self.octave_position + other) // 12
                if not isInTheRange(octave, Note.octaveRange):
                    raise ValueError(Note.errorBase['octaveRangeError'])
            else:
                octave = ''
            for name in nBase:
                if nBase[name] == octave_position:
                    return Note(name + str(octave))
            for name in nBase:
                if other > 0 and nBase[name] == octave_position - 1:
                    return Note(name + '#' + str(octave))
                elif other < 0 and nBase[name] == octave_position + 1:
                    return Note(name + 'b' + str(octave))
        elif isinstance(other, Note):
            return Interval(self, other)
        else:
            raise TypeError("Вы вели не количество полутонов!")

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.octave_position == other.octave_position

    def __repr__(self):
        return self.name

    def __sub__(self, other):
        return self + (-other)

    def __alteration(self):
        self.octave_position = nBase[self.name[0]]
        if self.alt:
            if self.alt == 'b':
                octave_position = (self.octave_position - 1) % 12
                if isinstance(self.octave, int):
                    self.octave = self.octave + (self.octave_position - 1) // 12
            else:
                octave_position = (self.octave_position + 1) % 12
                if isinstance(self.octave, int):
                    self.octave = self.octave + (self.octave_position + 1) // 12
            self.octave_position = octave_position
        for name in nBase:
            if nBase[name] == self.octave_position:
                self.name = name if not isinstance(self.octave, int) else name + str(self.octave)
                self.alt = None
                break

    def changeAlt(self, newAlt):
        if newAlt == self.alt or self.alt is None:
            pass
        elif newAlt == '#':
            for name in nBase:
                if nBase[name] == self.octave_position - 1:
                    self.alt = '#'
                    if isinstance(self.octave, int):
                        self.name = name + '#' + str(self.octave)
                    else:
                        self.name = name + '#'
                    break
        elif newAlt == 'b':
            for name in nBase:
                if nBase[name] == self.octave_position + 1:
                    self.alt = 'b'
                    if isinstance(self.octave, int):
                        self.name = name + 'b' + str(self.octave)
                    else:
                        self.name = name + 'b'
                    break
        else:
            raise ValueError

    @property
    def octave(self):
        return self.__octave

    @octave.setter
    def octave(self, value):
        if value is None or isInTheRange(value, Note.octaveRange):
            self.__octave = value
        else:
            raise ValueError(Note.errorBase['octaveRangeError'])


class Accord:
    """
    Create a new Accord object from the given objects.
    """

    def __init__(self, *args):
        self.buffer = None      # C#m               F                   Gb7                 A#maj7
        self.mood = None        # minor             major               major               maj7
        self.notes = None       # [C#, E, G#]       [F, A, C]           [F#, A#, C#, E]     [A#, D, F, A]
        self.tonic = None       # C#                F                   Gb                  A#
        self.type = None        # None              None                None                None

        if len(args) == 1:

            if isinstance(args[0], str):
                self.buffer = args[0]
            else:
                raise ValueError

            if self.buffer[0] not in nBase:
                raise ValueError

            if len(self.buffer) > 1:
                if self.buffer[1] == 'b' or self.buffer[1] == '#':
                    self.tonic = Note(self.buffer[0:2])
                    self.buffer = self.buffer[2:]
                else:
                    self.tonic = Note(self.buffer[0])
                    self.buffer = self.buffer[1:]
            else:
                self.tonic = Note(self.buffer[0])
                self.buffer = self.buffer[1:]

            if self.buffer == '':
                ton = Tonality(self.tonic, 'major').degree
                self.mood = 'major'
                self.notes = [ton[0], ton[2], ton[4]]
            elif self.buffer == 'm':
                ton = Tonality(self.tonic, 'minor').degree
                self.mood = 'minor'
                self.notes = [ton[0], ton[2], ton[4]]
            elif self.buffer == 'maj7':
                ton = Tonality(self.tonic, 'major').degree
                self.mood = 'maj7'
                self.notes = [ton[0], ton[2], ton[4], ton[0] + intNameBase['б.7']]
            elif self.buffer == '7':
                ton = Tonality(self.tonic, 'major').degree
                self.mood = '7'
                self.notes = [ton[0], ton[2], ton[4], ton[0] + intNameBase['м.7']]
            elif self.buffer == 'dim':
                self.mood = 'dim'
                self.notes = [self.tonic, self.tonic + intNameBase['м.3'], self.tonic + intNameBase['тритон']]

        elif len(args) != 0:
            pass
        else:
            raise ValueError

    def changeAlt(self, newAlt):
        if newAlt == self.tonic.alt:
            pass
        elif newAlt == '#':
            self.tonic.changeAlt('#')
            for note in self.notes:
                note.changeAlt('#')
        elif newAlt == 'b':
            self.tonic.changeAlt('b')
            for note in self.notes:
                note.changeAlt('b')
        else:
            raise ValueError

    def __add__(self, other):
        return Accord(str(self.tonic + other) + self.buffer)

    def __eq__(self, other):
        if isinstance(other, Accord):
            return self.tonic == other.tonic and self.mood == other.mood

    def __sub__(self, other):
        return self + (-other)

    def __repr__(self):
        if self.mood == 'major':
            mood = ''
        elif self.mood == 'minor':
            mood = 'm'
        else:
            mood = self.mood
        return f'{str(self.tonic)}{mood}'


class Tonality:

    def __init__(self, tonic, harmony='major'):

        self.alt = '#'

        if isinstance(tonic, Accord):
            self.type = 'Accord'
            self.tonic = tonic
            self.__Accord(tonic)
            return

        if not isinstance(tonic, Note):
            try:
                self.tonic = Note(tonic)
            except Exception:
                raise ValueError
        else:
            self.tonic = tonic

        self.type = 'Note'
        self.tonic.changeAlt('#')
        self.degree = [self.tonic]

        if not isinstance(harmony, str):
            raise ValueError

        if harmony in accIntervalBase:
            self.harmony = harmony
            for i in range(6):
                self.degree.append(self.degree[-1] + accIntervalBase[harmony][i])
        else:
            raise ValueError

    def __repr__(self):
        return str(self.degree)

    def __Accord(self, tonicAcc):
        tonicAcc.changeAlt('#')
        self.tonic = tonicAcc
        self.degree = [self.tonic]
        self.harmony = self.tonic.mood
        if self.harmony == 'major':
            x = ['m', 'm', '', '', 'm', 'dim']
        else:
            x = ['dim', '', 'm', 'm', '', '']

        for i in range(6):
            self.degree.append(Accord(str(self.degree[-1].tonic + accIntervalBase[self.harmony][i]) + x[i]))

    def changeAlt(self, newAlt):
        if newAlt == self.alt:
            pass
        elif newAlt == '#':
            self.alt = '#'
            for obj in self.degree:
                obj.changeAlt('#')
        elif newAlt == 'b':
            self.alt = 'b'
            for obj in self.degree:
                obj.changeAlt('b')
        else:
            raise ValueError

    def __add__(self, other):
        if self.type == 'Accord' and isinstance(other, int):
            return Tonality(self.tonic + other)
        if not isinstance(other, int):
            raise ValueError
        return Tonality(self.tonic + other, self.harmony)

    def __sub__(self, other):
        return self + (-other)


class Interval:

    def __init__(self, note1: Note, note2: Note):
        self.note1 = note1
        self.note2 = note2
        self.name = None
        if note1.octave is None and note2.octave is None:
            self.length = abs(note2.octave_position - note1.octave_position)
        else:
            self.length = abs(note2.global_position - note1.global_position)
        for name in intNameBase:
            if intNameBase[name] == self.length:
                self.name = name

    def __repr__(self):
        return f'[{self.note1}, {self.note2}] — {self.name}'


def searchTonic(*args: Accord):
    base = []
    tonic = Accord('C')
    for i in range(12):
        flag = 1
        for arg in args:
            if arg in Tonality(tonic + i).degree:
                flag = flag * 1
            else:
                flag = flag * 0
        if flag == 1:
            base.append(Tonality(tonic + i).degree)
    return base



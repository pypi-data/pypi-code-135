class DotString(str):

    """ dot string   -- [ex]: 'hello new world' -->  'hello.new.world """

    locations = []

    def __init__(self, string):
        super().__init__()
        self._string_ = str(string)
        self = self._dotted()


    def _dotted(self):

        """ removes spaces and replaces them with dots """

        if isinstance(self._string_, str):
            ret = []
            for index, ch in enumerate(self._string_):
                if ch == ' ':
                    self.locations.append(int(index))
                    ret.append('.')
                else:
                    ret.append(ch)
            retstr = "".join(ret)
            return ret

    def original(self):

        """ turns the str back to spaced by memory """

        if isinstance(self._string_, str):
            for index, ch in enumerate(self._string_):
                pos = int(index)
                if pos in self.locations:
                    self._string_.replace(self._string_[pos], ' ')
            return self._string_


dstr = DotString


def example():
    print("normal string:", "'hello new world'")
    print("dstr:         ", "'hello.new.world'")
    print('[usage]')
    print("\033[32mdstr\033[0m\033[34m(\033[0m'\033[31mhello new world\033[0m'\033[34m)\033[0m")



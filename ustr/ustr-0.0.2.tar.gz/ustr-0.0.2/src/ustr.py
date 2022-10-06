
class UnderlineString(str):

    """ underlined string   -- [ex]: 'hello new world' -->  'hello_new_world """

    locations = []

    def __init__(self, string) -> None:
        super().__init__()
        self._string_ = string
        self = self._underlined()


    def _underlined(self):

        """ removes the spaces and puts underscore """

        if isinstance(self._string_, str):
            ret = []
            for index, ch in enumerate(self._string_):
                if ch == ' ':
                    self.locations.append(int(index))
                    ret.append('_')
                else:
                    ret.append(ch)
            retstr = "".join(ret)
            return ret

    def original(self):

        """ reverses the underlining and returns the string """

        if isinstance(self._string_, str):
            for index, ch in enumerate(self._string_):
                pos = int(index)
                if pos in self.locations:
                    self._string_.replace(self._string_[pos], ' ')
            return self._string_

ustr = UnderlineString


def example():
    print("normal string:", "'hello new world'")
    print("ustr:         ", "'hello_new_world'")
    print('[usage]')
    print("\033[32mustr\033[0m\033[34m(\033[0m'\033[31mhello new world\033[0m'\033[34m)\033[0m")


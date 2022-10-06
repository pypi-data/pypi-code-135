class HyphenString(str):

    locations = []

    def __init__(self, string):
        super().__init__()
        self._string_ = string
        self = self._hypenated()


    def _hypenated(self):

        """ removes spaces and replaces them with - """

        if isinstance(self._string_, str):
            ret = []
            for index, ch in enumerate(self._string_):
                if ch == ' ':
                    self.locations.append(int(index))
                    ret.append('-')
                else:
                    ret.append(ch)
            retstr = "".join(ret)
            return ret

    def original(self):

        """ turns the str back to spaced string by memory """

        if isinstance(self._string_, str):
            for index, ch in enumerate(self._string_):
                pos = int(index)
                if pos in self.locations:
                    self._string_.replace(self._string_[pos], ' ')
            return self._string_


hstr = HyphenString
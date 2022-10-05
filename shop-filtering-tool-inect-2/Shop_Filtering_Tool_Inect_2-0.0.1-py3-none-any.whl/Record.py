try:
    import Parsers
except ModuleNotFoundError:
    import shop.Parsers as Parsers


class Record(dict):
    def __init__(self):
        super().__init__(self)
        self.parsed = {}

    def __eq__(self, other):
        if not isinstance(other, Record):
            return False
        return self.parsed == other.parsed

    @staticmethod
    def from_dict(d, parser=Parsers.default_parser):
        self = Record()
        for key in d:
            if d[key] is not None:
                self[key] = str(d[key])
                self.parsed[key] = parser(str(d[key]))
        return self


def test():
    a = Record.from_dict({1: 'l l'}, Parsers.remove_spaces)
    c = Record.from_dict({1: 'll'}, Parsers.default_parser)
    b = [c]
    print(a in b)


if __name__ == '__main__':
    test()
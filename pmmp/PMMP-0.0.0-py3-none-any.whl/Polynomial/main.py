import copy


class Polynomial:
    def __init__(self, *args):
        self.contents = {i: coeff for i, coeff in enumerate(args)}

    def __str__(self):
        return str(self.contents)

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        _temp = copy.copy(self)
        if len(_temp.contents) < len(other.contents):
            for i in range(max(_temp.contents.keys()) + 1, len(other.contents.keys())):
                _temp.contents[i] = 0
            print(_temp)
            return Polynomial({i: _temp.contents[i] + other.contents[i] for i in _temp.contents.keys()})
        return other + self

    def __neg__(self):
        _temp = copy.copy(self)

        _temp.contents = {t[0]: -t[1] for t in zip(self.contents.keys(), self.contents.values())}
        return _temp

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        _temp = copy.copy(self)
        if len(_temp.contents) <= len(other.contents):
            for i in range(max(_temp.contents.keys()) + 1, len(other.contents.keys())):
                _temp.contents[i] = 0
            print(_temp)
            return Polynomial({i: _temp.contents[i] - other.contents[i] for i in _temp.contents.keys()})
        return -(other - self)


print(Polynomial(2, 3) - Polynomial(1))
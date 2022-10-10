import random as rnd


class ranged():
    def __init__(self, min, max, dif):
        if(float(dif) > float(max)) or (float(dif) < float(min)): raise ValueError("Argument out of range")
        self.min = float(min)
        self.max = float(max)
        self.default = float(dif)

    def ranged_value(self, val):
        try: val = float(val)
        except: val = self.default
        if (val > self.max) or (val < self.min): val = self.default
        return val

    def random_in_range(self):
        return rnd.uniform(float(self.min), float(self.max))

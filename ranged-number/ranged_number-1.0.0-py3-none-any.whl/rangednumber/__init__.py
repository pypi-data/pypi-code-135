import random as rnd


class ranged():
    def __init__(self, min, max, dif):
        if((isinstance(max, int)) == False and (isinstance(max, float)) == False) or ((isinstance(min, int)) == False and (isinstance(min, float)) == False) or ((isinstance(dif, int)) == False and (isinstance(dif, float)) == False):
            print(f'\033[31mYou can only use int or float!\nArg 1: {type(min)}\nArg 2: {type(max)}\nArg 3: {type(dif)}\033[0m')
            exit()
        if(dif > max) or (dif < min):
            print(f'\033[31mDefault: {dif}\nis not in range!\033[0m')
            exit()
        self.min = min
        self.max = max
        self.default = dif

    def ranged_value(self, val):
        if((isinstance(val, int) == False) and (isinstance(val, float) == False)) or (val > self.max) or (val < self.min):
            return self.default
        return val

    def random_in_range(self):
        return rnd.uniform(float(self.min), float(self.max))

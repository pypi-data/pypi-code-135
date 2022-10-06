"""Simple math calculator"""

__version__ = "0.1.5"

class Calculator:
    '''Module to solve math actions:
    add(number) adds number to current value
    sub(number) substracts number from current value
    mul(number) multiplies current value by number
    div(number) divides current value by number
    root(number) takes root of current value
    reset() resets current value back to 0

    for example:
        >>> Calculator.add(5)
        5.0
        >>> Calculator.sub(2)
        3.0
    '''

    def __init__(self):
        self.memory = 0
        self.err = ('Entered value must be float or integer. '
        'Check your input and try again')

    def add(self, a:float):
        try:
            self.memory += float(a)
            return (self.memory)
        except:
            print(self.err)

    def sub(self, a:float):
        try:
            self.memory -= float(a)
            return (self.memory)
        except:
            print(self.err)

    def mul(self, a:float):
        try:
            self.memory = self.memory * float(a)
            return (self.memory)
        except:
            print(self.err)

    def div(self, a:float):
        try:
            self.memory = self.memory / float(a)
            return (self.memory)
        except:
            print(self.err)

    def root(self, a:float):
        try:
            self.memory = self.memory**(1/float(a))
            return (self.memory)
        except:
            print(self.err)

    def reset(self):
        self.memory = 0
        return (self.memory)
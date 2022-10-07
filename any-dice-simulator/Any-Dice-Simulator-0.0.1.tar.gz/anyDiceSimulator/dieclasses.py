import random


class Die:
    def __init__(self, sides=6, numOnSides=[1, 2, 3, 4, 5, 6]):
        self.sides = sides
        self.numOnSides = numOnSides

    def dieProperties(self):
        print("==========================================")
        print("Die properties ->")
        print(f"Number of sides: {self.sides}")
        print(f"Numbering on sides: {self.numOnSides}")
        print("Biased: False")
        print("Side weights: None")
        print("==========================================")

    def rollDie(self, n):
        print(f"Number of rolls: {n}")
        result = random.choices(self.numOnSides, k=n)
        return result, sum(result)


class regularDie(Die):
    def __init__(self, sides=6, numOnSides=[1, 2, 3, 4, 5, 6]):
        self.sides = sides
        self.numOnSides = list(range(1, self.sides + 1))

    def dieProperties(self):
        print("==========================================")
        print("Die properties ->")
        print(f"Number of sides: {self.sides}")
        print(f"Numbering on sides: {self.numOnSides}")
        print("Biased: False")
        print("Side weights: None")
        print("==========================================")

    def rollDie(self, n):
        print(f"Number of rolls: {n}")
        result = random.choices(self.numOnSides, k=n)
        return result, sum(result)


class biasedDie(Die):
    def __init__(self, sides=6, numOnSides=[1, 2, 3, 4, 5, 6], biasWeights=[1, 1, 1, 1, 1, 10]):
        self.sides = sides
        self.numOnSides = numOnSides
        self.biasWeights = biasWeights

    def dieProperties(self):
        print("==========================================")
        print("Die properties ->")
        print(f"Number of sides: {self.sides}")
        print(f"Numbering on sides: {self.numOnSides}")
        print("Biased: True")
        print(f"Side weights: {self.biasWeights}")
        print("==========================================")

    def rollDie(self, n):
        print(f"Number of rolls: {n}")
        result = random.choices(self.numOnSides, k=n, weights=self.biasWeights)
        return result, sum(result)

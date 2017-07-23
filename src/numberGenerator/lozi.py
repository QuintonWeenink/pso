import random
import math

from numberGenerator import CPRNG

class Lozi(CPRNG):

    def __init__(self, a = 1.7, b = 0.5):
        self._a = a
        self._b = b
        super(Lozi, self).__init__()


    def getRandomSet(self, x, y):
        pass

    def random(self):
        self.y = self._b * self.x
        self.x = 1 - (self._a * abs(self.x)) + self.y

        return (self.x, self.y)

    def uniform(self, x, y):
        return random.uniform(x, y)

    def toString(self):
        return "Printing the set"
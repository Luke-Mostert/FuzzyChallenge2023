import numpy as np
import math
import matplotlib.pyplot as plt


class FuzzySet:
    def __init__(self, name):
        self.name = name

    @classmethod
    def calcMembership(cls, x):
        pass
    #@classmethod
    #def draw(cls):
    #    pass

class Triangle(FuzzySet):
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.domain = c - a

    @classmethod
    def calcMembership(cls, x):
        if cls.a <= x <= cls.b:
            return (x - cls.a) / (cls.b - cls.a)
        elif cls.b <= x <= cls.c:
            return (cls.c - x) / (cls.c - cls.b)
        else:
            return 0


class Trapezoid(FuzzySet):
    def __init__(self, name, a, b, c, d):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.domain = d - a

    @classmethod
    def calcMembership(cls, x):
        if x < cls.a:
            return 0
        elif cls.a <= x < cls.b:
            return (x - cls.a) / (cls.b - cls.a)
        elif cls.b <= x <= cls.c:
            return 1
        elif cls.c < x <= cls.d:
            return (cls.d - x) / (cls.d - cls.c)
        elif cls.d < x:
            return 0


class Gaussian(FuzzySet):
    def __init__(self, name, mean, std):
        self.name = name
        self.mean = mean
        self.std = std

    @classmethod
    def calcMembership(cls, x):
        return pow(math.e, -pow(2, (x - cls.mean)) / 2 * pow(2, cls.std))



  # def Union(self, USet):
  #     pass

  # def Intersection(self, ISet):
  #     pass

  # def Complement(self):
  #     pass

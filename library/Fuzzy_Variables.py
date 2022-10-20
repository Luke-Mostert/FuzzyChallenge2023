import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Set


class FuzzyVariables:
    def __init__(self, name, universe, xMin, xMax, sets):
        self.name = name
        self.universe = universe
        self.xMin = xMin
        self.xMax = xMax
        self.sets = sets

    #@classmethod
    #def draw(cls):
    #    pass

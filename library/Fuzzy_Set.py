import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Membership_Functions


class FuzzySet:
    def __init__(self, name):
        self.name = name
        self.memFuncList = []

    def addTriangle(self, name, domainMin, domainMax, resolution):
        pass

    def addTrapezoid(self, name, domainMin, domainMax, resolution):
        pass

    def addGaussian(self, name, domainMin, domainMax, resolution):
        pass

    def Union(self, USet):
        pass

    def Intersection(self, ISet):
        pass

    def Complement(self):
        pass

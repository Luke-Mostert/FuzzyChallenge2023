import numpy as np
import matplotlib.pyplot as plt


class MembershipFunctions:
    def __init__(self, name, domainMin, domainMax, resolution):
        self.name = name
        self.domainMin = domainMin
        self.domainMax = domainMax
        self.resolution = resolution

        self.domain = np.linspace(domainMin, domainMax, resolution)
        self.DOM = np.zeroes(self.domain.shape)

    @classmethod
    def Triangle(cls, peak):
        pass

    @classmethod
    def Trapezoid(cls, peakA, peakB):
        pass

    @classmethod
    def Gaussian(cls, avg):
        pass

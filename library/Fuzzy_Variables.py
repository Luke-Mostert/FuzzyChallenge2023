import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Set


class FuzzyVariables:
    def __init__(self, name, xMin, xMax, sets):
        self.name = name
        self.xMin = xMin
        self.xMax = xMax
        self.sets = sets

    def draw(self):
        arrX = np.linspace(self.xMin, self.xMax, (self.xMax - self.xMin) * 8)
        arrY = []
        for i in range(len(self.sets)):
            for j in range(len(arrX)):
                arrY.append(self.sets[i].calcMembership(arrX[j]))
            plt.plot(arrX, arrY, linewidth=1.0, label=self.sets[i].name)
            arrY = []
        plt.show()


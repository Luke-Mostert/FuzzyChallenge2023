import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Inference_System
from Fuzzy_Inference_System import Fuzzy_Rule_Set
from Fuzzy_Rule_Set import Fuzzy_Rules
from Fuzzy_Inference_System import Fuzzy_Variables
from Fuzzy_Variables import Fuzzy_Set

class TSKLearning:

    def __init__(self, n):
        self.n = n

    def TSKLearn(self, input, epochs):
        xk = []
        wk = []
        rules = []
        memFunctions = []
        error = 0
        for k in range(0, self.n + 1):
            xk[k] = ((2 * np.pi) / self.n) * (k - 1)
        for j in range(1, self.n):
            #how do these line up, xk is 2 bigger than memfunctions what size should wk be
            memFunctions[j - 1] = Fuzzy_Set.Triangle("A" + str(k), xk[k - 1], xk[k], xk[k + 1])
            wk[j - 1] = np.sin(xk[j - 1])
        for i in range(epochs):
            x = np.random.rand() * (2 * np.pi)
            output = 0
            for k in range(len(self.ruleset.rules)):
                output += wk[k] * memFunctions[k]
            error += TSKLearning.MSE(np.sin(), output)


    def MSE(self, input, output):
        coeff = (1/(2 *self.n))
        diff = output - input
        result = coeff * (diff * diff)
        return result


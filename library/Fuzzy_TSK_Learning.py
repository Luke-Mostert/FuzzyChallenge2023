import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Inference_System
import Fuzzy_Variables
import Fuzzy_Rule_Set

class TSKLearning:

    def __init__(self, n):
        self.n = n

    def TSKLearn(self, input, epochs):

        for i in range(epochs):
            x = np.random.rand() * (2 * np.pi)
            for k in range(len(self.ruleset.rules)):
                output += self.ruleset.rules[k].output *
            error += TSKLearning.MSE(input, output)


    def MSE(self, input, output):
        coeff = (1/(2 *self.n))
        diff = output - input
        result = coeff * (diff * diff)
        return result

    def addRule(self, ruleset, rule):

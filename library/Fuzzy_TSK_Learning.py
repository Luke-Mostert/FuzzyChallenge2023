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

    #hard coded for sin
    def TSKLearn(self, epochs):
        xk = []
        wk = []
        rules = []
        memFunctions = []
        error = []
        output = 0
        gradient = [0] * self.n
        outputX = [0] * self.n
        outputY = [0] * self.n
        for k in range(0, self.n + 2):
            xk.append(((2 * np.pi) / self.n) * (k - 1))
            #print(xk[k])
        for j in range(1, self.n + 1):
            memFunctions.append(Fuzzy_Set.Triangle("A" + str(j), xk[j - 1], xk[j], xk[j + 1]))
            #print(memFunctions[0])
            wk.append(np.sin(xk[j]))
            #print(memFunctions)
        for i in range(epochs):
            x = np.random.rand() * (2 * np.pi)
            for k in range(len(wk)):
                output = wk[k] * memFunctions[k].calcMembership(x)
                gradient[k] = (output - np.sin(x)) * memFunctions[k].calcMembership(x)
                wk[k] = wk[k] - (0.01 * output)
            error.append(TSKLearning.MSE(self, np.sin(x), output))
        for l in range(self.n):
            outputX[l] = l * ((2 * np.pi) / self.n)
            outputY[l] = wk[l] * memFunctions[l].calcMembership(l * ((2 * np.pi) / self.n))
        #print(error)
        print(output)
        print(len(wk))
        print(outputX)
        print(outputY)
        #print(wk)
        #print(gradient)
        self.DrawError(error)
        self.DrawFunction(outputX, outputY)


    def MSE(self, input, output):
        coeff = (1/(2 * self.n))
        diff = output - input
        result = coeff * (diff * diff)
        return result

    def DrawError(self, error):
        plt.plot(error)
        plt.title("Error")
        plt.show()

    def DrawFunction(self, outputX, outputY):
        x = np.arange(0, 2 * np.pi, 0.1)  # start,stop,step
        plt.plot(x, np.sin(x), label="Sin()")
        plt.plot(outputX, outputY, label="Approximation")
        plt.grid(color='k', linestyle='-', linewidth=.3)
        plt.legend(loc='upper right')
        plt.show()


import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Variables
import Fuzzy_Rule_Set


class FuzzyInferenceSystem:
    def __init__(self, variables, ruleset):
        self.variables = list([variables])
        self.ruleset = list([ruleset])

    def TSKEval(self, x, varName):
        numer = 0
        denom = 0
        for i in range(len(self.ruleset)):
            for j in range(len(self.variables)):
                if self.variables[j].name == varName:
                    for k in range(len(self.variables[j].sets)):
                        if self.variables[j].sets[k].name == self.ruleset[i].antecedents[0]:
                            numer += self.variables[j].sets[k].calcMembership(x) * self.ruleset[i].output
                            denom += self.variables[j].sets[k].calcMembership(x)

        return numer / denom

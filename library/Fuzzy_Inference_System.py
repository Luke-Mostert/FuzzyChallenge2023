import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Variables
import Fuzzy_Rule_Set


class FuzzyInferenceSystem:
    def __init__(self, variables, ruleset):
        self.variables = variables
        self.ruleset = ruleset

    def TSKEval(self, x, varName):
        numer = 0
        denom = 0
        for i in range(self.ruleset.len()):
            for j in range(self.variables.len()):
                if self.variables[j].name == varName:
                    for k in range(self.variables[j].sets.len()):
                        if self.variables[j].sets[k].name == self.ruleset[i].antecedents[0]:
                            numer += self.variables[j].sets[k].calcMembership(x) * self.ruleset[i].output
                            denom += self.variables[j].sets[k].calcMembership(x)

        return numer / denom

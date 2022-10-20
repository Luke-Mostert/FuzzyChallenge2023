import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Variables
import Fuzzy_Rule_Set


class FuzzyInferenceSystem:
    def __init__(self, variables, rules):
        self.variables = variables
        self.rules = rules

    @classmethod
    def TSKEval(cls, x):
        numer = 0
        denom = 0
        for i in range(1, cls.variables.len()):
            numer += cls.variables["temp"].sets[i].calcMembership(x) * cls.rules.output
            denom += cls.variables["temp"].sets[i].calcMembership(x)
        return numer / denom

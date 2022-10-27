import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Rules


class FuzzyRuleSet:
    def __init__(self, rules=[]):
        self.rules = rules

    def __getitem__(self, i):
        return self.rules[i]


    def printRules(self):
        for i in range(len(self.rules)):
            print(self.rules[i].rule)

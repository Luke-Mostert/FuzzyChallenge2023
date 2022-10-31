import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Rules


class FuzzyRuleSet:
    def __init__(self, rules=[]):
        self.rules = rules


    def printRules(self):
        for i in range(len(self.rules)):
            print(self.rules[i].rule)

import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Rules


class FuzzyRuleSet:
    def __init__(self, rules):
        self.rules = rules

    @classmethod
    def printRules(cls):
        for i in range(len(cls.rules)):
            print(cls.rules[i].rule)

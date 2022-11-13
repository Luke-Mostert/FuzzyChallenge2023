import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Variables
import Fuzzy_Rule_Set


class FuzzyInferenceSystem:
    def __init__(self, ruleset, variables=[]):
        self.variables = variables
        self.ruleset = ruleset
        self.dictAntecedent = {}
        #creating dictionary where key is rule antecedent and value is index to membership function
        for i in range(len(ruleset.rules)):
            for j in range(len(ruleset.rules[i].antecedents)):
                self.dictAntecedent[ruleset.rules[i].antecedents[j]] = [0, 0]
        for i in range(len(self.variables)):
            for j in range(len(self.variables[i].sets)):
                for k in range(len(self.variables[i].sets[j].name)):
                    if self.variables[i].sets[j].name in self.dictAntecedent:
                        self.dictAntecedent[self.variables[i].sets[j].name] = [i, j]



    def TSKEvalOne(self, x,varName):
        numer = 0
        denom = 0
        #Loop for each rule
        for i in range(len(self.ruleset.rules)):
            #Loop to find the correct variable with the matching name
            for j in range(len(self.variables)):
                if self.variables[j].name == varName:
                    #Check that the x value is in the range of the variable
                    if self.variables[j].xMin > x or self.variables[j].xMax < x:
                        print("This value is out of range")
                        return -999999999
                    #Searching for the matching membership function that goes with the current rule
                    for k in range(len(self.variables[j].sets)):
                        if self.variables[j].sets[k].name == self.ruleset.rules[i].antecedents[0]:
                            numer += self.variables[j].sets[k].calcMembership(x) * self.ruleset.rules[i].output
                            denom += self.variables[j].sets[k].calcMembership(x)

        return numer / denom

    #make the input a dictionary
    def TSKEvalTwo(self, inputs={}):
        #Creating a 2D list where rows are equal to the number of inputs
        # Columns are equal to number of sets in variables to the power of antecedents in the rules.
        rows = len(inputs)
        cols = len(self.variables[0].sets) ** len(self.ruleset.rules[0].antecedents)
        numer = [[0] * cols] * rows
        denom = [[0] * cols] * rows

        #Check if the values are in range of the variables
        for b in range(len(inputs)):
            for a in range(len(self.variables)):
                if self.variables[a].name == list(inputs)[b]:
                    # Check that the x value is in the range of the variable
                    if self.variables[a].xMin > list(inputs.values())[b] or self.variables[a].xMax < list(inputs.values())[b]:
                        print("This value is out of range")
                        return -999999999
        #Loop for each rule
        for m in range(len(inputs)):
            for i in range(len(self.ruleset.rules)):
                for k in range(len(self.ruleset.rules[i].antecedents)):
                    #Searching for the matching membership function that goes with the current rule
                    #Won't need these loops bc dictionary
                    varsIndex = self.dictAntecedent[self.ruleset.rules[i].antecedents[k]][0]
                    setIndex = self.dictAntecedent[self.ruleset.rules[i].antecedents[k]][1]
                    currInput = list(inputs.values())[m]
                    # We only want to multiply by the rules output once so do it to the first iteration
                    if m == 0:
                        numer[m][k] = self.variables[varsIndex].sets[setIndex].calcMembership(currInput) * self.ruleset.rules[i].output
                    else:
                        numer[m][k] = self.variables[varsIndex].sets[setIndex].calcMembership(currInput)
                    denom[m][k] = self.variables[varsIndex].sets[setIndex].calcMembership(currInput)
            print(m)

        numerReturn = 0
        denomReturn = 0

        for i in range(cols):
            numerTemp = 1
            denomTemp = 1
            for j in range(rows):
                numerTemp *= numer[i][j]
                denomTemp *= denom[i][j]
            numerReturn += numerTemp
            denomReturn += denomTemp
        return numerReturn / denomReturn

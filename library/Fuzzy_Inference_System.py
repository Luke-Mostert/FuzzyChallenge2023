import numpy as np
import matplotlib.pyplot as plt
import Fuzzy_Variables
import Fuzzy_Rule_Set


class FuzzyInferenceSystem:
    def __init__(self, ruleset,variables=[]):
        self.variables = variables
        self.ruleset = ruleset

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

    def TSKEvalTwo(self, x, y, varName=[]):
        numerX = []
        denomX = []
        numerY = []
        denomY = []

        #Loop for each rule
        for m in range(len(varName)):
            for i in range(len(self.ruleset.rules)):
                #Loop to find the correct variable with the matching name
                for j in range(len(self.variables)):
                    if self.variables[j].name == varName[m]:
                        #Check that the x value is in the range of the variable
                        if self.variables[j].xMin > x or self.variables[j].xMax < x:
                            print("This value is out of range")
                            return -999999999
                        if self.variables[j].xMin > y or self.variables[j].xMax < y:
                            print("This value is out of range")
                            return -999999999
                        #Searching for the matching membership function that goes with the current rule
                        for k in range(len(self.variables[j].sets)):
                            for l in range(len(self.ruleset.rules[i].antecedents)):
                                if self.variables[j].sets[k].name == self.ruleset.rules[i].antecedents[l]:
                                    if m == 0:

                                        numerX.append(self.variables[j].sets[k].calcMembership(x) * self.ruleset.rules[i].output)
                                        denomX.append(self.variables[j].sets[k].calcMembership(x))
                                    elif m == 1:
                                        numerY.append(self.variables[j].sets[k].calcMembership(y))
                                        denomY.append(self.variables[j].sets[k].calcMembership(y))
        numerReturn = 0
        denomReturn = 0
        print(*numerX , sep = ", ")
        print(*numerY , sep = ", ")
        print(*denomX, sep = ", ")
        print(*denomY , sep = ", ")

        for i in range(len(numerX)):
            numerReturn += numerX[i] * numerY[i]
            denomReturn += denomX[i] * denomY[i]
        return numerReturn / denomReturn
    #{service : 20, food : 20}
    #def TSKEval(self, inputs):
    #    numer = []
    #    denom = []
    #    z = []
    #    #Loop for each rule
    #    for i in range(len(self.ruleset.rules)):
    #        #Loop for each different variable in the rule
    #        for j in range(self.ruleset.rules[i].variableName):
    #            #Loop for each variable to find the matching one in the rule
    #            for k in range(len(self.variables)):
    #                #Checking if the two variable name matches whats in the rule
    #                if self.variables[k].name == self.ruleset.rules[i].variableName[j]:
    #                    #Loop for each membership function in the variable that was found
    #                    for l in range(len(self.variables[k].sets)):
    #                        #Loop for each antecedent in the current rule
    #                        for m in range(len(self.ruleset.rules[i].antecedents)):
    #                            #Checking if the antecedent and the current set name match
    #                            if self.variables[k].sets[l].name == self.ruleset.rules[i].antecedents[m]:
    #                                numer.append(self.variables[k].sets[l].calcMembership(inputs[self.ruleset.rules[i].variableName[j]]))
    #                                denom.append(self.variables[k].sets[l].calcMembership(inputs[self.ruleset.rules[i].variableName[j]]))
    #                                z.append(self.ruleset.rules[i].output)
    #    return numer / denom

import Fuzzy_Inference_System
from Fuzzy_Inference_System import Fuzzy_Rule_Set
from Fuzzy_Rule_Set import Fuzzy_Rules
from Fuzzy_Inference_System import Fuzzy_Variables
from Fuzzy_Variables import Fuzzy_Set

#rules
tempRuleCold = Fuzzy_Rules.TSKFuzzyRules("If temp is cold then 1")
tempRuleRoom = Fuzzy_Rules.TSKFuzzyRules("If temp is room then 0")
tempRuleHot = Fuzzy_Rules.TSKFuzzyRules("If temp is hot then -1")

#sets
triColdSet = Fuzzy_Set.Trapezoid("cold", 50, 50, 60, 70)
triRoomSet = Fuzzy_Set.Triangle("room", 60, 70, 80)
triHotSet = Fuzzy_Set.Trapezoid("hot", 70, 80, 90, 90)

#gaussian test
gSet = Fuzzy_Set.Gaussian("lilBaby", 50, 10)
gVar = Fuzzy_Variables.FuzzyVariables("temp", 0, 100, [gSet])

#variables
tempVar = Fuzzy_Variables.FuzzyVariables("temp", 50, 90, [triColdSet, triRoomSet, triHotSet])
#rulesets
tempRuleSet = Fuzzy_Rule_Set.FuzzyRuleSet([tempRuleCold, tempRuleRoom, tempRuleHot])
#create fis variables and rules
fis = Fuzzy_Inference_System.FuzzyInferenceSystem(tempVar, tempRuleSet)
#print(tempRuleSet[0].antecedents[0])
#tempRuleSet.printRules()
#call TSKfis with x and the variables we want to use
returnVal = fis.TSKEval(75, "temp")
print(returnVal)
gVar.draw()
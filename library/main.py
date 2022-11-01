import Fuzzy_Inference_System
from Fuzzy_Inference_System import Fuzzy_Rule_Set
from Fuzzy_Rule_Set import Fuzzy_Rules
from Fuzzy_Inference_System import Fuzzy_Variables
from Fuzzy_Variables import Fuzzy_Set


#This is how to create the full FIS and use the TSK eval with one antecedent

#rules
tempRuleCold = Fuzzy_Rules.TSKFuzzyRules("If temp is cold then 1")
tempRuleRoom = Fuzzy_Rules.TSKFuzzyRules("If temp is room then 0")
tempRuleHot = Fuzzy_Rules.TSKFuzzyRules("If temp is hot then -1")

#sets
triColdSet = Fuzzy_Set.Trapezoid("cold", 50, 50, 60, 70)
triRoomSet = Fuzzy_Set.Triangle("room", 60, 70, 80)
triHotSet = Fuzzy_Set.Trapezoid("hot", 70, 80, 90, 90)

#gaussian test
#gSet = Fuzzy_Set.Gaussian("lilBaby", 50, 10)
#gVar = Fuzzy_Variables.FuzzyVariables("temp", 0, 100, [gSet])

#variables
tempVar = Fuzzy_Variables.FuzzyVariables("temp", 50, 90, [triColdSet, triRoomSet, triHotSet])
#rulesets
tempRuleSet = Fuzzy_Rule_Set.FuzzyRuleSet([tempRuleCold, tempRuleRoom, tempRuleHot])
#create fis variables and rules
fis = Fuzzy_Inference_System.FuzzyInferenceSystem(tempRuleSet, [tempVar] )
#print(tempRuleSet[0].antecedents[0])
#tempRuleSet.printRules()
#call TSKfis with x and the variables we want to use
#returnVal = fis.TSKEvalOne(75, "temp")
#print(returnVal)
tempVar.draw("Temperature Problem", "Temperature")


#This is how to create a fis that uses TSK Eval with 2 antecedents
#T co norm
#rules
tempRuleGoodGreat = Fuzzy_Rules.TSKFuzzyRules("If service is good and food is great then 25")
tempRuleGoodAverage  = Fuzzy_Rules.TSKFuzzyRules("If service is good and food is average then 20")
tempRuleGoodGross  = Fuzzy_Rules.TSKFuzzyRules("If service is good and food is gross then 15")
tempRuleMidGreat  = Fuzzy_Rules.TSKFuzzyRules("If service is mid and food is great then 20")
tempRuleMidAverage   = Fuzzy_Rules.TSKFuzzyRules("If service is mid and food is average then 15")
tempRuleMidGross   = Fuzzy_Rules.TSKFuzzyRules("If service is mid and food is gross then 10")
tempRuleBadGreat  = Fuzzy_Rules.TSKFuzzyRules("If service is bad and food is great then 15")
tempRuleBadAverage   = Fuzzy_Rules.TSKFuzzyRules("If service is bad and food is average then 10")
tempRuleBadGross  = Fuzzy_Rules.TSKFuzzyRules("If service is bad and food is gross then 5")
#add in last 6 rules for all possible combinations

#sets
triGoodServiceSet = Fuzzy_Set.Triangle("good", 5, 10, 10)
triMidServiceSet = Fuzzy_Set.Triangle("mid", 0, 5, 10)
triBadServiceSet = Fuzzy_Set.Triangle("bad", 0, 0, 5)

triGoodFoodSet = Fuzzy_Set.Triangle("great", 5, 10, 10)
triMidFoodSet = Fuzzy_Set.Triangle("average", 0, 5, 10)
triBadFoodSet = Fuzzy_Set.Triangle("gross", 0, 0, 5)

#variables
serviceVar = Fuzzy_Variables.FuzzyVariables("service", 0, 10, [triGoodServiceSet, triMidServiceSet, triBadServiceSet])
foodVar = Fuzzy_Variables.FuzzyVariables("food", 0, 10, [triGoodFoodSet, triMidFoodSet, triBadFoodSet])
serviceVar.draw("Tipping Problem (Service)", "Service Quality")
foodVar.draw("Tipping Problem (Food)", "Food Quality")
#rulesets
tempRuleSet = Fuzzy_Rule_Set.FuzzyRuleSet([ tempRuleGoodGreat,
                                            tempRuleGoodAverage ,
                                            tempRuleGoodGross ,
                                            tempRuleMidGreat ,
                                            tempRuleMidAverage  ,
                                            tempRuleMidGross  ,
                                            tempRuleBadGreat ,
                                            tempRuleBadAverage  ,
                                            tempRuleBadGross  ])
#create fis variables and rules
fis = Fuzzy_Inference_System.FuzzyInferenceSystem(tempRuleSet, [serviceVar, foodVar])
#print(tempRuleSet[0].antecedents[0])
#tempRuleSet.printRules()
#call TSKfis with x and the variables we want to use
#returnVal = fis.TSKEvalTwo(3, 7, ["service", "food"])
#print(returnVal)
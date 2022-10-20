class FuzzyRules:
    def __init__(self, rule):
        self.rule = rule


class MamdaniFuzzyRules(FuzzyRules):
    def __init__(self, rule):
        super().__init__(self, rule)


class TSKFuzzyRules(FuzzyRules):
    def __init__(self, rule, output):


class FuzzyRules:
    def __init__(self, rule):
        self.rule = rule


class MandaniFuzzyRules(FuzzyRules):
    def __init__(self, rule):
        super().__init__(self, rule)


class TSKFuzzyRules(FuzzyRules):
    def __init__(self, rule, output):
        super().__init__(self, rule)
        self.output = output

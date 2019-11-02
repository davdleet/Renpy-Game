class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        print(self.value)


class UpgradeCalculator(Calculator):
    def minus(self, value):
        self.value -= value
        print(self.value)


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

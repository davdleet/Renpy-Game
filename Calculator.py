class Calc:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        print(result)

    def sub(self):
        result = self.first - self.second
        print(result)

    def mul(self):
        result = self.first * self.second
        print(result)

    def div(self):
        result = self.first / self.second
        print(result)


class CalcPlus(Calc):
    def pow(self):
        def pow(self):
            result = self.first ** self.second
            return result


class OverCalc(Calc):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
      
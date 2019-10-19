class calc:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        print(result)

a= calc()
a.setdata(4,5)
a.add()

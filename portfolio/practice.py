class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum_number(self):
        return self.a + self.b


class Run(Test):

    def pr(self):
        print(self.sum_number())

    def sum_number(self):
        return self.a - self.b


a = 5
b = 4

instance = Run(a, b)
instance.pr()

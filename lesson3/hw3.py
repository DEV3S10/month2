class Fraction:

    def __init__(self, numertor, denumerator):
        self.num = numertor
        self.denum = denumerator

    def __add__(self, other):
        c = self.num + self.denum
        print(c)

    def __sub__(self, other):
        c = self.num - self.denum
        print(c)

    def __mul__(self, other):
        c = self.num * self.denum
        print(c)

    def __floordiv__(self, other):
        c = self.num / self.denum
        print(c)





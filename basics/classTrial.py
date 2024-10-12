class Calc:
    num: int = 100

    def __init__(self, a: object, b: object):
        self.a = a
        self.b = b

    def print_val(self) -> object:
        return self.num

    def summation(self) -> int:
        return self.a + self.b + Calc.num


x: int = 10
y: int = 12
obj: Calc = Calc(x, y)
print(obj.print_val())
print(obj.num)
print(obj.summation())

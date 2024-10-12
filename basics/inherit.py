from classTrial import Calc


class InheritCheck(Calc):
    def __init__(self, a: object, b: object):
        Calc.__init__(self, a, b)


obj = InheritCheck(10, 20)
print(obj.summation())
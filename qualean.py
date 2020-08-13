import random
from decimal import Decimal, ROUND_HALF_EVEN
from math import sqrt, isclose
import pdb

class Qualean(object):

    def __init__(self, num):
        num = num * random.uniform(-1, 1)
        if type(num) == type(float()):
            num = str(num)
        self.num = Decimal(num).quantize(Decimal("0.0000000001"), rounding=ROUND_HALF_EVEN)

    def __and__(self, other):
        #pdb.set_trace()
        return self.num & other

    def __or__(self, other):
        return self.num | other

    def __repr__(self):
        return f"Length of num {len(str(self.num))}"

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return self.num + other

    def __eq__(self, other):
        return self.num == other

    def __float__(self):
        return float(self.num)

    def __ge__(self, other):
        return self.num >= other

    def __gt__(self, other):
        return self.num > other

    # def __invert__(self):
    #     pass

    def __invertsign__(self):
        return ~ self.num

    def __le__(self, other):
        return self.num <= other

    def __lt__(self, other):
        return self.num < other

    def __mul__(self, other):
        return self.num * other

    def __sqrt__(self):
        if self.num >= 0:
            return sqrt(self.num)
        else:
            raise ValueError("Provide valid number")

    def __bool__(self):
        return True if self.num else False


if __name__ == "__main__":
    l = [1, 0, -1]
    inp1 = random.choice(l)
    inp2 = random.choice(l)
    q1 = Qualean(inp1)
    q2 = Qualean(inp2)
    print(q1.num)
    print(q1.__sqrt__())
   # print(q1.__eq__(q2.num))
    #print(q1.__bool__())
    #print(sqrt(q1))

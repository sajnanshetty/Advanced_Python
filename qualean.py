import random
from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation
from math import isclose, sqrt
import pdb
#from cmath import sqrt


class Qualean(object):

    def __init__(self, num):
        if num not in [-1, 0, 1]:
            raise ValueError("Pass value range between -1 to 1")
        num = num * random.uniform(-1, 1)
        if type(num) == type(float()):
            num = str(num)
        self.num = Decimal(num).quantize(Decimal("1E-10"), rounding=ROUND_HALF_EVEN)


    def __and__(self, other):
        if not other:
            other = 0
        return round(self.num) & round(other)

    def __or__(self, other):
        if not other:
            return round(self.num) | round(0)
        return round(self.num) | round(other)

    def __repr__(self):
        return f"Length of num {len(str(self.num))}"

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        if not other:
            other = 0
        return self.num + other

    def __eq__(self, other):
        return self.num == other

    def __float__(self):
        return float(self.num)

    def __ge__(self, other):
        return self.num >= other

    def __gt__(self, other):
        return self.num > other

    def __invertsign__(self):
        return self.num * -1

    def __le__(self, other):
        return self.num <= other

    def __lt__(self, other):
        return self.num < other

    def __mul__(self, other):
        if not other:
            other = 0
        return self.num * other

    def __sqrt__(self):
        # if self.num._sign == 1:
        #     raise InvalidOperation('sqrt(-x), x > 0')
        # return sqrt(self.num)

        if self.num >= 0:
            return sqrt(self.num)
        else:
            raise InvalidOperation('sqrt(-x), x > 0')
        #return sqrt(self.num)

    def __bool__(self):
        return True if self.num else False


if __name__ == "__main__":
    l = [1, 0, -1]
    inp1 = random.choice(l)
    inp2 = random.choice(l)
    q1 = Qualean(inp1)
    #q2 = Qualean(inp2)
    q2 = None
    # print(bool(q1.__and__(q2)))
    print(False and None)
    # print(bool(q1.__or_(q2)))
    # print(int(q1.num) or None)
    print(q1)

    # print(q1.__sqrt__())
    #     print(q1.num)
    #     print(q2.num)
    #     print(q1.num and  q2)
    #     print(q1.num or q2)
# # print(q1.__eq__(q2.num))
# print(q1.__bool__())
# print(sqrt(q1))

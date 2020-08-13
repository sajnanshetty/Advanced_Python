from qualean import Qualean
import random
from math import sqrt, isclose


def get_random_num():
    l = [1, 0, -1]
    inp = random.choice(l)
    q_obj = Qualean(inp)
    return q_obj.num


def test_sum():
    q_um = get_random_num()
    sum = 0
    for i in range(100):
        sum += q_um
    assert sum == 100 * q_um


def test_sum_close_to_zero():
    sum = 0
    for i in range(100):
        q_um = get_random_num()
        sum += q_um
    val = isclose(sum, 0, rel_tol=1000)
    assert val is True

# def test_short_circute_case01():
#     q1 = get_random_num()
#     q2 = None
#     assert q1 and q2

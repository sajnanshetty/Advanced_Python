from qualean import Qualean
import random
from math import sqrt, isclose
from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation
import pytest
import pdb


def get_qualean_random_num():
    l = [1, 0, -1]
    inp = random.choice(l)
    q_obj = Qualean(inp)
    return q_obj.num


def get_qualean_obj():
    l = [1, 0, -1]
    inp = random.choice(l)
    q_obj = Qualean(inp)
    return q_obj


def test_sum_case_01():
    q_um = get_qualean_random_num()
    sum = 0
    for i in range(100):
        sum += q_um
    assert sum == 100 * q_um


def test_sum_close_to_zero_case_02():
    sum = 0
    for i in range(100):
        q_um = get_qualean_random_num()
        sum += q_um
    val = isclose(sum, 0, rel_tol=1000)
    assert val is True


# def test_sqrt_case_03():
#     q_obj = Qualean(1)
#     if q_obj.num > 0:
#         assert q_obj.__sqrt__() == q_obj.num.sqrt()
#     else:
#         with pytest.raises(InvalidOperation):
#             q_obj.__sqrt__()


@pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "q2": None}, {"q1": Qualean(0), "q2": None}])
def test_q1_and_q2_case_04(param):
    q1_obj = param["q1"]
    q2 = param["q2"]
    assert bool(q1_obj.__and__(q2)) is False


# @pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "q2": None}, {"q1": Qualean(1), "q2": None}])
# def test_q1_or_q2_case_05(param):
#     q1_obj = param["q1"]
#     q2 = param["q2"]
#     pdb.set_trace()
#     assert bool(q1_obj.__or__(q2)) is True


def test_repr_case_06():
    q_obj = get_qualean_obj()
    oup = q_obj.__repr__()
    assert oup == f"Length of num {len(str(q_obj.num))}"


def test_str_case_07():
    q_obj = get_qualean_obj()
    oup = q_obj.__str__()
    assert oup == str(q_obj.num)


@pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "q2": None, "out": "q1"},
                                   {"q1": Qualean(0), "q2": None, "out": "q1"},
                                   {"q1": get_qualean_obj(), "q2": get_qualean_random_num(), "out": "q1+q2"}])
def test_add_case_08(param):
    q1_obj = param["q1"]
    q2 = param["q2"]
    out = param["out"]
    if out == "q1":
        out = q1_obj.num
    else:
        out = q1_obj.num + q2
    actual_out = q1_obj.__add__(q2)
    assert actual_out == out


@pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "out": "same"}, {"q1": Qualean(0), "out": "same"},
                                   {"q1": get_qualean_obj(), "out": "diff"}])
def test_eq_case_07(param):
    q1_obj = param["q1"]
    out = param["out"]
    if out == "same":
        q2 = q1_obj.num
        target_out = True
    else:
        q2 = Decimal("3")
        target_out = False
    actual_out = q1_obj.__eq__(q2)
    assert actual_out is target_out


def test_float_case_08():
    q_obj = get_qualean_obj()
    oup = q_obj.__float__()
    assert oup == float(q_obj.num)


@pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "q2": get_qualean_random_num()}])
def test_ge_case_09(param):
    q1_obj = param["q1"]
    q2 = param["q2"]
    if q1_obj.num >= q2:
        target_out = True
    else:
        target_out = False
    actual_out = q1_obj.__ge__(q2)
    assert actual_out is target_out


@pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "q2": get_qualean_random_num()}])
def test_gt_case_10(param):
    q1_obj = param["q1"]
    q2 = param["q2"]
    if q1_obj.num > q2:
        target_out = True
    else:
        target_out = False
    actual_out = q1_obj.__gt__(q2)
    assert actual_out is target_out


@pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "q2": get_qualean_random_num()}])
def test_le_case_10(param):
    q1_obj = param["q1"]
    q2 = param["q2"]
    if q1_obj.num <= q2:
        target_out = True
    else:
        target_out = False
    actual_out = q1_obj.__le__(q2)
    assert actual_out is target_out


@pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "q2": get_qualean_random_num()}])
def test_lt_case_10(param):
    q1_obj = param["q1"]
    q2 = param["q2"]
    if q1_obj.num < q2:
        target_out = True
    else:
        target_out = False
    actual_out = q1_obj.__lt__(q2)
    assert actual_out is target_out


@pytest.mark.parametrize("param",
                         [{"q1": get_qualean_obj(), "q2": None, "out": 0}, {"q1": Qualean(0), "q2": None, "out": 0},
                          {"q1": get_qualean_obj(), "q2": get_qualean_random_num(), "out": "q1*q2"}])
def test_mul_case_11(param):
    q1_obj = param["q1"]
    q2 = param["q2"]
    out = param["out"]
    if out == "q1*q2":
        out = q1_obj.num * q2
    else:
        out = out
    actual_out = q1_obj.__mul__(q2)
    assert actual_out == out


@pytest.mark.parametrize("param", [{"q1": get_qualean_obj(), "q2": get_qualean_random_num()}])
def test_bool_case_12(param):
    q1_obj = param["q1"]
    out = True if q1_obj.num else False
    actual_out = q1_obj.__bool__()
    assert actual_out == out


def test_bool_case_13():
    q1_obj = get_qualean_random_num()
    assert isinstance(q1_obj, Decimal)


def test_bool_case_14():
    with pytest.raises(ValueError, match="Pass value range between -1 to 1"):
        Qualean(50)


def test_invertsign_case_15():
    q1 = get_qualean_obj()
    out = q1.__invertsign__()
    assert out == q1.num * -1

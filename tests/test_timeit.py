from modules.timeit import *
import pytest
import os


def test_time_it_print_case_01():
    print_args = (1, 2, 3)
    print_kwargs = dict(sep='-', end=' ***\n')
    print_repetations = 5
    avg_time, out = time_it(print, *print_args, repetitons=print_repetations, **print_kwargs)
    assert avg_time >= 0.0
    assert out is "Nothing"


def test_time_it_square_case_02():
    square_args = (2,)
    square_kwargs = dict(start=0, end=5)
    square_repetations = 5
    avg_time, out = time_it(squared_power_list, *square_args, repetitons=square_repetations, **square_kwargs)
    assert isinstance(avg_time, float) and avg_time > 0.0
    assert all(out) > 0


def test_time_it_polygon_area_case_03():
    poly_repetations = 10
    polygon_args = (15,)
    polygon_kwargs = dict(sides=3)
    avg_time, out = time_it(polygon_area, *polygon_args, repetitons=poly_repetations, **polygon_kwargs)
    assert isinstance(avg_time, float) and avg_time >= 0.0
    assert out > 0


def test_time_it_temp_converter_case_04():
    temp_repetations = 100
    temp_args = (100,)
    temp_kwargs = dict(temp_given_in='f')
    avg_time, out = time_it(temp_converter, *temp_args, repetitons=temp_repetations, **temp_kwargs)
    assert isinstance(avg_time, float) and avg_time >= 0.0
    assert out == 37.77777777777778


def test_time_it_speed_converter_case_05():
    speed_repetations = 200
    speed_args = (100,)
    speed_kwargs = dict(dist='km', time='min')
    avg_time, out = time_it(speed_converter, *speed_args, repetitons=speed_repetations, **speed_kwargs)
    assert type(avg_time) is float and avg_time > 0.0
    assert out > 0


def test_time_it_speed_converter_case_06():
    speed_repetations = 0
    speed_args = (100,)
    speed_kwargs = dict(dist='km', time='min')
    with pytest.raises(ValueError) as err:
        time_it(speed_converter, *speed_args, repetitons=speed_repetations, **speed_kwargs)
    assert err.value.args[0] == "Invalid value for repetitons is used.should be greater than 0."


def test_validate_fn_case_07():
    with pytest.raises(ValueError) as err:
        validate_fn(dir)
    assert err.value.args[0] == "Invalid function used. Valid lists are:" \
                                " print, squared_power_list, polygon_area, temp_converter, speed_converter."


def test_validate_fn_expected_print_case_08():
    print_args = ()
    print_kwargs = dict(sep='-', end=' ***\n')
    fn = "print"
    with pytest.raises(ValueError, match=f"No inputs given to {fn}.") as err:
        validate_fn_expected_case("print", ["sep", "end"], *print_args, **print_kwargs)


@pytest.mark.parametrize('kwargs', (
        ["The sep is required argument for print.", {'end': '*'}],
        ["The end is required argument for print.", {'sep': '-'}]))
def test_validate_fn_expected_print_case_09(kwargs):
    print_args = (1, 2,)
    print_kwargs = kwargs[1]
    msg1 = kwargs[0]
    with pytest.raises(ValueError, match=msg1) as err:
        validate_fn_expected_case("print", ["sep", "end"], *print_args, **print_kwargs)


@pytest.mark.parametrize('kwargs', ({'sep': 2, 'end': 'xxx'}, {'sep': '-', 'end': 1}))
def test_validate_fn_expected_print_case_10(kwargs):
    print_args = (1, 2,)
    print_kwargs = kwargs
    fn = "print"
    if isinstance(print_kwargs["sep"], int):
        msg = f"sep must be a {str}, not {type(print_kwargs['sep'])}"
    else:
        msg = f"end must be a {str}, not {type(print_kwargs['end'])}"
    with pytest.raises(TypeError, match=msg) as err:
        validate_fn_expected_case("print", ["sep", "end"], *print_args, **print_kwargs)


def test_validate_fn_expected_squared_power_list_case_11():
    square_args = ()
    square_kwargs = dict(start=0, end=5)
    fn = "squared_power_list"
    with pytest.raises(ValueError, match=f"No inputs given to {fn}.") as err:
        validate_fn_expected_case("squared_power_list", ["start", "end"], *square_args, **square_kwargs)


@pytest.mark.parametrize('kwargs', (
        ["The end is required argument for squared_power_list.", {'start': 2}],
        ["The start is required argument for squared_power_list.", {'end': 1}]))
def test_validate_fn_expected_squared_power_list_case_12(kwargs):
    square_args = (2,)
    print_kwargs = kwargs[1]
    msg1 = kwargs[0]
    with pytest.raises(ValueError, match=msg1):
        validate_fn_expected_case("squared_power_list", ["start", "end"], *square_args, **print_kwargs)


@pytest.mark.parametrize('kwargs', ({'start': 2, 'end': 'xxx'}, {'start': '-', 'end': 1}))
def test_validate_fn_expected_squared_power_list_case_13(kwargs):
    square_args = (3,)
    square_kwargs = kwargs
    fn = "squared_power_list"
    if isinstance(square_kwargs["end"], str):
        msg = f"end must be a {int}, not {type(square_kwargs['end'])}"
    else:
        msg = f"start must be a {int}, not {type(square_kwargs['start'])}"
    with pytest.raises(TypeError, match=msg):
        validate_fn_expected_case("squared_power_list", ["start", "end"], *square_args, **square_kwargs)

    polygon_args = (15,)
    polygon_kwargs = dict(sides=3)


def test_validate_fn_expected_polygon_area_case_14():
    poly_args = ()
    poly_kwargs = {"sides": 2}
    fn = "polygon_area"
    with pytest.raises(ValueError, match=f"No inputs given to {fn}."):
        validate_fn_expected_case("polygon_area", ["sides"], *poly_args, **poly_kwargs)


def test_validate_fn_expected_polygon_area_case_15():
    poly_args = (12,)
    poly_kwargs = {}
    msg = "The sides is required argument for polygon_area."
    with pytest.raises(ValueError, match=msg):
        validate_fn_expected_case("polygon_area", ["sides"], *poly_args, **poly_kwargs)


def test_validate_fn_expected_polygon_area_case_16():
    poly_args = (15,)
    poly_kwargs = dict(sides="one")
    fn = "polygon_area"
    msg = f"sides must be a {int}, not {str}"
    with pytest.raises(TypeError, match=msg):
        validate_fn_expected_case("polygon_area", ["sides"], *poly_args, **poly_kwargs)


def test_validate_fn_expected_temp_converter_case_17():
    temp_args = ()
    temp_kwargs = {'temp_given_in': 'f'}
    fn = "temp_converter"
    with pytest.raises(ValueError, match=f"No inputs given to {fn}."):
        validate_fn_expected_case("temp_converter", ["temp_given_in"], *temp_args, **temp_kwargs)


def test_validate_fn_expected_temp_converter_case_18():
    temp_args = (100,)
    temp_kwargs = {}
    msg = "The temp_given_in is required argument for temp_converter."
    with pytest.raises(ValueError, match=msg):
        validate_fn_expected_case("temp_converter", ["temp_given_in"], *temp_args, **temp_kwargs)


def test_validate_fn_expected_temp_converter_case_19():
    temp_args = (100,)
    temp_kwargs = {'temp_given_in': 37}
    fn = "temp_converter"
    msg = f"temp_given_in must be a {str}, not {int}"
    with pytest.raises(TypeError, match=msg):
        validate_fn_expected_case("temp_converter", ["temp_given_in"], *temp_args, **temp_kwargs)


def test_validate_fn_expected_speed_converter_case_20():
    temp_args = ()
    temp_kwargs = dict(dist='km', time='min')
    fn = "speed_converter"
    with pytest.raises(ValueError, match=f"No inputs given to {fn}."):
        validate_fn_expected_case("speed_converter", ["dist", "time"], *temp_args, **temp_kwargs)


@pytest.mark.parametrize('kwargs', (
        ["The time is required argument for speed_converter.", {'dist': 'km'}],
        ["The dist is required argument for speed_converter.", {'time': 'min'}]))
def test_validate_fn_expected_speed_converter_case_21(kwargs):
    temp_args = (100,)
    temp_kwargs = kwargs[1]
    msg = kwargs[0]
    with pytest.raises(ValueError, match=msg):
        validate_fn_expected_case("speed_converter", ["dist", "time"], *temp_args, **temp_kwargs)


@pytest.mark.parametrize('kwargs', ({'dist': 200, 'time': 'min'}, {'dist': 'km', 'time': 100}))
def test_validate_fn_expected_speed_converter_case_22(kwargs):
    temp_args = (100,)
    temp_kwargs = kwargs
    if isinstance(temp_kwargs["dist"], int):
        msg = f"dist must be a {str}, not {int}"
    else:
        msg = f"time must be a {str}, not {int}"
    with pytest.raises(TypeError, match=msg):
        validate_fn_expected_case("speed_converter", ["dist", "time"], *temp_args, **temp_kwargs)


def test_validate_fn_expected_value_choices_temp_converter_case_23():
    temp_kwargs = dict(temp_given_in='k')
    msg = "The expected choices for temp_given_in is not valid. Provide choices from f, c"
    with pytest.raises(ValueError, match=msg):
        validate_fn_expected_value_choices(**temp_kwargs)


time_choice_msg1 = 'The expected choices for time is not valid. Provide choices from ms, min, hr, day, sec'
time_choice_msg2 = 'The expected choices for dist is not valid. Provide choices from km, mt, ft, yrd'


@pytest.mark.parametrize('kwargs', (
        [time_choice_msg1, dict(dist='km', time='m')], [time_choice_msg2, dict(dist='km1', time='min')]))
def test_validate_fn_expected_value_choices_speed_converter_case_24(kwargs):
    speed_kwargs = kwargs[1]
    msg = kwargs[0]
    with pytest.raises(ValueError, match=msg):
        validate_fn_expected_value_choices(**speed_kwargs)


@pytest.mark.parametrize('kwargs', (dict(start=-2, end=5), dict(start=2, end=-5)))
def test_validate_positive_values_squared_power_list_case_25(kwargs):
    square_kwargs = kwargs
    if kwargs["start"] < 0:
        msg = "The start should be given positive value."
    else:
        msg = "The end should be given positive value."
    with pytest.raises(ValueError, match=msg):
        validate_positive_values(**square_kwargs)


@pytest.mark.parametrize('sides', (2, 7))
def test_validate_polygon_restrict_sides_case_26(sides):
    msg = 'Invalid value passed. Expected values are 3, 4, 5, 6'
    with pytest.raises(ValueError, match=msg):
        validate_polygon_restrict_sides(sides)


@pytest.mark.parametrize("dist", ["km", "mt", "ft", "yrd"])
@pytest.mark.parametrize("time", ["ms", "min", "hr", "day", "sec"])
def test_time_it_speed_converter_case_27(dist, time):
    speed_repetations = 300
    speed_args = (200,)
    speed_kwargs = dict(dist=dist, time=time)
    avg_time, out = time_it(speed_converter, *speed_args, repetitons=speed_repetations, **speed_kwargs)
    assert type(avg_time) is float and avg_time > 0.0
    assert out > 0


def test_time_it_temp_converter_case_28():
    temp_repetations = 300
    temp_args = (27,)
    temp_kwargs = dict(temp_given_in='c')
    avg_time, out = time_it(temp_converter, *temp_args, repetitons=temp_repetations, **temp_kwargs)
    assert type(avg_time) is float and avg_time > 0.0
    assert out == 80.6


def test_readme_exists_case_29():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_validate_positive_values_polygon_area_case_30():
    polygon_kwargs = dict(sides=-3)
    msg = "The sides should be given positive value."
    with pytest.raises(ValueError, match=msg):
        validate_positive_values(**polygon_kwargs)

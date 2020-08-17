import time
import math

allowed_fns = ["print", "squared_power_list", "polygon_area", "temp_converter", "speed_converter"]
choice_map = {
    "dist": ["km", "mt", "ft", "yrd"],
    "time": ["ms", "min", "hr", "day", "sec"],
    "temp_given_in": ["f", "c"]
}
value_type_map = {
    "print": str,
    "squared_power_list": int,
    "polygon_area": int,
    "temp_converter": str,
    "speed_converter": str
}


def validate_fn(fn):
    """
    :param fn: function name
    :return: Throws error when fn is not allowed list i.e print, squared_power_list,
     polygon_area, temp_converter, speed_converter
    """
    if fn.__name__ not in allowed_fns:
        raise ValueError(f"Invalid function used. Valid lists are: {', '.join(allowed_fns)}.")


def time_it(fn, *args, repetitons=1, **kwargs):
    """
    :param fn: fn names any one from  list [print, squared_power_list, polygon_area, temp_converter, speed_converter]
    :param args: Number of arguments of fn
    :param repetitons: the number of times fn needs to be called
    :param kwargs: key word arguments which is accepted by fn
    :return: tuple: average time taken by fn and the return value of fn
    """
    validate_fn(fn)
    if fn.__name__ == "print":
        fn = print_lines
    if repetitons <= 0:
        raise ValueError("Invalid value for repetitons is used.should be greater than 0.")
    start = time.time()
    for i in range(repetitons):
        out = fn(*args, **kwargs)
    end = time.time()
    return (end - start) / repetitons, out


def validate_fn_expected_case(fn, expected_kwargs, *args, **kwargs):
    """
    :param fn: function name
    :param expected_kwargs: valid keys which is expected from fn
    :param args: arguments which is accepted by fn
    :param kwargs: key value pairs which is accepted by fn
    :return: None for Success. raises error for failure case
        1) arguments are empty
        2) positional argument values are negative
        3) keys in kwargs are invalid key
        4) mandatory keys are not passed in kwargs
        5) kwargs values are invalid type.
    """
    if len(args) < 1:
        raise ValueError(f"No inputs given to {fn}.")
    elif fn != "print" and args[0] <= 0:
        raise ValueError(f"Given input can't be negative for {fn}.")
    for key in expected_kwargs:
        if key not in kwargs:
            raise ValueError(f"The {key} is required argument for {fn}.")
        elif not isinstance(kwargs[key], value_type_map.get(fn)):
            raise TypeError(f"{key} must be a {value_type_map[fn]}, not {type(kwargs[key])}")


def validate_fn_expected_value_choices(**kwargs):
    """
    :param kwargs: key value pairs which is passed from user
    :return: None for Success. raises error for failure case
    i.e if values are not in the valid choice
    """
    for key, val in kwargs.items():
        if val not in choice_map[key]:
            raise ValueError(
                f"The expected choices for {key} is not valid. Provide choices from {', '.join(choice_map[key])}")


def validate_positive_values(**kwargs):
    """
    :param kwargs:  key value pairs which is entered from users
    :return:  None for Success. raises error for failure case
    i.e if values are not positive
    """
    for key, val in kwargs.items():
        if val < 0:
            raise ValueError(f"The {key} should be given positive value.")


def validate_polygon_restrict_sides(num_sides):
    """
    :param num_sides: int
    :return: None for Success. raises error for failure case
    i.e if num_sides not in range btw 3-6
    """
    if num_sides < 3 or num_sides > 6:
        raise ValueError(
            f"Invalid value passed. Expected values are {', '.join([str(num) for num in list(range(3, 7))])}")


def print_lines(*args, **kwargs):
    """
    :param args: the words need to be printed.
    :param kwargs: This accepts key sep, end.
    - Validation is handled for below cases:
        case1: args does not holds any value.
        case2: sep and end keys not exist in kwargs
        case3: sep and keys not passed as string
    :return: 'Nothing'
    """
    validate_fn_expected_case("print", ["sep", "end"], *args, **kwargs)
    print(*args, sep=kwargs["sep"], end=kwargs["end"])
    return "Nothing"


def squared_power_list(*args, **kwargs):
    """
    :param args: num which power value has to be calculated
    :param kwargs: This accepts key start, end.
    - Validation is handled for below cases:
        case1: args are empty.
        case2: args hold more than one value.
        case3: args value is negative
        case4: start and end keys not exist in kwargs
        case5: start and end keys values are negative
    :return: list of all power calculated from start to end range.
    """
    print("Entered squared_power_list")
    validate_fn_expected_case("squared_power_list", ["start", "end"], *args, **kwargs)
    validate_positive_values(**kwargs)
    pow_list = list(range(kwargs["start"], kwargs["end"]))
    val = [math.pow(args[0], i) for i in pow_list]
    print(f"squared_power_list: Num {args[0]} calculated power for {', '.join([str(i) for i in pow_list])} is"
          f" {', '.join([str(i) for i in val])} respectively.")
    print("Exit squared_power_list")
    return val


def polygon_area(*args, **kwargs):
    """
    :param args: side length for creating polygon.
    :param kwargs: This accepts key 'sides'.
    - Validation is handled for below cases:
        case1: args are empty.
        case2: args hold more than one value i.e side length
        case3: side length value is negative
        case4: side length value lesser than 3 and more than 6
    :return: The area of created polygon
    """
    validate_fn_expected_case("polygon_area", ["sides"], *args, **kwargs)
    validate_positive_values(**kwargs)
    side_length = args[0]
    num_sides = kwargs['sides']
    validate_polygon_restrict_sides(num_sides)
    area = (num_sides * side_length * side_length) / (4 * math.tan(math.pi / num_sides))
    print(f"polygon_area for num sides {num_sides} and side length {side_length} is {area}")
    return area


def temp_converter(*args, **kwargs):
    """
    :param args: base temperature given to be converted.
    :param kwargs: This accepts key 'temp_given_in' with choices ['f', 'c'].
    - If temperature given is 'f' which converts to celcius
    - If temperature given is 'c' which converts to farenheit
    - Validation is handled for below cases:
        case1: args are empty.
        case2: args hold more than one value i.e base value
        case3: if base value is negative
        case4: temp_given_in' not exists in kwargs
        case5: 'temp_given_in' is not 'f' or 'c'
    :return: Converted values from celcius to farenheit/ farenheit to celcius
    """
    validate_fn_expected_case("temp_converter", ["temp_given_in"], *args, **kwargs)
    validate_fn_expected_value_choices(**kwargs)
    if kwargs['temp_given_in'] == 'f':
        # convert to celsius
        conv_val = (args[0] - 32) / (9.0 / 5.0)
    else:
        # convert to fahrenheit
        conv_val = (9.0 / 5.0) * args[0] + 32
    return conv_val


def speed_converter(*args, **kwargs):
    """
    :param args: base value which is given by user in kmph
    :param kwargs: allowed keys are 'dist' referce to distance and time
    - Allowable choices for dist: ["km", "mt", "ft", "yrd"]
    - Allowable choices for time: ["ms", "min", "hr", "day", "sec"]
    - Validation is handled for below cases:
        case1: args are empty
        case2: args hold more than one value i.e base value
        case3: if base value is negative
        case4: dist and time not exists in kwargs
        case5: dist is not valid choice
        case6: time is not valid choice
    :return: converted speed value based on the 'dist' and 'time'
    """
    print("speed_converter")
    validate_fn_expected_case("temp_converter", ["dist", "time"], *args, **kwargs)
    validate_fn_expected_value_choices(**kwargs)

    # all values are wrt one kilo-metre
    dist_map = {'km': 1, 'mt': 1000, 'ft': 3280.8, 'yrd': 1093.61}

    # all values wrt one hour
    time_map = {'hr': 1, 'min': 60, 'sec': 3600, 'ms': 3.6e+6, 'day': 0.041667}

    in_speed = args[0]
    out_speed = in_speed * dist_map[kwargs['dist']] / time_map[kwargs['time']]
    return out_speed

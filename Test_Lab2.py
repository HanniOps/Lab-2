import Lab2

def test_find_min_max():
    input_value = [1,-1, 2, 3, 4, 5, 99]
    test = [-1,99]

    result = Lab2.find_min_max(input_value)
    assert (result == test)


def test_calc_average():
    input_value = [1,-1, 2, 3, 4, 5, 99]
    test = 16.14
    result = Lab2.calc_average(input_value)
    assert (result == test)


def test_calc_median_temperature():
    input_value = [1,-1, 2, 3, 4, 5, 99]
    test = 3
    result = Lab2.calc_median_temperature(input_value)
    assert (result == test)
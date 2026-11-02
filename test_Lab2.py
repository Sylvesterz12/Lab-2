import ex3


def test_find_min_max():
    temperatures = [5.0, 67.0, 32.0, 12.0]

    result = ex3.find_min_max(temperatures)

    assert (result == (5.0, 67.0))


def test_find_min_max_single_value():
    temperatures = [10.0]

    result = ex3.find_min_max(temperatures)

    assert (result == (10.0, 10.0))


def test_calc_average():
    temperatures = [10.0, 20.0, 30.0]

    result = ex3.calc_average(temperatures)

    assert (result == 20.0)


def test_calc_median_temperature_odd():
    temperatures = [30.0, 10.0, 20.0]

    result = ex3.calc_median_temperature(temperatures)

    assert (result == 20.0)


def test_calc_median_temperature_even():
    temperatures = [40.0, 10.0, 30.0, 20.0]

    result = ex3.calc_median_temperature(temperatures)

    assert (result == 25.0)
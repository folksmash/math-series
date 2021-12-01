from math_series.series import fibonacci, lucas, sum_series

def test_import():
    assert fibonacci


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_lucas():
    actual = lucas(2)
    expected = 3
    assert actual == expected

# 4, 6, 10, 16, 26
def test_sum():
    actual = sum_series(5, 4, 6)
    expected = 26
    assert actual == expected 
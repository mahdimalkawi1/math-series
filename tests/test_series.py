import pytest
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_three():
    actual = lucas(6)
    expected = 18
    assert actual == expected

def test_lucas_four():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(7,2,1)
    expected = 29
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(7,0,1)
    expected = 13
    assert actual == expected

def test_sum_series_three():
    actual = sum_series(4,7,10)
    expected = 44
    assert actual == expected

def test_sum_series_four():
    actual = sum_series(5,7,10)
    expected = 71
    assert actual == expected


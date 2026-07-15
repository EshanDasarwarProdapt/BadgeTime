import pytest
from addition import add, subtract, multiply, divide

# ------------------ Addition ------------------

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5

def test_add_positive_and_negative():
    assert add(5, -3) == 2

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)


# ------------------ Subtraction ------------------

def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8


# ------------------ Multiplication ------------------

def test_multiply_positive_numbers():
    assert multiply(4, 5) == 20

def test_multiply_negative_numbers():
    assert multiply(-4, -5) == 20

def test_multiply_positive_and_negative():
    assert multiply(4, -5) == -20

def test_multiply_zero():
    assert multiply(10, 0) == 0


# ------------------ Division ------------------

def test_divide_positive_numbers():
    assert divide(10, 2) == 5

def test_divide_floats():
    assert divide(5, 2) == pytest.approx(2.5)

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5

def test_divide_by_one():
    assert divide(8, 1) == 8

def test_divide_by_zero():
    try:
        divide(5, 0)
    except ZeroDivisionError:
        pass
    else:
        assert False
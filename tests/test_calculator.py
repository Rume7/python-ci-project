# tests/test_calculator.py

import pytest
from calculator.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 3) == -3

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


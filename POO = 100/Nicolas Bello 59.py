import pytest
from simple_math import divide, multiply

def test_divide_success():
    assert divide(10, 2) == 5.0
    assert divide(-10, 5) == -2.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_multiply_success():
    assert multiply(5, 2) == 10.0
    assert multiply(-3, 4) == -12.0

import pytest
from app_to_test import add, subtract

@pytest.fixture
def sample_numbers():
    return (10, 5)

def test_add_pytest(sample_numbers):
    num1, num2 = sample_numbers
    assert add(num1, num2) == 15
    assert add(-5, 5) == 0

def test_subtract_pytest(sample_numbers):
    num1, num2 = sample_numbers
    assert subtract(num1, num2) == 5
    assert subtract(0, 0) == 0

@pytest.mark.parametrize("input_a, input_b, expected_sum", [
    (1, 2, 3),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add_parametrized(input_a, input_b, expected_sum):
    assert add(input_a, input_b) == expected_sum

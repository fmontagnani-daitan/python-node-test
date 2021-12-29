import pytest
from src.operations.operations import soma, multiply, subtract, divide # pylint: disable=import-error

@pytest.fixture(name="num1")
def set_num_1():
    num1 = 1
    return num1

@pytest.fixture(name="num2")
def set_num_2():
    num2 = 2
    return num2

def test_soma(num1, num2):
    assert soma(num1, num2) == 3

def test_subtract(num1, num2):
    assert subtract(num1, num2) == -1

def test_multiply(num1, num2):
    assert multiply(num1, num2) == 2

def test_divide(num1, num2):
    assert divide(num1, num2) == 0.5

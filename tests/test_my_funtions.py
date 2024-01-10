import pytest
import source.my_functions as my_functions



def test_add_numbers():
    # Test addition of two positive numbers
    assert my_functions.add_numbers(1, 2) == 3

    # Test addition of a positive and a negative number
    assert my_functions.add_numbers(5, -3) == 2

    # Test addition of two negative numbers
    assert my_functions.add_numbers(-10, -5) == -15

    # Test addition of zero and a positive number
    assert my_functions.add_numbers(0, 7) == 7

    # Test addition of zero and a negative number
    assert my_functions.add_numbers(0, -4) == -4
"test for add string"
def test_add_string():
    assert my_functions.add_numbers("hello", "world") == "helloworld"
def test_divide_numbers_valid_input():
    # Test division of two positive numbers
    assert my_functions.divide_numbers(10, 2) == 5

    # Test division of a positive number by zero
    assert my_functions.divide_numbers(10, 0) == None

    # Test division of a negative number by a positive number
    assert my_functions.divide_numbers(-10, 2) == -5

def test_divide_numbers_invalid_input():
    # Test division of zero by a positive number
    assert my_functions.divide_numbers(0, 5) == 0

    # Test division of zero by zero
    assert my_functions.divide_numbers(0, 0) == None

def test_divide_numbers_float_input():
    # Test division of two floating-point numbers
    assert my_functions.divide_numbers(3.14, 2) == 1.57

    # Test division of a floating-point number by zero
    assert my_functions.divide_numbers(3.14, 0) == None

    # Test division of a negative floating-point number by a positive floating-point number
    assert my_functions.divide_numbers(-3.14, 2) == -1.57


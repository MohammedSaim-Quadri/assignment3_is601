"""
this file is the modifed version of the previous test_operations.py. 
Now we are testing the methods of the Operations class using parametrized tests.
"""
import pytest
from typing import Union
from app.operations import Operations

Number = Union[int, float]

# ---------------------------------------------
# Unit Tests for the 'addition' Method
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (0, 0, 0),           # Test adding two zeros
        (-1, 1, 0),          # Test adding a negative and a positive integer
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]
)

def test_addition(a: Number, b: Number, expected: Number) -> None:
    """
    Verifies the Operations.addition method with various numeric inputs,
    ensuring it correctly calculates the sum.
    """
    # Create an instance of the Operations class
    
    # Call the 'addition' method with the provided arguments
    result = Operations.addition(a, b)
    
    # Assert that the result of addition(a, b) matches the expected value
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtraction' Method
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (0, 0, 0),           # Test subtracting two zeros
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (10.5, 5.5, 5.0),    # Test subtracting two positive floats
        (-10.5, -5.5, -5.0), # Test subtracting two negative floats
    ],
    ids=[
        "subtract_smaller_positive_integer_from_larger",
        "subtract_two_zeros",
        "subtract_negative_integer_from_negative_integer",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    
    """
    Verifies the Operations.subtraction method with various numeric inputs,
    ensuring it correctly calculates the difference.
    """
    # Create an instance of the Operations class
    
    # Call the 'subtraction' method with the provided arguments
    result = Operations.subtraction(a, b)
    
    # Assert that the result of subtraction(a, b) matches the expected value
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"



# ---------------------------------------------
# Unit Tests for the 'multiplication' Method
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (0, 10, 0),          # Test multiplying zero with a positive integer
        (-2, -3, 6),         # Test multiplying two negative integers
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_zero_with_positive_integer",
        "multiply_two_negative_integers",
        "multiply_two_positive_floats",
        "multiply_negative_float_with_positive_float",
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    
    """
    Verifies the Operations.multiplication method with various numeric inputs,
    ensuring it correctly calculates the product.
    """

    # Call the 'multiplication' method with the provided arguments
    result = Operations.multiplication(a, b)
    
    # Assert that the result of multiplication(a, b) matches the expected value
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"



# ---------------------------------------------
# Unit Tests for the 'division' Method
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, -3, 2.0),         # Test dividing two negative integers
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_division(a: Number, b: Number, expected: float) -> None:
    
    """
    Verifies the Operations.division method with valid numeric inputs,
    ensuring it correctly calculates the quotient.
    """
    # Call the 'division' method with the provided arguments
    result = Operations.division(a, b)
    
    # Assert that the result of division(a, b) matches the expected value
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"



# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),    # Test dividing by zero with positive dividend
        (-1, 0),   # Test dividing by zero with negative dividend
        (0, 0),    # Test dividing zero by zero
    ],
    ids=[
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero",
    ]
)
def test_division_by_zero(a: Number, b: Number) -> None:
    
    """
    Ensures that the Operations.division method raises a ValueError
    when attempting to divide by zero.
    """
    
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        # Attempt to divide 'a' by 'b', which should raise a ValueError
        Operations.division(a, b)
    
    # Assert that the exception message contains the expected error message
    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got '{excinfo.value}'"



# import pytest
# from app.operations import addition, division, subtraction, multiplication

# def test_addition_positive():
#     assert addition(1,1) == 2
#     assert addition(6,4) == 10
#     assert addition(-10,5) == -5

# def test_addition_negative():
#     assert addition(-6,-4) == -10
#     assert addition(-10,-5) == -15

# def test_subtraction_positive():
#     assert subtraction(1,1) == 0
#     assert subtraction(5,3) == 2
#     assert subtraction(6,4) == 2

# def test_subtraction_negative():
#     assert subtraction(-1,-1) == 0
#     assert subtraction(-5,-3) == -2

# def test_multiplication_positive():
#     assert multiplication(2,3) == 6
#     assert multiplication(6,4) == 24
#     assert multiplication(-10,5) == -50

# def test_multiplication_negative():
#     assert multiplication(-2,-3) == 6
#     assert multiplication(-1,-1) == 1

# def test_division_positive():
#     assert division(1,1) == 1
#     assert division(6,3) == 2

# def test_division_negative():
#     assert division(-6,-3) == 2
#     assert division(-1,-1) == 1
    
# def test_division_by_zero():
#     """Test division by zero."""
#     with pytest.raises(ValueError, match="Division by zero is not allowed."):
#         division(1, 0)

"""
Test suite for calc.py calculator module
"""
import pytest
import sys
import os

# -------------------------------------------------------------------------
# CRITICAL FIX: Add 'src' directory to sys.path so we can import calc.py
# -------------------------------------------------------------------------
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# ✅ Import exactly what is inside your calc.py
from calc import add, subtract, multiply, divide, power

class TestAddition:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 5) == 15

class TestSubtraction:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 3) == 7

class TestMultiplication:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

class TestDivision:
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
        
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

class TestPower:
    """Test cases for the new power function"""
    def test_power_positive(self):
        # This will FAIL because your code uses ^ (XOR) instead of ** (Power)
        assert power(2, 3) == 8
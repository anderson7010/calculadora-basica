import pytest
from pytest import approx
from src.calculator import add, subtract, multiply, divide


class TestAddOperation:
    """Tests para la operación de suma."""
    
    def test_should_add_two_positive_numbers(self):
        result = add(5.0, 3.0)
        assert result == approx(8.0)
    
    def test_should_add_positive_and_negative_numbers(self):
        result = add(10.0, -3.0)
        assert result == approx(7.0)
    
    def test_should_add_two_negative_numbers(self):
        result = add(-5.0, -3.0)
        assert result == approx(-8.0)
    
    def test_should_add_zero_to_number(self):
        result = add(42.0, 0.0)
        assert result == approx(42.0)
    
    def test_should_add_decimal_numbers(self):
        result = add(1.5, 2.7)
        assert result == approx(4.2)
    
    def test_should_add_very_large_numbers(self):
        result = add(1e10, 2e10)
        assert result == approx(3e10)
    
    def test_should_add_very_small_numbers(self):
        result = add(1e-10, 2e-10)
        assert result == approx(3e-10)


class TestSubtractOperation:
    """Tests para la operación de resta."""
    
    def test_should_subtract_smaller_from_larger_number(self):
        result = subtract(10.0, 3.0)
        assert result == approx(7.0)
    
    def test_should_subtract_larger_from_smaller_number(self):
        result = subtract(3.0, 10.0)
        assert result == approx(-7.0)
    
    def test_should_subtract_negative_number(self):
        result = subtract(5.0, -3.0)
        assert result == approx(8.0)
    
    def test_should_subtract_zero_from_number(self):
        result = subtract(42.0, 0.0)
        assert result == approx(42.0)
    
    def test_should_subtract_number_from_zero(self):
        result = subtract(0.0, 42.0)
        assert result == approx(-42.0)
    
    def test_should_subtract_same_numbers(self):
        result = subtract(15.5, 15.5)
        assert result == approx(0.0)
    
    def test_should_subtract_decimal_numbers(self):
        result = subtract(5.7, 2.3)
        assert result == approx(3.4)


class TestMultiplyOperation:
    """Tests para la operación de multiplicación."""
    
    def test_should_multiply_two_positive_numbers(self):
        result = multiply(4.0, 5.0)
        assert result == approx(20.0)
    
    def test_should_multiply_positive_and_negative_numbers(self):
        result = multiply(6.0, -3.0)
        assert result == approx(-18.0)
    
    def test_should_multiply_two_negative_numbers(self):
        result = multiply(-4.0, -5.0)
        assert result == approx(20.0)
    
    def test_should_multiply_by_zero(self):
        result = multiply(42.0, 0.0)
        assert result == approx(0.0)
    
    def test_should_multiply_zero_by_number(self):
        result = multiply(0.0, 42.0)
        assert result == approx(0.0)
    
    def test_should_multiply_by_one(self):
        result = multiply(42.0, 1.0)
        assert result == approx(42.0)
    
    def test_should_multiply_decimal_numbers(self):
        result = multiply(2.5, 4.0)
        assert result == approx(10.0)
    
    def test_should_multiply_very_small_numbers(self):
        result = multiply(0.001, 0.002)
        assert result == approx(0.000002)
    
    def test_should_multiply_large_numbers(self):
        result = multiply(1e6, 2e6)
        assert result == approx(2e12)


class TestDivideOperation:
    """Tests para la operación de división."""
    
    def test_should_divide_positive_numbers(self):
        result = divide(10.0, 2.0)
        assert result == approx(5.0)
    
    def test_should_divide_negative_by_positive(self):
        result = divide(-10.0, 2.0)
        assert result == approx(-5.0)
    
    def test_should_divide_positive_by_negative(self):
        result = divide(10.0, -2.0)
        assert result == approx(-5.0)
    
    def test_should_divide_negative_by_negative(self):
        result = divide(-10.0, -2.0)
        assert result == approx(5.0)
    
    def test_should_divide_zero_by_number(self):
        result = divide(0.0, 5.0)
        assert result == approx(0.0)
    
    def test_should_divide_decimal_numbers(self):
        result = divide(7.5, 2.5)
        assert result == approx(3.0)
    
    def test_should_divide_resulting_in_decimal(self):
        result = divide(1.0, 3.0)
        assert result == approx(0.3333333333333333)
    
    def test_should_divide_large_numbers(self):
        result = divide(1e12, 1e6)
        assert result == approx(1e6)
    
    def test_should_raise_error_when_dividing_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10.0, 0.0)
    
    def test_should_raise_error_when_dividing_negative_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(-10.0, 0.0)
    
    def test_should_raise_error_when_dividing_zero_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0.0, 0.0)
import pytest
from pydantic import ValidationError
from src.models import CalculationRequest, CalculationResponse, ErrorResponse


class TestCalculationRequest:
    """Tests para el modelo CalculationRequest."""
    
    def test_should_create_valid_calculation_request_with_add_operation(self):
        request = CalculationRequest(operation="add", a=5.0, b=3.0)
        assert request.operation == "add"
        assert request.a == 5.0
        assert request.b == 3.0
    
    def test_should_create_valid_calculation_request_with_subtract_operation(self):
        request = CalculationRequest(operation="subtract", a=10.0, b=7.0)
        assert request.operation == "subtract"
        assert request.a == 10.0
        assert request.b == 7.0
    
    def test_should_create_valid_calculation_request_with_multiply_operation(self):
        request = CalculationRequest(operation="multiply", a=4.0, b=6.0)
        assert request.operation == "multiply"
        assert request.a == 4.0
        assert request.b == 6.0
    
    def test_should_create_valid_calculation_request_with_divide_operation(self):
        request = CalculationRequest(operation="divide", a=12.0, b=3.0)
        assert request.operation == "divide"
        assert request.a == 12.0
        assert request.b == 3.0
    
    def test_should_accept_negative_numbers(self):
        request = CalculationRequest(operation="add", a=-5.0, b=-3.0)
        assert request.a == -5.0
        assert request.b == -3.0
    
    def test_should_accept_zero_values(self):
        request = CalculationRequest(operation="multiply", a=0.0, b=42.0)
        assert request.a == 0.0
        assert request.b == 42.0
    
    def test_should_accept_decimal_numbers(self):
        request = CalculationRequest(operation="add", a=1.5, b=2.7)
        assert request.a == 1.5
        assert request.b == 2.7
    
    def test_should_convert_integers_to_floats(self):
        request = CalculationRequest(operation="add", a=5, b=3)
        assert request.a == 5.0
        assert request.b == 3.0
        assert isinstance(request.a, float)
        assert isinstance(request.b, float)
    
    def test_should_accept_very_large_numbers(self):
        request = CalculationRequest(operation="add", a=1e15, b=2e15)
        assert request.a == 1e15
        assert request.b == 2e15
    
    def test_should_accept_very_small_numbers(self):
        request = CalculationRequest(operation="multiply", a=1e-10, b=2e-10)
        assert request.a == 1e-10
        assert request.b == 2e-10
    
    def test_should_reject_missing_operation_field(self):
        with pytest.raises(ValidationError):
            CalculationRequest(a=5.0, b=3.0)
    
    def test_should_reject_missing_operand_a(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation="add", b=3.0)
    
    def test_should_reject_missing_operand_b(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation="add", a=5.0)
    
    def test_should_reject_invalid_operation_type(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation=123, a=5.0, b=3.0)
    
    def test_should_reject_invalid_operand_a_type(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation="add", a="not_a_number", b=3.0)
    
    def test_should_reject_invalid_operand_b_type(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation="add", a=5.0, b="not_a_number")
    
    def test_should_reject_null_operation(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation=None, a=5.0, b=3.0)
    
    def test_should_reject_null_operand_a(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation="add", a=None, b=3.0)
    
    def test_should_reject_null_operand_b(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation="add", a=5.0, b=None)
    
    def test_should_reject_empty_operation_string(self):
        with pytest.raises(ValidationError):
            CalculationRequest(operation="", a=5.0, b=3.0)


class TestCalculationResponse:
    """Tests para el modelo CalculationResponse."""
    
    def test_should_create_valid_calculation_response(self):
        response = CalculationResponse(result=8.0, operation="add")
        assert response.result == 8.0
        assert response.operation == "add"
    
    def test_should_accept_negative_result(self):
        response = CalculationResponse(result=-5.0, operation="subtract")
        assert response.result == -5.0
    
    def test_should_accept_zero_result(self):
        response = CalculationResponse(result=0.0, operation="multiply")
        assert response.result == 0.0
    
    def test_should_accept_decimal_result(self):
        response = CalculationResponse(result=3.14159, operation="divide")
        assert response.result == 3.14159
    
    def test_should_convert_integer_result_to_float(self):
        response = CalculationResponse(result=42, operation="add")
        assert response.result == 42.0
        assert isinstance(response.result, float)
    
    def test_should_accept_very_large_result(self):
        response = CalculationResponse(result=1e15, operation="multiply")
        assert response.result == 1e15
    
    def test_should_accept_very_small_result(self):
        response = CalculationResponse(result=1e-15, operation="divide")
        assert response.result == 1e-15
    
    def test_should_reject_missing_result_field(self):
        with pytest.raises(ValidationError):
            CalculationResponse(operation="add")
    
    def test_should_reject_missing_operation_field(self):
        with pytest.raises(ValidationError):
            CalculationResponse(result=8.0)
    
    def test_should_reject_invalid_result_type(self):
        with pytest.raises(ValidationError):
            CalculationResponse(result="not_a_number", operation="add")
    
    def test_should_reject_invalid_operation_type(self):
        with pytest.raises(ValidationError):
            CalculationResponse(result=8.0, operation=123)
    
    def test_should_reject_null_result(self):
        with pytest.raises(ValidationError):
            CalculationResponse(result=None, operation="add")
    
    def test_should_reject_null_operation(self):
        with pytest.raises(ValidationError):
            CalculationResponse(result=8.0, operation=None)
    
    def test_should_reject_empty_operation_string(self):
        with pytest.raises(ValidationError):
            CalculationResponse(result=8.0, operation="")


class TestErrorResponse:
    """Tests para el modelo ErrorResponse."""
    
    def test_should_create_valid_error_response(self):
        error = ErrorResponse(detail="Cannot divide by zero")
        assert error.detail == "Cannot divide by zero"
    
    def test_should_accept_empty_detail_message(self):
        error = ErrorResponse(detail="")
        assert error.detail == ""
    
    def test_should_accept_long_detail_message(self):
        long_message = "This is a very long error message " * 10
        error = ErrorResponse(detail=long_message)
        assert error.detail == long_message
    
    def test_should_reject_missing_detail_field(self):
        with pytest.raises(ValidationError):
            ErrorResponse()
    
    def test_should_reject_invalid_detail_type(self):
        with pytest.raises(ValidationError):
            ErrorResponse(detail=123)
    
    def test_should_reject_null_detail(self):
        with pytest.raises(ValidationError):
            ErrorResponse(detail=None)
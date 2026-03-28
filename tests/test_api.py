import pytest
from fastapi.testclient import TestClient
from pytest import approx


class TestCalculateEndpoint:
    """Tests para el endpoint POST /calculate."""
    
    def test_should_perform_addition_operation(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "a": 5.0,
            "b": 3.0
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(8.0)
        assert data["operation"] == "add"
    
    def test_should_perform_subtraction_operation(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "subtract",
            "a": 10.0,
            "b": 3.0
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(7.0)
        assert data["operation"] == "subtract"
    
    def test_should_perform_multiplication_operation(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "multiply",
            "a": 4.0,
            "b": 5.0
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(20.0)
        assert data["operation"] == "multiply"
    
    def test_should_perform_division_operation(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "divide",
            "a": 10.0,
            "b": 2.0
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(5.0)
        assert data["operation"] == "divide"
    
    def test_should_handle_negative_numbers_in_addition(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "a": -5.0,
            "b": 3.0
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(-2.0)
    
    def test_should_handle_decimal_numbers(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "multiply",
            "a": 2.5,
            "b": 4.2
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(10.5)
    
    def test_should_handle_zero_values(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "a": 0.0,
            "b": 42.0
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(42.0)
    
    def test_should_return_400_for_division_by_zero(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "divide",
            "a": 10.0,
            "b": 0.0
        })
        assert response.status_code == 400, response.text
        data = response.json()
        assert "detail" in data
        assert "Cannot divide by zero" in data["detail"]
    
    def test_should_return_400_for_invalid_operation(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "power",
            "a": 2.0,
            "b": 3.0
        })
        assert response.status_code == 400, response.text
        data = response.json()
        assert "detail" in data
        assert "Invalid operation" in data["detail"]
    
    def test_should_return_422_for_missing_operation_field(self, client: TestClient):
        response = client.post("/calculate", json={
            "a": 5.0,
            "b": 3.0
        })
        assert response.status_code == 422, response.text
    
    def test_should_return_422_for_missing_operand_a(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "b": 3.0
        })
        assert response.status_code == 422, response.text
    
    def test_should_return_422_for_missing_operand_b(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "a": 5.0
        })
        assert response.status_code == 422, response.text
    
    def test_should_return_422_for_invalid_number_type_in_a(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "a": "not_a_number",
            "b": 3.0
        })
        assert response.status_code == 422, response.text
    
    def test_should_return_422_for_invalid_number_type_in_b(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "a": 5.0,
            "b": "not_a_number"
        })
        assert response.status_code == 422, response.text
    
    def test_should_return_422_for_empty_request_body(self, client: TestClient):
        response = client.post("/calculate", json={})
        assert response.status_code == 422, response.text
    
    def test_should_return_422_for_null_values(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "a": None,
            "b": 3.0
        })
        assert response.status_code == 422, response.text
    
    def test_should_handle_very_large_numbers(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "add",
            "a": 1e15,
            "b": 2e15
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(3e15)
    
    def test_should_handle_very_small_numbers(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "multiply",
            "a": 1e-10,
            "b": 2e-10
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(2e-20)
    
    def test_should_handle_integer_inputs_as_floats(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "divide",
            "a": 15,
            "b": 3
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(5.0)
    
    def test_should_return_precise_division_result(self, client: TestClient):
        response = client.post("/calculate", json={
            "operation": "divide",
            "a": 1.0,
            "b": 3.0
        })
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["result"] == approx(0.3333333333333333)
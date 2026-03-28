"""Definición de endpoints FastAPI para la calculadora.

Este módulo define los endpoints de la API REST para realizar operaciones
aritméticas básicas. Maneja la validación de entrada, el procesamiento
de operaciones y el manejo de errores.
"""

from fastapi import APIRouter, HTTPException
from src.models import CalculationRequest, CalculationResponse
from src import calculator

router = APIRouter()

# Mapeo de operaciones a funciones
OPERATIONS = {
    "add": calculator.add,
    "subtract": calculator.subtract,
    "multiply": calculator.multiply,
    "divide": calculator.divide
}


@router.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest) -> CalculationResponse:
    """Realiza una operación aritmética.
    
    Args:
        request: Petición con la operación y operandos
        
    Returns:
        Respuesta con el resultado de la operación
        
    Raises:
        HTTPException: Si la operación es inválida o hay división por cero
        
    Examples:
        POST /calculate
        {
            "operation": "add",
            "a": 5.0,
            "b": 3.0
        }
        
        Response:
        {
            "result": 8.0,
            "operation": "add"
        }
    """
    # Validar que la operación sea válida
    if request.operation not in OPERATIONS:
        valid_operations = ", ".join(OPERATIONS.keys())
        raise HTTPException(
            status_code=400,
            detail=f"Invalid operation '{request.operation}'. Valid operations are: {valid_operations}"
        )
    
    # Obtener la función de operación
    operation_func = OPERATIONS[request.operation]
    
    try:
        # Realizar la operación
        result = operation_func(request.a, request.b)
        
        # Retornar la respuesta
        return CalculationResponse(
            result=result,
            operation=request.operation
        )
    
    except ValueError as e:
        # Manejar errores de división por cero
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
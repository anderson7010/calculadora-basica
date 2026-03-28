"""Modelos Pydantic para validación de requests y responses.

Este módulo define los modelos de datos utilizados por la API de calculadora
para validar las peticiones entrantes y estructurar las respuestas.
"""

from pydantic import BaseModel, Field
from typing import Union


class CalculationRequest(BaseModel):
    """Modelo para las peticiones de cálculo.
    
    Attributes:
        operation: Tipo de operación a realizar (add, subtract, multiply, divide)
        a: Primer operando
        b: Segundo operando
    """
    operation: str = Field(..., min_length=1, description="Operación a realizar")
    a: float = Field(..., description="Primer operando")
    b: float = Field(..., description="Segundo operando")


class CalculationResponse(BaseModel):
    """Modelo para las respuestas de cálculo exitosas.
    
    Attributes:
        result: Resultado de la operación matemática
        operation: Operación que se realizó
    """
    result: float = Field(..., description="Resultado de la operación")
    operation: str = Field(..., min_length=1, description="Operación realizada")


class ErrorResponse(BaseModel):
    """Modelo para las respuestas de error.
    
    Attributes:
        detail: Mensaje descriptivo del error
    """
    detail: str = Field(..., description="Mensaje de error")
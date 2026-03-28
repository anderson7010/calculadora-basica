"""Módulo con funciones puras para operaciones matemáticas básicas.

Este módulo proporciona las operaciones aritméticas fundamentales:
suma, resta, multiplicación y división. Todas las funciones son puras
y no tienen efectos secundarios.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> float:
    """Suma dos números.
    
    Args:
        a: Primer operando
        b: Segundo operando
        
    Returns:
        La suma de a y b como float
        
    Examples:
        >>> add(5.0, 3.0)
        8.0
        >>> add(-2.5, 1.5)
        -1.0
    """
    return float(a + b)


def subtract(a: Number, b: Number) -> float:
    """Resta el segundo número del primero.
    
    Args:
        a: Minuendo (número del cual se resta)
        b: Sustraendo (número que se resta)
        
    Returns:
        La diferencia de a - b como float
        
    Examples:
        >>> subtract(10.0, 3.0)
        7.0
        >>> subtract(5.0, -2.0)
        7.0
    """
    return float(a - b)


def multiply(a: Number, b: Number) -> float:
    """Multiplica dos números.
    
    Args:
        a: Primer factor
        b: Segundo factor
        
    Returns:
        El producto de a * b como float
        
    Examples:
        >>> multiply(4.0, 5.0)
        20.0
        >>> multiply(-3.0, 2.0)
        -6.0
    """
    return float(a * b)


def divide(a: Number, b: Number) -> float:
    """Divide el primer número por el segundo.
    
    Args:
        a: Dividendo (número que se divide)
        b: Divisor (número por el cual se divide)
        
    Returns:
        El cociente de a / b como float
        
    Raises:
        ValueError: Si b es cero (división por cero)
        
    Examples:
        >>> divide(10.0, 2.0)
        5.0
        >>> divide(1.0, 3.0)
        0.3333333333333333
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a / b)
"""Punto de entrada de la aplicación FastAPI.

Este módulo configura y ejecuta la aplicación de calculadora básica.
Define la instancia principal de FastAPI y registra los routers de la API.
"""

from fastapi import FastAPI
from src.api import router

# Crear la instancia principal de FastAPI
app = FastAPI(
    title="Calculadora Básica",
    description="API REST para operaciones aritméticas básicas (suma, resta, multiplicación, división)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Registrar el router de la API
app.include_router(router)

# Endpoint de salud para verificar que la aplicación esté funcionando
@app.get("/health")
def health_check() -> dict[str, str]:
    """Endpoint de verificación de salud de la aplicación.
    
    Returns:
        Diccionario con el estado de la aplicación
    """
    return {"status": "healthy", "service": "calculator-api"}


if __name__ == "__main__":
    import uvicorn
    
    # Configuración para desarrollo local
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
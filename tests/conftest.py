import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """Fixture que proporciona un cliente de prueba para FastAPI."""
    return TestClient(app)
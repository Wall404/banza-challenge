import pytest
from fastapi.testclient import TestClient
from debug_app import app  # assuming your FastAPI app is defined in a file called main.py

# Create a test client for the FastAPI app
client = TestClient(app)

def test_create_cliente():
    # Define a test payload
    payload = {
        "nombre": "John Doe"
    }

    # Make a POST request to the create_cliente endpoint
    response = client.post("/clientes", json=payload)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON contains the expected keys
    assert "id" in response.json()
    assert "nombre" in response.json()

    # Assert that the response JSON values match the payload
    assert response.json()["nombre"] == payload["nombre"]

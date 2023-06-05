from fastapi.testclient import TestClient
from sqlalchemy import delete
from debug_app import app
from config.db import SessionLocal
from models.cliente import Cliente as ClienteModel
from models.categoria import Categoria as CategoriaModel

client = TestClient(app)

def test_get_clientes():
    response = client.get("/clientes")
    assert response.status_code == 200
    assert response.json() == []


def test_create_cliente():
    cliente_data = {
        "nombre": "John Doe"
    }
    response = client.post("/clientes", json=cliente_data)
    assert response.status_code == 200
    cliente = response.json()
    assert cliente["nombre"] == "John Doe"
    assert cliente["id"] is not None


def test_get_cliente():
    response = client.get("/clientes/1")
    assert response.status_code == 404


def test_update_cliente():
    cliente_data = {
        "nombre": "John Doe Updated"
    }
    response = client.put("/clientes/1", json=cliente_data)
    assert response.status_code == 404


def test_delete_cliente():
    response = client.delete("/clientes/1")
    assert response.status_code == 404


def test_get_cliente_cuentas():
    response = client.get("/clientes/1/cuentas")
    assert response.status_code == 404


def test_get_cliente_categorias():
    response = client.get("/clientes/1/categorias")
    assert response.status_code == 404


def test_add_categoria_to_cliente():
    response = client.post("/clientes/1/categorias/1")
    assert response.status_code == 404


def test_get_cliente_saldo_cuentas():
    response = client.get("/clientes/1/saldo-cuentas")
    assert response.status_code == 404

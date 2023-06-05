from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from debug_app import app
from config.db import Base, engine, get_db
from schemas.movimiento import Movimiento
from models.movimiento import Movimiento as MovimientoModel

def override_get_db():
    try:
        db = Session(bind=engine)
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_movimiento():
    movimiento_data = {
        "id_cuenta": 1,
        "nombre": "Pago",
        "tipo": "egreso",
        "importe": "100.0",
        "fecha": "2023-06-04T12:00:00",
    }
    response = client.post("/movimientos", json=movimiento_data)
    assert response.status_code == 200
    assert response.json()["id_cuenta"] == movimiento_data["id_cuenta"]
    assert response.json()["nombre"] == movimiento_data["nombre"]
    assert response.json()["tipo"] == movimiento_data["tipo"]
    assert response.json()["importe"] == movimiento_data["importe"]
    assert response.json()["fecha"] == movimiento_data["fecha"]

def test_get_movimientos():
    response = client.get("/movimientos")
    assert response.status_code == 200
    movimientos = response.json()
    assert isinstance(movimientos, list)

def test_get_movimiento():
    movimiento_id = 2
    response = client.get(f"/movimientos/{movimiento_id}")
    assert response.status_code == 200
    movimiento = response.json()
    assert movimiento["id"] == movimiento_id

def test_delete_movimiento():
    movimiento_id = 2
    response = client.delete(f"/movimientos/{movimiento_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Movimiento deleted"

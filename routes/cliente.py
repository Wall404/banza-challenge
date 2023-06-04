from typing import List
from fastapi import APIRouter
from sqlalchemy import select
from schemas.cliente import Cliente
from models.cliente import clientes
from config.db import conn
# from starlette.status import HTTP_200, HTTP_201, HTTP_204_NO_CONTENT, HTTP_400, HTTP_404

cliente = APIRouter()


@cliente.get("/clientes", tags=["clientes"], response_model=List[Cliente])
def get_clientes():
    return conn.execute(clientes.select()).fetchall()


@cliente.post("/clientes", tags=["clientes"])
def create_cliente(cliente: Cliente):
    new_cliente = {"nombre": cliente.nombre}
    result = conn.execute(clientes.insert(), new_cliente)
    return conn.execute(clientes.select().where(clientes.c.id == result.lastrowid)).first()


@cliente.get("/clientes/{id}", tags=["clientes"], response_model=Cliente)
def get_cliente(id: str):
    return conn.execute(clientes.select().where(clientes.c.id == id)).first()


@cliente.delete("/clientes/{id}", tags=["clientes"])
def delete_cliente():
    result = conn.execute(clientes.delete().where(clientes.c.id == id))
    return conn.execute(clientes.select().where(clientes.c.id == id)).first()


# @cliente.get("/clientes")
# def helloworld():
#     return "hello world"

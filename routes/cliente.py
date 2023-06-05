from typing import List
from fastapi import APIRouter
from config.db import conn
from schemas.cliente import Cliente
from models.cliente import clientes
from sqlalchemy import select, func

cliente = APIRouter()


@cliente.get("/clientes", tags=["clientes"], response_model=List[Cliente])
def get_clientes():
    lista_clientes = conn.execute(clientes.select()).fetchall()
    return lista_clientes


@cliente.post("/clientes", tags=["clientes"], response_model=Cliente)
def create_cliente(cliente: Cliente):
    new_cliente = {"nombre": cliente.nombre}
    result = conn.execute(clientes.insert().values(new_cliente))
    conn.commit()
    return conn.execute(clientes.select().where(clientes.c.id == result.lastrowid)).first()


@cliente.get("/clientes/{id}", tags=["clientes"], response_model=Cliente)
def get_cliente(id: int):
    return conn.execute(clientes.select().where(clientes.c.id == id)).first()


@cliente.delete("/clientes/{id}", tags=["clientes"])
def delete_cliente(id: int):
    result = conn.execute(clientes.delete().where(clientes.c.id == id))
    conn.commit()
    return conn.execute(clientes.select().where(clientes.c.id == id)).first()

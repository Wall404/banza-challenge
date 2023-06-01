from fastapi import APIRouter, Response
from cryptography.fernet import Fernet
from config.db import conn
from models.cliente import clientes
from schemas.cliente import Cliente
# from starlette.status import HTTP_200, HTTP_201, HTTP_204_NO_CONTENT, HTTP_400, HTTP_404


# key = Fernet.generate_key()
# f = Fernet(key)

cliente = APIRouter()


# @cliente.get("/clientes", status_code=status.HTTP_200_OK)
# def get_clientes():
#     return conn.execute(clientes.select()).fetchall()


@cliente.post("/clientes")
def create_cliente(cliente: Cliente):
    new_cliente = {"nombre": Cliente.nombre}
    result = conn.execute(clientes.insert(), new_cliente)
    return conn.execute(clientes.select().where(clientes.c.id == result.lastrowid)).first()


@cliente.get("/clientes/{id}")
def get_cliente(id: str):
    return conn.execute(clientes.select().where(clientes.c.id == id)).first()


@cliente.delete("/clientes/{id}")
def delete_cliente():
    result = conn.execute(clientes.delete().where(clientes.c.id == id))
    return Response(status_code=204)


@cliente.get("/clientes")
def helloworld():
    return "hello world"

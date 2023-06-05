from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.cliente import Cliente
from schemas.categoria import Categoria
from schemas.cuenta import Cuenta
from config.db import get_db
from models.cliente import Cliente as ClienteModel
from models.categoria import Categoria as CategoriaModel
from models.cuenta import Cuenta as CuentaModel

cliente_router = APIRouter()


@cliente_router.get("/clientes", tags=["clientes"], response_model=List[Cliente])
def get_clientes(db: Session = Depends(get_db)):
    clientes = db.query(ClienteModel).all()
    return clientes


@cliente_router.post("/clientes", tags=["clientes"], response_model=Cliente)
def create_cliente(cliente: Cliente, db: Session = Depends(get_db)):
    new_cliente = ClienteModel(nombre=cliente.nombre)
    db.add(new_cliente)
    db.commit()
    db.refresh(new_cliente)
    return new_cliente


@cliente_router.put("/clientes/{cliente_id}", tags=["clientes"], response_model=Cliente)
def update_cliente(cliente_id: int, cliente: Cliente, db: Session = Depends(get_db)):
    existing_cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not existing_cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    existing_cliente.nombre = cliente.nombre
    db.commit()
    db.refresh(existing_cliente)
    return existing_cliente


@cliente_router.delete("/clientes/{cliente_id}", tags=["clientes"])
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    existing_cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not existing_cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    db.delete(existing_cliente)
    db.commit()
    return {"message": "Cliente deleted"}


@cliente_router.get("/clientes/{cliente_id}", tags=["clientes"], response_model=Cliente)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return cliente


@cliente_router.get("/clientes/{cliente_id}/cuentas", tags=["clientes"], response_model=List[Cuenta])
def get_cliente_cuentas(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    cuentas = db.query(CuentaModel).filter(CuentaModel.cliente_id == cliente_id).all()
    return cuentas


@cliente_router.get("/clientes/{cliente_id}/categorias", tags=["clientes"], response_model=list[Categoria])
def get_cliente_categorias(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")

    categorias = db.query(CategoriaModel).join(ClienteModel.categorias).filter(ClienteModel.id == cliente_id).all()
    return categorias

@cliente_router.post("/clientes/{cliente_id}/categorias/{categoria_id}", tags=["clientes"], response_model=Categoria)
def add_categoria_to_cliente(cliente_id: int, categoria_id: int, db: Session = Depends(get_db)):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    categoria = db.query(CategoriaModel).filter(CategoriaModel.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")

    cliente.categorias.append(categoria)
    db.commit()

    return categoria



@cliente_router.get("/clientes/{cliente_id}/saldo-cuentas", tags=["clientes"])
def get_cliente_saldo_cuentas(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    cuentas = db.query(CuentaModel).filter(CuentaModel.cliente_id == cliente_id).all()
    saldo_cuentas = {}
    for cuenta in cuentas:
        cuenta_schema = Cuenta.from_orm(cuenta)
        saldo_cuentas[cuenta_schema.nombre] = cuenta_schema.get_total_usd()  # Utiliza el método get_total_usd() de la clase Cuenta
    return saldo_cuentas

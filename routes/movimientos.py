from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.movimiento import Movimiento
from config.db import get_db
from models.movimiento import Movimiento as MovimientoModel

movimiento_router = APIRouter()


@movimiento_router.post("/movimientos", tags=["movimientos"], response_model=Movimiento)
def create_movimiento(movimiento: Movimiento, db: Session = Depends(get_db)):
    new_movimiento = MovimientoModel(**movimiento.dict())
    db.add(new_movimiento)
    db.commit()
    db.refresh(new_movimiento)
    return new_movimiento


@movimiento_router.get("/movimientos", tags=["movimientos"], response_model=List[Movimiento])
def get_movimientos(db: Session = Depends(get_db)):
    movimientos = db.query(MovimientoModel).all()
    return movimientos


@movimiento_router.get("/movimientos/{movimiento_id}", tags=["movimientos"], response_model=Movimiento)
def get_movimiento(movimiento_id: int, db: Session = Depends(get_db)):
    movimiento = db.query(MovimientoModel).filter(MovimientoModel.id == movimiento_id).first()
    if not movimiento:
        raise HTTPException(status_code=404, detail="Movimiento not found")
    return movimiento


@movimiento_router.delete("/movimientos/{movimiento_id}", tags=["movimientos"])
def delete_movimiento(movimiento_id: int, db: Session = Depends(get_db)):
    movimiento = db.query(MovimientoModel).filter(MovimientoModel.id == movimiento_id).first()
    if not movimiento:
        raise HTTPException(status_code=404, detail="Movimiento not found")
    db.delete(movimiento)
    db.commit()
    return {"message": "Movimiento deleted"}

import datetime
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base

class Movimiento(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cuenta = Column(Integer, ForeignKey("cuentas.id"))
    nombre = Column(String(255))
    tipo = Column(Enum("ingreso", "egreso"))
    importe = Column(Float)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)

    cuenta = relationship("Cuenta", back_populates="movimientos")


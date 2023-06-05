from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Cuenta(Base):
    __tablename__ = "cuentas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente", back_populates="cuentas")
    movimientos = relationship("Movimiento", back_populates="cuenta")

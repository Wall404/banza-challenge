from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

cliente_categoria = Table(
    "cliente_categoria",
    Base.metadata,
    Column("cliente_id", Integer, ForeignKey("clientes.id"), primary_key=True),
    Column("categoria_id", Integer, ForeignKey("categorias.id"), primary_key=True),
)

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))

    cuentas = relationship("Cuenta", back_populates="cliente")
    categorias = relationship("Categoria", secondary=cliente_categoria, back_populates="clientes", cascade="all, delete")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))

    clientes = relationship("Cliente", secondary="cliente_categoria")


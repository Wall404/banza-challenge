import datetime
from typing import Optional
from pydantic import BaseModel

class Movimiento(BaseModel):
    id: int
    id_cuenta: int
    nombre: str
    tipo: str
    importe: str
    fecha: datetime

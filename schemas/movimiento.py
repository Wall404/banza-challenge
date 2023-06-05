import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field

class Movimiento(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_cuenta: int
    nombre: str
    tipo: Literal['ingreso', 'egreso']
    importe: str
    fecha: datetime.datetime

    class Config:
        orm_mode = True


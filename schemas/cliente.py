from typing import Optional
from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nombre: str

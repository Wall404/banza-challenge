from typing import Optional
from pydantic import BaseModel

class Categoria(BaseModel):
    id: int
    nombre: str

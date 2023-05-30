from typing import Optional
from pydantic import BaseModel

class Cuenta(BaseModel):
    id: int
    nombre: str

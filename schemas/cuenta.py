from typing import Optional
from pydantic import BaseModel, Field

class Cuenta(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str

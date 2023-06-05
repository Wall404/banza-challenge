from typing import Optional
from pydantic import BaseModel, Field

class Categoria(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str

    class Config:
        orm_mode = True
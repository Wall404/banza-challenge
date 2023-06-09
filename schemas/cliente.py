from typing import Optional
from pydantic import BaseModel, Field


class Cliente(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(default="")

    class Config:
        orm_mode = True

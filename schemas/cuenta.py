from typing import Optional

import requests
from pydantic import BaseModel, Field


class Cuenta(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    saldo: float = Field(default=0.0)

    class Config:
        orm_mode = True

    def get_total_usd(self):
        url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
        response = requests.get(url)
        data = response.json()
        dolar_bolsa = None

        for item in data:
            if item.get("casa", {}).get("nombre") == "Dolar Bolsa":
                dolar_bolsa_str = item.get("casa", {}).get("venta")
                dolar_bolsa_str = dolar_bolsa_str.replace(",", "")
                dolar_bolsa = float(dolar_bolsa_str)
                break

        if dolar_bolsa is None:
            raise Exception("No se pudo obtener la cotización del Dolar Bolsa")

        total_usd = self.saldo / dolar_bolsa
        return total_usd

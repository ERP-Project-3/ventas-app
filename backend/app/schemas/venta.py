from pydantic import BaseModel
from datetime import date
from typing import Literal

class VentaCreate(BaseModel):
    cliente: str
    monto: float
    fecha: date
    metodo_pago: Literal["contado", "credito"]

class VentaOut(VentaCreate):
    id: int

    class Config:
        orm_mode = True

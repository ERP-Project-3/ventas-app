from datetime import date

from pydantic import BaseModel


class VentaBase(BaseModel):
    cliente: str
    monto: float
    fecha: date
    metodo_pago: str


class VentaCreate(VentaBase):
    pass


class VentaOut(VentaBase):
    id: int
    organization_id: int

    class Config:
        from_attributes = True

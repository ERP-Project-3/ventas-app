from app.models.venta import Venta
from app.schemas.venta import VentaCreate
from sqlalchemy.orm import Session


def crear_venta(db: Session, datos: VentaCreate):
    nueva = Venta(**datos.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

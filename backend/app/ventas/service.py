from app.ventas.models import Venta
from app.ventas.schemas import VentaCreate
from sqlalchemy.orm import Session


def crear_venta(db: Session, datos: VentaCreate):
    nueva = Venta(**datos.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

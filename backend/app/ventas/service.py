from app.ventas.models import Venta
from app.ventas.schemas import VentaCreate
from sqlalchemy.orm import Session


def crear_venta(db: Session, datos: VentaCreate, organization_id: int) -> Venta:
    nueva = Venta(**datos.dict(), organization_id=organization_id)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

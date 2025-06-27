from app.db.database import SessionLocal
from app.models.venta import Venta
from app.schemas.venta import VentaCreate
from app.services.venta_service import crear_venta
from sqlalchemy.orm import Session


def test_crear_venta():
    db: Session = SessionLocal()
    datos = VentaCreate(
        cliente="Juan", monto=100.0, fecha="2025-01-01", metodo_pago="contado"
    )

    venta = crear_venta(db, datos)

    assert isinstance(venta, Venta)
    assert venta.cliente == "Juan"

    # 🧹 Limpiar: borrar el registro
    db.delete(venta)
    db.commit()
    db.close()

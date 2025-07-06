from db.database import SessionLocal
from sqlalchemy.orm import Session
from ventas.models import Venta
from ventas.schemas import VentaCreate
from ventas.service import crear_venta


def test_crear_venta():
    db: Session = SessionLocal()
    try:
        datos = VentaCreate(
            cliente="Juan", monto=100.0, fecha="2025-01-01", metodo_pago="contado"
        )

        venta = crear_venta(db, datos)

        assert isinstance(venta, Venta)
        assert venta.cliente == "Juan"

        # 🧹 Limpiar: borrar el registro
        db.delete(venta)
        db.commit()
    finally:
        db.close()

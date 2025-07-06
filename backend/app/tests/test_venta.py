from datetime import date

from app.db.database import SessionLocal
from app.ventas.models import Venta
from app.ventas.schemas import VentaCreate
from app.ventas.service import crear_venta
from sqlalchemy.orm import Session


def test_crear_venta() -> None:
    db: Session = SessionLocal()
    try:
        datos = VentaCreate(
            cliente="Empresa S.A.",
            monto=1200.50,
            fecha=date.today(),
            metodo_pago="Transferencia",
        )

        venta = crear_venta(db, datos, organization_id=1)

        assert isinstance(venta, Venta)
        assert venta.organization_id == 1
        assert venta.cliente == "Empresa S.A."
        assert venta.monto == 1200.50
        assert venta.fecha == date.today()
        assert venta.metodo_pago == "Transferencia"

        # 🧹 Limpiar: borrar el registro
        db.delete(venta)
        db.commit()
    finally:
        db.close()

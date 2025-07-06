from app.db.database import SessionLocal
from app.ventas.schemas import VentaCreate, VentaOut
from app.ventas.service import crear_venta
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def health() -> dict:
    return {"message": "Backend de ventas funcionando 🚀"}


@router.post("/ventas", response_model=VentaOut)
def crear_venta_endpoint(datos: VentaCreate, db: Session = Depends(get_db)) -> VentaOut:
    # TODO: Obtener organization_id del usuario autenticado o de los datos de la solicitud
    organization_id = 1
    return crear_venta(db, datos, organization_id)

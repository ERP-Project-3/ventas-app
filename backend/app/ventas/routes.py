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
def health():
    return {"message": "Backend de ventas funcionando 🚀"}


@router.post("/ventas", response_model=VentaOut)
def registrar_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    return crear_venta(db, venta)

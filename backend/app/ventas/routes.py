from db.database import SessionLocal
from fastapi import APIRouter, Depends
from schemas import VentaCreate, VentaOut
from service import crear_venta
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

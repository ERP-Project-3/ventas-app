from sqlalchemy import Column, Integer, String, Float, Date
from app.db.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    metodo_pago = Column(String, nullable=False)

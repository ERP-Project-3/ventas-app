from app.db.database import Base, engine
from app.ventas.models import Venta  # noqa: F401

print("Creando tablas...")
Base.metadata.create_all(bind=engine)

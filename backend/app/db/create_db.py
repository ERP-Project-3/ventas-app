from app.db.database import Base, engine
from app.models import venta  # noqa: F401

# importa tus modelos aquí

print("Creando tablas...")
Base.metadata.create_all(bind=engine)

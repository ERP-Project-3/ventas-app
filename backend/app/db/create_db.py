from database import Base, engine
from ventas.models import venta  # noqa: F401

# importa tus modelos aquí

print("Creando tablas...")
Base.metadata.create_all(bind=engine)

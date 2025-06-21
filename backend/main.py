from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.routes import router
from app.db.database import Base, engine
from app.models.venta import Venta  # Asegura que la tabla se registre

# Instancia principal de FastAPI
app: FastAPI = FastAPI(title="Módulo de Registro de Ventas")

# Configuración de CORS para permitir el frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambiar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

# Ruta de prueba para verificar que el backend está vivo
@app.get("/", response_class=JSONResponse)
def health_check() -> dict[str, str]:
    return {"message": "Backend de ventas funcionando 🚀"}

# Incluir todas las rutas definidas en api/routes.py
app.include_router(router)


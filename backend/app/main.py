from app.api.routes import router
from app.db.database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# Incluir todas las rutas definidas en api/routes.py
app.include_router(router)

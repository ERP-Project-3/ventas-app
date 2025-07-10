import os
from typing import ClassVar

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    API_SECRET_KEY: str = os.getenv("API_SECRET_KEY", "s3cret0ERP")

    # Usa variables de la clase, no os.getenv
    DATABASE_URL: ClassVar[str]

    class Config:
        env_file = ".env"


settings = Settings()
# Definimos después para poder usar los atributos ya cargados
Settings.DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:{settings.DB_PASS}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

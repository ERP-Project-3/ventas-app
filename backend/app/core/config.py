import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    API_SECRET_KEY: str = os.getenv("API_SECRET_KEY", "s3cret0ERP")

    # Usa variables de la clase, no os.getenv
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
# Accede a la URL de la base de datos como propiedad: settings.DATABASE_URL

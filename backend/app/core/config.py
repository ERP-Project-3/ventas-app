import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://scige:scige@localhost:5432/scige_db"
    )
    API_SECRET_KEY: str = os.getenv("API_SECRET_KEY", "s3cret0ERP")

    class Config:
        env_file = ".env"


settings = Settings()

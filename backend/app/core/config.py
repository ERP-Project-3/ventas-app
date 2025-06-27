from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./ventas.db"
    API_SECRET_KEY: str = "s3cret0ERP"

    class Config:
        env_file = ".env"


settings = Settings()

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ventas.db")
API_SECRET_KEY = os.getenv("API_SECRET_KEY", "changeme")

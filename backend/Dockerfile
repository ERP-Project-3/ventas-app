# Imagen base ligera de Python
FROM python:3.11-slim

# Carpeta donde se ejecutarán los comandos
WORKDIR /app

# Copia solo el archivo de dependencias primero para aprovechar el cache
COPY backend/requirements.txt .

# Instala todas las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código del backend al contenedor
COPY backend /app

# Comando para iniciar el servidor FastAPI en modo desarrollo
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

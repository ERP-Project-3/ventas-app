#!/bin/bash
set -e

echo "🚀 Iniciando ERP SCIGE..."

# 🚫 Verifica si hay contenedores de docker-compose activos
if docker ps --format '{{.Names}}' | grep -q 'ventas-app-'; then
  echo "❌ Ya hay contenedores activos de Docker Compose."
  echo "🛑 Por favor, deténlos con 'docker compose down' antes de usar este script."
  exit 1
fi

# 🐘 PostgreSQL con Docker
if ! docker container inspect scige-postgres &> /dev/null; then
  echo "📦 Creando contenedor de PostgreSQL..."
  docker run --name scige-postgres \
    -e POSTGRES_USER=scige \
    -e POSTGRES_PASSWORD=scige \
    -e POSTGRES_DB=scige_db \
    -p 5432:5432 -d postgres
else
  echo "🔁 Contenedor PostgreSQL ya existe. Iniciando..."
  docker start scige-postgres
fi

echo "⏳ Esperando que PostgreSQL esté listo..."
until docker exec scige-postgres pg_isready -U scige &> /dev/null; do
  sleep 1
done

# 🔧 Backend
pushd backend

if [ ! -d "env" ]; then
  python -m venv env
fi

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  source env/Scripts/activate
else
  source env/bin/activate
fi

pip install -r requirements.txt

../scripts/setup-db.sh

uvicorn app.main:app --reload &

popd

# 🖥️ Frontend
pushd frontend
npm install
npm run dev
popd

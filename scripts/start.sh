#!/bin/bash
set -e

echo "🚀 Iniciando ERP SCIGE..."

# 🐘 PostgreSQL con Docker
if ! docker ps --format '{{.Names}}' | grep -q scige-postgres; then
  echo "📦 Levantando contenedor de PostgreSQL..."
  docker run --name scige-postgres \
    -e POSTGRES_USER=scige \
    -e POSTGRES_PASSWORD=scige \
    -e POSTGRES_DB=scige_db \
    -p 5432:5432 -d postgres
  echo "⏳ Esperando que PostgreSQL esté listo..."
  sleep 5
fi

# 🔧 Backend
pushd backend

# Crea entorno si no existe
if [ ! -d "env" ]; then
  python -m venv env
fi

# Activa entorno
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  source env/Scripts/activate
else
  source env/bin/activate
fi

# Instala dependencias
pip install -r requirements.txt

# Crea base de datos
../scripts/setup-db.sh

# Inicia backend
uvicorn app.main:app --reload &
popd

# 🖥️ Frontend
pushd frontend
npm install
npm run dev
popd

#!/bin/bash
set -e
echo "🧪 Ejecutando pruebas con Pytest..."

# Checa si hay algún contenedor de postgres activo
if ! docker ps --format '{{.Image}}' | grep -q 'postgres'; then
  echo "❌ No hay ningún contenedor de Postgres corriendo."
  echo "🟦 Inicia tu base con './scripts/start.sh' o './scripts/start-docker.sh' antes de testear."
  exit 1
fi

cd backend

if [ -f "env/Scripts/activate" ]; then
  source env/Scripts/activate
elif [ -f "env/bin/activate" ]; then
  source env/bin/activate
else
  echo "No se encontró el entorno virtual. Por favor, crea uno en 'env'."
  exit 1
fi

PYTHONPATH=$(pwd) pytest app/tests/

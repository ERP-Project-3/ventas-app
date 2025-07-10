#!/bin/bash
set -e
echo "🧪 Ejecutando pruebas con Pytest..."

# Verifica que Postgres esté escuchando en localhost:5432
echo "🔍 Verificando que Postgres esté corriendo en localhost:5432..."
if ! nc -z localhost 5432; then
  echo "❌ No se detectó Postgres en localhost:5432."
  echo "Por favor, inicia tu contenedor con Docker antes de correr los tests."
  echo "🟢 Comando que inicia el contenedor en local: './scripts/start.sh'"
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

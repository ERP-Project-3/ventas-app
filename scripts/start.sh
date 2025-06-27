#!/bin/bash
set -e
# Inicia backend y frontend en paralelo
echo "🚀 Iniciando ERP SCIGE..."
# Backend
pushd backend

# Crea entorno solo si no existe
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

# Inicia backend
uvicorn app.main:app --reload &

popd

# Frontend
pushd frontend
npm install
npm run dev
popd
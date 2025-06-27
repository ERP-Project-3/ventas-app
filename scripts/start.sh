#!/bin/bash
# Inicia backend y frontend en paralelo
echo "🚀 Iniciando ERP SCIGE..."
# Backend
cd backend

# Crea entorno solo si no existe
if [ ! -d "env" ]; then
  python -m venv env
fi

# Activa entorno
source env/Scripts/activate

# Instala dependencias
pip install -r requirements.txt

# Inicia backend
uvicorn app.main:app --reload &

# Frontend
cd ..
cd frontend
npm install
npm run dev
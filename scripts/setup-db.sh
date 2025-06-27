#!/bin/bash
echo "🗄️ Creando base de datos desde modelos..."

cd backend
source env/Scripts/activate  # o env/bin/activate para Linux/macOS

# Ejecuta el script como módulo para que Python reconozca `app` como paquete
python -m app.db.create_db
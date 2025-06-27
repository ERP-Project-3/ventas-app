#!/bin/bash
set -e
echo "🗄️ Creando base de datos desde modelos..."

cd backend
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
	source env/Scripts/activate
else
	source env/bin/activate
fi

# Ejecuta el script como módulo para que Python reconozca `app` como paquete
python -m app.db.create_db
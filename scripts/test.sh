#!/bin/bash
set -e
echo "🧪 Ejecutando pruebas con Pytest..."
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
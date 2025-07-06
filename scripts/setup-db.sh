#!/bin/bash
set -e

echo "📦 Creando base de datos desde modelos..."

# Detecta ruta absoluta del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$SCRIPT_DIR/../backend"

cd "$BACKEND_DIR"

# Activa entorno virtual
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  source env/Scripts/activate
else
  source env/bin/activate
fi

# Ejecuta la creación de tablas
python -m app.db.create_db

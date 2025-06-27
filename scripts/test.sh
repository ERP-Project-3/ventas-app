#!/bin/bash
set -e
echo "🧪 Ejecutando pruebas con Pytest..."
cd backend
source env/Scripts/activate  # usa env/bin/activate en Linux
PYTHONPATH=$(pwd) pytest app/tests/
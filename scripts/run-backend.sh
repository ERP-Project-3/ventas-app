#!/bin/bash
set -e
echo "🚀 Iniciando backend..."
cd backend
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
	source env/Scripts/activate
else
	source env/bin/activate
fi
uvicorn app.main:app --reload 
#!/bin/bash
set -e
echo "🚀 Iniciando backend..."
cd backend
source env/bin/activate
uvicorn app.main:app --reload 
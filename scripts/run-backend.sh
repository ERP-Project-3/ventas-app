#!/bin/bash
set -e
echo "🚀 Iniciando backend..."
cd backend
uvicorn app.main:app --reload 
#!/bin/bash
echo "🚀 Iniciando backend..."
cd backend
uvicorn app.main:app --reload 
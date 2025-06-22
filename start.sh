#!/bin/bash
# Inicia backend y frontend en paralelo

# Backend
cd backend
source env/bin/activate  # activa tu entorno virtual
uvicorn main:app --reload &
cd ..

# Frontend
cd frontend
npm run dev

#!/bin/bash
# Script para iniciar el backend en desarrollo

cd backend
source env/bin/activate
uvicorn main:app --reload

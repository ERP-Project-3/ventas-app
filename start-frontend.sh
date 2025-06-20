#!/bin/bash
# Script para iniciar el frontend en modo desarrollo

cd frontend

# Instala dependencias si no están instaladas
if [ ! -d "node_modules" ]; then
  echo "Instalando dependencias de React..."
  npm install
fi

# Levanta el servidor de desarrollo
npm run dev

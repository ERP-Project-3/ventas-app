#!/bin/bash
set -e

echo "🐳 Iniciando ERP SCIGE con Docker Compose..."

# 🚫 Verifica si existe un contenedor local conflictivo (como 'scige-postgres')
if docker ps --format '{{.Names}}' | grep -q '^scige-postgres$'; then
  echo "❌ El contenedor local 'scige-postgres' ya está corriendo."
  echo "🛑 Deténlo con 'docker stop scige-postgres && docker rm scige-postgres' antes de usar Docker Compose."
  exit 1
fi

docker compose up --build

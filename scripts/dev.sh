#!/bin/bash
echo "🔧 Formateando código con Black + isort..."
black backend/app
isort backend/app
echo "✅ Validación con Flake8..."
flake8 backend/app
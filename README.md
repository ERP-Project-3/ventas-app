# 🧾 ventas-app – Módulo de Registro de Ventas

Este repositorio contiene el desarrollo del módulo principal de la aplicación: **Registro de Ventas**, encargado de gestionar transacciones comerciales, asociarlas a clientes y controlar el estado de pago (contado o crédito).  
Actualmente está compuesto por un backend en **FastAPI** y un frontend en **React + TypeScript + Vite**.

---

## 🎯 Objetivo

Desarrollar un módulo funcional que permita:

- Registrar ventas manuales o por formulario.
- Asociar ventas a clientes y condiciones de pago.
- Consultar historial de ventas.
- Iniciar la base del control de cobranzas.

---

## 🏗️ Estructura del proyecto
```
ventas-app/
├── backend/ # Backend en FastAPI
│ └── main.py
├── frontend/ # Frontend en React + Vite
│ └── src/App.tsx
├── .gitignore
├── start-backend.sh
├── start-frontend.sh
└── README.md
```
## 🚀 Cómo iniciar el proyecto

### 1. Backend (FastAPI)

```bash
cd backend
python -m venv env
source env/bin/activate   # o env\Scripts\activate en Windows
pip install -r requirements.txt
uvicorn main:app --reload
```
O simplemente:
```bash
./start-backend.sh
```
Backend disponible en: http://localhost:8000

### 2. Frontend (React + Vite + TS)

```bash
cd frontend
npm install
npm run dev
```
O simplemente:
```bash
./start-frontend.sh
```
Frontend disponible en: http://localhost:5173

### 3. Variables de entorno
Backend:
Crea .env a partir de .env.example

Frontend:
Crea .env a partir de .env.example
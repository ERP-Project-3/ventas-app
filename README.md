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
- Evolucionar hacia un sistema ERP completo, integrable con herramientas como Salesforce, Contpaqi, SAP, Oracle, Tress, entre otras.

---

## 🏗️ Estructura del proyecto

```
ChatGPT said:
Claro, aquí tienes una versión actualizada y más completa del README.md, adaptada al nuevo estado del proyecto y los scripts disponibles como start.sh, setup-db.sh, dev.sh, etc.:

markdown
Copy
Edit
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
- Evolucionar hacia un sistema ERP completo, integrable con herramientas como Salesforce, Contpaqi, SAP, Oracle, Tress, entre otras.

---

## 🏗️ Estructura del proyecto

```
ventas-app/
├── backend/ # Backend en FastAPI
│ ├── app/ # Código modular del backend
│ │ ├── api/ # Rutas de la API
│ │ ├── core/ # Configuración y constantes
│ │ ├── db/ # Base de datos y conexión
│ │ ├── models/ # Modelos ORM
│ │ ├── schemas/ # Esquemas Pydantic
│ │ ├── services/ # Lógica de negocio
│ │ └── tests/ # Pruebas unitarias
│ ├── env/ # Entorno virtual (excluido del repo)
│ ├── main.py # Punto de entrada de FastAPI
│ └── requirements.txt # Dependencias del backend
│
├── frontend/ # Frontend en React + Vite
│ └── src/
│ └── App.tsx
│
├── scripts/ # Scripts útiles para desarrollo
│ ├── dev.sh # Formateo + lint
│ ├── start.sh # Inicia backend y frontend
│ ├── run-backend.sh # Solo backend
│ ├── setup-db.sh # Crea base de datos desde modelos
│ └── test.sh # Corre pruebas con pytest
│
├── .env.example # Variables de entorno de ejemplo
├── .gitignore
├── CODEOWNERS
└── README.md
```

---

## 🚀 Cómo iniciar el proyecto

### 🔧 1. Requisitos

- Python 3.10+
- Node.js 18+
- pip, venv, bash (o terminal compatible)

---

### 🟢 Opción rápida: Todo en uno

``` bash
./scripts/start.sh
```

Este script:

Crea el entorno virtual (si no existe)

Instala dependencias backend

Inicia el backend (FastAPI)

Instala dependencias frontend

Inicia el frontend (React)

⚙️ Opción manual paso a paso
🖥️ Backend (FastAPI)

``` bash
cd backend
python -m venv env
source env/bin/activate     # En Windows: env\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

🌐 Frontend (React + Vite)
``` bash
cd frontend
npm install
npm run dev
```

🧪 Ejecutar pruebas (Pytest)
```bash
./scripts/test.sh
🧼 Formateo + Lint (Black, isort, Flake8)
```bash
./scripts/dev.sh
```
🛠️ Crear base de datos desde modelos
```bash
./scripts/setup-db.sh
```
🌍 URLs locales
Backend API Docs: http://localhost:8000/docs

Frontend App: http://localhost:5173

🔐 Variables de entorno
Backend
Crear .env en backend/ a partir del archivo .env.example:

``` env
DATABASE_URL=sqlite:///./ventas.db
API_SECRET_KEY=s3cret0ERP
```
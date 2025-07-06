# 🧾 ventas-app – Módulo de Registro de Ventas

Este repositorio contiene el desarrollo del módulo inicial del sistema **SCIGE ERP**: el **Registro de Ventas**, responsable de capturar transacciones comerciales, asociarlas a clientes y preparar el flujo de control de cobranzas.  
Está compuesto por un **backend modular en FastAPI** y un **frontend en React + Vite**, listo para escalar y adaptarse a un entorno empresarial.

---

## 🎯 Objetivo de esta fase

Entregar un MVP funcional centrado en:

- Registrar ventas con cliente, monto, fecha y método de pago.
- Servir como base para los módulos de Cobranzas y CRM.
- Validar integración backend + frontend.
- Obtener retroalimentación de usuarios y maquiladoras reales.

---

## 🏗️ Estructura del proyecto

```
ventas-app/
├── backend/
│   ├── app/
│   │   ├── core/           # Configuración (env, conexión DB)
│   │   ├── db/             # Conexión y creación de la DB
│   │   ├── ventas/         # Módulo de ventas: modelos, rutas, lógica
│   │   └── tests/          # Pruebas unitarias
│   ├── main.py             # Entry point de FastAPI
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── modules/        # Módulos separados: Ventas, Cobranzas, CRM
│   │   ├── components/     # Componentes comunes (ej. Layout)
│   │   ├── App.tsx         # Configuración de rutas
│   │   └── main.tsx        # Punto de entrada React
│   └── vite.config.ts
│
├── scripts/
│   ├── start.sh            # Inicia backend + frontend
│   ├── run-backend.sh      # Solo backend
│   ├── setup-db.sh         # Crea tablas en PostgreSQL
│   ├── dev.sh              # Lint + formato
│   └── test.sh             # Corre Pytest
│
├── .env.example
├── .pre-commit-config.yaml
└── README.md
```

---

## 🚀 Cómo iniciar el proyecto

### 🔧 Requisitos

- Python 3.10+
- Node.js 18+
- PostgreSQL (via Docker)
- Bash (o terminal compatible)

---

### ⚡ Opción rápida: Todo en uno

```bash
./scripts/start.sh
```

Este script:

1. Crea entorno virtual e instala dependencias.
2. Levanta el contenedor PostgreSQL.
3. Crea la base de datos desde los modelos.
4. Inicia el backend FastAPI.
5. Instala e inicia el frontend React.

---

### ⚙️ Opción manual paso a paso

#### 🖥️ Backend (FastAPI)

```bash
cd backend
python -m venv env
source env/bin/activate         # En Windows: env\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### 🐘 Base de datos PostgreSQL con Docker

```bash
docker run --name scige-postgres \
  -e POSTGRES_USER=scige \
  -e POSTGRES_PASSWORD=scige \
  -e POSTGRES_DB=scige_db \
  -p 5432:5432 -d postgres
```

```bash
./scripts/setup-db.sh
```

#### 🌐 Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 Pruebas y herramientas

- 🧪 **Tests** (Pytest): `./scripts/test.sh`
- 🧼 **Lint + formato**: `./scripts/dev.sh`
- ✅ **Hooks pre-commit**: ejecuta pruebas y validación automática antes de cada commit

---

## 🔗 URLs locales

- Backend (FastAPI Docs): [http://localhost:8000/docs](http://localhost:8000/docs)
- Frontend (Vite + React): [http://localhost:5173](http://localhost:5173)

---

## 🔐 Variables de entorno

### Backend

Crear archivo `.env` en `backend/` basado en `.env.example`:

```env
DATABASE_URL=postgresql://scige:scige@localhost:5432/scige_db
```

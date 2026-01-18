# 🏗️ IMPLEMENTATION PLAN - MVP v0.30.0

**Proyecto**: Salesforce Admin Learning Platform  
**Versión**: v0.30.0 (Web Platform MVP)  
**Tech Lead**: AI Agent (Gemini)  
**Developer**: Wilmer  
**Fecha**: 17 Enero 2026  
**Duración estimada**: 4 semanas (24 días)

---

## 📑 Tabla de Contenidos

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Decisiones Técnicas](#decisiones-técnicas)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Plan de Refactorización](#plan-de-refactorización)
6. [Implementación por Fases](#implementación-por-fases)
7. [Estrategia de Testing](#estrategia-de-testing)
8. [Plan de Deployment](#plan-de-deployment)

---

## Resumen Ejecutivo

### Objetivo
Migrar la plataforma de documentación estática (v0.25.1) a una aplicación web dinámica e interactiva que permita:
- Autenticación de usuarios
- Tracking de progreso persistente
- Renderizado dinámico de Markdown
- Experiencia unificada para el equipo

### Alcance
- **In Scope**: Auth, Markdown rendering, Progress tracking, Dashboard, Team view
- **Out of Scope**: OAuth, Notificaciones, Comentarios, Búsqueda avanzada, Gamificación

### Métricas de Éxito
- ✅ 90% del equipo usa la plataforma
- ✅ Response time < 500ms (p95)
- ✅ < 3 bugs críticos en primer mes
- ✅ Coverage de tests > 75%

---

## Arquitectura del Sistema

### Diagrama de Alto Nivel

```
┌─────────────────────────────────────────────────────────────┐
│                    USUARIOS (Navegador)                     │
│              Chrome, Firefox, Safari, Edge                  │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTPS
                         │ (TLS 1.3)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   RENDER WEB SERVICE                        │
│                  (salesforce-admin.onrender.com)            │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              FASTAPI APPLICATION                      │  │
│  │                                                       │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │  PRESENTATION LAYER (Templates)                 │ │  │
│  │  │  ├─ Jinja2 Templates                            │ │  │
│  │  │  ├─ TailwindCSS (Styling)                       │ │  │
│  │  │  └─ Alpine.js (Interactivity)                   │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  │                         ▲                             │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │  API LAYER (REST Endpoints)                     │ │  │
│  │  │  ├─ /api/auth/* (Authentication)                │ │  │
│  │  │  ├─ /api/progress/* (Progress Tracking)         │ │  │
│  │  │  ├─ /api/sprints/* (Sprint Management)          │ │  │
│  │  │  └─ /docs/* (Markdown Rendering)                │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  │                         ▲                             │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │  BUSINESS LOGIC LAYER (Services)                │ │  │
│  │  │  ├─ AuthService (JWT, bcrypt)                   │ │  │
│  │  │  ├─ MarkdownService (MD → HTML)                 │ │  │
│  │  │  ├─ ProgressService (Tracking)                  │ │  │
│  │  │  └─ TaskService (Task Management)               │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  │                         ▲                             │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │  DATA ACCESS LAYER (ORM)                        │ │  │
│  │  │  ├─ SQLAlchemy Models                           │ │  │
│  │  │  ├─ Database Session Management                 │ │  │
│  │  │  └─ Alembic Migrations                          │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │ PostgreSQL Protocol
                         │ (Port 5432)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              RENDER POSTGRESQL DATABASE                     │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Tables:                                              │  │
│  │  ├─ users (authentication, profiles)                 │  │
│  │  ├─ sprints (course structure)                       │  │
│  │  ├─ tasks (assignments, classes)                     │  │
│  │  └─ user_progress (completion tracking)              │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  GITHUB REPOSITORY                          │
│              (Source of Truth para Contenido)               │
│  ├─ content/curriculum/ (Markdown files)                    │
│  ├─ content/Superbadges/                                    │
│  ├─ content/Practica_Financiera/                            │
│  └─ content/Gestor_de_Versiones/                            │
└────────────────────────┬────────────────────────────────────┘
                         │ Git Pull / Webhook
                         │ (Sync contenido)
                         ▼
                   [FastAPI App]
```

### Flujo de Datos: Renderizado de Markdown

```
Usuario solicita /docs/curriculum/sprint_01/semana_01/01-clase_1_teoria
                         │
                         ▼
              ┌──────────────────────┐
              │  FastAPI Router      │
              │  (docs.py)           │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  MarkdownService     │
              │  - Valida path       │
              │  - Lee archivo .md   │
              │  - Convierte a HTML  │
              │  - Resuelve links    │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Jinja2 Template     │
              │  (doc_viewer.html)   │
              │  - Renderiza HTML    │
              │  - Agrega sidebar    │
              │  - Breadcrumbs       │
              └──────────┬───────────┘
                         │
                         ▼
                   HTML Response
```

### Flujo de Datos: Tracking de Progreso

```
Usuario marca checkbox en clase
                         │
                         ▼
              ┌──────────────────────┐
              │  Alpine.js           │
              │  (Frontend)          │
              │  - Captura evento    │
              │  - POST a API        │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  FastAPI Endpoint    │
              │  /api/progress/      │
              │  task/{id}/mark      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  ProgressService     │
              │  - Valida user       │
              │  - Actualiza status  │
              │  - Guarda timestamp  │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  SQLAlchemy ORM      │
              │  - UPDATE query      │
              │  - Commit a DB       │
              └──────────┬───────────┘
                         │
                         ▼
                   PostgreSQL
                         │
                         ▼
              ┌──────────────────────┐
              │  Response JSON       │
              │  { success: true,    │
              │    new_progress: 45% }│
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Alpine.js           │
              │  - Actualiza UI      │
              │  - Marca checkbox    │
              │  - Actualiza %       │
              └──────────────────────┘
```

---

## Decisiones Técnicas

### 1. Backend Framework: FastAPI

**Opciones evaluadas:**
- Flask
- Django
- FastAPI ✅

**Decisión: FastAPI**

**Justificación:**
1. **Performance**: Async/await nativo, comparable a Node.js
2. **Validación automática**: Pydantic schemas reducen código boilerplate
3. **Documentación automática**: Swagger UI out-of-the-box
4. **Type hints**: Mejor mantenibilidad y autocomplete
5. **Moderno**: Diseñado para Python 3.7+
6. **Comunidad activa**: Gran ecosistema de plugins

**Trade-offs:**
- ❌ Menos maduro que Flask/Django
- ❌ Curva de aprendizaje para async
- ✅ Pero: Mejor para APIs modernas

---

### 2. ORM: SQLAlchemy 2.0

**Opciones evaluadas:**
- Django ORM
- Peewee
- SQLAlchemy 2.0 ✅

**Decisión: SQLAlchemy 2.0**

**Justificación:**
1. **Async support**: Compatible con FastAPI async
2. **Maduro y robusto**: 15+ años de desarrollo
3. **Flexible**: Soporta múltiples DBs
4. **Migrations**: Alembic integrado
5. **Type hints**: Mejoras en 2.0

---

### 3. Database: PostgreSQL

**Opciones evaluadas:**
- SQLite
- MySQL
- PostgreSQL ✅

**Decisión: PostgreSQL**

**Justificación:**
1. **Render free tier**: Incluye PostgreSQL gratis
2. **ACID compliant**: Transacciones robustas
3. **JSON support**: Para datos semi-estructurados
4. **Full-text search**: Para futuras features
5. **Escalabilidad**: Soporta millones de registros

---

### 4. Templating: Jinja2

**Opciones evaluadas:**
- React/Vue SPA
- Jinja2 SSR ✅

**Decisión: Jinja2 (Server-Side Rendering)**

**Justificación:**
1. **Simplicidad**: No requiere build process
2. **SEO-friendly**: HTML renderizado en servidor
3. **Performance**: Menos JavaScript en cliente
4. **Integración**: Nativo en FastAPI
5. **Progressive enhancement**: Funciona sin JS

**Para interactividad:**
- Alpine.js (3KB) para checkboxes, modals, etc.

---

### 5. CSS Framework: TailwindCSS

**Opciones evaluadas:**
- Bootstrap
- Bulma
- TailwindCSS ✅

**Decisión: TailwindCSS**

**Justificación:**
1. **Utility-first**: Rápido desarrollo
2. **Customizable**: Fácil personalización
3. **Pequeño bundle**: Solo clases usadas
4. **Moderno**: Diseños actuales
5. **Dark mode**: Built-in

---

### 6. Markdown Parser: python-markdown

**Opciones evaluadas:**
- mistune
- markdown2
- python-markdown ✅

**Decisión: python-markdown**

**Justificación:**
1. **Extensible**: Plugins para tablas, code highlighting
2. **Maduro**: Estable y bien mantenido
3. **Compatible**: Sintaxis GitHub Flavored Markdown
4. **Seguro**: Sanitización de HTML

---

## Estructura del Proyecto

### Estructura Completa de Carpetas

```
salesforce_admin/
├── app/                              # Aplicación FastAPI
│   ├── __init__.py
│   ├── main.py                       # Entry point, FastAPI app
│   ├── config.py                     # Configuración (env vars)
│   ├── database.py                   # DB connection, session
│   ├── dependencies.py               # Dependency injection
│   │
│   ├── models/                       # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── base.py                   # Base model class
│   │   ├── user.py                   # User model
│   │   ├── sprint.py                 # Sprint model
│   │   ├── task.py                   # Task model
│   │   └── progress.py               # UserProgress model
│   │
│   ├── schemas/                      # Pydantic schemas (validation)
│   │   ├── __init__.py
│   │   ├── user.py                   # UserCreate, UserResponse
│   │   ├── auth.py                   # LoginRequest, TokenResponse
│   │   ├── sprint.py                 # SprintResponse
│   │   ├── task.py                   # TaskResponse
│   │   └── progress.py               # ProgressUpdate, ProgressResponse
│   │
│   ├── routers/                      # API routes (controllers)
│   │   ├── __init__.py
│   │   ├── auth.py                   # POST /api/auth/register, /login
│   │   ├── docs.py                   # GET /docs/{path:path}
│   │   ├── progress.py               # GET/POST /api/progress/*
│   │   ├── sprints.py                # GET /api/sprints/*
│   │   ├── tasks.py                  # GET /api/tasks/*
│   │   └── users.py                  # GET/PATCH /api/users/* (admin)
│   │
│   ├── services/                     # Business logic
│   │   ├── __init__.py
│   │   ├── auth_service.py           # JWT, bcrypt, login logic
│   │   ├── markdown_service.py       # MD → HTML, link resolution
│   │   ├── progress_service.py       # Progress calculations
│   │   ├── task_service.py           # Task management
│   │   └── user_service.py           # User CRUD
│   │
│   ├── middleware/                   # Middleware
│   │   ├── __init__.py
│   │   ├── auth.py                   # JWT verification
│   │   ├── cors.py                   # CORS configuration
│   │   ├── logging.py                # Request logging
│   │   └── error_handler.py          # Global error handling
│   │
│   ├── utils/                        # Utilities
│   │   ├── __init__.py
│   │   ├── security.py               # Password hashing, JWT
│   │   ├── validators.py             # Custom validators
│   │   └── helpers.py                # Helper functions
│   │
│   ├── templates/                    # Jinja2 templates
│   │   ├── base.html                 # Base layout
│   │   ├── components/               # Reusable components
│   │   │   ├── navbar.html
│   │   │   ├── sidebar.html
│   │   │   ├── breadcrumbs.html
│   │   │   ├── footer.html
│   │   │   └── progress_bar.html
│   │   ├── auth/                     # Authentication pages
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── logout.html
│   │   ├── dashboard.html            # User dashboard
│   │   ├── doc_viewer.html           # Markdown viewer
│   │   ├── team.html                 # Team progress view
│   │   └── errors/                   # Error pages
│   │       ├── 404.html
│   │       ├── 500.html
│   │       └── 403.html
│   │
│   └── static/                       # Static assets
│       ├── css/
│       │   ├── tailwind.css          # TailwindCSS (CDN o compiled)
│       │   └── custom.css            # Custom styles
│       ├── js/
│       │   ├── alpine.js             # Alpine.js (CDN)
│       │   ├── app.js                # Custom JavaScript
│       │   └── markdown.js           # Markdown enhancements
│       └── images/
│           ├── logo.png
│           └── favicon.ico
│
├── content/                          # Contenido Markdown (migrado)
│   ├── curriculum/
│   │   └── sprint_01/
│   │       ├── semana_01/
│   │       ├── semana_02/
│   │       ├── semana_03/
│   │       └── semana_04/
│   ├── Superbadges/
│   ├── Practica_Financiera/
│   └── Gestor_de_Versiones/
│
├── tests/                            # Tests
│   ├── __init__.py
│   ├── conftest.py                   # Pytest fixtures
│   ├── unit/                         # Unit tests
│   │   ├── test_auth_service.py
│   │   ├── test_markdown_service.py
│   │   ├── test_progress_service.py
│   │   └── test_models.py
│   ├── integration/                  # Integration tests
│   │   ├── test_auth_api.py
│   │   ├── test_progress_api.py
│   │   └── test_docs_api.py
│   └── e2e/                          # End-to-end tests (optional)
│       └── test_user_flow.py
│
├── alembic/                          # Database migrations
│   ├── versions/
│   │   ├── 001_initial_schema.py
│   │   ├── 002_add_user_roles.py
│   │   └── ...
│   ├── env.py
│   ├── script.py.mako
│   └── alembic.ini
│
├── scripts/                          # Utility scripts
│   ├── seed_data.py                  # Seed initial data (sprints, tasks)
│   ├── sync_tasks.py                 # Sync tasks from Markdown structure
│   ├── backup_db.py                  # Database backup
│   └── create_admin.py               # Create admin user
│
├── docs/                             # Project documentation
│   ├── SDLC.md
│   ├── DEVELOPMENT_RULES.md
│   ├── ROADMAP.md
│   ├── TASK_LIST_MVP.md
│   ├── AI_ROLE_FRAMEWORK.md
│   ├── IMPLEMENTATION_PLAN.md        # Este documento
│   ├── API.md                        # API documentation
│   └── DEPLOYMENT.md                 # Deployment guide
│
├── .env.example                      # Example environment variables
├── .env                              # Environment variables (gitignored)
├── .gitignore
├── requirements.txt                  # Python dependencies
├── requirements-dev.txt              # Dev dependencies (pytest, black, etc.)
├── docker-compose.yml                # Local development
├── Dockerfile                        # Production container (opcional)
├── render.yaml                       # Render deployment config
├── pytest.ini                        # Pytest configuration
├── pyproject.toml                    # Black, isort config
└── README.md                         # Main README
```

---

## Plan de Refactorización

### Fase 1: Preparación (Día 1)

**Objetivo**: Preparar el proyecto para la migración sin romper v0.25.1

**Pasos:**

1. **Crear rama de desarrollo**
   ```bash
   git checkout -b feature/web-platform-mvp
   ```

2. **Crear estructura de carpetas `app/`**
   ```bash
   mkdir -p app/{models,schemas,routers,services,middleware,utils,templates,static}
   mkdir -p app/templates/{components,auth,errors}
   mkdir -p app/static/{css,js,images}
   mkdir -p tests/{unit,integration,e2e}
   mkdir -p alembic/versions
   mkdir -p scripts
   ```

3. **Crear archivos `__init__.py`**
   ```bash
   touch app/__init__.py
   touch app/models/__init__.py
   touch app/schemas/__init__.py
   # ... etc
   ```

4. **Mover contenido a `content/`**
   ```bash
   git mv curriculum content/curriculum
   git mv Superbadges content/Superbadges
   git mv Practica_Financiera content/Practica_Financiera
   git mv Gestor_de_Versiones content/Gestor_de_Versiones
   ```

5. **Crear `requirements.txt`**
   ```txt
   fastapi==0.109.0
   uvicorn[standard]==0.27.0
   sqlalchemy==2.0.25
   alembic==1.13.1
   psycopg2-binary==2.9.9
   python-jose[cryptography]==3.3.0
   passlib[bcrypt]==1.7.4
   python-markdown==3.5.2
   jinja2==3.1.3
   python-multipart==0.0.6
   pydantic==2.5.3
   pydantic-settings==2.1.0
   ```

6. **Crear `.env.example`**
   ```env
   # Database
   DATABASE_URL=postgresql://user:password@localhost:5432/salesforce_admin_dev
   
   # Security
   SECRET_KEY=your-secret-key-here-change-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_DAYS=7
   
   # App
   ENVIRONMENT=development
   DEBUG=True
   ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
   
   # Content
   CONTENT_PATH=./content
   ```

7. **Crear `docker-compose.yml` para desarrollo local**
   ```yaml
   version: '3.8'
   
   services:
     db:
       image: postgres:15-alpine
       container_name: salesforce_admin_db
       environment:
         POSTGRES_USER: admin
         POSTGRES_PASSWORD: dev_password
         POSTGRES_DB: salesforce_admin_dev
       ports:
         - "5432:5432"
       volumes:
         - postgres_data:/var/lib/postgresql/data
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -U admin"]
         interval: 10s
         timeout: 5s
         retries: 5
   
     web:
       build: .
       container_name: salesforce_admin_web
       command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
       volumes:
         - .:/app
       ports:
         - "8000:8000"
       environment:
         DATABASE_URL: postgresql://admin:dev_password@db:5432/salesforce_admin_dev
         SECRET_KEY: dev_secret_key_change_in_production
         ENVIRONMENT: development
       depends_on:
         db:
           condition: service_healthy
   
   volumes:
     postgres_data:
   ```

**Criterios de Aceptación:**
- ✅ Estructura de carpetas creada
- ✅ Contenido movido a `content/`
- ✅ Git history preservado
- ✅ `requirements.txt` creado
- ✅ Docker Compose funcional

---

### Fase 2: Database Setup (Día 2)

**Objetivo**: Configurar SQLAlchemy, crear modelos, setup Alembic

**Archivos a crear:**

#### `app/config.py`
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_DAYS: int = 7
    
    # App
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # Content
    CONTENT_PATH: str = "./content"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

#### `app/database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependency for database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### `app/models/user.py`
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class User(Base):
    """User model for authentication and profile"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    team = Column(String(50), default="VISIONARY ADMINS")
    role = Column(String(20), default="student")  # student, instructor, admin
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Relationships
    progress = relationship("UserProgress", back_populates="user", cascade="all, delete-orphan")
```

#### `app/models/sprint.py`, `task.py`, `progress.py`
(Similar structure, ver SDLC.md para schema completo)

#### Setup Alembic
```bash
alembic init alembic
# Editar alembic.ini y env.py para usar settings.DATABASE_URL
alembic revision --autogenerate -m "Initial schema"
alembic upgrade head
```

**Criterios de Aceptación:**
- ✅ SQLAlchemy configurado
- ✅ 4 modelos creados (User, Sprint, Task, UserProgress)
- ✅ Alembic configurado
- ✅ Primera migration ejecutada
- ✅ Tablas creadas en PostgreSQL

---

## Implementación por Fases

### FASE 1: Infrastructure (Días 1-2)
- ✅ Estructura de carpetas
- ✅ Database setup
- ✅ Docker Compose

### FASE 2: Authentication (Días 3-5)
- Implementar AuthService (JWT, bcrypt)
- Crear endpoints `/api/auth/*`
- Templates de login/register
- Middleware de autenticación

### FASE 3: Markdown Rendering (Días 6-8)
- Implementar MarkdownService
- Crear endpoint `/docs/{path:path}`
- Template `doc_viewer.html`
- Resolución de links relativos

### FASE 4: Progress Tracking (Días 9-12)
- Implementar ProgressService
- Crear endpoints `/api/progress/*`
- Dashboard con Alpine.js
- Vista de equipo

### FASE 5: Frontend Polish (Días 13-15)
- TailwindCSS setup
- Componentes reutilizables
- Responsive design
- Navegación jerárquica

### FASE 6: Testing (Días 16-18)
- Unit tests (services, models)
- Integration tests (API)
- Coverage > 75%

### FASE 7: Deployment (Días 19-21)
- Configurar Render
- Migrations en producción
- Seed data
- Smoke testing

### FASE 8: Polish & Documentation (Días 22-24)
- Bug fixes
- Performance optimization
- API documentation
- User guide

---

## Estrategia de Testing

### Unit Tests (75% del coverage)
```python
# tests/unit/test_auth_service.py
def test_hash_password():
    password = "SecurePass123!"
    hashed = auth_service.hash_password(password)
    assert hashed != password
    assert auth_service.verify_password(password, hashed)

def test_create_access_token():
    data = {"sub": "user@example.com"}
    token = auth_service.create_access_token(data)
    assert token is not None
    decoded = auth_service.verify_token(token)
    assert decoded["sub"] == "user@example.com"
```

### Integration Tests (20%)
```python
# tests/integration/test_auth_api.py
def test_register_user(client):
    response = client.post("/api/auth/register", json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "SecurePass123!"
    })
    assert response.status_code == 201
    assert "id" in response.json()
```

---

## Plan de Deployment

### Render Configuration (`render.yaml`)
```yaml
services:
  - type: web
    name: salesforce-admin-platform
    env: python
    region: oregon
    plan: free
    buildCommand: |
      pip install -r requirements.txt
      alembic upgrade head
      python scripts/seed_data.py
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: salesforce-admin-db
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: ENVIRONMENT
        value: production
      - key: DEBUG
        value: false

databases:
  - name: salesforce-admin-db
    databaseName: salesforce_admin_prod
    user: admin
    plan: free
```

---

## 🚨 Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Render free tier se duerme | Alta | Medio | Documentar cold start, considerar ping service |
| Desarrollo toma más tiempo | Media | Alto | Priorizar MVP features, postponer nice-to-haves |
| Bugs en producción | Media | Alto | Tests exhaustivos, staging environment |
| Pérdida de datos | Baja | Crítico | Backups automáticos, migrations testeadas |

---

## ✅ Checklist de Aprobación

Antes de proceder a la implementación, confirmar:

- [ ] Arquitectura aprobada
- [ ] Stack tecnológico aceptado
- [ ] Estructura de carpetas clara
- [ ] Plan de refactorización entendido
- [ ] Timeline de 4 semanas realista
- [ ] Riesgos identificados y mitigados

---

**Creado por**: Tech Lead (AI Agent)  
**Fecha**: 17 Enero 2026  
**Versión**: 1.0  
**Estado**: Pendiente de aprobación

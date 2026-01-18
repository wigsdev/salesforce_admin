# 📋 SDLC: Salesforce Admin Learning Platform

**Proyecto**: Salesforce Admin Learning Platform (Plataforma Integral)  
**Equipo**: VISIONARY ADMINS  
**Versión**: 0.30.0 (Web Platform MVP)  
**Fecha**: 17 Enero 2026  
**Tipo**: Aplicación Web Full-Stack con Contenido Dinámico

---

## 📑 Tabla de Contenidos

1. [Fase 1: Planificación](#fase-1-planificación)
2. [Fase 2: Análisis de Requerimientos](#fase-2-análisis-de-requerimientos)
3. [Fase 3: Diseño](#fase-3-diseño)
4. [Fase 4: Desarrollo](#fase-4-desarrollo)
5. [Fase 5: Pruebas](#fase-5-pruebas)
6. [Fase 6: Implementación](#fase-6-implementación)
7. [Fase 7: Mantenimiento](#fase-7-mantenimiento)

---

## Fase 1: Planificación

### 1.1 Visión del Proyecto

**Evolución del Proyecto:**
- **v0.25.0**: Documentación estática en GitHub Pages
- **v0.30.0**: Plataforma web interactiva con persistencia
- **v1.0.0**: Plataforma completa con 4 Sprints

**Problema a Resolver:**
Crear una plataforma web integral que combine:
- Contenido educativo (Markdown renderizado dinámicamente)
- Tracking de progreso individual y grupal
- Interactividad (checkboxes, comentarios, notas)
- Experiencia unificada (un solo sitio, un solo login)

**Objetivo del MVP (v0.30.0):**
Migrar la documentación estática a una aplicación web que:
- Renderice Markdown dinámicamente desde el repositorio
- Permita autenticación de usuarios del equipo
- Registre progreso de tareas en base de datos
- Mantenga la simplicidad de edición (Markdown)
- Despliegue en Render (no GitHub Pages)

### 1.2 Alcance del MVP

#### ✅ **In Scope (Versión 0.30.0)**

**Core Features:**
- Sistema de autenticación (email/password)
- Renderizado dinámico de Markdown
- Dashboard personal con progreso por Sprint
- Marcar tareas como completadas (persistente)
- Vista de progreso del equipo
- Navegación jerárquica (igual que v0.25.0)
- Links entre documentos funcionales

**Contenido:**
- Todo el contenido de v0.25.0 (Sprint 1)
- Estructura preparada para Sprints 2, 3, 4

**Infraestructura:**
- Deploy en Render
- PostgreSQL para persistencia
- Git como fuente de contenido

#### ❌ **Out of Scope (Futuras versiones)**

- OAuth con GitHub/Google (v0.35.0)
- Notificaciones por email (v0.40.0)
- Comentarios en documentos (v0.45.0)
- Búsqueda full-text (v0.50.0)
- Gamificación (badges, leaderboards) (v0.60.0)
- Mobile app nativa (v2.0.0)
- Integración con Trello/Slack (v2.0.0)

### 1.3 Stakeholders

| Rol | Responsabilidad | Persona |
|-----|-----------------|---------|
| **Product Owner** | Visión del producto, priorización, validación | Wilmer (Usuario único) |
| **AI Agent** | Asume múltiples roles según fase (Tech Lead, Backend Dev, Frontend Dev, QA, DevOps, Code Reviewer) | Gemini AI |
| **Developer/Implementador** | Ejecuta código, prueba, reporta errores, valida funcionalidad | Wilmer (Usuario único) |
| **Content Manager** | Actualización de Markdown | Wilmer (Usuario único) |
| **End Users** | Estudiantes del curso | 5-10 miembros VISIONARY ADMINS |

### 1.4 Cronograma Estimado

| Fase | Duración | Entregables |
|------|----------|-------------|
| **Planificación** | 1 día | SDLC, Roadmap, Task List, AI Role Framework |
| **Análisis** | 1 día | Requerimientos, User Stories |
| **Diseño** | 2 días | Arquitectura, DB Schema |
| **Refactorización** | 1 día | Nueva estructura de carpetas |
| **Desarrollo Backend** | 6 días | API, Auth, DB, Markdown Renderer |
| **Desarrollo Frontend** | 5 días | Templates, CSS, JavaScript |
| **Integración** | 2 días | Backend + Frontend + Contenido |
| **Pruebas** | 3 días | Unit, Integration, Manual |
| **Deploy** | 1 día | Render setup, migrations |
| **Documentación** | 1 día | API docs, User guide |
| **TOTAL** | **~24 días (4 semanas)** | v0.30.0 en producción |

**Nota**: Timeline para desarrollo solo con AI Agent. Desarrollo paralelo de múltiples features no es posible.

### 1.5 Presupuesto

**Costo Total: $0 USD**

| Recurso | Proveedor | Costo |
|---------|-----------|-------|
| Hosting Web | Render Free Tier | $0 |
| Database | PostgreSQL (Render) | $0 |
| Domain | Render subdomain | $0 |
| Git Hosting | GitHub | $0 |
| Desarrollo | Equipo (voluntario) | $0 |

**Limitaciones Free Tier:**
- 750 horas/mes de uptime
- App se "duerme" tras 15 min inactividad
- 1GB RAM, 0.5 CPU
- Suficiente para 10-20 usuarios concurrentes

---

## Fase 2: Análisis de Requerimientos

### 2.1 Requerimientos Funcionales

#### RF-001: Renderizado Dinámico de Markdown
- **Prioridad**: Crítica
- **Descripción**: La plataforma debe leer archivos `.md` del repositorio y renderizarlos como HTML.
- **Criterios de Aceptación**:
  - Soporta sintaxis Markdown estándar (headers, listas, code blocks)
  - Soporta tablas y emojis
  - Mantiene enlaces relativos funcionales
  - Renderiza en < 200ms

#### RF-002: Autenticación de Usuarios
- **Prioridad**: Alta
- **Descripción**: Los usuarios del equipo pueden registrarse e iniciar sesión.
- **Criterios de Aceptación**:
  - Registro con nombre, email, contraseña
  - Login con email/password
  - Sesión persistente (JWT)
  - Logout funcional
  - Contraseñas hasheadas (bcrypt)

#### RF-003: Dashboard Personal
- **Prioridad**: Alta
- **Descripción**: Cada usuario ve su progreso del Sprint actual.
- **Criterios de Aceptación**:
  - Muestra % de completitud
  - Lista tareas por categoría (Superbadges, Prácticas)
  - Indica estado (Not Started, In Progress, Completed)
  - Muestra deadline del Sprint

#### RF-004: Tracking de Progreso
- **Prioridad**: Alta
- **Descripción**: Los usuarios pueden marcar tareas como completadas.
- **Criterios de Aceptación**:
  - Click en checkbox marca tarea
  - Estado se guarda en base de datos
  - Timestamp de inicio y completitud
  - Progreso se actualiza automáticamente

#### RF-005: Vista de Equipo
- **Prioridad**: Media
- **Descripción**: Los usuarios ven el progreso de sus compañeros.
- **Criterios de Aceptación**:
  - Tabla con todos los miembros
  - % de progreso de cada uno
  - Ordenable por progreso
  - Actualización automática (polling 30s)

#### RF-006: Navegación Jerárquica
- **Prioridad**: Alta
- **Descripción**: Navegación igual que en v0.25.0 (Curriculum → Sprint → Semana → Clase).
- **Criterios de Aceptación**:
  - Breadcrumbs funcionales
  - Sidebar con índice
  - Botones "Anterior" / "Siguiente"
  - Links entre documentos funcionan

#### RF-007: Gestión de Contenido
- **Prioridad**: Media
- **Descripción**: Los instructores pueden actualizar contenido editando Markdown.
- **Criterios de Aceptación**:
  - Git push actualiza contenido automáticamente
  - Webhook de GitHub dispara refresh
  - O polling cada 5 minutos
  - Sin necesidad de redeploy

### 2.2 Requerimientos No Funcionales

#### RNF-001: Performance
- Tiempo de carga inicial: < 2 segundos
- Renderizado de Markdown: < 200ms
- Respuesta de API: < 300ms (p95)
- Soporte para 20 usuarios concurrentes

#### RNF-002: Seguridad
- Contraseñas hasheadas con bcrypt (cost 12)
- JWT tokens con expiración de 7 días
- HTTPS obligatorio en producción
- Validación de inputs (SQL injection, XSS)
- CORS configurado correctamente

#### RNF-003: Usabilidad
- Interfaz responsive (mobile-first)
- Accesibilidad WCAG 2.1 AA
- Mensajes de error claros
- Feedback visual inmediato

#### RNF-004: Mantenibilidad
- Código documentado (docstrings)
- Tests con coverage > 75%
- Logs estructurados (JSON)
- Separación de concerns (MVC)

#### RNF-005: Escalabilidad
- Arquitectura preparada para 100+ usuarios
- Base de datos normalizada (3NF)
- Caché de Markdown renderizado (Redis en v0.40.0)
- Paginación en listas largas

#### RNF-006: Disponibilidad
- Uptime > 95% (limitación free tier)
- Tiempo de "wake up" < 30s
- Backup de DB automático (Render)

### 2.3 User Stories

#### US-001: Como estudiante, quiero ver el contenido del curso renderizado
```gherkin
Given que estoy autenticado
When navego a "Curriculum → Sprint 1 → Semana 1 → Clase 1 Teoría"
Then veo el contenido Markdown renderizado como HTML
And veo un sidebar con el índice de la clase
And veo breadcrumbs de navegación
And veo botones "Anterior" y "Siguiente"
```

#### US-002: Como estudiante, quiero marcar una clase como completada
```gherkin
Given que estoy viendo una clase
When marco el checkbox "Clase completada"
Then el sistema guarda mi progreso en la base de datos
And mi % de progreso del Sprint se actualiza
And el checkbox permanece marcado al recargar la página
```

#### US-003: Como estudiante, quiero ver mi progreso general
```gherkin
Given que estoy en el dashboard
When veo la sección "Mi Progreso"
Then veo mi % de completitud del Sprint 1
And veo cuántas clases he completado
And veo cuántos Superbadges he terminado
And veo cuántos días quedan para el deadline
```

#### US-004: Como estudiante, quiero comparar mi progreso con el equipo
```gherkin
Given que estoy en el dashboard
When navego a la pestaña "Equipo"
Then veo una tabla con todos los miembros
And veo el % de progreso de cada uno
And veo mi posición en el ranking
And la tabla se actualiza automáticamente cada 30 segundos
```

#### US-005: Como instructor, quiero actualizar el contenido
```gherkin
Given que tengo acceso al repositorio
When edito un archivo Markdown y hago git push
Then la plataforma detecta el cambio (webhook o polling)
And actualiza el contenido automáticamente
And los usuarios ven el nuevo contenido sin necesidad de redeploy
```

---

## Fase 3: Diseño

### 3.1 Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────┐
│                    USUARIOS (Web Browser)               │
└────────────────────────┬────────────────────────────────┘
                         │ HTTPS
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  RENDER WEB SERVICE                     │
│  ┌───────────────────────────────────────────────────┐  │
│  │           FASTAPI APPLICATION                     │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │  Routers                                    │  │  │
│  │  │  ├─ /auth (login, register, logout)        │  │  │
│  │  │  ├─ /docs (render markdown)                │  │  │
│  │  │  ├─ /progress (track user progress)        │  │  │
│  │  │  └─ /api (REST endpoints)                  │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │  Services (Business Logic)                  │  │  │
│  │  │  ├─ MarkdownRenderer                        │  │  │
│  │  │  ├─ AuthService                             │  │  │
│  │  │  └─ ProgressService                         │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │  Models (SQLAlchemy ORM)                    │  │  │
│  │  │  ├─ User                                    │  │  │
│  │  │  ├─ Sprint                                  │  │  │
│  │  │  ├─ Task                                    │  │  │
│  │  │  └─ UserProgress                            │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │  Templates (Jinja2)                         │  │  │
│  │  │  ├─ base.html                               │  │  │
│  │  │  ├─ dashboard.html                          │  │  │
│  │  │  ├─ doc_viewer.html                         │  │  │
│  │  │  └─ team.html                               │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────┘
                         │ SQL
                         ▼
┌─────────────────────────────────────────────────────────┐
│              RENDER POSTGRESQL DATABASE                 │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Tables:                                          │  │
│  │  ├─ users                                         │  │
│  │  ├─ sprints                                       │  │
│  │  ├─ tasks                                         │  │
│  │  └─ user_progress                                 │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                  GITHUB REPOSITORY                      │
│  (Contenido Markdown - Source of Truth)                │
│  ├─ curriculum/                                         │
│  ├─ Superbadges/                                        │
│  ├─ Practica_Financiera/                                │
│  └─ Gestor_de_Versiones/                                │
└────────────────────────┬────────────────────────────────┘
                         │ Git Pull / Webhook
                         ▼
                   [FastAPI App]
```

### 3.2 Modelo de Datos (Database Schema)

```sql
-- users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    team VARCHAR(50) DEFAULT 'VISIONARY ADMINS',
    role VARCHAR(20) DEFAULT 'student', -- 'student', 'instructor', 'admin'
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- sprints table
CREATE TABLE sprints (
    id SERIAL PRIMARY KEY,
    number INTEGER NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- tasks table (auto-generated from Markdown structure)
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    sprint_id INTEGER REFERENCES sprints(id) ON DELETE CASCADE,
    category VARCHAR(50) NOT NULL, -- 'Clase', 'Superbadge', 'Practica'
    title VARCHAR(200) NOT NULL,
    description TEXT,
    markdown_path VARCHAR(500) NOT NULL, -- Path relativo al repo
    order_index INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(sprint_id, markdown_path)
);

-- user_progress table
CREATE TABLE user_progress (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    task_id INTEGER REFERENCES tasks(id) ON DELETE CASCADE,
    status VARCHAR(20) DEFAULT 'not_started', -- 'not_started', 'in_progress', 'completed'
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, task_id)
);

-- indexes for performance
CREATE INDEX idx_user_progress_user_id ON user_progress(user_id);
CREATE INDEX idx_user_progress_task_id ON user_progress(task_id);
CREATE INDEX idx_user_progress_status ON user_progress(status);
CREATE INDEX idx_tasks_sprint_id ON tasks(sprint_id);
CREATE INDEX idx_tasks_markdown_path ON tasks(markdown_path);
CREATE INDEX idx_users_email ON users(email);
```

### 3.3 API Endpoints

#### Autenticación
```
POST   /api/auth/register          - Registrar nuevo usuario
POST   /api/auth/login             - Iniciar sesión (retorna JWT)
POST   /api/auth/logout            - Cerrar sesión
GET    /api/auth/me                - Obtener usuario actual
```

#### Renderizado de Documentos
```
GET    /docs/{path:path}           - Renderizar Markdown dinámicamente
                                     Ejemplo: /docs/curriculum/sprint_01/semana_01/01-clase_1_teoria
```

#### Progreso
```
GET    /api/progress/me            - Progreso del usuario actual
GET    /api/progress/team          - Progreso de todo el equipo
POST   /api/progress/task/{task_id}/mark - Marcar tarea (toggle status)
PATCH  /api/progress/{id}          - Actualizar notas de tarea
```

#### Sprints y Tareas
```
GET    /api/sprints                - Listar todos los sprints
GET    /api/sprints/{id}           - Obtener sprint específico
GET    /api/sprints/{id}/tasks     - Obtener tareas del sprint
GET    /api/tasks/{id}             - Obtener tarea específica
```

#### Usuarios (Admin only)
```
GET    /api/users                  - Listar todos los usuarios
GET    /api/users/{id}             - Obtener usuario específico
PATCH  /api/users/{id}             - Actualizar usuario
DELETE /api/users/{id}             - Desactivar usuario
```

### 3.4 Estructura del Proyecto (Refactorizada)

```
salesforce_admin/
├── app/                           # Aplicación FastAPI
│   ├── __init__.py
│   ├── main.py                    # Entry point
│   ├── config.py                  # Configuración (env vars)
│   ├── database.py                # DB connection
│   ├── dependencies.py            # Dependency injection
│   ├── models/                    # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── sprint.py
│   │   ├── task.py
│   │   └── progress.py
│   ├── schemas/                   # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── sprint.py
│   │   ├── task.py
│   │   └── progress.py
│   ├── routers/                   # API routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── docs.py                # Markdown rendering
│   │   ├── progress.py
│   │   ├── sprints.py
│   │   └── users.py
│   ├── services/                  # Business logic
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── markdown_service.py    # Markdown → HTML
│   │   ├── progress_service.py
│   │   └── task_service.py
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── cors.py
│   │   └── logging.py
│   ├── templates/                 # Jinja2 templates
│   │   ├── base.html
│   │   ├── components/
│   │   │   ├── navbar.html
│   │   │   ├── sidebar.html
│   │   │   └── breadcrumbs.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── dashboard.html
│   │   ├── doc_viewer.html        # Renderiza Markdown
│   │   └── team.html
│   └── static/                    # Assets estáticos
│       ├── css/
│       │   ├── tailwind.css
│       │   └── custom.css
│       ├── js/
│       │   ├── alpine.js
│       │   └── app.js
│       └── images/
├── content/                       # Contenido Markdown (sin cambios)
│   ├── curriculum/
│   ├── Superbadges/
│   ├── Practica_Financiera/
│   └── Gestor_de_Versiones/
├── tests/                         # Tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_markdown.py
│   ├── test_progress.py
│   └── test_api.py
├── alembic/                       # DB migrations
│   ├── versions/
│   └── env.py
├── docs/                          # Documentación del proyecto
│   ├── SDLC.md                    # Este documento
│   ├── DEVELOPMENT_RULES.md       # Reglas de desarrollo
│   ├── ROADMAP.md                 # Roadmap del proyecto
│   ├── TASK_LIST.md               # Lista de tareas
│   ├── IMPLEMENTATION_PLAN.md     # Plan de implementación
│   ├── API.md                     # Documentación de API
│   └── DEPLOYMENT.md              # Guía de deploy
├── scripts/                       # Scripts de utilidad
│   ├── seed_data.py               # Cargar datos iniciales
│   ├── sync_tasks.py              # Sincronizar tareas desde Markdown
│   └── backup_db.py               # Backup de base de datos
├── .env.example                   # Ejemplo de variables de entorno
├── .gitignore
├── requirements.txt               # Dependencias Python
├── docker-compose.yml             # Para desarrollo local
├── render.yaml                    # Configuración de Render
└── README.md                      # README principal

```

---

## Fase 4: Desarrollo

### 4.1 Stack Tecnológico

| Capa | Tecnología | Versión | Justificación |
|------|------------|---------|---------------|
| **Backend** | FastAPI | 0.109+ | Async, rápido, autodocumentación |
| **ORM** | SQLAlchemy | 2.0+ | ORM maduro, async support |
| **Database** | PostgreSQL | 15+ | Relacional, robusto |
| **Auth** | python-jose | 3.3+ | JWT tokens |
| **Password** | passlib[bcrypt] | 1.7+ | Bcrypt hashing |
| **Markdown** | python-markdown | 3.5+ | Markdown → HTML |
| **Templates** | Jinja2 | 3.1+ | Server-side rendering |
| **JS Framework** | Alpine.js | 3.13+ | Interactividad (3KB) |
| **CSS** | TailwindCSS | 3.4+ | Utility-first |
| **Testing** | pytest | 7.4+ | Unit & integration tests |
| **Migrations** | Alembic | 1.13+ | DB schema versioning |
| **Deploy** | Render | - | Free tier, auto-deploy |

### 4.2 Convenciones de Código

#### Python (PEP 8 + Black + isort)
```python
# Imports ordenados (isort)
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService

# Naming conventions
class UserService:                    # PascalCase para clases
    def get_user_by_email(self):      # snake_case para métodos
        user_email = "test@example.com"  # snake_case para variables

# Type hints obligatorios
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
) -> User:
    """
    Crea un nuevo usuario en el sistema.
    
    Args:
        user_data: Datos del usuario a crear
        db: Sesión de base de datos
        
    Returns:
        User: Usuario creado
        
    Raises:
        ValueError: Si el email ya existe
    """
    pass

# Constants en UPPER_CASE
MAX_LOGIN_ATTEMPTS = 5
DEFAULT_PAGE_SIZE = 20
```

#### Git Commits (Conventional Commits)
```
feat(auth): add JWT token refresh endpoint
fix(markdown): correct relative link resolution
docs(api): update progress endpoints documentation
test(users): add unit tests for user service
refactor(models): simplify user_progress relationship
style(frontend): format templates with prettier
chore(deps): update fastapi to 0.109.0
```

### 4.3 Proceso de Desarrollo

#### Workflow de Git
```
main (production)
  ↑
develop (staging)
  ↑
feature/add-markdown-renderer
feature/implement-auth
hotfix/fix-login-error
```

#### Pull Request Template
```markdown
## Descripción
[Descripción clara de los cambios]

## Tipo de cambio
- [ ] Bug fix
- [ ] Nueva feature
- [ ] Breaking change
- [ ] Documentación

## Checklist
- [ ] Tests agregados/actualizados
- [ ] Documentación actualizada
- [ ] Code review solicitado
- [ ] CI/CD pasa
```

---

## Fase 5: Pruebas

### 5.1 Estrategia de Testing

```
        /\
       /  \      E2E Tests (5%)
      /────\     - Playwright
     /      \    - User flows críticos
    /────────\   
   /          \  Integration Tests (20%)
  /────────────\ - API endpoints
 /              \- DB queries
/────────────────\
  Unit Tests (75%)
  - Services
  - Models
  - Utilities
```

### 5.2 Coverage Goal

**Mínimo aceptable**: 75% coverage  
**Objetivo**: 85% coverage

```bash
pytest --cov=app --cov-report=html --cov-report=term
```

---

## Fase 6: Implementación (Deployment)

### 6.1 Proceso de Deploy en Render

#### render.yaml
```yaml
services:
  - type: web
    name: salesforce-admin-platform
    env: python
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

databases:
  - name: salesforce-admin-db
    databaseName: salesforce_admin
    user: admin
```

### 6.2 Checklist Pre-Deploy

- [ ] Todos los tests pasan
- [ ] Coverage > 75%
- [ ] Variables de entorno configuradas
- [ ] Database migrations ejecutadas
- [ ] Seed data cargado
- [ ] HTTPS configurado
- [ ] CORS configurado
- [ ] Logs funcionando

---

## Fase 7: Mantenimiento

### 7.1 Monitoreo

**Métricas:**
- Uptime > 95%
- Response time p95 < 500ms
- Error rate < 1%
- Active users/day

**Herramientas:**
- Render built-in logs
- Sentry (opcional, free tier)

### 7.2 Backup Strategy

- **Database**: Render backup automático diario
- **Código**: GitHub (source of truth)
- **Contenido**: Git (versionado)

---

## 📊 Métricas de Éxito

| Métrica | Objetivo v0.30.0 |
|---------|------------------|
| **Adopción** | 90% del equipo usa la plataforma |
| **Engagement** | Usuarios activos 4+ veces/semana |
| **Performance** | 95% requests < 500ms |
| **Bugs** | < 3 bugs críticos en primer mes |
| **Satisfacción** | NPS > 8/10 |

---

**Documento creado por**: Equipo VISIONARY ADMINS  
**Última actualización**: 17 Enero 2026  
**Versión**: 1.0

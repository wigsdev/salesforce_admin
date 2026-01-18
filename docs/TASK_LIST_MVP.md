# ✅ TASK LIST - Web Platform Migration (v0.30.0)

**Proyecto**: Salesforce Admin Learning Platform  
**Sprint**: Migration to Web Platform  
**Fecha inicio**: 17 Enero 2026  
**Fecha objetivo**: 14 Febrero 2026 (4 semanas)  
**Última actualización**: 17 Enero 2026

---

## 📊 Progreso General

**Total**: 25/45 tareas (56%)

- 📋 Planning: 5/5 (100%) ✅
- 🏗️ Infrastructure: 8/8 (100%) ✅
- 🔐 Authentication: 7/7 (100%) ✅
- 📄 Markdown Rendering: 5/5 (100%) ✅
- 📊 Progress Tracking: 0/6 (0%)
- 🎨 Frontend: 0/7 (0%)
- 🧪 Testing: 0/4 (0%)
- 🚀 Deployment: 0/3 (0%)

**Última actualización**: 18 Enero 2026 - 00:05  
**Estado**: Fase 4 completada, iniciando Fase 5 (Progress Tracking)

---

## 📋 FASE 1: Planning & Documentation ✅ COMPLETA (5/5 tareas)

- [x] Crear SDLC.md
- [x] Crear DEVELOPMENT_RULES.md
- [x] Crear ROADMAP.md
- [x] Crear AI_ROLE_FRAMEWORK.md
- [x] Crear TASK_LIST_MVP.md (este archivo)
- [x] Crear IMPLEMENTATION_PLAN.md

---

## 🏗️ FASE 2: Infrastructure Setup ✅ COMPLETA (8/8 tareas)

### Refactorización de Estructura
- [x] Crear estructura de carpetas `app/`
- [x] Mover contenido a `content/`
- [x] Crear `requirements.txt` (actualizado para Python 3.13)
- [x] Crear `docker-compose.yml` para desarrollo local
- [x] Crear `.env.example`

### Base de Datos
- [x] Configurar SQLAlchemy con psycopg v3
- [x] Crear modelos (User, Sprint, Task, UserProgress)
- [x] Setup Alembic para migrations

---

## 🔐 FASE 3: Authentication ✅ COMPLETA (7/7 tareas)

- [x] Implementar modelo User con campos de autenticación
- [x] Implementar hash de passwords (bcrypt 4.0.1)
- [x] Implementar JWT tokens (7 días de expiración)
- [x] Crear endpoint `/api/auth/register`
- [x] Crear endpoint `/api/auth/login`
- [x] Crear endpoint `/api/users/me` (protegido)
- [x] Crear AuthService y security utilities

---

## 📄 FASE 4: Markdown Rendering ✅ COMPLETA (5/5 tareas)

- [x] Instalar python-markdown
- [x] Crear MarkdownService con lectura de archivos .md
- [x] Implementar conversión Markdown → HTML con TOC
- [x] Crear endpoint `/docs/browse` para navegación
- [x] Crear endpoint `/docs/{path}` para visualización
- [x] Crear templates `doc_viewer.html` y `docs_browser.html`
- [x] Resolver links relativos y breadcrumbs

---

## 📊 FASE 5: Progress Tracking (8 tareas)

### Backend
- [ ] Implementar modelo Sprint
- [ ] Implementar modelo Task
- [ ] Implementar modelo UserProgress
- [ ] Crear endpoint `/api/progress/me`
- [ ] Crear endpoint `/api/progress/team`
- [ ] Crear endpoint `/api/progress/task/{id}/mark`

### Frontend
- [ ] Crear dashboard.html
- [ ] Implementar checkboxes interactivos (Alpine.js)

---

## 🎨 FASE 6: Frontend (6 tareas)

- [ ] Setup TailwindCSS
- [ ] Crear `base.html` template
- [ ] Crear componentes (navbar, sidebar, breadcrumbs)
- [ ] Crear `login.html` y `register.html`
- [ ] Crear `team.html`
- [ ] Implementar navegación jerárquica

---

## 🧪 FASE 7: Testing (3 tareas)

- [ ] Escribir unit tests (coverage > 75%)
- [ ] Escribir integration tests (API endpoints)
- [ ] Manual testing checklist

---

## 🚀 FASE 8: Deployment (2 tareas)

- [ ] Configurar Render (render.yaml)
- [ ] Deploy a producción
- [ ] Verificar funcionamiento

---

## 📝 Tareas Detalladas

### TASK-001: Crear estructura de carpetas `app/`
**Prioridad**: Alta  
**Estimación**: 1 hora  
**Asignado**: Tech Lead  
**Dependencias**: Ninguna

**Descripción**:
Crear la estructura completa de carpetas según `docs/SDLC.md`.

**Criterios de Aceptación**:
- [ ] Carpetas `app/models/`, `app/routers/`, `app/services/` creadas
- [ ] Carpetas `app/templates/`, `app/static/` creadas
- [ ] Archivos `__init__.py` en todos los módulos
- [ ] `app/main.py` con FastAPI app básica

---

### TASK-002: Mover contenido a `content/`
**Prioridad**: Alta  
**Estimación**: 30 min  
**Asignado**: Developer  
**Dependencias**: TASK-001

**Descripción**:
Mover carpetas de contenido Markdown a `content/`.

**Criterios de Aceptación**:
- [ ] `curriculum/` → `content/curriculum/`
- [ ] `Superbadges/` → `content/Superbadges/`
- [ ] `Practica_Financiera/` → `content/Practica_Financiera/`
- [ ] `Gestor_de_Versiones/` → `content/Gestor_de_Versiones/`
- [ ] Git history preservado (usar `git mv`)

---

### TASK-003: Configurar SQLAlchemy
**Prioridad**: Alta  
**Estimación**: 2 horas  
**Asignado**: Backend Developer  
**Dependencias**: TASK-001

**Descripción**:
Setup de SQLAlchemy con async support.

**Criterios de Aceptación**:
- [ ] `app/database.py` creado
- [ ] Connection pool configurado
- [ ] Session dependency creado
- [ ] Funciona con PostgreSQL

---

### TASK-004: Implementar modelo User
**Prioridad**: Alta  
**Estimación**: 2 horas  
**Asignado**: Backend Developer  
**Dependencias**: TASK-003

**Descripción**:
Crear modelo User con todos los campos necesarios.

**Criterios de Aceptación**:
- [ ] `app/models/user.py` creado
- [ ] Campos: id, name, email, password_hash, team, role
- [ ] Timestamps: created_at, updated_at, last_login
- [ ] Schema Pydantic correspondiente

---

### TASK-005: Implementar JWT tokens
**Prioridad**: Alta  
**Estimación**: 3 horas  
**Asignado**: Backend Developer  
**Dependencias**: TASK-004

**Descripción**:
Sistema de autenticación con JWT.

**Criterios de Aceptación**:
- [ ] `app/services/auth_service.py` creado
- [ ] Función `create_access_token()`
- [ ] Función `verify_token()`
- [ ] Middleware de autenticación
- [ ] Dependency `get_current_user()`

---

### TASK-006: Crear MarkdownService
**Prioridad**: Alta  
**Estimación**: 4 horas  
**Asignado**: Backend Developer  
**Dependencias**: TASK-001

**Descripción**:
Servicio para renderizar Markdown dinámicamente.

**Criterios de Aceptación**:
- [ ] `app/services/markdown_service.py` creado
- [ ] Función `render_markdown(path: str) -> str`
- [ ] Soporta sintaxis Markdown estándar
- [ ] Resuelve links relativos correctamente
- [ ] Maneja errores (archivo no encontrado)

---

### TASK-007: Crear dashboard.html
**Prioridad**: Alta  
**Estimación**: 4 horas  
**Asignado**: Frontend Developer  
**Dependencias**: TASK-005, TASK-006

**Descripción**:
Dashboard principal con progreso del usuario.

**Criterios de Aceptación**:
- [ ] Muestra % de progreso del Sprint actual
- [ ] Lista tareas por categoría
- [ ] Checkboxes funcionales (Alpine.js)
- [ ] Responsive design
- [ ] Breadcrumbs de navegación

---

### TASK-008: Escribir unit tests
**Prioridad**: Media  
**Estimación**: 6 horas  
**Asignado**: QA + Developers  
**Dependencias**: Todas las features implementadas

**Descripción**:
Tests unitarios para servicios y modelos.

**Criterios de Aceptación**:
- [ ] Tests para AuthService
- [ ] Tests para MarkdownService
- [ ] Tests para ProgressService
- [ ] Coverage > 75%
- [ ] Todos los tests pasan

---

### TASK-009: Deploy a Render
**Prioridad**: Alta  
**Estimación**: 3 horas  
**Asignado**: Tech Lead  
**Dependencias**: Todos los tests pasan

**Descripción**:
Despliegue inicial a producción en Render.

**Criterios de Aceptación**:
- [ ] `render.yaml` configurado
- [ ] Variables de entorno configuradas
- [ ] Database migrations ejecutadas
- [ ] Seed data cargado
- [ ] App accesible en URL de Render
- [ ] Health check funciona

---

## 📅 Sprint Planning

### Semana 1 (20-24 Enero)
- Planning & Documentation
- Infrastructure Setup
- Authentication (inicio)

### Semana 2 (27-31 Enero)
- Authentication (completar)
- Markdown Rendering
- Progress Tracking (inicio)

### Semana 3 (3-7 Febrero)
- Progress Tracking (completar)
- Frontend
- Testing (inicio)

### Semana 4 (10-14 Febrero)
- Testing (completar)
- Deployment
- Bug fixes y polish

---

## 🚨 Bloqueadores Actuales

Ninguno

---

## 📝 Notas

- Este task list se actualizará diariamente
- Nuevas tareas pueden agregarse según necesidad
- Prioridades pueden cambiar según feedback

---

**Creado por**: Tech Lead  
**Versión**: 1.0

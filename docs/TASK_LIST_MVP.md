# ✅ TASK LIST - Web Platform Migration (v0.32.0)

**Proyecto**: Salesforce Admin Learning Platform  
**Sprint**: Migration to Web Platform  
**Fecha inicio**: 17 Enero 2026  
**Fecha objetivo**: 14 Febrero 2026 (4 semanas)  
**Última actualización**: 30 Enero 2026

---

## 📊 Progreso General

**Total**: 45/45 tareas MVP Original (100%) + FASE 2 Iniciada

- 📋 Planning: 5/5 (100%) ✅
- 🏗️ Infrastructure: 8/8 (100%) ✅
- 🔐 Authentication: 7/7 (100%) ✅
- 📄 Markdown Rendering: 5/5 (100%) ✅
- 📊 Progress Tracking: 6/6 (100%) ✅
- 🎨 Frontend Polish: 7/7 (100%) ✅
- 🧪 Testing: 4/4 (100%) ✅
- 🚀 Deployment: 3/3 (100%) ✅

**Última actualización**: 30 Enero 2026
**Estado**: MVP Completado. Fase de Mejora Continua (Phase 2 & Lumina Tech) activa.

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

## 📊 FASE 5: Progress Tracking ✅ COMPLETA (6/6 tareas)

### Backend
- [x] Implementar modelo Sprint
- [x] Implementar modelo Task
- [x] Implementar modelo UserProgress
- [x] Crear endpoint `/api/progress/me`
- [x] Crear endpoint `/api/progress/team`
- [x] Crear endpoint `/api/progress/task/{id}/mark`

### Frontend
- [x] Crear dashboard.html
- [x] Implementar checkboxes interactivos (Alpine.js)

---

## 🎨 FASE 6: Frontend ✅ COMPLETA (7/7 tareas)
- [x] Setup TailwindCSS (Migrado a CLI v4 Professional)
- [x] Crear `base.html` template
- [x] Crear componentes (navbar, sidebar, breadcrumbs)
- [x] Crear `login.html` y `register.html`
- [x] Crear `team.html` (Integrado en Dashboard como Role View)
- [x] Implementar navegación jerárquica
- [x] **Lumina Dyanmic Dashboard** (CRUD + Strict Curriculum)

---

## 🧪 FASE 7: Testing & Quality ✅ COMPLETA (3/3 tareas)
- [x] Escribir unit tests (Security & Services)
- [x] Escribir integration tests (Auth API Endpoints)
- [x] **Crear Scripts de Debug y Seed Data** (scripts/seed_data.py, debug_auth.py)

---

## 🚀 FASE 8: Deployment & Professionalization ✅ COMPLETA (3/3 tareas)
- [x] Migrar Tailwind CDN a CLI (Build Process implementado)
- [x] Configurar Render (render.yaml)
- [x] **Deploy a producción (Verificado)**

---

## 🏗️ Phase 2: Improvement & Polish 🚀 (En Progreso)
- [ ] **Experiencia Mobile First (UX/UI)**
    - [x] 📄 Documentar Guías de Diseño Responsivo
    - [x] Refactorizar Tablas para scroll horizontal/cards
    - [x] Implementar Menú Hamburguesa en Navbar
    - [x] Ajustar tamaños de fuente y paddings táctiles
    - [x] Refinar Navegación Móvil (Trello-style & Compact Header)
    - [x] Refactorizar Layout DocViewer (Grid Areas & Alineación)
    - [x] Implementar Toast Notifications (Feedback Visual)
    - [x] Añadir Skeleton Loaders
- [ ] **Dark Mode**
    - [x] Implementar Toggle de tema (Persistente)
    - [x] Configurar paleta Dark Mode en Tailwind
- [ ] **Nuevos Dashboards**
    - [x] **Dashboard de Proyecto: Lumina Tech (v2 DB) 📊**
        - [x] Modelos: `LuminaDeliverable` & `LuminaTask` (SQLAlchemy)
        - [x] Migraciones: Alembic
        - [x] Backend: `SyncService` (Soporte Exclusiones, Pesos y Contenido Auto-Inyectado)
        - [x] API: `POST /tasks/{id}/toggle`
        - [x] Frontend: V2 (Acordeón, Reactividad sin recarga, UX limpia)
        - [x] Integración: Conexión dinámica con Markdown (`Checklist_por_dia.md`)
- [ ] **Limpieza y Contenido**
    - [x] Estandarizar Guía Trello (7 Historias de Usuario)
    - [x] Script de limpieza de Markdown (eliminar 'volver inicio')
    - [x] Implementar escaneo recursivo de contenido

---

## 🏛️ Proyecto Especial: Lumina Tech ✅
- [x] **Análisis y Diseño (Día 0)**
    - [x] Formatear Requerimientos (BA & Roles)
    - [x] Crear Checklist Maestro (`Checklist_por_dia.md`)
    - [x] Consolidar en Gestor de Versiones (`00`, `01`, `02`, `03`, `04`)
- [x] **Modelo de Datos Core (Día 1)**
    - [x] 📝 Draft: Historias de Usuario (`dia_1/Historias_de_Usuario_Dia_1.md`)
    - [x] 📂 Consolidar: Actualizar `01-Business_Analyst` (HU Backlog)
- [x] **Consolidación Documental (Cleanup)**
    - [x] Poblar `Gestor_de_Versiones` con Bitácoras de Ejecución
    - [x] Mover archivos sueltos a `Archivos_intermedios` (Limpieza Root)
    - [x] Consolidar `MASTER_INDEX` en `Archivos_intermedios`
    - [x] Versionar Material Curriculum (Semana 4)
- [x] **Mejoras Dashboard (Feedback & Robustez)**
    - [x] DB schema: `LuminaDeliverable.source_link`
    - [x] Seed: Parsear `**Fuente**` regex
    - [x] API: Exponer nuevo campo
    - [x] Frontend: Mostrar botón "Ver Clase"
    - [x] UI Polish: Ocultar Log, Fuente custom y Botones pequeños
    - [x] **Persistencia Inteligente (Smart Sync)**: Seed script actualiza en vez de borrar.
    - [x] **Atomic Transactions**: Seed script usa rollback ante fallos (Deployment Safety).

---

## 🚨 Bloqueadores Actuales

Ninguno

---

## 📝 Notas

- Este task list se actualiza con cada hito.
- Version aligned with internal Logic.

---

**Creado por**: Tech Lead  
**Versión**: 1.2

# CHANGELOG

All notable changes to the Salesforce Admin Learning Platform project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.31.0] - 2026-01-19
### Added
- **Mobile First UX**:
  - Implementado menú "Hamburguesa" responsivo en la barra de navegación para móviles.
  - Diseño de tarjetas de tareas apilables (`flex-col`) para mejorar la vista en pantallas pequeñas.
  - Aumentados los tamaños de objetivos táctiles (botones, checkboxes) para facilitar el uso en móviles.
- **Feedback Visual**:
  - Sistema de notificaciones "Toast" flotantes para feedback inmediato (Éxito/Error).
  - Integración de notificaciones al completar/desmarcar tareas.

## [Unreleased]

### Added
- **Database Models** (Phase 3)
  - User model with authentication fields (email, password_hash, role, team)
  - Sprint model for course structure (number, name, dates, is_active)
  - Task model for content items (title, category, markdown_path, sprint relationship)
  - UserProgress model for completion tracking (status, timestamps, notes)
  - All models with proper relationships, indexes, and constraints

- **Alembic Migrations**
  - Initial migration (001_initial) with all 4 tables
  - Configured env.py with psycopg dialect conversion
  - Migration applied successfully to PostgreSQL

- **Authentication System**
  - JWT token generation with 7-day expiration (HS256 algorithm)
  - Password hashing with bcrypt (cost factor 12)
  - Security utilities (hash_password, verify_password, create_access_token, verify_token)
  - AuthService for user registration and login
  - Last login timestamp tracking

- **API Endpoints**
  - `POST /api/auth/register` - User registration with email uniqueness validation
  - `POST /api/auth/login` - User login returning JWT access token
  - `POST /api/auth/logout` - Logout endpoint (client-side token removal)
  - `GET /api/users/me` - Get current authenticated user (protected endpoint)

- **Pydantic Schemas**
  - UserCreate, UserLogin, UserResponse, UserUpdate schemas
  - TokenResponse and TokenData schemas
  - Email validation and password length constraints (8-72 chars)

- **Markdown Rendering System** (Phase 4)
  - MarkdownService for reading and converting .md files to HTML
  - Support for tables, fenced code, syntax highlighting, and TOC generation
  - Directory listing and file browsing capabilities
  - Title extraction from H1 headers or filenames
  
- **Documentation Endpoints**
  - `GET /docs/browse` - Browse documentation directory with folder navigation
  - `GET /docs/{path}` - View markdown document rendered as HTML
  
- **Progress Tracking System** (Phase 5)
  - `ProgressService` for managing user task completion
  - REST API endpoints for user, sprint, and team progress
  - Automatic timestamp tracking (started_at, completed_at)
  - Status validation (not_started, in_progress, completed)
  - Seed data script for initial content population

- **Frontend Dashboard**
  - Interactive Dashboard with Alpine.js
  - Real-time progress stats calculation
  - Task completion toggling with optimistic UI updates
  - Login page with JWT token management and error handling
  - Responsive layout with navigation bar and sprint visualization

- **Frontend Polish & Unification** (Phase 6)
  - Unified Design System with Vanilla CSS (`styles.css`)
  - `base.html` Jinja2 template for consistent layout and navigation
  - Full Authentication Flow: Login and **Registration** (`/register`)
  - Refactored `dashboard.html` with responsive grid layout
  - Improved Documentation Browser with folder/file icons
  - Enhanced Document Viewer with Table of Contents sidebar
  - Responsive design for mobile devices

- **Documentation Templates**
  - `doc_viewer.html` - Render markdown with TOC sidebar and breadcrumbs
  - `docs_browser.html` - Directory navigation interface with file/folder icons
  - Responsive design with purple gradient theme
  - Clean, modern UI with proper typography

- **Infrastructure** (Phase 2)
  - Complete project structure (app/, content/, tests/, alembic/, scripts/)
  - Docker Compose configuration for local PostgreSQL
  - FastAPI application with CORS, static files, and Jinja2 templates
  - Environment configuration with .env support
  - Dependency injection for database sessions and authentication

### Changed
- Updated SQLAlchemy from 2.0.25 to 2.0.36 for Python 3.13 compatibility
- Updated Pydantic from 2.5.3 to 2.10.5 (pre-built wheels for Python 3.13)
- Updated FastAPI from 0.109.0 to 0.115.6 (Pydantic 2.10 compatible)
- Moved content directories (curriculum/, Superbadges/, etc.) to `content/` folder
- Database URL auto-conversion to postgresql+psycopg:// dialect

### Fixed
- psycopg2 compatibility by migrating to psycopg v3 (3.2.3)
- bcrypt version pinned to 4.0.1 for passlib 1.7.4 compatibility
- ALLOWED_ORIGINS parsing from comma-separated .env string
- Password max length validation (72 bytes for bcrypt)
- SQLAlchemy TypingOnly inheritance error with Python 3.13

### In Progress
### In Progress
- Web Platform MVP (v0.30.0) development - 84% complete (38/45 tasks)
- Next: Phase 7 - Testing & Quality Assurance

---

## [0.25.1] - 2026-01-17

### Added
- **Documentation Framework**
  - `SDLC.md`: Complete Software Development Life Cycle documentation (7 phases)
  - `DEVELOPMENT_RULES.md`: Coding standards, Git workflow, security guidelines
  - `ROADMAP.md`: Project roadmap from v0.25.0 to v1.0.0
  - `TASK_LIST_MVP.md`: Detailed task list with 45 tasks for MVP v0.30.0
  - `AI_ROLE_FRAMEWORK.md`: Framework for AI agent role-switching in solo development
  - `IMPLEMENTATION_PLAN.md`: Comprehensive architecture and implementation plan for MVP

### Added
- **Feature**: Implementación de fechas límite (Task Deadlines).
  - Nuevo campo `due_date` en modelo `Task`.
  - Cálculo automático de fechas en `seed_data.py`.
  - Indicadores visuales en Dashboard (A tiempo, Atrasado, Completado).

### Fixed
- **UI/UX**: Corregido el diseño del Dashboard (Flexbox) y restaurada la carga de TailwindCSS en `base.html`.
- **Lógica**: Corregida validación de fechas (`isOverdue`) para no marcar fechas futuras como atrasadas.

### In Progress
- **Testing**: Verificación visual por parte del usuario.

### Changed
- **Gestor de Versiones Documentation**
  - Fixed markdown table formatting in `00-ORGANIZACION_EQUIPO.md`
  - Added 75+ clickable markdown links across all documentation files
  - Improved navigation between `00-GUIA_DE_USO.md`, `00-INTEGRACION_TRELLO.md`, and `00-PLAN_DE_TRABAJO.md`
  - Updated username format examples in `10_12-clase_5_practica.md`

- **Project Alignment**
  - Standardized timeline to 4 weeks across all documentation
  - Updated stakeholders to reflect solo developer + AI agent approach
  - Aligned dates: Start 17 Jan 2026, Target 14 Feb 2026

### Technical Details
- Total documentation: 6 major documents (866+ lines in Implementation Plan alone)
- Coverage: Architecture, database schema, API design, folder structure, deployment strategy
- Development approach: Sequential development with AI agent assuming multiple roles

---

## [0.25.0] - 2026-01-17

### Added
- **Sprint 1 Curriculum** (Fundamentos y Seguridad - 25% Course Progress)
  - Semana 1: Clases 1-2 (Teoría y Práctica)
  - Semana 2: Clases 3-6 (Teoría, Práctica, Superbadges)
  - Semana 3: Placeholder structure
  - Semana 4: Placeholder structure
  - Total: 14 clase files in Markdown format

- **Superbadges**
  - Object Relationships for Lightning Experience
  - Formula Fields
  - User Authentication

- **Práctica Financiera** (Case Study: Financiera Horizonte S.A.)
  - Case study document with business context
  - Student guide with Agile methodology
  - 3 requirements with complete solutions:
    - Requerimiento 1: Garantes (Contact Roles)
    - Requerimiento 2: Salario Oculto (Field-Level Security)
    - Requerimiento 3: Múltiples Cuentas (Custom Object)
  - Trello integration guide
  - Visual summary with Mermaid diagrams

- **Gestor de Versiones** (Version Control System)
  - 18 comprehensive documents:
    - Team organization and role distribution
    - Usage guide and Trello integration
    - Work plan and sprint documentation
    - Templates for Sprints 1-3 and final demo
    - Environment setup guides (DEV, QA, PROD)
    - DevOps workflow documentation
  - README with categorized navigation

- **Project Structure**
  - Hierarchical folder structure: `curriculum/sprint_01/semana_XX/`
  - Wiki-style navigation with README files at each level
  - Deep linking between related documents

### Changed
- Migrated from raw PowerPoint text files to structured Markdown
- Removed duplicate content across multiple files
- Optimized for GitHub Pages rendering
- Fixed relative links throughout documentation

### Technical Details
- Total files: 50+ Markdown documents
- Total lines of content: 5000+ lines
- Navigation depth: 4 levels (Project → Sprint → Week → Class)
- Cross-references: 100+ internal links

---

## Project Milestones

### v0.25.x - Static Documentation Phase
- **Focus**: Content creation and organization
- **Platform**: GitHub Pages (static)
- **Status**: ✅ Complete

### v0.30.0 - Web Platform MVP (Target: Feb 14, 2026)
- **Focus**: Dynamic web application with authentication and progress tracking
- **Platform**: Render (FastAPI + PostgreSQL)
- **Status**: 🔄 Planning Complete, Ready for Implementation

### v0.40.0 - Enhanced Features (Target: Feb 25, 2026)
- **Focus**: Notifications, comments, search
- **Status**: 📋 Planned

### v0.50.0 - Sprint 2 Content (Target: Mar 20, 2026)
- **Focus**: Automation processes content
- **Status**: 📋 Planned

### v1.0.0 - Complete Platform (Target: Jun 15, 2026)
- **Focus**: All 4 sprints, certificates, final project
- **Status**: 🎯 Goal

---

## Version History Summary

| Version | Date | Type | Description |
|---------|------|------|-------------|
| 0.25.1 | 2026-01-17 | Documentation | MVP planning and architecture |
| 0.25.0 | 2026-01-17 | Content | Sprint 1 complete documentation |

---

## Contributing

This project follows:
- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **Conventional Commits**: `feat:`, `fix:`, `docs:`, `refactor:`, etc.
- **Keep a Changelog**: Categorized changes (Added, Changed, Deprecated, Removed, Fixed, Security)

---

**Maintained by**: VISIONARY ADMINS Team  
**Last Updated**: 2026-01-17

# CHANGELOG

All notable changes to the Salesforce Admin Learning Platform project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### In Progress
- Web Platform MVP (v0.30.0) development
- Infrastructure setup for FastAPI application
- Database schema design and implementation

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

# 🚀 Salesforce Admin Learning Platform (MVP v0.30.0)

[![Status](https://img.shields.io/badge/Status-Active_Development-success?style=for-the-badge&logo=statuspage)](https://salesforce-admin.onrender.com)
[![Version](https://img.shields.io/badge/MVP-v0.30.0-blue?style=for-the-badge&logo=semver)](docs/NO_VERSION_YET)
[![Tech Stack](https://img.shields.io/badge/Stack-FastAPI%20%7C%20Tailwind%20%7C%20PostgreSQL-005A9C?style=for-the-badge&logo=python)](docs/IMPLEMENTATION_PLAN.md)

> **Plataforma Web Interactiva** para la gestión y aprendizaje del curso Salesforce Administrator.  
> Diseñada para el equipo **VISIONARY ADMINS (Grupo 3)**.

---

## 🏛️ Sobre el Proyecto: "Lumina Tech"

Esta plataforma no es solo un repositorio de documentación. Es el **Centro de Comando** digital donde simulamos la implementación real de Salesforce para nuestro cliente ficticio, la universidad **Lumina Tech**.

Permite a los estudiantes (rol Admin) y profesores (rol Stakeholders) visualizar el avance del Sprint, validar requisitos y acceder a la documentación técnica centralizada.

### 🌟 Características Principales (MVP)

*   **🔐 Autenticación Segura**: Sistema de Login/Registro con JWT.
*   **📊 Centro de Comando (Dashboard)**:
    *   Visualización de avance por Sprints.
    *   Filtrado por Roles (Admin, Consultant, QA).
    *   KPIs de Calidad de Datos.
*   **📄 Documentación Viva**: Motor de renderizado Markdown que convierte apuntes de clase en guías visuales (Soporte Mermaid.js).
*   **📱 Diseño Responsivo**: Interfaz moderna adaptable a cualquier dispositivo (Dark Mode incluido).

---

## 🛠️ Stack Tecnológico

La plataforma ha sido migrada de una web estática a una aplicación Full-Stack robusta:

| Capa | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Backend** | ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | API REST asíncrona de alto rendimiento. |
| **Database** | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white) | Persistencia de usuarios, tareas y progreso. |
| **Frontend** | ![Tailwind](https://img.shields.io/badge/-TailwindCSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white) | Estilos utilitarios y diseño responsivo. |
| **Templating** | ![Jinja2](https://img.shields.io/badge/-Jinja2-B41717?style=flat-square&logo=jinja&logoColor=white) | Renderizado del lado del servidor (SSR). |
| **Interactivity** | ![Alpine.js](https://img.shields.io/badge/-Alpine.js-8BC0D0?style=flat-square&logo=alpine.js&logoColor=white) | Micro-interacciones sin la complejidad de React. |

---

## 📂 Estructura del Proyecto

```bash
salesforce_admin/
├── app/
│   ├── main.py              # 🚀 Punto de entrada FastAPI
│   ├── models/              # 🗄️ Modelos de Base de Datos (User, Progress)
│   ├── routers/             # 🚦 Endpoints de la API (Auth, Docs)
│   ├── services/            # 🧠 Lógica de Negocio (Markdown Parser)
│   └── templates/           # 🎨 Vistas HTML (Jinja2)
│       ├── lumina_dashboard.html  # Centro de Comando
│       └── doc_viewer.html        # Visor de Documentación
├── content/                 # 📚 Documentación del Curso (Markdown)
│   └── Lumina_Tech/         # Proyecto Práctico
├── docs/                    # 📋 Documentación del Sistema (SDLC, Roadmap)
└── scripts/                 # 🛠️ Scripts de utilidad (Seed Data)
```

---

## 🚀 Cómo Iniciar (Local)

Sigue estos pasos para levantar el Centro de Comando en tu máquina:

### 1. Prerrequisitos
*   Python 3.10+
*   PostgreSQL (o Docker)

### 2. Instalación
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/admin_salesforce.git
cd admin_salesforce

# Activar entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
# Instalar dependencias Python
pip install -r requirements.txt

# Instalar dependencias Frontend (Tailwind)
npm install
npm run build:css
```

### 3. Configuración
Crea un archivo `.env` en la raíz (puedes copiar `.env.example`):
```env
DATABASE_URL=postgresql://user:pass@localhost/salesforce_db
SECRET_KEY=tu_secreto_super_seguro
```

### 4. Ejecutar
```bash
# Iniciar servidor de desarrollo
uvicorn app.main:app --reload
```
Visita `http://localhost:8000` para ver el Dashboard.

---

## 🗺️ Roadmap & Progreso

Estamos en la fase de **Mantenimiento y Evolución (v0.32.0)**.

- [x] **Fase 1**: Infraestructura Backend ✅
- [x] **Fase 2**: Autenticación y Usuarios ✅
- [x] **Fase 3**: Motor de Documentación ✅
- [x] **Fase 4**: Dashboard Interactivo "Lumina" ✅
- [x] **Fase 7**: Mantenimiento & DevOps (Backups, Sentry) ✅

---

## 📚 Documentación Técnica y Estratégica

Hemos profesionalizado el proyecto con guías especializadas:

*   📘 **[Manual de Mantenimiento](docs/MAINTENANCE_GUIDE.md)**: Protocolos de actualización, backups y respuesta a incidentes.
*   🏛️ **[Arquitectura & Stack](docs/ARCHITECTURE_STACK.md)**: Análisis del stack tecnológico y estrategia de migración futura.
*   🚀 **[Manual de Mejoras Futuras](docs/FUTURE_IMPROVEMENTS.md)**: Vision del Product Manager para la v1.0 (Admin Panel, Gamification).
*   🛡️ **[SDLC & Roles](docs/SDLC.md)**: Marco de trabajo y ciclo de vida del software.

---

## 👥 Equipo Visionary Admins - Grupo 3

*   **Product Owner**: (Tu Nombre)
*   **Salesforce Admin**: (Tu Nombre)
*   **AI Developer Agent**: Gemini

---
*Hecho con ❤️ y ☕ para dominar Salesforce.*

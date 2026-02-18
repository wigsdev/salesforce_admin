# 📅 Plan de Trabajo y Bitácora - Fase Inicial
**Proyecto**: Lumina Tech

---

## 📅 DIA 0 - Inicio y Definición de Equipo

### Asignación de Roles (Agile Team)
**Fuente**: [Tarea 2 - Definir Roles](../Bitacoras_Sprint_1/dia_0/2_Definir_Roles.md) y `00-MATRIZ_ROLES_EQUIPO.md`.

*   **Product Owner (PO)**: Dra. Vance (Define el "Qué").
*   **Scrum Master**: Facilita el proceso y cuida el tablero.
*   **Business Analyst (BA)**: Releva requerimientos.
*   **Salesforce Consultant**: Diseño Técnico.
*   **Salesforce Admin**: Configuración (Builder).
*   **QA Tester / Release Manager**: Calidad y Despliegues.

### Roles del Sistema (Usuarios)
1.  **Administrativos**: Gestión de inscripciones y cobros.
2.  **Profesores**: Carga de notas (Acceso restringido).
3.  **Directores**: Visión estratégica.
**Sprint**: 01 (Fundamentos)

![Flujo de Trabajo Sprint 1](/uploaded_media_1769735775852.png)
> **Referencia Visual**: Flujo de desarrollo validado (Modelado -> App -> Formularios -> Seguridad).

---

## 📅 DIA 1 - Data Foundation
**Estado**: ✅ COMPLETO
**Entregables**:
1.  **Objetos Custom**: `Carrera`, `Materia`, `Alumno`, `Inscripción`, `Nota`, `Asistencia`.
2.  **ERD Visual**: Diagrama de entidades-relaciones validado.
3.  **Backlog Técnico**: **12 Historias de Usuario** (HU-001 a HU-012) definidas.

---

## 📅 DIA 2 - Branding & App
**Estado**: ✅ COMPLETO
**Entregables**:
1.  **My Domain**: Desplegado (`lumina-tech-university`).
2.  **Theme**: "Lumina Oficial" activo (Azul Lumina `#005A9C`).
3.  **Lightning App**: "Gestión Académica Lumina" configurada y asignada.

---

## 📅 DIA 3 - Automatización y Calidad
**Estado**: ✅ COMPLETO
**Entregables**:
1.  **Formularios Inteligentes**: Reglas de validación activas.
2.  **Calidad**: Regex para Emails y Rango Numérico para Notas.
3.  **Backlog**: HU-007 y HU-008 listas para test.

---

## 📅 DIA 4 - Zero Trust Security
**Estado**: ✅ COMPLETO
**Entregables**:
1.  **Seguridad Base**: OWD Private para `Alumno`.
2.  **Gestión de Accesos**: Perfiles (`Lumina_Professor`, `Lumina_Registrar`, `Lumina_Student`).
3.  **Backlog**: HU-010 a HU-012 (Seguridad y Privacidad) implementadas.

---

## 🚀 Fase 2 - Mejoras Estratégicas (Propuesta)
**Estado**: 🧠 En Análisis
**Detalle**: [Ver Propuesta de Arquitectura](../Archivos_intermedios/08-PROPUESTA_MEJORAS_ARQUITECTURA.md)
*   Automatización (Flows).
*   Analytics (Dashboards).
*   UX/UI Avanzado.

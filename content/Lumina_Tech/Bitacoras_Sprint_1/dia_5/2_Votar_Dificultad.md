# 🃏 Tarea 2: Votar la dificultad (Planning Poker)

**Objetivo**: Asignar un valor de esfuerzo (Story Points) a cada Historia de Usuario consensuado por el equipo.

---

## 📝 Descripción
Utilizar la técnica de Planning Poker para estimar la complejidad.

### Escala de Estimación (Salesforce):
| Story Points (SP) | Nivel | Descripción | Tiempo Aprox. |
| :---: | :---: | :--- | :---: |
| **1 SP** 🟢 | **Baja** | Cambios simples, campos, listas. | 1-3 días |
| **3 SP** 🟡 | **Media** | Flows simples, validaciones, permisos. | 3-6 días |
| **5 SP** 🔴 | **Alta** | Automatización compleja, LWC, Integración. | 6-12 días |

### Pasos:
1.  Seleccionar una HU.
2.  Cada miembro elige una carta (1, 3, o 5) mentalmente.
3.  Revelar votos al mismo tiempo.
4.  Si hay divergencia, debatir y revotar hasta llegar a un consenso.
5.  **Ingresar el puntaje final en el campo "Story Points"** de la tarjeta (Power-Up activado).
    *   *Nota*: Debería visualizarse una etiqueta con el número (ej. ✅ 3) en la portada de la tarjeta.

---

## 📊 Resultados del Planning Poker - Sprint 1 (Refinado Post-Feedback)

Este listado refleja las historias ajustadas tras la sesión de Q&A con la Rectora (Dra. Vance).

### 📅 DIA 1: Data Foundation

**HU-001: Gestión de Inscripciones (Recursantes)**
*   **Estimación**: 🟡 **3 SP**
*   **Justificación**: `Junction Object` complejo (`Enrollment`). Validación de duplicados para permitir historial.

**HU-002: Identidad Única del Alumno**
*   **Estimación**: 🟢 **1 SP**
*   **Justificación**: `National ID` (Unique/External ID) + `Auto-Number` Record Name.

**HU-003: Integridad de Notas y Auditoría**
*   **Estimación**: 🟡 **3 SP**
*   **Justificación**: Precisión decimal (`4,2`) y **Field History Tracking**.

### 📅 DIA 2: Branding & UI

**HU-004: Dominio Seguro**
*   **Estimación**: 🟢 **1 SP**
*   **Justificación**: Configuración de My Domain (`lumina-university`).

**HU-005: Identidad Institucional**
*   **Estimación**: 🟢 **1 SP**
*   **Justificación**: Branding oficial (`#005A9C`) y Themes.

**HU-006: App de Gestión Central**
*   **Estimación**: 🟡 **3 SP**
*   **Justificación**: **Lightning App** optimizada con pestañas limpias (`Students`, `Subjects`, `Enrollments`).

### 📅 DIA 3: Data Quality & Automation

**HU-007: Validación de Contactos (Email)**
*   **Estimación**: 🟡 **3 SP**
*   **Justificación**: Lógica **REGEX** compleja para validar dominios educativos `.edu`.

**HU-008: Integridad Numérica (Hard Validation)**
*   **Estimación**: 🟢 **1 SP**
*   **Justificación**: **Validation Rule** simple para rango 1-10.

**HU-009: Control de Asistencias (Automatización)**
*   **Estimación**: 🔴 **5 SP**
*   **Justificación**: Múltiples campos de fórmula y lógica de negocio para "Academic Condition".

### 📅 DIA 4: Zero Trust Security

**HU-010: Matriz de Visibilidad (Comisiones)**
*   **Estimación**: 🔴 **5 SP**
*   **Justificación**: OWD Private + **Sharing Rules** basadas en criterios para Profesores.

**HU-011: Acceso Seguro (MFA)**
*   **Estimación**: 🟡 **3 SP**
*   **Justificación**: Configuración crítica de seguridad y onboarding de **Salesforce Authenticator**.

**HU-012: Segregación de Funciones (FLS)**
*   **Estimación**: 🟡 **3 SP**
*   **Justificación**: Configuración granular de Perfiles (`Registrar` vs `Professor`) y **Field-Level Security**.

---

### 📉 Resumen del Sprint
*   **Total Story Points**: 32 SP
*   **Velocidad Estimada**: ~8 SP/día (Equipo de 6 personas)


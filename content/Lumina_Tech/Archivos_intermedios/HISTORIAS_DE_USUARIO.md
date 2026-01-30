# 📖 Backlog de Historias de Usuario (Consolidado Sprint 1)
**Proyecto**: Universidad Lumina Tech
**Sprint**: 01 (Fundamentos)
**Alcance**: Días 1 a 4

---

## 📅 DIA 1: Modelado de Datos (Data Foundation)
*Objetivo: Estructurar la base de datos para soportar la operación académica.*

### HU-001: Gestión de Inscripciones (Historial Académico)
*   **Prioridad**: Crack (Core)
*   **Enlace Req**: [REQ-DATA-002]
*   **Descripción**: Como Director, quiero vincular alumnos a materias para tener un historial.
*   **Criterios de Aceptación**:
    - [x] Objeto `Inscripción` creado como Junction Object (M:N).
    - [x] Relación Master-Detail con Alumno y Materia.
    - [x] Tab visible solo para perfiles Directivos.

### HU-002: Unicidad de Alumnos
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-003]
*   **Descripción**: Como Sistema, quiero evitar duplicados por DNI.
*   **Criterios de Aceptación**:
    - [x] Campo `DNI` configurado como Unique.
    - [x] Campo `DNI` configurado como External ID.

### HU-003: Integridad de Notas
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-002]
*   **Descripción**: Como Administrativo, quiero guardar notas numéricas con decimales.
*   **Criterios de Aceptación**:
    - [x] Campo `Nota__c` tipo Number(2,2).
    - [x] Existe Validation Rule para rango 0-10.

---

## 📅 DIA 2: Identidad e Interfaz (Branding)
*Objetivo: Generar pertenencia y confianza en la plataforma.*

### HU-004: Dominio Seguro
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-SEC]
*   **Descripción**: Como Usuario, quiero ver una URL segura institucional.
*   **Criterios de Aceptación**:
    - [x] My Domain desplegado: `lumina-university`.
    - [x] Login page con logo de la universidad.

### HU-005: Identidad Institucional
*   **Prioridad**: Baja (UI)
*   **Enlace Req**: [REQ-BRAND]
*   **Descripción**: Como Rectoría, quiero ver los colores oficiales en la App.
*   **Criterios de Aceptación**:
    - [x] Header Azul (`#005A9C`).
    - [x] Fondo Gris claro para reducir fatiga visual.

### HU-006: App de Gestión Central
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-FUNC]
*   **Descripción**: Como Usuario, quiero tener un lanzador de aplicaciones dedicado.
*   **Criterios de Aceptación**:
    - [x] Lightning App "Gestión Académica" creada.
    - [x] Barra de navegación con: Alumnos, Materias, Inscripciones.

---

## 📅 DIA 3: Calidad y Automatización
*Objetivo: "Data Quality at Source" (Calidad en origen).*

### HU-007: Validación de Contactos (Email)
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-QUAL-001]
*   **Descripción**: Como Marketing, quiero evitar correos con formato erróneo.
*   **Criterios de Aceptación**:
    - [x] Regex activada: Requiere `@` y dominio `.edu`.
    - [x] Rechaza `juan.perez` o `gmail.com`.

### HU-008: Integridad Numérica (Hard Validation)
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-002]
*   **Descripción**: Como Sistema, quiero bloquear notas ilógicas (-1 o 11).
*   **Criterios de Aceptación**:
    - [x] Error bloqueante al ingresar valores fuera de rango.

---

## 📅 DIA 4: Seguridad y Accesos
*Objetivo: Zero Trust (Confianza Cero).*

### HU-009: Matriz de Visibilidad (OWD)
*   **Prioridad**: Crítica
*   **Enlace Req**: [REQ-SEC-002]
*   **Descripción**: Como Profesor, solo quiero ver MIS alumnos.
*   **Criterios de Aceptación**:
    - [x] OWD Alumno = Private.
    - [x] Sharing Rules configuradas para excepciones.

### HU-010: Acceso Seguro (MFA)
*   **Prioridad**: Crítica
*   **Enlace Req**: [REQ-SEC-001]
*   **Descripción**: Como CISO, quiero requerir segundo factor de autenticación.
*   **Criterios de Aceptación**:
    - [x] Permission Set "MFA Authorization" asignado.
    - [x] Login desafía con Authenticator App.

### HU-011: Segregación de Funciones (FLS)
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-SEC-003]
*   **Descripción**: Como Auditoría, quiero que Bedelía no pueda cambiar notas cerradas.
*   **Criterios de Aceptación**:
    - [x] Perfil Administrativo: `Nota__c` es Read-Only.
    - [x] Perfil Profesor: `Nota__c` es Edit.

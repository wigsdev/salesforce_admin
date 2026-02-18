# 🕵️ Business Analyst (BA) - Registro de Requerimientos
**Proyecto**: Lumina Tech
**Sprint**: 01 (Fundamentos)

---

## 📅 DIA 0 - Relevamiento Detallado

### Catálogo de Requerimientos (Backlog)
**Fuente**: [Tarea 1 - Leer juntos y conocer la Empresa](../Bitacoras_Sprint_1/dia_0/1_Leer_juntos_y_conocer_la_Empresa.md)

#### 👮 Seguridad (SEC)
*   **[REQ-SEC-001] Perfiles de Usuario**: Distinción estricta de roles (Lumina_Professor, Lumina_Registrar, Lumina_Student).
*   **[REQ-SEC-002] Privacidad Cruzada**: Visibilidad restringida (un profesor solo ve sus alumnos).
*   **[REQ-SEC-003] Protección de Calificaciones**: Registrar ve contactos pero NO edita notas cerradas.

#### 🏛️ Datos (DATA)
*   **[REQ-DATA-001] Entidades Core**: Gestión de `Carreras` y `Materias`.
*   **[REQ-DATA-002] Historial Académico**: Relación Muchos-a-Muchos (`Inscripción`) con soporte de historial.

#### 💎 Calidad (QUAL)
*   **[REQ-QUAL-001] Validación de Contacto**: Formato de Email Personal estricto.
*   **[REQ-QUAL-002] Consistencia de Notas**: Rango 1.00 - 10.00.
*   **[REQ-QUAL-003] Identidad Obligatoria**: `DNI__c` requerido para crear `Alumno`.

#### ⚙️ Funcionalidad (FUNC)
*   **[REQ-FUNC-001] Ciclo de Evaluaciones**: Registro de Parciales/Finales (`Nota`).
*   **[REQ-FUNC-002] Asistencia**: Registro de `Asistio__c` en el objeto `Asistencia`.

---

## 📅 DIA 1 - Modelo de Datos Detallado
**Fuente**: [Tarea 5 - Crear HU en TRELLO](../Bitacoras_Sprint_1/dia_1/5_Crear_las_HU_en_TRELLO.md)

### Backlog de Historias de Usuario (Sprint 1)
Desglose técnico de los requerimientos anteriores. Total: **12 User Stories**.

| ID | Título | Traza a | Criterios de Aceptación Clave |
| :--- | :--- | :--- | :--- |
| **HU-001** | Gestión de Inscripciones | [REQ-DATA-002] | Objeto `Inscripcion__c` (M:N). Pestaña visible para Registrar y Admin. |
| **HU-002** | Unicidad de Alumnos | [REQ-QUAL-003] | Campo `DNI__c` (Unique, External ID). Estado y Carrera requeridos. |
| **HU-003** | Gestión de Notas | [REQ-QUAL-002, REQ-FUNC-001] | Objeto `Nota__c` (Lookup), `Calificacion__c` y `Nota_Final__c` en Inscripción. |

---

## 📅 DIA 2 - Identidad e Interfaz
**Fuente**: [Tarea 5 - Crear HU en TRELLO (Día 2)](../Bitacoras_Sprint_1/dia_2/5_Crear_las_HU_en_TRELLO.md)

### User Stories (Visual & Branding)

### User Stories (Visual & Branding) - Día 2

#### 🏷️ [HU-004] Dominio Seguro (My Domain)
*   **Enlace Req**: [REQ-SEC]
*   **Criterios de Aceptación**:
    - [x] La URL de la organización contiene `lumina-tech-university`.
    - [x] La pantalla de inicio de sesión muestra el branding correcto de la universidad.

#### 🏷️ [HU-005] Identidad Institucional
*   **Enlace Req**: [REQ-BRAND]
*   **Criterios de Aceptación**:
    - [x] El encabezado global se muestra en color azul corporativo (`#005A9C`).
    - [x] El isologo de Lumina Tech es visible en la barra de navegación.
    - [x] El fondo de las páginas es gris claro (`#F3F3F3`) para descanso visual.

#### 🏷️ [HU-006] App de Gestión Central
*   **Enlace Req**: [REQ-FUNC]
*   **Criterios de Aceptación**:
    - [x] Existe una aplicación Lightning llamada "Gestión Académica Lumina" y es accesible.
    - [x] La barra de navegación incluye: Home, Alumnos, Carreras, Materias, Inscripciones, Asistencias, Notas.

### User Stories (Optimización y Calidad) - Día 3

#### 🏷️ [HU-007] Validación de Contactos (Email)
*   **Enlace Req**: [REQ-QUAL-001]
*   **Criterios de Aceptación**:
    - [x] El campo `Email_Personal__c` usa Regex estricto.
    - [x] Rechaza `juan@gmail,com` (coma en lugar de punto).
    - [x] Acepta `usuario@lumina.edu`.

#### 🏷️ [HU-008] Integridad de Datos (Reglas de Negocio)
*   **Enlace Req**: [REQ-QUAL-002]
*   **Criterios de Aceptación**:
    - [x] **Validación**: Ingresar `1` o `10` en `Calificacion__c` es válido.
    - [x] **Error**: Ingresar `10.5` o `-1` muestra: *"Calificación inválida. Debe ser entre 1 y 10."*.

#### 🏷️ [HU-009] Control de Asistencias
*   **Enlace Req**: [REQ-FUNC-002]
*   **Criterios de Aceptación**:
    - [x] Objeto `Asistencia__c` registra cada clase individualmente.
    - [x] Campos `Clases_Presentes__c` y `Porcentaje_Asistencia__c` calculan regularidad en `Inscripcion__c`.

### User Stories (Seguridad y Accesos) - Día 4

#### 🏷️ [HU-010] Matriz de Visibilidad
*   **Enlace Req**: [REQ-SEC-002]
*   **Criterios de Aceptación**:
    - [x] **OWD**: `Alumno` configurado como `Private`.
    - [x] **Prueba Negativa**: Profesor NO ve alumnos de otras materias.

#### 🏷️ [HU-011] Acceso Seguro (MFA)
*   **Enlace Req**: [REQ-SEC-001]
*   **Criterios de Aceptación**:
    - [x] MFA activado vía Permission Set `Lumina_MFA_Required`.
    - [x] Login requiere Authenticator App.

#### 🏷️ [HU-012] Segregación de Funciones (SoD)
*   **Enlace Req**: [REQ-SEC-003]
*   **Criterios de Aceptación**:
    - [x] **Lumina_Registrar**: FLS Read-Only en objeto `Nota`. No puede editar calificaciones.
    - [x] **Lumina_Professor**: Puede crear y editar `Nota__c`. No puede crear `Inscripciones`.

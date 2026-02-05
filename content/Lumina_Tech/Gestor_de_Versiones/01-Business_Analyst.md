# 🕵️ Business Analyst (BA) - Registro de Requerimientos
**Proyecto**: Lumina Tech
**Sprint**: 01 (Fundamentos)

---

## 📅 DIA 0 - Relevamiento Detallado

### Catálogo de Requerimientos (Backlog)
**Fuente**: [Tarea 1 - Leer juntos y conocer la Empresa](../Bitacoras_Sprint_1/dia_0/1_Leer_juntos_y_conocer_la_Empresa.md)

#### 👮 Seguridad (SEC)
*   **[REQ-SEC-001] Perfiles de Usuario**: Distinción estricta de roles (Admin, Profesor, Director).
*   **[REQ-SEC-002] Privacidad Cruzada**: Visibilidad restringida (un profesor solo ve sus alumnos).
*   **[REQ-SEC-003] Protección de Calificaciones**: Admin ve contactos pero NO edita notas cerradas.

#### 🏛️ Datos (DATA)
*   **[REQ-DATA-001] Entidades Core**: Gestión de `Careers` y `Subjects`.
*   **[REQ-DATA-002] Historial Académico**: Relación Muchos-a-Muchos (`Enrollment`) con soporte de historial.

#### 💎 Calidad (QUAL)
*   **[REQ-QUAL-001] Validación de Contacto**: Formato de Email estricto.
*   **[REQ-QUAL-002] Consistencia de Notas**: Rango 0.00 - 10.00.
*   **[REQ-QUAL-003] Identidad Obligatoria**: `National_ID` requerido para crear `Student`.

#### ⚙️ Funcionalidad (FUNC)
*   **[REQ-FUNC-001] Ciclo de Exámenes**: Registro de Parciales/Finales (`Exams`).
*   **[REQ-FUNC-002] Asistencia**: Registro de `Attended__c` en exámenes.

---

## 📅 DIA 1 - Modelo de Datos Detallado
**Fuente**: [Tarea 5 - Crear HU en TRELLO](../Bitacoras_Sprint_1/dia_1/5_Crear_las_HU_en_TRELLO.md)

### Backlog de Historias de Usuario (Sprint 1)
Desglose técnico de los requerimientos anteriores. Total: **12 User Stories**.

| ID | Título | Traza a | Criterios de Aceptación Clave |
| :--- | :--- | :--- | :--- |
| **HU-001** | Gestión de Inscripciones | [REQ-DATA-002] | Objeto `Enrollment` (M:N). Tab visible solo para Directores. |
| **HU-002** | Unicidad de Alumnos | [REQ-QUAL-003] | Campo `National_ID__c` (Unique, External ID). |
| **HU-003** | Gestión de Exámenes | [REQ-QUAL-002, REQ-FUNC-002] | Objeto `Exam` (M-D), `Score` y `Final_Grade__c` en Enrollment. |

---

## 📅 DIA 2 - Identidad e Interfaz
**Fuente**: [Tarea 5 - Crear HU en TRELLO (Día 2)](../Bitacoras_Sprint_1/dia_2/5_Crear_las_HU_en_TRELLO.md)

### User Stories (Visual & Branding)

### User Stories (Visual & Branding) - Día 2

#### 🏷️ [HU-004] Dominio Seguro (My Domain)
*   **Enlace Req**: [REQ-SEC]
*   **Criterios de Aceptación**:
    - [x] La URL de la organización contiene `lumina-university`.
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
    - [x] Existe una aplicación Lightning llamada "Lumina Academic" y es accesible.
    - [x] La barra de navegación incluye acceso directo a `Students`, `Subjects`, `Enrollments`.

### User Stories (Optimización y Calidad) - Día 3

#### 🏷️ [HU-007] Validación de Contactos (Email)
*   **Enlace Req**: [REQ-QUAL-001]
*   **Criterios de Aceptación**:
    - [x] El campo `Email__c` usa Regex.
    - [x] Rechaza `juan.perez` (sin arroba).
    - [x] Rechaza `juan@gmail.com` (requiere `.edu`).

#### 🏷️ [HU-008] Integridad de Calificaciones
*   **Enlace Req**: [REQ-QUAL-002]
*   **Criterios de Aceptación**:
    - [x] **Validation**: Ingresar `0` o `10` es válido.
    - [x] **Error**: Ingresar `10.5` o `-1` muestra el error: *"Invalid Grade"*.

#### 🏷️ [HU-009] Control de Asistencias
*   **Enlace Req**: [REQ-FUNC-002]
*   **Criterios de Aceptación**:
    - [x] Campos `Classes_Attended__c` calculan porcentaje.

### User Stories (Seguridad y Accesos) - Día 4

#### 🏷️ [HU-010] Matriz de Visibilidad
*   **Enlace Req**: [REQ-SEC-002]
*   **Criterios de Aceptación**:
    - [x] **OWD**: `Student` configurado como `Private`.
    - [x] **Negative Test**: Profesor NO ve alumnos de otras materias.

#### 🏷️ [HU-011] Acceso Seguro (MFA)
*   **Enlace Req**: [REQ-SEC-001]
*   **Criterios de Aceptación**:
    - [x] MFA activado vía Permission Set `Lumina_MFA_Access`.
    - [x] Login requiere Authenticator App.

#### 🏷️ [HU-012] Segregación de Funciones
*   **Enlace Req**: [REQ-SEC-003]
*   **Criterios de Aceptación**:
    - [x] **Bedelía**: FLS Read-Only en `Final_Grade__c`.
    - [x] **Profesor**: Puede editar `Final_Grade__c`.

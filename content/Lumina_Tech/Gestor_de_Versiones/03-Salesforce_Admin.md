# 03-Salesforce_Admin.md - Configuration Workbook (Data Dictionary)

**Proyecto**: Universidad Lumina Tech
**Rol**: Senior Salesforce Administrator
**Sprint**: 1 - Core Académico

---

## 🏗️ 1. Matriz de Objetos (Data Model)

Esta sección funciona como "Receta de Cocina" para la creación de objetos.

### 🟡 Objeto Maestro: Carrera
*Entidad que agrupa las materias. Padre de Materia.*

*   **API Name**: `Carrera__c`
*   **Plural Label**: `Carreras`
*   **Record Name**: `Código` (Auto Number: `CAR-{0000}`)
*   **Features**: Allow Reports, Allow Search.

| Label | API Name | Type | Required | Help Text |
|---|---|---|---|---|
| **Duración (Años)** | `Duracion_Anios__c` | Number(2, 0) | ✅ Yes | Duración oficial del plan de estudios. |

### 🟡 Objeto Maestro: Materia
*La unidad académica basica. Hija de Carrera.*

*   **API Name**: `Materia__c`
*   **Plural Label**: `Materias`
*   **Record Name**: `Nombre Materia` (Text)

| Label | API Name | Type | Required | Relación |
|---|---|---|---|---|
| **Carrera** | `Carrera__c` | Master-Detail | ✅ Yes | Relacionado a `Carrera__c`. |
| **Año Plan** | `Anio_Plan__c` | Number(4, 0) | ❌ No | Año del plan de estudios (ej: 2024). |

---

### 🟢 Objeto Transaccional: Alumno
*El estudiante. Entidad principal del sistema.*

*   **API Name**: `Alumno__c`
*   **Plural Label**: `Alumnos`
*   **Record Name**: `Legajo` (Auto Number: `LEG-{000000}`)

| Label | API Name | Type | Options |
|---|---|---|---|
| **DNI** | `DNI__c` | Text(15) | **Unique**, Case Insensitive. |
| **Email** | `Email__c` | Email | **Required**. |
| **Fecha Nacimiento** | `Fecha_Nacimiento__c` | Date | |

### 🔴 Objeto de Unión: Inscripción (Junction)
*Conecta Alumno con Materia.*

*   **API Name**: `Inscripcion__c`
*   **Plural Label**: `Inscripciones`
*   **Record Name**: `ID Inscripción` (Auto Number: `INS-{000000}`)

| Label | API Name | Type | Detalles |
|---|---|---|---|
| **Alumno** | `Alumno__c` | Master-Detail | Master 1. |
| **Materia** | `Materia__c` | Master-Detail | Master 2. |
| **Estado** | `Estado__c` | Picklist | Cursando, Aprobado, Libre. Default: Cursando. |
| **Nota Final** | `Nota_Final__c` | Number(2,2) | |

---

## 🛡️ 2. Reglas de Validación (Business Logic)

Copiar y pegar estas fórmulas en la sección "Validation Rules" del objeto correspondiente.

### En Objeto: `Inscripcion__c` / `Examen__c`

**VR-001: Rango de Notas**
*   **Error Message**: "La nota debe estar entre 0 y 10."
*   **Formula**:
    ```
    OR(
      Nota__c < 0,
      Nota__c > 10
    )
    ```

### En Objeto: `Alumno__c`

**VR-002: Email Estricto**
*   **Error Message**: "Formato de email inválido. Debe ser @lumina.edu"
*   **Formula**:
    ```
    NOT(REGEX(Email__c, "[a-zA-Z0-9._-]+@lumina\\.edu"))
    ```

---

## 🔐 3. Matriz de Seguridad (Security Model)

### OWD (Sharing Settings)
| Objeto | Default Internal Access | Grant Hierarchy? |
|---|---|---|
| **Alumno** | **Private** | ✅ Yes |
| **Carrera** | Public Read Only | ✅ Yes |
| **Materia** | Public Read Only | ✅ Yes |
| **Inscripción** | Controlled by Parent | N/A |

### Perfiles (Profiles)
*   **Lumina_Profesor**: Clonar de "Standard User".
    *   `Alumno`: Read Only.
    *   `Inscripción`: Read/Create/Edit.
    *   `Examen`: Read/Create/Edit.
    *   **NO DELETE ACCESS** en ningún objeto.

---

## 🚀 4. Guía de Deployment (Pre-Production)

1.  **Tab Visibility**: Asegurar que las Tabs de `Alumnos` e `Inscripciones` sean "Default On" para el perfil Profesor.
2.  **App Menu**: Agregar objetos a la App "Gestión Académica".
3.  **Lightning Pages**: Activar "Alumno Record Page" como Org Default.


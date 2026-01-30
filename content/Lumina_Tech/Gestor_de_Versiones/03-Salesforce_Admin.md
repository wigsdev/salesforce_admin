# ⚙️ Admin - Guía de Implementación
**Proyecto**: Lumina Tech
**Sprint**: 01 (Fundamentos)

---

## 📅 DIA 0 - Configuración Inicial

### Check de Pre-Requisitos
1.  [x] Org de Desarrollo creada.
2.  [x] Mi Dominio configurado (recomendado).
3.  [x] Usuarios de prueba definidos (Profesor, Admin).

---

## 📅 DIA 1 - Creación de Objetos (Schema Builder)

### 📦 Objetos Custom Nuevos
Basado en [REQ-DATA-001] y [REQ-DATA-002].

| Objeto | API Name | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| **Carrera** | `Carrera__c` | Custom | Oferta académica. |
| **Materia** | `Materia__c` | Custom | Unidad curricular. Lookup a Carrera. |
| **Alumno** | `Alumno__c` | Custom | Estudiante. Golden Record. |
| **Inscripción** | `Inscripcion__c` | Custom | **Junction**. Une Alumno y Materia. |
| **Examen** | `Examen__c` | Custom | Detalle de evaluación. |

### 📝 Diccionario de Campos Clave
Basado en [REQ-QUAL] (Calidad de Datos).

#### Objeto: Alumno
*   **Legajo** (`Name`): Auto-Number `{L-0000}`.
*   **DNI** (`DNI__c`): Number(8,0) - **Unique, External ID**. [REQ-QUAL-003]
*   **Email** (`Email__c`): Email Standard. [REQ-QUAL-001]

#### Objeto: Examen
*   **Nota** (`Nota__c`): Number(2,2). **Validación**: `0 <= Nota <= 10`. [REQ-QUAL-002]
*   **Fecha** (`Fecha__c`): Date (Required). [REQ-FUNC-001]
*   **Asistió** (`Asistio__c`): Checkbox (Default: True). [REQ-FUNC-002]

---

## 📅 DIA 2 - Configuración de Branding

### 🌐 My Domain
*   **Nombre**: `lumina-university` (Ejemplo).
*   **Estado**: Deployed to users.
*   **Propósito**: Habilita componentes Lightning custom.

### 🎨 Themes and Branding
*   **Theme Name**: `Lumina Official`.
*   **Brand Color**: `#005A9C`.
*   **Page Background**: `#F4F6F9`.
*   **Active**: ✅ Yes.

### 📱 App Manager
*   **App Name**: `Gestión Académica Lumina` (Lightning App).
*   **Developer Name**: `Gestion_Academica_Lumina`.
*   **Navigation Items**: Home, Alumnos, Inscripciones, Materias, Exámenes, Carreras.
*   **Profiles**: System Admin, Lumina Admin, Lumina Profesor.

---

## 📅 DIA 3 - Automatización y Calidad (Formularios)

### 📦 Nuevos Campos (Schema Update)

#### Objeto: Inscripción (`Inscripcion__c`)
*   **Estado** (`Estado__c`): Picklist (Cursando, Aprobado, Libre). Default: Cursando.
*   **Nota Final** (`Nota_Final__c`): Number(2,2).
*   **Materia Display** (`Materia_Display__c`): Formula (Text). `Materia__r.Name`.

### 🛡️ Reglas de Validación

#### Objeto: Examen
*   **VR-001**: `Nota_0_a_10`.
    *   Formula: `OR(Nota__c < 0, Nota__c > 10)`
    *   Error: "La nota debe estar entre 0 y 10".

#### Objeto: Alumno
*   **VR-002**: `Email_Educativo`.
    *   Formula: `NOT(REGEX(Email__c, "[a-zA-Z0-9._-]+@[a-z]+\\.edu"))`
    *   Error: "Formato inválido. Requiere .edu".

---

## 📅 DIA 4 - Seguridad y Permisos

### 🛡️ Permission Sets (Atomicidad)
1.  **Lumina_MFA_Authorization**: `Multi-Factor Authentication for User Interface Logins`.
2.  **Gestion_Calificaciones_Docente**: Objeto Examen (R/W), Campo Nota (Edit).
3.  **Operador_Bedelia**: Objeto Alumno (R/W), Examen (Read Only).

### 👥 Permission Set Groups (Roles)
1.  **PSG - Profesor Standard**: Incluye MFA + Calificaciones.
2.  **PSG - Administrativo Bedelia**: Incluye MFA + Operador.

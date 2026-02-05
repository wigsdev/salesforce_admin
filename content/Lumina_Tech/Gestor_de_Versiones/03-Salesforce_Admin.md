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
| **Career** | `Career__c` | Custom | Oferta académica. |
| **Subject** | `Subject__c` | Custom | Unidad curricular. Lookup a Career. |
| **Student** | `Student__c` | Custom | Estudiante. Golden Record. |
| **Enrollment** | `Enrollment__c` | Custom | **Junction**. Une Student y Subject. |
| **Exam** | `Exam__c` | Custom | Detalle de evaluación. |

### 📝 Diccionario de Campos Clave
Basado en [REQ-QUAL] (Calidad de Datos).

#### Objeto: Student
*   **Record Name** (`Name`): Auto-Number `A-{YYYY}-{0000}`.
*   **National ID** (`National_ID__c`): Number(8,0) - **Unique, External ID**. [REQ-QUAL-003]
*   **Email** (`Email__c`): Email Standard. [REQ-QUAL-001]

#### Objeto: Exam
*   **Final Grade** (`Final_Grade__c`): Number(4,2). **Validación**: `0 <= Grade <= 10`. [REQ-QUAL-002]
*   **Date** (`Date__c`): Date (Required). [REQ-FUNC-001]
*   **Attended** (`Attended__c`): Checkbox (Default: True). [REQ-FUNC-002]

---

## 📅 DIA 2 - Configuración de Branding

### 🌐 My Domain
*   **Nombre**: `lumina-university` (Ejemplo).
*   **Estado**: Deployed to users.
*   **Propósito**: Habilita componentes Lightning custom.

### 🎨 Themes and Branding
*   **Theme Name**: `Lumina Official`.
*   **Brand Color**: `#005A9C`.
*   **Page Background**: `#F3F3F3`.
*   **Active**: ✅ Yes.

### 📱 App Manager
*   **App Name**: `Lumina Academic` (Lightning App).
*   **Developer Name**: `Lumina_Academic`.
*   **Navigation Items**: Home, Students, Enrollments, Subjects, Exams, Careers.
*   **Profiles**: System Admin, Standard User.

---

## 📅 DIA 3 - Automatización y Calidad (Formularios)

### 📦 Nuevos Campos (Schema Update)

#### Objeto: Enrollment (`Enrollment__c`)
*   **Status** (`Status__c`): Picklist (Enrolled, Passed, Failed). Default: Enrolled.
*   **Final Grade** (`Final_Grade__c`): Number(4,2).
*   **Subject Display** (`Subject_Display__c`): Formula (Text). `Subject__r.Name`.

### 🛡️ Reglas de Validación

#### Objeto: Enrollment
*   **VR-001**: `Grade_Range`.
    *   Formula: `OR(Final_Grade__c < 0, Final_Grade__c > 10)`
    *   Error: "Invalid Grade. Must be 0-10".

#### Objeto: Student
*   **VR-002**: `Email_Format`.
    *   Formula: `NOT(REGEX(Email__c, "[a-zA-Z0-9._-]+@[a-z]+\\.edu"))`
    *   Error: "Invalid Format. Requires .edu".

---

## 📅 DIA 4 - Seguridad y Permisos

### 🛡️ Permission Sets (Atomicidad)
1.  **Lumina_MFA_Access**: `Multi-Factor Authentication for User Interface Logins`.
2.  **Lumina_Professor_Access**: Objeto Exam (R/W), Campo Final Grade (Edit).
3.  **Lumina_Registrar_Access**: Objeto Student (R/W), Exam (Read Only).

### 👥 Permission Set Groups (Roles)
1.  **PSG - Professor Standard**: Incluye MFA + Professor Access.
2.  **PSG - Registrar Staff**: Incluye MFA + Registrar Access.

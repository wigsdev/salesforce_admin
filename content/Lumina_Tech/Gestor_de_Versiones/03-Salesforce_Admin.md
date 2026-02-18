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
| **Materia** | `Materia__c` | Custom | Unidad curricular. Master-Detail a Carrera. |
| **Alumno** | `Alumno__c` | Custom | Estudiante. Golden Record. |
| **Inscripción** | `Inscripcion__c` | Custom | **Junction**. Une Alumno y Materia. |
| **Nota** | `Nota__c` | Custom | Detalle de evaluación. |
| **Asistencia** | `Asistencia__c` | Custom | Registro de asistencia por clase. |

### 📝 Diccionario de Campos Clave
Basado en [REQ-QUAL] (Calidad de Datos).

#### Objeto: Alumno
*   **Record Name** (`Name`): Auto-Number `A-{YYYY}-{0000}`.
*   **DNI** (`DNI__c`): Text(15) - **Unique, External ID**. [REQ-QUAL-003]
*   **Email Personal** (`Email_Personal__c`): Email Standard. [REQ-QUAL-001]

#### Objeto: Nota
*   **Calificación** (`Calificacion__c`): Number(4,2). **Validación**: `1 <= Calificacion <= 10`. [REQ-QUAL-002]
*   **Fecha** (`Fecha__c`): Date (Required). [REQ-FUNC-001]
*   **Asistió** (`Asistio__c`): Checkbox (Default: True). [REQ-FUNC-002]

---

## 📅 DIA 2 - Configuración de Branding

### 🌐 My Domain
*   **Nombre**: `lumina-tech-university`.
*   **Estado**: Deployed to users.
*   **Propósito**: Habilita componentes Lightning custom.

### 🎨 Themes and Branding
*   **Theme Name**: `Lumina Official`.
*   **Brand Color**: `#005A9C`.
*   **Page Background**: `#F3F3F3`.
*   **Active**: ✅ Yes.

### 📱 App Manager
*   **App Name**: `Gestión Académica Lumina` (Lightning App).
*   **Developer Name**: `Gestion_Academica_Lumina`.
*   **Navigation Items**: Home, Alumnos, Carreras, Materias, Inscripciones, Asistencias, Notas.
*   **Profiles**: Lumina_Professor, Lumina_Registrar, Lumina_Student.

---

## 📅 DIA 3 - Automatización y Calidad (Formularios)

### 📦 Nuevos Campos (Schema Update)

#### Objeto: Inscripción (`Inscripcion__c`)
*   **Estado** (`Estado__c`): Picklist (Matriculado, Aprobado, Reprobado). Default: Matriculado.
*   **Nota Final** (`Nota_Final__c`): Number(4,2). Calculado por Flow.
*   **Nombre Materia** (`Nombre_Materia__c`): Formula (Text). `Materia__r.Name`.

### 🛡️ Reglas de Validación

#### Objeto: Inscripción
*   **VR-001**: `Rango_Nota_Valida`.
    *   Formula: `OR(Nota_Final__c < 1, Nota_Final__c > 10)`
    *   Error: "Calificación inválida. Debe ser entre 1 y 10."

#### Objeto: Alumno
*   **VR-002**: `Formato_Email_Valido`.
    *   Formula: `NOT(REGEX(Email_Personal__c, "[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\\.[a-zA-Z]{2,}"))`
    *   Error: "El formato del email no es válido."

---

## 📅 DIA 4 - Seguridad y Permisos

### 🛡️ Permission Sets (Atomicidad)
1.  **Lumina_MFA_Required**: `Multi-Factor Authentication for User Interface Logins`.
2.  **Lumina_Professor**: Objeto Nota (R/W), Objeto Inscripción (Read).
3.  **Lumina_Registrar**: Objeto Alumno (R/W), Objeto Nota (Read Only).

### 👥 Perfiles Personalizados
1.  **Lumina_Professor**: Incluye MFA + acceso a Notas.
2.  **Lumina_Registrar**: Incluye MFA + acceso a Alumnos e Inscripciones.

# 🎓 Guía Técnica: Objeto Alumno (Persona)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-002](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Identidad), [HU-007](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Validación Email)

---

## 🎯 Objetivo
Crear el objeto `Alumno__c` configurando restricciones de unicidad para evitar duplicados en DNI y Email.

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto
1.  Ve a **Setup** > **Object Manager**.
2.  Haz clic en **Create** > **Custom Object**.
3.  Completa los detalles:
    *   **Label**: `Alumno`
    *   **Plural Label**: `Alumnos`
    *   **Object Name**: `Alumno`
    *   **Record Name**: `Legajo`
    *   **Data Type**: **Auto Number**
    *   **Display Format**: `A-{YYYY}-{0000}`
    *   **Starting Number**: `1`
    *   **Allow Search**: ☑️ Marca la casilla.
5.  En "Object Creation Options" (al final), marca: ☑️ **Launch New Custom Tab Wizard after saving custom object**.
6.  Haz clic en **Save**.

### Paso 1.1: Definir Estilo de Pestaña (Tab)
1.  **Tab Style**: Selecciona un ícono (ej: *People*).
2.  Haz clic en **Next**.
3.  **Profiles**: Deja **Default On**. Haz clic en **Next**.
4.  **Apps**: Desmarca "Include Tab" (lo haremos manualmente luego) o déjalo marcado. Haz clic en **Save**.

### Paso 1.2: Crear Vista "Todos los Alumnos" (List View)
*Por defecto Salesforce muestra "Recently Viewed". Crearemos la vista "All".*
1.  Ve a la pestaña **Alumnos**.
2.  Haz clic en el ícono de engranaje (List View Controls) > **New**.
3.  Name: `Todos`. API Name: `Todos`.
4.  Who sees this list view?: **All users can see this list view**.
5.  **Save**.
6.  **Select Fields to Display**: `Nombres`, `Apellidos`, `DNI`, `Carrera`, `Estado`.

### Paso 2: Campos de Identidad y Contacto (Core Fields)

#### 2.1 First Name & Last Name (Nombres)
*Como usamos AutoNumber en el ID, necesitamos campos reales para el nombre.*
1.  **New** > Data Type: **Text**.
2.  **Field Label**: `Nombres`. Length: `80`. **Field Name**: `Nombres`. ☑️ **Required**. **Save & New**.
3.  **New** > Data Type: **Text**.
4.  **Field Label**: `Apellidos`. Length: `80`. **Field Name**: `Apellidos`. ☑️ **Required**. **Save & New**.

#### 2.2 National ID (DNI)
1.  **New** > Data Type: **Text**.
2.  **Field Label**: `DNI`. Length: `15`. **Field Name**: `DNI`.
3.  ☑️ **Required** & ☑️ **Unique** (Case Insensitive) & ☑️ **External ID**.
4.  **Save & New**.

#### 2.3 Date of Birth (Natalicio)
1.  **New** > Data Type: **Date**.
2.  **Field Label**: `Fecha de Nacimiento`. **Field Name**: `Fecha_Nacimiento`. **Save & New**.

#### 2.4 Phone & Email
1.  **New** > Data Type: **Phone**.
2.  **Field Label**: `Teléfono`. **Field Name**: `Telefono` (Sin tilde). **Save & New**.
3.  **New** > Data Type: **Email**.
4.  **Field Label**: `Email Personal`. **Field Name**: `Email_Personal`.
5.  ☑️ **Required** & ☑️ **Unique**.
6.  **Save & New**.

#### 2.5 Admission Date (Ingreso)
1.  **New** > Data Type: **Date**.
2.  **Field Label**: `Fecha de Ingreso`. **Field Name**: `Fecha_Ingreso`.
3.  **Default Value**: `Today()`.
4.  ☑️ **Required** (Important for Cohort calculation).
5.  **Save**.

#### 2.6 Carrera (Matrícula - Lookup) (NUEVO)
*Vincula al alumno con su plan de estudios.*
1.  **New** > Data Type: **Lookup Relationship**. Next.
2.  **Related To**: `Carrera`. Next.
3.  **Field Label**: `Carrera`. **Field Name**: `Carrera`.
4.  ☑️ **Required** (Always require a value...).
5.  **Next** > **Next** > **Next** (Save default Label `Alumnos`). **Save & New**.

#### 2.7 Ciclo de Ingreso (Cohorte) - Fórmula (NUEVO)
*Calculamos automáticamente la cohorte basándonos en la Fecha de Ingreso.*
1.  **New** > Data Type: **Formula**. Next.
2.  **Field Label**: `Ciclo de Ingreso`. **Field Name**: `Ciclo_Ingreso` (Type: Text).
3.  **Formula**:
    ```sql
    TEXT(YEAR(Fecha_Ingreso__c)) & "-" & IF(MONTH(Fecha_Ingreso__c) < 7, "1", "2")
    ```
4.  **Check Syntax**. (Resultado esperado: `2024-1` o `2024-2`).
5.  **Next** > **Next** > **Save & New**.

#### 2.8 Student Status (Estado - Picklist) (NUEVO)
*Para gestionar el ciclo de vida del alumno.*
1.  Data Type: **Picklist**.
2.  **Field Label**: `Estado`. **Field Name**: `Estado`.
3.  **Values** (Enter manually):
    *   `Matriculado` (Activo cursando)
    *   `Inscrito` (Ingresante sin materias)
    *   `Graduado`
    *   `Inactivo` (Temporal)
    *   `Baja` (Definitiva)
4.  **Next** > **Next** > **Save**.

### Paso 3: Mejorar la Búsqueda (Search Layouts)
*CRÍTICO: Para que al inscribir busquemos por "Nombre" y no por "Legajo" (A-2024-001).*
1.  En el Object Manager de **Alumno**, haz clic en **Search Layouts**.
2.  Haz clic en la flecha ▼ al lado de **Search Results** > **Edit**.
3.  En "Available Fields", agrega en este orden:
    *   `Nombres`
    *   `Apellidos`
    *   `DNI`
    *   `Carrera`
    *   `Estado`
4.  Haz clic en **Save**.
5.  Repite el paso para **Lookup Dialogs** (si tu edición lo muestra por separado) para asegurar que en la "Lupita" aparezcan estos datos.

### Paso 4: Validaciones de Negocio (Referencia)

> **Ver Configuración en:** [Guía 09 - Validaciones (Casos 1, 2 y 3)](./09-Tutorial_Validaciones_Es_Es.md#objeto-alumno-ver-guía-03)
> *   Regla `DNI_Numerico_8` (Caso 1).
> *   Regla `Formato_Email_Valido` (Caso 2).
> *   Regla `Fecha_Ingreso_No_Futura` (Caso 3).

### Paso 6: Identidad Digital (Campos Calculados)
*Generamos automáticamente el Usuario y Email Institucional para facilitar el alta del usuario.*

#### 6.1 Usuario de Sistema (Sugerido)
1.  **New** > Data Type: **Formula**.
2.  **Field Label**: `Usuario Sistema`. **Field Name**: `Usuario_Sistema`.
3.  Type: **Text**.
4.  Formula:
    ```sql
    DNI__c & "@lumina.edu.ar"
    ```
5.  **Save & New**.

#### 6.2 Email Institucional (Sugerido)
1.  **New** > Data Type: **Formula**.
2.  **Field Label**: `Email Institucional`. **Field Name**: `Email_Institucional`.
3.  Type: **Text**.
4.  Formula (Copia y Pega Exactamente):
    ```sql
    LOWER(
      SUBSTITUTE(
        SUBSTITUTE(
          SUBSTITUTE(
            SUBSTITUTE(
              SUBSTITUTE(
                SUBSTITUTE(
                  SUBSTITUTE(Nombres__c, " ", ".") & "." & Apellido__c,
                  "á", "a"),
                "é", "e"),
              "í", "i"),
            "ó", "o"),
          "ú", "u"),
        "ñ", "n"),
      "ü", "u")
    ) & "@lumina.edu.ar"
    ```
    *(Nota: Reemplaza tildes y eñes automáticamente para generar un email limpio).*
5.  **Save**.

---

## ✅ Verificación de Éxito
1.  Cree un Alumno "Juan" con DNI `123`.
2.  Intente crear otro Alumno "Pedro" con el mismo DNI `123`.
3.  Salesforce debe arrojar error: *"Duplicate value found"*.
4.  Intente guardar un alumno dejando el Email vacío. Debe dar error de campo requerido.

---

## 📝 Resumen Técnico del Objeto

| Característica | Detalle |
| :--- | :--- |
| **API Name** | `Alumno__c` |
| **Tipo** | Custom Object (Detail of Carrera via Lookup) |
| **Relaciones** | **Lookup** con `Carrera` (Campo Obligatorio). |

### Campos Clave

| Field Label | API Name | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| **Legajo** | `Name` | Auto Number | ID académico (A-{YYYY}-{0000}). |
| **Nombres** | `Nombres__c` | Text (80) | Nombre de pila. |
| **Apellidos** | `Apellidos__c` | Text (80) | Apellido familiar. |
| **DNI** | `DNI__c` | Text (15) | Documento Nacional (Unique, External ID). |
| **Email Personal** | `Email_Personal__c` | Email | Correo de contacto (Unique). |
| **Email Institucional** | `Email_Institucional__c` | Formula | Email oficial Limpio (nombre.apellido@lumina). |
| **Teléfono** | `Telefono__c` | Phone | Número de contacto. |
| **Fecha Nacimiento** | `Fecha_Nacimiento__c` | Date | Fecha de nacimiento. |
| **Fecha Ingreso** | `Fecha_Ingreso__c` | Date | Fecha de matriculación inicial. |
| **Carrera** | `Carrera__c` | Lookup | Plan de estudios del alumno (Required). |
| **Estado** | `Estado__c` | Picklist | Matriculado, Graduado, Baja. |
| **Ciclo de Ingreso** | `Ciclo_Ingreso__c` | Formula | Calcula cohorte (ej: 2024-1). |
| **Usuario Sistema** | `Usuario_Sistema__c` | Formula | Genera `DNI@lumina.edu.ar`. |

### Validaciones
*   `DNI_Numerico_8`: El DNI debe tener 8 dígitos numéricos.
*   `Formato_Email_Valido`: El email personal debe respetar el formato estándar (Regex).
*   `Fecha_Ingreso_No_Futura`: No se pueden registrar ingresos con fecha mayor a HOY.

# 🎓 Guía Técnica: Objeto Materia (Catálogo)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-001](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Catálogo), [HU-010](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Visibilidad)

---

## 🎯 Objetivo
Crear el objeto `Materia__c` y vincularlo fuertemente a una Carrera usando una relación Master-Detail.

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto
1.  Ve a **Setup** > **Object Manager**.
2.  Haz clic en **Create** > **Custom Object**.
3.  Completa los detalles:
    *   **Label**: `Materia`
    *   **Plural Label**: `Materias`
    *   **Object Name**: `Materia`
    *   **Record Name**: `Nombre de Materia`
    *   **Data Type**: Selecciona **Text**.
    *   **Allow Search**: ☑️ Marca la casilla.
5.  En "Object Creation Options" (al final), marca: ☑️ **Launch New Custom Tab Wizard after saving custom object**.
6.  Haz clic en **Save**.

### Paso 1.1: Definir Estilo de Pestaña (Tab)
1.  **Tab Style**: Selecciona un ícono (ej: *Books*).
2.  Haz clic en **Next**.
3.  **Profiles**: Deja **Default On**. Haz clic en **Next**.
4.  **Apps**: Desmarca "Include Tab" (lo haremos manualmente luego) o déjalo marcado. Haz clic en **Save**.

### Paso 2: Crear Relación Master-Detail (Hijo-Padre)
1.  En el menú izquierdo, ve a **Fields & Relationships**.
2.  Haz clic en **New**.
3.  Selecciona Data Type: **Master-Detail Relationship**. Haz clic en **Next**.
4.  En "Related To", selecciona **Carrera**. Haz clic en **Next**.
5.  **Field Label**: `Carrera`.
6.  **Field Name**: `Carrera`.
7.  **Sharing Setting**: Deja la opción por defecto ("Read/Write...").
8.  **Allow Reparenting**: ☑️ **Marca esta casilla** (Es vital para corregir errores).
9.  Haz clic en **Next**.
10. Haz clic en **Next** (Add to layouts).
11. Haz clic en **Save**.

### Paso 3: Crear Campos del Objeto (Business Fields)

#### 3.1 Subject Code (Código - AutoNumber)
*Identificador interno automático (ej: MAT-0001).*
1.  **New** > Data Type: **Auto Number**. Next.
2.  **Field Label**: `Código de Materia`.
3.  **Field Name**: `Codigo_Materia`.
4.  **Display Format**: `MAT-{0000}`.
5.  **Starting Number**: `1`.
6.  **Next** > **Next** > **Save & New**.

#### 3.2 Credits (Créditos - Picklist) (MODIFICADO)
*Peso académico de la materia.*
1.  Data Type: **Picklist**. Next.
2.  **Field Label**: `Créditos`.
3.  **Field Name**: `Creditos`.
4.  **Values** (Enter manually):
    *   1
    *   2
    *   3
    *   4
    *   5
    *   6
    *   7
    *   8
    *   9
    *   10
5.  ☑️ **Required**.
6.  **Next** > **Next** > **Save & New**.

#### 3.3 Subject Type (Tipo)
*Obligatoria u Optativa.*
1.  Data Type: **Picklist**. Next.
2.  **Field Label**: `Tipo de Materia`.
3.  **Field Name**: `Tipo_Materia`.
4.  Values:
    *   `Obligatoria`
    *   `Electiva`
5.  **Next** > **Next** > **Save & New**.

#### 3.4 Plan Year (Año del Plan - Picklist)
*Año sugerido de cursada (1o, 2o, 3o...)*
1.  Data Type: **Picklist**. Next.
2.  **Field Label**: `Año del Plan`.
3.  **Field Name**: `Anio_Plan` (Usando convención 'ni').
4.  Values (Enter manually):
    *   1
    *   2
    *   3
    *   4
    *   5
5.  **Next** > **Next** > **Save & New**.

#### 3.5 Active (Estado)
1.  Data Type: **Checkbox**. Next.
2.  **Field Label**: `Activa`.
3.  **Field Name**: `Activa`.
4.  **Default Value**: `Checked`.
5.  **Next** > **Next** > **Save & New**.

#### 3.6 External Code (Código Externo - Migración)
*Clave única para identificar la materia desde un CSV (ej: INF-001).*
1.  Data Type: **Text**. Next.
2.  **Field Label**: `Código Externo`.
3.  **Field Name**: `Codigo_Externo`.
4.  Length: `20`.
5.  ☑️ **Unique** (Case Sensitive).
6.  ☑️ **External ID** (Set this field as the unique record identifier...).
7.  **Next** > **Next** > **Save**.

#### 3.7 Crear Vista "Todas las Materias" (List View)
1.  Ve a la pestaña **Materias**.
2.  **List View Controls** (Engranaje) > **New**.
3.  Name: `Todas`. API Name: `Todas`.
4.  Visibility: **All users can see this list view**.
5.  **Save**.
6.  **Select Fields to Display**: `Nombre de Materia`, `Carrera`, `Año del Plan`, `Tipo`.

---

#### 3.8 Ciclo (Ciclo Formativo)
*Agrupa materias por etapa (CBC, Troncales, Orientación).*
1.  Data Type: **Picklist**.
2.  **Field Label**: `Ciclo`. **Field Name**: `Ciclo`.
3.  Values:
    *   `CBC`
    *   `Segundo Ciclo` (Grado)
    *   `Electivas`
4.  **Save & New**.

#### 3.9 Cuatrimestre Sugerido
*Orden ideal en el plan (1 al 10).*
1.  Data Type: **Number** (Length 2, decimals 0).
2.  **Field Label**: `Cuatrimestre Sugerido`. **Field Name**: `Cuatrimestre_Sugerido`.
3.  **Save & New**.

#### 3.10 Carga Horaria
*Vital para el cálculo de asistencia y créditos.*
1.  **Horas Semanales**: Number (2,0). Label: `Horas Semanales`. Name: `Horas_Semanales`. **Save & New**.
2.  **Horas Totales**: Number (3,0). Label: `Horas Totales`. Name: `Horas_Totales`. **Save**.

---

## ✅ Verificación de Éxito
1.  Abre el App Launcher y busca "**Materias**".
2.  Haz clic en **New**.
3.  Intente guardar sin elegir Carrera.
    *   **Resultado**: Salesforce debe mostrar un error rojo obligando a usar la lupa para buscar una **Carrera**.
4.  Si borras una Carrera (Prueba destructiva), verifica que sus Materias también desaparezcan.

---

## 📝 Resumen Técnico del Objeto

| Característica | Detalle |
| :--- | :--- |
| **API Name** | `Materia__c` |
| **Tipo** | Custom Object (Detail) |
| **Relaciones** | **Master-Detail** con `Carrera` (Si se borra la Carrera, se borran las Materias). |

### Campos Clave

| Field Label | API Name | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| **Nombre de Materia** | `Name` | Text (80) | Nombre de la asignatura (ej: Análisis Matemático I). |
| **Carrera** | `Carrera__c` | Master-Detail | Carrera a la que pertenece el plan. |
| **Código Materia** | `Codigo_Materia__c` | Auto Number | ID único (MAT-{0000}). |
| **Créditos** | `Creditos__c` | Picklist | Valor académico (1-10). |
| **Tipo de Materia** | `Tipo_Materia__c` | Picklist | Obligatoria, Electiva. |
| **Año del Plan** | `Anio_Plan__c` | Picklist | Año sugerido (1-5). |
| **Código Externo** | `Codigo_Externo__c` | Text (Unique) | ID para integración (External ID). |
| **Ciclo** | `Ciclo__c` | Picklist | CBC, Ciclo Superior, etc. |

### Validaciones
*   La relación Master-Detail obliga a que toda materia tenga una carrera asignada.
*   `Codigo_Externo__c` debe ser único para evitar duplicados en cargas masivas.

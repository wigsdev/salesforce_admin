# 🎓 Guía Técnica: Objeto Alumno (Persona)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-002](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Identidad), [HU-007](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Validación Email)

---

## 🎯 Objetivo
Crear el objeto `Alumno__c` configurando restricciones de unicidad para evitar duplicados en DNI y Email.

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto
1.  Ve a **Setup** > **Object Manager**.
2.  Haz clic en **Create** > **Custom Object**.
3.  Completa los detalles:
    *   **Label**: `Student`
    *   **Plural Label**: `Students`
    *   **Record Name**: `File Number`
    *   **Data Type**: **Auto Number**
    *   **Display Format**: `A-{YYYY}-{0000}`
    *   **Starting Number**: `1`
    *   **Allow Search**: ☑️ Marca la casilla.
4.  Haz clic en **Save**.

### Paso 2: Campos de Identidad y Contacto (Core Fields)

#### 2.1 First Name & Last Name (Nombres)
*Como usamos AutoNumber en el ID, necesitamos campos reales para el nombre.*
1.  **New** > Data Type: **Text**.
2.  **Field Label**: `First Name`. Length: `80`. ☑️ **Required**. **Save & New**.
3.  **New** > Data Type: **Text**.
4.  **Field Label**: `Last Name`. Length: `80`. ☑️ **Required**. **Save & New**.

#### 2.2 National ID (DNI)
1.  **New** > Data Type: **Text**.
2.  **Field Label**: `National ID`. Length: `15`.
3.  ☑️ **Required** & ☑️ **Unique** (Case Insensitive) & ☑️ **External ID**.
4.  **Save & New**.

#### 2.3 Date of Birth (Natalicio)
1.  **New** > Data Type: **Date**.
2.  **Field Label**: `Date of Birth`. **Save & New**.

#### 2.4 Phone & Email
1.  **New** > Data Type: **Phone**.
2.  **Field Label**: `Phone`. **Save & New**.
3.  **New** > Data Type: **Email**.
4.  **Field Label**: `Personal Email`.
5.  ☑️ **Required** & ☑️ **Unique**.
6.  **Save & New**.

#### 2.5 Admission Date (Ingreso)
1.  **New** > Data Type: **Date**.
2.  **Field Label**: `Admission Date`.
3.  **Default Value**: `Today()`.
4.  **Save**.



---

## ✅ Verificación de Éxito
1.  Cree un Alumno "Juan" con DNI `123`.
2.  Intente crear otro Alumno "Pedro" con el mismo DNI `123`.
3.  Salesforce debe arrojar error: *"Duplicate value found"*.
4.  Intente guardar un alumno dejando el Email vacío. Debe dar error de campo requerido.

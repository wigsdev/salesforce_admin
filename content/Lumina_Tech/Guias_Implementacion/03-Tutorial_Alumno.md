# 🎓 Guía Técnica: Objeto Alumno (Persona)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-001 (Privacidad Base), HU-007 (Identidad)

---

## 🎯 Objetivo
Crear el objeto `Alumno__c` configurando restricciones de unicidad para evitar duplicados en DNI y Email.

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto
1.  Ve a **Setup** > **Object Manager**.
2.  Haz clic en **Create** > **Custom Object**.
3.  Completa los detalles:
    *   **Label**: `Alumno`
    *   **Plural Label**: `Alumnos`
    *   **Record Name**: `Legajo`
    *   **Data Type**: **Auto Number**
    *   **Display Format**: `LEG-{000000}`
    *   **Starting Number**: `1`
    *   **Allow Search**: ☑️ Marca la casilla.
4.  Haz clic en **Save**.

### Paso 2: Campos de Identidad (DNI)
1.  Ve a **Fields & Relationships** > **New**.
2.  Selecciona Data Type: **Text**. Haz clic en **Next**.
3.  **Field Label**: `DNI`.
4.  **Length**: `15`.
5.  **Opciones Críticas (General Options)**:
    *   Marca ☑️ **Required**.
    *   Marca ☑️ **Unique**.
    *   Marca ☑️ **External ID** (Esta opción aparece debajo de Unique).
    *   En "Unique Case Sensitivity", selecciona: **"Treat 'ABC' and 'abc' as duplicate values (case insensitive)"**.
6.  Haz clic en **Next**.
7.  Haz clic en **Next**.
8.  Haz clic en **Save & New** (Para crear otro campo inmediatamente).

### Paso 3: Campos de Contacto (Email)
1.  Selecciona Data Type: **Email**. Haz clic en **Next**.
2.  **Field Label**: `Email Personal`.
3.  **Opciones Críticas**:
    *   Marca ☑️ **Required**.
    *   Marca ☑️ **Unique**.
    *   Seleccione "Treat 'ABC' and 'abc' as duplicate values".
4.  Haz clic en **Next**.
5.  Haz clic en **Next**.
6.  Haz clic en **Save**.

---

## ✅ Verificación de Éxito
1.  Cree un Alumno "Juan" con DNI `123`.
2.  Intente crear otro Alumno "Pedro" con el mismo DNI `123`.
3.  Salesforce debe arrojar error: *"Duplicate value found"*.
4.  Intente guardar un alumno dejando el Email vacío. Debe dar error de campo requerido.

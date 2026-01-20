# 🎓 Guía Paso a Paso: Creación de Objeto Alumno
**Nivel**: Intermedio
**Tiempo Estimado**: 15 minutos
**Focus**: Calidad de Datos

---

## 🎯 Objetivo
Crear el objeto `Alumno__c` configurando restricciones de unicidad para evitar duplicados en DNI y Email.

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Alumno`
    *   **Plural Label**: `Alumnos`
    *   **Record Name**: `Legajo`
    *   **Data Type**: **Auto Number**
    *   **Format**: `LEG-{000000}`
3.  **Allow Search**: ☑️ Sí.
4.  **Save**.

### Paso 2: Campos de Identidad (DNI)
1.  **Fields & Relationships** > **New**.
2.  Tipo: **Text**.
3.  Label: `DNI`. Length: `15`.
4.  **Opciones Críticas**:
    *   ☑️ **Required**: Sí.
    *   ☑️ **Unique**: Sí.
    *   Seleccione: **"Treat "ABC" and "abc" as duplicate values (case insensitive)"**.
5.  **Next** > **Save & New**.

### Paso 3: Campos de Contacto (Email)
1.  Tipo: **Email**.
2.  Label: `Email Personal`.
3.  **Opciones Críticas**:
    *   ☑️ **Required**: Sí.
    *   ☑️ **Unique**: Sí.
4.  **Next** > **Save**.

---

## ✅ Verificación de Éxito
1.  Cree un Alumno "Juan" con DNI `123`.
2.  Intente crear otro Alumno "Pedro" con DNI `123`.
3.  Salesforce debe arrojar error: *"Duplicate value found"*.
4.  Intente guardar un alumno sin Email. Debe dar error de campo requerido.

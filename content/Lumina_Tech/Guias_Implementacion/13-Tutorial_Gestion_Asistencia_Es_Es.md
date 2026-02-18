# 🎓 Guía Técnica: Gestión de Asistencia (Modelo Clase)

**Sprint**: 03 (Automatización y UX)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-009] (Asistencia Masiva)

---

## 🎯 Objetivo
Implementar un modelo de "Planilla de Asistencia" donde el profesor crea una **Clase** y el sistema genera automáticamente la lista de alumnos para pasar lista ("Presente/Ausente").

## 🧩 Arquitectura (Header-Detail)
*   **Materia** (Abuelo): La asignatura (ej: Matemática).
*   **Clase** (Padre): La sesión del día (ej: Clase 12/03).
*   **Asistencia** (Hijo): El registro individual del alumno en esa clase.

---

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto "Clase" (Contenedor)
1.  **Object Manager** > **Create** > **Custom Object**.
2.  **Label**: `Clase`. **Plural**: `Clases`.
3.  **Record Name**: `ID Clase` (Auto Number: `CLS-{0000}`).
4.  **Allow Search**: ☑️.
5.  **Launch New Custom Tab Wizard**: ☑️. **Save**.
6.  **Tab Style**: Elige un ícono (ej: *Desk*). **Next** > **Next** > **Save**.

### Paso 2: Relacionar Clase con Materia
1.  **Fields & Relationships** > **New** > **Master-Detail Relationship**.
2.  Related To: **Materia**.
3.  Field Name: `Materia`.
4.  **Next** > **Next** > **Save**.

### Paso 3: Campos de la Clase
1.  **Fecha** (Date): Required. Default `Today`.
2.  **Tema** (Text 255): Opcional, para bitácora.
3.  **Estado** (Picklist): `Planificada`, `Realizada`, `Cancelada`. Default `Realizada`.

### Paso 4: Conectar Asistencia a Clase
*Ahora `Asistencia` será hija de `Clase`, no directa de Materia.*
1.  Ve al objeto **Asistencia**.
2.  **Fields & Relationships** > **New** > **Master-Detail Relationship**.
3.  Related To: **Clase**.
4.  Field Name: `Clase`.
5.  **Next** > **Next** > **Save**.

### Paso 5: Automatización "Generar Planilla" (Flow)
*Cuando se crea una Clase, generamos las asistencias.*

1.  **Flows** > **New Flow** > **Record-Triggered Flow**.
2.  **Object**: `Clase`. **Trigger**: A record is created.
3.  **Optimization**: Actions and Related Records (After Save).
4.  **Get Records**: `Obtener_Inscripciones`.
    *   Object: `Inscripción`.
    *   Condition: `Materia__c` Equals `{!$Record.Materia__c}` AND `Estado__c` Equals `Cursando`.
    *   Store All Records.
5.  **Loop**: `Iterar_Alumnos`.
6.  **Assignment**: `Preparar_Asistencia`.
    *   Var `single_Asistencia` (Asistencia).
    *   `Clase__c` = `{!$Record.Id}`.
    *   `Inscripcion__c` = `{!Loop.Id}`.
    *   `Estado__c` = "Presente" (Default).
    *   Add to `coll_Asistencias`.
7.  **Create Records**: `Insertar_Planilla`.
8.  **Save**. Label: `Clase: Generar Asistencias`. **Activate**.

### Paso 6: La Interfaz del Profesor (Related List)
1.  Ve a un registro de **Materia**.
2.  **Edit Page** (Lightning App Builder).
3.  Agrega la **Related List Single**: "Clases".
4.  Entra a una **Clase**.
5.  Asegúrate de que la Related List "Asistencias" muestre los campos:
    *   `Inscripción` (Alumno).
    *   `Estado` (Editable).
6.  **Tip**: Habilita "Inline Editing" en la Related List desde las propiedades del componente ("Enable Inline Editing" en Dynamic Related List si usas esa, o List View).

---

## 🚀 Resultado
1.  Profesor entra a "Matética".
2.  Crea nueva **Clase** (Fecha Hoy).
3.  Al guardar, aparece la lista de 30 alumnos en "Asistencias".
4.  Marca los ausentes. ¡Listo! ✅

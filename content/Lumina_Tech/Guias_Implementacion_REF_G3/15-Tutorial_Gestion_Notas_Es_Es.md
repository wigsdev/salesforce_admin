# 🎓 Guía Técnica: Gestión de Notas (Modelo Evaluación)

**Sprint**: 03 (Automatización y UX)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-003] (Planilla de Notas)

---

## 🎯 Objetivo
Implementar un modelo de "Planilla de Calificaciones" donde el profesor crea una **Evaluación** (acta) y el sistema genera los casilleros vacíos para cargar las notas masivamente.

## 🧩 Arquitectura (Header-Detail)
*   **Materia** (Abuelo): La asignatura (ej: Matemática).
*   **Evaluación** (Padre): La instancia de examen (ej: Parcial 1, TP Final).
*   **Nota** (Hijo): La calificación individual del alumno.

---

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto "Evaluación" (Contenedor)
1.  **Object Manager** > **Create** > **Custom Object**.
2.  **Label**: `Evaluación`. **Plural**: `Evaluaciones`.
3.  **Record Name**: `Nombre Evaluación` (Text, ej: "Parcial 1").
4.  **Allow Search**: ☑️.
5.  **Launch New Custom Tab Wizard**: ☑️. **Save**.
6.  **Tab Style**: Elige un ícono (ej: *Clipboard*). **Next** > **Next** > **Save**.

### Paso 2: Relacionar Evaluación con Materia
1.  **Fields & Relationships** > **New** > **Master-Detail Relationship**.
2.  Related To: **Materia**.
3.  Field Name: `Materia`.
4.  **Next** > **Next** > **Save**.

### Paso 3: Campos de la Evaluación
1.  **Fecha** (Date): Required.
2.  **Tipo** (Picklist): `Parcial 1`, `Práctica 1`, `Medio Curso`, `Parcial 2`, `Práctica 2`, `Final`.
3.  **Ponderación** (Percent): **Field Name**: `Ponderacion`.
    *   *Nota*: Aquí definís cuánto vale esta nota (ej: 0.10, 0.30).
    *   Decimals: `0` (Opcional: 2).
4.  **Estado** (Picklist): `Abierta`, `Cerrada`. Default `Abierta`.

### Paso 4: Conectar Nota a Evaluación
*Reemplazamos la conexión directa a Inscripción por esto (o la complementamos).*
*NOTA: Nota debe seguir conectada a Inscripción para saber de quién es. Pero también conectada a Evaluación.*

1.  Ve al objeto **Nota**.
2.  **Fields & Relationships** > **New** > **Master-Detail Relationship**.
3.  Related To: **Evaluación**.
4.  Field Name: `Evaluacion`.
5.  **Next** > **Next** > **Save**.

### Paso 5: Automatización "Generar Acta" (Flow)
*Al crear la Evaluación, generamos las notas vacías.*

1.  **Flows** > **New Flow** > **Record-Triggered Flow**.
2.  **Object**: `Evaluación`. **Trigger**: A record is created.
3.  **Actions and Related Records**.
4.  **Get Records**: `Obtener_Inscripciones`.
    *   Object: `Inscripción`.
    *   Condition: `Materia__c` Equals `{!$Record.Materia__c}` AND `Estado__c` Equals `Cursando`.
    *   Store All Records.
5.  **Loop**: `Iterar`.
6.  **Assignment**: `Preparar_Nota`.
    *   Var `single_Nota`.
    *   `Evaluacion__c` = `{!$Record.Id}`.
    *   `Inscripcion__c` = `{!Loop.Id}`.
    *   `Fecha__c` = `{!$Record.Fecha__c}`.
    *   `Tipo__c` = `{!$Record.Tipo__c}`.
    *   Add to `coll_Notas`.
7.  **Create Records**: `Insertar_Acta`.
8.  **Save**. Label: `Evaluación: Generar Acta`. **Activate**.

### Paso 6: La Interfaz (Planilla Editable)
1.  Ve a un registro de **Materia**.
2.  Agrega la Related List "Evaluaciones".
3.  Entra a una **Evaluación** (ej: "Parcial 1").
4.  En la Related List **Notas**, asegúrate de exponer:
    *   `Inscripción` (Alumno).
    *   `Calificación` (Editable).
    *   `Escala` (Formula).
5.  Al hacer clic en "View All" sobre la lista de notas, tendrás la **Planilla Completa**.

---

## 🚀 Resultado
1.  Profesor entra a "Matemática".
2.  Crea Evaluación: "Primer Parcial" (Fecha Hoy).
3.  Automáticamente aparecen 30 filas vacías en "Notas".
4.  Entra a la lista, clic en el lápiz, carga: `7`, `8`, `9`...
5.  **Save**. 💾

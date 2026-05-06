# 🎓 Guía Técnica: Gestión Masiva de Evaluaciones (Actas de Examen) [MODIFICADO SPRINT 2/3]

**Sprint**: 03 (Automatización y UX)
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Developer**
**HUs Relacionadas**: Planilla de Calificaciones Masiva (UX).

---

## 🔍 Parte 1: Implementación Original (As-Is / Sprint 1)

*En la concepción original (Sprint 1), el profesor debía ir alumno por alumno creando el registro de la nota. Luego se propuso crear un objeto contenedor ("Evaluación") que genere los registros hijos ("Notas"). Sin embargo, la nomenclatura chocaba con la refactorización del Sprint 2, donde consolidamos que el registro de la nota individual se llama estrictamente `Evaluacion__c`.*

### 🎯 Objetivo de la Mejora
Crear un objeto "Header" llamado **Instancia de Evaluación** (el Acta). Cuando el docente crea esta Acta (ej: "Parcial 1 de Matemática"), el sistema genera automáticamente la planilla con todos los inscriptos para que el profesor solo tenga que tipear los números de forma rápida (Inline Editing).

---

## 🛠️ Parte 2: Refactorización a Modelo "Acta de Examen" (To-Be / Sprint 3)

### 🧩 Arquitectura Requerida
*   **Materia** (Abuelo): La asignatura.
*   **Instancia de Evaluación** (Padre Header - *NUEVO OBJETO*): El acta del examen.
*   **Evaluación** (Hijo Detail): El registro individual que almacena la nota del alumno (Refactorizado en Guía 06). Mantiene su Lookup hacia la Inscripción.

### Paso 1: Crear el Objeto "Instancia de Evaluación" (El Acta)
1.  Ve a **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  **Label**: `Instancia de Evaluación`. **Plural**: `Instancias de Evaluación`. **API Name**: `Instancia_Evaluacion__c`.
3.  **Record Name**: `Nombre del Acta` (Text, ej: "Acta Parcial 1").
4.  Marca **Allow Reports** y **Launch New Custom Tab Wizard**. **Save**.
5.  Elige un ícono (ej: *Clipboard* o *Form*).

### Paso 2: Relacionar Instancia con Materia
1.  En `Instancia_Evaluacion__c` > **Fields & Relationships** > **New** > **Master-Detail Relationship**.
2.  Related To: **Materia**.
3.  Field Name: `Materia__c`.

### Paso 3: Definir Propiedades del Acta
*Estos valores se heredarán a cada alumno automáticamente.*
1.  **Fecha del Examen** (Date): Required. API: `Fecha__c`.
2.  **Tipo de Examen** (Picklist): `Parcial 1`, `Parcial 2`, `Trabajo Práctico`, `Final`. API: `Tipo_Examen__c`.
3.  **Peso Porcentual** (Percent): Required. Define cuánto vale el examen. API: `Peso__c`.
4.  **Estado del Acta** (Picklist): `Abierta`, `Cerrada`. Default = `Abierta`.

### Paso 4: Ajustar el Objeto Evaluación (El registro individual)
*Conectaremos la nota individual al Acta.*
1.  Ve al objeto **Evaluación** (`Evaluacion__c`).
2.  **Fields & Relationships** > **New** > **Master-Detail Relationship**.
    *   *Nota Arquitectónica:* Como Evaluación solo tiene un Lookup a Inscripción (por el límite de Junction), **SÍ** podemos crearle un Master-Detail hacia Instancia de Evaluación.
3.  Related To: **Instancia de Evaluación**.
4.  Field Name: `Instancia_Evaluacion__c`.

### Paso 5: Automatización "Generar Acta" (Record-Triggered Flow)
*Al guardar el Acta, el sistema busca a los inscriptos y les crea su renglón vacío.*

1.  Ve a **Setup** > **Flows** > **New Flow** > **Record-Triggered Flow**.
2.  **Object**: `Instancia_Evaluacion__c`. **Trigger**: *A record is created*.
3.  **Optimization**: *Actions and Related Records* (After Save).
4.  **Elemento Get Records**: `Obtener_Inscriptos_Activos`.
    *   Object: `Inscripcion__c`.
    *   Condition: `Materia__c` Equals `{!$Record.Materia__c}` AND `Estado__c` Equals `Activo`.
    *   Store All Records.
5.  **Elemento Loop**: `Iterar_Alumnos`.
6.  **Elemento Assignment 1**: `Mapear_Nota_Individual`.
    *   Crea una variable `var_Evaluacion` (Record Type: Evaluacion).
    *   Asigna: `Instancia_Evaluacion__c` = `{!$Record.Id}`.
    *   Asigna: `Inscripcion__c` = `{!Iterar_Alumnos.Id}`.
    *   Asigna: `Tipo_Examen__c` = `{!$Record.Tipo_Examen__c}`.
    *   Asigna: `Peso__c` = `{!$Record.Peso__c}`.
    *   *(El campo Nota__c queda vacío para que el profesor lo llene).*
7.  **Elemento Assignment 2**: `Agregar_a_Lista`.
    *   Añade `var_Evaluacion` a una colección `coll_Evaluaciones_Nuevas`.
8.  **Elemento Create Records**: `Insertar_Renglones_Acta`.
    *   Crea los registros usando la colección.
9.  **Save** y **Activate**.

### Paso 6: La Interfaz del Docente (Planilla Editable)
1.  Ve a un registro de **Materia** y edita el *Page Layout*. Agrega la Related List de "Instancias de Evaluación".
2.  Entra a una **Instancia de Evaluación** y edita su *Page Layout*. En su lista relacionada de "Evaluaciones" asegúrate de mostrar:
    *   `Alumno` (Fórmula cruzada desde Inscripción).
    *   `Nota` (¡Este es el campo que se editará masivamente!).
    *   `Nota Ponderada`.
3.  *Tip para UX:* Habilita el *Inline Editing* (Edición en línea) en las vistas de lista de Evaluaciones para que el docente pueda tipear todas las notas como si fuera Excel y hacer un solo click en Guardar.

---

## 🚀 Verificación de Éxito
1.  Entra a la Materia "Matemática".
2.  Crea una nueva **Instancia de Evaluación**: Acta "Primer Parcial", Tipo = Parcial 1, Peso = 30%.
3.  Al darle a Guardar, la pantalla te mostrará el Acta.
4.  En la lista inferior, aparecerán las 30 filas vacías (una por alumno).
5.  El profesor entra a la lista, hace doble clic en el primer casillero de "Nota", carga un `7`, baja a la siguiente fila, carga un `8`, etc.
6.  Presiona "Save" y todas las notas quedan registradas y sus promedios en la Inscripción actualizados. ¡Magia pura! 🪄

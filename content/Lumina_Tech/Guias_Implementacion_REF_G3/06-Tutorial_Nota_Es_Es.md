# 🎓 Guía Técnica: Objeto Nota (Evaluación Académica)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos - Extensión)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-003](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Gestión de Notas)

---

## 🎯 Objetivo
Permitir la carga granular de calificaciones (Parciales, TPs, Orales, Concepto) relacionándolas a la Inscripción del alumno.

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto Custom
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Nota`
    *   **Plural Label**: `Notas`
    *   **Object Name**: `Nota` (API: `Nota__c`).
    *   **Record Name**: `ID Nota` (Data Type: **Auto Number**).
    *   **Display Format**: `NT-{000000}`.
    *   **Starting Number**: `1`.
    *   En "Optional Features", marca: ☑️ **Track Field History**.
3.  En "Object Creation Options" (al final), marca: ☑️ **Launch New Custom Tab Wizard after saving custom object**.
4.  Haz clic en **Save**.

### Paso 1.1: Definir Estilo de Pestaña (Tab)
1.  **Tab Style**: Selecciona un ícono (ej: *Scorecard* o *Form*).
2.  Haz clic en **Next**.
3.  **Profiles**: Deja **Default On**. Haz clic en **Next**.
4.  **Apps**: Desmarca "Include Tab" (lo haremos manualmente luego) o déjalo marcado. Haz clic en **Save**.

### Paso 1.2: Crear Vista "Todas las Notas" (List View)
1.  Ve a la pestaña **Notas**.
2.  **New**. Name: `Todas`. Visibility: **All users**.
3.  **Fields**: `Inscripción`, `Tipo`, `Calificación`, `Fecha`.
4.  **Save**.

### Paso 2: Crear el Vínculo Padre (Hacia Inscripción)
*La nota pertenece a una cursada concreta.*

> **⚠️ Nota de Arquitectura (Junction Object limitation)**
> Como `Inscripción` ya es un objeto conector (Hijo de Alumno y Materia) mediante Master-Detail, Salesforce **no permite** que sea "Master" de otro objeto.
> Por eso, usaremos una **Lookup Relationship** (Búsqueda) obligatoria en lugar de Master-Detail.

1.  **Fields & Relationships** > **New**.
2.  Tipo: **Lookup Relationship** (Búsqueda).
3.  Related To: **Inscripción** (`Inscripcion`).
4.  **Field Label**: `Inscripción`.
5.  **Field Name**: `Inscripcion` (Sin tilde).
6.  **Next**.
7.  **Importante**: Marca ☑️ **Always require an value in this field in order to save a record**.
8.  **Next** > **Next** > **Save & New**.

### Paso 3: Crear Campos de Datos

#### 3.1 Date (Fecha de Evaluación)
1.  Data Type: **Date**.
2.  **Field Label**: `Fecha`.
3.  **Field Name**: `Fecha`.
4.  **Required**: ☑️ (Always require a value).
5.  **Save & New**.

#### 3.2 Score (Calificación)
1.  Data Type: **Number**.
2.  **Field Label**: `Calificación`.
3.  **Field Name**: `Calificacion`.
4.  **Length**: `4`, **Decimal Places**: `2` (ej: 10.00).
5.  **Save & New**.

#### 3.3 Attended (Asistió)
1.  Data Type: **Checkbox**.
2.  **Field Label**: `Asistió`.
3.  **Field Name**: `Asistio`.
4.  **Default Value**: `Checked` (True).
5.  **Save & New**.

#### 3.4 Type (Tipo de Evaluación)
1.  Data Type: **Picklist**.
2.  **Field Label**: `Tipo`.
3.  **Field Name**: `Tipo`.
4.  Values:
    *   `Parcial 1`
    *   `Práctica 1`
    *   `Medio Curso`
    *   `Parcial 2`
    *   `Práctica 2`
    *   `Final`
5.  **Save**.

#### 3.5 Ponderación (Peso)
*Porcentaje de incidencia en la nota final (Ej: 0.10 = 10%).*
1.  Data Type: **Percent**.
2.  **Field Label**: `Ponderación`. **Field Name**: `Ponderacion`.
3.  Length: `3`, Decimals: `0`.
4.  **Required**: ☑️.
5.  **Save & New**.

#### 3.6 Rating Scale (Escala de Calificación)
*Traducción automática de nota numérica a concepto cualitativo.*
1.  Data Type: **Formula**.
2.  **Field Label**: `Escala de Calificación`. **Field Name**: `Escala_Calificacion`.
3.  Type: **Text**.
4.  Formula:
    ```sql
    IF( Calificacion__c < 6, "Reprobado",          /* 1-5 */
      IF( Calificacion__c < 8, "Aprobado",         /* 6-7 */
        IF( Calificacion__c < 9, "Distinguido",    /* 8 */
          "Sobresaliente"                          /* 9-10 */
        )
      )
    )
    ```
5.  **Save**.

#### 3.7 Weighted Grade (Nota Ponderada) (NUEVO)
*Calcula el aporte real de esta nota al promedio final.*
1.  **New** > Data Type: **Formula**.
2.  **Field Label**: `Nota Ponderada`. **Field Name**: `Nota_Ponderada`.
3.  Type: **Number** (2 decimals).
4.  Formula:
    ```sql
    Calificacion__c * Ponderacion__c
    ```
5.  **Save**.

#### 3.8 Observaciones (Feedback) (NUEVO)
*Espacio para que el docente deje comentarios cualitativos sobre el desempeño.*
1.  **New** > Data Type: **Text Area** (Long preferiblemente, o Text Area simple).
2.  **Field Label**: `Observaciones`. **Field Name**: `Observaciones`.
3.  **Save**.

### Paso 3.9: Configurar Historial de Campo (Auditoría)
*Requerimiento crítico de seguridad: Trazabilidad de cambios en notas.*
1.  En **Object Manager** > **Nota**, haz clic en **Fields & Relationships**.
2.  Haz clic en el botón superior derecho **Set History Tracking**.
3.  Marca las casillas:
    *   `Calificación`
    *   `Ponderación`
    *   `Fecha`
    *   `Asistió`
4.  **Save**.

4.  **Save**.

### Paso 4: Automatización (Flows de Cálculo)
*Como usamos Lookup y no Master-Detail, la Nota Final no se calcula sola. Necesitamos 2 Flows.*

#### 4.1 Crear Flow "Calcular Nota Inscripción" (Create/Update)
*Se dispara cuando creas o modificas una nota.*

1.  **Setup** > **Flows** > **New Flow** > **Record-Triggered Flow**.
2.  **Configurar Start (Inicio)**:
    *   **Object**: `Nota`.
    *   **Trigger**: A record is created or updated.
    *   **Condition Requirements**: `None`.
    *   **Authorize**: Haz clic en la **(X)** para cerrar el cuadro de Start.
3.  **Agregar Elemento 1 (Get Records)**:
    *   Haz clic en el círculo **(+)** debajo del Start. Selecciona **Get Records**.
    *   **Label**: `Obtener Notas Hermanas`.
    *   **Object**: `Nota`.
    *   **Filter Note Records**: `Inscripcion__c` **Equals** `{!$Record.Inscripcion__c}`.
    *   **How Many Records to Store**: **All records**.
4.  **Agregar Elemento 2 (Loop)**:
    *   Haz clic en el **(+)** debajo de Get Records. Selecciona **Loop**.
    *   **Label**: `Iterar Notas`.
    *   **Collection Variable**: `{!Obtener_Notas_Hermanas}`.
5.  **Agregar Elemento 3 (Assignment)**:
    *   Haz clic en el **(+)** dentro del camino "For Each". Selecciona **Assignment**.
    *   **Label**: `Sumar`.
    *   **Variable**: Aquí crearemos una nueva cajita para sumar:
        *   Haz clic en el cuadro de búsqueda y selecciona **New Resource** (al principio de la lista).
        *   **Resource Type**: `Variable`.
        *   **API Name**: `var_SumaNotas`.
        *   **Data Type**: `Number`.
        *   **Decimal Places**: `2`.
        *   **Default Value**: `0` (¡Importante para que empiece de cero!).
        *   Haz clic en **Done**.
    *   **Operator**: **Add** (Sumar).
    *   **Value**: Ahora buscaremos el valor de la nota actual:
        *   Haz clic en el cuadro de búsqueda y baja hasta **Loop Variables**.
        *   Selecciona `Current Item from Loop Iterar_Notas` (o similar).
        *   Luego busca y selecciona el campo **Nota Ponderada** (`Nota_Ponderada__c`).
        *   Quedará así: `{!Iterar_Notas.Nota_Ponderada__c}`.
6.  **Agregar Elemento 4 (Update Records)**:
    *   Haz clic en el **(+)** en el camino "After Last Item". Selecciona **Update Records**.
    *   **Label**: `Actualizar Inscripcio`.
    *   **Find Records**: Specify conditions.
    *   **Object**: `Inscripción`.
    *   **Filter**: `Id` **Equals** `{!$Record.Inscripcion__c}`.
    *   **Set Field**: `Nota_Final__c` <- `{!var_SumaNotas}`.
7.  **Activate**. Label: `Nota: Calcular Nota Final (Create/Update)`.

#### 4.2 Crear Flow "Recalcular al Borrar" (Delete)
*Se dispara cuando eliminas una nota por error. Resta el valor.*

1.  **New Flow** > **Record-Triggered Flow**.
2.  **Configurar Start (Inicio)**:
    *   **Object**: `Nota`.
    *   **Trigger**: A record is **Deleted**.
    *   **Condition Requirements**: `None` (¡Importante! No pongas nada aquí).
    *   Cierra el cuadro con la **(X)**.
3.  **Agregar Elemento 1 (Get Records)**:
    *   Haz clic en el círculo **(+)** debajo del Start. Selecciona **Get Records**.
    *   **Label**: `Obtener Notas Restantes`.
    *   **Object**: `Nota`.
    *   **Filter Note Records**:
        *   `Inscripcion__c` **Equals** `{!$Record.Inscripcion__c}`.
        *   **AND**: `Id` **Does Not Equal** `{!$Record.Id}`.
    *   **How Many Records to Store**: **All records**.
4.  **Loop & Sum**: Repite los pasos 4 y 5 del flow anterior (Iterar y Sumar a variable).
5.  **Update Records**: Repite el paso 6 (Actualizar Inscripción padre con la variable).
6.  **Activate**. Label: `Nota: Recalcular al Borrar (Delete)`.

### Paso 5: Validaciones de Calidad (Referencia)

> **Ver Configuración en:** [Guía 09 - Validaciones (Caso H)](./09-Tutorial_Validaciones_Es_Es.md#caso-h-rango-de-calificación-parcial-nota) (Regla `Rango_Nota_Valida`).

---

## 🚀 Resultado Final
1.  Ve a la App "Gestión Académica Lumina".
2.  Entra a una **Inscripción** activa.
3.  En la pestaña **Related** (Relacionado), verás la lista "Notas".
4.  Desde ahí podrás cargar:
    *   "TP 1" - 05/03/2026 - Calificación: 8.50
    *   "Oral" - 20/04/2026 - Calificación: 9.00

¡Ahora tienes trazabilidad completa del rendimiento académico! 📈

---

## 📝 Resumen Técnico del Objeto

| Característica | Detalle |
| :--- | :--- |
| **API Name** | `Nota__c` |
| **Tipo** | Custom Object (Detail) |
| **Relaciones** | **Lookup (Required)** con `Inscripción`. |

### Campos Clave

| Field Label | API Name | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| **Código** | `Name` | Auto Number | ID único (NT-{0000}). |
| **Inscripción** | `Inscripcion__c` | Lookup | Vínculo con el alumno/materia. |
| **Fecha** | `Fecha__c` | Date | Cuándo se rindió. |
| **Tipo** | `Tipo__c` | Picklist | Parcial, Final, TP. |
| **Calificación** | `Calificacion__c` | Number (4,2) | Nota numérica (ej: 8.50). |
| **Ponderación** | `Ponderacion__c` | Percent | Peso en la nota final (ej: 30%). |
| **Nota Ponderada** | `Nota_Ponderada__c` | Formula | Calcula puntos reales para el promedio. |
| **Escala** | `Escala_Calificacion__c` | Formula | Traduce nota a texto (Aprobado/Reprobado). |

### Validaciones y Automatización
*   **Flows de Cálculo**: Existen 2 Flows ("Calcular Nota" y "Recalcular al Borrar") que suman las `Nota_Ponderada__c` y actualizan el campo `Nota_Final__c` en la Inscripción.
*   **Rango de Nota**: Regla `Rango_Nota_Valida` impide cargar notas menores a 0 o mayores a 10.

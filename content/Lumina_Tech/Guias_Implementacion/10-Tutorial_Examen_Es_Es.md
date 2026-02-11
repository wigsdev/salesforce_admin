# 🎓 Guía Técnica: Objeto Examen (Exam)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos - Extensión)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-003](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Gestión de Exámenes y Notas)

---

## 🎯 Objetivo
Permitir la carga granular de evaluaciones (Parciales, Trabajos Prácticos, Finales) relacionándolas a la Inscripción del alumno.

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto Custom
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Examen`
    *   **Plural Label**: `Exámenes`
    *   **Object Name**: `Examen` (API: `Examen__c`).
    *   **Record Name**: `Nombre del Examen` (Data Type: Text).
    *   En "Optional Features", marca: ☑️ **Track Field History**.
3.  **Save**.

### Paso 2: Crear el Vínculo Padre (Hacia Inscripción)
*El examen no existe en el aire, pertenece a una cursada concreta.*

> **⚠️ Nota de Arquitectura (Junction Object limitation)**
> Como `Inscripción` ya es un objeto conector (Hijo de Alumno y Materia) mediante Master-Detail, Salesforce **no permite** que sea "Master" de otro objeto.
> Por eso, usaremos una **Lookup Relationship** (Búsqueda) obligatoria en lugar de Master-Detail para conectar el Examen. Funcionalmente obtenemos el mismo resultado.

1.  **Fields & Relationships** > **New**.
2.  Tipo: **Lookup Relationship** (Búsqueda).
3.  Related To: **Inscripción** (`Inscripcion`).
4.  **Field Label**: `Inscripción`.
5.  **Field Name**: `Inscripcion` (Sin tilde).
6.  **Next**.
7.  **Importante**: Marca ☑️ **Always require an value in this field in order to save a record**. (Esto simula el comportamiento estricto de un Master-Detail).
8.  **Next** > **Next** > **Save & New**.

### Paso 3: Crear Campos de Datos

#### 3.1 Exam Date (Fecha de Examen)
1.  Data Type: **Date**.
2.  **Field Label**: `Fecha de Examen`.
3.  **Field Name**: `Fecha_Examen`.
4.  **Required**: ☑️ (Always require a value).
5.  **Save & New**.

#### 3.2 Score (Nota)
*La nota específica de esta evaluación.*
1.  Data Type: **Number**.
2.  **Field Label**: `Nota`.
3.  **Field Name**: `Nota`.
4.  **Length**: `4`, **Decimal Places**: `2` (ej: 10.00).
5.  **Save & New**.

#### 3.3 Attended (Asistió)
*Para diferenciar un 0 por "Desconocimiento" de un 0 por "Ausente".*
1.  Data Type: **Checkbox**.
2.  **Field Label**: `Asistió`.
3.  **Field Name**: `Asistio` (Sin tilde).
4.  **Default Value**: `Checked` (True).
5.  **Save & New**.

#### 3.4 Type (Tipo de Examen)
*Opcional pero recomendado para categorizar.*
1.  Data Type: **Picklist**.
2.  **Field Label**: `Tipo`.
3.  **Field Name**: `Tipo`.
4.  Values:
    *   `Parcial 1`
    *   `Parcial 2`
    *   `Final`
    *   `Trabajo Práctico`
5.  **Save**.

### Paso 4: Validaciones de Calidad (Data Quality)

#### 4.1 Rango de Nota
1.  **Validation Rules** > **New**.
2.  **Rule Name**: `Rango_Nota_Examen`.
3.  **Description**: Impide notas menores a 0 o mayores a 10.
4.  **Error Condition Formula**:
    ```sql
    OR( Nota__c < 0, Nota__c > 10 )
    ```
5.  **Error Message**: "Nota inválida. Debe ser un valor entre 0 y 10."
6.  **Save**.

---

## 🚀 Resultado Final
1.  Ve a la App "Gestión Académica Lumina".
2.  Entra a una **Inscripción** activa.
3.  En la pestaña **Related** (Relacionado), verás la lista "Exámenes".
4.  Desde ahí podrás cargar:
    *   "Parcial 1" - 05/03/2026 - Nota: 8.50
    *   "Parcial 2" - 20/04/2026 - Nota: 9.00

¡Ahora tienes trazabilidad completa del rendimiento académico! 📈

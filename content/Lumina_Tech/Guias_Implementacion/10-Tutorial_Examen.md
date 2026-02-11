# 🎓 Guía Técnica: Objeto Examen (Exam)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos - Extensión)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-003](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Gestión de Exámenes y Notas)

---

## 🎯 Objetivo
Permitir la carga granular de evaluaciones (Parciales, Trabajos Prácticos, Finales) relacionándolas a la Inscripción del alumno.
Esto habilita una relación **1 a N** (Una Inscripción tiene Muchos Exámenes).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto Custom
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Exam`
    *   **Plural Label**: `Exams`
    *   **Record Name**: `Exam Name` (Data Type: Text)
    *   En "Optional Features", marca: ☑️ **Track Field History**.
3.  **Save**.

### Paso 2: Crear el Vínculo Padre (Hacia Inscripción)
*El examen no existe en el aire, pertenece a una cursada concreta.*

> **⚠️ Nota de Arquitectura (Junction Object limitation)**
> Dado que `Enrollment` ya es un Objeto Conector (Hijo de Student y Subject), Salesforce **no permite** que sea el "Master" de otro objeto.
> Por lo tanto, usaremos una **Lookup Relationship** obligatoria en su lugar. Funcionalmente es casi idéntico.

1.  **Fields & Relationships** > **New**.
2.  Tipo: **Lookup Relationship**.
3.  Related To: **Enrollment**.
4.  **Label**: `Enrollment`.
5.  **Next**.
6.  **Importante**: Marca la casilla ☑️ **Always require an value in this field in order to save a record**. (Esto simula el comportamiento estricto de un Master-Detail).
7.  **Next** > **Next** > **Save & New**.

### Paso 3: Crear Campos de Datos

#### 3.1 Exam Date (Fecha de Examen)
1.  Data Type: **Date**.
2.  **Field Label**: `Exam Date`.
3.  **Required**: ☑️ (Always require a value).
4.  **Save & New**.

#### 3.2 Score (Nota)
*La nota específica de esta evaluación.*
1.  Data Type: **Number**.
2.  **Field Label**: `Score`.
3.  **Length**: `4`, **Decimal Places**: `2` (ej: 10.00).
4.  **Save & New**.

#### 3.3 Attended (Asistió)
*Para diferenciar un 0 por "Desconocimiento" de un 0 por "Ausente".*
1.  Data Type: **Checkbox**.
2.  **Field Label**: `Attended`.
3.  **Default Value**: `Checked` (True).
4.  **Save & New**.

#### 3.4 Type (Tipo de Examen)
*Opcional pero recomendado para categorizar.*
1.  Data Type: **Picklist**.
2.  **Field Label**: `Type`.
3.  Values:
    *   Partial 1
    *   Partial 2
    *   Final Exam
    *   Practical Work
4.  **Save**.

### Paso 4: Validaciones de Calidad (Data Quality)

#### 4.1 Rango de Nota
1.  **Validation Rules** > **New**.
2.  **Rule Name**: `Exam_Score_Range`.
3.  **Description**: Impide notas menores a 0 o mayores a 10.
4.  **Error Condition Formula**:
    ```sql
    OR( Score__c < 0, Score__c > 10 )
    ```
5.  **Error Message**: "Invalid Score. Please enter a value between 0.00 and 10.00."
6.  **Save**.

---

## 🚀 Resultado Final
1.  Ve a la App "Gestión Académica".
2.  Entra a una **Inscripción** activa.
3.  En la pestaña **Related**, verás la lista "Exams".
4.  Desde ahí podrás cargar:
    *   "Parcial 1" - 05/03/2026 - Nota: 8.50
    *   "Parcial 2" - 20/04/2026 - Nota: 9.00

¡Ahora tienes trazabilidad completa del rendimiento académico! 📈

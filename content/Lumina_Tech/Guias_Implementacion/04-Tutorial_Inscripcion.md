# 🎓 Guía Técnica: Objeto Inscripción (Junction)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-001](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Recursantes), [HU-003](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Notas), [HU-009](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Asistencia)

---

## 🎯 Objetivo
Relacionar "Muchos Alumnos" con "Muchas Materias" mediante un objeto intermedio (Junction Object).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto Conector
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Enrollment`
    *   **Plural Label**: `Enrollments`
    *   **Record Name**: `Enrollment ID`
    *   **Data Type**: **Auto Number** (`ENR-{000000}`)
    *   En "Optional Features", marca: ☑️ **Track Field History**.
3.  **Save**.

### Paso 2: Crear Pata 1 (Hacia Student)
1.  **Fields & Relationships** > **New**.
2.  Tipo: **Master-Detail Relationship**.
3.  Related To: **Student**.
4.  Label: `Student`.
5.  **Next** > **Next** > **Save & New**.

### Paso 3: Crear Pata 2 (Hacia Subject)
1.  Tipo: **Master-Detail Relationship**.
2.  Related To: **Subject**.
3.  Label: `Subject`.
4.  **Next** > **Next** > **Save**.

### Paso 4: Crear Atributos de la Relación (Operativos)

#### 4.1 Cycle (Ciclo Lectivo)
*Fundamental para recursantes (mismo alumno, misma materia, distinto ciclo).*
1.  **New** > Data Type: **Picklist**. Next.
2.  **Field Label**: `Cycle`.
3.  Values:
    *   2024-1
    *   2024-2
    *   2025-1
    *   2025-2
4.  **Next** > **Next** > **Save & New**.

#### 4.2 Commission (Comisión)
1.  **New** > Data Type: **Picklist**. Next.
2.  **Field Label**: `Commission`.
3.  Values (Enter manually):
    *   `Morning A`
    *   `Morning B`
    *   `Afternoon A`
    *   `Afternoon B`
    *   `Night A`
4.  **Save & New**.

#### 4.3 Status (Estado de Cursada)
1.  **New** > Data Type: **Picklist**.
2.  **Field Label**: `Status`.
3.  Valores:
    *   Enrolled (Cursando)
    *   Passed (Aprobado)
    *   Failed (Desaprobado)
4.  **Use first value as default**: ☑️ (Enrolled).
5.  **Next** > **Next** > **Save**.

### Paso 5: Campo de Nota Final (Crucial HU-003)
*Este campo es necesario para calcular aprobaciones.*

1.  En el Object Manager de **Enrollment**, ve a **Fields & Relationships**.
2.  Haz clic en el botón **Set History Tracking** (arriba a la derecha) y activa el tracking para **Final Grade** una vez creado.
3.  Haz clic en el botón **New**.
4.  Selecciona el Data Type: **Number**. Haz clic en **Next**.
5.  Completa los detalles exactos (Refinado por Cliente):
    *   **Field Label**: `Final Grade`
    *   **Length**: `4`
    *   **Decimal Places**: `2`
    *   *Resultado visible*: `10.00`
6.  Haz clic en **Next** (Field Level Security). Dejar visible.
7.  Haz clic en **Next** (Add to Page Layout).
8.  Haz clic en **Save & New**.

### Paso 6: Automatización de Asistencia (HU-009)
*Implementación del requisito de 75% de asistencia para regularidad.*

#### 6.1 Classes Attended (Clases Presentes)
1.  Data Type: **Number**.
2.  **Field Label**: `Classes Attended`.
3.  Length: `3`, Decimals: `0`.
4.  **Save & New**.

#### 6.2 Classes Total (Clases Totales - Snapshot)
*Nota: Idealmente esto viene de la Materia, pero lo creamos aquí para cálculo directo por ahora.*
1.  Data Type: **Number**.
2.  **Field Label**: `Total Classes`.
3.  Length: `3`, Decimals: `0`.
4.  **Save & New**.

#### 6.3 Attendance % (Porcentaje)
1.  Data Type: **Formula**.
2.  **Field Label**: `Attendance Percentage`.
3.  Type: **Percent**, Decimal Places: `2`.
4.  Formula:
    ```sql
    IF( Total_Classes__c > 0, Classes_Attended__c / Total_Classes__c, 0 )
    ```
5.  **Save & New**.

#### 6.4 Academic Condition (Semáforo)
1.  Data Type: **Formula**.
2.  **Field Label**: `Academic Condition`.
3.  Type: **Text**.
4.  Formula:
    ```sql
    IF( Attendance_Percentage__c < 0.75, "Libre (Failed)", "Regular")
    ```
5.  **Save**.

### 🛠️ Nota Técnica: Unicidad de Recursantes (HU-001)
Para evitar duplicados en el *mismo* ciclo, se recomienda crear un campo texto único `Enrollment_Key__c` (Unique, Case Sensitive) y llenarlo mediante Flow con la concatenación: `StudentId & "_" & SubjectId & "_" & Cycle__c`.
*(Esta configuración avanzada se realizará en el Sprint de Automatización).*

**IMPORTANTE**: Activa **Set History Tracking** para `Final Grade` y `Academic Condition`. **Save**.

---

## 🚀 Resultado Final (Efecto Many-to-Many)
Ahora, si vas al registro de un **Alumno**, verás una lista relacionada "Inscripciones".
Si vas al registro de una **Materia**, verás una lista relacionada "Inscripciones".

Esto permite que:
*   Juan curse Matemática.
*   Juan curse Historia.
*   María curse Matemática.

¡Has creado una arquitectura escalable! 🏛️

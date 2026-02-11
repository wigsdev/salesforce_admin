# 🎓 Guía Técnica: Objeto Inscripción (Junction)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-001](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Recursantes), [HU-003](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Notas), [HU-009](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Asistencia)

---

## 🎯 Objetivo
Relacionar "Muchos Alumnos" con "Muchas Materias" mediante un objeto intermedio (Junction Object).

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto Conector
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Inscripción`
    *   **Plural Label**: `Inscripciones`
    *   **Object Name**: `Inscripcion` (Sin tilde para API: `Inscripcion__c`).
    *   **Record Name**: `ID Inscripción`
    *   **Data Type**: **Auto Number** (`INS-{000000}`)
    *   En "Optional Features", marca: ☑️ **Track Field History**.
3.  **Save**.

### Paso 2: Crear Pata 1 (Hacia Alumno)
1.  **Fields & Relationships** > **New**.
2.  Tipo: **Master-Detail Relationship**.
3.  Related To: **Alumno**.
4.  Label: `Alumno`. **Field Name**: `Alumno`.
5.  **Next** > **Next** > **Save & New**.

### Paso 3: Crear Pata 2 (Hacia Materia)
1.  Tipo: **Master-Detail Relationship**.
2.  Related To: **Materia**.
3.  Label: `Materia`. **Field Name**: `Materia`.
4.  **Next** > **Next** > **Save**.

### Paso 4: Crear Atributos de la Relación (Operativos)

#### 4.1 Cycle (Ciclo Lectivo)
*Fundamental para recursantes (mismo alumno, misma materia, distinto ciclo).*
1.  **New** > Data Type: **Picklist**. Next.
2.  **Field Label**: `Ciclo`. **Field Name**: `Ciclo`.
3.  Values:
    *   2024-1
    *   2024-2
    *   2025-1
    *   2025-2
4.  **Next** > **Next** > **Save & New**.

#### 4.2 Commission (Comisión)
1.  **New** > Data Type: **Picklist**. Next.
2.  **Field Label**: `Comisión`. **Field Name**: `Comision` (Sin tilde).
3.  Values (Enter manually):
    *   `Mañana A`
    *   `Mañana B`
    *   `Tarde A`
    *   `Tarde B`
    *   `Noche A`
4.  **Save & New**.

#### 4.3 Status (Estado de Cursada)
1.  **New** > Data Type: **Picklist**.
2.  **Field Label**: `Estado`. **Field Name**: `Estado`.
3.  Values:
    *   `Cursando`
    *   `Aprobado`
    *   `Reprobado`
4.  **Use first value as default**: ☑️ (Cursando).
5.  **Next** > **Next** > **Save**.

### Paso 5: Campo de Nota Final (Crucial HU-003)
*Este campo es necesario para calcular aprobaciones.*

1.  En el Object Manager de **Inscripción**, ve a **Fields & Relationships**.
2.  Haz clic en el botón **Set History Tracking** (arriba a la derecha) y activa el tracking para **Nota Final** (`Nota_Final__c`) una vez creado.
3.  Haz clic en el botón **New**.
4.  Selecciona el Data Type: **Number**. Haz clic en **Next**.
5.  Completa los detalles exactos (Refinado por Cliente):
    *   **Field Label**: `Nota Final`
    *   **Field Name**: `Nota_Final`
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
2.  **Field Label**: `Clases Asistidas`. **Field Name**: `Clases_Asistidas`.
3.  Length: `3`, Decimals: `0`.
4.  **Save & New**.

#### 6.2 Classes Total (Clases Totales - Snapshot)
1.  Data Type: **Number**.
2.  **Field Label**: `Clases Totales`. **Field Name**: `Clases_Totales`.
3.  Length: `3`, Decimals: `0`.
4.  **Save & New**.

#### 6.3 Attendance % (Porcentaje)
1.  Data Type: **Formula**.
2.  **Field Label**: `% Asistencia`. **Field Name**: `Porcentaje_Asistencia`.
3.  Type: **Percent**, Decimal Places: `2`.
4.  Formula:
    ```sql
    IF( Clases_Totales__c > 0, Clases_Asistidas__c / Clases_Totales__c, 0 )
    ```
5.  **Save & New**.

#### 6.4 Academic Condition (Semáforo)
1.  Data Type: **Formula**.
2.  **Field Label**: `Condición Académica`. **Field Name**: `Condicion_Academica`.
3.  Type: **Text**.
4.  Formula:
    ```sql
    IF( Porcentaje_Asistencia__c < 0.75, "Libre", "Regular")
    ```
5.  **Save**.

### Paso 7: Prevención de Duplicados (Composite Key)
*Evitar que un alumno se inscriba dos veces a la misma materia en el mismo ciclo.*

#### 7.1 Crear Campo de Clave Única
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Text**. Next.
3.  **Field Label**: `Clave de Inscripción`.
4.  **Field Name**: `Clave_Inscripcion`. Length: `255`.
5.  ☑️ **Unique** (Treat "ABC" and "abc" as different values - Case Sensitive).
6.  ☑️ **External ID** (Recomendado para cargas masivas).
7.  **Next** > **Next** > **Save**.

#### 7.2 Crear Flow de Automatización (Before Save)
1.  Ve a **Setup** > **Process Automation** > **Flows**.
2.  Haz clic en **New Flow** > **Record-Triggered Flow** > **Create**.
3.  **Configure Start**:
    *   **Object**: `Inscripción`.
    *   **Trigger**: A record is created or updated.
    *   **Condition Requirements**: None.
    *   **Optimize for**: Fast Field Updates (Before Save).
4.  Haz clic en el círculo (+) > **Update Triggering Record**.
5.  **Label**: `Set Composite Key`.
6.  **Set Field Values for the Enrollment Record**:
    *   **Field**: `Clave_Inscripcion__c`
    *   **Value**: New Resource > Formula.
        *   **API Name**: `form_CompositeKey`
        *   **Data Type**: Text
        *   **Formula**: `{!$Record.Alumno__c} & "_" & {!$Record.Materia__c} & "_" & TEXT({!$Record.Ciclo__c})`
7.  Haz clic en **Check Syntax** > **Done**.
8.  Haz clic en **Save**. Label: `Inscripción: Generar Clave Compuesta`.
9.  Haz clic en **Activate**.

**IMPORTANTE**: Activa **Set History Tracking** para `Nota Final` y `Condición Académica`. **Save**.

---

## 🚀 Resultado Final (Efecto Many-to-Many)
Ahora, si vas al registro de un **Alumno**, verás una lista relacionada "Inscripciones".
Si vas al registro de una **Materia**, verás una lista relacionada "Inscripciones".

Esto permite que:
*   Juan curse Matemática.
*   Juan curse Historia.
*   María curse Matemática.

**Prueba de Fuego (Duplicados):**
1.  Inscribe a Juan en "Matemática" (Ciclo 2024-1).
2.  Intenta inscribir DE NUEVO a Juan en "Matemática" (Ciclo 2024-1).
3.  **Resultado**: Salesforce bloqueará el guardado con un error de "Duplicate Value".

¡Has creado una arquitectura escalable y robusta! 🏛️

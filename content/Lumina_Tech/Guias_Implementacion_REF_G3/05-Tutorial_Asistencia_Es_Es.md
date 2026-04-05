# 🎓 Guía Técnica: Objeto Asistencia (Granularidad)

**Sprint**: 02 (Control Académico)
**Día**: 4 (Seguimiento Diario)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-009](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Control de Asistencia)

---

## 🎯 Objetivo
Desacoplar el control de asistencia del objeto de Inscripción. En lugar de números manuales ("Faltó 5 veces"), registraremos **cada clase** individualmente.
Esto permite saber *cuándo* faltó el alumno y calcular la regularidad automáticamente.

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto Detalle (Hijo)
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Asistencia`
    *   **Plural Label**: `Asistencias`
    *   **Object Name**: `Asistencia`
    *   **Record Name**: `ID Asistencia` (Auto Number: `AST-{000000}`)
    *   **Optional Features**: ☑️ Track Field History.
3.  **Launch New Custom Tab Wizard**: ☑️.
4.  **Save**.

### Paso 1.1: Configurar Tab
*   Elige un ícono (ej: *Calendar*).
*   Visibility: **Default On**.
*   Apps: Incluir en **Gestión Académica Lumina**.

### Paso 1.2: Crear Vista "Todas las Asistencias" (List View)
1.  Ve a la pestaña **Asistencias**.
2.  **New**. Name: `Todas`. Visibility: **All users**.
3.  **Fields**: `Fecha`, `Nombre del Alumno`, `Nombre de la Materia`, `Estado`, `Tipo de Clase`.
4.  **Save**.

### Paso 2: Crear la Relación (Lookup Relationship)
*Al tener Inscripción ya 2 padres (Materia/Alumno), debemos usar Lookup.*
1.  **Fields & Relationships** > **New**.
2.  Type: **Lookup Relationship**.
3.  Related To: **Inscripción**.
4.  **Field Label**: `Inscripción`. **Field Name**: `Inscripcion`.
5.  **Required**: ☑️ (Always require a value...).
6.  **Next** > **Next** > **Save**.

### Paso 3: Crear Campos de Registro

#### 3.1 Fecha de Clase
1.  **New** > Data Type: **Date**.
2.  **Field Label**: `Fecha`. **Field Name**: `Fecha`.
3.  **Required**: ☑️.
4.  **Default Value**: `Today()`.
5.  **Save & New**.

#### 3.2 Estado (Picklist)
1.  **New** > Data Type: **Picklist**.
2.  **Field Label**: `Estado`. **Field Name**: `Estado`.
3.  **Values**:
    *   `Presente`
    *   `Ausente`
    *   `Tarde`
    *   `Justificado`
4.  **Default Value (Formula Editor)**: `"Presente"` (Con comillas dobles).
5.  **Save & New**.

#### 3.3 Tipo de Clase (NUEVO)
*Distingue entre carga teórica (4h) y práctica (2h).*
1.  **New** > Data Type: **Picklist**.
2.  **Field Label**: `Tipo de Clase`. **Field Name**: `Tipo_Clase`.
3.  **Values**:
    *   `Teórica`
    *   `Práctica`
    *   `Laboratorio`
4.  **Required**: ☑️.
5.  **Save & New**.

#### 3.4 Nombre del Alumno (Fórmula - UX)
*Campo calculado para mostrar el nombre completo del alumno en las listas, en lugar del ID de inscripción.*
1.  **New** > Data Type: **Formula**. Next.
2.  **Field Label**: `Nombre del Alumno`. **Field Name**: `Nombre_Alumno`.
3.  Type: **Text**.
4.  **Formula**:
    ```sql
    Inscripcion__r.Alumno__r.Nombres__c & " " & Inscripcion__r.Alumno__r.Apellidos__c
    ```
5.  **Check Syntax**. (Resultado esperado: "Juan Pérez")
6.  **Next** > **Next** > **Save & New**.

#### 3.5 Nombre de la Materia (Fórmula - UX)
*Campo calculado para mostrar el nombre de la materia en lugar del ID de inscripción.*
1.  **New** > Data Type: **Formula**. Next.
2.  **Field Label**: `Nombre de la Materia`. **Field Name**: `Nombre_Materia`.
3.  Type: **Text**.
4.  **Formula**:
    ```sql
    Inscripcion__r.Materia__r.Name
    ```
5.  **Check Syntax**. (Resultado esperado: "Matemática I")
6.  **Next** > **Next** > **Save & New**.

#### 3.6 Observaciones
1.  **New** > Data Type: **Text Area**.
2.  **Field Label**: `Observaciones`. **Field Name**: `Observaciones`.
3.  **Save**.

### Paso 4: Automatización (Referencia)
*La lógica de cálculo de regularidad (Target Semestral vs Clases Presentes) se ha centralizado en el objeto Inscripción.*

> **Ver Configuración en:** [Guía 04 - Inscripción (Paso 7)](./04-Tutorial_Inscripcion_Es_Es.md#paso-7-automatización-de-asistencia-lógica-rectora) (Configura los campos `Clases_Esperadas`, `Clases_Presentes`, y `% Asistencia`).

---

## 🛡️ Validaciones de Calidad (Referencia)
> **Ver Configuración en:** [Guía 09 - Validaciones (Caso 5)](./09-Tutorial_Validaciones_Es_Es.md#objeto-asistencia-ver-guía-05)
> *   Regla `Fecha_No_Futura` (Caso 5).

---

## 🚀 Validaciones Funcionales
1.  Entra una **Inscripción** existente vinculada a una Materia con `4 horas semanales`.
    *   *Cálculo Esperado*: `(4 / 2) * 16` = 32 Clases Esperadas.
2.  Verifica que el campo `Clases Esperadas` muestre **32**.
3.  Ve a la lista relacionada **Asistencias** y crea 2 registros `Presente`.
    *   *Nota*: El Flow debe incrementar `Clases Presentes` en 2.
4.  Verifica:
    *   % Asistencia = 2 / 32 = 6.25%
    *   Condición = "Libre" (Obvio, recién empieza).

¡Has automatizado el control de regularidad con la lógica de la Rectora! 📉📈

---

## 📝 Resumen Técnico del Objeto

| Característica | Detalle |
| :--- | :--- |
| **API Name** | `Asistencia__c` |
| **Tipo** | Custom Object (Detail) |
| **Relaciones** | **Lookup (Required)** con `Inscripción`. |

### Campos Clave

| Field Label | API Name | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| **ID Asistencia** | `Name` | Auto Number | ID único (AST-{000000}). |
| **Inscripción** | `Inscripcion__c` | Lookup | Vínculo con la cursada del alumno (Required). |
| **Nombre del Alumno** | `Nombre_Alumno__c` | Formula | Muestra nombre completo del estudiante (UX). |
| **Nombre de la Materia** | `Nombre_Materia__c` | Formula | Muestra nombre de la asignatura (UX). |
| **Fecha** | `Fecha__c` | Date | Fecha de la clase (Required, Default: Today). |
| **Estado** | `Estado__c` | Picklist | Presente, Ausente, Tarde, Justificado (Default: Presente). |
| **Tipo de Clase** | `Tipo_Clase__c` | Picklist | Teórica, Práctica, Laboratorio (Required). |
| **Observaciones** | `Observaciones__c` | Text Area | Notas adicionales del docente. |

### Validaciones
*   `Fecha_No_Futura`: No se puede registrar asistencia para fechas futuras (Ver Guía 09, Caso 5).

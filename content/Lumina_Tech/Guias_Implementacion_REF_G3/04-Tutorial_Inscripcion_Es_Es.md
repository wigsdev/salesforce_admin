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
4.  En "Object Creation Options" (al final), marca: ☑️ **Launch New Custom Tab Wizard after saving custom object**.
5.  Haz clic en **Save**.

### Paso 1.1: Definir Estilo de Pestaña (Tab)
1.  **Tab Style**: Selecciona un ícono (ej: *Form*).
2.  Haz clic en **Next**.
3.  **Profiles**: Deja **Default On**. Haz clic en **Next**.
4.  **Apps**: Desmarca "Include Tab" (lo haremos manualmente luego) o déjalo marcado. Haz clic en **Save**.

### Paso 1.2: Crear Vista "Todas las Inscripciones" (List View)
1.  Ve a la pestaña **Inscripciones**.
2.  **New**. Name: `Todas`. Visibility: **All users**.
3.  **Fields**: `Alumno`, `Materia`, `Ciclo`, `Estado`.
4.  **Save**.

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

#### 4.2 Turno (Comisión)
*Define el horario de cursada. Vital para separar los grupos.*
1.  **New** > Data Type: **Picklist**. Next.
2.  **Field Label**: `Turno`. **Field Name**: `Turno`.
3.  Values (Enter manually):
    *   `Mañana`
    *   `Tarde`
    *   `Noche`
4.  **Save & New**.

#### 4.3 Profesor Titular (Lookup)
*Vincula la inscripción al docente responsable (para seguridad y asignación).*
1.  **New** > Data Type: **Lookup Relationship**.
2.  **Related To**: **User**.
3.  **Field Label**: `Profesor Titular`. **Field Name**: `Profesor`.
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

### Paso 5: Prevención de Duplicados (Composite Key)
*Evitar que un alumno se inscriba dos veces a la misma materia en el mismo ciclo.*

#### 5.1 Crear Campo de Clave Única
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Text**. Next.
3.  **Field Label**: `Clave de Inscripción`.
4.  **Field Name**: `Clave_Inscripcion`. Length: `255`.
5.  ☑️ **Unique** (Treat "ABC" and "abc" as different values - Case Sensitive).
6.  ☑️ **External ID** (Recomendado para cargas masivas).
7.  **Next** > **Next** > **Save**.

#### 5.2 Crear Flow de Automatización (Before Save)
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
8.  Haz clic en **Save**. Label: `Inscripción: Generar Clave Compuesta`.
9.  Haz clic en **Activate**.

### Paso 6: Validaciones de Negocio (Referencia)

> **Ver Configuración en:** [Guía 09 - Validaciones (Casos 3 y 4)](./09-Tutorial_Validaciones_Es_Es.md#objeto-inscripción-ver-guía-04)
> *   Regla `Solo_Alumnos_Matriculados` (Caso 3).
> *   Regla `Coherencia_Carrera_Materia` (Caso 4).

### Paso 7: Automatización de Asistencia (Lógica "Rectora")
*Cálculo automático de Regularidad basado en horas de la materia.*

#### 7.1 Clases Presentes (Acumulador)
*Este campo recibirá la suma de asistencias (Count) desde el objeto Asistencia (vía Flow).*
1.  **New** > Data Type: **Number**.
2.  **Field Label**: `Clases Presentes`. **Field Name**: `Clases_Presentes`.
3.  Length: `3`, Decimals: `0`. Default: `0`.
4.  **Save & New**.

#### 7.2 Nota Final (Calculada - NUEVO)
*Suma de notas ponderadas. Se llena automáticamente por un Flow.*
1.  **New** > Data Type: **Number**.
2.  **Field Label**: `Nota Final`. **Field Name**: `Nota_Final`.
3.  Length: `4`, Decimals: `2`.
4.  **Save & New**.

#### 7.3 Clases Esperadas (Target Semestral)
*Calcula cuántas clases debería haber en un cuatrimestre (16 semanas) según la carga horaria.*
*Regla: División entera de Horas Semanales / 2.*
1.  **New** > Data Type: **Formula**.
2.  **Field Label**: `Clases Esperadas`. **Field Name**: `Clases_Esperadas`.
3.  Type: **Number** (0 decimals).
4.  Formula:
    ```sql
    FLOOR( Materia__r.Horas_Semanales__c / 2 ) * 16
    ```
5.  **Save & New**.

#### 7.3 % Asistencia (Real vs Esperado)
*Porcentaje de cumplimiento.*
1.  **New** > Data Type: **Formula**.
2.  **Field Label**: `% Asistencia`. **Field Name**: `Porcentaje_Asistencia`.
3.  Type: **Percent** (2 decimals).
4.  Formula:
    ```sql
    IF( Clases_Esperadas__c > 0, Clases_Presentes__c / Clases_Esperadas__c, 0 )
    ```
5.  **Save & New**.

#### 7.4 Condición Académica (Semáforo)
*Calcula si el alumno queda Libre (< 75%).*
1.  **New** > Data Type: **Formula**.
2.  **Field Label**: `Condición Académica`. **Field Name**: `Condicion_Academica`.
3.  Type: **Text**.
4.  Formula:
    ```sql
    IF( Porcentaje_Asistencia__c < 0.75, "Libre", "Regular")
    ```
5.  **Save**.

---

## 🚀 Resultado Final (Modelo "Limpio")
Ahora la Inscripción es un contrato puro:
*   **Alumno** (Quién)
*   **Materia** (Qué)
*   **Ciclo/Comisión** (Cuándo/Dónde)

**¿Y las Notas y Asistencia?**
*   Las Notas se gestionan con el objeto **Nota** ([Guía 10](./10-Tutorial_Nota_Es_Es.md)).
*   La Asistencia se gestiona con el objeto **Asistencia** ([Guía 11](./11-Tutorial_Asistencia_Es_Es.md)).
*   Estos módulos avanzados se conectarán a la inscripción más adelante, manteniendo el núcleo limpio.

**Prueba de Fuego (Duplicados):**
1.  Inscribe a Juan en "Matemática" (Ciclo 2024-1).
2.  Intenta inscribir DE NUEVO a Juan en "Matemática" (Ciclo 2024-1).
3.  **Resultado**: Salesforce bloqueará el guardado con un error de "Duplicate Value".

¡Has creado una arquitectura modular y escalable! 🏛️

---

## 📝 Resumen Técnico del Objeto

| Característica | Detalle |
| :--- | :--- |
| **API Name** | `Inscripcion__c` |
| **Tipo** | Junction Object (Conector M:N) |
| **Relaciones** | **Master-Detail** con `Alumno` y `Materia`. |

### Campos Clave

| Field Label | API Name | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| **Código** | `Name` | Auto Number | ID único (INS-{0000}). |
| **Alumno** | `Alumno__c` | Master-Detail | Estudiante inscrito. |
| **Materia** | `Materia__c` | Master-Detail | Asignatura a cursar. |
| **Ciclo y Turno** | `Ciclo__c`, `Turno__c` | Picklist | Coordenadas espacio-temporales. |
| **Clave Única** | `Clave_Inscripcion__c` | Text (Unique) | Clave compuesta para evitar duplicados. |
| **Estado** | `Estado__c` | Picklist | Cursando, Aprobado, Reprobado. |
| **Nota Final** | `Nota_Final__c` | Number | Promedio calculado (vía Flow). |
| **Condición** | `Condicion_Academica__c` | Formula | Libre / Regular (Semáforo de Asistencia). |

### Validaciones y Automatización
*   **Unicidad**: Flow `Set Composite Key` + campo Unique `Clave_Inscripcion` evitan dobles inscripciones en el mismo ciclo.
*   `Solo_Alumnos_Matriculados`: Bloquea inscripción si el alumno está de baja.
*   `Coherencia_Carrera_Materia`: Bloquea si la materia no pertenece a la carrera del alumno.
```

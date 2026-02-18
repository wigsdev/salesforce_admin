# 🎓 Guía Técnica: Reglas de Validación (Business Logic)

**Sprint**: 01 (Fundamentos)
**Día**: 3 (Calidad de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-007](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Email), [HU-008](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Grade Range)

---

## 🎯 Objetivo
"Blindar" la base de datos para asegurar que no entre basura. Implementaremos lógica para Emails, DNI y Notas.

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

---

### [OBJETO: ALUMNO] (Ver Guía 03)

#### Caso 1: Validación de DNI (LatAm - HU-002)
**Contexto**: El documento debe ser numérico y tener exactamente 8 dígitos.

1.  Ve a **Setup** > **Object Manager** > **Alumno**.
2.  En el menú izquierdo, haz clic en **Validation Rules** > **New**.
3.  **Rule Name**: `DNI_Numerico_8`.
4.  **Error Condition Formula**:
    ```sql
    NOT(REGEX(DNI__c, "^[0-9]{8}$"))
    ```
5.  **Error Message**: "El DNI debe tener exactamente 8 dígitos numéricos."
6.  **Error Location**: Selecciona **Field** > `DNI`.
7.  **Save & New**.

#### Caso 2: Validación de Formato de Email (HU-007)
**Contexto**: Queremos asegurar que el email tenga un formato válido (ej: usuario@dominio.com).

1.  **Rule Name**: `Formato_Email_Valido`.
2.  **Description**: Enforces valid email structure.
3.  **Error Condition Formula**:
    ```sql
    NOT(REGEX(Email_Personal__c, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$"))
    ```
4.  **Error Message**: "El formato del email es inválido (ej: nombre@dominio.com)".
5.  **Error Location**: Selecciona **Field** > `Email Personal`.
6.  **Save & New`.

#### Caso 3: Fecha de Ingreso No Futura (NUEVO)
**Contexto**: No se puede registrar un ingreso con fecha mayor a hoy.
1.  Ve a **Object Manager** > **Alumno**.
2.  **Validation Rules** > **New**.
3.  **Rule Name**: `Fecha_Ingreso_No_Futura`.
4.  **Formula**: `Fecha_Ingreso__c > TODAY()`
5.  **Error Message**: "La fecha de ingreso no puede ser futura."
6.  **Location**: `Fecha de Ingreso`.
7.  **Save**.

---

### [OBJETO: MATERIA] (Ver Guía 02)

#### Validación de Esquema (Schema Validations)
*A diferencia de las Reglas de Validación (Fórmulas), estas restricciones YA fueron configuradas en la definición del campo (Guía 02). **No debes crear nada nuevo aquí**.*

1.  **Integridad Referencial (Master-Detail)**:
    *   **Regla**: Toda Materia debe pertenecer obligatoriamente a una Carrera.
    *   **Estado**: ✅ **Configurada** (Al crear la relación `Master-Detail`). Salesforce impide guardar una materia huérfana automáticamente.

2.  **Unicidad de Código Externo**:
    *   **Regla**: El campo `Codigo_Externo__c` no puede duplicarse.
    *   **Estado**: ✅ **Configurada** (Marcando la casilla `Unique` en el campo). Evita duplicados durante cargas.

---

### [OBJETO: INSCRIPCIÓN] (Ver Guía 04)

#### Caso 3: Solo Alumnos Matriculados
**Contexto**: Impide inscribir alumnos que no tengan la cuota al día (Estado = Matriculado).

1.  Ve a **Object Manager** > **Inscripción**.
2.  **Validation Rules** > **New**.
3.  **Rule Name**: `Solo_Alumnos_Matriculados`.
4.  **Error Condition Formula**:
    ```sql
    TEXT(Alumno__r.Estado__c) <> "Matriculado"
    ```
5.  **Error Message**: "El alumno no está Matriculado activo. Verifique su situación administrativa."
6.  **Location**: `Alumno`.
7.  **Save & New**.

#### Caso 4: Coherencia de Carrera (Cross-Object)
**Contexto**: Un alumno de Ingeniería no puede cursar materias de Medicina.

1.  **Rule Name**: `Coherencia_Carrera_Materia`.
2.  **Formula**:
    ```sql
    Materia__r.Carrera__c <> Alumno__r.Carrera__c
    ```
3.  **Error Message**: "Error Académico: La materia seleccionada no pertenece a la carrera del alumno."
4.  **Location**: `Materia`.
5.  **Save & New**.

#### Caso 5: Seguridad Alumno (Anti-Fraude)
**Contexto**: Impide que un usuario Alumno inscriba a otro alumno que no sea él mismo.
1.  **Rule Name**: `Seguridad_Inscripcion_Propia`.
2.  **Formula**:
    ```sql
    AND(
      $Profile.Name = "Lumina Student",
      Alumno__r.Usuario_Sistema__c != $User.Username
    )
    ```
    *(Requisito: El Username del usuario logueado debe coincidir exactamente con el DNI@lumina.edu.ar calculado en la ficha del alumno).*
3.  **Error Message**: "Solo puedes inscribirte a ti mismo."
4.  **Location**: `Alumno`.
5.  **Save**.

---

### [OBJETO: ASISTENCIA] (Ver Guía 05)

#### Caso 5: Fecha no Futura
**Contexto**: No se puede registrar asistencia para días que aún no han ocurrido.

1.  Ve a **Object Manager** > **Asistencia**.
2.  **Validation Rules** > **New**.
3.  **Rule Name**: `Fecha_No_Futura`.
4.  **Formula**:
    ```sql
    Fecha__c > TODAY()
    ```
5.  **Error Message**: "La fecha de asistencia no puede ser futura."
6.  **Location**: `Fecha`.
7.  **Save & New`.

#### Caso 6: Rango de Calificación Parcial
**Contexto**: Impide notas parciales menores a 1 o mayores a 10 en el objeto Nota.

1.  Ve a **Object Manager** > **Nota**.
2.  **Validation Rules** > **New**.
3.  **Rule Name**: `Rango_Nota_Valida`.
4.  **Error Condition Formula**:
    ```sql
    OR( Calificacion__c < 1, Calificacion__c > 10 )
    ```
5.  **Error Message**: "Calificación inválida. Debe ser entre 1 y 10."
6.  **Location**: `Calificación`.
7.  **Save**.

---

## ✅ Verificación de Éxito
1.  **Alumno**: Intenta crear uno con DNI `ABC` o Email `pepe@gmail` (sin .com). -> **Error**.
2.  **Inscripción**: Intenta inscribir a un alumno `Suspendido`. -> **Error**.
3.  **Asistencia**: Intenta cargar fecha `01/01/2099`. -> **Error**.
4.  **Nota**: Intenta cargar un parcial con `-1`. -> **Error**.

# 🎓 Guía Técnica: Reglas de Validación (Business Logic)

**Sprint**: 01 (Fundamentos)
**Día**: 3 (Calidad de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-007](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Email), [HU-008](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Grade Range)

---

## 🎯 Objetivo
"Blindar" la base de datos para asegurar que no entre basura. Implementaremos lógica para Emails y Notas.

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Caso A: Validación de Formato de Email (HU-007)
**Contexto**: Queremos asegurar que el email tenga un formato válido (ej: usuario@dominio.com).

1.  Ve a **Setup** > **Object Manager**.
2.  Busca y haz clic en **Alumno**.
3.  En el menú izquierdo, haz clic en **Validation Rules**.
4.  Haz clic en **New**.
5.  **Rule Name**: Escribe `Formato_Email_Valido`.
6.  **Description**: Escribe "Enforces valid email structure".
7.  **Error Condition Formula**:
    *   Copia y pega EXACTAMENTE esto en el cuadro grande:
    ```sql
    NOT(REGEX(Email_Personal__c, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$"))
    ```
8.  Haz clic en el botón **Check Syntax**. Espera a ver "No errors found".
9.  **Error Message**: Escribe "El formato del email es inválido (ej: nombre@dominio.com)".
10. **Error Location**: Selecciona la opción **Field** y busca `Email Personal`.
11. Haz clic en **Save**.

### Caso B: Rango de Notas Lógico (HU-008)
**Contexto**: No existen notas negativas ni mayores a 10.

1.  Ve a **Object Manager** > **Inscripción**.
2.  Ve a **Validation Rules**. Haz clic en **New**.
3.  **Rule Name**: Escribe `Rango_Nota_1_10`.
4.  **Error Condition Formula**:
    *   Copia y pega:
    ```sql
    OR(
      Nota_Final__c < 1,
      Nota_Final__c > 10
    )
    ```
5.  Haz clic en **Check Syntax**.
6.  **Error Message**: "Nota Inválida. Debe estar entre 1 y 10."
7.  **Error Location**: Selecciona **Field** > `Nota Final`.
8.  Haz clic en **Save**.

### Caso C: Consistencia de Estado (Integridad)
**Contexto**: No puedo estar "Aprobado" sin tener nota.

1.  **Object Manager** > **Inscripción** > **Validation Rules** > **New**.
2.  **Rule Name**: `Estado_Requiere_Nota`.
3.  **Formula**:
    ```sql
    AND(
      OR(
        ISPICKVAL(Estado__c, "Aprobado"),
        ISPICKVAL(Estado__c, "Reprobado")
      ),
      ISBLANK(Nota_Final__c)
    )
    ```
4.  **Error Message**: "El estado no puede ser Aprobado/Reprobado sin una Nota Final."
5.  **Location**: `Nota Final`.
6.  **Save**.

### Caso D: Validación de DNI (LatAm - HU-002)
**Contexto**: El documento debe ser numérico y tener exactamente 8 dígitos.

1.  **Object Manager** > **Alumno** > **Validation Rules** > **New**.
2.  **Rule Name**: `DNI_Numerico_8`.
3.  **Formula**:
    ```sql
    NOT(REGEX(DNI__c, "^[0-9]{8}$"))
    ```
4.  **Error Message**: "El DNI debe tener exactamente 8 dígitos numéricos."
5.  **Location**: `DNI`.
6.  **Save**.

---

## ✅ Verificación de Éxito
1.  Ve a la pestaña **Alumnos**.
2.  Intenta crear uno con email: `pepe@gmail.com`.
    *   **Resultado**: Bloqueo con mensaje de error rojo.
3.  Cambia el email a `pepe@lumina.edu` y guarda.
    *   **Resultado**: Éxito.
4.  Ve a **Inscripciones**. Intenta poner nota `15`.
    *   **Resultado**: Bloqueo.
5.  Intenta cambiar Estado a "Aprobado" dejando la nota vacía.
    *   **Resultado**: Bloqueo "Debe ingresar una Nota Final".

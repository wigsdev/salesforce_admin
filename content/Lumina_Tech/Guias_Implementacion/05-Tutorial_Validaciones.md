# 🎓 Guía Técnica: Reglas de Validación (Business Logic)

**Sprint**: 01 (Fundamentos)
**Día**: 3 (Calidad de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-007](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Email), [HU-008](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Grade Range)

---

## 🎯 Objetivo
"Blindar" la base de datos para asegurar que no entre basura. Implementaremos lógica para Emails y Notas.

## 🛠️ Procedimiento

### Caso A: Validación de Formato de Email (HU-007)
**Contexto**: Queremos asegurar que el email tenga un formato válido de estructura (ej: usuario@dominio.com).

1.  Ve a **Setup** > **Object Manager**.
2.  Busca y haz clic en **Student**.
3.  En el menú izquierdo, haz clic en **Validation Rules**.
4.  Haz clic en **New**.
5.  **Rule Name**: Escribe `Valid_Email_Format`.
6.  **Description**: Escribe "Enforces valid email structure".
7.  **Error Condition Formula**:
    *   Copia y pega EXACTAMENTE esto en el cuadro grande:
    ```sql
    NOT(REGEX(Personal_Email__c, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$"))
    ```
    *(Nota: Asegúrate de usar el API Name correcto. Si creaste el campo en inglés será `Personal_Email__c`).*
8.  Haz clic en el botón **Check Syntax**. Espera a ver "No errors found".
9.  **Error Message**: Escribe "Invalid email format (e.g. name@domain.com)".
10. **Error Location**: Selecciona la opción **Field** y busca `Personal Email`.
11. Haz clic en **Save**.

### Caso B: Rango de Notas Lógico (HU-008)
**Contexto**: No existen notas negativas ni mayores a 10.

1.  Ve a **Object Manager** > **Enrollment**.
2.  Ve a **Validation Rules**. Haz clic en **New**.
3.  **Rule Name**: Escribe `Grade_Range_1_10`.
4.  **Error Condition Formula**:
    *   Copia y pega:
    ```sql
    OR(
      Final_Grade__c < 1,
      Final_Grade__c > 10
    )
    ```
5.  Haz clic en **Check Syntax**.
6.  **Error Message**: "Invalid Grade. Must be between 1 and 10."
7.  **Error Location**: Selecciona **Field** > `Final Grade`.
8.  Haz clic en **Save**.

### Caso C: Consistencia de Estado (Integridad)
**Contexto**: No puedo estar "Aprobado" sin tener nota.

1.  **Object Manager** > **Enrollment** > **Validation Rules** > **New**.
2.  **Rule Name**: `Status_Requires_Grade`.
3.  **Formula**:
    ```sql
    AND(
      OR(
        ISPICKVAL(Status__c, "Passed"),
        ISPICKVAL(Status__c, "Failed")
      ),
      ISBLANK(Final_Grade__c)
    )
    ```
4.  **Error Message**: "Status cannot be Passed/Failed without a Final Grade."
5.  **Location**: `Final Grade`.
6.  **Save**.

### Caso D: Validación de DNI (LatAm - HU-002)
**Contexto**: El documento debe ser numérico y tener exactamente 8 dígitos.

1.  **Object Manager** > **Student** > **Validation Rules** > **New**.
2.  **Rule Name**: `National_ID_Numeric_8`.
3.  **Formula**:
    ```sql
    NOT(REGEX(National_ID__c, "^[0-9]{8}$"))
    ```
4.  **Error Message**: "National ID must be exactly 8 digits (Numeric)."
5.  **Location**: `National ID`.
6.  **Save**.

---

## ✅ Verificación de Éxito
1.  Ve a la pestaña **Students**.
2.  Intenta crear uno con email: `pepe@gmail,com` (coma).
    *   **Resultado**: Bloqueo con mensaje de error rojo.
3.  Cambia el email a `pepe@gmail.com` y guarda.
    *   **Resultado**: Éxito.
4.  Ve a **Enrollments**. Intenta poner nota `15`.
    *   **Resultado**: Bloqueo.
5.  Intenta cambiar Estado a "Passed" dejando la nota vacía.
    *   **Resultado**: Bloqueo "Debe ingresar una Nota Final".

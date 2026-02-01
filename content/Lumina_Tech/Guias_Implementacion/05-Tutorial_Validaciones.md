# 🎓 Guía Técnica: Reglas de Validación (Business Logic)

**Sprint**: 01 (Fundamentos)
**Día**: 3 (Calidad de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-005 (Email), HU-006 (Rango Notas)

---

## 🎯 Objetivo
"Blindar" la base de datos para asegurar que no entre basura. Implementaremos lógica para Emails y Notas.

## 🛠️ Procedimiento

### Caso A: Validación de Email Institucional
**Contexto**: Queremos que todos los alumnos tengan email `@lumina.edu`.

1.  Ve a **Setup** > **Object Manager**.
2.  Busca y haz clic en **Alumno**.
3.  En el menú izquierdo, haz clic en **Validation Rules**.
4.  Haz clic en **New**.
5.  **Rule Name**: Escribe `Email_Institucional_Valido`.
6.  **Description**: Escribe "Fuerza el formato @lumina.edu".
7.  **Error Condition Formula**:
    *   Copia y pega EXACTAMENTE esto en el cuadro grande:
    ```sql
    NOT(REGEX(Email_Personal__c, "[a-zA-Z0-9._%+-]+@lumina\\.edu"))
    ```
    *(Nota: Asegúrate de usar el API Name correcto de tu campo email, si es diferente).*
8.  Haz clic en el botón **Check Syntax**. Espera a ver "No errors found".
9.  **Error Message**: Escribe "El email debe ser institucional (@lumina.edu)".
10. **Error Location**: Selecciona la opción **Field** y busca `Email Personal`.
11. Haz clic en **Save**.

### Caso B: Rango de Notas Lógico
**Contexto**: No existen notas negativas ni mayores a 10.

1.  Ve a **Object Manager** > **Inscripción**.
2.  Ve a **Validation Rules**. Haz clic en **New**.
3.  **Rule Name**: Escribe `Nota_Rango_0_a_10`.
4.  **Error Condition Formula**:
    *   Copia y pega:
    ```sql
    OR(
      Nota_Final__c < 0,
      Nota_Final__c > 10
    )
    ```
5.  Haz clic en **Check Syntax**.
6.  **Error Message**: "La nota es inválida. Ingrese un valor entre 0 y 10."
7.  **Error Location**: Selecciona **Field** > `Nota Final`.
8.  Haz clic en **Save**.

---

## ✅ Verificación de Éxito
1.  Ve a la pestaña **Alumnos**.
2.  Intenta crear uno con email: `pepe@gmail.com`.
    *   **Resultado**: Bloqueo con mensaje de error rojo.
3.  Cambia el email a `pepe@lumina.edu` y guarda.
    *   **Resultado**: Éxito.
4.  Ve a **Inscripciones**. Intenta poner nota `15`.
    *   **Resultado**: Bloqueo.

# 🎓 Guía Paso a Paso: Reglas de Validación (Business Logic)
**Nivel**: Intermedio
**Tiempo Estimado**: 20 minutos
**Requisito**: Haber creado objetos Alumno e Inscripción.

---

## 🎯 Objetivo
"Blindar" la base de datos para asegurar que no entre basura. Implementaremos lógica para Emails y Notas.

## 🛠️ Procedimiento

### Caso A: Validación de Email Institucional
**Contexto**: Queremos que todos los alumnos tengan email `@lumina.edu`.

1.  **Setup > Object Manager > Alumno**.
2.  Menu izquierdo: **Validation Rules**.
3.  Click **New**.
4.  **Rule Name**: `Email_Institucional_Valido`.
5.  **Description**: "Fuerza el formato @lumina.edu".
6.  **Error Condition Formula**:
    (Copia y pega con cuidado)
    ```sql
    NOT(REGEX(Email__c, "[a-zA-Z0-9._-]+@lumina\\.edu"))
    ```
    > *Explicación Tech*: `REGEX` revisa patrones. `NOT` invierte la lógica (si NO coincide, lanza error).

7.  **Check Syntax**: Click en el botón para verificar que no falten paréntesis.
8.  **Error Message**: "El email debe ser institucional (@lumina.edu)".
9.  **Error Location**: Selecciona "Field: Email".
10. **Save**.

### Caso B: Rango de Notas Lógico
**Contexto**: No existen notas negativas ni mayores a 10.

1.  **Object Manager > Inscripción**.
2.  **Validation Rules > New**.
3.  **Rule Name**: `Nota_Rango_0_a_10`.
4.  **Formula**:
    ```sql
    OR(
      Nota_Final__c < 0,
      Nota_Final__c > 10
    )
    ```
    > *Explicación Tech*: La función `OR` dice "Si pasa esto O pasa esto otro, Error".

5.  **Error Message**: "La nota es inválida. Ingrese un valor entre 0 y 10."
6.  **Error Location**: Field: Nota Final.
7.  **Save**.

---

## ✅ Verificación de Éxito
1.  Ve a la tab **Alumnos**.
2.  Intenta crear uno con email: `pepe@gmail.com`.
3.  **Resultado Esperado**: Bloqueo con mensaje de error rojo.
4.  Ve a **Inscripciones**.
5.  Intenta poner nota `15`.
6.  **Resultado Esperado**: Bloqueo.

¡Has implementado tu primera lógica de negocio! 🧠

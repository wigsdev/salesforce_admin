# 🎓 Guía Técnica: Campos Fórmula (Automation Lite)

**Sprint**: 01 (Fundamentos)
**Día**: 3 (Automatización)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-003 ( UX Upgrade)

---

## 🎯 Objetivo
Automatizar cálculos y mostrar información "cruzada" sin que el usuario tenga que escribirla manualmente. Cumple con los requisitos de la **Clase 10**.

## 🛠️ Procedimiento

### Caso A: Estado de Aprobación (Calculado)
**Contexto**: No queremos que el profesor escriba "Aprobado" o "Reprobado". Queremos que Salesforce lo decida según la nota automáticamente.

1.  **Setup > Object Manager > Inscripción**.
2.  **Fields & Relationships > New**.
3.  Tipo: **Formula**. Next.
4.  **Field Label**: `Estado de Cursada`.
5.  **Field Name**: `Estado_Cursada`.
6.  **Formula Return Type**: **Text**. Next.
7.  **Formula Editor**:
    ```sql
    IF( ISBLANK(Nota_Final__c), "En Curso",
      IF( Nota_Final__c >= 6, "Aprobado", "Reprobado")
    )
    ```
    > *Lógica*: Primero revisa si la nota está vacía. Si hay nota, revisa si es mayor o igual a 6.
8.  **Check Syntax**: (Debe salir verde).
9.  **Treat blank fields as**: Blanks.
10. **Next > Next > Save**.

### Caso B: Semáforo Visual (Imagen)
**Contexto**: Queremos una bandera visual rápida para identificar alumnos en riesgo.

1.  **Object Manager > Inscripción**.
2.  **Fields & Relationships > New**.
3.  Tipo: **Formula**.
4.  **Field Label**: `Semáforo`.
5.  **Return Type**: **Text** (¡Sí, texto, aunque sea imagen!).
6.  **Formula**:
    ```sql
    IMAGE( 
      IF( Nota_Final__c >= 6, "/img/samples/flag_green.gif", 
      IF( Nota_Final__c >= 4, "/img/samples/flag_yellow.gif", 
      "/img/samples/flag_red.gif")), 
      "Estado"
    )
    ```
7.  **Save**.

### Caso C: Nombre Completo (Concatenación)
**Contexto**: En los reportes queremos ver "Apellido, Nombre" en una sola columna.

1.  **Object Manager > Alumno**.
2.  **New > Formula > Text**.
3.  **Label**: `Nombre Completo Formato`.
4.  **Formula**:
    ```sql
    Apellido__c & ", " & Nombre__c
    ```
5.  **Save**.

---

## ✅ Verificación
1.  Ve a una **Inscripción**.
2.  Pon nota `8`. Guarda.
    *   *Resultado*: Campo "Estado" debe decir "Aprobado" y Semáforo Verde.
3.  Pon nota `2`. Guarda.
    *   *Resultado*: Campo "Estado" debe decir "Reprobado" y Semáforo Rojo.

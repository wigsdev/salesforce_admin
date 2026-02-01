# 🎓 Guía Técnica: Campos Fórmula (Automation Lite)

**Sprint**: 01 (Fundamentos)
**Día**: 3 (Automatización)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-003 (UX Upgrade)

---

## 🎯 Objetivo
Automatizar cálculos y mostrar información "cruzada".

## 🛠️ Procedimiento

### Caso A: Estado de Aprobación (Calculado)
**Contexto**: Salesforce decidirá si el alumno aprobó basado en la nota.

1.  Ve a **Setup** > **Object Manager** > **Inscripción**.
2.  Ve a **Fields & Relationships**. Haz clic en **New**.
3.  Selecciona Data Type: **Formula**. Haz clic en **Next**.
4.  **Field Label**: `Estado de Cursada`.
5.  **Field Name**: `Estado_Cursada`.
6.  **Formula Return Type**: Selecciona **Text**. Haz clic en **Next**.
7.  **Simple Formula Editor**:
    *   Copia y pega:
    ```sql
    IF( ISBLANK(Nota_Final__c), "En Curso",
      IF( Nota_Final__c >= 6, "Aprobado", "Reprobado")
    )
    ```
8.  Haz clic en **Check Syntax**.
9.  Busca la opción "Blank Field Handling" y selecciona: **Treat blank fields as blanks**.
10. Haz clic en **Next**.
11. Haz clic en **Next**.
12. Haz clic en **Save**.

### Caso B: Semáforo Visual (Imagen)
**Contexto**: Una bandera visual rápida (Verde/Amarillo/Rojo).

1.  En el mismo objeto (**Inscripción**), haz clic en **New**.
2.  Selecciona **Formula**. Haz clic en **Next**.
3.  **Field Label**: `Semáforo`.
4.  **Field Name**: `Semaforo` (Sin tilde).
5.  **Formula Return Type**: Selecciona **Text** (Aunque sea imagen, el output es un string HTML). Haz clic en **Next**.
6.  **Simple Formula Editor**:
    *   Copia y pega:
    ```sql
    IMAGE( 
      IF( Nota_Final__c >= 6, "/img/samples/flag_green.gif", 
      IF( Nota_Final__c >= 4, "/img/samples/flag_yellow.gif", 
      "/img/samples/flag_red.gif")), 
      "Estado"
    )
    ```
7.  Haz clic en **Check Syntax**.
8.  Haz clic en **Next** > **Next** > **Save**.

### Caso C: Nombre Completo (Concatenación)
**Contexto**: Unir Apellido y Nombre en el objeto Alumno.

1.  Ve a **Object Manager** > **Alumno**.
2.  Ve a **Fields & Relationships** > **New**.
3.  Selecciona **Formula**. Haz clic en **Next**.
4.  **Field Label**: `Nombre Completo Formato`.
5.  **Return Type**: **Text**. Haz clic en **Next**.
6.  **Formula**:
    ```sql
    Apellido__c & ", " & Nombre__c
    ```
    *(Nota: Asegúrate de tener un campo llamado `Apellido__c` o usa el standard `Name` si corresponde. Para custom objects, suele ser Name. Si usaste AutoNumber en Alumno, debiste crear campos Texto independientes para Nombre y Apellido primero, pero asumiremos que tienes `Name` o campos custom).*
7.  Haz clic en **Check Syntax**.
8.  Haz clic en **Next** > **Next** > **Save**.

---

## ✅ Verificación
1.  Abre una **Inscripción** existente.
2.  Edita la **Nota Final**: Pon `8`. Guarda.
    *   *Resultado*: Campo "Estado" dice "Aprobado". Bandera Verde.
3.  Edita la nota: Pon `2`. Guarda.
    *   *Resultado*: Campo "Estado" dice "Reprobado". Bandera Roja.

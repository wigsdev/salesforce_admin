# 🎓 Guía Técnica: Módulo de Correlativas (Prerrequisitos)

**Sprint**: 03 (Lógica Académica Avanzada)
**Día**: 5 (Reglas de Negocio)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-004](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Validación de Correlativas)

---

## 🎯 Objetivo
Impedir que un alumno se inscriba en una materia si no ha aprobado las materias correlativas previas.
*Ejemplo: No puedes cursar "Análisis Matemático II" sin haber aprobado "Análisis Matemático I".*

## 🛠️ Procedimiento

### Paso 1: Preparar el Terreno (Inscripción)
*Necesitamos saber si una materia está "Aprobada" o solo "Cursando".*

1.  Ve a **Object Manager** > **Inscripción**.
2.  **Fields & Relationships** > **New**.
3.  Tipo: **Picklist**.
4.  Label: `Estado Académico`. Name: `Estado_Academico`.
5.  Values:
    *   `Cursando` (Default)
    *   `Regularizada` (Aprobó cursada, debe final).
    *   `Aprobada` (Aprobó todo).
    *   `Reprobada`.
6.  **Save**.

### Paso 2: Crear el Objeto "Correlativa"
*Este objeto define las reglas del juego. Es una tabla de conexión.*

1.  **Create** > **Custom Object**.
2.  Label: `Correlativa`. Plural: `Correlativas`.
3.  Name: `Correlativa`.
4.  Record Name: `ID Regla` (Auto Number: `CORR-{0000}`).
5.  **Save**.

#### 2.1 Relación 1: Materia Destino (La que quieres cursar)
*Esta es la relación principal (Master).*
1.  **Fields & Relationships** > **New**.
2.  Type: **Master-Detail**.
3.  Related To: **Materia**.
4.  Label: `Materia Destino`. Name: `Materia_Destino`.
5.  **Save**.

#### 2.2 Relación 2: Materia Requisito (La que debes tener)
*Esta es la materia filtro.*
1.  **New** > Type: **Lookup** (Required).
2.  Related To: **Materia**.
3.  Label: `Materia Requisito`. Name: `Materia_Requisito`.
4.  **Save**.

#### 2.3 Tipo de Requisito
1.  **New** > Type: **Picklist**.
2.  Label: `Tipo Requisito`. Name: `Tipo_Requisito`.
3.  Values:
    *   `Final Aprobado` (Debe tener Estado = Aprobada).
    *   `Cursada Aprobada` (Debe tener Estado = Regularizada o Aprobada).
4.  **Save**.

---

### Paso 3: El Motor de Validación (Flow)

**Lógica**: Al crear una Inscripción, buscar todas las `Correlativas` de la materia. Verificar si el alumno las tiene.

*Por simplicidad en este MVP, usaremos un **Flow de Validación (Before-Save)** que busca en el historial.*

1.  **Flows** > **New Flow** > **Record-Triggered Flow**.
2.  **Object**: `Inscripción`. Trigger: **Create**.
3.   **Decision**: ¿Tiene Correlativas?
    *   (Aquí usamos un elemento **Get Records** para buscar registros en `Correlativa` donde `Materia_Destino` = `{!$Record.Materia__c}`).
    *   Almacena todos los registros.

4.  **Loop**: Iterar sobre las Correlativas encontradas.
    *   **Get Records (Historial)**: Buscar en `Inscripción`.
        *   Criteria: `Alumno` = `{!$Record.Alumno__c}` AND `Materia` = `{!Loop.Materia_Requisito__c}` AND `Estado_Academico` = `Aprobada`.
    *   **Decision**: ¿Encontró registro aprobado?
        *   **NO**: Asignar variable `Falta_Requisito` = `True` y agregar nombre a `Lista_Faltantes`.

5.  **Decision Final**: ¿`Falta_Requisito` es True?
    *   **SÍ**: **Custom Error**.
        *   Message: "No puedes inscribirte. Te faltan las siguientes correlativas aprobadas: {!Lista_Faltantes}".

---

## 🚀 Puesta en Marcha
1.  Crea la materia "Matemática I" y "Matemática II".
2.  Crea un registro en **Correlativas**:
    *   Destino: Matemática II.
    *   Requisito: Matemática I.
    *   Tipo: Final Aprobado.
3.  Intenta inscribir a un alumno nuevo en "Matemática II".
    *   **Resultado**: ❌ Error customizado.
4.  Inscribe al alumno en "Matemática I", cambia su estado a "Aprobada".
5.  Intenta inscribir de nuevo en "Matemática II".
    *   **Resultado**: ✅ Éxito.

¡Has implementado un control académico real! 🎓⛔

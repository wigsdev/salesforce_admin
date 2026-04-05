# 🎓 Guía Técnica: Objeto Inscripción (Junction) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Escudo Anti-Duplicados)
**Referencia**: Gestión de Matrícula y Migración Histórica.

---

## 🎯 Objetivo
Relacionar "Alumnos" con "Materias" mediante un objeto intermedio. En el Sprint 2, este objeto se convierte en el núcleo de la migración de 7,500 registros, incorporando un **Escudo Anti-Duplicados**.

## 🛠️ Procedimiento de Configuración

### Paso 1: Atributos del Objeto (Sprint 1 Baseline)
1.  **Object Manager** > **Inscripcion__c**.
2.  **Record Name**: `ID Inscripción` (Auto Number: `INS-{000000}`).
3.  **Optional Features**: Marcar ☑️ **Allow Reports** (Permitir informes).
4.  **Relationships**: Master-Detail hacia **Alumno** (Contact) y **Materia**.

### Paso 2: [NUEVO S2] Escudo Anti-Duplicados (ID Importación)
*Este campo es la clave maestra para evitar errores en la carga masiva.*

1.  **Fields & Relationships** > **New**.
2.  Data Type: **Text**.
3.  **Field Label**: `ID de Importación`.
4.  **Field Name**: `ID_Importacion`.
5.  **Length**: `50`.
6.  ☑️ **Unique**: **Case Insensitive**. (Bloquea físicamente la duplicidad).
7.  ☑️ **External ID**: **SÍ**. (Permite que las Evaluaciones se vinculen a esta Inscripción).
8.  **Save**.

### Paso 3: Campos Operativos
- **Ciclo**: Picklist (2024-1, 2024-2, etc.).
- **Turno**: Picklist (Mañana, Tarde, Noche).
- **Estado**: Picklist (Cursando, Aprobado, Reprobado).
- **Carrera (F)**: Fórmula (Texto) -> `Materia__r.Carrera__r.Name`. (Crucial para reportes).
- **Año Lectivo**: Campo utilizado en la migración histórica para auditoría.

### Paso 4: Automatización de Asistencia
- **Clases Esperadas**: Fórmula que calcula el target semestral (Horas/2 * 16).
- **% Asistencia**: Fórmula (`Clases_Presentes__c / Clases_Esperadas__c`).
- **Condición Académica**: Fórmula que marca "Libre" si la asistencia es < 75%.

---

## 🚀 Estrategia de Carga (Sprint 2)
Al importar Inscripciones:
1.  **Mapeo de Padres**:
    - `Alumno` -> use `Alumno__r:Numero_Documento__c`.
    - `Materia` -> use `Materia__r:Codigo_Materia__c`.
2.  **ID Importación**: Este campo debe poblarse con el formato `{DNI}-{COD_MATERIA}` (Ej: `45147679-DEV-101`).

### Paso 5: [SOLUCIÓN] Resolución de Problemas de Búsqueda (Materias)
*Si al inscribir un alumno las Materias no aparecen y solo sale "New", sigue estos pasos:*

1.  Ve a **Object Manager** > **Inscripción** > **Fields & Relationships**.
2.  Busca el campo **Materia** (Materia__c) y haz clic en él.
3.  Desplázate hasta la sección **Lookup Filter**.
4.  Si hay un filtro activo, haz clic en **Edit** y:
    - **Recomendación**: Desactiva el filtro (Enable this filter = ❌) y confía en la **Validation Rule** `Coherencia_Carrera_Materia` (Guía 08).
    - **Opción B**: Si quieres mantenerlo, cámbialo de "Required" a **Optional** para que al menos las materias aparezcan en la lista.
5.  Haz clic en **Save**.

---

## ✅ Verificación de Éxito
1.  Intenta inscribir al Alumno X en la Materia Y dos veces en el mismo ciclo (Duplicidad).
    - **Resultado**: Salesforce arroja error por `ID_Importacion__c`.
2.  Busca una materia creada previamente.
    - **Resultado**: La lista de materias aparece correctamente sin requerir "New Materia".

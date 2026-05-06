# 🎓 Guía Técnica: Objeto Inscripción (Junction) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Escudo Anti-Duplicados) / **Refactorización G3/G6**
**Rol Responsable**: 🛡️ **Salesforce Admin / Architect**

---

## 🔍 Parte 1: Implementación Original (As-Is)

*La siguiente sección documenta los pasos que se ejecutaron originalmente en la org. No borrar para mantener el historial de decisiones (especialmente el Escudo Anti-Duplicados).*

### 🎯 Objetivo Original
Relacionar "Alumnos" con "Materias" mediante un objeto intermedio. En el Sprint 2, este objeto se convierte en el núcleo de la migración de 7,500 registros, incorporando un **Escudo Anti-Duplicados**.

### 🛠️ Procedimiento Original

#### Paso 1: Atributos del Objeto (Sprint 1 Baseline)
1.  **Object Manager** > **Inscripcion__c**.
2.  **Record Name**: `ID Inscripción` (Auto Number: `INS-{000000}`).
3.  **Optional Features**: Marcar ☑️ **Allow Reports** (Permitir informes).
4.  **Relationships**: Master-Detail hacia **Alumno** (Contact) y **Materia**.

#### Paso 2: [NUEVO S2] Escudo Anti-Duplicados (ID Importación)
*Este campo es la clave maestra para evitar errores en la carga masiva.*
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Text**. **Field Label**: `ID de Importación`. **Field Name**: `ID_Importacion`.
3.  **Length**: `50`.
4.  ☑️ **Unique**: **Case Insensitive**. (Bloquea físicamente la duplicidad).
5.  ☑️ **External ID**: **SÍ**. (Permite que las Evaluaciones se vinculen a esta Inscripción).
6.  **Save**.

#### Paso 3: Campos Operativos (Originales)
- **Ciclo**: Picklist (2024-1, 2024-2, etc.).
- **Turno**: Picklist (Mañana, Tarde, Noche).
- **Estado**: Picklist (Cursando, Aprobado, Reprobado).
- **Carrera (F)**: Fórmula (Texto) -> `Materia__r.Carrera__r.Name`.
- **Año Lectivo**: Campo utilizado en la migración histórica para auditoría.

#### Paso 4: Automatización de Asistencia
- **Clases Esperadas**: Fórmula que calcula el target semestral (Horas/2 * 16).
- **% Asistencia**: Fórmula (`Clases_Presentes__c / Clases_Esperadas__c`).
- **Condición Académica**: Fórmula que marca "Libre" si la asistencia es < 75%.

---

## 🛠️ Parte 2: Refactorización y Mejoras (To-Be)

*Basándonos en la auditoría técnica consolidada, el objeto Inscripción es el corazón del sistema. Identificamos que faltan campos de control operativo y que las reglas de negocio (Data Quality) deben aplicarse a nivel de Validación, no solo mediante filtros.*

### 🚨 Diagnóstico de Arquitectura
El objeto tiene excelentes métricas de asistencia, pero carece de campos de auditoría temporal (Cuándo se inscribió) y de reglas estrictas. Además, el campo `Alumno__c` debe apuntar inequívocamente al objeto estándar `Contact` (y opcionalmente ser filtrado por el Record Type 'Alumno').

### Paso 1: Corrección y Creación de Campos Faltantes
Modifica o añade los siguientes campos para alinear el objeto con la realidad operativa de la universidad:

1.  **Fecha Oficial de Inscripción (Nuevo):**
    *   Tipo: **Date/Time**. Name: `Fecha_de_Inscripcion__c`.
    *   *Propósito:* Auditoría (saber si se inscribió a tiempo o fuera de término).
2.  **Tipo de Inscripción (Nuevo):**
    *   Tipo: **Picklist**. Name: `Tipo_Inscripcion__c`.
    *   Valores: `Regular`, `Oyente`, `Equivalencia`.
3.  **Observaciones (Nuevo):**
    *   Tipo: **Text Area**. Name: `Observaciones__c`.
4.  **Limpieza de Campos (Eliminación):**
    *   Revisar si "Año Lectivo" y "Turno" siguen siendo necesarios a nivel Inscripción, ya que el Turno suele ser un atributo de la Materia/Comisión. Mantener "Ciclo" (Ej: 2024-1).

### Paso 2: Implementación de Reglas de Validación (Crucial)
Implementa estas tres reglas maestras descubiertas en la auditoría. Son obligatorias para garantizar la calidad de la base de datos:

1.  **Regla 1: Coherencia Carrera-Materia (LuminaRT)**
    *   **Rule Name**: `Coherencia_Carrera_Materia`
    *   **Fórmula**: `Alumno__r.Carrera__c <> Materia__r.Carrera__c`
    *   **Mensaje**: "Error: La materia seleccionada no pertenece a la carrera en la que está matriculado el alumno."
2.  **Regla 2: Alumno Activo (LuminaRT)**
    *   **Rule Name**: `Alumno_Activo_Para_Inscribir`
    *   **Fórmula**: `Alumno__r.Activo__c = FALSE`
    *   **Mensaje**: "El alumno debe estar en estado Activo para inscribirse. Verifique su situación en Admisiones."
3.  **Regla 3: Materia Obligatoria (LuminaFinal)**
    *   **Rule Name**: `Materia_Obligatoria_Ciclo_Univ`
    *   **Fórmula**: `ISBLANK(Materia__c)`
    *   **Mensaje**: "Debe seleccionar obligatoriamente una Materia para asentar la inscripción."

### Paso 3: Seguridad y Visibilidad (Zero Trust)
Debido a que este es un objeto transaccional clave que vincula alumnos con materias, heredará la seguridad estricta:

1.  Ve a **Setup** > **Sharing Settings**.
2.  Verifica que el **Default Internal Access** de **Inscripcion__c** sea **Controlled by Parent**.
    *   *(Esto significa que si el Profesor no tiene acceso a la Materia, tampoco verá sus inscripciones).*

---

## ✅ Verificación de Éxito de Refactorización
1.  Intenta inscribir a un Alumno (cuya carrera sea "Abogacía") en una Materia perteneciente a la carrera de "Ingeniería". 
    *   El sistema **debe bloquearte** gracias a la regla `Coherencia_Carrera_Materia`.
2.  Desmarca la casilla `Activo__c` de un Alumno e intenta crearle una inscripción.
    *   El sistema **debe bloquearte** exigiendo que el alumno esté activo.
3.  Verifica que el layout incluya los nuevos campos de `Fecha_de_Inscripcion__c` y `Tipo_Inscripcion__c`.

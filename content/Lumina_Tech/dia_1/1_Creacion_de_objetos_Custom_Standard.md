# 📝 Tarea: Creación de objetos Custom - Standard

**Rol Responsable**: 🛡️ **Salesforce Admin**
**Sprint**: 1 (Fundamentos)
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../Gestor_de_Versiones/03-Salesforce_Admin.md)

## Bitácora de Implementación (Admin)

Como Admin, mi objetivo es traducir el modelo de datos diseñado en la "nube" de Salesforce. Basado en el requerimiento de "Estructura Académica", he identificado los siguientes objetos.

### 1. Objetos Estándar (Reutilización)
Analicé si podíamos usar objetos estándar, pero:
*   *Contact*: Se usará para Profesores y Admin (Staff).
    *   **Trazabilidad**: [REQ-SEC-001] (Distinción de perfiles). No mezclamos Alumnos aquí por ahora.

### 2. Objetos Personalizados (Nuevos)
He creado los siguientes objetos en la Org para responder a **[REQ-DATA-001] Entidades Core**:

*   **Carrera** (`Carrera__c`):
    *   *Descripción*: Representa la oferta académica (ej. "Ingeniería en Sistemas").
    *   *Justificación*: Necesitamos agrupar materias y alumnos bajo un paraguas académico.

*   **Materia** (`Materia__c`):
    *   *Descripción*: La unidad curricular (ej. "Matemática I").
    *   *Decisión de Diseño*: Siguiendo ADR-001 (Consultant), crearemos registros duplicados si se comparten entre carreras para simplificar [REQ-SEC-002] (Privacidad Cruzada).

*   **Alumno** (`Alumno__c`):
    *   *Descripción*: El estudiante matriculado.
    *   *Nota*: Objeto separado para facilitar [REQ-DATA-002] (M:N limpio) y [REQ-QUAL-003] (Identidad obligatoria y única).

---
** Estado**: ✅ Objetos creados vacíos.

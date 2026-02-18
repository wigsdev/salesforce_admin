# 11-Ambiente_DEV.md - Bitácora de Desarrollo
**Org ID**: `00Dxxxxxxxxxxxx` (Lumina Dev)
**Login**: `admin@lumina.dev.com`
**Estado**: 🟢 Activo

---

## 🛠️ Configuración Inicial (Setup)

### Datos de la Org
*   **Edición**: Developer Edition.
*   **Dominio**: `lumina-tech-university-dev-ed`
*   **Timezone**: GMT-5 (Perú/Colombia).
*   **Currency**: USD (Multicurrency desactivado).

### Usuarios de Desarrollo
1.  **System Admin**: WIGUSA (Arquitecto).
2.  **Integration User**: Usuario API (para Trello/Jira).

---

## 📝 Inventario de Cambios (Sprint 1)

Registro de metadata creada directamente en este ambiente.

### Objetos Custom
*   `Carrera__c` (Master)
*   `Materia__c` (Master-Detail de Carrera)
*   `Alumno__c` (Transaccional)
*   `Inscripcion__c` (Junction)
*   `Nota__c` (Lookup a Inscripción)
*   `Asistencia__c` (Lookup a Inscripción)

### Automatización
*   **Validation Rules**: 6 activas (ver Guía 09).
*   **Flows**: 2 activos (`Nota: Calcular Nota Final`, `Nota: Recalcular al Borrar`).
*   **Approval Processes**: 0.

---

## 🚧 Deuda Técnica Conocida
*   Faltan Description en algunos campos creados el Día 1 (mejora para Sprint 2).

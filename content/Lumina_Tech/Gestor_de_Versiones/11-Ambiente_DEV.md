# 11-Ambiente_DEV.md - Bitácora de Desarrollo
**Org ID**: `00Dxxxxxxxxxxxx` (Lumina Dev)
**Login**: `admin@lumina.dev.com`
**Estado**: 🟢 Activo

---

## 🛠️ Configuración Inicial (Setup)

### Datos de la Org
*   **Edición**: Developer Edition.
*   **Dominio**: `lumina-university-dev-ed`
*   **Timezone**: GMT-3 (Argentina).
*   **Currency**: USD (Multicurrency desactivado).

### Usuarios de Desarrollo
1.  **System Admin**: WIGUSA (Arquitecto).
2.  **Integration User**: Usuario API (para Trello/Jira).

---

## 📝 Inventario de Cambios (Sprint 1)

Registro de metadata creada directamente en este ambiente.

### Objetos Custom
*   `Carrera__c` (Master)
*   `Materia__c` (Master)
*   `Alumno__c` (Transaccional)
*   `Inscripcion__c` (Junction)
*   `Examen__c` (Detail)

### Automatización
*   **Validation Rules**: 3 activas.
*   **Flows**: 0 (Sprint 1 es Config pura).
*   **Approval Processes**: 0.

---

## 🚧 Deuda Técnica Conocida
*   Los nombres de las pestañas están en inglés ("Students" vs "Alumnos"). Se debe corregir en la traducción de la Tab.
*   Faltan Description en los campos creados el Día 1.

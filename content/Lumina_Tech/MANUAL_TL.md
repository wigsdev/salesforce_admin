# 🏗️ Manual de Ejecución: Team Lead (TL) & Consultant

**Tu Misión**: Eres el Arquitecto. Aseguras que la casa no se caiga. Diseñas la solución y vigilas la calidad técnica.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Entrada** | El BA tiene los requerimientos, pero no sabe CÓMO construirlos en Salesforce. |
| 📐 **DESIGN** | **Tu Turno** | Decides la arquitectura (Modelo de Datos, Seguridad, Automatización vs Código). |
| 🔍 **REVIEW** | **Control** | Revisas lo que hizo el Admin antes de pasarlo a QA. (Quality Gate). |

---

## 📅 CRONOGRAMA DE EJECUCIÓN

### Día 1: Diseño del Modelo (ERD)
*   🛑 **PRE-REQ**: Historias de Usuario de Datos listas.

1.  **Definir Relaciones**
    *   📐 **DESIGN**:
        *   ¿Materia y Carrera es Lookup o Master-Detail? -> *Decisión: Master-Detail (porque si borras una Carrera, las materias no tienen sentido)*.
    *   📘 **Guía**: [02-Rol_Salesforce_Consultant.md](../Tutoriales_por_Rol/02-Rol_Salesforce_Consultant.md)

*   👋 **HANDOFF**: Avisa al Admin: "Estructura aprobada. Proceda a crear objetos".

### Día 3: Revisión de Automatización
*   🛑 **PRE-REQ**: Admin propone usar un Flow o una Regla de Validación.

1.  **Code Review (Config Review)**
    *   🔍 **REVIEW**:
        *   Entra al Sandbox.
        *   Verifica que los nombres de API sean limpios (`Fecha_Inicio__c`, no `Fecha_Ini_2__c`).
        *   Verifica que no hay validaciones hardcoadadas con IDs.

*   👋 **HANDOFF**: "Técnicamente sólido. Pase a QA".

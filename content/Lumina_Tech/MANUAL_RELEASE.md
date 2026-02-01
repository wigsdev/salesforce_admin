# 🚀 Manual de Ejecución: Release Manager

**Tu Misión**: Eres el Controlador Aéreo. Aseguras que lo que sale a Producción esté versionado, aprobado y no explote.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Entrada** | Todas las historias de usuario de un Día/Sprint están en la columna "Aprobado" (QA Done). |
| 📦 **DEPLOY** | **Tu Turno** | Registras la versión en el historial y ejecutas el despliegue (Change Set / Metadata API). |
| 👋 **HANDOFF** | **Al terminar** | Notificas al equipo: "Versión v.X.X Disponible en Producción". Cierras el Sprint. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN (Sprint 1)

### Día 1: Versión Alfa 0.1 (Estructura)
*   🛑 **PRE-REQ**: Admin & QA confirman que los Objetos `Carrera` y `Materia` existen y funcionan.

1.  **Registrar Versión**
    *   📦 **DEPLOY**: Abre el documento "Gestor de Versiones".
    *   **Acción**:
        *   Versión: `0.1.0`
        *   Cambios: "Objetos iniciales creados".
        *   Responsable: Tu nombre.
    *   📘 **Guía**: [04-Rol_Release_Manager.md](../Tutoriales_por_Rol/04-Rol_Release_Manager.md)

2.  **Despliegue a Test/Staging**
    *   📦 **DEPLOY**: Mueve los cambios del Sandbox Developer al Sandbox QA (si aplica) o marca el hito.

*   👋 **HANDOFF**: "Baseline v0.1.0 establecida".

---

### Día 4: Release Candidate 1.0 (Seguridad)
*   🛑 **PRE-REQ**: Todos los hitos anteriores (UI, Validaciones, Seguridad) están completos.

1.  **Auditoría Final**
    *   📦 **DEPLOY**: Verifica que no haya "To Do" pendientes en Trello.
    *   **Acción**: Ejecuta todos los tests una última vez (o pide al QA una regresión rápida).

2.  **Cierre de Versión v1.0**
    *   📦 **DEPLOY**:
        *   Versión: `1.0.0` (MVP Sprint 1).
        *   Cambios: "Sprint 1 Completo - Lumina Tech Core".
        *   Acción: Congelar código en Git (Tag `v1.0.0`).

*   👋 **HANDOFF**: "Sprint 1 Finalizado. ¡A celebrar!".

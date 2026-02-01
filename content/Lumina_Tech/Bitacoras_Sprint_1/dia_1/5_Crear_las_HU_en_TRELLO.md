# 📝 Tarea: Crear las HU en TRELLO

**Rol Responsable**: 👑 **Product Owner** (con apoyo del BA)
**Herramienta**: Trello / Jira (Simulado)
**Destino en Gestor**: [`01-Business_Analyst.md`](../../Gestor_de_Versiones/01-Business_Analyst.md) (Backlog)

## Backlog Grooming (Día 1)

He formalizado las Historias de Usuario para que el equipo técnico empiece a construir. Estas tarjetas ya están en la columna **"Sprint Backlog"**.

### Tarjetas Creadas (Detalle)

#### 🏷️ [HU-001] Gestión de Inscripciones
*   **Trazabilidad**: Responde a **[REQ-DATA-002] Historial Académico**.
*   **Descripción**: "Como Director, quiero inscribir alumnos a materias para trackear su avance."
*   **Checklist Technical (Consultant accepted)**:
    *   [ ] Objeto `Inscripcion__c` creado.
    *   [ ] Master-Detail a Alumno y Materia.
    *   [ ] Tab visible solo para Directores y Admin.

#### 🏷️ [HU-002] Unicidad de Alumnos
*   **Trazabilidad**: Responde a **[REQ-QUAL-003] Identidad Obligatoria**.
*   **Descripción**: "Como Sistema, quiero impedir alumnos duplicados por DNI."
*   **Checklist Technical**:
    *   [ ] Campo `DNI__c` marcado como Unique.
    *   [ ] Campo `DNI__c` marcado como External ID.

#### 🏷️ [HU-003] Integridad de Notas
*   **Trazabilidad**: Responde a **[REQ-QUAL-002] Consistencia de Notas**.
*   **Descripción**: "Como Rectoría, quiero evitar notas inválidas (11 o -1)."
*   **Checklist Technical**:
    *   [ ] Campo `Nota__c` es Number(2,2).
    *   [ ] Validation Rule `Nota_0_a_10` activa.
    *   [ ] Mensaje de error amigable.

---
**Status del Backlog**: Listo para desarrollo. Trazabilidad actualizada a los nuevos IDs requeridos.

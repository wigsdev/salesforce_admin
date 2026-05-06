# 📝 Tarea: Crear las HU en TRELLO

**Rol Responsable**: 👑 **Product Owner** (con apoyo del BA)
**Herramienta**: Trello / Jira (Simulado)
**Destino en Gestor**: [`01-Business_Analyst.md`](../../Gestor_de_Versiones/01-Business_Analyst.md) (Backlog)

## Backlog Grooming (Día 1)

He formalizado las **12 Historias de Usuario** para que el equipo técnico empiece a construir. Estas tarjetas ya están en la columna **"Sprint Backlog"**.

### Tarjetas Creadas (Detalle de Muestra)

#### 🏷️ [HU-001] Gestión de Inscripciones
*   **Trazabilidad**: Responde a **[REQ-DATA-002] Historial Académico**.
*   **Descripción**: "Como Director, quiero inscribir alumnos a materias para trackear su avance."
*   **Checklist Technical (Consultant accepted)**:
    *   [ ] Objeto `Enrollment__c` creado.
    *   [ ] Master-Detail a `Student__c` y `Subject__c`.
    *   [ ] Tab visible solo para Directores y Admin.

#### 🏷️ [HU-002] Unicidad de Alumnos
*   **Trazabilidad**: Responde a **[REQ-QUAL-003] Identidad Obligatoria**.
*   **Descripción**: "Como Sistema, quiero impedir alumnos duplicados por DNI."
*   **Checklist Technical**:
    *   [ ] Campo `National_ID__c` marcado como Unique y External ID.
    *   [ ] Record Name configurado como **Auto-Number** `A-{YYYY}-{0000}`.

#### 🏷️ [HU-003] Integridad de Notas
*   **Trazabilidad**: Responde a **[REQ-QUAL-002] Consistencia de Notas**.
*   **Descripción**: "Como Rectoría, quiero evitar notas inválidas (11 o -1)."
*   **Checklist Technical**:
    *   [ ] Campo `Final_Grade__c` es Number(4,2).
    *   [ ] Validation Rule `Grade_Range_1_10` activa.
    *   [ ] Mensaje de error amigable (En Inglés).

---
**Status del Backlog**: Listo para desarrollo. Trazabilidad actualizada a los nuevos IDs requeridos.

# 📋 Crear las HU en TRELLO

**Rol Responsable**: 👑 **Product Owner** (PO & BA Persona)
**Destino en Gestor**: [`01-Business_Analyst.md`](../../Gestor_de_Versiones/01-Business_Analyst.md)
**Justificación**: "Traducir necesidades de negocio (Seguridad/Roles) en historias ejecutables que aporten valor y sean auditables."

## 🛡️ Epica: Seguridad Corporativa ("Trust is our #1 Value")

Estas historias aseguran que Lumina Tech cumpla con los estándares de seguridad de datos (GDPR) y prevenga fraudes académicos.

### User Stories Refinadas (Ready for Dev)

#### 🏷️ [HU-009] Matriz de Visibilidad (Privacidad)
*   **Prioridad**: Alta (Compliance).
*   **As a** (Como): Responsable de Privacidad de Datos (DPO).
*   **I Want** (Quiero): Que los legajos de los alumnos sean privados por defecto.
*   **So That** (Para): Garantizar que solo los profesores asignados puedan ver los datos de sus estudiantes, cumpliendo la normativa.
*   **✅ Acceptance Criteria**:
    - [ ] **Negative Test**: Un profesor logueado NO puede buscar ni ver el registro de un alumno que no está en su materia.
    - [ ] **Positive Test**: Al inscribir al alumno en "Matemática", el profesor obtiene acceso de lectura automático.

#### 🏷️ [HU-010] Acceso Seguro (MFA)
*   **Prioridad**: Crítica (Security).
*   **As a** (Como): Gerente de Seguridad Informática (CISO).
*   **I Want** (Quiero): Reforzar el login con un segundo factor de autenticación.
*   **So That** (Para): Prevenir accesos no autorizados incluso si una contraseña es comprometida.
*   **✅ Acceptance Criteria**:
    - [ ] Al loguearse, Salesforce solicita el código de la App Authenticator.
    - [ ] El permiso está centralizado en un Permission Set (`Lumina_MFA`).

#### 🏷️ [HU-011] Segregación de Funciones (SoD)
*   **Prioridad**: Media (Process).
*   **As a** (Como): Auditor Académico.
*   **I Want** (Quiero): Separar quien inscribe (Bedelía) de quien califica (Profesor).
*   **So That** (Para): Evitar conflictos de interés y asegurar la integridad de las notas finales.
*   **✅ Acceptance Criteria**:
    - [ ] **Bedelía**: Puede editar `Email`, `Dirección` del alumno, pero campo `Nota` está grisado (Read-Only).
    - [ ] **Profesor**: Puede editar campo `Nota`, pero no puede cambiar el `DNI` del alumno.

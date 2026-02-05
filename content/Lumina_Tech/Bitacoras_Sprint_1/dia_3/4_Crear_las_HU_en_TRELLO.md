# 📋 Crear las HU en TRELLO

**Rol Responsable**: 👑 **Product Owner**
**Destino en Gestor**: [`01-Business_Analyst.md`](../../Gestor_de_Versiones/01-Business_Analyst.md) (Backlog Update)

## Backlog Grooming (Día 3: Automatización)

Hemos tomado las historias relevantes del backlog maestro y las hemos preparado para el sprint técnico de hoy.

### Tarjetas para Copiar (Trello)

#### 🏷️ [HU-007] Validación de Contactos (Email)
*   **Trazabilidad**: Responde a **HU-007**.
*   **Descripción**: "Como Equipo de Admisión, **Quiero** que el sistema valide automáticamente la sintaxis del correo electrónico, **Para** asegurar que las notificaciones lleguen a los alumnos y no reboten."
*   **Criterios de Aceptación**:
    - [ ] **Syntax Check**: El campo `Email__c` utiliza Regex para validar `.edu`.
    - [ ] **Negative Test**: Ingresar "gmail.com" bloquea el guardado.
    - [ ] **Error UI**: El mensaje de error es claro ("Invalid Email").

#### 🏷️ [HU-008] Integridad Numérica
*   **Trazabilidad**: Responde a **HU-008**.
*   **Descripción**: "Como Rectoría, **Quiero** que el sistema rechace automáticamente cualquier nota fuera del rango 1-10, **Para** evitar inconsistencias estadísticas."
*   **Criterios de Aceptación**:
    - [ ] **Validation**: Ingresar `0` o `10` es válido.
    - [ ] **Error**: Ingresar `10.5` muestra el error: *"Invalid Grade"*.

#### 🏷️ [HU-009] Control de Asistencias (Automatización)
*   **Trazabilidad**: Responde a **HU-009**.
*   **Descripción**: "Como Preceptor, quiero identificar alumnos Libres (<75% asistencia) automáticamente."
*   **Criterios de Aceptación**:
    - [ ] Campos `Total_Classes__c` y `Classes_Attended__c` creados.
    - [ ] Fórmula `Attendance_Percentage__c` calcula % correctamente.
    - [ ] Fórmula `Academic_Condition__c` muestra "Libre" si es < 75%.

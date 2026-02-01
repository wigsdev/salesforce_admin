# 📋 Crear las HU en TRELLO

**Rol Responsable**: 👑 **Product Owner**
**Destino en Gestor**: [`01-Business_Analyst.md`](../../Gestor_de_Versiones/01-Business_Analyst.md) (Backlog Update)

## Backlog Grooming (Día 3: Automatización)

Hemos tomado las historias relevantes del backlog maestro y las hemos preparado para el sprint técnico de hoy.

### Tarjetas para Copiar (Trello)

#### 🏷️ [HU-007] Comprobación de Formato de Email
*   **Trazabilidad**: Responde a **HU-005** del Master Backlog.
*   **Descripción**: "Como Equipo de Admisión, **Quiero** que el sistema valide automáticamente la sintaxis del correo electrónico, **Para** asegurar que las notificaciones lleguen a los alumnos y no reboten."
*   **Criterios de Aceptación**:
    - [ ] **Syntax Check**: El campo `Email__c` utiliza el tipo de dato estándar "Email".
    - [ ] **Negative Test**: Ingresar "nombre,apellido" (coma en vez de punto) o "sin_arroba" bloquea el guardado.
    - [ ] **Error UI**: El mensaje de error es claro para el usuario ("Formato de correo inválido").

#### 🏷️ [HU-008] Integridad de Calificaciones
*   **Trazabilidad**: Responde a **HU-006** del Master Backlog.
*   **Descripción**: "Como Rectoría, **Quiero** que el sistema rechace automáticamente cualquier nota fuera del rango 1-10, **Para** evitar inconsistencias estadísticas."
*   **Criterios de Aceptación**:
    - [ ] **Validation**: Ingresar `0` o `10` es válido.
    - [ ] **Error**: Ingresar `10.5` o `-1` muestra el error: *"La nota debe estar entre 0 y 10"*.

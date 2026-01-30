# 👥 Configuración de Permission Sets Groups

**Rol Responsable**: 🛡️ **Salesforce Admin** (Delegated Admin Persona)
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../Gestor_de_Versiones/03-Salesforce_Admin.md)
**Justificación**: "Simplificar la gestión de usuarios (Onboarding/Offboarding). Asignar 1 Grupo es más rápido y seguro que asignar 5 Sets manuales."

## 🧩 Estrategia de Agrupación (Personas)

Un **Permission Set Group (PSG)** representa una "Persona" en la organización. Combina capacidades técnicas (Sets) para formar un Rol de Negocio funcional.

### Definición de Grupos (PSG)

#### 1. PSG: `Persona_Profesor_Standard`
*   **Concepto**: "Todo lo que necesita un docente nuevo para empezar a enseñar el Día 1."
*   **Composición (Bundling)**:
    1.  `Lumina_MFA_Authorization` (Seguridad obligatoria).
    2.  `Gestion_Calificaciones_Docente` (Funcionalidad core).
    3.  `Chatter_User` (Colaboración - Standard).
*   **Ventaja**: Si mañana agregamos una App de "Asistencia", solo actualizamos el PSG y los 50 profesores lo heredan automáticamente.

#### 2. PSG: `Persona_Administrativo_Bedelia`
*   **Concepto**: "Gestor de trámites y matrículas."
*   **Composición**:
    1.  `Lumina_MFA_Authorization`.
    2.  `Operador_Bedelia`.
    3.  `Export_Reports` (System Permission para reportes básicos).
*   **Restricción**: Este grupo **EXCLUYE** explícitamente permisos de borrado (`Delete`).

### ⚙️ Mantenimiento (Muting Permission Sets)
*   **Best Practice**: Si un sub-set otorga "Delete" por error, usaremos un **Muting Permission Set** dentro del grupo para bloquear esa acción sin modificar el set original reutilizable.

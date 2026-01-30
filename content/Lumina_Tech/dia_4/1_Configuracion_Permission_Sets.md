# 🛡️ Configuración de Permission Sets

**Rol Responsable**: 🛡️ **Salesforce Admin** (System Architect Persona)
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../Gestor_de_Versiones/03-Salesforce_Admin.md)
**Justificación**: "Evitar el 'Profile Explosion'. Usamos Permission Sets para extender funcionalidades específicas (Atomicidad)."

## 🧠 Análisis de Seguridad (Identity & Access Management)

En el modelo de seguridad moderno de Salesforce, los **Perfiles** deben ser mínimos (Base Profiles) y los permisos deben otorgarse mediante **Permission Sets** (Capacidades). Esto facilita la auditoría y el mantenimiento.

### 🔧 Especificación Técnica (Permission Sets)

#### 1. Set: `Lumina_MFA_Authorization`
*   **Tipo**: System Permission.
*   **Contexto de Negocio**: Cumplimiento normativo (Compliance). Salesforce exige MFA contractual desde 2022.
*   **Permiso Crítico**: `Multi-Factor Authentication for User Interface Logins`.
*   **Asignación**: Mandatoria para **TODOS** los usuarios internos (Admin, Profesores, Bedelía).

#### 2. Set: `Gestion_Calificaciones_Docente`
*   **Tipo**: Object & Field Permission.
*   **Contexto de Negocio**: Delegar la capacidad de "Evaluar" sin dar poderes administrativos.
*   **Configuración**:
    *   **Objeto Examen (`Examen__c`)**: `Read`, `Create`, `Edit`.
    *   **Campo Nota (`Nota__c`)**: `Edit` Access.
    *   **Objeto Inscripción**: `Read`. (Para ver a quién calificar).

#### 3. Set: `Operador_Bedelia`
*   **Tipo**: Object Permission.
*   **Contexto de Negocio**: Personal administrativo que gestiona el ciclo de vida del alumno pero no evalúa.
*   **Configuración**:
    *   **Objeto Alumno (`Alumno__c`)**: `Read`, `Create`, `Edit`.
    *   **Objeto Inscripción (`Inscripcion__c`)**: `Read`, `Create`, `Edit`. (Inscribe alumnos).
    *   **Objeto Examen**: `Read` ONLY. (Audita notas, no las cambia).

# 👁️ Visibilidad de Objetos y Campos

**Rol Responsable**: 🏗️ **Salesforce Consultant** (Security Specialist Persona)
**Destino en Gestor**: [`02-Salesforce_Consultant.md`](../../Gestor_de_Versiones/02-Salesforce_Consultant.md)
**Justificación**: "Principio de Menor Privilegio (PoLP). Todo está prohibido a menos que se permita explícitamente."

## 1. Nivel Macro: Organization-Wide Defaults (OWD)
El "piso" de la seguridad. Define qué ven los usuarios que NO son dueños del registro.

*   **Alumno (`Alumno__c`)**: 🔒 **Private**.
    *   *Justificación*: Datos PII (Información Personal Identificable). Un profesor de "Matemáticas" no tiene por qué ver los datos de contacto de un alumno de "Derecho" si no está inscrito.
*   **Inscripción (`Inscripcion__c`)**: 🔗 **Controlled by Parent**.
    *   *Justificación*: Al ser Junction, su visibilidad depende de si tienes acceso al Alumno y a la Materia.
*   **Materia (`Materia__c`)**: 🌐 **Public Read Only**.
    *   *Justificación*: El catálogo académico es información pública interna. Todos deben poder buscar materias, pero solo Bedelía las crea/edita.

## 2. Nivel Micro: Field Level Security (FLS)
La "última milla" de la seguridad. Oculta datos sensibles incluso si tienes acceso al registro.

### Matriz de Seguridad de Campo (FLS Matrix)

| Campo | Rol: Profesor | Rol: Administrativo | Datos Sensitive? |
| :--- | :--- | :--- | :--- |
| **Examen.Nota__c** | ✅ Read / Edit | 👁️ **Read-Only** | Sí (Integridad Académica) |
| **Alumno.DNI__c** | 👁️ Read-Only | ✅ Read / Edit | Sí (Identidad Única) |
| **Alumno.Email__c** | ✅ Read / Edit | ✅ Read / Edit | No (Comunicación) |

*   **Nota Técnica**: FLS se aplicará vía Permission Sets, dejando el Perfil "Minimum Access - Salesforce" limpio.

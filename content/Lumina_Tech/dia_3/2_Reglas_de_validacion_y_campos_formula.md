# 🛡️ Reglas de validación y campos formula

**Rol Responsable**: 🛡️ **Salesforce Admin** / 🏗️ **Salesforce Consultant**
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../Gestor_de_Versiones/03-Salesforce_Admin.md) (Lógica de Negocio)

## Automatización y Calidad

Implementamos lógica "dura" en la base de datos para prevenir errores humanos.

### 1. Reglas de Validación (Validation Rules)

#### VR-001: Rango de Notas Válido
*   **Objeto**: `Inscripcion__c` y `Examen__c`
*   **Problema**: Profesores cargando notas como "15" o "-1".
*   **Fórmula de Error**:
    ```
    OR(
      Nota__c < 0,
      Nota__c > 10
    )
    ```
*   **Mensaje**: *"La nota debe estar entre 0.00 y 10.00."*

#### VR-002: Email Institucional Estricto
*   **Objeto**: `Alumno__c`
*   **Problema**: Errores de dedo ("gmail,com") o dominios no educativos.
*   **Fórmula de Error**:
    ```
    NOT(REGEX(Email__c, "[a-zA-Z0-9._-]+@[a-z]+\\.edu"))
    ```
*   **Mensaje**: *"Formato de correo inválido. Debe ser un dominio educativo (.edu)."*

### 2. Campos Fórmula (Cross-Object)

#### F-001: Nombre Completo de Materia (en Inscripción)
*   **Label**: `Materia_Display__c`
*   **Type**: Text
*   **Fórmula**: `Materia__r.Name & " - " & Materia__r.Carrera__r.Name`
*   **Uso**: Permite ver "Matemática - Ingeniería" en reportes sin ir al registro padre.

# 🛡️ Reglas de validación y campos formula

**Rol Responsable**: 🛡️ **Salesforce Admin** / 🏗️ **Salesforce Consultant**
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../../Gestor_de_Versiones/03-Salesforce_Admin.md) (Lógica de Negocio)

## Automatización y Calidad

Implementamos lógica "dura" en la base de datos para prevenir errores humanos.

### 1. Reglas de Validación (Validation Rules)

#### VR-001: Rango de Notas Válido
*   **Objeto**: `Enrollment__c`
*   **Problema**: Profesores cargando notas como "15" o "-1".
*   **Fórmula de Error**:
    ```
    OR(
      Final_Grade__c < 0,
      Final_Grade__c > 10
    )
    ```
*   **Mensaje**: *"Invalid Grade. Must be between 0.00 and 10.00."*

#### VR-002: Email Institucional Estricto
*   **Objeto**: `Student__c`
*   **Problema**: Errores de dedo ("gmail,com") o dominios no educativos.
*   **Fórmula de Error**:
    ```
    NOT(REGEX(Email__c, "[a-zA-Z0-9._-]+@[a-z]+\\.edu"))
    ```
*   **Mensaje**: *"Invalid Email Format. Must be .edu domain."*

### 2. Campos Fórmula (Cross-Object)

#### F-001: Subject Display Name
*   **Label**: `Subject_Display__c`
*   **Type**: Text
*   **Fórmula**: `Subject__r.Name & " - " & Subject__r.Career__r.Name`
*   **Uso**: Permite ver "Matemática - Ingeniería" en reportes sin ir al registro padre.

# 📝 Campos adicionales

**Rol Responsable**: 🛡️ **Salesforce Admin**
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../../Gestor_de_Versiones/03-Salesforce_Admin.md) (Diccionario de Datos)

## Configuración de Nuevos Campos (Schema Builder)

Durante el setup inicial, nos faltaron algunos campos para completar el modelo de datos robusto que requiere la Dra. Vance.

### Objeto: Enrollment (`Enrollment__c`)

1.  **Status**
    *   **Label**: `Status`
    *   **API Name**: `Status__c`
    *   **Type**: Picklist
    *   **Values**: `Enrolled` (Default), `Passed`, `Failed`.
    *   *Propósito*: Permite filtrar alumnos activos vs históricos.

2.  **Final Grade**
    *   **Label**: `Final Grade`
    *   **API Name**: `Final_Grade__c`
    *   **Type**: Number(4,2)
    *   **Help Text**: "Promedio calculado de los exámenes rendidos."

# 📝 Campos adicionales

**Rol Responsable**: 🛡️ **Salesforce Admin**
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../Gestor_de_Versiones/03-Salesforce_Admin.md) (Diccionario de Datos)

## Configuración de Nuevos Campos (Schema Builder)

Durante el setup inicial, nos faltaron algunos campos para completar el modelo de datos robusto que requiere la Dra. Vance.

### Objeto: Inscripción (`Inscripcion__c`)

1.  **Estado de Cursada**
    *   **Label**: `Estado`
    *   **API Name**: `Estado__c`
    *   **Type**: Picklist
    *   **Values**: `Cursando` (Default), `Aprobado`, `Libre`, `Recursando`.
    *   *Propósito*: Permite filtrar alumnos activos vs históricos.

2.  **Nota Final**
    *   **Label**: `Nota Final`
    *   **API Name**: `Nota_Final__c`
    *   **Type**: Number(2,2)
    *   **Help Text**: "Promedio calculado de los exámenes rendidos."

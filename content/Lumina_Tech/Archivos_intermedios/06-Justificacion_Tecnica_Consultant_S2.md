# Justificación Técnica de Arquitectura - Sprint 2

## Decisiones Críticas de Diseño

### 1. Relación Master-Detail en Materia
Se justifica mantener la relación **Master-Detail** hacia Carrera para habilitar campos de resumen (Roll-up Summary) en la Carrera, permitiendo saber el total de créditos activos sin usar Apex. Se habilitó **Allow Reparenting** para facilitar la carga masiva.

### 2. Uso de Contact sobre Persona__c
Se elige `Contact` para:
- Aprovechar reglas de duplicados nativas de Salesforce.
- Facilitar la integración futura con Marketing Cloud / Gmail.
- Reducir el consumo de almacenamiento de datos personalizados (Custom Objects).

### 3. Estrategia de Identidad Compuesta
La creación del `ID_Importacion__c` en Inscripciones se justifica por la necesidad de referenciar cursadas específicas desde el objeto Evaluaciones (CSV-04). Al ser de tipo **Unique**, sirve de "Escudo" contra fallos humanos en la carga manual.

### 4. Gestión del Storage Limit (17.3 MB)
Se justifica la limpieza profunda de los CSVs originales (Deduplicación de 1,145 filas) para garantizar que el modelo de datos quepa en la infraestructura de la org Developer.

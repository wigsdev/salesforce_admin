# Análisis de Consolidación: Arquitectura G3 vs G6

Este documento analiza los gaps técnicos identificados al intentar unificar el entorno G6 (Desarrollo Base) con el Estándar de Oro (G3) durante el Sprint 2.

## Gaps Técnicos Identificados (Chat Audit)

### 1. Modelo de Identidad (Persona vs Contacto)
- **G6**: Utiliza el objeto custom `Persona__c`.
- **G3**: Exige el uso del objeto estándar `Contact` con Record Types.
- **Acción**: Refactorizar todas las relaciones para que apunten al objeto estándar `Contact` (Alumno).

### 2. Claves de Integridad (External IDs)
- **Problemática**: El entorno G6 carecía de campos de identidad unificados.
- **Acción**: Creación obligatoria de `Numero_Documento__c` (Contact) y `Abreviatura__c` (Carrera) marcados como **External ID** para permitir el Upsert masivo.

### 3. El Escudo Anti-Duplicados
- **Gap**: En G6 se registraban dobles inscripciones en el mismo ciclo.
- **Acción Sprint 2**: Implementación del campo `ID_Importacion__c` en Inscripción, concatenando `DNI-COD_MAT`.

## Plan de Mitigación de Capacidad
- El análisis de storage revela que G6 tiene un límite de **17.3 MB**.
- **Acción de Emergencia**: Deduplicación de 1,145 registros en el CSV 03 (`Inscripciones_CLEAN`) para optimizar cada KB de espacio.

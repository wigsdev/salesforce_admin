# Auditoría de Preguntas, Dudas y Propuestas - Sprint 2

## Registro de Sesiones Técnicas

### Preguntas del Administrador
- **P: ¿Podemos borrar el campo ID_Importacion tras la carga?**
  - **R**: Sí, es posible, pero se recomienda conservarlo (aunque oculto) para auditoría o futuras cargas delta. Se debe exportar el mapeo antes de borrarlo.
- **P: ¿El campo Anio_Lectivo es necesario?**
  - **R**: Es dato histórico. Se decidió mantenerlo para reportes de cohorte pero se omitirá si el storage llega al límite crítico.

### Dudas de Implementación
- **Typo en CSV**: Se detectó la columna `Inscripcion_ID_Imporado__c`. Se propuso corregir en Salesforce o mapear en Data Loader.
- **Lookup Filters**: Se detectó que los filtros de "Al día" bloquean la carga de alumnos históricos morosos. Se decidió desactivarlos temporalmente.

### Propuestas de Mejora
1. **Deduplicación Agresiva**: Procesar el CSV de Inscripciones para bajar de 7.5k a 6.3k registros. (EJECUTADO).
2. **Dashboard de Storage**: Crear reporte de uso de disco por objeto.

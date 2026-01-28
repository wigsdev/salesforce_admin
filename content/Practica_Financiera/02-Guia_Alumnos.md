# 🎓 Guía para los Alumnos (Rol Business Analyst & Consultor)

---

## Paso 1: El rol del Consultor (La Indagación)

Antes de escribir la historia en Trello, deben hacer preguntas para aclarar los requerimientos "crudos" del Gerente.

### Para el Req A (Aprobaciones):
- "¿Qué pasa si usted está de vacaciones, quién más puede aprobar?"
- "¿El 5% es para todos los productos o solo préstamos personales?"

### Para el Req B (Reportes):
- "¿Ese gráfico debe ser visible para todos o solo para la gerencia?"
- "¿Necesita ver el desglose por vendedor o solo el total?"

### Para el Req C (Automatización):
- "¿El aviso debe ser un email o una tarea en Salesforce?"
- "¿Cuántos días antes de la última cuota quiere que avisemos?"

---

## Paso 2: Redacción de Historias de Usuario (Formato Agile)

Deben trasladar el requerimiento a una tarjeta de Trello usando el formato estándar:

**Como** [Rol] **Quiero** [Acción/Funcionalidad] **Para** [Beneficio/Valor].

### Ejemplo de cómo deberían redactar el Requerimiento A:

**Título en Trello**: Proceso de Aprobación para Tasas Bajas.

**Descripción**:
- **Como**: Gerente de Finanzas.
- **Quiero**: Que el sistema bloquee el cierre de oportunidades con tasas menores al 5% y solicite una aprobación.
- **Para**: Evitar pérdidas por créditos mal negociados y controlar el riesgo.

**Criterios de Aceptación (Definition of Done)**:
- [ ] El vendedor no puede cambiar la etapa a "Cerrada Ganada" si la tasa < 5%.
- [ ] Al intentar cerrar, se dispara un proceso de aprobación.
- [ ] El Gerente recibe una notificación.
- [ ] Si el Gerente rechaza, la oportunidad vuelve a etapa "Negociación".

---

## Paso 3: Organización en Trello

Para simular el ciclo de vida de desarrollo, configuren su tablero de Trello con las siguientes columnas:

1. **Backlog** - Todas las historias de usuario identificadas
2. **Sprint Backlog** - HU seleccionadas para el sprint actual
3. **En Progreso** - Trabajo activo
4. **SF Desarrollo** - Configuración en Sandbox
5. **SF QA** - Pruebas internas
6. **Aprobación TL** - Revisión del Team Lead
7. **SF Producción** - Despliegue final
8. **Terminado** - Completado y validado

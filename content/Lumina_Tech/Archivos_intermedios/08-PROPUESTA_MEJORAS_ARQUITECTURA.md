# 🚀 Propuesta de Mejoras de Arquitectura (Gap Analysis)

**Rol Responsable**: 🏗️ **Salesforce Solution Architect**
**Fecha**: Día 4 (Cierre de Fase de Seguridad)
**Objetivo**: Elevar la implementación de "Operativa" a "Excelencia Académica" (100%).

---

## 🧠 Análisis de Situación (Solicitud vs. Implementación)

Hemos cubierto los requerimientos explícitos de la Dra. Vance (Seguridad, Datos, Estructura). Sin embargo, como Arquitectos, detectamos oportunidades para aportar valor agregado que no fue solicitado explícitamente pero que resolverá "dolores silenciosos".

### 1. Automatización de Procesos (Process Automation)
*   **Dolor Latente**: "La administración es un desastre de papeles".
*   **Solución Actual**: Base de datos estructurada.
*   **Mejora Propuesta (Flows)**:
    *   **Auto-Naming de Inscripciones**: Dejar de pedirle al usuario que nombre el registro. Usar un `Record-Triggered Flow` para nombrarlo automáticamente `[2024-MATEMATICA-JUANPEREZ]`.
    *   **Alerta de Riesgo Académico**: Si un alumno saca menos de 4 en un parcial, enviar email automático al Director de Carrera y al Alumno ofreciendo tutoría.
    *   **Cierre de Cursada**: Un `Schedule-Triggered Flow` que pase a "Histórico" las inscripciones al finalizar el cuatrimestre.

### 2. Inteligencia de Negocio (Analytics)
*   **Dolor Latente**: "Quiero saber el estado de mi operación".
*   **Solución Actual**: Datos guardados.
*   **Mejora Propuesta (Dashboards)**:
    *   **Tablero del Rector**:
        *   Gráfico: "Alumnos por Carrera" (Doughnut).
        *   Métrica: "Promedio General de la Universidad".
        *   Lista: "Top 10 Alumnos con mejor desempeño".
    *   **Tablero de Bedelía**: "Inscripciones sin Documentación Completa".

### 3. Experiencia de Usuario (UX/UI)
*   **Dolor Latente**: Adopción del sistema por usuarios no técnicos.
*   **Solución Actual**: Lightning App estándar.
*   **Mejora Propuesta (App Builder)**:
    *   **Páginas Dinámicas**: Usar *Dynamic Forms* en el objeto Alumno para mostrar secciones de "Becas" solo si el alumno es becado.
    *   **Path Visual**: Agregar un *Path* en la Inscripción para visualizar el estado (`Inscrito` -> `Cursando` -> `Aprobado`).

### 4. Calidad de Datos Avanzada
*   **Dolor Latente**: "Errores de dedo".
*   **Solución Actual**: Regex y Rangos.
*   **Mejora Propuesta**:
    *   **Duplicate Rules**: Activar reglas de duplicados estándar para Contactos/Alumnos (Matching Rule por DNI y Email). Bloquear la creación si ya existe.
    *   **Help Text & Tooltips**: Agregar instrucciones en cada campo complejo para reducir la capacitación necesaria.

## 🗺️ Roadmap Sugerido (Fase 2)

| Prioridad | Iniciativa | Esfuerzo | Impacto |
| :--- | :--- | :--- | :--- |
| 🔴 **Alta** | **Flow de Naming Convention** | Bajo | Alto (Orden visual inmediato) |
| 🟠 **Media** | **Dashboard de Gestión** | Medio | Alto (Visibilidad para Dra. Vance) |
| 🟢 **Baja** | **Email Templates** | Bajo | Medio (Comunicación institucional) |

---

> **Recomendación del Arquitecto**:
> Implementar inmediatamente el **Flow de Auto-Naming** y el **Dashboard del Rector**. Son "Quick Wins" que demosrtarán el poder de la plataforma más allá del simple ingreso de datos.

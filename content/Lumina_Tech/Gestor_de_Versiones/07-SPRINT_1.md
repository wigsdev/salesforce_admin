# 07-SPRINT_1.md - Resumen Ejecutivo del Sprint
**Estado**: ✅ Completado
**Fechas**: 15/01/2026 - 30/01/2026

---

## 🏆 Logros Principales

### 1. Infraestructura Core
Se desplegó la arquitectura base "Lumina University" sobre una Developer Edition.
*   **Objetos**: 6 (`Carrera`, `Materia`, `Alumno`, `Inscripción`, `Nota`, `Asistencia`).
*   **Relaciones**: Modelo "Estrella" centrado en `Inscripción`.

### 2. Seguridad Implementada ("Zero Trust")
*   **Capas**:
    *   Nivel 1: Login seguro con MFA (`Lumina_MFA_Required`).
    *   Nivel 2: OWD Private para `Alumno`.
    *   Nivel 3: FLS Read-Only para `Nota_Final__c` (perfil `Lumina_Registrar`).

### 3. Calidad de Datos
*   **Validaciones**: Se impide por sistema la carga de notas ilógicas (>10) y emails mal formados.
*   **Integridad**: No existen alumnos "huérfanos" (sin `DNI__c` o `Carrera__c`).

---

## 📉 Métricas de Ejecución
*   **Historias de Usuario**: 12 Comprometidas / 12 Entregadas ([Ver Detalle](../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES_ES.md)).
*   **Bugs Críticos Post-Dev**: 0 (Zero Defects Philosophy).
*   **Coverage**: N/A (No Code Solution).

---

## 🎓 Lecciones Aprendidas (Retrospectiva)
*   **Keep**: El uso de Trello para visibilidad funcionó perfecto.
*   **Improve**: Definir los nombres de campos antes de crearlos (hubo que renombrar `Duration` a `Duracion_Anios__c`).
*   **Action Item**: Crear un "Diccionario de Datos" vivo para el Sprint 2.

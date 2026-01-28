# 📖 Backlog de Historias de Usuario

**Proyecto**: Universidad Lumina Tech
**Rol**: Product Owner
**Sprint**: 01 (Fundamentos)
**Estado**: 🟢 Validado con Cliente

---

## 🔐 Épica A: Seguridad y Privacidad ("Nuestra Gente")
*Objetivo: Segregar el acceso para que Profesores y Administrativos no pisen sus funciones.*

### HU-001: Visibilidad de Profesores
*   **Prioridad**: Alta (Must Have)
*   **Estimación**: 3 SP
*   **Enlace Req**: [REQ-001](Gestor_de_Versiones/01-Business_Analyst.md#req-001-privacidad-de-datos-nuestra-gente)

> **Como** Profesor titular, **Quiero** visualizar únicamente a los alumnos inscritos en mis comisiones, **Para** proteger la privacidad de los estudiantes de otras cátedras y evitar errores de carga.

**✅ Criterios de Aceptación (Definition of Done)**:
1.  [ ] **OWD**: Al ingresar como Profesor, la lista "Todos los Alumnos" muestra solo mis registros compartidos.
2.  [ ] **Search**: Al buscar un alumno de otra cátedra por DNI, el sistema muestra "No records found".
3.  [ ] **Scalability**: Si un Administrativo me asigna una nueva materia, los alumnos aparecen automáticamente.

### HU-002: Restricción de Edición de Notas
*   **Prioridad**: Crítica (Security)
*   **Estimación**: 3 SP
*   **Enlace Req**: [REQ-001](Gestor_de_Versiones/01-Business_Analyst.md)

> **Como** Administrativo de Bedelía, **Quiero** visualizar la ficha del alumno para contactarlo pero ver el campo "Nota" bloqueado, **Para** garantizar que solo el personal docente pueda asentar calificaciones.

**✅ Criterios de Aceptación**:
1.  [ ] **FLS**: Logueado como Administrativo, el campo `Nota__c` en el objeto Examen es visible pero **Read-Only**.
2.  [ ] **API**: Intentar actualizar el campo Nota vía Data Loader con credenciales de Admin arroja error `INSUFFICIENT_ACCESS`.

---

## 📚 Épica B: Arquitectura Académica ("La Estructura")
*Objetivo: Modelar la realidad universitaria en Salesforce (M:N).*

### HU-003: Historial Académico (Inscripciones)
*   **Prioridad**: Alta
*   **Estimación**: 5 SP (High Complexity)
*   **Enlace Req**: [REQ-002](Gestor_de_Versiones/01-Business_Analyst.md#req-002-estructura-académica-la-estructura)

> **Como** Director de Carrera, **Quiero** vincular un alumno a múltiples materias en distintos ciclos lectivos, **Para** obtener una "Foto 360" de su rendimiento a lo largo del tiempo.

**✅ Criterios de Aceptación**:
1.  [ ] **Data Model**: Existe un objeto `Inscripcion__c` que conecta `Alumno` y `Materia`.
2.  [ ] **Integridad**: No se puede crear una inscripción sin seleccionar un Alumno y una Materia (Campos obligatorios).
3.  [ ] **UX**: Desde la ficha del Alumno, veo la lista relacionada "Inscripciones" con columnas `Materia`, `Año`, `Estado`.

### HU-004: Gestión de Exámenes (Parciales/Finales)
*   **Prioridad**: Media
*   **Estimación**: 5 SP
*   **Enlace Req**: [REQ-004](Gestor_de_Versiones/01-Business_Analyst.md#req-04-gestión-de-exámenes-el-ciclo)

> **Como** Profesor, **Quiero** crear registros de exámenes individuales (Parcial 1, Recuperatorio) asociados a una inscripción, **Para** documentar la evaluación continua.

**✅ Criterios de Aceptación**:
1.  [ ] **Structure**: El objeto `Examen__c` es hijo de `Inscripcion__c` (Master-Detail).
2.  [ ] **Roll-up**: La nota del examen impacta en el promedio de la inscripción (si aplica).

---

## 🛡️ Épica C: Calidad del Dato ("Data Quality")
*Objetivo: Prevenir la entrada de basura al sistema.*

### HU-005: Comprobación de Formato de Email
*   **Prioridad**: Media
*   **Estimación**: 2 SP
*   **Enlace Req**: [REQ-003](Gestor_de_Versiones/01-Business_Analyst.md#req-03-calidad-de-datos-errores-de-dedo)

> **Como** Equipo de Admisión, **Quiero** que el sistema valide automáticamente la sintaxis del correo electrónico, **Para** asegurar que las notificaciones lleguen a los alumnos y no reboten.

**✅ Criterios de Aceptación**:
1.  [ ] **Syntax Check**: El campo `Email__c` utiliza el tipo de dato estándar "Email".
2.  [ ] **Negative Test**: Ingresar "nombre,apellido" (coma en vez de punto) o "sin_arroba" bloquea el guardado.
3.  [ ] **Error UI**: El mensaje de error es claro para el usuario ("Formato de correo inválido").

### HU-006: Integridad de Calificaciones
*   **Prioridad**: Media
*   **Estimación**: 2 SP
*   **Enlace Req**: [REQ-003](Gestor_de_Versiones/01-Business_Analyst.md#req-03-calidad-de-datos-errores-de-dedo)

> **Como** Rectoría, **Quiero** que el sistema rechace automáticamente cualquier nota fuera del rango 1-10, **Para** evitar inconsistencias estadísticas.

**✅ Criterios de Aceptación**:
1.  [ ] **Validation**: Ingresar `0` o `10` es válido.
2.  [ ] **Error**: Ingresar `10.5` o `-1` muestra el error: *"La nota debe estar entre 0 y 10"*.

### HU-007: Unicidad de Identidad (DNI)
*   **Prioridad**: Alta
*   **Estimación**: 1 SP

> **Como** Sistema, **Quiero** impedir la duplicación de alumnos basada en su DNI, **Para** mantener una base de datos limpia.

**✅ Criterios de Aceptación**:
1.  [ ] **Unique**: Intentar crear un alumno con DNI ya existente arroja error de duplicado.


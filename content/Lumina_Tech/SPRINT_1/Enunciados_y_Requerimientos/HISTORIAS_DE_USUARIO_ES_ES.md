# 📖 Backlog de Historias de Usuario (Consolidado Sprint 1)
**Proyecto**: Universidad Lumina Tech
**Versión**: Localizada (Objetos y API Names en Español)
**Sprint**: 01 (Fundamentos)
**Alcance**: Días 1 a 4

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definen en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

---

> **🔒 FREEZE NOTE (SPRINT 1 BASELINE)**
> Las Historias de Usuario HU-001 a HU-009 forman la Línea Base del Sprint 1 (Fundamentos).
> **NO MODIFICAR**. Cualquier cambio funcional debe ser documentado como una Nueva Historia en el próximo Sprint.
> *Fecha de Congelamiento: 17-Feb-2026*

---

## 📅 DIA 1: Foundation Académica y de Identidad
*Objetivo: Estructurar los pilares de la base de datos de forma atómica y segura.*

### HU-001: Gestión de Identidad Digital (Persona)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Crítica
*   **Enlace Req**: [REQ-DATA-001]
*   **Descripción**:
    > **Como** Administrador del Sistema,
    > **Quiero** utilizar un único objeto central para registrar a todas las personas y asegurar su privacidad,
    > **Para** evitar la duplicidad de registros y proteger la información sensible.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Renombrar el objeto estándar **`Contact`** a "Persona".
    - [x] 2. Configurar **OWD (Visibilidad)**: Establecer el acceso predeterminado como **Privado**.
    - [x] 3. Crear campos: **`Numero_Documento__c`** (Texto, ID Externo, Único), **`Tipo_Documento__c`** (Picklist), **`Rol__c`** (Picklist con valores Alumno/Docente), y **`Activo__c`** (Checkbox).
    - [x] 4. **Seguridad FLS**: Ocultar el campo `Numero_Documento__c` y el correo electrónico para el perfil **Lumina Professor** (Privacidad).
    - [x] 5. **Validación DNI**: Crear `Formato_DNI_Numerico` (Requerir 8 o 9 dígitos numéricos).
    - [x] 6. **Validación Nombres**: Crear `No_numbers_in_names` (Evitar que nombres contengan números).
    - [x] 7. **Validación Edad**: Crear `Mayoria_de_Edad_Requerida` (Asegurar >18 años).
    - [x] 8. **Validación Email**: Crear `Formato_Email_Valido` (Regex estricto).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Loguearse como Lumina Professor y verificar que el DNI del alumno está oculto.
    - [ ] 2. Intentar crear una persona con DNI de 6 dígitos (Debe fallar).
    - [ ] 3. Intentar crear una persona con 17 años (Debe fallar).

### HU-002: Catálogo de Oferta Educativa (Carrera)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-DATA-002]
*   **Descripción**:
    > **Como** Director Académico,
    > **Quiero** registrar el catálogo público de las carreras disponibles en la universidad,
    > **Para** estructurar el plan de estudios general.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Custom Object: **`Carrera__c`**.
    - [x] 2. Configurar **OWD (Visibilidad)**: Establecer el acceso como **Public Read Only** (El catálogo es público).
    - [x] 3. Crear campos académicos: **`Codigo_de_carrera__c`** (Autonumérico), **`Abreviatura__c`** (Único), **`Facultad__c`** (Picklist), **`Duracion_de_la_carrera__c`** (Picklist).
    - [x] 4. **Validación Nombre**: Implementar `Formato_Nombre_Carrera` (Solo letras).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar crear una carrera llamada "Ingeniería 2026" (Debe fallar por la validación de letras).
    - [ ] 2. Intentar modificar una carrera usando el perfil de un Profesor (Debe fallar por ser Read Only).

### HU-003: Estructura de Asignaturas (Materia)
*   **Estimación**: 🟢 **2 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-DATA-003]
*   **Descripción**:
    > **Como** Bedel,
    > **Quiero** definir las materias y asignarlas a los docentes de manera privada,
    > **Para** tener el catálogo de cursos listos sin que docentes ajenos interfieran.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Custom Object: **`Materia__c`**.
    - [x] 2. Configurar **OWD (Visibilidad)**: Establecer el acceso como **Privado** (Los profesores solo ven las suyas).
    - [x] 3. Crear relación **Master-Detail** apuntando a **`Carrera__c`**.
    - [x] 4. Crear campos: **`Codigo_Materia__c`** (Id Externo), **`Persona__c`** (Lookup a Docente), **`Creditos__c`** (Número).
    - [x] 5. **Validación Créditos**: Implementar `Validar_Creditos_Positivos` (El valor debe ser > 0).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar crear una materia con 0 créditos (Debe fallar).
    - [ ] 2. Entrar como Profesor A y verificar que NO ve las materias asignadas al Profesor B.

---

## 📅 DIA 2: Transacciones y Calidad de Datos
*Objetivo: Registrar el paso del alumno por la universidad con reglas estrictas.*

### HU-004: Registro de Matrículas (Inscripción)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Crítica
*   **Enlace Req**: [REQ-TRANS-001]
*   **Descripción**:
    > **Como** Administrativo,
    > **Quiero** inscribir alumnos garantizando que se anoten en materias que les corresponden,
    > **Para** formalizar su cursada sin violar la lógica académica.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Custom Object (Junction): **`Inscripcion__c`**.
    - [x] 2. Configurar **OWD (Visibilidad)**: Establecer acceso como **Controlado por el Padre** (Si el profe ve la Materia, ve a los inscriptos).
    - [x] 3. Crear relaciones de **Búsqueda (Lookup)** apuntando a **`Contact`** y a **`Materia__c`**.
    - [x] 4. Crear campos: **`Periodo_Academico__c`**, **`Anio_Lectivo__c`**, **`Concepto__c`**, **`Estado__c`**.
    - [x] 5. **Validación Lógica**: Implementar `Coherencia_Carrera_Materia` (La Materia debe pertenecer a la Carrera que cursa el Alumno).
    - [x] 6. **Validación Suspensión**: Implementar `Alumno_Activo_Para_Inscribir` (Evitar inscribir alumnos suspendidos).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar inscribir a un alumno de "Medicina" en una materia de "Derecho" (Debe fallar).

### HU-005: Registro de Asistencias
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Media
*   **Descripción**:
    > **Como** Profesor,
    > **Quiero** registrar el presentismo de mis alumnos con exactitud cronológica,
    > **Para** evaluar su regularidad.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Custom Object: **`Asistencia__c`**.
    - [x] 2. Configurar **OWD (Visibilidad)**: Establecer acceso **Privado**.
    - [x] 3. Crear relación apuntando a **`Inscripcion__c`**.
    - [x] 4. Crear campos: **`Fecha__c`** (Date), **`Estado__c`** (Presente/Ausente).
    - [x] 5. **Validación Cronológica**: Implementar `Solo_Fecha_Actual` (Impedir fechas futuras).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar registrar una asistencia para el día de mañana (Debe fallar).

### HU-006: Registro de Calificaciones (Evaluación)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-TRANS-002]
*   **Descripción**:
    > **Como** Profesor,
    > **Quiero** cargar las notas garantizando segregación de funciones,
    > **Para** que los administrativos no puedan adulterar mis calificaciones.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Custom Object: **`Evaluacion__c`**.
    - [x] 2. Configurar **OWD (Visibilidad)**: Establecer acceso **Privado**.
    - [x] 3. Crear relación apuntando a **`Inscripcion__c`**.
    - [x] 4. Crear campos numéricos: **`Examen_Parcial_1__c`**, **`Examen_Parcial_2__c`**, y **`Promedio_Final__c`** (Fórmula).
    - [x] 5. **Validación Escala**: Implementar `Rango_Nota_Examen` (Valores de 0 a 10 únicamente).
    - [x] 6. **Seguridad (SoD)**: En el perfil **Lumina Registrar** (Administrativo), establecer acceso estricto de **Solo Lectura** al objeto.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar guardar un examen con nota 12 (Debe fallar).
    - [ ] 2. Loguearse como Lumina Registrar e intentar cambiar una nota (Debe fallar por permisos).

### HU-007: Módulo de Tesorería (Cobro)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-FIN-001]
*   **Descripción**:
    > **Como** Personal de Administración,
    > **Quiero** registrar pagos bloqueando completamente la visibilidad a los docentes,
    > **Para** proteger la privacidad financiera.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Custom Object: **`Cobro__c`**.
    - [x] 2. Crear relación **Master-Detail** apuntando a **`Contact`** (Alumno). OWD queda Controlado por el Padre.
    - [x] 3. Crear campo **Roll-up Summary** llamado **`Deudas_Vencidas__c`** en Contacto.
    - [x] 4. Crear campos: **`Monto_Admin__c`**, **`Fecha_de_Pago__c`**, **`Cuota_Vencida__c`**.
    - [x] 5. **Validación Financiera**: Implementar `Prevenir_Datos_Invalidos_Cobro` (Montos > 0).
    - [x] 6. **Seguridad Financiera**: En el perfil **Lumina Professor**, quitar permisos de visualización al objeto (No Read, No View All) y ocultar la pestaña.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Loguearse como Profesor y buscar la pestaña "Cobros" (No debe existir).
    - [ ] 2. Intentar registrar un cobro por $-500 (Debe fallar).

---

## 📅 DIA 3: Infraestructura y Accesos
*Objetivo: Mejorar la experiencia del usuario final y asegurar el ingreso.*

### HU-008: Acceso Seguro y Dominio Institucional
*   **Estimación**: 🟢 **2 SP**
*   **Prioridad**: Crítica
*   **Descripción**:
    > **Como** CISO,
    > **Quiero** una URL segura y requerir doble factor de autenticación,
    > **Para** prevenir ingresos no autorizados.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Desplegar **Mi Dominio** (`lumina-tech-university-dev-ed.trailblaze.my.salesforce.com/`).
    - [x] 2. Crear Permission Set `Lumina_MFA_Access` con el permiso "MFA for User Interface Logins" activo.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar el ingreso con la nueva URL y que el sistema solicite MFA a los usuarios asignados.

### HU-009: Navegación Centralizada (Lightning App)
*   **Estimación**: 🟢 **2 SP**
*   **Prioridad**: Media
*   **Descripción**:
    > **Como** Usuario,
    > **Quiero** un menú que contenga solo los objetos relevantes para mi rol,
    > **Para** agilizar mi trabajo diario.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Lightning App "Gestión Académica Lumina".
    - [x] 2. Añadir pestañas: Personas, Carreras, Materias, Inscripciones, Asistencias, Evaluaciones, Cobros.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Abrir la app y verificar el orden de las pestañas configuradas.

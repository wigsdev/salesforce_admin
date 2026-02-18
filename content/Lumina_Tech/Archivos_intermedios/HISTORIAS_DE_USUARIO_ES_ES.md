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
> Las Historias de Usuario HU-001 a HU-012 forman la Línea Base del Sprint 1 (Fundamentos).
> **NO MODIFICAR**. Cualquier cambio funcional debe ser documentado como una Nueva Historia (HU-013+) en el próximo Sprint.
> *Fecha de Congelamiento: 17-Feb-2026*

---

## 📅 DIA 1: Modelado de Datos (Data Foundation)
*Objetivo: Estructurar la base de datos para soportar la operación académica.*

### HU-001: Gestión de Oferta Académica (Carrera y Materia)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Crack (Core)
*   **Enlace Req**: [REQ-DATA-001]
*   **Descripción**:
    > **Como** Director Académico,
    > **Quiero** definir las Carreras y sus Materias asociadas con detalle granular (créditos, horas, ciclo),
    > **Para** estructurar el plan de estudios disponible para los alumnos y calcular cargas horarias.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Custom Object: **Carrera** (`Carrera__c`).
        *   **Nombre de Registro**: `Nombre de Carrera` (Texto).
        *   Campos: **Código Interno** (`Codigo_Interno__c` - AutoNumber), **Tipo de Título** (`Tipo_Titulo__c` - Picklist), **Duración (Años)** (`Duracion_Anios__c` - Picklist 1-5), **Activa** (`Activa__c` - Checkbox).
    - [x] 2. Crear Custom Object: **Materia** (`Materia__c`).
        *   **Nombre de Registro**: `Nombre de Materia` (Texto).
        *   **Relación**: Master-Detail hacia **Carrera**.
        *   Campos Core: **Código de Materia** (`Codigo_Materia__c` - AutoNumber), **Créditos** (`Creditos__c` - Picklist 1-10), **Tipo** (`Tipo_Materia__c` - Picklist), **Año del Plan** (`Anio_Plan__c` - Picklist 1-5).
        *   Campos Académicos: **Ciclo** (`Ciclo__c` - Picklist), **Cuatrimestre Sugerido** (`Cuatrimestre_Sugerido__c` - Number), **Horas Semanales** (`Horas_Semanales__c`), **Horas Totales** (`Horas_Totales__c`).
        *   Campos Sistema: **Activa** (`Activa__c`), **Código Externo** (`Codigo_Externo__c` - Unique ID).
    - [x] 3. Crear **Vistas de Lista** (List Views) "Todas" para ambos objetos.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar creación de una Carrera (ej: "Ingeniería de Software") con duración 5 años (Pickist).
    - [ ] 2. Verificar creación de una Materia vinculada a esa Carrera (ej: "Algoritmos I") con sus Horas y Créditos (Picklist).
    - [ ] 3. Validar que al borrar la Carrera, se borren sus Materias (Cascada).
    - [ ] 4. Verificar que no se pueda guardar una materia sin elegir Carrera (Master-Detail).

### HU-002: Gestión de Alumnos e Inscripciones (Alumno & Inscripción)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-003, REQ-DATA-002]
*   **Descripción**:
    > **Como** Administrativo,
    > **Quiero** registrar alumnos con identidad digital unificada e inscribirlos a materias por ciclo/turno,
    > **Para** formalizar su cursada garantizando seguridad y coherencia académica.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    *Parte A: Alumno (Identidad)*
    - [x] 1. Crear Custom Object: **Alumno** (`Alumno__c`). Registro Autonumérico (`A-{YYYY}-{0000}`).
    - [x] 2. Campos Core: **DNI** (`DNI__c` - Único), **Nombres**, **Apellidos**, **Email Personal**.
    - [x] 3. Campos Académicos: **Carrera** (Lookup), **Fecha Ingreso**, **Ciclo Ingreso** (Fórmula), **Estado** (Picklist: Matriculado/Graduado...).
    - [x] 4. **Identidad Digital**: Campos Fórmula `Usuario_Sistema__c` (DNI@lumina.edu.ar) y `Email_Institucional__c` (Sanitizado).
    
    *Parte B: Inscripción (Matrícula)*
    - [x] 5. Crear Custom Object: **Inscripción** (`Inscripcion__c`).
    - [x] 6. Relación **Maestro-Detalle** hacia **Alumno** y **Materia**.
    - [x] 7. Campos Operativos: **Ciclo** (Picklist 2024-1...), **Turno** (Mañana/Noche), **Estado** (Cursando/Aprobado).
    - [x] 8. **Integridad**: Flow "Set Composite Key" para llenar `Clave_Inscripcion__c` (Alumno+Materia+Ciclo) y evitar duplicados.
    - [x] 9. **Asistencia Automática**: Campos para cálculo de regularidad (`Clases_Esperadas`, `Clases_Presentes`, `% Asistencia`).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [x] 1. Verificar que el Usuario Sistema se genere automático (DNI@lumina.edu.ar).
    - [x] 2. Verificar que el Email Institucional se genere sin tildes ni espacios.
    - [x] 3. Validar bloqueo de DNI duplicado y formato de 8 dígitos (`DNI_Numerico_8`).
    - [x] 4. Intentar ingresar fecha de ingreso futura; el sistema debe bloquearlo (`Fecha_Ingreso_No_Futura`).
    - [x] 5. Intentar inscribir al mismo alumno en la misma materia y ciclo; el sistema debe bloquearlo (Flow).
    - [x] 6. Verificar que al inscribir, se calculen automáticamente las "Clases Esperadas".

### HU-003: Gestión de Seguimiento Académico (Notas y Asistencias)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-002, REQ-FUNC-002, REQ-AUTO-001]
*   **Descripción**:
    > **Como** Profesor,
    > **Quiero** registrar calificaciones (parciales, prácticas) y asistencias diario/clase,
    > **Para** tener una trazabilidad granular del desempeño y la regularidad del alumno durante el ciclo.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    *Parte A: Objeto Nota (Evaluación)*
    - [x] 1. Crear Custom Object: **Nota** (`Nota__c`). Habilitar **Track Field History**.
    - [x] 2. Relación **Lookup** (Obligatoria) hacia **Inscripción** (`Inscripcion__c`).
    - [x] 3. Campos: **Calificación** (`Calificacion__c` - Number 4,2), **Tipo** (`Tipo__c` - Picklist), **Fecha**, **Ponderación** (`Ponderacion__c` - Percent), **Observaciones** (`Observaciones__c` - Text Area).
    - [x] 4. Lógica:
        *   Fórmula `Escala_Calificacion__c` (Traduce nota a texto: Aprobado/Reprobado).
        *   Fórmula `Nota_Ponderada__c` (Calcula `Calificación * Ponderación`).
    - [x] 5. **Automatización**: Crear Flow que sume las `Notas Ponderadas` y actualice el campo `Nota_Final__c` en la **Inscripción**.
    - [x] 6. **Auditoría**: Configurar **Set History Tracking** para auditar cambios en `Calificación` y `Ponderación`.
    
    *Parte B: Objeto Asistencia (Presentismo)*
    - [x] 5. Crear Custom Object: **Asistencia** (`Asistencia__c`).
    - [x] 6. Relación **Lookup** (Obligatoria) hacia **Inscripción** (`Inscripcion__c`).
    - [x] 7. Campos: **Fecha** (Date), **Estado** (Picklist: Presente/Ausente...), **Tipo de Clase** (Teórica/Práctica).
    - [x] 8. Integridad: Regla de Validación `Fecha_No_Futura` en ambos objetos.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Registrar una Nota "Parcial 1" con calificación 8.00 y Ponderación 25%.
    - [ ] 2. Verificar que el campo "Nota Ponderada" muestre automáticamente **2.00**.
    - [ ] 3. Modificar la Calificación de 8.00 a 9.00.
    - [ ] 4. Ir a la pestaña "Related" > "Nota History" y verificar que aparezca el registro del cambio (Valor anterior: 8.00, Valor nuevo: 9.00).
    - [ ] 5. Intentar guardar una Nota sin vincularla a una Inscripción (Debe fallar).

---

## 📅 DIA 2: Identidad e Interfaz (Branding)
*Objetivo: Generar pertenencia y confianza en la plataforma.*

### HU-004: Dominio Seguro (My Domain)
*   **Estimación**: 🟢 **1 SP**
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-SEC]
*   **Descripción**:
    > **Como** Usuario Institucional,
    > **Quiero** ver una URL segura y personalizada (lumina-tech-university),
    > **Para** tener confianza de que estoy navegando en el sitio oficial.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Desplegar **Mi Dominio** (My Domain). URL: `https://lumina-tech-university-dev-ed.trailblaze.my.salesforce.com/`.
    - [x] 2. Ejecutar **Deploy to Users** una vez provisionado.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar que la URL del navegador comience con `lumina-tech-university`.
    - [ ] 2. Verificar que el botón de login redirija correctamente a la nueva URL.

### HU-005: Identidad Institucional (Theme & Branding)
*   **Estimación**: 🟢 **1 SP**
*   **Prioridad**: Baja (UI)
*   **Enlace Req**: [REQ-BRAND]
*   **Descripción**:
    > **Como** Equipo de Rectoría,
    > **Quiero** ver los colores y logo oficiales en la aplicación (Azul Lumina),
    > **Para** reforzar la identidad y pertenencia institucional.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear un **Theme & Branding** llamado "Lumina Oficial" (API: `Lumina_Oficial`).
    - [x] 2. Configurar **Brand Color**: `#005A9C`.
    - [x] 3. Cargar Assets Gráficos: `lumina_logo_header.png`, `lumina_banner.png` (Page Background), `lumina_avatar_user.png`.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar que la barra de navegación sea de color Azul Lumina `#005A9C`.
    - [ ] 2. Verificar que el fondo de página muestre el banner institucional.
    - [ ] 3. Verificar que el avatar por defecto sea el logo de Lumina.

### HU-006: App de Gestión Central (Lightning App)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-FUNC]
*   **Descripción**:
    > **Como** Usuario,
    > **Quiero** tener un lanzador de aplicaciones dedicado a la gestión académica,
    > **Para** acceder rápidamente a Alumnos, Materias e Inscripciones sin distracciones.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear **Lightning App**: "Gestión Académica Lumina" (API: `Gestion_Academica_Lumina`).
    - [x] 2. Configurar **Navigation Items**: **Home**, **Alumnos**, **Carreras**, **Materias**, **Inscripciones**, **Asistencias**, **Notas**.
    - [x] 3. Asignar Perfiles: **System Administrator**, **Lumina Professor**, **Lumina Registrar**.
    - [x] 4. (Recuperación) Crear Tabs para todos los objetos si no existen.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Buscar "Gestión Académica" en el App Launcher y acceder.
    - [ ] 2. Verificar que las pestañas sean: Alumnos, Carreras, Materias, Inscripciones, Asistencias, Notas (en ese orden).

---

## 📅 DIA 3: Calidad y Automatización
*Objetivo: "Data Quality at Source" y Automatización de Procesos.*

### HU-007: Validación de Contactos (Email)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-QUAL-001]
*   **Descripción**:
    > **Como** Departamento de Marketing,
    > **Quiero** asegurar que los correos electrónicos tengan un formato válido,
    > **Para** evitar errores de tipeo y asegurar la comunicación.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear una **Regla de Validación** llamada `Formato_Email_Valido` en el objeto **Alumno** (`Alumno__c`).
    - [x] 2. Implementar lógica **REGEX** estricta: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$`.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar registrar `usuario@gmail,com` (con coma); el sistema debe rechazarlo.
    - [ ] 2. Registrar `usuario@lumina.edu`; el sistema debe aceptarlo exitosamente.

### HU-008: Integridad de Datos (Reglas de Negocio)
*   **Estimación**: 🟢 **1 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-002]
*   **Descripción**:
    > **Como** Sistema,
    > **Quiero** bloquear automáticamente ingresos ilógicos (notas >10, fechas futuras, cruce de carreras),
    > **Para** mantener la coherencia y calidad de los datos.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. **Inscripción**: Regla `Solo_Alumnos_Matriculados` (Estado = Matriculado).
    - [x] 2. **Inscripción**: Regla `Coherencia_Carrera_Materia` (Materia y Alumno deben ser de la misma Carrera).
    - [x] 3. **Asistencia**: Regla `Fecha_No_Futura` (No registrar presente futuro).
    - [x] 4. **Nota**: Regla `Rango_Nota_Valida` (1-10 solamente).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [x] 1. Intentar inscribir a un alumno "Suspendido"; debe fallar.
    - [x] 2. Intentar inscribir a un alumno de Ingeniería en una materia de Medicina; debe fallar.
    - [x] 3. Intentar tomar asistencia para mañana; debe fallar.
    - [x] 4. Intentar ingresar nota 15; debe fallar.

### HU-009: Control de Asistencias (Automatización)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-AUTO-001]
*   **Descripción**:
    > **Como** Preceptor,
    > **Quiero** identificar automáticamente a los alumnos "Libres" (<75% asistencia),
    > **Para** intervenir tempranamente sin realizar cálculos manuales.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear campo **Número** llamado **Clases Asistidas** (`Clases_Asistidas__c`).
    - [x] 2. Crear campo **Número** llamado **Clases Totales** (`Clases_Totales__c`).
    - [x] 3. Crear campo **Fórmula** (Porcentaje) llamado **% Asistencia** (`Porcentaje_Asistencia__c`).
        *   Fórmula: `Clases_Asistidas__c / Clases_Totales__c`
    - [x] 4. Crear campo **Fórmula** (Texto) llamado **Condición Académica** (`Condicion_Academica__c`) con lógica `< 0.75`.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Ingresar 5 clases asistidas de 10 totales.
    - [ ] 2. Verificar que el % de Asistencia se calcule automáticamente en 50%.
    - [ ] 3. Verificar que la Condición Académica muestre el texto "Libre".

---

## 📅 DIA 4: Seguridad y Accesos
*Objetivo: Zero Trust (Confianza Cero).*

### HU-010: Matriz de Visibilidad (Comisiones)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Crítica
*   **Enlace Req**: [REQ-SEC-002]
*   **Descripción**:
    > **Como** Profesor,
    > **Quiero** ver solo las notas y alumnos de MIS comisiones asignadas,
    > **Para** proteger la privacidad de los estudiantes.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Configurar **Valores Predeterminados (OWD)** de **Materia** como **Privado**.
    - [x] 2. Configurar **Valores Predeterminados (OWD)** de **Nota** como **Privado**.
    - [x] 3. Verificar que el **OWD** de **Inscripción** sea **Controlado por el Padre** (Controlled by Parent).
    - [x] 4. Crear una **Regla de Uso Compartido** (Sharing Rule) para compartir registros con el Owner/Profesor.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Loguearse como Profesor A.
    - [ ] 2. Verificar que NO pueda ver la Materia asignada al Profesor B.
    - [ ] 3. Verificar que solo pueda ver los alumnos inscritos en SUS Materias.

### HU-011: Acceso Seguro (MFA)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Crítica
*   **Enlace Req**: [REQ-SEC-001]
*   **Descripción**:
    > **Como** CISO,
    > **Quiero** requerir un segundo factor de autenticación para el login,
    > **Para** prevenir accesos no autorizados.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear un **Conjunto de Permisos** (Permission Set) llamado `Lumina_MFA_Access`.
    - [x] 2. Habilitar el permiso de sistema de MFA.
    - [x] 3. Asignar el Conjunto de Permisos a los usuarios.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar loguearse con un usuario con MFA.
    - [ ] 2. Verificar que solicite código o autenticación móvil.

### HU-012: Segregación de Funciones (FLS)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-SEC-003]
*   **Descripción**:
    > **Como** Auditoría,
    > **Quiero** diferenciar qué roles pueden editar notas y cuáles ver datos sensibles,
    > **Para** implementar SoD efectiva.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Perfil: **Lumina Professor** (Docente).
        *   **Objetos**: `Nota` y `Asistencia` (Lectura/Crear/Editar). `Inscripción` (Solo Lectura).
        *   **FLS (Privacidad)**: Ocultar `DNI`, `Teléfono`, `Email` del objeto **Alumno**.
    - [x] 2. Crear Perfil: **Lumina Registrar** (Administrativo).
        *   **Objetos**: `Alumno` e `Inscripción` (Lectura/Crear/Editar).
        *   **Restricción**: SIN acceso a `Nota` ni `Asistencia` (SoD: No puede manipular calificaciones).
    - [x] 3. Crear Perfil: **Lumina Student** (Alumno).
        *   **Objetos**: `Inscripción` (Lectura/Crear - Auto-Inscripción). `Carrera` y `Materia` (Solo Lectura).
        *   **Restricción**: SIN acceso a `Nota` (Se publica vía Portal/Comunidad).
        *   **Seguridad**: Regla de Validación `Seguridad_Inscripcion_Propia` (Solo puede inscribirse a sí mismo).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Loguearse como **Lumina Professor** y verificar que NO ve el campo DNI de sus alumnos.
    - [ ] 2. Intentar crear una Inscripción siendo Profesor; el sistema debe impedirlo (Solo Lectura).
    - [ ] 3. Loguearse como **Lumina Registrar** y verificar que no ve la pestaña "Notas".
    - [ ] 4. Loguearse como **Lumina Student** e intentar borrar una Inscripción; debe fallar.

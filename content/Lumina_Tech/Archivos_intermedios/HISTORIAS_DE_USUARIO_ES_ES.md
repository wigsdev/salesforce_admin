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

## 📅 DIA 1: Modelado de Datos (Data Foundation)
*Objetivo: Estructurar la base de datos para soportar la operación académica.*

### HU-001: Gestión de Oferta Académica (Carrera y Materia)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Crack (Core)
*   **Enlace Req**: [REQ-DATA-001]
*   **Descripción**:
    > **Como** Director Académico,
    > **Quiero** definir las Carreras y sus Materias asociadas,
    > **Para** estructurar el plan de estudios disponible para los alumnos.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [ ] 1. Crear Custom Object: **Carrera** (`Carrera__c`).
        *   **Nombre de Registro**: `Código de Carrera` (Autonumérico).
        *   Campos: **Nombre de la Carrera** (`Nombre_Carrera__c`), **Duración (Años)** (`Duracion_Anios__c`), **Tipo de Título** (`Tipo_Titulo__c`).
    - [ ] 2. Crear Custom Object: **Materia** (`Materia__c`).
        *   **Nombre de Registro**: `Nombre de Materia` (Texto).
        *   Campos: **Código de Materia** (`Codigo_Materia__c`), **Créditos** (`Creditos__c`), **Año del Plan** (`Anio_Plan__c`).
    - [ ] 3. Crear relación **Maestro-Detalle** en Materia hacia **Carrera** (`Carrera__c`).
    - [ ] 4. Configurar **Visibilidad de Pestaña** en *Default On* para Admin/Director.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar creación de una Carrera (ej: "Ingeniería de Software").
    - [ ] 2. Verificar creación de una Materia vinculada a esa Carrera (ej: "Algoritmos I" -> "Ing. Software").
    - [ ] 3. Validar que al borrar la Carrera, se borren sus Materias (Maestro-Detalle).

### HU-002: Gestión de Alumnos e Inscripciones (Alumno & Inscripción)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-003, REQ-DATA-002]
*   **Descripción**:
    > **Como** Administrativo,
    > **Quiero** registrar alumnos con identidad única e inscribirlos a materias,
    > **Para** formalizar su cursada garantizando que no existan duplicados.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    *Parte A: Alumno*
    - [ ] 1. Crear Custom Object: **Alumno** (`Alumno__c`).
    - [ ] 2. Configurar **Nombre de Registro** (Legajo) como **Autonumérico** `A-{YYYY}-{0000}`.
    - [ ] 3. Crear campo **Texto** **DNI** (`DNI__c`) (Único, ID Externo) con Regla de Validación `DNI_Numerico_8`.
    - [ ] 4. Crear campos básicos: **Nombres** (`Nombres__c`), **Apellidos** (`Apellidos__c`), **Email Personal** (`Email_Personal__c`) (Email), **Teléfono** (`Telefono__c`) (Teléfono).
    
    *Parte B: Inscripción*
    - [ ] 5. Crear Custom Object: **Inscripción** (`Inscripcion__c`).
    - [ ] 6. Relacionar **Maestro-Detalle** hacia **Alumno** (`Alumno__c`) y **Materia** (`Materia__c`).
    - [ ] 7. Crear campos Lista de Selección: **Ciclo** (`Ciclo__c`), **Comisión** (`Comision__c`) y **Estado** (`Estado__c`) (Cursando/Aprobado/Reprobado).
    - [ ] 8. (Avanzado) Implementar **Flujo** (Flow) para llenar campo único `Clave_Inscripcion__c` (Alumno+Materia+Ciclo) para evitar duplicados.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar que el Legajo se genere automático (A-2024-xxxx).
    - [ ] 2. Validar bloqueo de DNI duplicado y formato incorrecto.
    - [ ] 3. Verificar creación de Inscripción vinculando Alumno y Materia existentes.
    - [ ] 4. Confirmar que borrar un Alumno elimina sus Inscripciones.
    - [ ] 5. Intentar inscribir al mismo alumno en la misma materia y ciclo (Ej: Mat-2024-1) dos veces; el sistema debe bloquearlo.

### HU-003: Gestión de Exámenes y Notas
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-002, REQ-FUNC-002]
*   **Descripción**:
    > **Como** Administrativo de Actas y Profesor,
    > **Quiero** guardar notas con precisión decimal, auditoría y registrar exámenes parciales,
    > **Para** garantizar la transparencia académica, prevenir fraudes y tener evaluación granular.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    *Parte A: Integridad de Notas (Original)*
    - [x] 1. En el objeto **Inscripción**: Crear un campo **Número** llamado **Nota Final** (`Nota_Final__c`) con precisión `(4,2)`.
    - [x] 2. Crear un campo **Lista de Selección** llamado **Estado** (`Estado__c`) con valores Cursando/Aprobado/Reprobado.
    - [x] 3. Crear una **Regla de Validación** llamada `Rango_Nota_1_10` (Fórmula: `OR(Nota_Final__c < 1, Nota_Final__c > 10)`).
    - [x] 4. Habilitar **Seguimiento de Historial** (Field History Tracking) para el campo `Nota_Final__c`.
    
    *Parte B: Gestión de Exámenes (Ampliación)*
    - [ ] 5. Crear Custom Object **Examen** (`Examen__c`).
    - [ ] 6. Crear relación **Búsqueda** (Lookup) Obligatoria hacia **Inscripción** (`Inscripcion__c`).
    - [ ] 7. Crear campos: **Nota** (`Nota__c`) (Número 4,2), **Fecha Examen** (`Fecha_Examen__c`) (Fecha), **Asistió** (`Asistio__c`) (Casilla/Checkbox).
    - [ ] 8. Crear Regla de Validación `Rango_Nota_Examen` (Fórmula: `OR(Nota__c < 0, Nota__c > 10)`).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Ingresar una nota de 8.55 y verificar que se guarde correctamente.
    - [ ] 2. Intentar ingresar una nota de 11 o -1; el sistema debe mostrar error.
    - [ ] 3. Modificar una nota existente y verificar que el cambio aparezca en el historial.
    - [ ] 4. (Nuevo) Crear un Examen vinculado a una Inscripción con nota 8.50.
    - [ ] 5. (Nuevo) Intentar ingresar nota de Examen 11; el sistema debe bloquearlo.

---

## 📅 DIA 2: Identidad e Interfaz (Branding)
*Objetivo: Generar pertenencia y confianza en la plataforma.*

### HU-004: Dominio Seguro
*   **Estimación**: 🟢 **1 SP**
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-SEC]
*   **Descripción**:
    > **Como** Usuario Institucional,
    > **Quiero** ver una URL segura y personalizada (lumina-university),
    > **Para** tener confianza de que estoy navegando en el sitio oficial.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Desplegar **Mi Dominio** (My Domain) con el nombre `lumina-university`.
    - [x] 2. Desplegar la configuración a los usuarios (**Deploy to Users**).
    - [x] 3. Configurar el logo oficial en la **Página de Inicio de Sesión**.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar que la URL del navegador comience con `lumina-university.my.salesforce.com`.
    - [ ] 2. Verificar que la pantalla de Login muestre el logo de Lumina Tech.

### HU-005: Identidad Institucional
*   **Estimación**: 🟢 **1 SP**
*   **Prioridad**: Baja (UI)
*   **Enlace Req**: [REQ-BRAND]
*   **Descripción**:
    > **Como** Equipo de Rectoría,
    > **Quiero** ver los colores y logo oficiales en la aplicación,
    > **Para** reforzar la identidad y pertenencia institucional.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear un **Temas y Marca** (Theme & Branding) llamado "Lumina Oficial".
    - [x] 2. Configurar el **Color de Marca** con el valor `#005A9C` (Azul Lumina).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar que la barra de navegación sea de color Azul Lumina `#005A9C`.
    - [ ] 2. Verificar que el fondo de página sea gris claro y no blanco por defecto.

### HU-006: App de Gestión Central
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-FUNC]
*   **Descripción**:
    > **Como** Usuario,
    > **Quiero** tener un lanzador de aplicaciones dedicado a la gestión académica,
    > **Para** acceder rápidamente a Alumnos, Materias e Inscripciones sin distracciones.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear una **Aplicación Lightning** llamada "Gestión Académica Lumina".
    - [x] 2. Añadir los **Elementos de Navegación**: **Alumnos**, **Materias**, **Inscripciones**, **Carreras**.
    - [x] 3. Asignar la App a los Perfiles: **Administrador del Sistema**, **Lumina Professor**, **Lumina Registrar**.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Buscar "Gestión Académica" en el Iniciador de Aplicación (App Launcher) y acceder.
    - [ ] 2. Verificar que las pestañas sean exclusivamente las académicas.

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
    - [x] 2. Implementar lógica **REGEX** para validar la estructura estándar.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar registrar `usuario@gmail,com` (con coma); el sistema debe rechazarlo.
    - [ ] 2. Registrar `usuario@lumina.edu`; el sistema debe aceptarlo exitosamente.

### HU-008: Integridad Numérica (Hard Validation)
*   **Estimación**: 🟢 **1 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-002]
*   **Descripción**:
    > **Como** Sistema,
    > **Quiero** bloquear automáticamente el ingreso de notas ilógicas (fuera de rango 1-10),
    > **Para** mantener la calidad de los datos.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Verificar existencia de la **Regla de Validación** `Rango_Nota_1_10` en **Inscripción**.
    - [x] 2. Verificar mensaje de error en español ("Nota inválida...").
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar que al ingresar nota 15, aparezca el mensaje de error.
    - [ ] 2. Verificar que permita ingresar nota 1.00 y 10.00.

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
    - [x] 2. Verificar que el **OWD** de **Inscripción** sea **Controlado por el Padre** (Controlled by Parent).
    - [x] 3. Crear una **Regla de Uso Compartido** (Sharing Rule) para compartir registros con el Owner/Profesor.
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
    - [x] 1. Crear Perfil: **Lumina Registrar**. Configurar `Nota_Final__c` como **Solo Lectura**.
    - [x] 2. Crear Perfil: **Lumina Professor**. Configurar `Nota_Final__c` como **Editar**.
    - [x] 3. Configurar Perfil: Remover **Acceso de Lectura** para `DNI__c` y `Telefono__c` en el perfil Professor.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Loguearse como "Registrar" y verificar que no puede editar la nota.
    - [ ] 2. Loguearse como "Professor" y verificar que no ve el DNI del alumno.

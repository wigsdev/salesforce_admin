# 📖 Backlog de Historias de Usuario (Consolidado Sprint 1)
**Proyecto**: Universidad Lumina Tech
**Sprint**: 01 (Fundamentos)
**Alcance**: Días 1 a 4

---

## 📅 DIA 1: Modelado de Datos (Data Foundation)
*Objetivo: Estructurar la base de datos para soportar la operación académica.*

### HU-001: Gestión de Oferta Académica (Career & Subject)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Crack (Core)
*   **Enlace Req**: [REQ-DATA-001]
*   **Descripción**:
    > **Como** Director Académico,
    > **Quiero** definir las Carreras y sus Materias asociadas,
    > **Para** estructurar el plan de estudios disponible para los alumnos.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [ ] 1. Crear Custom Object: **Career** (`Career__c`). Campos: `Name` (Text), `Duration_Years__c` (Number), `Type__c` (Picklist).
    - [ ] 2. Crear Custom Object: **Subject** (`Subject__c`). Campos: `Credits__c` (Number), `Max_Capacity__c` (Number).
    - [ ] 3. Crear relación **Master-Detail** en Subject hacia **Career** (`Career__c`).
    - [ ] 4. Configurar **Tab Visibility** en *Default On* para Admin/Director.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar creación de una Carrera (ej: "Ingeniería de Software").
    - [ ] 2. Verificar creación de una Materia vinculada a esa Carrera (ej: "Algoritmos I" -> "Ing. Software").
    - [ ] 3. Validar que al borrar la Carrera, se borren sus Materias (Master-Detail).

### HU-002: Gestión de Alumnos e Inscripciones (Student & Enrollment)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-003, REQ-DATA-002]
*   **Descripción**:
    > **Como** Administrativo,
    > **Quiero** registrar alumnos con identidad única e inscribirlos a materias,
    > **Para** formalizar su cursada garantizando que no existan duplicados.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    *Parte A: Alumno (Student)*
    - [ ] 1. Crear Custom Object: **Student** (`Student__c`).
    - [ ] 2. Configurar **Record Name** como **Auto-Number** `A-{YYYY}-{0000}`.
    - [ ] 3. Crear campo **Text** `National_ID__c` (Unique, External ID) con Validation Rule (8 dígitos).
    - [ ] 4. Crear campos básicos: `First_Name__c`, `Last_Name__c`, `Email__c` (Email), `Phone__c` (Phone), `Address__c` (Text Area).
    
    *Parte B: Inscripción (Enrollment)*
    - [ ] 5. Crear Custom Object: **Enrollment** (`Enrollment__c`).
    - [ ] 6. Relacionar **Master-Detail** hacia **Student** (`Student__c`) y **Subject** (`Subject__c`).
    - [ ] 7. Crear campos Picklist: `Cycle__c`, `Commission__c` y `Status__c` (Enrolled/Passed/Failed).
    - [ ] 8. (Advanced) Implementar **Flow** para llenar campo único `Enrollment_Key__c` (Student+Subject+Cycle) para evitar duplicados.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar que el Student ID se genere automático (A-2024-xxxx).
    - [ ] 2. Validar bloqueo de National ID duplicado y formato incorrecto.
    - [ ] 3. Verificar creación de Inscripción vinculando Student y Subject existentes.
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
    - [x] 1. En el objeto **Enrollment**: Crear un campo **Number** llamado **Final Grade** (`Final_Grade__c`) con precisión `(4,2)`.
    - [x] 2. Crear un campo **Picklist** llamado **Status** (`Status__c`) con valores Passed/Failed/Enrolled.
    - [x] 3. Crear una **Validation Rule** llamada `Grade_Range_1_10` (Fórmula: `OR(Grade < 1, Grade > 10)`).
    - [x] 4. Habilitar **Field History Tracking** para el campo `Final_Grade__c`.
    
    *Parte B: Gestión de Examenes (Ampliación)*
    - [ ] 5. Crear Custom Object **Exam** (`Exam__c`).
    - [ ] 6. Crear relación **Master-Detail** hacia **Enrollment**.
    - [ ] 7. Crear campos: `Score__c` (Number 4,2), `Exam_Date__c` (Date), `Attended__c` (Checkbox).
    - [ ] 8. Crear Validation Rule `Exam_Score_Range` (Fórmula: `OR(Score__c < 0, Score__c > 10)`).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Ingresar una nota de 8.55 y verificar que se guarde correctamente.
    - [ ] 2. Intentar ingresar una nota de 11 o -1; el sistema debe mostrar error.
    - [ ] 3. Modificar una nota existente y verificar que el cambio aparezca en el historial (Field History).
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
    - [x] 1. Desplegar **My Domain** con el nombre `lumina-university`.
    - [x] 2. Desplegar la configuración a los usuarios (**Deploy to Users**).
    - [x] 3. Configurar el logo oficial en la **Login Page**.
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
    - [x] 1. Crear un **Theme & Branding** llamado "Lumina Official".
    - [x] 2. Configurar el **Brand Color** con el valor `#005A9C` (Azul Lumina).
    - [x] 3. Configurar el **Page Background Color** con `#F3F3F3` (Gris Claro).
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
    - [x] 1. Crear una **Lightning App** llamada "Gestión Académica" (`Lumina_Academic`).
    - [x] 2. Añadir los **Navigation Items**: **Students**, **Subjects**, **Enrollments**.
    - [x] 3. Asignar la App a los Perfiles: **System Administrator** y **Standard User**.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Buscar "Gestión Académica" en el App Launcher y acceder.
    - [ ] 2. Verificar que las pestañas sean exclusivamente Students, Subjects y Enrollments (sin basura extra).

---

## 📅 DIA 3: Calidad y Automatización
*Objetivo: "Data Quality at Source" y Automatización de Procesos.*

### HU-007: Validar Formato de Email
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Media
*   **Enlace Req**: [REQ-QUAL-001]
*   **Descripción**:
    > **Como** Departamento de Marketing,
    > **Quiero** asegurar que los correos electrónicos tengan un formato válido,
    > **Para** evitar errores de tipeo y asegurar la comunicación.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear una **Validation Rule** llamada `Valid_Email_Format` en el objeto **Student**.
    - [x] 2. Implementar lógica **REGEX** para validar estructura estándar (user@domain.com).
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar registrar `user@gmail,com` (con coma); el sistema debe rechazarlo.
    - [ ] 2. Registrar `user@gmail.com` o `user@lumina.edu`; el sistema debe aceptarlo exitosamente.

### HU-008: Integridad Numérica (Hard Validation)
*   **Estimación**: 🟢 **1 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-QUAL-002]
*   **Descripción**:
    > **Como** Sistema,
    > **Quiero** bloquear automáticamente el ingreso de notas ilógicas (fuera de rango),
    > **Para** mantener la calidad de los datos y evitar errores de tipeo.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Verificar existencia de la **Validation Rule** `Grade_Range_1_10` en **Enrollment**.
    - [x] 2. Verificar que el **Error Message** esté en Inglés ("Invalid Grade...").
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Verificar que al ingresar nota 15, aparezca el mensaje de error en inglés: "Invalid Grade...".
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
    - [x] 1. Crear campo **Number** llamado **Classes Attended** (`Classes_Attended__c`).
    - [x] 2. Crear campo **Number** llamado **Total Classes** (`Total_Classes__c`).
    - [x] 3. Crear campo **Formula** (Percent) llamado **Attendance %** (`Attendance_Percentage__c`).
    - [x] 4. Crear campo **Formula** (Text) llamado **Academic Condition** (`Academic_Condition__c`) con lógica `< 0.75`.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Ingresar 5 clases asistidas de 10 totales.
    - [ ] 2. Verificar que el % de Asistencia se calcule automáticamente en 50%.
    - [ ] 3. Verificar que la Condición Académica muestre el texto (o semáforo/mensaje) correspondiente a "Libre".

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
    > **Para** proteger la privacidad de los estudiantes de otros cursos (Compliance).
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Configurar **Organization-Wide Defaults (OWD)** de **Subject** como **Private**.
    - [x] 2. Verificar que el **OWD** de **Enrollment** sea **Controlled by Parent**.
    - [x] 3. Crear una **Sharing Rule** (Criteria-Based) para compartir registros con el Owner/Profesor.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Loguearse como Profesor A (Propietario de Materia 1).
    - [ ] 2. Verificar que NO pueda ver la Materia 2 (propiedad de Profesor B).
    - [ ] 3. Verificar que solo pueda ver los alumnos inscritos en SU Materia 1.

### HU-011: Acceso Seguro (MFA)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Crítica
*   **Enlace Req**: [REQ-SEC-001]
*   **Descripción**:
    > **Como** CISO (Oficial de Seguridad),
    > **Quiero** requerir un segundo factor de autenticación para el login,
    > **Para** prevenir accesos no autorizados incluso si la contraseña es comprometida.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear un **Permission Set** llamado `Lumina_MFA_Access`.
    - [x] 2. Habilitar el permiso de sistema "**Multi-Factor Authentication for User Interface Logins**".
    - [x] 3. Asignar el **Permission Set** a los usuarios de prueba.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Intentar loguearse con un usuario que tenga el permiso MFA asignado.
    - [ ] 2. Verificar que el sistema solicite conectar Salesforce Authenticator (o código) antes de entrar.

### HU-012: Segregación de Funciones (FLS)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Alta
*   **Enlace Req**: [REQ-SEC-003]
*   **Descripción**:
    > **Como** Auditoría,
    > **Quiero** diferenciar qué roles pueden editar notas y qué roles pueden ver datos sensibles,
    > **Para** implementar una segregación de funciones (SoD) efectiva.
*   **⚙️ Pasos de Implementación (Admin Task)**:
    - [x] 1. Crear Profile: **Lumina Registrar**. Configurar `Final_Grade__c` como **Read-Only**.
    - [x] 2. Crear Profile: **Lumina Professor**. Configurar `Final_Grade__c` como **Edit**.
    - [x] 3. Configurar Profile: Remover **Read Access** para `National_ID__c` y `Phone` en el perfil Professor.
*   **✅ Criterios de Aceptación (QA Check)**:
    - [ ] 1. Loguearse como "Registrar" y verificar que, aunque vea la nota, el campo esté grisado (no editable).
    - [ ] 2. Loguearse como "Professor", entrar a un alumno, y verificar que los campos DNI y Teléfono no sean visibles (ocultos).

---

## 📚 Glosario Técnico (Salesforce Terms)

| Término (Inglés) | Definición (Español) |
| :--- | :--- |
| **Junction Object** | Objeto "conector" que permite relacionar dos objetos entre sí (Relación Muchos a Muchos). Ej: *Inscripción* une *Alumno* y *Materia*. |
| **Master-Detail Relationship** | Relación padre-hijo fuerte. El registro hijo ("Detail") depende totalmente del padre ("Master"). Si borras el padre, se borran los hijos. |
| **Organization-Wide Defaults (OWD)** | Configuración de seguridad base ("El Piso"). Define si los registros son Públicos o Privados por defecto. |
| **Field-Level Security (FLS)** | Configuración de visibilidad a nivel de campo. Permite ocultar campos sensibles (como DNI) a ciertos perfiles. |
| **Roll-Up Summary** | Campo especial en el objeto Padre que calcula valores de los hijos (Suma, Cuenta, Mínimo, Máximo). Ej: Contar clases presentes. |
| **Validation Rule** | Regla lógica ("Semáforo") que impide guardar un registro si los datos no cumplen cierto criterio (ej: Nota negativa). |
| **Permission Set** | Conjunto de permisos extra que se asignan a un usuario ("Llave extra"). Sirve para dar accesos puntuales (ej: MFA) sin cambiar el Perfil. |
| **External ID** | Atributo de un campo que lo marca como identificador único para integraciones. Facilita la carga masiva de datos (Data Import). |
| **Sharing Rule** | Regla de excepción para "abrir" la seguridad. Permite compartir registros privados con usuarios específicos bajo ciertas condiciones. |

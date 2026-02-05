# 📋 Guía Passo a Paso: Configuración de Trello - Sprint 1 (Full Scope)

Esta guía te ayudará a configurar el tablero de gestión de proyectos para **Lumina Tech**, garantizando que refleje el 100% del trabajo realizado en los 4 días del Sprint Inicial.

---

## 🎯 Objetivo
Visualizar el flujo de trabajo completo, desde el Modelado de Datos (Día 1) hasta la Seguridad Avanzada (Día 4), totalizando **12 Historias de Usuario**.

---

## 🏗️ Paso 1: Configuración del Tablero

### 1.1 Crear Tablero
*   **Título**: `Lumina Tech - Sprint 1 (MVP)`.
*   **Visibilidad**: Espacio de Trabajo.

### 1.2 Definir Columnas (Organización Estricta)
Configura tu tablero con las siguientes 11 columnas, en este orden exacto:

1.  **Backlog** - Todas las historias de usuario identificadas
2.  **Sprint Backlog** - HU seleccionadas para el sprint actual
3.  **En Progreso** - Trabajo activo
4.  **SF Desarrollo** - Configuración en Sandbox
5.  **DevOps - Dev**
6.  **SF QA** - Pruebas internas
7.  **DevOps - QA**
8.  **Aprobación TL** - Revisión del Team Lead
9.  **DevOps - Prod**
10. **SF Producción** - Despliegue final
11. **Terminado** - Completado y validado

---

## 🏷️ Paso 2: Etiquetas (Categorías) - Semáforo
*   🔵 **Modelado** (Datos Core - Día 1)
*   🟢 **Branding** (UI/UX - Día 2)
*   🟣 **Data Quality** (Validaciones - Día 3)
*   🔴 **Seguridad** (Accesos - Día 4)

---

## 🃏 Paso 3: Carga de Historias de Usuario (Backlog Consolidado)

Copia estas tarjetas en tu columna **Sprint Backlog**.

### 📅 DÍA 1: Cimientos de Datos (🔵 Modelado)

**HU-001: Gestión de Inscripciones (Recursantes)**
```markdown
**Como**: Director Académico.
**Quiero**: vincular alumnos a materias permitiendo recursadas (historial).
**Para**: tener una trazabilidad completa del desempeño del alumno a lo largo del tiempo.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Crear un **Custom Object** llamado **Enrollment** (`Enrollment__c`).
- [ ] 2. Crear un campo tipo **Master-Detail Relationship** hacia **Student** (`Student__c`).
- [ ] 3. Crear un campo tipo **Master-Detail Relationship** hacia **Subject** (`Subject__c`).
- [ ] 4. Crear un campo **Picklist** llamado **Cycle** (`Cycle__c`).
- [ ] 5. Crear un campo **Picklist** llamado **Commission** (`Commission__c`).
- [ ] 6. Configurar la **Tab Visibility** en *Default On* solo para perfiles Admin/Director.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Verificar que se pueda crear un registro de Inscripción relacionando un Alumno y una Materia existente.
- [ ] 2. Verificar que se pueda seleccionar el Ciclo y la Comisión desde una lista desplegable.
- [ ] 3. Verificar que si se borra un Alumno, se borren sus inscripciones (Master-Detail).
```

**HU-002: Identidad Única del Alumno**
```markdown
**Como**: Sistema de Gestión.
**Quiero**: identificar unívocamente a cada estudiante mediante ID y Documento.
**Para**: asegurar la integridad de los datos y evitar registros duplicados.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Configurar el **Record Name** con formato **Auto-Number** `A-{YYYY}-{0000}`.
- [ ] 2. Crear un campo **Text** llamado **National ID** (`National_ID__c`).
- [ ] 3. Habilitar el atributo **Unique** (Case Insensitive) en el campo.
- [ ] 4. Habilitar el atributo **External ID** en el campo.
- [ ] 5. Crear una **Validation Rule** para forzar formato numérico de 8 dígitos.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Crear un Alumno y verificar que el ID se genere automáticamente (ej. A-2024-0001).
- [ ] 2. Intentar crear dos alumnos con el mismo National ID; el sistema debe impedirlo.
- [ ] 3. Intentar ingresar un National ID con letras o menos de 8 dígitos; el sistema debe impedirlo.
```

**HU-003: Integridad de Notas y Auditoría**
```markdown
**Como**: Administrativo de Actas.
**Quiero**: guardar notas con precisión decimal y auditoría de cambios.
**Para**: garantizar la transparencia académica y prevenir fraudes.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Crear un campo **Number** llamado **Final Grade** (`Final_Grade__c`) con precisión `(4,2)`.
- [ ] 2. Crear un campo **Picklist** llamado **Status** (`Status__c`) con valores Passed/Failed/Enrolled.
- [ ] 3. Crear una **Validation Rule** llamada `Grade_Range_1_10` (Fórmula: `OR(Grade < 1, Grade > 10)`).
- [ ] 4. Habilitar **Field History Tracking** para el campo `Final_Grade__c`.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Ingresar una nota de 8.55 y verificar que se guarde correctamente.
- [ ] 2. Intentar ingresar una nota de 11 o -1; el sistema debe mostrar error.
- [ ] 3. Modificar una nota existente y verificar que el cambio aparezca en el historial (Field History).
```

### 📅 DÍA 2: Identidad e Interfaz (🟢 Branding)

**HU-004: Dominio Seguro**
```markdown
**Como**: Usuario Institucional.
**Quiero**: ver una URL segura y personalizada (lumina-university).
**Para**: tener confianza de que estoy navegando en el sitio oficial.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Desplegar **My Domain** con el nombre `lumina-university`.
- [ ] 2. Desplegar la configuración a los usuarios (**Deploy to Users**).
- [ ] 3. Configurar el logo oficial en la **Login Page**.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Verificar que la URL del navegador comience con `lumina-university.my.salesforce.com`.
- [ ] 2. Verificar que la pantalla de Login muestre el logo de Lumina Tech.
```

**HU-005: Identidad Institucional**
```markdown
**Como**: Equipo de Rectoría.
**Quiero**: ver los colores y logo oficiales en la aplicación.
**Para**: reforzar la identidad y pertenencia institucional.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Crear un **Theme & Branding** llamado "Lumina Official".
- [ ] 2. Configurar el **Brand Color** con el valor `#005A9C` (Azul Lumina).
- [ ] 3. Configurar el **Page Background Color** con `#F3F3F3` (Gris Claro).

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Verificar que la barra de navegación sea de color Azul Lumina `#005A9C`.
- [ ] 2. Verificar que el fondo de página sea gris claro y no blanco por defecto.
```

**HU-006: App de Gestión Central**
```markdown
**Como**: Usuario.
**Quiero**: tener un lanzador de aplicaciones dedicado a la gestión académica.
**Para**: acceder rápidamente a Alumnos, Materias e Inscripciones sin distracciones.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Crear una **Lightning App** llamada "Gestión Académica" (`Lumina_Academic`).
- [ ] 2. Añadir los **Navigation Items**: **Students**, **Subjects**, **Enrollments**.
- [ ] 3. Asignar la App a los Perfiles: **System Administrator** y **Standard User**.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Buscar "Gestión Académica" en el App Launcher y acceder.
- [ ] 2. Verificar que las pestañas sean exclusivamente Students, Subjects y Enrollments (sin basura extra).
```

### 📅 DÍA 3: Calidad y Automatización (🟣 Data Quality)

**HU-007: Validación de Contactos (Email)**
```markdown
**Como**: Departamento de Marketing.
**Quiero**: impedir el registro de correos que no sean institucionales.
**Para**: asegurar que las comunicaciones oficiales lleguen correctamente.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Crear una **Validation Rule** llamada `Valid_Institutional_Email` en el objeto **Student**.
- [ ] 2. Implementar lógica **REGEX** para forzar el dominio `@lumina.edu`.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Intentar registrar `usuario@gmail.com`; el sistema debe rechazarlo.
- [ ] 2. Registrar `usuario@lumina.edu`; el sistema debe aceptarlo exitosamente.
```

**HU-008: Integridad Numérica (Hard Validation)**
```markdown
**Como**: Sistema.
**Quiero**: bloquear automáticamente el ingreso de notas ilógicas.
**Para**: mantener la calidad de los datos y evitar errores de tipeo.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Verificar existencia de la **Validation Rule** `Grade_Range_1_10` en **Enrollment**.
- [ ] 2. Verificar que el **Error Message** esté en Inglés ("Invalid Grade...").

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Verificar que al ingresar nota 15, aparezca el mensaje de error en inglés: "Invalid Grade...".
- [ ] 2. Verificar que permita ingresar nota 1.00 y 10.00.
```

**HU-009: Control de Asistencias (Automatización)**
```markdown
**Como**: Preceptor.
**Quiero**: identificar automáticamente a los alumnos "Libres" (<75% asistencia).
**Para**: intervenir tempranamente sin realizar cálculos manuales.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Crear campo **Number** llamado **Classes Attended** (`Classes_Attended__c`).
- [ ] 2. Crear campo **Number** llamado **Total Classes** (`Total_Classes__c`).
- [ ] 3. Crear campo **Formula** (Percent) llamado **Attendance %** (`Attendance_Percentage__c`).
- [ ] 4. Crear campo **Formula** (Text) llamado **Academic Condition** (`Academic_Condition__c`) con lógica `< 0.75`.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Ingresar 5 clases asistidas de 10 totales.
- [ ] 2. Verificar que el % de Asistencia se calcule automáticamente en 50%.
- [ ] 3. Verificar que la Condición Académica muestre el texto (o semáforo/mensaje) correspondiente a "Libre".
```

### 📅 DÍA 4: Seguridad Zero Trust (🔴 Seguridad)

**HU-010: Matriz de Visibilidad (Comisiones)**
```markdown
**Como**: Profesor.
**Quiero**: ver solo las notas y alumnos de MIS comisiones asignadas.
**Para**: proteger la privacidad de los estudiantes de otros cursos.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Configurar **Organization-Wide Defaults (OWD)** de **Subject** como **Private**.
- [ ] 2. Verificar que el **OWD** de **Enrollment** sea **Controlled by Parent**.
- [ ] 3. Crear una **Sharing Rule** (Criteria-Based) para compartir registros con el Owner/Profesor.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Loguearse como Profesor A (Propietario de Materia 1).
- [ ] 2. Verificar que NO pueda ver la Materia 2 (propiedad de Profesor B).
- [ ] 3. Verificar que solo pueda ver los alumnos inscriptos en SU Materia 1.
```

**HU-011: Acceso Seguro (MFA)**
```markdown
**Como**: CISO (Oficial de Seguridad).
**Quiero**: requerir un segundo factor de autenticación para el login.
**Para**: prevenir accesos no autorizados incluso si la contraseña es comprometida.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Crear un **Permission Set** llamado `Lumina_MFA_Access`.
- [ ] 2. Habilitar el permiso de sistema "**Multi-Factor Authentication for User Interface Logins**".
- [ ] 3. Asignar el **Permission Set** a los usuarios de prueba.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Intentar loguearse con un usuario que tenga el permiso MFA asignado.
- [ ] 2. Verificar que el sistema solicite conectar Salesforce Authenticator (o código) antes de entrar.
```

**HU-012: Segregación de Funciones (FLS)**
```markdown
**Como**: Auditoría.
**Quiero**: diferenciar qué roles pueden editar notas y qué roles pueden ver datos sensibles.
**Para**: implementar una segregación de funciones (SoD) efectiva.
---
**⚙️ Pasos de Implementación (Admin Task)**:
- [ ] 1. Crear Profile: **Lumina Registrar**. Configurar `Final_Grade__c` como **Read-Only**.
- [ ] 2. Crear Profile: **Lumina Professor**. Configurar `Final_Grade__c` como **Edit**.
- [ ] 3. Configurar Profile: Remover **Read Access** para `National_ID__c` y `Phone` en el perfil Professor.

**✅ Criterios de Aceptación (QA Check)**:
- [ ] 1. Loguearse como "Registrar" y verificar que, aunque vea la nota, el campo esté grisado (no editable).
- [ ] 2. Loguearse como "Professor", entrar a un alumno, y verificar que los campos DNI y Teléfono no sean visibles (ocultos).
```

---

## 🚀 Protip: Simulación de Sprint
Al cargar estas tarjetas, mueve todas a **Sprint Backlog**.
Luego, simula el paso de los días moviendo de a 3 tarjetas a **Done**.
¡Así verás cómo "quema" el Sprint (Burndown Chart)!

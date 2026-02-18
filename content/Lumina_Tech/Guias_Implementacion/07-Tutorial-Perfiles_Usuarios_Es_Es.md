# 🎓 Guía Técnica: Perfiles y Usuarios (Seguridad)

**Sprint**: 01 (Fundamentos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-010], [HU-011]

---

## 🎯 Objetivo
Configurar los perfiles de seguridad para separar las funciones de **Profesor** (Calificar) y **Registrar/Bedel** (Inscribir), cumpliendo con el principio de Segregación de Funciones (SoD).

---

## 🛠️ Procedimiento

### Paso 1: Preparación de UI (Requerido)
*Para ver la pantalla igual que esta guía, activaremos la interfaz mejorada.*
1.  Ve a **Setup**.
2.  En el cuadro de búsqueda escribe **User Management Settings**.
3.  Busca la opción **Enhanced Profile User Interface**.
4.  Cámbiala a **Enabled** (Activado).

### Paso 2: Habilitar "Login as Any User" (Pruebas)
*Para poder probar la App como si fueras el Profesor o el Bedel.*
1.  Ve a **Setup**.
2.  Escribe **Login Access Policies**.
3.  Marca la casilla: ☑️ **Administrators Can Log in as Any User**.
4.  Haz clic en **Save**.

### Paso 3: Ajustar Campo DNI (Requisito Previo)
*Para ocultar el DNI al Profesor (HU-011), no puede ser obligatorio a nivel de base de datos.*
1.  Ve a **Object Manager** > **Alumno**.
2.  Ve a **Fields & Relationships** y haz clic en **DNI**.
3.  Haz clic en **Edit**.
4.  **Desmarca** la casilla ☑️ **Required** (Always require a value in this field...).
5.  Haz clic en **Save**.

### Paso 4: Creación Perfil Professor (Docente)
*Puede calificar y tomar asistencia. Solo ve lo necesario.*
1.  Ve a **Setup > Profiles**.
2.  Busca el perfil **Standard User** (o **Standard Platform User**) > **Clone**.
3.  Nombre: `Lumina Professor`. **Save**.
4.  **Object Settings**:
    *   **Inscripción**: ☑️ Read (Para ver alumnos inscritos). ☐ **Sin** Create/Edit/Delete.
    *   **Nota** y **Asistencia**: ☑️ Read, ☑️ Create, ☑️ Edit.
    *   **Carrera** y **Materia**: ☑️ Read.
    *   **Alumno**: ☑️ Read (Obligatorio por Master-Detail).
5.  **Field Permissions (FLS - Privacidad)**:
    *   En Objeto **Alumno**, busca `DNI`, `Teléfono`, `Email`.
    *   ☐ **Desmarca Read Access** (Ocultos). Solo debe ver el Nombre.

### Paso 5: Creación Perfil Registrar (Administrativo)
*Gestiona la matrícula, no académico.*
1.  Clone de **Standard User**. Nombre: `Lumina Registrar`.
2.  **Object Settings**:
    *   **Alumno**: ☑️ Read, ☑️ Create, ☑️ Edit.
    *   **Inscripción**: ☑️ Read, ☑️ Create, ☑️ Edit.
    *   **Carrera** y **Materia**: ☑️ Read (Para buscar al inscribir). ☐ **Sin** Edit.
    *   **Nota** y **Asistencia**: ☐ **Sin Acceso** (Ni siquiera Read).

### Paso 6: Creación Perfil Student (Auto-Inscripción)
*Destinado a alumnos que solo pueden matricularse a cursadas, sin ver notas ni asistencias.*
1.  Clone de **Standard User**. Nombre: `Lumina Student`.
2.  **Object Settings**:
    *   **Inscripción**: ☑️ Read, ☑️ Create. ☐ **Sin** Edit/Delete (Seguridad).
    *   **Carrera** y **Materia**: ☑️ Read.
    *   **Alumno**: ☑️ Read. ☐ **Sin** Edit (Salvo campos permitidos).
    *   **Nota** y **Asistencia**: ☐ **Sin Acceso**.
3.  **Field Permissions**:
    *   En **Inscripción**, asegúrate de que `Nota Final` y `Asistencia` estén ocultos (No Read).

### Verificación de Seguridad (Murallas)
1.  **Muralla 1 (Sharing)**: OWD de Alumno **Private**. El alumno solo ve su propio registro.
2.  **Muralla 2 (Validación)**: Regla en Inscripción para impedir inscribir a otros. (Ver Guía 09).
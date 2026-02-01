# 🎓 Guía Técnica: Seguridad Avanzada (Permissions)

**Sprint**: 01 (Fundamentos)
**Día**: 4 (Seguridad)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-009 (Visibilidad), HU-010 (MFA), HU-011 (FLS)

---

## 🎯 Objetivo
Configurar el modelo de seguridad "Zero Trust". Por defecto nadie ve nada, a menos que se le de permiso.

## 🛠️ Procedimiento

### Parte 1: Organization-Wide Defaults (OWD)
*Define el nivel base de acceso. "El piso".*

1.  **Setup > Sharing Settings**.
2.  Click **Edit** (Botón gris arriba).
3.  Busca el objeto **Alumno**.
4.  Cambia "Default Internal Access" a **Private**.
    *   *Significado*: Yo solo veo mis propios registros. No veo los de otros.
5.  Busca **Carrera** y **Materia**.
6.  Cambia a **Public Read Only**.
    *   *Significado*: Todos pueden ver las carreras, pero solo el Admin puede editarlas.
7.  **Save**. (Salesforce tardará unos minutos recálculando).

### Parte 2: Perfiles (SoD - HU-011)
*Separamos funciones: Bedelía inscribe, Profesores califican.*

#### Perfil Profesor
1.  **Setup > Profiles** > Clone **Standard User** > `Lumina Profesor`.
2.  **Object Settings > Inscripción**.
    *   ☑️ Read, ☑️ Edit.
    *   **Field Permissions**: `Nota Final` -> ☑️ Edit.

#### Perfil Bedel (Administrativo)
1.  Clone **Standard User** > `Lumina Bedel`.
2.  **Object Settings > Inscripción**.
    *   ☑️ Read, ☑️ Create, ☑️ Edit.
    *   **Field Permissions**: `Nota Final` -> ☑️ **Read Access** (⚠️ Uncheck Edit).
    *   *Resultado*: El Bedel puede inscribir alumnos, pero NO puede ponerles nota.

### Parte 3: MFA Permission Set (HU-010)
1.  **Setup > Permission Sets > New**.
2.  Label: `Lumina_MFA_Access`.
3.  Click en **System Permissions** > **Edit**.
4.  Marca: ☑️ **Multi-Factor Authentication for User Interface Logins**.
5.  **Save**.

### Parte 4: Asignación a Usuarios
1.  **Setup > Users > New User**.
2.  Crea "Bedel Test". Perfil: `Lumina Bedel`.
3.  Crea "Profe Test". Perfil: `Lumina Profesor`.
4.  **Permission Set Assignments** > Asigna `Lumina_MFA_Access` a ambos (para simular, aunque en Dev no tengas app móvil).

---

## ✅ Verificación de Éxito (Login As)
1.  Loguéate como **Bedel Test**.
2.  Abre una Inscripción. Intenta cambiar la Nota.
    *   **Resultado**: El campo está bloqueado (Candado). ✅
3.  Loguéate como **Profe Test**.
    *   **Resultado**: Puedes editar la nota. ✅

¡Seguridad Militar Implementada! 🔐

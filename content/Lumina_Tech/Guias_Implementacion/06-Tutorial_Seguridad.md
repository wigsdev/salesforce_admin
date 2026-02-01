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

1.  Ve a **Setup** (engranaje) y busca **Sharing Settings** en la barra Quick Find.
2.  Haz clic en el botón gris **Edit** (ubicado arriba de la lista).
3.  Busca el objeto **Alumno**.
4.  Cambia la columna **Default Internal Access** a **Private**.
    *   *Significado*: Yo solo veo mis propios registros. No veo los de otros.
5.  Busca **Carrera** y **Materia**.
6.  Cambia a **Public Read Only**.
    *   *Significado*: Todos pueden ver las carreras, pero solo el Admin puede editarlas.
7.  Haz clic en **Save**. (Es posible que Salesforce envíe un email cuando termine de recalcular).

### Parte 2: Perfiles (SoD - HU-011)
*Separamos funciones: Bedelía inscribe, Profesores califican.*

#### Creación Perfil Profesor
1.  Ve a **Setup > Profiles**.
2.  Busca el perfil **Standard User**.
3.  Haz clic en **Clone**.
4.  Escribe el nombre: `Lumina Profesor`. Haz clic en **Save**.
5.  En la pantalla del perfil, haz clic en **Object Settings**.
6.  Busca y haz clic en **Inscripción**. Haz clic en **Edit**.
    *   En **Object Permissions**, marca: ☑️ Read, ☑️ Edit.
    *   En **Field Permissions**, busca `Nota Final` y asegúrate de que ☑️ **Edit Access** esté marcado.
    *   Haz clic en **Save**.

#### Creación Perfil Bedel (Administrativo)
1.  Vuelve a **Profiles**. Haz clic en **Standard User** > **Clone**.
2.  Nombre: `Lumina Bedel`. Haz clic en **Save**.
3.  Ve a **Object Settings** > **Inscripción** > **Edit**.
    *   En **Object Permissions**, marca: ☑️ Read, ☑️ Create, ☑️ Edit.
    *   En **Field Permissions** (¡Atención!):
        *   Busca `Nota Final`.
        *   **DESMARCA** la casilla **Edit Access**. (Solo debe quedar ☑️ Read Access).
    *   Haz clic en **Save**.
    *   *Resultado*: El Bedel puede inscribir alumnos, pero NO puede ponerles nota.

### Parte 3: MFA Permission Set (HU-010)
1.  Ve a **Setup** y busca **Permission Sets**.
2.  Haz clic en **New**.
3.  Label: `Lumina_MFA_Access`. Haz clic en **Save**.
4.  Haz clic en **System Permissions** (abajo en la sección System).
5.  Haz clic en **Edit**.
6.  Busca la opción: ☑️ **Multi-Factor Authentication for User Interface Logins**. (Puedes usar Ctrl+F para buscar "Multi-Factor").
7.  Haz clic en **Save**. Confirma el mensaje emergente si aparece.

### Parte 4: Asignación a Usuarios de Prueba
1.  Ve a **Setup > Users**.
2.  Haz clic en **New User**.
3.  Crea el usuario "Bedel Test":
    *   Last Name: `Test`. Alias: `btest`. Email: (tu email). Username: `bedel@lumina.test`.
    *   **Profile**: Selecciona `Lumina Bedel`.
    *   Haz clic en **Save**.
4.  Repite para "Profe Test" con perfil `Lumina Profesor`.
5.  Para asignar MFA:
    *   Ve a **Permission Sets**. Haz clic en `Lumina_MFA_Access`.
    *   Haz clic en **Manage Assignments**.
    *   Haz clic en **Add Assignments**.
    *   Selecciona a ambos usuarios (`Bedel Test` y `Profe Test`).
    *   Haz clic en **Assign** > **Done**.

---

## ✅ Verificación de Éxito (Login As)
1.  Ve a **Users**.
2.  Al lado de "Bedel Test", haz clic en **Login**.
3.  Abre una Inscripción existente. Intenta cambiar la Nota haciendo doble clic en el lápiz.
    *   **Resultado**: El campo está bloqueado (candado) o no permite edición. ✅
4.  Haz clic en **Log out as Bedel Test** (arriba).
5.  Loguéate como **Profe Test**.
    *   **Resultado**: Puedes editar la nota. ✅

¡Seguridad Militar Implementada correctamente! 🔐

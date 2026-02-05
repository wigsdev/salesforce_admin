# 🎓 Guía Técnica: Seguridad Avanzada (Permissions)

**Sprint**: 01 (Fundamentos)
**Día**: 4 (Seguridad)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-010](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Visibilidad), [HU-011](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (MFA), [HU-012](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (FLS)

---

## 🎯 Objetivo
Configurar el modelo de seguridad "Zero Trust". Por defecto nadie ve nada, a menos que se le de permiso.

## 🛠️ Procedimiento

### Parte 1: Organization-Wide Defaults (OWD)
*Define el nivel base de acceso. "El piso".*

1.  Ve a **Setup** (engranaje) y busca **Sharing Settings** en la barra Quick Find.
2.  Haz clic en el botón gris **Edit** (ubicado arriba de la lista).
3.  Busca el objeto **Student**.
4.  Cambia la columna **Default Internal Access** a **Private**.
    *   *Significado*: Yo solo veo mis propios registros. No veo los de otros.
5.  Busca **Career**. Cambia a **Public Read Only**.
6.  Busca **Subject** (Materia). Cambia a **Private**.
    *   *Significado*: Fundamental para HU-009. Un profesor solo verá las Materias (Comisiones) que le pertenezcan o se le compartan.
    *   *Nota*: El objeto **Enrollment** heredará esta privacidad "Controlled by Parent".
7.  Haz clic en **Save**.

### Parte 2: Perfiles (SoD - HU-011)
*Separamos funciones: Registrar inscribe, Professor califica.*

#### Creación Perfil Professor
1.  Ve a **Setup > Profiles**.
2.  Busca el perfil **Standard User**.
3.  Haz clic en **Clone**.
4.  Escribe el nombre: `Lumina Professor`. Haz clic en **Save**.
5.  En la pantalla del perfil, haz clic en **Object Settings**.
6.  Busca y haz clic en **Enrollment**. Haz clic en **Edit**.
    *   En **Object Permissions**, marca: ☑️ Read, ☑️ Edit.
    *   En **Field Permissions**, busca `Final Grade` y asegúrate de que ☑️ **Edit Access** esté marcado.
    *   *(Privacidad)*: Busca `National ID` y `Phone`. **DESMARCA** Read Access (o asegúrate de que esté vacío) para cumplir HU-011 estricto.
    *   Haz clic en **Save**.

#### Creación Perfil Registrar (Administrativo)
1.  Vuelve a **Profiles**. Haz clic en **Standard User** > **Clone**.
2.  Nombre: `Lumina Registrar`. Haz clic en **Save**.
3.  Ve a **Object Settings** > **Enrollment** > **Edit**.
    *   En **Object Permissions**, marca: ☑️ Read, ☑️ Create, ☑️ Edit.
    *   En **Field Permissions** (¡Atención!):
        *   Busca `Final Grade`.
        *   **DESMARCA** la casilla **Edit Access**. (Solo debe quedar ☑️ Read Access).
    *   Haz clic en **Save**.
    *   *Resultado*: El Registrar puede inscribir alumnos, pero NO puede ponerles nota.

### Parte 3: MFA Permission Set (HU-010)
1.  Ve a **Setup** y busca **Permission Sets**.
2.  Haz clic en **New**.
3.  Label: `Lumina_MFA_Access`. Haz clic en **Save**.
4.  Haz clic en **System Permissions** (abajo en la sección System).
5.  Haz clic en **Edit**.
6.  Busca la opción: ☑️ **Multi-Factor Authentication for User Interface Logins**.
7.  Haz clic en **Save**. Confirma el mensaje emergente si aparece.

### Parte 4: Asignación a Usuarios de Prueba
1.  Ve a **Setup > Users**.
2.  Haz clic en **New User**.
3.  Crea el usuario "Registrar Test":
    *   Last Name: `Test`. Alias: `rtest`. Email: (tu email). Username: `registrar@lumina.test`.
    *   **Profile**: Selecciona `Lumina Registrar`.
    *   Haz clic en **Save**.
4.  Repite para "Profe Test" con perfil `Lumina Professor`.
    *   *Tip*: Asigna a este profesor como **Owner** de un registro de Materia para probar la visibilidad.
5.  Para asignar MFA:
    *   Ve a **Permission Sets**. Haz clic en `Lumina_MFA_Access`.
    *   Haz clic en **Manage Assignments**.
    *   Haz clic en **Add Assignments**.
    *   Selecciona a ambos usuarios.
    *   Haz clic en **Assign** > **Done**.

### Parte 5: Sharing Rules (Visibilidad Comisiones HU-010)
*Si no usas Owners directos, puedes crear reglas.*
1.  Ve a **Sharing Settings**.
2.  Baja hasta **Subject Sharing Rules**.
3.  **New**.
4.  Label: `Share with Commission Owner`.
5.  Rule Type: **Based on Criteria**.
6.  Criteria: `Active` equals `True`.
7.  Share with: `Public Group: Professors` (Requiere crear grupo previo).
8.  Access Level: **Read Only** (o Read/Write si deben editar temario).
*(Para este Sprint, asignaremos el registro de Materia directamente al Profesor Owner para cumplir la privacidad).*

---

## 🧪 Parte 6: Estrategia de Testing (QA - HU-010, HU-011, HU-012)
*Simularemos la operación real con "Actores de Prueba".*

### 1. El Elenco (Test Users)
Necesitamos crear usuarios ficticios para validar las restricciones.

| Nombre Usuario | Perfil (Profile) | Objetivo de la Prueba |
| :--- | :--- | :--- |
| **Severus S.** | `Lumina Professor` | Valida **HU-010** (Visibilidad) y **HU-012** (No ver DNI). |
| **Dolores U.** | `Lumina Registrar` | Valida **HU-012** (Read-Only en Notas). |

### 2. Configuración de Actores
1.  Ve a **Users** > **New User**.
2.  Crea a **Severus Snape**:
    *   **Profile**: `Lumina Professor`.
    *   **Importante**: Asígnale como **Owner** de una Materia (ej: "Pociones").
3.  Crea a **Dolores Umbridge**:
    *   **Profile**: `Lumina Registrar`.
4.  Asigna el **Permission Set** `Lumina_MFA_Access` a ambos si deseas probar **HU-011**.

### 3. Guion de Pruebas (Script)

#### 🎭 Escenario A: Privacidad del Profesor (Severus)
1.  Haz clic en **Login** al lado de Severus.
2.  **Prueba de Visibilidad**: Ve a **Subjects**.
    *   **Esperado**: Solo debe ver "Pociones" (suya). NO debe ver materias de otros.
3.  **Prueba de Edición**: Entra a un **Enrollment** de "Pociones".
    *   **Esperado**: Puede editar `Final Grade`. ✅
4.  **Prueba de Datos Sensibles**: Ve al **Student** relacionado.
    *   **Esperado**: NO ve `National ID` ni `Phone`. 🙈

#### 🎭 Escenario B: Integridad Administrativa (Dolores)
1.  Haz **Login** como Dolores.
2.  **Prueba de Creación**: Crea un nuevo **Enrollment**.
    *   **Esperado**: Éxito. ✅
3.  **Prueba Read-Only**: Intenta modificar una `Final Grade` existente.
    *   **Esperado**: Campo bloqueado/grisado. ⛔

#### 🎭 Escenario C: Auditoría (Director/Admin)
1.  Loguéate como Admin.
2.  Ve a un Enrollment modificado por Severus.
3.  Revisa **Field History**.
    *   **Esperado**: "Changed Final Grade from X to Y by Severus Snape". 🕵️‍♂️

---
¡Seguridad Militar Implementada y Verificada! 🔐

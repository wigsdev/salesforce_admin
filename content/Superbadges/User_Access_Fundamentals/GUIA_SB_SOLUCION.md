# Guía de Solución: User Access Fundamentals Superbadge

## 🚀 Reto 1: Marketing Integration User Setup

### Paso 1: Crear el Perfil Personalizado
1.  Ve a **Setup > Profiles**.
2.  Busca el perfil **Minimum Access - Salesforce**.
3.  Haz clic en **Clone**.
4.  **Profile Name**: `Marketing Email Integration User`
5.  Haz clic en **Save**.
6.  Haz clic en **Edit** en el nuevo perfil.
7.  **Description**: `Profile for ThunderMail integration` (Obligatorio poner algo).
8.  Haz clic en **Save**.
9.  Haz clic en el nombre del perfil (`Marketing Email Integration User`) para entrar a su configuración.
10. Busca la sección **Login IP Ranges**.
11. Haz clic en **New**.
    *   **Start IP Address**: `13.108.0.0`
    *   **End IP Address**: `13.108.0.0`
    *   **Description**: `ThunderMail Server`
12. Haz clic en **Save**.

### Paso 2: Crear el Usuario de Integración
1.  Ve a **Setup > Users**.
2.  Haz clic en **New User**.
3.  Llena los datos:
    *   **First Name**: `Marketing Integration`
    *   **Last Name**: `User`
    *   **Email**: `marketingintegrationuser@cloudmouth.com`
    *   **Username**: `marketingintegrationuser.TUS_INICIALES_HOY@cloudmouth.com` (Asegúrate de que incluya "marketingintegrationuser").
    *   **User License**: `Salesforce`
    *   **Profile**: `Marketing Email Integration User`
4.  (Desmarca las casillas de generar contraseña para agilizar).
5.  Haz clic en **Save**.

### Paso 3: Crear el Objeto "Bulk Mail"
1.  Ve a **Setup > Object Manager**.
2.  Haz clic en **Create > Custom Object**.
3.  Llénalo con:
    *   **Label**: `Bulk Mail`
    *   **Plural Label**: `Bulk Mails`
    *   **Object Name**: `Bulk_Mail`
    *   **Description**: `Stores email campaign data` (Obligatorio).
    *   **Record Name**: `Bulk Mail Name` (Dejar como está).
    *   **Data Type**: `Text` (Dejar como está).
4.  Haz clic en **Save**.

### Paso 4: Crear Campos en Bulk Mail (¡Cuidado con la Visibilidad!)
En **Object Manager > Bulk Mail > Fields & Relationships**, crea estos 3 campos.

**Campo 1: Subject**
*   **Type**: Text
*   **Label**: `Subject`
*   **Length**: 255
*   **Description**: `Subject of the email`
*   **Field-Level Security (Paso Crítico)**:
    *   Haz clic en "Visible" en la cabecera para desmarcar todo.
    *   Marca Visible **SOLO** para System Administrator.
*   **Save & New**.

**Campo 2: Send Date**
*   **Type**: Date/Time
*   **Label**: `Send Date`
*   **Description**: `Date email was sent`
*   **Field-Level Security**:
    *   Marca Visible **SOLO** para System Administrator.
*   **Save & New**.

**Campo 3: Number of Recipients**
*   **Type**: Number
*   **Label**: `Number of Recipients`
*   **Length**: 18, Decimal Places: 0
*   **Description**: `Total recipients`
*   **Field-Level Security**:
    *   Marca Visible **SOLO** para System Administrator.
*   **Save**.

### Paso 5: Configuración de Uso Compartido (OWD)
1.  Ve a **Setup > Sharing Settings**.
2.  Haz clic en **Edit**.
3.  Busca el objeto **Bulk Mail**.
4.  Cambia **Default Internal Access** a: **Public Read Only**.
5.  Haz clic en **Save**.

---

## 🚀 Reto 2: Marketing Integration User Access

### Paso 1: Crear Permission Set
1.  Ve a **Setup > Permission Sets**.
2.  Haz clic en **New**.
    *   **Label**: `Marketing Email Integration User`
    *   **API Name**: `Marketing_Email_Integration_User` (Verificar exactitud).
    *   **Description**: `Permissions for integration user.`
    *   **License**: `None` (o Salesforce).
3.  Haz clic en **Save**.

### Paso 2: Configurar Permisos de Objetos (Object Settings)
Entra a **Object Settings** dentro del Permission Set y configura lo siguiente:

**A. Objeto: Contact (Contacto)**
*   **Object Permissions**: ✅ Read, ✅ Edit
*   **Field Permissions** (Aquí estaba el error de interpretación):
    *   Email: ✅ Read Access | ⬜ Edit Access (**NO MARCAR EDIT**)
    *   Lead Source: ✅ Read Access | ⬜ Edit Access (**NO MARCAR EDIT**)
    *   Email Opt Out: ✅ Read Access | ✅ Edit Access (**SÍ MARCAR EDIT**)

**B. Objeto: Lead (Candidato)**
*   **Object Permissions**: ✅ Read, ✅ Edit
*   **Field Permissions**:
    *   Email: ✅ Read Access | ⬜ Edit Access (**NO MARCAR EDIT**)
    *   Lead Source: ✅ Read Access | ⬜ Edit Access (**NO MARCAR EDIT**)
    *   Email Opt Out: ✅ Read Access | ✅ Edit Access (**SÍ MARCAR EDIT**)

**C. Objeto: Bulk Mail**
*   **Object Permissions**: ✅ Read, ✅ Create, ✅ Edit
*   **Field Permissions**:
    *   Number of Recipients: ✅ Read | ✅ Edit
    *   Send Date: ✅ Read | ✅ Edit
    *   Subject: ✅ Read | ✅ Edit

### Paso 3: Configurar Permisos del Sistema
1.  En el Permission Set, ve a **System Permissions**.
2.  Haz clic en **Edit**.
3.  Marca la casilla: ✅ **API Enabled**.
4.  Haz clic en **Save**.

### Paso 4: Asignar al Usuario
1.  En el Permission Set, haz clic en **Manage Assignments**.
2.  Haz clic en **Add Assignment**.
3.  Selecciona al usuario: `Marketing Integration User`.
4.  Haz clic en **Next > Assign**.

---

## 🚀 Reto 3: Additional User Access

### Paso 1: Crear Permission Set (Solo Lectura)
1.  Ve a **Setup > Permission Sets**.
2.  Haz clic en **New**.
    *   **Label**: `Bulk Mail Read Access`
    *   **API Name**: `Bulk_Mail_Read_Access`
    *   **Description**: `Read access for standard users.`
3.  Haz clic en **Save**.
4.  Ve a **Object Settings > Bulk Mail**.
5.  Haz clic en **Edit**.
    *   **Object Permissions**: ✅ **Read** (Solo Read, NO Edit, NO Create).
    *   **Field Permissions**:
        *   Number of Recipients: ✅ **Read Access** (NO Edit).
        *   Send Date: ✅ **Read Access** (NO Edit).
        *   Subject: ✅ **Read Access** (NO Edit).
6.  Haz clic en **Save**.

### Paso 2: Crear Permission Set Group
1.  Ve a **Setup > Permission Set Groups**.
2.  Haz clic en **New Permission Set Group**.
    *   **Label**: `All Users`
    *   **API Name**: `All_Users`
    *   **Description**: `Standard access bundle.`
3.  Haz clic en **Save**.
4.  Haz clic en **Permission Sets in Group**.
5.  Haz clic en **Add Permission Set**.
6.  Selecciona estos tres (3):
    *   ✅ `Bulk Mail Read Access` (El que creaste).
    *   ✅ `CRM User` (Estándar de Salesforce).
    *   ✅ `Standard Einstein Activity Capture` (Estándar de Salesforce).
7.  Haz clic en **Add**.
8.  Haz clic en **Done**.

---

## ✅ Pasos Finales
1.  Vuelve a la página del Superbadge en Trailhead.
2.  Haz clic en **Check Challenge** para el Reto 1.
3.  Haz clic en **Check Challenge** para el Reto 2 (Ahora debería pasar con la corrección de campos).
4.  Haz clic en **Check Challenge** para el Reto 3.
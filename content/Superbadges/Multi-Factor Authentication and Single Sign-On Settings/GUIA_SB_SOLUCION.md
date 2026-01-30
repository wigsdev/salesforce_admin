# 🏆 Guía de Solución: Multi-Factor Authentication & SSO Settings Superbadge

## 🚨 Paso 0: Preparación de la Organización (Crucial)
Antes de empezar los retos, debes configurar los usuarios en la Special Developer Edition Org.

1. Inicia sesión en tu org especial.
2. Ve a **Setup** > **Users** > **Users**.

### Configurar a Murphy Jean:
1. Edita el usuario.
2. Cambia el **Email** a tu correo real.
3. Marca la casilla: **Generate new password and notify user immediately**.
4. Guarda y anota su Username.

### Configurar a Brochan Pane:
1. Edita el usuario.
2. Cambia el **Email** a tu correo real.
3. Marca la casilla: **Generate new password...**
4. Guarda y anota su Username.

**Establecer Contraseñas:** Revisa tu bandeja de entrada y crea las contraseñas para ambos usuarios.

---

## 🔹 Reto 1: Configuración de Single Sign-On (SSO)

### 1. Activar el Motor SAML (El paso secreto)
Sin esto, los permisos de SSO no aparecen.

1. Ve a **Setup** > **Single Sign-On Settings**.
2. Haz clic en **Edit**.
3. Marca la casilla **SAML Enabled**.
4. (Opcional) Si aparece, marca también **Delegated Authentication**.
5. Haz clic en **Save**.

### 2. Crear Permission Set para SSO
1. Ve a **Setup** > **Permission Sets**.
2. Haz clic en **New**.
    * **Label:** `Single Sign-On`
    * **API Name:** `Single_Sign_On`
    * ⚠️ **License:** Selecciona `--None--` (Dejar en blanco es vital).
3. Haz clic en **Save**.
4. Ve a **System Permissions** > **Edit**.
5. Busca y marca: `Is Single Sign-On Enabled`.
6. Haz clic en **Save**.
7. Haz clic en **Manage Assignments** > **Add Assignment**.
8. Asigna este permiso al usuario **Murphy Jean**.

### 3. Configurar Federation ID
1. Ve a **Setup** > **Users** > **Users**.
2. Edita a **Murphy Jean**.
3. En la sección **Single Sign On Information**, campo **Federation ID**, escribe:
    * **Valor:** `murphy_sso`
4. Haz clic en **Save**.

### 4. Configurar SAML (Axiom & Salesforce)
1. Abre una nueva pestaña: **Axiom Heroku**.
2. Ve a **SAML Identity Provider & Tester**.
3. Haz clic en **Download the Identity Provider Certificate** (Guarda el archivo).
4. Vuelve a Salesforce (**Setup** > **Single Sign-On Settings**).
5. En **SAML Single Sign-On Settings**, haz clic en **New**.
6. Completa el formulario:
    * **Name:** `Axiom SSO Test`
    * **Issuer:** `https://axiomsso.herokuapp.com`
    * **Identity Provider Certificate:** Sube el archivo descargado.
    * **Request Signature Method:** `RSA-SHA1`
    * **SAML Identity Type:** Assertion contains the Federation ID from the User object
    * **SAML Identity Location:** Identity is in the NameIdentifier element of the Subject statement
    * **Identity Provider Login URL:** `https://axiomsso.herokuapp.com/RequestSamlResponse.action`
    * **Entity ID:** Copia la URL de tu dominio (ej: `https://tu-org-dev-ed.my.salesforce.com`). **IMPORTANTE:** Sin barra `/` al final.
7. Haz clic en **Save**.
8. **Copiar URL:** En la sección **Endpoints** (abajo), copia la **Login URL**.

### 5. Configurar My Domain y Restricciones
1. Ve a **Setup** > **My Domain**.
2. En **Authentication Configuration**, haz clic en **Edit**.
3. Marca **Axiom SSO Test** (mantén marcado "Login Form" por ahora).
4. Haz clic en **Save**.

### Prueba de Fuego (Testing):
1. Ve a Axiom > **Generate a SAML Response**.
    * **SAML Version:** 2.0 (¡Importante!)
    * **Username or Federation ID:** `murphy_sso`
    * **Issuer:** `https://axiomsso.herokuapp.com`
    * **Recipient URL:** Pega la Login URL de Salesforce (la que termina en `?so=XXXX`).
    * **Entity ID:** Tu dominio (sin barra al final).
2. Clic en **Request SAML Response** > **Login**.
3. Debe iniciar sesión exitosamente como Murphy Jean.

### Bloquear Acceso Directo:
1. Vuelve a Salesforce como Admin.
2. Ve a **My Domain** > **Routing** > **Edit**.
3. Marca: **Prevent login from https://login.salesforce.com**.
4. Haz clic en **Save**.

---

## 🔹 Reto 2: MFA para Break Glass Admin

### 1. Crear Permission Set MFA
1. Ve a **Setup** > **Permission Sets** > **New**.
    * **Label:** `MFA Authorization for Break Glass Admin`
    * **API Name:** `MFA_Authorization_for_Break_Glass_Admin`
    * **License:** `--None--`
2. Ve a **System Permissions** > **Edit**.
3. Marca: `Multi-Factor Authentication for User Interface Logins`.
4. Haz clic en **Save**.
5. **Manage Assignments** > **Add Assignment**: Asigna a **Brochan Pane**.

---

## 🔹 Reto 3: Lightning Login

### 1. Activar Lightning Login (Global)
1. Ve a **Setup** > **Session Settings**.
2. Busca y marca la casilla: **Allow Lightning Login**.
3. Haz clic en **Save** (al final de la página).

### 2. Crear Permission Set Lightning Login
1. Ve a **Setup** > **Permission Sets** > **New**.
    * **Label:** `Lightning Login User`
    * **API Name:** `Lightning_Login_User`
    * **License:** `--None--`
2. Ve a **System Permissions** > **Edit**.
3. Marca: `Lightning Login User`.
4. Haz clic en **Save**.
5. **Manage Assignments** > **Add Assignment**: Asigna a **Brochan Pane**.

---

## 🔹 Reto 4: Prueba Móvil y Finalización

### 1. Conexión de App y Enrollment
Necesitarás la app **Salesforce Authenticator** en tu móvil.

1. Abre una ventana de **Incógnito/Privada**.
2. Ve a tu dominio e inicia sesión como **Brochan Pane** (Usuario y Contraseña).
3. Conecta la app usando la frase de dos palabras.
4. Una vez dentro, haz clic en el Avatar de Perfil > **Settings**.
5. Ve a **Advanced User Details**.
6. Busca el campo **Lightning Login** y haz clic en **Enroll**.
7. Aprueba la solicitud en tu móvil. (Debe aparecer un check verde ✅).

### 2. Prueba Final
1. Cierra sesión como Brochan.
2. En la pantalla de login, haz clic en el usuario **Brochan Pane** (que tendrá un icono de rayo ⚡).
3. Aprueba la entrada en el móvil (sin escribir contraseña).
4. Si entraste correctamente, cierra la ventana de incógnito.

---

## 🏁 Validación
Vuelve a Trailhead y haz clic en **Check Challenge**.
# 🏆 Guía de Solución: Multi-Factor Authentication & SSO Settings Superbadge

## 🚨 PASO 0: Preparación (Crucial)
**Basado en Video 1:** Si no haces esto, no podrás loguearte como los usuarios de prueba.

1. Regístrate en la Special Developer Edition Org (enlace en la sección "Sign Up" del reto).
2. Conecta la org a Trailhead.
3. Ve a **Setup** > **Users** > **Users**.

### Configura a Murphy Jean:
* **Email:** Tu correo real.
* **Marca:** Generate new password and notify user immediately.
* **Username:** Anótalo (no lo cambies).
* Haz clic en **Save**.

### Configura a Brochan Pane:
* **Email:** Tu correo real.
* **Marca:** Generate new password...
* **Username:** Anótalo.
* Haz clic en **Save**.

**Acción:** Ve a tu email, abre los correos de Salesforce y establece las contraseñas para ambos.

---

## 🔹 RETO 1: Single Sign-On (SSO)

### 1. Activar el Motor SAML (El "Paso Secreto")
Sin esto, el permiso "Is Single Sign-On Enabled" no aparecerá.

1. Ve a **Setup** > **Single Sign-On Settings**.
2. Haz clic en **Edit**.
3. Marca la casilla **SAML Enabled**.
4. (Opcional) Si aparece, marca **Delegated Authentication**.
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
7. Haz clic en **Manage Assignments** > **Add Assignment**: Asigna a **Murphy Jean**.

### 3. Configurar Federation ID
1. Ve a **Setup** > **Users** > **Users**.
2. Edita a **Murphy Jean**.
3. En la sección **Single Sign On Information**, campo **Federation ID**:
    * **Escribe:** `murphy_sso`
4. Haz clic en **Save**.

### 4. Configurar SAML (Axiom & Salesforce)
1. Abre **Axiom Heroku** en otra pestaña.
2. Ve a **SAML Identity Provider & Tester** > **Download Identity Provider Certificate**.
3. Vuelve a Salesforce (**Single Sign-On Settings**).
4. En **SAML Single Sign-On Settings**, haz clic en **New**.
5. Completa:
    * **Name:** `Axiom SSO Test`
    * **Issuer:** `https://axiomsso.herokuapp.com`
    * **Identity Provider Certificate:** Sube el archivo descargado.
    * **Request Signature Method:** `RSA-SHA1`
    * **SAML Identity Type:** Assertion contains the Federation ID from the User object
    * **SAML Identity Location:** Identity is in the NameIdentifier element of the Subject statement
    * **Identity Provider Login URL:** `https://axiomsso.herokuapp.com/RequestSamlResponse.action`
    * **Entity ID:** Tu dominio (ej: `https://midominio-dev-ed.my.salesforce.com`). **IMPORTANTE:** Sin barra `/` al final.
6. Haz clic en **Save**.
7. **Copiar URL Crítica:** En la sección **Endpoints** (abajo), copia la **Login URL**.
    * **Nota del Video:** Asegúrate de copiar la URL larga que termina con `?so=XXXXXXXX`.

### 5. Configurar My Domain y Restricciones
1. Ve a **Setup** > **My Domain**.
2. En **Authentication Configuration**, haz clic en **Edit**.
3. Marca **Axiom SSO Test** (mantén marcado "Login Form").
4. Haz clic en **Save**.

### Validación en Axiom:
1. Ve a Axiom > **Generate a SAML Response**.
    * **SAML Version:** 2.0 (¡Importante!)
    * **Username:** `murphy_sso`
    * **Issuer:** `https://axiomsso.herokuapp.com`
    * **Recipient URL:** Pega la Login URL de Salesforce (la larga).
    * **Entity ID:** Tu dominio (sin barra al final).
2. Clic en **Request SAML Response** > **Login**.
3. Debe entrar como **Murphy Jean**.

### Bloquear Acceso:
1. Vuelve a Admin Salesforce.
2. **My Domain** > **Routing** > **Edit**.
3. Marca: **Prevent login from https://login.salesforce.com**.
4. Haz clic en **Save**.

---

## 🔹 RETO 2: MFA para Break Glass Admin

### 1. Permission Set MFA
1. Ve a **Setup** > **Permission Sets** > **New**.
    * **Label:** `MFA Authorization for Break Glass Admin`
    * **API Name:** `MFA_Authorization_for_Break_Glass_Admin`
    * **License:** `--None--`
2. Ve a **System Permissions** > **Edit**.
3. Marca: `Multi-Factor Authentication for User Interface Logins`.
4. Haz clic en **Save**.
5. **Manage Assignments**: Asigna a **Brochan Pane**.

---

## 🔹 RETO 3: Lightning Login

### 1. Activar Lightning Login (Global)
**Basado en Video 5.**

1. Ve a **Setup** > **Session Settings**.
2. Busca y marca: **Allow Lightning Login**.
3. Haz clic en **Save** (al final de la página).

### 2. Permission Set Lightning Login
1. Ve a **Setup** > **Permission Sets** > **New**.
    * **Label:** `Lightning Login User`
    * **API Name:** `Lightning_Login_User`
    * **License:** `--None--`
2. Ve a **System Permissions** > **Edit**.
3. Marca: `Lightning Login User`.
4. Haz clic en **Save**.
5. **Manage Assignments**: Asigna a **Brochan Pane**.

---

## 🔹 RETO 4: Prueba Móvil (El Truco Final)

### 1. Conexión y "Enrollment" Manual
Este paso soluciona el error "We can't see that you tested..."

1. Abre una ventana de **Incógnito**.
2. Loguéate como **Brochan Pane** (Usuario y Contraseña).
3. Conecta la app **Salesforce Authenticator**.
4. Una vez dentro, haz clic en el **Avatar** > **Settings** > **Advanced User Details**.
5. Busca el campo **Lightning Login**.
6. Haz clic explícitamente en **Enroll** (Inscribirse).
7. Aprueba en el móvil. (Debe salir un check ✅).

### 2. La Prueba con "Remember Me"
**Truco extraído del Video 5.**

1. Cierra sesión con Brochan.
2. En la pantalla de login, escribe usuario y contraseña de Brochan pero **MARCA LA CASILLA "Remember Me"**.
3. Entra.
4. Cierra sesión de nuevo.
5. Ahora, haz clic en el usuario (que tendrá un rayito ⚡).
6. Aprueba en el móvil sin escribir contraseña.

---

## ✅ FIN
Vuelve a Trailhead y haz clic en **Check Challenge**. ¡Debe salir el confeti! 🎉
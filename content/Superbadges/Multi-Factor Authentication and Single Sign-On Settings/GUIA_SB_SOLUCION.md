🏆 Guía de Solución: Multi-Factor Authentication & SSO Settings Superbadge
🚨 Paso 0: Preparación de la Organización (Crucial)
Antes de empezar los retos, debes configurar los usuarios en la Special Developer Edition Org.

Inicia sesión en tu org especial.

Ve a Setup > Users > Users.

Configurar a Murphy Jean:

Edita el usuario.

Cambia el Email a tu correo real.

Marca la casilla: Generate new password and notify user immediately.

Guarda y anota su Username.

Configurar a Brochan Pane:

Edita el usuario.

Cambia el Email a tu correo real.

Marca la casilla: Generate new password....

Guarda y anota su Username.

Establecer Contraseñas: Revisa tu bandeja de entrada y crea las contraseñas para ambos usuarios.

🔹 Reto 1: Configuración de Single Sign-On (SSO)
1. Activar el Motor SAML (El paso secreto)
Sin esto, los permisos de SSO no aparecen.

Ve a Setup > Single Sign-On Settings.

Haz clic en Edit.

Marca la casilla SAML Enabled.

(Opcional) Si aparece, marca también Delegated Authentication.

Haz clic en Save.

2. Crear Permission Set para SSO
Ve a Setup > Permission Sets.

Haz clic en New.

Label: Single Sign-On

API Name: Single_Sign_On

⚠️ License: Selecciona --None-- (Dejar en blanco es vital).

Haz clic en Save.

Ve a System Permissions > Edit.

Busca y marca: Is Single Sign-On Enabled.

Haz clic en Save.

Haz clic en Manage Assignments > Add Assignment.

Asigna este permiso al usuario Murphy Jean.

3. Configurar Federation ID
Ve a Setup > Users > Users.

Edita a Murphy Jean.

En la sección Single Sign On Information, campo Federation ID, escribe:

Valor: murphy_sso

Haz clic en Save.

4. Configurar SAML (Axiom & Salesforce)
Abre una nueva pestaña: Axiom Heroku.

Ve a SAML Identity Provider & Tester.

Haz clic en Download the Identity Provider Certificate (Guarda el archivo).

Vuelve a Salesforce (Setup > Single Sign-On Settings).

En SAML Single Sign-On Settings, haz clic en New.

Completa el formulario:

Name: Axiom SSO Test

Issuer: https://axiomsso.herokuapp.com

Identity Provider Certificate: Sube el archivo descargado.

Request Signature Method: RSA-SHA1

SAML Identity Type: Assertion contains the Federation ID from the User object

SAML Identity Location: Identity is in the NameIdentifier element of the Subject statement

Identity Provider Login URL: https://axiomsso.herokuapp.com/RequestSamlResponse.action

Entity ID: Copia la URL de tu dominio (ej: https://tu-org-dev-ed.my.salesforce.com). IMPORTANTE: Sin barra / al final.

Haz clic en Save.

Copiar URL: En la sección Endpoints (abajo), copia la Login URL.

5. Configurar My Domain y Restricciones
Ve a Setup > My Domain.

En Authentication Configuration, haz clic en Edit.

Marca Axiom SSO Test (mantén marcado "Login Form" por ahora).

Haz clic en Save.

Prueba de Fuego (Testing):

Ve a Axiom > Generate a SAML Response.

SAML Version: 2.0 (¡Importante!)

Username or Federation ID: murphy_sso

Issuer: https://axiomsso.herokuapp.com

Recipient URL: Pega la Login URL de Salesforce (la que termina en ?so=XXXX).

Entity ID: Tu dominio (sin barra al final).

Clic en Request SAML Response > Login.

Debe iniciar sesión exitosamente como Murphy Jean.

Bloquear Acceso Directo:

Vuelve a Salesforce como Admin.

Ve a My Domain > Routing > Edit.

Marca: Prevent login from https://login.salesforce.com.

Haz clic en Save.

🔹 Reto 2: MFA para Break Glass Admin
1. Crear Permission Set MFA
Ve a Setup > Permission Sets > New.

Label: MFA Authorization for Break Glass Admin

API Name: MFA_Authorization_for_Break_Glass_Admin

License: --None--

Ve a System Permissions > Edit.

Marca: Multi-Factor Authentication for User Interface Logins.

Haz clic en Save.

Manage Assignments > Add Assignment: Asigna a Brochan Pane.

🔹 Reto 3: Lightning Login
1. Activar Lightning Login (Global)
Ve a Setup > Session Settings.

Busca y marca la casilla: Allow Lightning Login.

Haz clic en Save (al final de la página).

2. Crear Permission Set Lightning Login
Ve a Setup > Permission Sets > New.

Label: Lightning Login User

API Name: Lightning_Login_User

License: --None--

Ve a System Permissions > Edit.

Marca: Lightning Login User.

Haz clic en Save.

Manage Assignments > Add Assignment: Asigna a Brochan Pane.

🔹 Reto 4: Prueba Móvil y Finalización
1. Conexión de App y Enrollment
Necesitarás la app Salesforce Authenticator en tu móvil.

Abre una ventana de Incógnito/Privada.

Ve a tu dominio e inicia sesión como Brochan Pane (Usuario y Contraseña).

Conecta la app usando la frase de dos palabras.

Una vez dentro, haz clic en el Avatar de Perfil > Settings.

Ve a Advanced User Details.

Busca el campo Lightning Login y haz clic en Enroll.

Aprueba la solicitud en tu móvil. (Debe aparecer un check verde ✅).

2. Prueba Final
Cierra sesión como Brochan.

En la pantalla de login, haz clic en el usuario Brochan Pane (que tendrá un icono de rayo ⚡).

Aprueba la entrada en el móvil (sin escribir contraseña).

Si entraste correctamente, cierra la ventana de incógnito.

🏁 Validación
Vuelve a Trailhead y haz clic en Check Challenge.
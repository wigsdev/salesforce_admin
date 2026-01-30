# Salesforce Admin + Agent Force

## daily
*   ¿Cómo venimos?
*   ¿Algo nos bloquea?
*   ¿Cómo estamos?

---

# SUPERBADGE

> Guia: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol

## Superbadges: La Prueba de Fuego del Administrador

### ¿Qué es un Superbadge?
*   **No es un módulo normal**: Es una Credencial basada en Habilidades.
*   **Adiós a las instrucciones**: Aquí no existe el "Paso 1, haz clic aquí". Salesforce te da un Caso de Negocio (un problema real de una empresa ficticia) y tú debes decidir cómo resolverlo.
*   **Evaluación Automática**: Un "robot" entra a tu organización de Salesforce y verifica si la configuración funciona correctamente según los requisitos del cliente.

### ¿Por qué son vitales para tu carrera?
*   **El Puente Teórico-Práctico**: Los módulos te enseñan a usar el martillo; los Superbadges te piden construir una casa.
*   **Resume Booster (CV)**: Los reclutadores saben que un Superbadge no se consigue leyendo, se consigue haciendo. Valen mucho más que 100 badges normales.
*   **Prerrequisito de Certificación**: Para algunas certificaciones avanzadas, debes tener ciertos Superbadges completados.

---

# ¡SUPERBADGE!
Avanzamos con los trails.

## El Portero Digital: Dominando MFA y SSO

### ¿Qué es este Superbadge?
Este es el **User Authentication Settings Superbadge Unit**. Se enfoca exclusivamente en quién eres (Identidad) y cómo pruebas que eres tú (Autenticación).

### Por qué ahora: Salesforce ha hecho obligatorio el MFA (Multi-Factor Authentication).
Ya no es opcional; si no saben configurar esto, no pueden administrar una Org moderna.

### ¿Qué van a aprender?
1.  **MFA (Autenticación Multifactor)**:
    *   Aprenderán a no activarlo a nivel global (lo cual es un error de novato), sino a usar Permission Sets para activarlo quirúrgicamente para ciertos usuarios primero.
    *   Usarán la app Salesforce Authenticator.
2.  **SSO (Single Sign-On)**:
    *   Entenderán la magia de "Loguearse con Google/Outlook" pero aplicado a empresas.
    *   Configurarán Salesforce como un "Service Provider" que confía en un sistema externo (usarán una herramienta llamada Axiom para simular esto).
3.  **My Domain y Login Policy**:
    *   Cómo personalizar la URL de la empresa (miempresa.my.salesforce.com) y cómo obligar a los usuarios a que no puedan usar el login genérico de Salesforce, forzándolos a usar el SSO corporativo.

### Importancia en un Proyecto Real (Por Roles)
*   **Para el Business Analyst (BA)**: El BA debe definir la Experiencia de Usuario (UX). ¿Queremos que el usuario recuerde otra contraseña más? No. El BA define: "El usuario debe entrar con sus credenciales de Windows". Ustedes configuran el SSO para cumplir eso.
*   **Para el QA / Tester**: El terror del QA: "Login Loop". Aprenderán a testear que el SSO redirija correctamente. Si el SSO falla en Producción, es un incidente de Sev-1 (Severidad Máxima) porque nadie puede trabajar.
*   **Para el DevSecOps**: La seguridad perimetral. Aprenderán a bloquear intentos de login desde métodos inseguros y a auditar quién entró y cómo (Login History).

### Nivel de Dificultad y "El Miedo"
*   **Nivel**: Intermedio-Técnico.
*   **¿Por qué asusta?**: A diferencia de crear campos, aquí hay riesgo de bloqueo (Lockout).
*   **La complejidad**: Requiere configurar un XML (SAML) externo. Si copias y pegas mal un link o un certificado, no funciona y el error suele ser críptico ("Assertion Invalid"). Requiere precisión de cirujano.

### Tips de Supervivencia
*   **La Regla de Oro**: "Nunca te cierres la puerta con llave si estás adentro".
*   **Tip**: Siempre prueben el SSO en una ventana de Incógnito. Mantengan la sesión de Administrador abierta en el navegador normal. Si el SSO falla en incógnito, aún pueden arreglarlo desde la sesión abierta.
*   **La Herramienta Axiom**: Trailhead les pedirá usar una web app llamada "Axiom" para simular ser el proveedor de identidad. Tienen que seguir la guía al pie de la letra. Un espacio en blanco extra rompe todo.
*   **MFA no es para todos (en el reto)**: Lean bien los requisitos. El reto suele pedir activar MFA solo para un usuario específico (ej: Samantha Cordero), no para toda la Org. Si lo activan para todos, el Superbadge fallará.

---

## Puntos Críticos

### Reto 1: Single Sign-On (SSO) & My Domain
La mayor adversidad aquí es la invisibilidad de los permisos y el bloqueo de acceso.

**Configuración Crítica**:
*   **SAML Enabled**: Si no activas SAML en la organización antes de buscar los permisos, la casilla Is Single Sign-On Enabled simplemente no aparecerá en los Permission Sets.
*   **My Domain Policies**: El error más común es olvidar marcar Prevent login from https://login.salesforce.com. Sin esto, el sistema no considera que la seguridad está "cerrada".
*   **Federation ID**: El nombre de usuario en Axiom debe coincidir exactamente con el campo Federation ID en el registro del usuario en Salesforce, no con su Username.

### Reto 2: MFA & Lightning Login
Aquí es donde la mayoría de los alumnos se bloquean por las políticas de seguridad de contraseñas.

**Configuración Crítica**:
*   **Session Settings**: Antes de buscar el permiso de Lightning Login en un Permission Set, se debe habilitar Allow Lightning Login en la configuración de sesión de la Org.
*   **Security Levels**: Es vital mover Multi-Factor Authentication y Lightning Login a la columna de High Assurance en Session Security Levels para que Salesforce los reconozca como métodos válidos de alta seguridad.
*   **Evitar el "Password Lockout"**: Si fallan muchos intentos, la cuenta entra en un estado de Password Lockout que bloquea incluso el Lightning Login. El alumno debe saber ir al usuario y usar el botón Unlock para seguir probando.

### Reto 3: Break Glass Admin (Brochan Pane)
El obstáculo principal es validar el éxito sin tener la contraseña del usuario de prueba.

**Configuración Crítica**:
*   **Administrators Can Log In as Any User**: Esta política debe estar activa para poder "suplantar" a Brochan Pane y realizar el enrolamiento inicial de la App sin conocer su clave.
*   **Temporary Verification Code**: Ante la imposibilidad de resetear claves (error de 24hs), el código temporal es la única vía para conectar la App Salesforce Authenticator manualmente desde los Advanced User Details.
*   **El Test de Incógnito**: Trailhead no valida la configuración si no existe un registro de éxito en el Login History. El alumno debe cerrar sesión y entrar en una ventana de incógnito usando solo el nombre de usuario para que el sistema dispare la notificación al móvil. Si pide contraseña, el enrolamiento no fue exitoso.

### Email personal / Configurar bien / Buscar bien (CTRL + F)
> [Repetido como énfasis en el original]

---

# ¡SUPERBADGE!
Avanzamos con los trails.

**LINK Superbadge**

---

# Guardianes del Dato: Calidad y Validación

> "¿De qué sirve tener el CRM más potente del mundo si los datos son basura? El reporte dice que vendimos 1 millón, pero Finanzas dice que fueron 500 mil. ¿Por qué? Porque alguien escribió mal el monto o duplicó la oportunidad."

*   **El Rol**: En este Superbadge, ustedes dejan de ser solo "configuradores" para convertirse en Arquitectos de Calidad.
*   **Concepto clave**: Garbage In, Garbage Out. Su misión es evitar que la basura entre al sistema.

### Profundidad Técnica (Lo que van a configurar)

1.  **Validation Rules (La Barrera de Entrada)**:
    *   No son solo "campos obligatorios". Aprenderán lógica booleana compleja (AND, OR, NOT).
    *   **Funciones Críticas**: Usarán VLOOKUP (sí, en Salesforce existe y se usa para validar códigos postales o referencias cruzadas con objetos custom) y REGEX (Expresiones Regulares) para forzar formatos de texto (ej: que un número de seguridad social tenga el formato 999-99-9999).

2.  **Duplicate Management (El Detective)**:
    *   Diferencia técnica entre **Matching Rules** (El algoritmo que detecta: "¿Se parece 'Bob' a 'Robert'?") y **Duplicate Rules** (La acción: "¿Bloqueo al usuario o solo le aviso?").
    *   Aprenderán a configurar el "Fuzzy Matching" (coincidencia difusa).

3.  **Data Quality Fields**:
    *   Uso de fórmulas para "puntuar" un registro. Ej: Si tiene teléfono y email, el registro vale 100%. Si solo tiene nombre, vale 20%.

### Aplicación en Proyecto Real
*   **Para el Product Owner (PO)**: El PO define la regla de negocio: "No quiero que nadie cierre una venta si no ha puesto la fecha de contrato". El estudiante traduce eso a una Validation Rule.
*   **Para el QA / Tester**: Este es su campo de juego. Tienen que intentar "romper" la validación. Escenario: "Si la regla dice que el descuento no puede superar el 20%, el QA debe intentar guardar con 20.01% para ver si el sistema lo frena".
*   **Para el DevOps**: Cuidado con las cargas masivas de datos (Data Loader). Las Validation Rules y Duplicate Rules se disparan durante las importaciones. Si no las desactivan o gestionan bien, la carga fallará masivamente.

### Nivel de Dificultad y La "Trampa Lógica"
*   **Nivel**: Intermedio.
*   **La mayor dificultad técnica**: Escribir la fórmula de la regla de validación al revés. En Salesforce, la regla de validación define el ERROR, no el éxito.
*   **Ejemplo**: Si quieres que el campo sea obligatorio, la fórmula debe ser `ISBLANK(Campo)`. Muchos juniors escriben `NOT(ISBLANK(Campo))` pensando en "lo que está permitido", y eso hace que la regla falle. Tienen que pensar en "¿Qué condición hace que esto sea inválido?".

### Tips Técnicos para Aprobar
*   **Ojo con el ISCHANGED() y ISNEW()**: El reto les pedirá que una regla aplique sólo cuando se edita un registro, no cuando se crea (o viceversa). Si olvidan envolver su lógica en estas funciones, fallaran los tests.
*   **Picklists vs. Texto**: El Superbadge les enseñará a estandarizar. Convertir campos de texto libre (donde la gente escribe "EEUU", "USA", "E.U.A") en Picklists estandarizados. Esto es vital para los reportes.
*   **VLOOKUP es traicionero**: Solo funciona en el objeto Custom y verifica contra el Name. Es muy estricto. Recomendación: leer la documentación oficial de VLOOKUP antes de empezar.

### Después de completar el Superbadge
es **OBLIGATORIO** llenar el formulario.

1.  Cargar la imágen del SuperBadge
2.  Análisis de lo aprendido
3.  Llenar formulario de entrega

**SuperBadge SPRINT 1**
**Fecha Límite**: 16 de Enero

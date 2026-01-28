# Superbadge: User Authentication Settings - Enunciado Original

**Traducción literal del enunciado oficial de Trailhead**

---

## Lo que tendrá que hacer para ganar esta Superbadge

- Establecer políticas de contraseña apropiadas.
- Configurar requisitos y límites de inicio de sesión.
- Controlar el acceso API para aplicaciones conectadas.
- Establecer direcciones IP confiables para usuarios.

## Conceptos probados en esta Superbadge

- User Authentication (Autenticación de Usuario)

---

## Nota

Estamos trabajando arduamente para traerte contenido de superbadge actualizado que refleje mejoras de producto y mejores prácticas de la industria. Para completar este superbadge, trabajarás con aplicaciones conectadas, pero ten en cuenta que la recomendación actual es usar aplicaciones de cliente externo en lugar de aplicaciones conectadas siempre que sea posible. Para más información, consulta esta documentación de Ayuda.

---

## Preparación y Notas

### Registrarse en una Developer Edition Org con Configuración Especial

Para completar este superbadge, necesitas una Developer Edition org especial que contiene configuración especial y datos de muestra. Nota que esta Developer Edition org está diseñada para trabajar con los desafíos en este superbadge.

Regístrate para una Developer Edition org gratuita con configuración especial.

Llena el formulario. Para dirección de Email, ingresa una dirección de email activa.

Después de llenar el formulario, haz clic en Sign me up.

Cuando recibas el email de activación (esto puede tomar algunos minutos), ábrelo y haz clic en Verify Account.

Completa tu registro estableciendo tu contraseña y pregunta de desafío. Consejo: Guarda tu nombre de usuario, contraseña y URL de inicio de sesión en un lugar seguro—como un administrador de contraseñas—para acceso fácil después.

Has iniciado sesión en tu superbadge Developer Edition org.

Ahora, conecta tu nueva Developer Edition org a Trailhead.

Asegúrate de estar conectado a tu cuenta de Trailhead.

En la sección Challenge en la parte inferior de esta página, selecciona Connect Org de la lista de selección.

En la pantalla de inicio de sesión, ingresa el nombre de usuario y contraseña para la Developer Edition org que acabas de configurar.

En la página Allow Access?, haz clic en Allow.

En la página Want to connect this org for hands-on challenges?, haz clic en Yes! Save it. Eres redirigido de vuelta a la página Challenge y listo para usar tu nueva Developer Edition org para ganar este superbadge.

Ahora que tienes una org de Salesforce con configuración especial para este superbadge, estás listo para comenzar.

---

### Nota

Antes de comenzar los desafíos, por favor revisa User Authentication Superbadges: Trailhead Challenge Help.

Asegúrate de estar usando una nueva Developer Edition org de este enlace de registro para completar los desafíos en este superbadge. Si usas una org que ha sido usada para otro trabajo, no pasarás los desafíos en este superbadge.

---

## Caso de Uso

Cirrus Cash Flow es una startup que proporciona servicios financieros para sus clientes. Mientras su equipo de tecnología de la información (IT) es fantástico, la compañía estaba menos que lista para ser adquirida por el gigante de servicios financieros, Cumulus Global Bank. Cumulus Global Bank ha puesto los sistemas de Cirrus Cash Flow a través de una auditoría de seguridad exhaustiva y ahora necesita hacer cambios.

Como un consultor de seguridad de Salesforce premier, te has reunido con los stakeholders clave y compilado un conjunto comprensivo de requerimientos de cambios de seguridad.

---

## Requerimientos de Negocio

Esta sección representa la culminación de muchas reuniones y es la base de tu trabajo para transformar la org de Salesforce de Cirrus Cash Flow en una fortaleza basada en la nube.

### Requerimientos de Contraseña

Para cumplir con regulaciones financieras gubernamentales, Cumulus Global Bank tiene políticas de contraseña estrictas que están en línea con las mejores prácticas de la industria. Cirrus Cash Flow no ha modificado la configuración predeterminada con la que comenzó su org y necesitará hacer los siguientes ajustes.

- Las contraseñas tienen que tener al menos 12 caracteres de largo e incluir caracteres alfa, numéricos y especiales.
- Los usuarios solo tienen permitidos tres intentos de inicio de sesión. Después de eso, serán bloqueados de su cuenta por 30 minutos.
- Un usuario no puede restablecer su contraseña más de una vez en un período de 24 horas.
- La respuesta a la pregunta de seguridad de un usuario debe ser oscurecida durante el proceso de restablecimiento de contraseña.

> [!NOTE]
> **Interpretación**: Configurar Password Policies en Setup → Security → Password Policies. Ajustar: Minimum password length (12), Password complexity (alpha + numeric + special), Maximum invalid login attempts (3), Lockout effective period (30 minutes), Minimum password lifetime (1 day), Obscure secret answer for password resets (activar).

Además de las políticas de contraseña a nivel de org, Cumulus Global Bank requiere que los usuarios privilegiados tengan contraseñas aún más complejas. Después de revisar los usuarios de Cirrus Cash Flow, has determinado que aquellos con el perfil System Administrator son los únicos usuarios privilegiados en la org con niveles elevados de acceso. Para estos usuarios, has determinado que se necesitan hacer los siguientes cambios.

- Las contraseñas para usuarios admin necesitan ser de 15 caracteres mínimo.
- Las contraseñas para admins también tienen que ser más complejas—deben incluir números, letras mayúsculas y minúsculas, y caracteres especiales.

> [!NOTE]
> **Interpretación**: Crear Password Policy específica para el perfil System Administrator con: Minimum password length (15), Password complexity requirement (números + mayúsculas + minúsculas + caracteres especiales).

---

### Nota

Espera. ¿Dónde está la autenticación multifactor (MFA)?

Por sí solos, los nombres de usuario y contraseñas ya no proporcionan protección suficiente contra ciberataques. Ahí es donde entra MFA. Es una de las formas más simples y efectivas de prevenir acceso no autorizado a cuentas y salvaguardar tus datos y los datos de tus clientes. También es requerido para todos los usuarios de Salesforce desde el 1 de febrero de 2022.

De hecho, ¡MFA es tan importante que ha ganado su propio superbadge! Asegúrate de revisar el Multi-Factor Authentication and Single Sign-On Settings Superbadge para demostrar tu conjunto de habilidades de seguridad multifacéticas.

---

### Requisitos y Límites de Inicio de Sesión

Además de las políticas de contraseña, Cumulus Global Bank tiene restricciones de inicio de sesión para empleados que tienen acceso a la información más sensible. Has explorado estas restricciones en detalle y has determinado que se aplican a los representantes de Inside Sales y agentes de Call Center de Cirrus Cash Flow. Haz los siguientes cambios en los perfiles personalizados existentes.

| | Ubicación de Inicio de Sesión | Horas de Inicio de Sesión |
|---|---|---|
| **Inside Sales Representatives** | Oficina corporativa o la red privada virtual (VPN) cuando trabajan remotamente | Sin restricciones de tiempo |
| **Call Center Agents** | Oficina corporativa | Solo de 8 AM a 5 PM de lunes a viernes |

Usa la siguiente dirección IP o rango en tus configuraciones y asegúrate de establecer una descripción para el admin en Cirrus Cash Flow.

- **Corporate Office**: 13.108.0.0
- **VPN**: 22.0.0.1 - 22.0.255.0

Estas direcciones IP muy probablemente excluirán tu dirección IP actual.

> [!NOTE]
> **Interpretación**: Configurar Login IP Ranges y Login Hours en los perfiles personalizados:
> - **Inside Sales Representatives**: Agregar IP Ranges (13.108.0.0 y 22.0.0.1-22.0.255.0), sin restricciones de Login Hours.
> - **Call Center Agents**: Agregar IP Range (13.108.0.0), configurar Login Hours (Lunes-Viernes, 8:00 AM - 5:00 PM).

---

### Control de Acceso de Aplicaciones Conectadas

#### Nota

**Importante**: Asegúrate de haber conectado tu Developer Edition org especial para este superbadge a Trailhead antes de hacer cualquiera de las configuraciones en la siguiente sección. No hacerlo puede crear un obstáculo innecesario o bloquearte de completar el desafío exitosamente.

Las instrucciones para conectar tu org a Trailhead están en la parte superior de este superbadge, debajo de la sección Conceptos Probados.

---

Para sobrevivir en un panorama competitivo, las startups están obligadas a adaptarse y moverse rápidamente. Y como parte de esa mentalidad de "actuar rápido y pedir perdón después", el admin de la org de Salesforce de Cirrus Cash Flow no ha restringido ninguna aplicación conectada o los usuarios que tienen acceso a ellas. Como consultor experimentado, estás bien consciente del acceso que las aplicaciones conectadas pueden tener sin restricciones y que puede representar un riesgo de seguridad mayor. Pero no juzgas. En su lugar, ya has contactado a Salesforce Support para habilitar la característica API Access Control para que puedas tener un mejor manejo de los usuarios de API en la org.

Primero, Cumulus Global Bank ha pedido que el admin de Cirrus Cash Flow bloquee todas las aplicaciones conectadas. Solo otorga acceso API a aplicaciones conectadas en la lista de permitidos; el administrador tiene que aprobar el acceso de usuario a estas apps. Nunca permitas que los usuarios se auto-autoricen para ninguna aplicación conectada. Nota: La Trailhead Connected App ha sido preinstalada en tu org para este superbadge. No necesitas hacer ningún ajuste a esta app para pasar el desafío.

> [!NOTE]
> **Interpretación**: Configurar en Setup → Security → API Access Control:
> - Block all connected apps by default (bloquear todas las apps conectadas por defecto).
> - Admin approved users are required to access allowlisted apps (usuarios aprobados por admin son requeridos para acceder a apps en lista de permitidos).
> - Users cannot self-authorize (los usuarios no pueden auto-autorizarse).

La org de Cirrus Cash Flow ya tiene el paquete Salesforce Mobile Apps Administration instalado. Pero para cumplir con las políticas de seguridad móvil de Cumulus Global Bank, los únicos empleados permitidos para acceder a la org vía su dispositivo móvil son usuarios de Inside Sales. Dado que la compañía da a todos los empleados de Inside Sales el mismo modelo de teléfono, solo necesitan acceso a la aplicación conectada Salesforce for iOS.

> [!NOTE]
> **Interpretación**: En la configuración de Connected Apps, permitir acceso a "Salesforce for iOS" solo para usuarios con el perfil Inside Sales Representatives. Bloquear acceso a otras apps móviles.

---

### Red IP Confiable

¡Wow! Realmente has llevado a Cirrus Cash Flow a los estándares de autenticación de usuario de Cumulus Global Bank y mejores prácticas de la industria. ¡Bien hecho! Pero ahora, los empleados se están quejando de todos los pasos adicionales y restricciones.

No estás dispuesto a sacrificar seguridad por conveniencia, por supuesto. Sin embargo, sí conoces una forma de permitir a los empleados omitir la activación de dispositivo cuando inician sesión en la oficina corporativa. Ejecutas la solución con los expertos de seguridad de Cumulus Global Bank. Luego configuras la org de Cirrus Cash Flow para permitir a los usuarios iniciar sesión en la dirección IP corporativa (13.108.0.0) sin recibir un desafío de inicio de sesión para verificación de identidad.

> [!NOTE]
> **Interpretación**: Configurar Trusted IP Ranges en Setup → Security → Network Access → Trusted IP Ranges. Agregar la IP corporativa (13.108.0.0) para que los usuarios no reciban desafíos de verificación de identidad cuando inicien sesión desde esa ubicación.

---

**Grupo**: 3 - VISIONARY ADMINS  
**Fecha**: 17 Enero 2026

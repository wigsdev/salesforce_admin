Salesforce
Admin +
Agent Force

Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Técnicas (El "Qué" haces)
Gestión de Usuarios y Seguridad: El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
Gestión de Datos (Data Management): Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
Automatización Básica (Flows): Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
Reportes y Dashboards: Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.
AgentForce: puedas familiarizarte con la configuración de agentes dentro de Salesforce.
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Blandas (El "Cómo" lo haces)
Comunicación Traducida: Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
Resolución de Problemas (Google-Fu): No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
Mentalidad de Aprendiz (Learner's Mindset): Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
Atención al Detalle: Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

vamos a ver la segunda parte de modelado de datos… 



 Gestión de Relaciones: Cuentas y Contactos
Concepto: Las Cuentas y los Contactos son el corazón de Salesforce (el "Quién" y el "Dónde").

Objetivo: Entender cómo se estructuran las empresas y las personas que trabajan en ellas.



¿Qué es una Cuenta?
Definición: Organizaciones o empresas con las que haces negocios.
Tipos de Cuentas:
Cuentas de Empresa (B2B): Para vender a otras compañías.
Cuentas Personales (B2C): Para vender a individuos (requiere habilitación previa).
Dato clave: La Cuenta es el registro "Padre" en la jerarquía estándar.



 ¿Qué es un Contacto?
Definición: Las personas que trabajan en las Cuentas.
Relación: Un contacto debe estar vinculado a una cuenta para tener contexto empresarial.
Información clave: Email, cargo, nivel de influencia y relación directa.



Relaciones entre Registros
Contactos en múltiples cuentas: Cómo un consultor puede trabajar para varias empresas (Relaciones de Contactos con Cuentas).
Jerarquía de Cuentas: Uso del campo "Cuenta principal" para mostrar empresas matrices y subsidiarias (ej. Google Cloud dentro de Alphabet).
Roles de contacto: Definir quién es el "Decisor" o el "Influyente" en una oportunidad de venta.



Mejores Prácticas y Calidad de Datos
Reglas de Duplicados: La importancia de no crear la misma empresa dos veces.
Nomenclatura: Establecer convenciones (ej: "Nombre Empresa, Inc").
Actualización: Uso de herramientas para mantener los datos frescos (News, Social Accounts).
Propiedad del registro: Quién es el responsable de mantener la relació



💡 Tips para los Retos (Hands-on Challenge)
Nombres y API Names: Salesforce es sensible a las mayúsculas, minúsculas y espacios. Si el reto dice "Low Priority", no escribas "Low priority". Copia y pega siempre que sea posible.
El Playground Limpio: Si un reto falla y estás seguro de que está bien, intenta en un Trailhead Playground nuevo. Los restos de configuraciones de otros módulos pueden causar conflictos.
Idioma del Org: El Playground debe estar en Inglés. Muchos validadores de Trailhead buscan etiquetas específicas en inglés y fallan si encuentran "Cuenta" en lugar de "Account".
Verificación de Pasos Previos: Asegúrate de haber guardado los cambios en el registro antes de validar.



💡 Tips para el proyecto  
La Cuenta (Account): Es la entidad, la empresa, la organización o la institución con la que hacemos negocios. Es "el edificio".
El Contacto (Contact): Es la persona de carne y hueso con la que hablamos. Es "quien está dentro del edificio".
La Relación: Una Cuenta puede tener muchos Contactos, pero un Contacto suele pertenecer a una sola Cuenta principal. Estos dos objetos estándar son los cimientos; casi todos los objetos personalizados que ellos están creando van a terminar vinculándose a una Cuenta o a un Contacto.



💡 Tips para el proyecto Novabank (App Bancaria)
Objetivo: Aplicar el modelo al sector financiero B2B (Business to Business).
¿Quién es la Cuenta? Una empresa cliente que utiliza los servicios corporativos de Novabank (ej. Textil San Martín S.A. o Constructora El Sol).
¿Quiénes son los Contactos? Las personas autorizadas para operar en nombre de esa empresa. (ej. María López, Gerente de Finanzas; Juan Pérez, Tesorero).
Conexión con sus objetos personalizados: El objeto llamado Productos financieros, se relacionaría a la Cuenta (la empresa que debe el dinero), mientras que un objeto como Reclamo de Atención al Cliente podría ir vinculado al Contacto que llamó para quejarse.



💡 Tips para el proyecto  VitalCore (App de Farmacia)
Objetivo: Aplicar el modelo a la gestión de proveedores e instituciones de salud.
¿Quién es la Cuenta? En una farmacia grande, las Cuentas no suelen ser los pacientes (al menos no con el modelo estándar sin Person Accounts), sino los Laboratorios que los proveen (ej. Bayer, Pfizer) o las Clínicas/Obras Sociales con las que tienen convenios.
¿Quiénes son los Contactos? El Visitador Médico de un laboratorio, o el Auditor Médico de la obra social con el que VitalCore necesita comunicarse para validar recetas.
Conexión con sus objetos personalizados: Si tienen un objeto Pedido de Reposición de medicamentos, este se vincula a la Cuenta (el Laboratorio). Si tienen un objeto de Capacitación de Producto, se invita a un Contacto específico.



💡 Tips para el proyecto Lumina Tech (App Universitaria)
Objetivo: Aplicar el modelo al ámbito educativo e institucional.
¿Quién es la Cuenta? Colegios secundarios de donde reclutan alumnos (ej. Instituto Belgrano), o Empresas que ofrecen pasantías a los egresados (ej. Google, Accenture).
¿Quiénes son los Contactos? El Director o Tutor Orientador del colegio secundario, o el Líder de Recursos Humanos de la empresa de pasantías.
Conexión con sus objetos personalizados: Si Lumina Tech tiene un objeto llamado Feria de Carreras, pueden registrar qué Cuentas (Colegios) asistieron. Si tienen un objeto Oferta de Pasantía, se relaciona directamente con la Cuenta (Empresa) y el Contacto (Reclutador).



Práctica Profesional - PROYECTO

EQUIPOS
 Proyecto - Práctica

Si no está escrito, no existe:
 Los 4 Pilares de la Documentación

Description Field (Para el Admin): Cada vez que creen un Campo, un Flow o una Regla de Validación, llenen el campo Description.
Qué poner: "¿Para qué sirve esto?" y "¿Quién lo pidió?".
Ejemplo: "Calcula el descuento total. Solicitado por Gerencia de Ventas (Sprint 2)."
Help Text (Para el Usuario): El texto que aparece al pasar el mouse por el signo ?.
Qué poner: Instrucciones claras. Ej: "Ingrese el monto sin impuestos".

El Diccionario de Datos (Data Dictionary)
Un archivo vivo (Excel/Sheet) que lista todos los objetos y campos personalizados creados.
Columnas clave: Nombre del Campo (API Name), Tipo de Dato, Valores de Picklist, y ¿Es obligatorio?
¿Por qué? Para que cuando alguien nuevo entre al proyecto, no tenga que adivinar qué es Monto_X_Aux__c.

Diagramas de Flujo (Visualizar la Lógica)
Antes de hacer un Flow o una Automatización, dibújalo.
Herramientas: Lucidchart, Miro o papel y lápiz.
Meta: Entender el "Camino Feliz" (todo sale bien) y el "Camino de Error" (qué pasa si el usuario se equivoca).

Registro de Cambios (Changelog)
Una bitácora simple de modificaciones.
Formato: [Fecha] - [Autor] - [Qué cambió] - [Por qué].
Ejemplo: "10/Oct - Rebeca - Cambie la Regla de Validación de Precio porque Ventas actualizó la política."

DAILY
⚡ Daily (15 min): 

Qué hizo ayer
En que se va a trabajar hoy
Qué bloqueos hay


FECHAS LÍMITES
Terminar HU de DEV: Fecha Límite 18/2 

La HU se trabaja y testea en el ambiente de DEV
Una vez lista se pasa a la pestaña DevOps Dev
Rol: DevOps Specialist - Tester QA pasan las HU a QA

FECHAS LÍMITES

Pasar HU a QA: Fecha Límite: 18-19/2
	Se tiene que testear cada HU y dejar evidencia

Rol: DevOps Specialist - Tester QA pasan las HU a QA y dejan evidencia con Screen shot que el requerimiento pasó con éxito en el GESTOR DE VERSIONES
Si no pasó con éxito se pasa a una pestaña llamada BUG y le avisan a los SF Admin para que la revisen y la corrijan


FECHAS LÍMITES
APROBACIÓN para PROD: Fecha límite 23/2

Una vez que la evidencia ya fue dejada como exitosa de deja en la pestaña APROBACIÓN TL
Si el TL lo aprueba ya está listo para dejar en el ambiente PROD qué es dónde se dará la demo

FECHAS
SPRINT 1
Duración del Sprint: 12 - 15 días.
Hitos Clave:
🟢 02 Feb: Sprint Planning (HOY - Inicio).
🟡 17 Feb: Análisis de SPRINT 2
🚀 26 Feb: Demo (1er Entregable al Cliente).
🔴 02 Mar: Sprint Retrospective & Planning Sprint 2.

HOY

CIERRE DE SPRINT
SPRINT 1
Fecha: 17 de Febrero .
QA: Comenzamos a pasar y evidenciar los cambios.

¡Manos a la obra!

Vamos ingresar para mostrarles cómo se crea una organización práctica y que todos puedan crear una.
Indiquemos que investiguen la organización, que entren y revisen
link: https://trailhead.salesforce.com/es/users/profiles/orgs
Compartir pantalla para que vean como se hace el proceso

TAREAS DE HOY

GESTOR DE VERSIONES
Pasar HU a QA y Testear
Después de terminar el testeo pasar a la pestaña DevOps QA

Fecha de Finalización
Miércoles 18/2

GESTOR DE VERSIONES
Pasar HU a PROD y Testear
Después de terminar el testeo pasar a la pestaña DevOps PROD para aprobación
Luego Terminado

Fecha de Finalización
Miércoles 23/2

¿Cómo nos fué?¿Qué cosas no quedaron claras y necesitamos repasar la próxima?
retro




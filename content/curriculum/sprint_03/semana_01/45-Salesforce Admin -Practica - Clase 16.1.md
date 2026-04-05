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

TRAIL DE HOY
vamos a ver la segunda parte de modelado de datos… 



El Ecosistema más allá de la Empresa
Hasta ahora en el curso, hemos visto Salesforce para empleados internos (Ventas, Servicio).
Pero ninguna empresa opera sola. Dependemos de distribuidores, revendedores, agencias, socios de manufactura.

El problema de negocio: Estos socios necesitan información actualizada (leads, cuentas, inventario) para vender nuestros productos.
¿Cómo les damos acceso sin comprometer la seguridad de toda nuestra organización? No podemos simplemente "prestarles una contraseña".



La Solución - ¿Qué es Salesforce Experience Cloud?
Definición: Experience Cloud es la plataforma de Salesforce que permite crear sitios web, portales y foros de marca, conectados directamente a tu Org de Salesforce.

Es una "ventana controlada" hacia tu CRM.
No es una base de datos separada; los datos que se muestran en el sitio provienen de los mismos objetos estándar y personalizados que usan tus equipos internos.

Permite una experiencia personalizada (branding) diferente a la interfaz interna de Lightning.



El Caso de Uso Específico - El Portal de Partners (Socios)
Basado en el módulo de Trailhead que vamos a realizar: Nos enfocaremos en un "Partner Portal".
¿Para qué sirve? Para gestionar la relación con el canal de ventas indirectas.
¿Qué hacen los socios ahí?
Registrar Leads (clientes potenciales que ellos encuentran).
Ver y actualizar Oportunidades en las que están trabajando con nosotros.
Acceder a recursos de marketing o soporte.
El objetivo es facilitarles la venta de nuestros productos, dándoles autoservicio.



Concepto Crítico para Admins  
Tipos de Licencias de Usuario
¡Este es el punto más importante!
No todos los usuarios en Salesforce son iguales.
Usuarios Internos: Tienen licencias completas de Salesforce (Sales Cloud, Service Cloud). Ven mucho y hacen mucho.
Usuarios Externos (Partners): Usan licencias de "Comunidad" (Experience Cloud licenses). Son más económicas y, fundamentalmente, tienen acceso limitado a objetos y funcionalidades.
Un Admin debe saber qué licencia asignar según lo que el socio necesita hacer. No se debe dar acceso de más.



La Regla de Oro - Seguridad y "Sharing" (Visibilidad)
Cuando abres una ventana a tu CRM, el riesgo de seguridad aumenta.
El principio de "Mínimo Privilegio": Un partner nunca debe ver los datos de otro partner competidor, ni datos internos sensibles de la empresa.

La herramienta clave: Sharing Rules (Reglas de Uso Compartido) y Organization-Wide Defaults (OWD).
En el contexto de comunidades, usamos mecanismos externos de "sharing" para asegurar que el Socio A solo vea las Cuentas que "le pertenecen" o que le hemos asignado explícitamente. Si esto falla, es una brecha de seguridad grave.



El Rol del Administrador en este Proyecto
En el ejercicio práctico que harán, ustedes como Admins llevarán dos "sombreros":
El Constructor (Builder): Configurar la apariencia del sitio (usando plantillas como "Partner Central"), poner el logo, los menús. Es la parte visual.
El Guardián (Security): Configurar los perfiles, permisos y reglas de "sharing" para asegurar que los datos fluyan correctamente pero de forma segura.
El éxito no es solo que el sitio se vea "bonito", sino que sea funcional y seguro.



Resumen
Experience Cloud extiende el poder del CRM a personas fuera de nuestra nómina.
Los portales de Partners aceleran las ventas indirectas mediante la colaboración de datos en tiempo real.
La diferencia crítica es el tipo de usuario (licencia externa) y el modelo de seguridad (sharing externo).
Como Admins Jr., su prioridad número uno al configurar esto es siempre la seguridad de los datos.



Práctica Profesional - PROYECTO

EQUIPOS
 Proyecto - Práctica

CALENDARIO

ROLES - de 1 a 3 personas máximo

EQUIPOS

EQUIPOS
MÉTODO DE TRABAJO

ROLES DE ANÁLISIS
Concepto Central: Cada rol responde a una pregunta diferente dentro del proyecto: 

¿Qué? (BA), 
¿Cómo? (Consultant), 
y ¿Por qué/Cuándo? (PO).

ROLES DE ANÁLISIS
Product Owner (PO) - El "Visionario"
Enfoque: Define el valor del negocio y la prioridad.
Tareas Principales:
Es la "voz del cliente" dentro del equipo.
Gestiona el Product Backlog: decide qué historias de usuario son más importantes y qué se construye primero.
Acepta o rechaza el trabajo entregado por el equipo (User Acceptance).
Frase típica: "Esto es prioritario para el lanzamiento del Q3, lo demás puede esperar."
Business Analyst (BA) - El "Traductor"
Enfoque: Define el requerimiento detallado.
Tareas Principales:
Se sienta con los usuarios para entender sus procesos actuales y puntos de dolor.
Documenta los requerimientos funcionales (escribe las Historias de Usuario y Criterios de Aceptación).
Asegura que el equipo técnico entienda qué necesita el negocio sin ambigüedades.
Frase típica: "El usuario necesita que al cambiar el estado a 'Cerrada', se envíe un correo automáticamente."
Salesforce Consultant - El "Solucionador"
Enfoque: Define la solución técnica dentro de la plataforma.
Tareas Principales:
Toma el requerimiento del BA y decide cómo implementarlo usando las "Best Practices" de Salesforce.
Decide si se usa configuración estándar (Flows, Campos) o si se requiere código (Apex/LWC).
Evita la "sobre-ingeniería" y protege la salud de la Org a largo plazo.
Frase típica: "No necesitamos código para eso; podemos resolverlo con un Flow y una Regla de Validación."

ROLES
Como Administradores Junior, a menudo les tocará ponerse los tres sombreros a la vez. Sin embargo, entender la distinción les ayudará a saber 

cuándo están "recopilando requisitos" (BA), 
cuándo están "priorizando" (PO) 
y cuándo están "diseñando la solución" (Consultant).

TAREAS - 2/3 al 6/3 

QUÉ HACEMOS HOY?
1-DAILY 15 min registrar en el gestor de versiones
2-Trailhead del dia de la fecha y si queda tiempo, los atrasados
3-Grupo de analisis del dia HOY Equipo 2- Solo los roles de esta semana.


¡Manos a la obra!
Avanzamos con los trails.



¿Cómo nos fué?¿Qué cosas no quedaron claras y necesitamos repasar la próxima?
retro




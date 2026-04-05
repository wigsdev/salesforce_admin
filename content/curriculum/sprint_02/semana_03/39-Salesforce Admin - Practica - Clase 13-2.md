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



¿Qué es Copado? (El Concepto)
Definición directa: Es una plataforma de DevOps construida nativamente dentro de Salesforce.
El traductor: Actúa como un puente entre la gestión de proyectos (lo que el cliente pide) y el control de versiones (el código y los metadatos reales).
Para Admins y Devs: Permite aprovechar el poder de Git (historial, ramas, protección de código) usando clics en lugar de complejas líneas de comandos.



¿Para qué sirve? (El Problema vs. La Solución)
El dolor de los Change Sets: Son lentos, ciegos (no guardan historial de quién tocó qué y cuándo de forma eficiente) y provocan que los equipos se sobrescriban el trabajo.
Trazabilidad total: Sirve para empaquetar exactamente qué campos, flujos o clases de Apex se modificaron y atarlos a una "Historia de Usuario" específica.
Despliegues predecibles: Sirve para mover cambios entre entornos (Dev -> QA -> Producción) de forma automatizada y con pruebas de calidad obligatorias en el medio.



💡 Tips para los Retos (Preguntas)
El foco del Reto 1 (Por qué DevOps): Las respuestas correctas del módulo apuntan a las limitaciones de las herramientas nativas básicas (como los Change Sets). ¿El porqué? Porque Trailhead quiere que quede claro que sin control de versiones (Git), trabajar en equipo en Salesforce es un riesgo de pérdida de datos.
El foco del Reto 2 (La Historia de Usuario como centro): Las respuestas correctas refuerzan que el Commit (guardar el cambio) se hace desde la User Story. ¿El porqué? Para auditar. Si un flujo falla en Producción, Copado te permite ver exactamente en qué Historia de Usuario se creó, por qué el negocio lo pidió y qué Admin lo hizo.
El foco del Reto 3 (Calidad y CI/CD): Las respuestas apuntan a los Quality Gates (filtros de calidad) y la integración continua. ¿El porqué? Porque el objetivo final de DevOps no es solo desplegar rápido, sino desplegar seguro. Las respuestas buscan que se entienda que Copado automatiza las pruebas antes de dejar que un error llegue a los usuarios finales.



Práctica Profesional - PROYECTO

EQUIPOS
 Proyecto - Práctica

DAILY
⚡ Daily (15 min): 

Qué hizo ayer
En que se va a trabajar hoy
Qué bloqueos hay


ANOTAR ACTIVIDAD EN EXCEL

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

🟡 17 Feb: Análisis de SPRINT 2
🚀 26 Feb: Demo (1er Entregable al Cliente).
🔴 02 Mar: Sprint Retrospective & Planning Sprint 2.

HOY

CIERRE DE SPRINT
SPRINT 1
Fecha: 17 de Febrero .
QA: Comenzamos a pasar y evidenciar los cambios.
SPRINT 2- BA nuevos requerimientos

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




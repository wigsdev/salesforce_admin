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



Teoría y Visión (El "Qué" y el "Por Qué")

Del Chatbot al Agente (El cambio de paradigma):
Antes: Programábamos árboles de decisión rígidos (Si el usuario dice A, responde B).
Ahora (Agentforce): Definimos un "Rol" y le damos "Herramientas". El Agente razona cuál es la mejor respuesta. No sigue un guión lineal.
vamos a ver la segunda parte de modelado de datos… 



Teoría y Visión (El "Qué" y el "Por Qué")

El Motor de Razonamiento "Atlas":
Es el "cerebro". Cuando un usuario pide algo, Atlas evalúa: ¿Qué me piden? ¿Qué datos tengo? ¿Qué herramientas (Flows) puedo usar? Y luego construye un plan de acción.
Data Cloud es el Combustible:
Un agente sin datos es un mentiroso confiado.
Para que la IA funcione, necesitamos unificar datos de todas partes (Gmail, pedidos antiguos, web) en Data Cloud para que el Agente tenga "contexto total" del cliente.
vamos a ver la segunda parte de modelado de datos… 



Teoría y Visión (El "Qué" y el "Por Qué")

Grounding (Anclaje de Datos):
Concepto vital. Evitamos que la IA invente (alucinaciones) obligándola a basar sus respuestas únicamente en tus datos de confianza (artículos de conocimiento, registros de CRM).
Einstein Trust Layer (Capa de Confianza):
Seguridad: Los datos del cliente nunca se usan para entrenar el modelo público de IA (como ChatGPT).
Enmascaramiento: Si hay tarjetas de crédito o emails, Salesforce los oculta antes de enviarlos a la IA y los des-oculta al regresar.
vamos a ver la segunda parte de modelado de datos… 



Teoría y Visión (El "Qué" y el "Por Qué")

Human in the Loop (El Humano en el Bucle):
El Agente no reemplaza al humano; lo libera de lo aburrido.
Siempre debe haber un camino fácil para "escalar" a un agente humano si la IA se confunde o el tema es sensible.
Actions (Acciones) = Flows:
¿Cómo hace cosas el Agente? Ejecutando Flows y Apex.
Si sabes crear un Flow, ya sabes construir las "manos" de un Agente.
vamos a ver la segunda parte de modelado de datos… 



Teoría y Visión (El "Qué" y el "Por Qué")

Topics (Temas) en lugar de Intenciones:
Ya no entrenamos frases infinitas. Agrupamos capacidades en "Temas" (ej: "Gestión de Pedidos", "Soporte Técnico"). El Agente decide qué Tema activar según la conversación.
Prompt Engineering (Instrucciones):
Es el arte de decirle al Agente cómo comportarse. "Eres un asistente amable y conciso que ayuda a estudiantes". Las instrucciones claras definen la personalidad y los límites.
El Rol del Admin en la IA:
La IA no se configura sola. El Admin es quien conecta los datos, crea los Flows seguros, define los permisos y monitorea que el Agente no diga tonterías.
vamos a ver la segunda parte de modelado de datos… 



Práctica Profesional - PROYECTO

EQUIPOS
 Proyecto - Práctica

INFORMACIÓN
Clara y concisa
Evitar confusiones
Evitar interpretaciones
Optimizar el tiempo

ROLES 

ESCALA
Story Points
Nivel de Dificultad
Tiempo Estimado de Resolución
1 Punto
Baja: Tarea sencilla, rutinaria, sin riesgos. Solución clara (ej. agregar un campo simple).
2 Días
3 Puntos
Media: Requiere análisis, configuración de varios elementos conectados o pruebas detalladas (ej. un Flow simple).
5 Días
5 Puntos
Alta: Alta complejidad técnica, involucra varios objetos, permisos, o hay incertidumbre/riesgos (ej. configurar toda una comunidad).
8 Días

CALENDARIO

INFORMACIÓN
Se van a turnar Rol de SFC Consultant - BA y PO para seguir creando y modelando las HU

EJ: 
Lunes = 
Rol BA termina de escribir y refinar 3 HU nuevas y tener 3 HU listas para asignar

Que hacen SFC Consultant y PO? 
Trails atrasados
Trails del día
Refinar Documentación

INFORMACIÓN
ASIGNACIÓN

3 SFC Admin listos para desarrollar las historias de esta semana.

Estas 3 personas deben realizar los trails fuera del horario del curso y se reunirán en una sala a parte junto con el rol de creación de HU

INFORMACIÓN
RESTO DEL EQUIPO Tiempo de estudio

Trails del día
Trails atrasados
Trails Opcionales
Superbadge Atrasados
Superbadge Opciones

Todo lo que aporte de teoría al equipo para responder a dudas y ideas

EXCEL
Ya estan cargados los Excel de los proyectos

LINK

PROYECTO

AL CLIENTE o TL
Pueden cargar sus nuevas dudas de esta semana

Tiempo Máximo hasta el jueves 

EQUIPOS
Método de trabajo


SANDBOXES
Tener la misma copia del SPRINT 1
Cargar los registros en ambas Sandboxes
Trabajar HU que no tengan dependencias

Ejemplo: Se puede trabajar en DEV - Reportes y Dashboards y en DEV QA trabajar Flows
4 Usuarios trabajando sin complicaciones

EQUIPOS
Tareas

TAREAS - LUNES 9 de Marzo 
CREACIÓN de HU - 1 solo ROL
DESARROLLO de HU - de 1 a 4 SFC Admin

Tener listas de 1 a 4 HU para trabajar
QA = se deben dejar Screen con DESCRIPCIÓN CLARA
Tener en cuenta dificultad para no pasarse del VIERNES para deploy a PROD


QUÉ HACEMOS HOY?
1-DAILY 15 min registrar en el gestor de versiones

DESPUÉS VIENEN AL CENTRO LOS MIEMBROS QUE VAN A LA OTRA SALITA

2-Trailhead del dia de la fecha y si queda tiempo, los atrasados, opcionales, SB atrasados u opcionales

20:45 RETRO


¡Manos a la obra!
Avanzamos con los trails.



¿Cómo nos fué?¿Qué cosas no quedaron claras y necesitamos repasar la próxima?
retro




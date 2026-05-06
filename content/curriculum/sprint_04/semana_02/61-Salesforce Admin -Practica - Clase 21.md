Salesforce
Admin +
Agent Force

vamos a ver la segunda parte de modelado de datos… 



El Concepto: ¿Qué es esto?
 Salesforce Inspector Reloaded es como tener "Rayos X" dentro del CRM.
Sin la extensión: Para ver un dato oculto o exportar registros, tardas 10 clics y vas a reportes o configuración.
Con la extensión: Es una capa transparente que vive sobre Salesforce y te permite hablar directamente con la base de datos sin salir de la página donde estás trabajando.
Si no la tienen, deben instalarla en Chrome o Edge:
Ir a la Chrome Web Store.
Buscar: Salesforce Inspector Reloaded (asegúrate que sea la versión "Reloaded", que tiene el icono de una pequeña nube con una flecha).
Click en Añadir a Chrome.



El Concepto: ¿Qué es esto?
 El Avistamiento: ¿Dónde está?
Una vez instalada, deben refrescar su pestaña de Salesforce.
La Flecha Invisible: Aparecerá una pequeña pestaña blanca con una flecha gris en el borde lateral derecho de la pantalla.
El Atajo Maestro: Diles que presionen Alt + I (o Option + I en Mac). Si el panel se abre y se cierra, ¡están listos para empezar!



El Concepto: ¿Qué es esto?
El Panel Lateral: Mostrar las 4 columnas principales (Objects, User, Org, Data).
La Herencia de Sesión: Explicar que si ellos están logueados en Salesforce, la extensión "se cuelga" de esa sesión. No hay usuario ni contraseña propia, lo cual es una ventaja de seguridad enorme.
Diferencia Interfaz vs. API: * Interfaz: Lo que ven en pantalla (botones, layouts).
Inspector: Acceso a los datos "crudos" (API). Si un campo existe pero no está en el Page Layout, Inspector lo ve igual.






EJERCICIO
No pueden cargar el formulario fuera de fecha
Tienen que subir la evidencia que es el resultado de cada ejercicio (Screenshot)
Hay corrección
No es quien termina más rápido es quien lo resuelve en el transcurso del día
Pueden utilizar la IA


Hay premio por participación

Trails al día
Ejercicios al dia

🎁



LINK



El Concepto: ¿Qué es esto?
Averiguar y tratar de resolver el ejercicio



EQUIPOS
SPRINT 3

SPRINT COMPLETOS
Comienzan el Sprint 3 de proyecto
100%
Proyecto
SPRINT COMPLETOS

Comienzan la 2da semana del Sprint 3 de proyecto
75%
SPRINT COMPLETOS
Ponerse al dia de forma URGENTE
-%

PARTICIPACIÓN
EQUIPO 1
100%
Robert 
75%
Andrea

Atrasados
El resto del equipo
EQUIPO 2
100%

75%
Hector
Patzy
Atrasados
El resto del equipo

EQUIPO 3
100%
Wilmer
75%
Irayda
Lindbergh
Atrasados
El resto del equipo



CHECKLIST SPRINT 1


Modelado de Datos
Todos los objetos necesarios declarados en el Sprint 1 
Creación de App
Logo, colores y formatos de diseño
Formularios 
Lightning page, page layouts
Gestión de Usuarios y Permisos
Creación de Usuarios y acceso a la información

vamos a ver la segunda parte de modelado de datos… 



CHECKLIST SPRINT 2


Carga Masiva de Datos
Haber podido subir al menos 500 Registros
Haber limpiado los excel
Tener data concreta
Reportes y Dashboards
Reportes requeridos por el cliente
Dashboards requeridos por el cliente
Automatizaciones
1 Screen Flow
1 Trigger Flow
1 Schedule Flow
vamos a ver la segunda parte de modelado de datos… 



PRESENTACIÓN DEL SPRINT 3
El Objetivo del Sprint: Expandiendo las fronteras del CRM

Este sprint gira en torno a una herramienta fundamental: Experience Cloud. El objetivo es que dejen de ver a Salesforce como una base de datos interna y lo transformen en un portal interactivo.
vamos a ver la segunda parte de modelado de datos… 



Estrategia Técnica: Screen Flows como Interfaz Web

Una de las soluciones más potentes que vamos a implementar es el uso de Screen Flows como formularios dentro del sitio. Para esto, quiero que sigan este orden de arquitectura:
Diseño del Flujo (Backend): Construyan el Screen Flow dentro de Salesforce con las pantallas necesarias (ej: Datos de contacto, motivos, carga de archivos). Asegúrense de que la lógica final cree el registro correspondiente (Lead, Caso o el Objeto Personalizado que definieron).
Definición de Audiencia y Seguridad: Este es el punto crítico. Deben decidir si el formulario es Público (ej: un "Contáctenos" para prospectos) o Privado (solo para usuarios logueados). Si es público, recuerden configurar los permisos del Guest User Profile para que tenga acceso a ejecutar el Flow y crear registros.
Implementación Visual (Experience Builder): Una vez que el flujo es seguro y funcional, su publicación en el sitio es simple. Usen el componente estándar de "Flow" en el Builder, arrástrenlo a la página y selecciónenlo del menú.
vamos a ver la segunda parte de modelado de datos… 



CHECKLIST SPRINT 3


Proyecto
Aplicación en el Portal (Experience Cloud)
Novabank
Portal de Clientes: Consulta de estado de tarjetas/préstamos, artículos de prevención de fraude y chat de soporte para emergencias financieras.
Vitacore
Portal del Paciente: Gestión de turnos, artículos de bienestar y formularios de autogestión para reintegros o consultas médicas.
Lumina Tech
Partner Central / Help Desk: Registro de leads por parte de distribuidores o levantamiento de tickets técnicos cuando el software reporta fallas.
vamos a ver la segunda parte de modelado de datos… 



EQUIPOS
SPRINT RETROSPECTIVE

Sprint Retrospective (Afilando el hacha)

Sprint Retrospective (Afilando el hacha)
1. ¿Qué es la Retro?
Es una reunión SOLO para el equipo (Admins + PM). A veces el PO no participa para que el equipo hable con total libertad.
Objetivo: Inspeccionar el PROCESO y las RELACIONES, no el producto. No hablamos de Salesforce, hablamos de cómo trabajamos juntos.
La Regla de las Vegas: "Lo que se dice en la Retro, se queda en la Retro". Es un espacio seguro para ventilar frustraciones y proponer mejoras sin miedo a represalias.

Dinámica de la RETRO
 La Dinámica: Start - Stop - Continue (15 min) El equipo responde 3 preguntas simples sobre el Sprint que terminó:
🟢 Start (Empezar a hacer): ¿Qué idea nueva deberíamos probar?
Ejemplo: "Empecemos a poner la etiqueta roja a los bugs urgentes".
🔴 Stop (Dejar de hacer): ¿Qué nos está frenando o molestando?
Ejemplo: "Dejemos de llegar 5 minutos tarde a la Daily".
🟡 Continue (Seguir haciendo): ¿Qué funcionó bien y debemos mantener?
Ejemplo: "El pair-programming (programar en parejas) para los Flows difíciles funcionó genial".

RESULTADO DE LAS RETRO
El Resultado: Action Items
De la queja se pasa a la acción.
Se elige 1 mejora concreta para aplicar en el próximo Sprint.
Ejemplo: "Para el Sprint 3, mantendremos un calendario de presencia y horarios".

QUÉ HACEMOS HOY?
1-Reunión de Retrospective 30 minutos
2-Análisis de las HU
3-TRAILS atrasados


¡Manos a la obra!
Avanzamos con los trails.



¿Cómo nos fué?¿Qué cosas no quedaron claras y necesitamos repasar la próxima?
retro




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

Skills Digitales
Uso de la IA: para resolución, investigación, búsqueda de información
Gestión de Herramientas Ágiles: Uso efectivo de tableros Kanban (Jira, Trello, etc.) para el seguimiento de tareas y Sprints.
Uso de foros, google, documentación: Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
Herramientas de Salesforce: Extensiones y herramientas útiles por fuera de salesforce
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Creativas
Resolución Lateral de Problemas (Workarounds): Capacidad de encontrar caminos alternativos e ingeniosos cuando la plataforma presenta limitaciones nativas.
Diseño Centrado en el Usuario (UX/UI): Creación de Page Layouts y pantallas que sean intuitivas, limpias y agradables para el usuario final.
Storytelling con Datos: Habilidad para construir Dashboards y Reportes que no solo muestren números, sino que cuenten una historia visual y clara.
Ingeniería de Procesos: Imaginar y diseñar el "camino más corto y fácil" para que un usuario complete sus tareas diarias.
Resiliencia Técnica: Ver los errores del sistema o bugs como un rompecabezas creativo a resolver, perdiéndole el miedo a "romper" en entornos de prueba.
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Estratégicas
Traducción de Negocio (Business Analysis): Capacidad para escuchar lo que pide el cliente y traducirlo en requerimientos técnicos reales (entender el "por qué" detrás del "qué").
Mentalidad Escalable: Construir soluciones pensando no solo en el problema de hoy, sino en cómo funcionará cuando la empresa crezca en 2 o 3 años.
Priorización de Valor (MVP): Saber distinguir entre lo esencial y lo accesorio para entregar valor rápido al cliente (Producto Mínimo Viable).
Gestión de Expectativas (Stakeholders): Aprender a negociar requerimientos y a decir "no" (o "lo dejamos para la fase 2") de manera profesional y fundamentada.
Gobernanza y Documentación: Entender que documentar (diccionarios de datos, descripciones) es una estrategia vital para la supervivencia a largo plazo del proyecto.
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

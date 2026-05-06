Salesforce
Admin +
Agent Force

vamos a ver la segunda parte de modelado de datos… 



EJERCICIO
Pueden cargar el formulario fuera de fecha
Tienen que subir la evidencia que es el resultado de cada ejercicio (Screenshot)
Hay corrección
No es quien termina más rápido es quien lo resuelve en el transcurso del día
Pueden utilizar la IA
Es obligatorio no importa que fecha lo terminen


Hay premio por participación

Trails al día
Ejercicios al dia

🎁



Correcciones
Se usa la Extesión
No la developer Console
No el Setup
No se suben Screen vacias
Si incompletas o con algun resultado aunque no sea el esperado
Todos los ejercicios son obligatorios y tienen que subir la evidencia



LOGIN
1. Acceso sin Fricción
Herencia de Sesión: La extensión utiliza el Access Token de tu pestaña activa. Si estás dentro de Salesforce, ya estás dentro de Inspector.
Shortcut de Usuario: Olvida el menú de Setup > Users. Busca cualquier usuario por nombre o username directamente en el buscador de la extensión y accede al botón "Login".
2. Anatomía del Login Experto
Aislamiento por Pestaña: Inspector permite mantener sesiones de diferentes usuarios en pestañas separadas del mismo navegador.
Validación de Perfiles: Es la herramienta #1 para el UAT (User Acceptance Testing). Permite verificar qué campos ve (o no ve) un usuario según su licencia y FLS (Field Level Security) en tiempo real usando Show all data.



LINK
EJERCICIO 3
USUARIOS
Crear 3 usuarios: Uno con licencia Salesforce, otro con Platform y un tercero (opcional) con Force.com o Chatter Free.
Loguearse con los 3 usando el atajo de Inspector desde la pestaña Users.
Validación de Visibilidad (Data View): Una vez logueados como el usuario con licencia limitada (ej. Platform), deben abrir un registro de Oportunidad y usar Show all data de Inspector.
El reto: qué notaron?.
Cambio de Atributo: Volver a su usuario Admin, buscar a uno de esos 3 usuarios en Inspector y, mediante Data Import, cambiarles el alias o el departamento de forma masiva (a los 3 a la vez) para practicar la edición de metadatos de usuario.
Tener en cuenta que para loguearse con la extensión hay un paso de configuración previa

La captura debe reflejar el cambio de alias de los usarios con la Extensión



LINK
EJERCICIO 3
USUARIOS
Pistas de Oro para el Challenge (Para completar tu slide):
Búsqueda Ultra-Rápida: No pierdan tiempo en el Setup de Salesforce buscando la lista de usuarios. Abran Inspector (Alt + I), vayan a la pestaña Users y escriban el nombre. El botón de Login aparecerá ahí mágicamente si activaron las Login Access Policies.
La Trampa de las Licencias: Si intentan loguearse y la página se queda en blanco o los saca de Salesforce, revisen si el usuario tiene el Profile asignado correctamente. Inspector no puede saltarse las reglas de acceso básicas de la licencia.
Identificación de Sesión: Para no confundirse entre pestañas, usen la función "User Info" de Inspector en cada pestaña abierta. Les dirá exactamente con qué nombre y qué ID de usuario están operando en ese segundo.
Multi-Pestaña: Pueden estar logueados como el Usuario A en una pestaña y como el Usuario B en otra. Inspector mantiene las sesiones separadas por pestaña si usan el botón de Login de la extensión.
El ID es Rey: Para cualquier cambio masivo en estos usuarios (ejercicio de Update), el campo User.Id es su mejor amigo. Cópienlo directamente desde el panel de búsqueda de la extensión.



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



HOY

ROLES DE ANÁLISIS
Concepto Central: Cada rol responde a una pregunta diferente dentro del proyecto: 

¿Qué? (BA), 
¿Cómo? (Consultant), 
y ¿Por qué/Cuándo? (PO).

Planning 
& 
Estrategia
SPRINT 1
Ceremonia: Sprint Planning.

Objetivo: Definir QUÉ haremos y QUIÉN lo hará.

Meta: Salir de esta reunión con nuestro Tablero listo para trabajar.

Planning 
& 
Estrategia
SPRINT 1

QUÉ HACEMOS HOY?
1-Análisis de los requerimientos
2- Creación de HU
3-Trails atrasados


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

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



El traductor universal entre Salesforce y el mundo
La búsqueda no es solo una barra de texto; es el motor que reduce la fricción entre el usuario y la solución. En Experience Cloud, el 80% de los usuarios prefiere buscar antes que navegar por menús.
Ejemplo Diario: Un cliente entra a tu portal de soporte buscando "cómo configurar mi router". Si la búsqueda falla, abre un ticket innecesario que cuesta dinero.



El Corazón del Buscador (Global Search)
Título: ¿Qué ve realmente el usuario?
Teoría: Salesforce utiliza una búsqueda federada y global. Los componentes clave son: la barra de búsqueda global, los resultados de búsqueda y el perfil del usuario (que determina qué puede ver).
Ejemplo Diario: Un usuario Jr. intenta buscar un "Artículo de Conocimiento", pero si el Admin no habilitó ese objeto en la configuración del sitio, el artículo será invisible aunque exista.



Autocompletado y Sugerencias
Título: Anticipándonos a la intención del usuario.
Teoría: El autocompletado muestra resultados mientras el usuario escribe. Esto se basa en los objetos más utilizados y en los títulos de los artículos de Knowledge.
Ejemplo Diario: Al escribir "Fra...", el sistema ya sugiere "Facturación" y "Fraccionamiento de pagos", ahorrando clics y reduciendo errores ortográficos.



Filtrado y Refinamiento
Título: Navegando en el Mar de Datos.
Teoría: No todos los resultados son iguales. Los filtros permiten segmentar por tipo de objeto (Casos, Artículos, Discusiones) y metadatos (Fecha, Estado).
Ejemplo Diario: Un Partner de ventas busca "Oportunidades" de "Este Mes". Sin filtros, vería registros de hace 3 años mezclados con los actuales.



Configuración para Admins (El "Behind the Scenes")
Título: ¿Cómo lo configuramos en Experience Builder?
Teoría: Como Admins, configuramos el componente "Search" definiendo: qué objetos se buscan, cuántos resultados se muestran por página y si permitimos búsqueda pública (sin login).
Ejemplo Diario: Entrar al Experience Builder -> Propiedades del componente Search -> Añadir "Pricebook" a la lista de objetos buscables para que los comerciales vean precios.



 El Poder de Knowledge en la Búsqueda
Título: El mejor amigo de la Búsqueda: Salesforce Knowledge.
Teoría: La búsqueda en sitios de Experience Cloud alcanza su máximo potencial cuando se integra con Knowledge. Los algoritmos de relevancia priorizan artículos con más vistas y mejores calificaciones.
Ejemplo Diario: Un cliente busca "Devolución". El buscador no solo le da el registro de su compra, sino el artículo "Política de Devoluciones" resaltado arriba.



Práctica Profesional - PROYECTO

EQUIPOS
 Proyecto - Práctica

CALENDARIO

ROLES

EQUIPOS

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
Ejemplo: "Para el Sprint 2, todos actualizaremos el estado de las tarjetas en Trello antes de las 18:00 hs".

QUÉ HACEMOS HOY?
1-Reunión de Retrospective 30 minutos
2-Trailhead del dia de la fecha
3-Grupo de analisis del dia


¡Manos a la obra!
Avanzamos con los trails.



¿Cómo nos fué?¿Qué cosas no quedaron claras y necesitamos repasar la próxima?
retro




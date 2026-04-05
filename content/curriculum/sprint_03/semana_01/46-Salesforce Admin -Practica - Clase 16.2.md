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



☁️ Construir un Sitio Experience Cloud con Knowledge y Chat
Objetivo del Trail: Crear un portal de autoservicio funcional donde los clientes puedan resolver dudas por sí mismos o contactar a un agente en tiempo real.



🎯 Puntos Fundamentales de Aprendizaje:
1. Implementación de Salesforce Knowledge: * Habilitar la base de conocimientos.
Crear y publicar artículos (FAQs) configurando los canales adecuados para que sean visibles para los clientes externos.
2. Despliegue de Experience Cloud: * Activar "Digital Experiences".
Levantar un sitio web rápidamente utilizando la plantilla preconfigurada de Customer Service.
3. Configuración de Soporte en Vivo (Chat & Omni-Channel):
Habilitar Web Chat (anteriormente Live Agent) y Omni-Channel.
Configurar la cola de atención y las habilidades para enrutar los chats al agente correcto de Salesforce.
4. Personalización con Experience Builder:
Aprender a usar el maquetador visual arrastrando y soltando componentes.
Integrar el componente de búsqueda de artículos y el botón flotante de chat (Embedded Service) en la interfaz del cliente.
Gestionar permisos de visibilidad (perfil de Guest User).



Práctica Profesional - PROYECTO

EQUIPOS
 Proyecto - Práctica

CALENDARIO

ROLES - de 1 a 3 personas máximo

EQUIPOS

EQUIPOS
Semana de Análisis

ROLES DE ANÁLISIS

 De la Petición a la Solución (Traduciendo el Lenguaje del Negocio)
Concepto Central: El cliente rara vez habla en términos de "Objetos", "Flows" o "Reglas de Validación". El equipo debe traducir la necesidad humana a la arquitectura de Salesforce, aportando valor en cada paso.

Técnica para el Business Analyst (BA): "Los 5 Porqués" (The 5 Whys)
El Problema: El cliente suele pedir una solución (ej. "Quiero un botón rojo aquí"), no explica el problema.
La Técnica: Ante cada requerimiento, preguntar "¿Por qué?" iterativamente hasta llegar a la raíz del problema de negocio.
La Traducción:
Cliente: "Necesito 10 campos nuevos en la Cuenta."
BA (aplicando técnica): 
"¿Por qué? -> Para saber qué productos tienen. -> 
¿Por qué? -> Para hacer marketing. -> 
Traducción: ¡Ah! No necesitas campos en la Cuenta, necesitas usar el objeto estándar de Activos (Assets) u Oportunidades."
El Aporte: Evita ensuciar la Org con campos innecesarios descubriendo el verdadero dolor del usuario.

Técnica para el Salesforce Consultant: Pensamiento "OOTB" (Out-of-the-Box First)
El Problema: Los clientes a menudo imaginan flujos de trabajo hiper-personalizados que requieren código complejo, porque no conocen lo que Salesforce ya trae hecho.
La Técnica: Mapear siempre el requerimiento del negocio contra las funcionalidades estándar de Salesforce antes de proponer automatizaciones o código a medida.
La Traducción:
Cliente: "Cuando el prospecto dice que sí, quiero que un sistema copie todos sus datos a una ficha de cliente y otra de venta."
Consultor (aplicando técnica): "En lugar de programar eso de cero, Salesforce tiene un proceso estándar llamado 'Conversión de Candidatos' (Lead Conversion) que hace exactamente esto de forma nativa."
El Aporte: Salva el presupuesto del proyecto, reduce el mantenimiento futuro y maximiza el retorno de inversión usando lo que ya viene en la licencia.

Técnica para el Salesforce Consultant: Pensamiento "OOTB" (Out-of-the-Box First)
El Problema: Los clientes a menudo imaginan flujos de trabajo hiper-personalizados que requieren código complejo, porque no conocen lo que Salesforce ya trae hecho.
La Técnica: Mapear siempre el requerimiento del negocio contra las funcionalidades estándar de Salesforce antes de proponer automatizaciones o código a medida.
La Traducción:
Cliente: "Cuando el prospecto dice que sí, quiero que un sistema copie todos sus datos a una ficha de cliente y otra de venta."
Consultor (aplicando técnica): "En lugar de programar eso de cero, Salesforce tiene un proceso estándar llamado 'Conversión de Candidatos' (Lead Conversion) que hace exactamente esto de forma nativa."
El Aporte: Salva el presupuesto del proyecto, reduce el mantenimiento futuro y maximiza el retorno de inversión usando lo que ya viene en la licencia.

Técnica para el Product Owner (PO): Priorización
 "MoSCoW"
El Problema: Para el cliente, todo es urgente y todo es para ayer.
La Técnica: Clasificar los requerimientos traducidos en 4 cubos para negociar el alcance:
Must have (Debe estar, o el sistema no sirve - Ej: Crear Oportunidades).
Should have (Debería estar, es importante pero hay alternativas temporales - Ej: Un Flow para automatizar una tarea).
Could have (Podría estar, estaría genial si sobra tiempo - Ej: Un dashboard súper complejo).
Won't have (No estará por ahora, queda para la Fase 2).
El Aporte: Protege al equipo técnico de la sobrecarga y asegura que el cliente reciba lo más valioso primero.

El Mindset Consultivo: Preguntar para Proponer
No digas: "No se puede hacer."
Di: "Salesforce no lo maneja exactamente así por diseño, pero la mejor práctica nos sugiere resolverlo de esta otra manera para que a futuro puedas escalar. ¿Qué te parece si..."
Regla de Oro: Nunca aceptes un requerimiento sin entender qué métrica de negocio espera mejorar el cliente con ese cambio (¿Vender más rápido? ¿Reducir quejas? ¿Ahorrar clics?).

EQUIPOS
Tareas

TAREAS - 2/3 al 6/3 

QUÉ HACEMOS HOY?
1-DAILY 15 min registrar en el gestor de versiones
2-Trailhead del dia de la fecha y si queda tiempo, los atrasados
3-Grupo de analisis del dia HOY Equipo 2- Solo los roles de esta semana.


¡Manos a la obra!
Avanzamos con los trails.



¿Cómo nos fué?¿Qué cosas no quedaron claras y necesitamos repasar la próxima?
retro




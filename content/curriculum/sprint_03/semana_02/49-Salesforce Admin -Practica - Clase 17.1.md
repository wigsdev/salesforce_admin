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



Aplicación Práctica en Proyecto Real
1. Preparación de los Datos (La Base)
En el Proyecto Real: Imagina que un alumno pregunta "¿Está pagada mi matrícula?".
La Tarea del Admin: Antes de encender la IA, debes asegurarte de que el objeto "Pagos" y "Alumnos" estén limpios y accesibles. Si los datos están sucios o duplicados, el Agente dará respuestas erróneas.
Acción: Revisar la calidad de los datos y configurar los Objetos que el Agente tiene permiso de leer.

Aplicación Práctica en Proyecto Real
 Creación de las "Herramientas" (Service Catalog & Flows)
En el Proyecto Real: El Agente necesita poder hacer cosas, no solo hablar. Necesita reenviar una factura o actualizar un estado.
La Tarea del Admin: Crear Autolaunched Flows (Flujos autoejecutables).
Ejemplo: Un Flow que toma el ID del alumno, busca el último recibo y lo marca como "Reenviar por Email".
Clave: El Agente "llama" a este Flow cuando detecta que el usuario lo necesita.

Aplicación Práctica en Proyecto Real
Configuración de "Topics" e Instrucciones
En el Proyecto Real: Definir qué sabe hacer el agente.
La Tarea del Admin: Entras al Agent Builder y creas un Topic llamado "Administración Académica".
Le das instrucciones: "Usa este tema cuando el usuario pregunte sobre dinero, fechas de pago o facturas. Sé formal y verifica la identidad primero".
Asignas las "Acciones" (los Flows del paso 2) a este Topic.

Aplicación Práctica en Proyecto Real
Testing en el "Playground" (Simulador)
En el Proyecto Real: No lanzamos a producción a ciegas.
La Tarea del Admin: Usar el panel de prueba (Simulador) dentro de Agent Builder.
Escribes: "Hola, quiero saber si debo algo".
Lo importante: Observas el "Reasoning Trace" (Rastro de Razonamiento). Verás cómo el Agente "piensa": 1. Detecté intención de deuda. 2. Busco en Topic Administración. 3. Ejecuto Flow 'Consultar Saldo'. 4. Respondo.
Si falla, ajustas las instrucciones del Topic, no código.

Aplicación Práctica en Proyecto Real
Auditoría y "Guardrails" (Barreras de Seguridad)
En el Proyecto Real: Evitar que el Agente prometa descuentos que no existen o hable de política.
La Tarea del Admin: Revisar los logs de interacciones regularmente.
Configurar reglas en la Trust Layer para bloquear palabras tóxicas o competidores.
Si el Agente alucina, se ajusta el "Prompt" o se mejora el artículo de Knowledge base que usa como referencia.

Práctica Profesional - PROYECTO

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

EQUIPOS Proyecto

EQUIPOS Proyecto
EQUIPO 1
Rol Analista: Robert
SFC Admin + QA:
Karla
Stefanny
Nicole
Andrea
EQUIPO 2
Rol Analista: Patzy
SFC Admin + QA:
Juliana
Hector
EQUIPO 3
Rol Analista: Wilmer
SFC Admin + QA
Anais
Grecia
Guillermo 
Marysol

EQUIPOS Proyecto - Semana 2
TAREAS

EXCEL CALIDAD DE DATOS
Modelo de Datos: Qué objetos, campos intervienen
Calidad: Limpieza, duplicados, celdas vacías
Hacer pruebas en alguna de las Sandbox

Por grupo tienen Sandbox
2 DEV - 2 QA - 2 PROD

BASE DE TODO EL SPRINT 2

EQUIPOS Proyecto - Semana 2 y 3
TAREAS

REPORTES Y DASHBOARDS
Configuración
Filtros
Visibilidad
Tipos de Gráficos

Necesitan datos para testear y que los reportes reflejen lo que se tiene que ver

EQUIPOS Proyecto - Semana 3
TAREAS

FLOWS - Automatizaciones
Configuración
Diseño
Debuguear

Necesitan tener bien en claro en proceso de negocio para poder hacer que funcionen 

EQUIPOS Proyecto - Semana 4
TAREAS

PROD
Registros
Reportes
Dashboards
Flows

DEMO
Guión
PPT

 
Todo Testeado
Terminado

Guión y PPT entregado y revisado

TIEMPO

TIEMPO
La Matriz de Impacto vs. Esfuerzo (Para priorizar visualmente)
Cuando todo parece urgente, los alumnos se abruman y pierden el foco. Enséñales a clasificar sus tareas antes de empezar a trabajar.
Cómo aplicarlo: dibujen un cuadrante. 
Las tareas de Alto Impacto / Bajo Esfuerzo (Quick Wins) se hacen de inmediato para ganar inercia. 
Las de Alto Impacto / Alto Esfuerzo se planifican. Si una tarea es de Bajo Impacto, se delega o se descarta.
El aprendizaje: Entender que no todas las tareas valen lo mismo y que deben invertir su energía donde mueva la aguja.

 El Método MoSCoW (Para filtrar qué hacer hoy)
Muchas veces se enredan queriendo hacer la solución "perfecta" en lugar de la funcional.
Cómo aplicarlo: etiquetar las tareas del día en 4 cubos:
Must do (Tengo que hacerlo sí o sí hoy).
Should do (Debería hacerlo si me da el tiempo).
Could do (Podría hacerlo, sería un buen "extra").
Won't do (No lo voy a hacer hoy).
El aprendizaje: Les enseña a soltar el perfeccionismo y asegurar primero el valor principal.

 La Regla de los 15 Minutos (Para no quedarse atascados)
Los perfiles técnicos tienden a meterse en "madrigueras de conejo" intentando resolver un problema solos durante horas, perdiendo todo el día.
Cómo aplicarlo: regla de equipo inquebrantable. Si llevan 15 minutos bloqueados con el mismo error, código o decisión sin avanzar, tienen la obligación de levantar la mano y pedir ayuda a un compañero o al TL.
El aprendizaje: Fomenta el trabajo en equipo, reduce la frustración y cuida el tiempo del proyecto.

  La Regla de las 2 Horas / "Trocear el Elefante" (Para gestionar la dificultad)
La falta de concentración suele nacer de la ansiedad que provoca una tarea gigante o mal definida (ej. "Armar la base de datos").
Cómo aplicarlo: Ninguna tarea en su tablero puede tener una estimación mayor a 2 horas (o 4 como máximo). Si la tarea es "Crear reporte" y lleva 8 horas, deben partirla: 1. Extraer datos (1h), 2. Limpiar datos (2h), 3. Armar gráfico (1h).
El aprendizaje: Al ver tareas pequeñas y muy específicas, el cerebro no se bloquea y es mucho más fácil mantener el foco y tachar pendientes.

Timeboxing Implacable (Para forzar la toma de decisiones)
La "Ley de Parkinson" dice que el trabajo se expande hasta llenar el tiempo disponible. Si les das 3 días para investigar un tema, tardarán 3 días.
Cómo aplicarlo: Asigna "cajas de tiempo" estrictas para las decisiones o la investigación. Ej: "Tienen exactamente 45 minutos para investigar qué herramienta usar. Cuando suene la alarma, tomamos una decisión con la información que tengamos hasta ese momento".
El aprendizaje: Les enseña a iterar, a conformarse con decisiones "suficientemente buenas" para avanzar, y a entender que hecho es mejor que perfecto.

QUÉ HACEMOS HOY?
1-DAILY 15 min registrar en el gestor de versiones por Grupo

Se dividen en  salas desde las 18:30
TENER LA PPT de GUÍA

2-Trailhead del dia de la fecha y si queda tiempo, los atrasados, opcionales, SB atrasados u opcionales

20:45 RETRO


EQUIPOS Proyecto - Semana 2
TAREAS

EXCEL CALIDAD DE DATOS
Modelo de Datos: Qué objetos, campos intervienen
Calidad: Limpieza, duplicados, celdas vacías
Hacer pruebas en alguna de las Sandbox

Por grupo tienen Sandbox
2 DEV - 2 QA - 2 PROD

BASE DE TODO EL SPRINT 2

EQUIPOS Proyecto - Semana 2 y 3
TAREAS

REPORTES Y DASHBOARDS
Configuración
Filtros
Visibilidad
Tipos de Gráficos

Necesitan datos para testear y que los reportes reflejen lo que se tiene que ver

¡Manos a la obra!
Avanzamos con los trails.



¿Cómo nos fué?¿Qué cosas no quedaron claras y necesitamos repasar la próxima?
retro




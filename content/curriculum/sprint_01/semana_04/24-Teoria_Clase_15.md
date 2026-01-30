# Salesforce Admin + Agent Force

## daily
*   Del 1 al 10 cómo te sentís?
*   Qué te proponés para hoy?


> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## Skills Técnicas (El "Qué" haces)
*   **Gestión de Usuarios y Seguridad**: El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
*   **Gestión de Datos (Data Management)**: Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
*   **Automatización Básica (Flows)**: Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
*   **Reportes y Dashboards**: Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.
*   **AgentForce**: puedas familiarizarte con la configuración de agentes dentro de Salesforce.

> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## Skills Blandas (El "Cómo" lo haces)
*   **Comunicación Traducida**: Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
*   **Resolución de Problemas (Google-Fu)**: No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
*   **Mentalidad de Aprendiz (Learner's Mindset)**: Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
*   **Atención al Detalle**: Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.

> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## COLABORACIÓN
*   Aprender con y de otras personas

### AUSENCIAS
*   Seguir con la planilla y actividades

### MIC o CHAT
*   Comunicación

### ERRORES
*   Atrasados

### JUEVES

### PREGUNTAS
*   Al final de la clase Teórica

## Para una buena clase…

### AUTONOMÍA
*   Utilizar las herramientas

---

# Service Cloud: El "Cockpit" de Atención al Cliente

vamos a ver la segunda parte de modelado de datos…

## El Corazón del Servicio: El Objeto "Caso"

## La Herramienta de Trabajo: La Consola de Servicio (Console)
Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:
*   **La Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
*   **La Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

## Productividad: Knowledge y Utilerías
¿Qué hacemos si ya tenemos 1000 duplicados? No se borran uno por uno.
Usamos la herramienta de **Merge (Fusionar)**. Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
Nunca eliminen un duplicado sin revisar qué información histórica tiene.

# ¡Manos a la obra!
Avanzamos con los trails.


> Guia: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol

## LEER CON ATENCIÓN
Las prácticas previas al challenge son importantes para entender el challenge

### NO DEJARLAS PASAR

### ATENCIÓN

### ERRORES
*   Agotar herramientas
*   Consultar con su grupo
*   Hacer una nueva ORG
*   Recién consultar a los profesores

### CONSULTAS
*   Haber agotado todas las instancias de herramientas

### Contexto
SB-Jueves

## PAIR PROGRAMING
*   Compartir pantalla
*   Hablar sobre el proceso del Trailhead
*   Ir rotando
*   No se puede estar en silencio
*   El trabajo individual es fuera de la cursada


**Service Cloud Basics**
[LINK]

---

# POSIBLES PREGUNTAS

### 1. Colas vs. Dueños (Queues vs. Users)
**Alumno**: "Profe, ¿un Caso puede ser de un grupo de personas o tiene que ser de una sola persona?"
**Respuesta**: "Puede ser de un grupo, y eso se llama Cola (Queue). En soporte, los casos nuevos suelen caer en una Cola (ej: 'Cola Nivel 1'). Los agentes miran la cola, toman un caso (lo 'aceptan') y en ese momento el dueño cambia de la 'Cola' al 'Usuario' (Juan Pérez). Regla: Un registro solo puede tener UN dueño a la vez (o la Cola o Juan, no ambos)".

### 2. ¿Por qué no veo la pestaña de "Knowledge"?
**Alumno**: "Estoy buscando la pestaña de Artículos de Conocimiento (Knowledge) en el App Launcher y no aparece, aunque soy Admin."
**Respuesta**: "¡Es el error más común de configuración! Para ver y crear Knowledge, necesitas marcar una casilla especial en tu registro de Usuario llamada 'Knowledge User'. Es una 'Licencia de Característica' (Feature License). Sin ese checkbox, Knowledge no existe para ti".

### 3. Web-to-Case (El Spam)
**Alumno**: "Si configuro Web-to-Case (formulario en la web que crea casos), ¿qué pasa si un bot me llena el formulario 1000 veces?"
**Respuesta**: "Salesforce creará 1000 casos y ensuciará tu org. Para evitarlo, en la vida real siempre activamos reCAPTCHA en la configuración de Web-to-Case. Es vital para la seguridad del proyecto".

### 4. La confusión de las "Apps"
**Alumno**: "¿Puedo ver Oportunidades dentro de la Service Console? ¿O tengo que cambiar de App?"
**Respuesta**: "Sí puedes, si el Admin lo configuró. La 'Service Console' es solo una App. Como Admins, ustedes deciden qué objetos (tabs) se ven ahí. Pueden agregar Oportunidades a la Consola de Servicio si sus agentes necesitan vender. No están limitados a solo Casos".

> ¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path.
> No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'.
> Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

### 5. Cerrar vs. Borrar Casos
**Alumno**: "Cuando termino un caso, ¿lo borro?"
**Respuesta**: "¡JAMÁS! En Salesforce casi nunca borramos. El Caso se cambia de Estado (Status) a 'Closed' (Cerrado). Así mantenemos el historial: qué pasó, cómo se resolvió y cuánto tardamos. Si lo borras, pierdes la inteligencia del negocio".

### 6. Email-to-Case
**Alumno**: "¿Cómo sabe Salesforce que el email que mandó el cliente es una respuesta a un caso existente y no uno nuevo?"
**Respuesta**: "Por el Thread ID (ID de Hilo). Es un código oculto (o visible en el asunto/cuerpo, dependiendo de la configuración) que Salesforce inserta en los emails. Si el cliente responde sobre ese mismo email, Salesforce lee el ID y pega la respuesta en el Caso original en lugar de crear uno nuevo".

> ¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path.
> No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'.
> Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

# Salesforce Admin + Agent Force

## Daily
*   Qué le dirías hoy a tu YO que va a empezar este curso

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

## AUSENCIAS
*   Seguir con la planilla y actividades 

## MIC o CHAT
*   Comunicación

## ERRORES
*   Atrasados

## JUEVES

## PREGUNTAS
*   Al final de la clase Teórica

## Para una buena clase…

### AUTONOMÍA
*   Utilizar las herramientas

---

**vamos a ver la segunda parte de modelado de datos…**

# El Cerebro del Flujo

**Concepto Teórico**:
Troubleshooting no es solo "arreglar errores rojos". Es entender el camino lógico que tomaron los datos.
*   Diferencia entre **Design Time** (cuando construyes en el Canvas) y **Run Time** (cuando el usuario lo usa).

> **Tip para el Trabajo (Real World)**:
> "El 90% de los errores en producción ocurren porque asumimos que los datos siempre estarían ahí. Un buen Admin diseña pensando en qué pasa si el dato falta."

## Elementos vs. Recursos

**Concepto Teórico**:
*   **Elementos (Elements)**: Son los verbos. Lo que el Flow hace (Crear, Actualizar, Pantalla, Decisión). Aparecen en el Canvas.
*   **Recursos (Resources)**: Son los sustantivos. Lo que el Flow usa (Variables, Fórmulas, Constantes). No se ven en el mapa, están en la "caja de herramientas".

> **Tip para el Trabajo**:
> "Si no pueden encontrar un error, pregúntense: ¿Falló la acción (el verbo) o estaba vacía la caja de datos (el sustantivo/recurso)?"

## Flow Interview

**Concepto Teórico**:
*   Un Flow es solo una plantilla.
*   Una **Flow Interview** es una instancia específica de ese Flow ejecutándose (ej: El usuario Juan está corriendo el Flow "Crear Caso" a las 3 PM).
*   Cuando hacemos Debug, estamos simulando una "Interview".

> **Tip para el Trabajo**:
> "Cuando reciban un correo de error de Salesforce, busquen el ID de la 'Interview'. Ese es el rastro forense de qué pasó exactamente en ese momento específico."

Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:
*   La **Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
*   La **Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

## Variables: Los Contenedores de Datos

**Concepto Teórico**:
*   Las variables son espacios temporales de memoria.
*   Diferencia clave entre una **Single Variable** (un dato) y una **Collection Variable** (una lista de datos/registros).

> **Tip para el Trabajo**:
> "El error más común de un Junior: Intentar guardar una lista de cuentas (Collection) en una caja diseñada para una sola cuenta (Single Variable). Salesforce les gritará por esto. Etiqueten bien sus variables (ej: var_AccountList vs var_SingleAccount)."

*   ¿Qué hacemos si ya tenemos 1000 duplicados? No se borran uno por uno.
*   Usamos la herramienta de **Merge** (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
*   Nunca eliminen un duplicado sin revisar qué información histórica tiene.

## Mejores Prácticas para evitar el "Caos"

**Puntos Clave**:
*   **Naming Conventions**: Usar prefijos estándar (ej: `get_Contacts`, `scr_Welcome`, `dec_IsActive`).
*   **Descriptions**: Llenar siempre el campo de descripción.
*   **Fault Paths**: ¿Qué pasa si el Get Records no encuentra nada?

> **Tip para el Trabajo**:
> "Tu 'yo' del futuro te agradecerá (o te odiará) dependiendo de si escribiste descripciones en los elementos. Documenten por qué hicieron lo que hicieron, no solo qué hicieron."

"¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path. No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'. Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

---

## ¡Manos a la obra!
Avanzamos con los trails.

### Guia
*   Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol

### LEER CON ATENCIÓN
Las prácticas previas al challenge son importantes para entender el challenge. **NO DEJARLAS PASAR**.

### ATENCIÓN / ERRORES
1.  Agotar herramientas
2.  Consultar con su grupo
3.  Hacer una nueva ORG
4.  Recién consultar a los profesores

### CONSULTAS
*   Haber agotado todas las instancias de herramientas

### Contexto
*   SB-Jueves

### PAIR PROGRAMING
*   Compartir pantalla
*   Hablar sobre el proceso del Trailhead o Proyecto
*   Ir rotando
*   No se puede estar en silencio
*   El trabajo individual es fuera de la cursada

### FLOWS 1
[LINK]

---

## Práctica Profesional - PROYECTO

### EQUIPOS
*   Proyecto - Práctica

### OBJETIVO
Creación de App, diseño, personalización e identidad de la empresa.

> ⏱️ **TIP de Gestión del Tiempo**: "Reutilización de Recursos". Ten a mano los códigos Hex (colores) y el logo de la empresa en una carpeta antes de abrir el App Manager.

### ⚡ Daily (5 min)
**Enfoque**: Navegación.
*   **Pregunta clave**: "¿Es intuitivo moverse entre pestañas? ¿La App tiene demasiadas cosas innecesarias?"

### ROLES
👥 **Roles**:
*   **BA**: Define qué pestañas son esenciales para el flujo diario del usuario.
*   **PO**: Valida que el logo y colores representen fielmente la marca.
*   **Consultant**: Configura la "Utility Bar" (Barra de utilidades) para acciones rápidas.
*   **QA**: Verifica que la App se vea bien en diferentes resoluciones.

### SALESFORCE ADMINISTRATOR

✅ **Tareas del día (Admin)**:
*   Usar el App Manager para crear la Lightning App (Branding y Navegación).
*   Configurar Temas y Branding (Themes).
*   Organizar el Menú de Navegación (Tabs).
*   Personalizar la Home Page con componentes útiles.

### TIPS / Otras Tareas
*   Solo 2 personas pueden trabajar en Dev
*   Los demás hacen los trails
*   Analizar los tickets si hay faltantes de criterios
*   Hacer la documentación
*   Mantener el gestor de versiones actualizado

### BLOQUEOS
📢 **Comunicación con TL**: Reportar inmediatamente si hay problemas de licencias o acceso al entorno. DUDAS

## ¡Manos a la obra!

Vamos ingresar para mostrarles cómo se crea una organización práctica y que todos puedan crear una.
Indiquemos que investiguen la organización, que entren y revisen.
*   Link: [https://trailhead.salesforce.com/es/users/profiles/orgs](https://trailhead.salesforce.com/es/users/profiles/orgs)
*   Compartir pantalla para que vean como se hace el proceso.

## retro
¿Cómo nos fué? ¿Qué cosas no quedaron claras y necesitamos repasar la próxima?

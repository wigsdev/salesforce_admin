# Salesforce Admin + Agent Force

## Daily
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

El 'Build Logic' no se trata de cuándo se ejecuta el flujo, sino de qué hace con la información que tiene. 

Hoy aprenderemos cómo el Flow toma decisiones, cómo recuerda datos y cómo maneja listas de cosas.

## Recursos y Variables (Las Cajas)
*   "Una 'Variable' (o Recurso en Flow) es simplemente una CAJA donde guardamos información temporalmente mientras el Flow se ejecuta."
*   "Cuando el Flow termina, las cajas se destruyen. No se guarda en la base de datos hasta que usamos un elemento rosa (Update/Create)."
*   "Regla de oro: No puedes meter una manzana en una caja de zapatos. Debes definir qué tipo de dato va en la caja (Texto, Número, Fecha, Verdadero/Falso)."

## Decisiones y Asignaciones (El Camino)
*   **Elemento Decisión (El Rombo Naranja)**: "Es el 'IF/THEN' (Si pasa esto, entonces aquello). Es una bifurcación en la carretera. El Flow evalúa una condición (ej. ¿La caja 'Ventas' tiene más de 100k?) y elige UN solo camino."

*   **Elemento Asignación (Assignment)**: "Es la herramienta más subestimada. Sirve para dos cosas:
    1.  Meter un valor en una variable (Escribir en una caja).
    2.  Hacer matemáticas simples (Sumar 1 a un contador, calcular un total)."

Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:
*   La **Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
*   La **Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

## Bucles (Loops) (La Cadena de Montaje)
*   "¿Qué pasa si tenemos que actualizar 50 Oportunidades a la vez? Usamos un Bucle (Loop)."
*   "El Loop toma una lista de registros y los procesa UNO POR UNO, como en una cadena de montaje."
*   "Concepto Vital: Dentro del Loop, existe una variable mágica llamada **Current Item from Loop** (Elemento actual del bucle). Es el coche que el robot está pintando en ese preciso instante. Toda la lógica dentro del bucle debe aplicarse a esa variable temporal, no a la lista completa.

*   ¿Qué hacemos si ya tenemos 1000 duplicados? No se borran uno por uno.
*   Usamos la herramienta de **Merge** (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
*   Nunca eliminen un duplicado sin revisar qué información histórica tiene.

## Aplicación en Proyecto Real (El Descuento Automático)
1.  El cliente dice: 'Si la cuenta es Gold, aplica 20% de descuento al cerrar la venta. Si no, el 5%'.
2.  El Flow arranca cuando se gana la Oportunidad.
3.  Usamos una **Decisión** para preguntar: '¿La cuenta asociada es Gold?'.
4.  Dependiendo del camino, usamos una **Asignación** para guardar '20' o '5' en una cajita numérica llamada `VarPorcentajeDescuento`.
5.  Al final, usamos esa variable para actualizar el campo de descuento en la Oportunidad. ¡Lógica pura!

"¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path. No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'. Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

## Tips "Pro" que Salesforce no enfatiza
*   **La trampa del Bucle** (Repetición del módulo anterior porque es vital): "En este módulo aprenden Loops. ¡NUNCA usen elementos Rosas (Get/Update/Create) DENTRO del Loop! Preparen los datos en el bucle usando Asignaciones, y hagan la actualización UNA sola vez FUERA del bucle. Si no, romperán Salesforce."
*   **Nombres de Variables Claros**: "No llamen a una variable 'Var1'. Llámenla 'Var_TotalVentas_Numero'. Sean obsesivos con los nombres, o su 'yo del futuro' los odiará."
*   **Decisiones "Default"**: "Siempre configuren el 'Default Outcome' (Resultado predeterminado) en una Decisión. ¿Qué pasa si ninguna de sus condiciones se cumple? El Flow necesita saber por dónde ir si todo falla."

"¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path. No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'. Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

## Tips que NO dice Salesforce (Para aprobar este módulo)
*   **Cuidado con los nombres exactos**: "Trailhead es un robot. Si el challenge pide una variable llamada `opptyStage` y tú la llamas `OpptyStage` (con mayúscula), fallará. Copia y pega los nombres de API de las instrucciones."
*   **Tipos de Variable incorrectos**: "Muchos fallan porque crean una variable de tipo 'Texto' cuando el ejercicio pedía 'Número' para hacer un cálculo. Lean el tipo de dato dos veces."
*   **Conecta los nodos**: "A veces crean la lógica perfecta, pero olvidan conectar la flecha del 'Start' al primer elemento. ¡Asegúrense de que el flujo tenga un camino continuo!"

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
*   Hablar sobre el proceso del Trailhead
*   Ir rotando
*   No se puede estar en silencio
*   El trabajo individual es fuera de la cursada

### FLOWS 1
[LINK]

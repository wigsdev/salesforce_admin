# Salesforce Admin + Agent Force

## Daily
Tu estado actual:
*   ✊ **(Puño cerrado):** "Estoy perdido/bloqueado. Necesito ayuda urgente".
*   🖐 **(5 dedos):** "Lo domino, podría enseñarle a otro".
*   ✌️ **(2-3 dedos):** "Lo entiendo, pero necesito practicar más".

> *Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN*

## Skills Técnicas (El "Qué" haces)
*   **Gestión de Usuarios y Seguridad:** El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
*   **Gestión de Datos (Data Management):** Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
*   **Automatización Básica (Flows):** Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
*   **Reportes y Dashboards:** Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.
*   **AgentForce:** puedas familiarizarte con la configuración de agentes dentro de Salesforce.

> *Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN*

## Skills Blandas (El "Cómo" lo haces)
*   **Comunicación Traducida:** Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
*   **Resolución de Problemas (Google-Fu):** No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
*   **Mentalidad de Aprendiz (Learner's Mindset):** Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
*   **Atención al Detalle:** Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.

> *Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN*

## COLABORACIÓN
Aprender con y de otras personas

## AUSENCIAS
Seguir con la planilla y actividades

## MIC o CHAT
Comunicación

## ERRORES
Atrasados

## JUEVES
PREGUNTAS
Al final de la clase Teórica

**Para una buena clase…**
**AUTONOMÍA:** Utilizar las herramientas

---

**Vamos a ver la segunda parte de modelado de datos…**

---

## ¿Qué es un Screen Flow?
Hasta ahora, hemos visto flujos que trabajan en silencio (en el background). El Screen Flow es diferente: es el único flujo que tiene cara.

*   **Concepto Teórico:** Un Screen Flow es una interfaz de usuario guiada. En la industria del software, a esto se le llama un 'Wizard' (Asistente).
*   **Diferencia clave:** Mientras que un Page Layout muestra todos los campos a la vez, un Screen Flow muestra solo lo necesario para el paso actual. Es como un GPS: no te muestra todo el mapa del país, solo te dice 'dobla a la derecha ahora'.
*   **Uso:** Se usa para procesos complejos que requieren entrada humana: guiones de llamadas, encuestas, o formularios de alta paso a paso.

### Anatomía de la Pantalla (Inputs vs. Display)
Teóricamente, una 'Screen' (Pantalla) es un lienzo en blanco. Ustedes deciden qué pintar en él usando Componentes:

*   **Componentes de Entrada (Input):** Son preguntas que le hacemos al usuario. (Nombre, Fecha, Elección única). *Dato clave:* Estos componentes guardan lo que el usuario escribe en variables temporales.
*   **Componentes de Visualización (Display):** Sirven para dar instrucciones, mostrar advertencias o guiones de lectura. El usuario no puede editarlos.
*   **Secciones:** Nos permiten dividir la pantalla en columnas. Ya no estamos limitados a una lista vertical aburrida; podemos diseñar una interfaz moderna.

### Control y Calidad (Validación y Visibilidad)
El superpoder teórico del Screen Flow es que piensa antes de guardar.

*   **Validación de Entrada:** A diferencia de una Regla de Validación (que salta al final, cuando intentas guardar), el Screen Flow puede validar el dato en el momento que el usuario escribe. Si el formato es incorrecto, no le deja avanzar a la siguiente pantalla. Es proactivo, no reactivo.
*   **Visibilidad Condicional:** Es el concepto de 'revelación progresiva'. No asustamos al usuario con 50 campos. Si el usuario marca la casilla 'Tiene coche', entonces y solo entonces aparece el campo 'Matrícula'. La pantalla se adapta dinámicamente a las respuestas.

> Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:
> *   La **Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
> *   La **Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?
>
> Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

### El Concepto de "Contexto" (La variable recordId)
*   **¿Qué pasa si tenemos que actualizar 50 Oportunidades a la vez?** Usamos un Bucle (Loop).
*   "El Loop toma una lista de registros y los procesa UNO POR UNO, como en una cadena de montaje."
*   "Concepto Vital: Dentro del Loop, existe una variable mágica llamada **Current Item from Loop** (Elemento actual del bucle). Es el coche que el robot está pintando en ese preciso instante. Toda la lógica dentro del bucle debe aplicarse a esa variable temporal, no a la lista completa."
*   **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
*   Usamos la herramienta de **Merge (Fusionar)**. Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
*   **Nunca eliminen un duplicado sin revisar qué información histórica tiene.**

### Resumen Teórico y Best Practices
*   **Menos es más:** No pongan 20 campos en una pantalla. Usen múltiples pantallas pequeñas (Pasos) en lugar de una gigante.
*   **Claridad ante todo:** Usen el componente 'Display Text' para explicarle al usuario qué está pasando. Un flujo mudo es confuso.
*   **Protección de Datos:** El Screen Flow es el portero. Usen validaciones y valores predeterminados para asegurar que lo que entra a la base de datos sea información limpia.

"El Screen Flow es el puente donde la tecnología se encuentra con la experiencia humana.
¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path.
No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'.
Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

---

**Guia:** Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol

---

# FLOWS 1
**LINK**

# Práctica Profesional - PROYECTO

## EQUIPOS
**Proyecto - Práctica**

# JUEVES - ETAPA 3

## DAILY
**⚡ Daily (10 min):**

**Enfoque: Integridad de Datos.**
*   **Pregunta clave:** "¿La relación debe ser Master-Detail (fuerte) o Lookup (flexible)? ¿Cómo afecta esto?"

**Enfoque: Navegación.**
*   **Pregunta clave:** "¿Es intuitivo moverse entre pestañas? ¿La App tiene demasiadas cosas innecesarias?"

**Enfoque: Bloqueo de Errores.**
*   **Pregunta clave:** "¿Estamos frustrando al usuario con demasiadas validaciones o protegiendo la base de datos?"

## AMBIENTES
✅ 2 Usuarios

**PRIORIDAD:**
**Trello:**
1.  Tickets Atrasados
2.  Tickets de HOY
3.  Una vez listos se deja en la pestaña DevOps Dev

## DEV
✅ **POR DIA**
*   Tickets del día (2 personas en Dev)

**El resto del equipo:**
1.  Trails
2.  SuperBadge
3.  Análisis de Tickets
4.  Preguntas y dudas
5.  Bloqueos

**NO RECARGAR A LAS MISMAS PERSONAS POR DIA**

## FECHAS

### SPRINT 1
**Duración del Sprint:** 12 - 15 días.

**Hitos Clave:**
*   🟢 **02 Feb:** Sprint Planning (HOY - Inicio).
*   🟡 **16 Feb:** Sprint Review (Validación interna).
*   🚀 **26 Feb:** Demo (1er Entregable al Cliente).
*   🔴 **02 Mar:** Sprint Retrospective & Planning Sprint 2.

### CALENDARIO

---

# OBJETIVO
Creación de usuarios, Permission Sets, Permission Set Groups, Jerarquía y Seguridad.

**⏱️ TIP de Gestión del Tiempo:** "El Principio de Menor Privilegio".
No pierdas tiempo dando acceso a todo. Empieza restrictivo (Perfil mínimo) y abre puertas solo donde sea necesario con Permission Sets.

**⚡ Daily (5 min): Enfoque: ¿Quién ve qué?**
*   **Pregunta clave:** "¿Tenemos clara la jerarquía de roles? ¿El Manager ve lo mismo que el empleado base?"

## ROLES
**👥 Roles:**
*   **BA:** Define la matriz de accesos (Quién necesita ver/editar qué campo).
*   **PO:** Valida que la Jerarquía de Roles refleje la realidad de la empresa.
*   **Consultant:** Diseña la estructura de Permission Set Groups para no asignar permisos uno a uno.
*   **QA:** Prueba iniciar sesión con diferentes usuarios para asegurar que NO vean lo que no deben.

## SALESFORCE ADMINISTRATOR
✅ **Tareas del día (Admin):**
1.  Crear Usuarios y asignar Licencias correctas.
2.  Configurar la Jerarquía de Roles (Role Hierarchy).
3.  Crear Permission Sets y agruparlos en Permission Set Groups.
4.  Configurar OWD (Org-Wide Defaults) como base de seguridad.

## BLOQUEOS
**📢 Comunicación con TL:** Reportar inmediatamente si hay problemas de licencias o acceso al entorno. DUDAS

**¡Manos a la obra!**

Vamos ingresar para mostrarles cómo se crea una organización práctica y que todos puedan crear una.
Indiquemos que investiguen la organización, que entren y revisen
**link:** https://trailhead.salesforce.com/es/users/profiles/orgs
Compartir pantalla para que vean como se hace el proceso

**¿Cómo nos fué? ¿Qué cosas no quedaron claras y necesitamos repasar la próxima?**
retro

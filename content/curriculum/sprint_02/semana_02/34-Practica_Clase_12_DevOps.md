# Salesforce Admin + Agent Force

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

### Flujo Autolanzado (Autolaunched Flow - No Trigger)
*   **¿Qué es?:** Un flujo que no tiene un disparador propio. Espera "dormido" hasta que algo externo lo invoca.
*   **¿Quién lo despierta?:**
    *   Un humano (vía Botón o Acción rápida).
    *   Otro sistema (Apex, API REST).
    *   Otro Flujo (Subflujo).
*   **Carácterística Clave:** Se ejecuta en segundo plano (background). No tiene pantallas.
*   **Caso de Uso:** Lógica compleja que quieres reusar en varios lugares (ej: "Calcular Descuento Total" invocado desde un botón y desde una actualización de registro).

### Flujo Programado (Scheduled Flow)
*   **¿Qué es?:** Un flujo que se ejecuta automáticamente en una fecha y hora específica.
*   **¿Cómo funciona?:**
    *   **Cuándo:** Defines la frecuencia (Una vez, Diario, Semanal).
    *   **A quién:** Defines un objeto y condiciones de filtro (ej: "Todas las Oportunidades Cerradas Ganadas").
    *   **Qué hace:** El flujo se ejecuta una vez por cada registro que cumpla el filtro.
*   **Caso de Uso:** Tareas de mantenimiento o limpieza (ej: "Cerrar casos viejos todos los viernes a las 6 PM" o "Felicitar cumpleaños diariamente").

### 💡 Tips para los Retos (Hands-on Challenge)
*   **Ojo con el "Entry Criteria" en Scheduled Flows:** En los retos, asegúrate de configurar bien el objeto y el filtro al inicio del flujo (en el botón "Start"). Si no filtras bien, el flujo correrá para todos los registros de la org y puede fallar por límites.
*   **Activar es obligatorio:** A diferencia de los tests, para que un Scheduled Flow funcione realmente (o para que el Trailhead checker lo vea), a veces necesitas que esté Activo.
*   **Debug (Depuración):**
    *   **Para Autolanzados:** Puedes usar el botón "Debug" y pasarle un ID de registro de prueba.
    *   **Para Programados:** El Debug te permite probarlo como si fuera a correr ahora mismo, sin esperar a la hora programada.

---

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

# ¿Qué es DevOps?
**Como pasar los cambios de Dev a QA a PROD**

## DEV OPS - Herramienta importante
**DevOps no es un software, es una cultura.** Nace de la unión de dos palabras: Development (Desarrollo) y Operations (Operaciones).

*   Históricamente, estos dos bandos se odiaban.
*   Los desarrolladores querían meter cambios rápidos y los de operaciones querían frenar todo para que el sistema no cayera.
*   DevOps es el arte de automatizar y unir estos dos mundos para entregar valor al cliente más rápido, pero sin romper nada en el camino.

Hoy vamos a entender por qué fallan los proyectos. No fallan por código, fallan por comunicación. El cliente habla de 'dolores' y 'dinero', y Salesforce habla de 'Objetos' y 'Flows'. Nuestro trabajo es ser el puente entre esos dos mundos. Vamos a ver los roles que hacen esto posible.

### La Pesadilla (Sin DevOps)
**¿Por qué necesitamos esto?**

*   Imaginen el 'Viejo Mundo': Ustedes hacen un cambio en su entorno de desarrollo. Lo copian manualmente a Producción. Y de repente... **¡Pum! Todo deja de funcionar.**
*   ¿Por qué? Porque en su entorno tenían un campo que en Producción no existía.
*   O peor, sobrescribieron el trabajo de un compañero.
*   **Sin DevOps, mover cambios es como llevar una bandeja de copas de cristal corriendo por una escalera: es manual, lento y muy riesgoso.**

### El Ciclo Infinito (Cómo funciona)
DevOps propone que el software nunca termina, es un ciclo infinito.
1.  **Planifican** (Trello).
2.  **Construyen** (Salesforce).
3.  **Testeamos** (Aquí entra QA).
4.  **Liberamos** (Release a Producción).

La clave es que este ciclo debe ser automatizado. No queremos mover archivos a mano. Queremos un botón que diga 'Desplegar' y que una máquina haga el trabajo sucio y repetitivo por nosotros.

### ¿Para qué sirve? (Los 3 Pilares)
Si les preguntan en una entrevista para qué sirve DevOps, respondan esto:
*   **Velocidad:** Pasamos de hacer 1 despliegue al mes (con miedo) a hacer 10 al día.
*   **Calidad:** Al obligarnos a pasar por entornos de prueba (QA), reducimos los errores que llegan al usuario final.
*   **Control de Versiones (El salvavidas):** Esto es lo más importante. DevOps usa sistemas como Git que guardan una 'foto' de cada cambio. Si rompemos algo hoy, podemos 'viajar en el tiempo' a la versión de ayer en un segundo.

### ¿Para qué sirve? (Los 3 Pilares)
Para terminar, quédense con este concepto: **El Pipeline.** Imaginen una tubería de agua con filtros.
*   El agua sucia entra por **DEV** (donde experimentamos).
*   Pasa por un filtro llamado **QA** (donde limpiamos errores).
*   Y sale agua pura en **PROD** (lo que usa el cliente).

**DevOps Center**, que vamos a usar ahora, es la herramienta que construye esa tubería para que nosotros no tengamos que cargar los baldes de agua a mano.

---

**¡Manos a la obra!**

Vamos ingresar para mostrarles cómo se crea una organización práctica y que todos puedan crear una.
Indiquemos que investiguen la organización, que entren y revisen
**link:** https://trailhead.salesforce.com/es/users/profiles/orgs
Compartir pantalla para que vean como se hace el proceso

**¿Cómo nos fué? ¿Qué cosas no quedaron claras y necesitamos repasar la próxima?**
retro

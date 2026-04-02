# 🎬 Guion de Presentación — Sprint 2: Lumina Tech
### *Revisión de Entregables para la Dirección Académica*
**Audiencia:** Dra. Elena Vance (Rectora) y equipo directivo de Lumina Tech  
**Tono:** Profesional, ejecutivo, orientado a resultados de negocio  
**Duración estimada:** 20–25 minutos

---

## 🎙️ Apertura

> *[El consultor toma la palabra. Se proyecta el logo de Lumina Tech.]*

Buenas tardes a todos.

En esta sesión les presentaremos los resultados del **Sprint 2** del proyecto de implementación de Salesforce para Lumina Tech. En este sprint, partimos del problema que ustedes identificaron con claridad en la solicitud inicial: tenían un sistema lleno de datos sin poder acceder a ellos, procesos manuales que consumen horas de sus equipos y cero visibilidad para la toma de decisiones.

Hoy, en 20 minutos, les vamos a mostrar que esos tres problemas **ya tienen solución operativa y funcionando en el sistema.**

Organizamos el trabajo en tres bloques que responden directamente a sus prioridades:

1. 📂 **El desastre del Excel histórico** — cómo lo migramos con integridad
2. ⚙️ **Las automatizaciones** — el sistema que ahora "piensa solo"
3. 📊 **El tablero de control** — los números que usted necesita ver

Comencemos.

---

## 📂 BLOQUE 1: La Migración de Datos Históricos
### *"Dra. Vance, los 1.000 alumnos ya están en el sistema."*

Usted nos planteó que su secretaria tardaría **3 meses en cargar a mano** el archivo histórico con los registros de alumnos, materias, inscripciones y notas. Nuestra respuesta fue diseñar una estrategia de migración en **cinco fases secuenciales**, donde cada etapa valida que la anterior esté correcta antes de avanzar. No migramos datos; migramos información con integridad.

**Antes de mover un solo dato**, configuramos dos barreras de protección críticas:

- Primero, marcamos el campo `Número de Documento` como **identificador único externo**. Esto significa que Salesforce ahora es incapaz de crear dos alumnos con el mismo DNI. Es un candado a nivel de base de datos.
- Segundo, activamos reglas de duplicidad que evalúan nombre, apellido y correo electrónico con lógica aproximada. Si alguien intenta ingresar a "Juan Pérez" y ya existe "Juan Perez" *(sin tilde)*, el sistema lo detecta y bloquea la operación.

¿Por qué esto importa? Porque **limpiar una base de datos corrupta cuesta diez veces más que evitar que se corrompa desde el inicio.**

Una vez blindado el sistema, procedimos con la migración en este orden:

| Fase | Qué se cargó | Técnica usada |
|:---|:---|:---|
| 1 | Carreras universitarias | Upsert por código de carrera |
| 2 | Alumnos (Contactos) | Upsert por Número de Documento |
| 3 | Materias (Catálogo de asignaturas) | Upsert por código de materia |
| 4 | Inscripciones (alumno ↔ materia) | Insert con llave única compuesta |
| 5 | Evaluaciones y notas históricas | Upsert con identificador de evaluación |

Un dato técnico relevante para el directorio: durante la carga de alumnos, **desactivamos temporalmente los flujos de correo automático** precisamente para que no se dispararan miles de correos de bienvenida a ex-alumnos que ya no son parte activa de la institución. Esa fue una decisión de arquitectura defensiva que protegió la imagen institucional de Lumina Tech.

**Resultado:** Los 1.000 registros históricos están disponibles en Salesforce, listos para ser consultados, reportados y vinculados a los nuevos procesos que les vamos a mostrar a continuación.

---

## ⚙️ BLOQUE 2: Las Automatizaciones — El Sistema que Piensa Solo
### *"El problema que tenían: perseguir personas y tareas. La solución: Salesforce lo hace por ustedes."*

Ustedes nos pidieron tres automatizaciones puntuales. Vamos una por una.

---

### ✉️ Automatización 1: El Correo de Bienvenida
**El problema original:** Cada vez que se inscribía un alumno nuevo, el equipo de admisiones perdía entre 10 y 15 minutos redactando manualmente un correo de bienvenida. Con 500 inscripciones al año, eso equivale a **más de 80 horas laborables perdidas** en una tarea repetitiva.

**Lo que construimos:** Un flujo automático activado en el instante en que se crea un nuevo registro de alumno en Salesforce. En ese momento, sin intervención humana, el sistema envía un correo de bienvenida con el diseño institucional de Lumina Tech —incluyendo logos, colores y el nombre personalizado del estudiante.

**Una decisión de diseño importante:** Este correo solo se activa cuando el alumno es ingresado "por ventanilla" —es decir, por el personal de recepción de forma individual. Esto impide que la automatización se dispare durante las cargas masivas de datos históricos, protegiendo la bandeja de entrada de sus ex-alumnos y la reputación de la institución.

**Resumen ejecutivo:** Si hoy su equipo inscribe a 10 alumnos, esos 10 alumnos reciben su correo de bienvenida sin que nadie lo haya redactado. El equipo de admisiones puede dedicar ese tiempo a tareas de mayor valor.

---

### 🖥️ Automatización 2: El Asistente de Carga Rápida para Recepción
**El problema original:** El personal de recepción se perdía en la pantalla estándar de Salesforce, que tiene decenas de campos. Esto generaba errores en la carga de datos y lentitud en la atención presencial.

**Lo que construimos:** Un asistente visual tipo "paso a paso" —técnicamente llamado Screen Flow— diseñado específicamente para el uso en ventanilla. El operador ve únicamente los datos esenciales:

```
[ Nombre ]         [ Apellido ]
[ Tipo de Documento: ○ DNI  ○ Carnet de Extranjería  ○ Pasaporte ]
[ Número de Documento * ]
[ Correo Electrónico * ]
[ Teléfono / Celular * ]
                           [ Cargar Alumno ]
```

**Decisiones de diseño que tomamos para el cliente:**

- **El campo "Tipo de Documento"** fue añadido como mejora respecto a la solicitud original. En una institución que atiende alumnos con DNI, Carnet de Extranjería y Pasaporte, no tiene sentido hardcodear un solo tipo. Ahora el sistema acepta los tres, con los mismos valores que ya existen en la base de datos.
- **La ubicación del asistente:** decidimos publicarlo en la barra inferior de la aplicación (Utility Bar), no en la página principal. Esto significa que el operador puede abrir el asistente con un clic desde cualquier pantalla, sin perder el contexto de lo que estaba haciendo.
- **La pantalla de confirmación:** Al guardar exitosamente, el sistema muestra un mensaje claro: *"Alumno registrado. Recibirá un correo de bienvenida."* El operador tiene certeza inmediata de que la operación fue exitosa.
- **El manejo de errores:** Si el operador intenta ingresar un DNI que ya existe en la base de datos, el sistema no colapsa ni muestra un error técnico. Muestra un mensaje amigable que le indica qué ocurrió y le ofrece la opción de reintentar. Esto es lo que en la industria llamamos "arquitectura defensiva".

**Resumen ejecutivo:** El personal de recepción ahora tiene una herramienta diseñada para su flujo de trabajo real. Menos errores, menos tiempo de capacitación para personal nuevo, y una experiencia de atención más rápida para el alumno que está físicamente en la ventanilla.

---

### 📋 Automatización 3: El Barrido Semanal de Actas Pendientes
**El problema original:** Los profesores olvidan cargar notas. Bedelía tiene que perseguirlos manualmente. Los alumnos sin nota no pueden acceder a correlatividades ni a sus certificados en tiempo y forma. Esto representa un riesgo legal y académico para la institución.

**Lo que construimos:** Un proceso automático que se ejecuta todos los **viernes a las 17:00 hs** —tal como lo solicitó Rectorado— y realiza lo siguiente:

1. Escanea todas las inscripciones cuya fecha de cierre ya pasó.
2. Identifica aquellas donde la nota está vacía *(distinguiendo correctamente entre "el profesor no cargó nada" y "el alumno obtuvo cero o fue marcado como ausente", que son situaciones diferentes)*.
3. Si detecta una omisión real, **crea automáticamente una tarea** asignada al profesor responsable con el asunto: *"Urgente: Cierre de Acta Pendiente"*, con fecha límite de dos días.
4. **Protección anti-duplicación:** Si ese mismo profesor ya tiene una tarea abierta por el mismo acta de la semana anterior y todavía no la resolvió, el sistema **no genera una segunda tarea**. Evitamos así una avalancha de notificaciones repetidas que perderían impacto.

**Una propuesta consultiva que dejamos documentada:** Técnicamente recomendamos evaluar mover el horario de ejecución a las 23:00 hs. Un escaneo masivo a las 17:00 hs coincide con el pico de uso del sistema —cuando los profesores todavía están cargando notas—, lo que puede afectar el rendimiento. Esta propuesta fue documentada y queda a decisión de la Dirección.

**Resumen ejecutivo:** Bedelía ya no tiene que recordar revisar las actas. El sistema lo hace solo, genera la alerta al docente responsable, y lo hace de forma inteligente sin generar ruido innecesario. El cumplimiento académico pasó de ser un proceso reactivo a uno proactivo.

---

## 📊 BLOQUE 3: El Tablero de Control
### *"Dra. Vance, usted nos dijo que volaba a ciegas. Eso cambió."*

Construimos tres tableros de control —Dashboards— con acceso restringido exclusivamente a los perfiles de Rectorado y Dirección. Cualquier usuario estándar (docentes, administrativos) que intente acceder a estos tableros verá acceso denegado. La información estratégica tiene protección por rol.

**Tablero 1 — Alumnos inscritos por carrera y año:**
- Gráfico de torta con la distribución de alumnos activos, permitiendo a Rectorado filtrar dinámicamente cohortes anuales (Ej: 2024-1 vs 2025-1).

**Tablero 1.1 — Alumnos reprobados por mes:**
- Listado en tiempo real de alumnos con notas menores a 6. **Decisión Arquitectónica:** Separamos este reporte del Tablero 1 original debido a que su necesidad de filtrado mensual estricto ("Filter by Mes_Año") reñía con el filtrado anual de las carreras. Mantenerlos separados garantiza el rendimiento y la integridad de las métricas.

**Tablero 2 — Gestión de Profesores:**
- Reporte de cuántas materias dicta cada docente, para detectar sobrecargas de trabajo.
- Reporte de asistencia por materia, identificando cuáles tienen mayor índice de ausentismo.

**Tablero 3 — Calidad de Datos y Auditoría:**
- Listado de alumnos con datos de contacto incompletos (sin email o sin teléfono), para que Administración pueda contactarlos y completar los registros.
- Gráfico lineal con la evolución de inscripciones mes a mes durante el último año, permitiendo identificar estacionalidades y planificar recursos.

**Resumen ejecutivo:** Cada uno de estos tableros puede ser consultado por usted en tiempo real, desde cualquier dispositivo, sin necesidad de que alguien le prepare un informe. La toma de decisiones ahora está respaldada por datos actualizados al momento.

---

## 🔒 CIERRE: Lo que entregamos y lo que protegimos

> *[Se proyecta una diapositiva resumen.]*

Quiero cerrar con la perspectiva del equipo técnico.

En este Sprint no solo implementamos lo que se pidió. Tomamos decisiones de arquitectura para **proteger la inversión a largo plazo:**

- **No hay IDs fijos** en las automatizaciones. Están diseñadas para funcionar igual en el entorno de desarrollo y en producción.
- **El correo de bienvenida tiene una barrera anti-spam** que protege a la institución de errores comunicacionales durante futuras cargas masivas.
- **Los errores del asistente de recepción** muestran mensajes entendibles, no pantallas rojas de sistema que nadie sabe cómo interpretar.
- **La auditoría de actas no genera ruido repetitivo**: si un problema persiste, el docente recibe una sola alerta por semana, no cinco.

Todo esto, señora Rectora, está documentado. Cada decisión, cada alternativa descartada y cada decisión de negocio tomada queda registrada en la documentación técnica del proyecto para que sea mantenible por cualquier Administrador Salesforce certificado en el futuro.

---

## ❓ Espacio para Preguntas

> *[El consultor abre el espacio.]*

Con esto concluimos la presentación del Sprint 2. Tenemos tiempo para sus preguntas.

A modo de agenda para los próximos pasos, les propongo tres acciones concretas:

1. **QA con usuarios reales:** idealmente que una persona del equipo de recepción pruebe el asistente en el entorno de desarrollo esta semana.
2. **Validar el correo de bienvenida:** confirmar que el diseño institucional y el contenido del mensaje representan la voz de Lumina Tech.
3. **Decisión de horario de la auditoría:** confirmar si se mantiene el horario de 17:00 hs o si aceptan la propuesta técnica de moverlo a las 23:00 hs.

Muchas gracias por su tiempo y confianza.

---
*Documento preparado por el equipo técnico de implementación Salesforce — Lumina Tech Sprint 2.*  
*Versión 1.0 — Fecha: Marzo 2026*

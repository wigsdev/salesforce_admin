# HISTORIAS DE USUARIO - SPRINT 2

## 🏗️ ÉPICA 1: Carga Inicial de Datos Históricos y Limpieza (Data Quality)

**Objetivo:** Migrar registros de un sistema legado asegurando la integridad transaccional y previniendo duplicidad de datos.

---

### HU-201A: Configuración Preventiva de Duplicados (Spike Técnico)
**Estimación:** 🟡 2 SP  
**Prioridad:** Crítica (Bloqueante para HU-201B)  
**Enlace Req:** `[REQ-MIG-001-A]`

**Descripción:**  
Como **Arquitecto de Datos**, Quiero configurar las capas de prevención de duplicados en Salesforce (Reglas y External IDs) antes de procesar el archivo adjunto `Historico_Alumnos_2024.csv`, Para garantizar que la inminente migración masiva y la carga diaria manual no genere registros basura ni alumnos clonados en el sistema.

**⛔ Pre-requisitos (Dependencias):** N/A. Esta historia es el cimiento de la Arquitectura de Datos del Sprint 2 y debe ejecutarse primero.

**💡 Justificación (Business Value):** Evita la "deuda técnica" desde el día 1. Limpiar una base de datos ya corrupta cuesta 10 veces más trabajo (y dinero) que evitar que se corrompa en la entrada.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Base de Datos (Herramienta: Setup > Object Manager):** Configurar los campos `Numero_Documento__c` y `Codigo_Unico__c` (Legajo) en el Objeto `Contact`, marcando ambas casillas como **Unique** y **External ID**. Esto habilitará la "Base Dura" para el Upsert.
2. **Matching Rules (Herramienta: Setup > Duplicate Management):** Configurar y activar una regla para el objeto Contacto que evalúe `Nombre + Apellido + Email` (con lógica Fuzzy/Aproximada).
3. **Duplicate Rules (Herramienta: Setup > Duplicate Management):** Crear una regla que aplique la Matching Rule anterior, configurada con la acción en modo **"Block"** (Bloquear) tanto para Creación como para Edición si hay sospecha de clonación.

**✅ Criterios de Aceptación (QA Check):**
1. Verificar visualmente en Setup que Numero_Documento__c y Legajo tienen el tilde en **External ID**.
2. Intentar crear manualmente un Contacto ficticio con un `Numero_Documento__c` o Nombre idéntico al de un registro existente; el sistema debe arrojar un cartel rojo de error nativo bloqueando la acción.

---

### HU-201B: Limpieza de Data Excel y External IDs (Data Cleansing)
**Estimación:** 🟡 3 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-MIG-201B]`

**Descripción:**  
Como **Analista de Datos**, Quiero tomar el Excel maestro provisto por Rectorado y curarlo usando funciones nativas (Buscar y Reemplazar, Fórmulas) según las reglas de negocio de la Rectora Elena, Para alimentar los 4 archivos CSV finales libres de errores tipográficos y de formato que consumirá Data Loader.

**⛔ Pre-requisitos (Dependencias):** N/A.

**💡 Justificación (Reglas de Negocio Oficiales):**
- **Teléfonos:** Formato internacional requerido para futuras alertas WhatsApp (`+54 9`).
- **Emails:** Estrictamente sin tildes y con espacios reemplazados por puntos para evitar rebotes de automatizaciones. Mantener guiones si existen.
- **Nombres/Apellidos:** Obligatorio mantener tildes para emisión formal de diplomas.
- **Edades:** Ignorar (dejar vacío) si no existe en el sistema legado.

**⚙️ Pasos de Implementación (Data Analyst Task - En Excel):**
1. **Data Cleansing (Correos):** Seleccionar la columna Emails. Usar Buscar y Reemplazar (`Ctrl+L` / `Ctrl+H`) para cambiar espacios por puntos `.`, y quitar tildes (`á`->`a`, `é`->`e`, etc).
2. **Data Cleansing (Teléfonos):** Seleccionar la columna Teléfonos. Usar Buscar y Reemplazar para cambiar el prefijo local `+54 15` a formato internacional `+54 9`.
3. **Extracción - Contactos (`01_Carga_Contactos.csv`):** Aislar la hoja de Alumnos. Mantener tildes en nombres. Dejar en blanco "Fecha de Nacimiento". Remover duplicados de Numero_Documento__c.
4. **Extracción - Materias (`02_Carga_Materias.csv`):** Aislar las Asignaturas (incluidas las nuevas 2025). Remover duplicados de `Codigo_Materia`.
5. **Extracción - Inscripciones/Evaluaciones (03 y 04):** Copiar la pestaña de historial cruzado. En Excel, generar las llaves únicas para evitar colisiones:
    - **ID_Importacion (Inscripción):** Aplicar la fórmula `= [DNI] & "_" & [Codigo_Materia] & "_" & [Anio_Lectivo]`. (Ej: `12345678_MAT101_2024-1`).
    - **ID_Evaluacion (Evaluación):** Aplicar la fórmula `= [ID_Importacion] & "_" & [Fecha_Examen]`. (Ej: `12345678_MAT101_2024-1_2024-03-15`).
    Extraer un archivo `03_Carga_Inscripciones.csv` y otro `04_Carga_Evaluaciones.csv` con estas nuevas huellas digitales listas para cruce por Data Loader.

**✅ Criterios de Aceptación (QA Check):**
1. Validar que los registros del CSV `Historico_Alumnos_2024.csv` e `Historico_Alumnos_2025.csv` informen éxito (Success) sin fallos formativos.
2. En el reporte el campo `Fecha_Examen` debe cumplir con el formato `YYYY-MM-DD`
3. En el reporte el campo `Nombre` debe cumplir
4. En el reporte el campo `Apellido` debe cumplir
5. En el reporte el campo `Numero_Documento__c` debe cumplir
6. En el reporte el campo `Email` debe cumplir
7. En el reporte el campo `Telefono` debe cumplir
8. En el reporte el campo `Codigo_Materia` debe cumplir
9. En el reporte el campo `Nombre_Materia` debe cumplir
10. En el reporte el campo `Nota` debe mostrar valores del 0 al 10
11. En el reporte el campo `Estado` debe cumplir

---

### HU-201C: Importación 1 - Carreras
**Estimación:** 🟡 2 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-MIG-201C]`

**Descripción:**  
Como **Administrador Salesforce**, Quiero inyectar el catálogo de carreras universitarias usando Data Loader, Para establecer la estructura académica base del sistema.

**⛔ Pre-requisitos (Dependencias):** Setup listo (Épica 0 finalizada). El campo `Abreviatura__c` debe existir en el objeto `Carrera__c` y tener marcado **External ID**. Los campos `Duracion_de_la_carrera` y `Facultad` deben tener temporalmente el check de Required removido para la carga inicial.

**⚙️ Pasos de Implementación (Admin Task):**
1. Usar Data Loader > **Upsert** en objeto `Carrera__c`.
2. Seleccionar `Abreviatura__c` como llave de cruce (**External ID**).
3. Mapear `Name` -> `Name` y `Abreviatura__c` -> `Abreviatura__c`.
4. Una vez cargado, volver a marcar como Required los campos de Facultad y Duración si es necesario para mantener la integridad.

**✅ Criterios de Aceptación (QA Check):**
1. Verificar que las carreras se han creado correctamente en Salesforce.
2. Confirmar que el campo `Abreviatura__c` actúa como identificador único.

---

### HU-201D: Importación 2 - Contactos (Alumnos)
**Estimación:** 🟢 1 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-MIG-201B]`

**Descripción:**  
Como **Administrador Salesforce**, Quiero inyectar el catálogo de alumnos usando Data Loader contra el objeto `Contact`, Para tener la base poblacional activa.

**⛔ Pre-requisitos (Dependencias):** Apagar Flows (Ej. Emails Automáticos). Setup listo (Épica 0 finalizada).

**⚙️ Pasos de Implementación (Admin Task):**
1. **Desactivación Preventiva:** Ir a `Setup > Duplicate Management > Duplicate Rules`. Desactivar temporalmente las reglas de duplicidad para el objeto `Contact` (Nombre, Apellido y Email) para permitir la carga masiva sin bloqueos.
2. **Preparación de Datos:** Concatenar nombre y apellido en el CSV si fuera necesario, o mapear directamente los campos recuperados.
3. Usar Data Loader > **Upsert** en objeto `Contact`.
4. Seleccionar como llave cruzada el campo `Numero_Documento__c` (External ID).
5. **Mapeo Avanzado (Forzar Constantes):** Como el equipo no utiliza scripts de limpieza y el CSV no posee columnas para los picklists obligatorios, el Administrador debe **FORZAR** estos valores directamente en la interfaz de "Mapping" de Data Loader. Deberá introducir manualmente el valor `'DNI'` (con comillas simples) apuntando al campo `Tipo_Documento__c`, y `'Alumno'` apuntando al campo `Rol__c`.

---

### HU-201E: Importación 3 - Materias (Catálogo)
**Estimación:** 🟢 1 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-MIG-201C]`

**Descripción:**  
Como **Administrador Salesforce**, Quiero inyectar las asignaturas únicas de la universidad usando Data Loader, Para establecer la malla contra la cual los alumnos cursaron sus notas.

**⛔ Pre-requisitos (Dependencias):** Setup listo (Épica 0 finalizada).

**⚙️ Pasos de Implementación (Admin Task):**
1. Usar Data Loader > **Upsert** en objeto `Materia__c`.
2. Seleccionar como llave cruzada el campo `Codigo_Materia__c` (External ID).
3. Forzar campos requeridos de G6 si hiciera falta.

---

### HU-201F: Importación 4 - Inscripciones (Junction Object)
**Estimación:** 🟡 3 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-MIG-201D]`

**Descripción:**  
Como **Administrador Salesforce**, Quiero enlazar a Alumnos y Materias mediante el objeto transaccional Inscripción, Para materializar la presencia académica del alumno en las aulas.

**⛔ Pre-requisitos (Dependencias):** HU-201B y HU-201C debieron poblar Alumnos y Materias exitosamente.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Desactivación de Seguridad Académica:** Ir a `Setup > Object Manager > Inscripcion__c`. Localizar los campos `Alumno__c` y `Materia__c` y desactivar temporalmente cualquier **Lookup Filter** activo. Esto es vital para permitir que Data Loader vincule registros históricos que podrían no cumplir con las reglas de validación de negocio actuales (ej. Alumnos inactivos).
2. Usar Data Loader > **Insert** o **Upsert** en objeto `Inscripcion__c`.
3. **Súper Crítico:** Mapear la columna calculada del CSV (`ID_Importacion` = `"34444555_MAT101_2024-1"`) directo contra nuestro nuevo campo External ID `ID_Importacion__c`. Esta llave asegura que la inscripción sea única para ese alumno, materia y periodo específico.
4. Mapear la relación de Contact cruzando por Numero_Documento__c, y la de Materia cruzando por `Codigo_Materia__c`.
5. Forzar cualquier Picklist requerido estipulado por G6 (Ej: `Periodo_Academico__c` = `"2024-1"`, `Concepto__c` = `"Matricula"`).

---

### HU-201G: Importación 5 - Evaluaciones (Notas Históricas)
**Estimación:** 🟡 2 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-MIG-201E]`

**Descripción:**  
Como **Administrador Salesforce**, Quiero cargar las notas, fechas de examen y resultados usando Data Loader hacia Evaluaciones, Para registrar el éxito académico del padrón que acabo de inscribir.

**⛔ Pre-requisitos (Dependencias):** HU-201D (Inscripciones vivas).

**⚙️ Pasos de Implementación (Admin Task):**
1. Usar Data Loader > **Upsert** en objeto `Evaluacion__c`.
2. Seleccionar `ID_Importacion__c` (o el nombre del campo que actúe como External ID en Evaluación) como llave de cruce, usando el valor de la columna `ID_Evaluacion` del CSV.
3. Mapear Nota hacia el campo numérico (`Examen_Final__c`).
4. Mapear Fecha_Examen hacia `Fecha_de_Examen__c`.
5. **Súper Crítico:** En la pantalla **Mapping**, decirle a Data Loader que el Padre (`Inscripcion__c`) no se cruzará por el Id nativo de Salesforce, sino a través del campo intermedio `ID_Importacion__c` del objeto Inscripción. Proveerle la columna de Excel `ID_Inscripcion` (que contiene el valor `DNI_Materia_Periodo`) para que enganche la nota a la inscripción adecuada.

---

## 🏗️ ÉPICA 2: Generación de Automatizaciones Core

**Objetivo:** Reducir la carga de trabajo manual del equipo (Flows y Emails).

---

### HU-202: Envío de Correo de Bienvenida (Automatización Simple)
**Estimación:** 🟢 1 SP  
**Prioridad:** Media  
**Enlace Req:** `[REQ-AUTO-002]`

**Descripción:**  
Como **Personal de Admisiones**, Quiero que el sistema envíe un correo electrónico de "Bienvenida a Lumina Tech" automáticamente cuando registro a un alumno nuevo, Para ahorrar 10 minutos por alumno en redacción de correos y asegurar una comunicación estandarizada con el estudiante.

**⛔ Pre-requisitos (Dependencias):** N/A funcional, pero su activación en producción (Go-Live) exige que la Migración Histórica masiva (HU-201B) haya concluido rigurosamente para prevenir envíos masivos accidentales a exalumnos.

**💡 Justificación (Business Value):** Retorno de Inversión (ROI) directo en tiempo humano. Si se inscriben 500 alumnos, se ahorran más de 80 horas laborables del equipo de Admisiones. Además, estandariza la comunicación institucional (Branding) garantizando que todo estudiante reciba exactamente la misma información oficial, mejorando radicalmente la experiencia del usuario (Student Journey).

**⚙️ Pasos de Implementación (Admin Task):**
1. **Definición de Plantilla Institucional (Estándar UI):** Como regla general en universidades y empresas serias, un correo de bienvenida debe tener diseño institucional (Branding, Logos, HTML). Construir un **Lightning Email Template** atractivo que contenga los colores de Lumina Tech y campos combinados o Merge Fields (Ej: `{!Contact.Name}`). (Bajo ninguna circunstancia usar Classic Email Templates).
2. Crear un **Record-Triggered Flow** en el objeto `Contact`, que corra en modo **Actions and Related Records (After Save)** cuando *"A record is created"*.
3. **Arquitectura Defensiva (Constraints):** Agregar en la configuración inicial del Flow los "Condition Requirements" obligatorios para filtrar la ejecución exclusivamente si: a) Record Type equivale a "Alumno", b) El campo Email no se encuentre vacío (Is Null = False para evitar error fatal del send email engine), AND c) La "Fuente de Origen" provenga desde "Ventanilla" para bloquear la catástrofe comunicacional en cargas masivas asíncronas de base de datos.
4. **Acción de Envío:** Según lo definido en el paso 1, añadir la acción nativa **Send Email** del Flow (recomendado para la mayoría de casos modernos por su facilidad para armar plantillas rich text in-situ) o disparar un **Email Alert** atado a un Lightning Email Template (si hay HTML complejo). Configurar destinatario (`{!$Record.Email}`).
5. **Protocolo del Administrador (Go-Live):** Este Flow debe activarse (Turn On) SOLO Y ÚNICAMENTE después de que el Equipo de Migración Histórica dé por concluida la subida de datos pasada de la HU-201.

**✅ Criterios de Aceptación (QA Check):**
1. Crear un Contacto y otorgarle tipo "Profesor" (o similar). Verificar que no llegue ningún correo de notificación al email definido.
2. Crear un nuevo Contacto seleccionando el record Type "Alumno", llenando exitosamente el email.
3. Verificar en la bandeja de entrada real del email proporcionado la recepción del correo personalizado de bienvenida Lumina Tech.

---

### HU-203: Asistente UI para Carga Rápida de Alumnos (Screen Flow)
**Estimación:** 🟡 3 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-UI-001]`

**Descripción:**  
Como **Personal de Recepción**, Quiero una pantalla simplificada tipo "asistente" (wizard) para registrar nuevos alumnos que me pida Nombre, Apellido, Tipo de Documento, Número de Documento, Correo Electrónico y opcionalmente Teléfono, Para cargar datos ágilmente mientras atiendo al público en el mostrador, sin perderme en el extenso Page Layout estándar. Al finalizar, el sistema debe confirmar visualmente que el alumno fue registrado con éxito.

**⛔ Pre-requisitos (Dependencias):** HU-201A debe estar activa y probada (Las validaciones de duplicidad son el escudo nativo que protegerá al Screen Flow de excepciones DML en vivo). El campo `Fuente_de_Origen__c` (Picklist: Ventanilla, Migración Histórica) debe existir en el objeto Persona (Contact) para activar el correo de bienvenida de HU-202. El campo `Rol__c` debe existir y tener el valor `Alumno` disponible en su picklist.

**💡 Justificación (Business Value):** Incrementa la velocidad de atención en ventanilla en picos de inscripción, reduciendo las colas de espera físicas en la universidad. Al minimizar los campos visibles mediante un Screen Flow, se reduce dramáticamente la curva de aprendizaje para empleados temporales o nuevos en Recepción, y se protege la integridad de los datos financieros a los que no deben tener acceso durante la carga inicial.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Definición de UI:** Publicar el flow en la **Utility Bar** de la app académica (Setup > App Manager > Utility Items). Label: `Registrar Alumno`. Esta ubicación permite al operador abrirlo desde cualquier pantalla.
2. Crear un **Screen Flow** con Label: `Lumina Asistente Carga Recepcion`.
3. Montar un componente Pantalla con estos campos **en orden**: `Name` (API: `NombreAlumno`, obligatorio) | `Radio Buttons` con **Picklist Choice Set** sobre `Tipo_de_Documento__c` del objeto Persona (API: `TipoDocumento`, obligatorio) | `Text` Número de Documento (obligatorio) | `Email` (API: `InputCorreo`, obligatorio) | `Phone` Teléfono (API: `InputTelefono`, **opcional**).
4. Footer: ocultar Pause y Previous. Botón de avance: `Guardar Alumno`.
5. *(Nota arquitectónica: Este entorno no usa Record Types en Persona/Contact. No añadir nodo Get Records de RecordType)*.
6. Insertar **Create Records** sobre objeto `Persona` mapeando: `First Name`, `Last Name`, `Tipo_de_Documento__c` ← `{!TipoDocumento}`, `Numero_Documento__c`, `Email` ← `{!InputCorreo.value}`, `Phone` ← `{!InputTelefono.value}`, `Rol__c` ← literal `Alumno` *(campo obligatorio en el entorno)*, `Fuente_de_Origen__c` ← literal `Ventanilla` *(activa HU-202)*.
7. Añadir **pantalla de éxito** después del Create Records: mensaje *"✅ Alumno registrado exitosamente. Recibirá un correo de bienvenida."* Botón: `Registrar Otro Alumno`.
8. **Fault Path:** desde Create Records hacia una pantalla con mensaje amigable + `{!$Flow.FaultMessage}` para diagnóstico del Administrador. Botón: `Reintentar`.

**✅ Criterios de Aceptación (QA Check):**
1. Abrir el flow desde la **Utility Bar** de la app académica.
2. Completar todos los campos obligatorios y presionar `Guardar Alumno`. Verificar que aparece la pantalla de éxito y el registro fue creado con `Fuente_de_Origen__c = Ventanilla` y `Rol__c = Alumno`.
3. Verificar que el alumno recibió el correo de bienvenida de HU-202.
4. **Prueba Negativa (Stress Test):** Intentar registrar un alumno con un Número de Documento existente. El Flow debe mostrar la pantalla de error amigable con `{!$Flow.FaultMessage}` y el botón `Reintentar`, sin colapsar.

---

### HU-204: Auditoría de Cierre de Actas (Scheduled Flow)
**Estimación:** 🔴 5 SP  
**Prioridad:** Crítica  
**Enlace Req:** `[REQ-AUTO-003]`

**Descripción:**  
Como **Rectora de Lumina Tech**, Quiero que el sistema revise automáticamente todos los viernes a las 17:00 hs si existen clases/exámenes finalizados que no tienen nota cargada y genere una tarea al respecto, Para evitar perseguir manualmente a profesores morosos y garantizar el cierre del ciclo académico en tiempo y forma.

**⛔ Pre-requisitos (Dependencias):** HU-201C finalizada (Para tener registros de inscripciones a evaluar). Estructura del Sprint 1 (Ausente__c y nota) debe estar validada para el control algorítmico de Nulos.

**💡 Justificación (Business Value):** Mitiga el riesgo de compliance académico y legal. Los estudiantes necesitan sus notas oficiales para mantener becas o correlatividades. Este Scheduled Flow automatiza la labor de auditoría reactiva de Bedelía, transformando un proceso de control manual frustrante ("perseguir profesores") en un sistema proactivo manejado por Salesforce, liberando a la dirección académica para tareas estratégicas.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Hora de Ejecución (Petición de Negocio):** Acatando explícitamente el documento original de Rectorado, crear un **Schedule-Triggered Flow** configurado con una periodicidad semanal para ejecutarse los días viernes a las 17:00 hs.
2. **Recomendación Consultiva (Performance):** Elevar la propuesta al cliente de mover este horario a las 23:00 hs. Un escaneo Batch en pleno horario administrativo ralentiza el ecosistema Salesforce y colisiona con el último horario de carga de los profesores.
3. Definir lógicas de consulta **Get Records** sobre el objeto Inscripción donde la Fecha de Cierre sea menor a `{!$Flow.CurrentDate}`.
4. Incluir un **Loop** y **Decisión** validando omisiones. Control de Nulos vs Ceros: La lógica debe discernir entre un campo de calificación IS NULL (Olvido de carga) versus un 0 o check de Ausente (Que sí es una carga válida).
5. **Protección Anti-Spam de Tareas:** Antes de ejecutar la acción final, introducir un validación condicional (Get Record del Objeto Task) cruzando el Id de la inscripción para comprobar que no existan previas tareas auditadas "Abiertas". Si un profesor continúa sin subir la nota la siguiente semana, no crear tareas duplicadas consecutivas sobre-avisando el mismo problema de acta.
6. Para cada nueva inconsistencia real (IS NULL sin tarea vigente), levantar una acción creando un registro en el objeto estándar **Task**.
7. **Anatomía de la Tarea:** El nodo Create Records (Task) debe mapear obligatoriamente: OwnerId (El profesor responsable), Subject (**"Urgente: Cierre de Acta Pendiente"**), ActivityDate (Today + 2 días), y WhoId/WhatId (Link al registro de la materia/inscripción afectada).

**✅ Criterios de Aceptación (QA Check):**
1. Crear una inscripción pasada de fecha con nota vacía (Null) y otra pasada de fecha con nota "0".
2. Forzar manualmente la corrida de "Debug/Run" del Schedule flow.
3. Visualizar que el sistema genere solamente la Tarea (Task) para la inscripción con nota Null, validando que el Asunto y el Dueño asignado sean los correctos.

---

## 🏗️ ÉPICA 3: Analítica y Tableros de Control

**Objetivo:** Visibilidad gerencial mediante métricas clave en tiempo real.

---

### HU-205A: Dashboard 1 - Visión Académica
**Estimación:** 🟢 1 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-REP-001]`

**Descripción:**  
Como **Rectora de Lumina Tech**, Quiero un dashboard que muestre métricas generales de los estudiantes, Para entender la distribución de la población estudiantil y su rendimiento (Alumnos inscritos por carrera, reprobados del mes).

**⛔ Pre-requisitos (Dependencias):** Fase Previa: Autorizar configuración en Pestaña "Dashboards > Folder Sharing" para restringir visibilidad a perfil Directorio. Para Visualización QA: HU-201B y HU-201C deben estar completas (Sin datos migrados, los gráficos reportarán Valores: 0).

**💡 Justificación (Business Value):** Transforma los datos crudos en inteligencia de negocio ("Data-Driven Decision Making"). Permite a la Alta Dirección identificar en tiempo real qué carreras son rentables (altas inscripciones) y predecir tasas de abandono o necesidad de tutorías mediante el monitoreo de aplazos masivos, sin depender de que un analista cruce planillas de Excel a fin de mes.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Seguridad (Folder Sharing):** Crear dos carpetas nuevas: una en **Reports** (`Reportes Directivos`) y otra en **Dashboards** (`Dashboard Directivo`). Configurar el **Folder Sharing** restringiendo el acceso exclusivamente a los perfiles `Lumina Rectorado` y Roles `CEO / Rectora` y `Gerentes`.
2. **Campo de Fórmula (Abuela):** En el objeto **Inscripción**, crear el campo de fórmula `Carrera (F)` (Tipo: Text) con la lógica `Materia__r.Carrera__r.Name`. Esto permite que la Carrera sea "visible" directamente en reportes de Inscripción sin navegar relaciones complejas.
3. **Reporte Base:** Crear un reporte de tipo **Inscripciones**, agrupado por `Carrera (F)` y filtrado por alumnos activos. Incluir el campo `Año Lectivo` para habilitar el filtrado dinámico posterior.
4. **Construcción del Dashboard:** Crear un nuevo Dashboard en la carpeta segura 🚩 `[MODIFICADO S2] con el nombre "Tablero 1: Alumnos inscritos por carrera y año"`. Añadir un **Widget** tipo **Chart or Table**, elegir el gráfico de **Donut Chart** (Torta) y agrupar ("Slice By") por el campo `Carrera (F)`.
5. **Filtrado Dinámico:** Agregar un **Dashboard Filter** global utilizando el campo `Año Lectivo`, permitiendo a la Rectora alternar entre ciclos escolares (Ej: 2024, 2025).

**✅ Criterios de Aceptación (QA Check):**
**Dashboard:**
1. Se ubicará dentro del menú de Dashboards
2. Se debe visualizar el dashboard en el gráfico **"Torta"**.
3. El dashboard deberá tener como título **“Tablero 1: Alumnos inscritos por carrera y año”** 🚩 `[MODIFICADO S2]`
4. Se debe crear un dashboard donde permite visualizar en la gráfica los alumnos inscritos por carrera por año
5. Debe ser alumnos que estén activos
6. Debe permitir filtrar por año los alumnos inscritos por carrera
7. El dashboard deberá acceder únicamente la Rectora y los Gerentes
8. Validar manualmente de forma relacional que un alumno en estado desfavorecido recesivo listado coincida con la nómina tabular en tiempo real.
9. **Prueba de Seguridad (Negative Testing):** Logearse como un usuario estándar (ej. Profesor o Admisiones) e intentar buscar los reportes o el Dashboard. Validar que el sistema devuelva "0 resultados encontrados" o acceso denegado.

---

### HU-205B: Reporte 1 - Visión Académica
**Estimación:** 🟢 1 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-REP-001]`

**Descripción:**  
Como **Rectora de Lumina Tech**, Quiero un reporte que muestre métricas generales de los estudiantes, Para entender la distribución de la población estudiantil y su rendimiento (Alumnos reprobados del mes).

**⛔ Pre-requisitos (Dependencias):** Fase Previa: Autorizar configuración en Pestaña "Dashboards > Folder Sharing" para restringir visibilidad a perfil Directorio.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Campo de Filtrado Histórico:** En el objeto **Evaluación**, crear el campo de fórmula `Mes_Año__c` (Tipo: Text) que concatene Año y Mes (Ej: "2024-03"). Esto es indispensable para filtrar meses específicos en el Dashboard.
2. **Reporte de Detalle:** Crear un reporte de tipo **Evaluaciones** con filtros: `Estado = Desaprobado` y `Fecha de Examen = All Time`. Incluir el campo `Mes_Año__c` en el Outline del reporte.
3. **Agrupación y Orden:** Agrupar el reporte por `Mes_Año__c` y ordenar las columnas por nota de menor a mayor para priorizar casos críticos.
4. **Dashboard Independiente:** 🚩 `[MODIFICADO S2] (Separación Arquitectónica Restaurada)` Crear el dashboard `Tablero 1.1: Alumnos reprobados por mes`. Añadir un Widget tipo **Lightning Table** configurado para mostrar el **Record Count** (Total de alumnos) en lugar de suma de notas.
5. **Configuración de Filtro:** Añadir un filtro de Dashboard basado en `Mes_Año__c` mapeándolo correctamente a la columna del reporte para permitir la navegación histórica.

**✅ Criterios de Aceptación (QA Check):**
**Reporte:**
1. Se ubicará dentro del menú de Reportes
2. El reporte deberá tener como título **“Alumnos Reprobados”**
3. Se debe visualizar en el reporte los siguientes campos: Nombre, Apellido, Número de Documento (o Legajo), Email, Materia reprobada y la Nota exacta
4. Se debe crear un listado donde permite visualizar alumnos reprobados con notas menores a 6 en el mes
5. Debe mostrar un total contabilizando los alumnos reprobados en el mes
6. El reporte deberá acceder únicamente la Rectora y los Gerentes
7. Se deberá visualizar el reporte en el orden de peor a mejor nota

---

### HU-206A: Dashboard 2 - Gestión de Profesores
**Estimación:** 🟢 1 SP  
**Prioridad:** Media  
**Enlace Req:** `[REQ-REP-002]`

**Descripción:**  
Como **Rectora de Lumina Tech**, Quiero un dashboard enfocado en la carga laboral docente y métricas de dictado, Para balancear el trabajo del profesorado y monitorear la asistencia global en sus materias.

**⛔ Pre-requisitos (Dependencias):** Fase Previa: Autorizar configuración en Pestaña "Dashboards > Folder Sharing" para restringir visibilidad a perfil Directorio.

**💡 Justificación (Business Value):** Facilita la toma de decisiones para Recursos Humanos y la Secretaría Académica. Evita el "burnout" (desgaste) de los docentes al transparentar quién está sobreasignado de materias, y expone tempranamente materias con asistencia crítica, lo cual suele ser el síntoma principal de insatisfacción estudiantil con un profesor o programa antes de que ocurran las bajas formales.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Configuración de Reporte (Workload):** Crear un reporte de tipo **Materias**, agrupado por `Materia Owner` (Profesor) para visualizar el conteo de materias asignadas por docente.
2. **Configuración de Reporte (Asistencia):** Crear un reporte de **Inscripciones**, agrupado por `Materia`, aplicando una función de resumen tipo **Average** (Promedio) sobre el campo `% Asistencia`.
3. **Construcción del Dashboard:** Crear el dashboard 🚩 `[MODIFICADO S2] "Tablero 2: Gestión de Profesores"` en la carpeta segura `Dashboard Directivo`.
4. **Visualización de Carga:** Añadir un Widget de **Horizontal Bar Chart** para mostrar el ranking de materias por profesor.
5. **Visualización de Asistencia:** Añadir un Widget de **Lightning Table** que liste las materias con menor promedio de asistencia (orden ascendente), permitiendo identificar clases en riesgo.
6. **Seguridad:** Configurar el acceso compartido únicamente para la Rectora y Gerentes.

**✅ Criterios de Aceptación (QA Check):**
**Dashboard:**
1. Se ubicará dentro del menú de Dashboards
2. Se debe visualizar el dashboard en el gráfico **"barras horizontales"**.
3. El dashboard deberá tener como título **“Tablero 2: Gestión de Profesores”** 🚩 `[MODIFICADO S2]`
4. Se debe crear un dashboard donde permite visualizar cuántas materias dicta cada Profesor por filtro. 
5. Debería estar filtrado por el cuatrimestre/año actual. 
6. El dashboard deberá acceder únicamente la Rectora y los Gerentes
7. A través de UI modificar o adjudicar una materia existente y cambiarla a otro Profesor Owner (ejemplo a Profesor Tester). Refrescar la vista posterior.
8. Comprobar que en la estadística, Profesor Tester aparezca rankeado superior por +1 materia frente al resto en su Dashboard.
9. **Prueba de Seguridad:** Un usuario tipo Profesor no debe poder acceder bajo ningún link ni buscador a este folder gerencial.

---

### HU-206B: Reporte 2 - Gestión de Profesores
**Estimación:** 🟢 1 SP  
**Prioridad:** Media  
**Enlace Req:** `[REQ-REP-002]`

**Descripción:**  
Como **Rectora de Lumina Tech**, Quiero un reporte enfocado en el ausentismo, Para monitorear la asistencia global en las materias.

**✅ Criterios de Aceptación (QA Check):**
**Reporte:**
1. Se ubicará dentro del menú de Reportes
2. El reporte deberá tener como título **“Ausentismo por materias”**
3. Se debe visualizar en el reporte los siguientes campos: Nombre de la Materia, Profesor a cargo, y el Porcentaje de Ausentismo
4. Se debe crear un listado donde permite visualizar que materias tiene el mayor porcentaje de ausentismo
5. El reporte deberá acceder únicamente la Rectora y los Gerentes
6. Se deberá visualizar el reporte en el orden de mayor a menor ausentismo

---

### HU-207A: Reporte 3 - Calidad de Datos y Auditoría
**Estimación:** 🟢 1 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-REP-003]`

**Descripción:**  
Como **Rectora de Lumina Tech**, Quiero un reporte que evidencie la salud de bases de datos maestras de estudiantes, Para que la admin dispare purgas a sus comunicaciones.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Reporte de Calidad:** Crear un reporte de tipo **Reporte de Contactos y Cuentas** (Contactos).
2. **Lógica de Filtros:** Filtrar por `Record Type = Alumno`. Agregar una lógica de filtros cruzados o filtros estándar con el operador OR: `Email equals "" OR Phone equals "" OR Mobile Phone equals ""`.
3. **Formatos de Salida:** Mostrar columnas de contacto directo (Nombre, Apellido, Email, Teléfono) y agrupar por **Tipo de Documento** para identificar si el faltante es sistemático.
4. **Ubicación:** Guardar el reporte en la carpeta `Auditoría y Calidad`.

**✅ Criterios de Aceptación (QA Check):**
**Reporte:**
1. Se ubicará dentro del menú de Reportes
2. El reporte deberá tener como título **“Alumnos con datos incompletos”**
3. Se debe visualizar en el reporte los campos de contacto.
4. Se debe crear un listado donde permite visualizar Alumnos sin Email o con datos de contacto incompletos (para que Administración los llame)
5. El reporte deberá acceder únicamente la Rectora, los Gerentes y el administrador
6. Se deberá visualizar el reporte en el orden adecuado.

---

### HU-207B: Dashboard 3 - Calidad de Datos y Auditoría
**Estimación:** 🟢 1 SP  
**Prioridad:** Alta  
**Enlace Req:** `[REQ-REP-003]`

**Descripción:**  
Como **Rectora de Lumina Tech**, Quiero un dashboard que evidencie la línea temporal de captación, Para evaluemos la tendencia métrica institucional generada.

**⛔ Pre-requisitos (Dependencias):** Fase Previa: Autorizar configuración en Pestaña "Dashboards > Folder Sharing" para restringir visibilidad a perfil Directorio.

**💡 Justificación (Business Value):** Actúa como el control de calidad (QA) sobre el trabajo diario de Bedelía y Admisiones. Un alumno sin email o teléfono es un cliente incomunicable en caso de deuda o emergencia. Este tablero expone la deuda técnica de datos sucios. Simultáneamente, el gráfico histórico de inscripciones es el KPI (Indicador Clave) indispensable para medir la efectividad de las campañas de marketing de la universidad año tras año.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Reporte Evolutivo:** Crear un reporte de **Inscripciones** (o Contactos).
2. **Métrica Temporal:** Usar el campo `Created Date` (Fecha de Creación). Agrupar las filas por `Created Date` y configurar la agrupación de fecha por **Calendar Month** y **Calendar Year**.
3. **Dashboards Widget:** Añadir un Widget de tipo **Line Chart** (Gráfico Lineal) al dashboard de Auditoría 🚩 `[MODIFICADO S2] (Nombrado "Tablero 3: Calidad de Datos y Auditoría")`. Configurar el eje X con la fecha agrupada y el eje Y con el **Record Count**.
4. **Consolidar Tablero 3:** 🚩 `[MODIFICADO S2] Añadir a este mismo Dashboard un segundo Widget tipo Lightning Table que muestre el reporte de "Alumnos con datos incompletos" creado en la HU-207A`.
5. **Seguridad:** Compartir la carpeta de Dashboards de Auditoría únicamente con la Rectora, Gerentes y perfiles de Administrador.

**✅ Criterios de Aceptación (QA Check):**
**Dashboard:**
1. Se ubicará dentro del menú de Dashboards
2. Se debe visualizar el dashboard con el gráfico **"Lineal"** y la **"Tabla de Datos Incompletos"** 🚩 `[MODIFICADO S2]`.
3. El dashboard deberá tener como título **“Tablero 3: Calidad de Datos y Auditoría”** 🚩 `[MODIFICADO S2]`
4. Se debe crear un dashboard donde permite visualizar cuántos alumnos se inscribieron por mes en el último año y fallas de captura de datos.
5. El dashboard deberá acceder únicamente la Rectora y los Gerentes
6. Insertar un contacto sin Email, otro sin Teléfono, y otro con todos los datos.
7. Verificar que el Reporte de Calidad ("Data Quality") capture exclusivamente a los dos primeros contactos irregulares.
8. **Prueba de Seguridad:** Validar que cualquier usuario no perteneciente a la cuadrilla de auditoría/Rectorado reciba error visual de "Falta de Privilegios" si intentase acceder a las métricas maestras de QA.

---

### HU-208: Configuración de Perfiles y Seguridad de Acceso (Lumina Tech)
**Trazabilidad:** Responde a `[REQ-SEC-001]` Principio de Mínimo Privilegio y `[REQ-SEC-002]` Segregación de Funciones identificados en el Sprint 2 (entrevista Rectora Vance).

**Descripción:** "Como Salesforce Admin, quiero configurar perfiles de usuario personalizados en Salesforce de forma que cada rol del personal de Lumina Tech tenga acceso únicamente a los objetos y campos que necesita para su función, minimizando el riesgo de exposición de datos sensibles (Número de Documento, finanzas, calificaciones)."

**✅ Criterios de Aceptación:**
1. El sistema debe tener 6 perfiles personalizados, ninguno con acceso total (excepto System Administrator).
2. Ningún perfil académico (Bedelía, Profesor) puede ver el módulo de Cobros.
3. Ningún perfil financiero (Tesorería) puede ver Notas ni Asistencias.
4. El perfil Rectorado es de solo lectura absoluta (sin botones de creación/edición).
5. Los perfiles docentes deben tener Field Level Security (FLS) que oculte Número de Documento, teléfono y email de los alumnos.

**Checklist Técnico:**
- [ ] **Paso 0:** Activar Enhanced Profile User Interface en Setup → User Management Settings.
- [ ] **Capa Académica:**
  - [ ] Perfil **Lumina Registrar** creado (clone de Standard User).
  - [ ] Perfil **Lumina Director** creado (clone de Standard User) + FLS en Contact.
  - [ ] Perfil **Lumina Admisiones** creado (clone de Standard User, acceso mínimo).
- [ ] **Capa Docente:**
  - [ ] Perfil **Lumina Professor** creado (clone de Standard User) + FLS oculta Número de Documento/Teléfono/Email.
- [ ] **Capa Financiero-Directiva:**
  - [ ] Perfil **Lumina Tesoreria** creado (clone de Standard User, Full CRUD en Cobro).
  - [ ] Perfil **Lumina Rectorado** creado (clone de Read Only, no de Standard User).
- [ ] **Validación final:** La pantalla de Profiles en Setup muestra los 6 perfiles listados

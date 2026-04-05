# 🏠 Tutorial 10: Configuración de Home Pages por Perfil de Usuario
**Proyecto:** Lumina Tech — Sistema de Gestión Académica  
**Módulo:** Lightning App Builder — Home Page  
**Sprint:** 2  
**Rol ejecutor:** Administrador Salesforce  
**Prerequisito global:** Los Dashboards y Reportes de la Épica 3 (HU-205A, HU-205B, HU-205C) deben estar creados y activos antes de ejecutar este tutorial. Los 4 perfiles base deben existir tal como se configuraron en la **Guía 07.1** (Perfiles y Seguridad).

---

## 📐 Arquitectura General

En Salesforce, la página de inicio (Home Page) puede personalizarse por **perfil de usuario** usando **Lightning App Builder**. Esto permite que cada actor del sistema vea exactamente lo que necesita al abrir la aplicación, sin información irrelevante que distraiga su flujo de trabajo.

Lumina Tech tiene **5 Home Pages** diferenciadas: 4 para los perfiles personalizados configurados en la Guía 07.1, y 1 para el perfil nativo **System Administrator** con foco en el monitoreo técnico del sistema.

| # | Perfil | Rol en la Jerarquía | Audiencia | Prioridad |
|:---|:---|:---|:---|:---|
| 1 | `Lumina Rectorado` | CEO / Rectora Lumina | Dra. Elena Vance y Alta Dirección | ⭐ Alta |
| 2 | `Lumina Registrar` | Gerencia Académica | Personal operativo, Recepción, Bedelía | ⭐ Alta |
| 3 | `Lumina Professor` | Profesor | Docentes de todas las carreras | 🔶 Media |
| 4 | `Lumina Director` | Director de Carrera | Directores y coordinadores académicos | 🔶 Media |
| 5 | `System Administrator` | Administrador Técnico | Admin Salesforce responsable del entorno | ⭐ Alta |

---

## ⚙️ Preparación Global (Ejecutar una sola vez)

Antes de configurar cualquier Home Page, completa estos pasos:

1. Ve a **Setup** (engranaje) > busca **Lightning App Builder** en el Quick Find > haz clic en él.
2. Familiarízate con la interfaz: el panel izquierdo tiene componentes arrastrables, el centro es el lienzo, y el panel derecho muestra las propiedades del componente seleccionado.
3. Verifica que los siguientes elementos ya existen en tu org (son requisitos):
   - Dashboard: `Dashboard Directivo` (dentro de la carpeta `Dashboard Directivo`)
   - Reporte: `Alumnos por Carrera`
   - Reporte: `Reprobados del Mes`
   - Reporte: `Evolución de Inscripciones`
   - Flow activo: `Lumina Asistente Carga Recepcion`
4. Si alguno de estos elementos no existe aún, completa primero los tutoriales de Épica 3 antes de continuar.

---

## 🏠 HOME 1 — Perfil: Rectora y Dirección
### `Perfil: Lumina Rectorado`
> **Objetivo de diseño:** La Rectora debe poder evaluar el estado académico de la institución en menos de 30 segundos sin abrir un solo reporte.

---

### Paso 1: Crear la nueva Home Page

1. Dentro de **Lightning App Builder**, haz clic en el botón **New** (parte superior derecha).
2. En el selector de tipo de página, elige **Home Page** y luego clic en **Next**.
3. En el campo **Label**, escribe: `Home Rectorado Lumina`.
4. En la sección de plantillas, selecciona **Home page header two columns left side bar**. Haz clic en **Finish**.
5. Se abrirá el lienzo con 3 áreas: Un encabezado superior (Header), una columna estrecha a la izquierda, y una columna principal ancha a la derecha.

---

### Paso 2: Añadir el banner institucional (Rich Text)

1. En el panel izquierdo, usa el buscador y escribe `Rich Text`.
2. Arrastra el componente **Rich Text** a la parte superior del lienzo (zona de encabezado / columna completa ancha).
3. En el panel derecho, dentro del editor de texto enriquecido, configura el contenido así:

   - Usa el editor para escribir un saludo institucional genérico (el componente Rich Text estándar es estático):
   ```
   🎓 Panel Ejecutivo — Lumina Tech
   Bienvenido/a al Sistema de Gestión Académica | Sprint 2
   ```
   - Selecciona el texto del título y aplica **Heading 1** o **Bold** para destacarlo.
   - *(Opcional)* Si tienes acceso a HTML directo, puedes añadir el color institucional de Lumina Tech.

4. Haz clic fuera del componente para guardar el texto.

> [!TIP]
> **Arquitectura Avanzada (Saludo Dinámico):**
> Si el negocio exige imperativamente que el panel diga *"Bienvenido/a, Elena"*, el componente Rich Text no sirve ya que no soporta variables como `{!User.FirstName}`. La solución "Pro" es crear un **Screen Flow** de una sola pantalla con un componente de *Display Text* que use las variables globales `{!$User.FirstName}` y `{!$User.LastName}`. Luego, simplemente arrastras el componente de Flow al encabezado en lugar del Rich Text.

---

### Paso 3: Añadir el Dashboard embebido (KPIs de Visión Académica y Profesores)

Este componente centralizado atenderá directamente a la solicitud de los tableros ejecutivos de la Rectora.

1. En el panel izquierdo, busca **Dashboard**.
2. Arrastra el componente **Dashboard** hacia la **columna derecha** (la zona principal más ancha).
3. En el panel derecho:
   - **Dashboard:** selecciona `Dashboard Directivo`. *(Nota funcional: Asegúrate que este dashboard contenga los gráficos del Tablero 1: Visión Académica y el **Tablero 2: Gestión de Profesores** que pidió la Dra. Vance).*
   - **Max Height:** puedes ajustar la altura a `500` o `600` para que los gráficos entren cómodamente.
   - **Show Title:** actívalo.
4. El Dashboard de Alto Nivel aparecerá renderizado en el lienzo.

---

### Paso 4: Añadir el Reporte de Reprobados del Mes

1. En el panel izquierdo, busca **Report Chart**.
2. Arrastra el componente **Report Chart** hacia la **columna izquierda** (la barra lateral estrecha).
3. En el panel derecho:
   - **Report:** busca y selecciona `Reprobados del Mes`.
   - **Show Title:** activado.
   - **Show Range:** activado (mostrará el período del reporte).
4. *(Si el reporte no tiene un gráfico configurado, deberás entrar al reporte desde la pestaña Reports, añadir un Chart y guardar antes de que aparezca aquí).*

---

### Paso 5: Añadir el Gráfico de Evolución de Inscripciones

1. Arrastra un segundo componente **Report Chart** hacia la **columna izquierda**, justo debajo del reporte anterior.
2. En el panel derecho:
   - **Report:** selecciona `Evolucion de Inscripciones`.
   - **Show Title:** activado.
3. Este gráfico de línea muestra la tendencia mensual de nuevas inscripciones del último año.

---

### Paso 6: Añadir el componente de Tareas pendientes

1. En el panel izquierdo, busca **Tasks**.
2. Arrastra el componente **Tasks** hacia la **columna izquierda**, debajo de los gráficos de reporte que acabas de cargar.
3. Este componente muestra automáticamente las tareas abiertas asignadas al usuario logeado, sin configuración adicional.

---

### Paso 7: Guardar y Activar para el perfil Rectorado

1. Haz clic en **Save** (botón superior derecho del Lightning App Builder).
2. Inmediatamente después, haz clic en **Activate**.
3. En la pantalla de activación, selecciona la pestaña **App, Record, Type, and Profile**.
4. Haz clic en **Assign to Users by Profile**.
5. En el selector de perfiles, busca y selecciona `Lumina Rectorado`.
6. Haz clic en **Save**.

> [!IMPORTANT]
> En este punto, **cualquier usuario con el perfil `Lumina Rectorado`** que entre a la aplicación verá esta Home Page automáticamente.

---

### ✅ QA Check — Home Rectorado

1. Cierra el Lightning App Builder.
2. Entra a Salesforce como un usuario con perfil `Lumina Rectorado`.
3. Navega a la Home Page de la app académica.
4. Verifica que se ven: el banner institucional, el gráfico de torta de alumnos por carrera, el widget de reprobados y el gráfico de evolución.
5. Confirma que los datos del gráfico corresponden a registros reales en el sistema.

---
---

## 🏠 HOME 2 — Perfil: Personal Operativo / Recepción
### `Perfil: Lumina Registrar`
> **Objetivo de diseño:** El operador de ventanilla (Rol: Gerencia Académica) debe poder registrar un alumno sin navegar a ninguna otra pantalla. Es el perfil con permisos de Crear y Editar sobre Contactos, Inscripciones y Cobros. La herramienta de carga está en su Home.

---

### Paso 1: Crear la nueva Home Page

1. En **Lightning App Builder** > **New**.
2. Tipo: **Home Page** > **Next**.
3. **Label:** `Home Recepcion Lumina`.
4. Plantilla: selecciona **Home page header two columns left side bar**. Haz clic en **Finish**.

---

### Paso 2: Añadir el banner de contexto operativo

1. Arrastra un componente **Rich Text** a la zona de encabezado superior.
2. En el editor, escribe:
   ```
   📋 Panel de Recepción — Lumina Tech
   Ingrese los datos del nuevo alumno en el formulario de abajo.
   Campos marcados con (*) son obligatorios.
   ```
3. Aplica formato **Bold** al título principal.

---

### Paso 3: Embeber el Flow de Carga Rápida directamente en la Home

Este es el componente más importante de esta página. El formulario de registro estará visible y listo para usar al abrir la aplicación.

1. En el panel izquierdo, busca `Flow`.
2. Arrastra el componente **Flow** hacia la **columna derecha** (la zona principal más ancha).
3. En el panel derecho:
   - **Flow:** despliega la lista y selecciona `Lumina Asistente Carga Recepcion`.
   - **Show Label:** desactívalo (el banner de arriba ya da el contexto).
4. Verás aparecer un bloque gris en el lienzo con el mensaje *"This is a placeholder. Flows don't run in the canvas"*. **Esto es natural y correcto**. Salesforce bloquea la ejecución de Flows en el modo editor por seguridad, para evitar que el Administrador cree registros de alumnos basura sin querer. El formulario real aparecerá cuando el usuario final vea la página.

> [!IMPORTANT]
> Esto significa que el operador de recepción abre Salesforce y el formulario ya está visible, sin hacer ningún clic adicional. Combinado con la Utility Bar, el flow está accesible desde **cualquier pantalla** de la aplicación.

---

### Paso 4: Añadir la Lista de Alumnos Registrados Hoy

1. En el panel izquierdo, busca **List View**.
2. Arrastra el componente **List View** hacia la **columna izquierda** (la barra lateral estrecha).
3. En el panel derecho:
   - **Object:** selecciona `Persona` (Contact).
   - **List View:** selecciona o crea la vista `Registrados Hoy`. *(Si no existe, créala desde el objeto Contact con el filtro `Fecha de Creación = HOY` y compártela con el perfil de Recepción).*
   - **Number of Records:** `10`.
   - **Show Header:** activado.
4. Esta lista mostrará los últimos alumnos ingresados durante el turno actual, permitiendo al operador verificar rápidamente sus cargas.

---

### Paso 5: Añadir el componente de Tareas

1. Arrastra el componente **Tasks** a la parte inferior de la **columna izquierda**, debajo de la vista de lista.
2. Sin configuración adicional; mostrará las tareas pendientes asignadas al operador logeado.

---

### Paso 6: Guardar y Activar para el perfil Registrar

1. **Save** > **Activate**.
2. Pestaña **App, Record, Type, and Profile** > **Assign to Users by Profile**.
3. Selecciona `Lumina Registrar` > **Save**.

---

### ✅ QA Check — Home Registrar

1. Entra como usuario con perfil `Lumina Registrar` (Rol: Gerencia Académica).
2. Verifica que el formulario de registro de alumno está visible directamente en la Home sin hacer ningún clic.
3. Completa el formulario con datos de prueba y presiona **Guardar Alumno**.
4. Verifica que el nuevo alumno aparece en la lista lateral derecha **Registrados Hoy**.
5. Confirma que el botón `Registrar Otro Alumno` reinicia el formulario correctamente.
6. **Prueba de permisos:** Verifica que este perfil puede crear y editar Contactos e Inscripciones, pero **no puede borrar** registros (según la matriz de la Guía 07.1).

---
---

## 🏠 HOME 3 — Perfil: Docentes
### `Perfil: Lumina Professor`
> **Objetivo de diseño:** El primer vistazo del profesor al entrar al sistema debe responder: ¿Tengo actas pendientes? ¿Cuáles son mis materias activas? Este perfil tiene acceso de lectura a Contactos/Inscripciones, y permisos de Crear/Editar sobre Asistencia y Evaluación. **No puede ver** el DNI, teléfono ni email de sus alumnos (FLS configurado en Guía 07.1).

---

### Paso 1: Crear la nueva Home Page

1. En **Lightning App Builder** > **New**.
2. Tipo: **Home Page** > **Next**.
3. **Label:** `Home Docente Lumina`.
4. Plantilla: **Header and Two Columns** (columnas iguales o 1/3 - 2/3). Haz clic en **Finish**.

---

### Paso 2: Añadir el banner del panel docente

1. Arrastra **Rich Text** al encabezado superior.
2. Escribe:
   ```
   👨‍🏫 Panel Docente — Lumina Tech
   Revisa tus actas pendientes y el estado académico de tus materias.
   ```

---

### Paso 3: Añadir el componente de Tareas Urgentes (Actas Pendientes)

Este es el componente más crítico para el docente. Las tareas generadas automáticamente por el **Scheduled Flow de HU-204** aparecerán aquí.

1. Arrastra **Tasks** a la **columna izquierda**, en la parte superior.
2. El componente mostrará automáticamente las tareas con asunto `Urgente: Cierre de Acta Pendiente` asignadas al docente logeado.
3. Con el componente seleccionado, en el panel derecho verifica que está configurado para mostrar tareas **abiertas** (Open).

> [!NOTE]
> Si el profesor no tiene tareas pendientes, el componente mostrará un mensaje vacío. Eso es el escenario ideal: significa que todas sus actas están al día.

---

### Paso 4: Añadir la Lista de Materias Asignadas

1. Arrastra **List View** a la **columna izquierda**, debajo del componente de Tareas.
2. En el panel derecho:
   - **Object:** `Materia__c`.
   - **List View:** selecciona la vista `Mis Materias Activas`. *(Créala en el objeto Materia__c filtrando por el campo del docente responsable = Usuario actual, y el estado activo).*
   - **Number of Records:** `10`.
   - **Show Header:** activado.

---

### Paso 5: Añadir el Reporte de Rendimiento de sus Alumnos

1. Arrastra **Report Chart** a la **columna derecha**.
2. En el panel derecho:
   - **Report:** selecciona el reporte de `Alumnos por Estado (Aprobado / Desaprobado / Ausente)` filtrado por el docente actual.
   - *(Si este reporte no existe aún, créalo en la pestaña Reports filtrando inscripciones/evaluaciones del docente logeado, agrupadas por estado).*
   - **Show Title:** activado.

---

### Paso 6: Añadir los Elementos Recientes (Recently Viewed)

1. Arrastra **Recently Viewed** o **Recent Items** a la columna derecha, debajo del gráfico.
2. Configura para mostrar objetos recientes de tipo `Materia__c` e `Inscripcion__c`.
3. Esto permite al docente retomar rápidamente el trabajo donde lo dejó en la sesión anterior.

---

### Paso 7: Guardar y Activar para el perfil Professor

1. **Save** > **Activate**.
2. **Assign to Users by Profile** > selecciona `Lumina Professor` > **Save**.

---

### ✅ QA Check — Home Professor

1. Entra como usuario con perfil `Lumina Professor`.
2. Verifica que el componente de Tareas muestra las actas pendientes asignadas a ese docente.
3. Verifica que la lista de Materias muestra únicamente las asignaturas que le corresponden a ese docente, no las de otros.
4. **Prueba de aislamiento:** entra con otro docente y confirma que solo ve SUS materias y SUS tareas, no las del docente anterior.
5. **Prueba de privacidad (FLS):** confirma que en ningún componente de esta Home se ven los campos `Tipo_Documento__c`, `Numero_Documento__c`, `Phone` ni `Email` del alumno. Esos campos están bloqueados a nivel de campo según la Guía 07.1.

---
---

## 🏠 HOME 4 — Perfil: Director de Carrera
### `Perfil: Lumina Director`
> **Objetivo de diseño:** El Director de Carrera necesita visibilidad del estado académico de su carrera: materias que supervisa, inscripciones activas y rendimiento de sus alumnos. Este perfil puede **editar Carreras y Materias** pero no tiene acceso a Cobros ni a datos de identidad de los alumnos (configurado en Guía 07.1).

---

### Paso 1: Crear la nueva Home Page

1. En **Lightning App Builder** > **New**.
2. Tipo: **Home Page** > **Next**.
3. **Label:** `Home Director Lumina`.
4. Plantilla: selecciona **Home page header two columns left side bar**. Haz clic en **Finish**.

---

### Paso 2: Añadir el banner de Dirección Académica

1. Arrastra **Rich Text** al encabezado superior.
2. Escribe:
   ```
   🎓 Panel de Dirección de Carrera — Lumina Tech
   Supervisión de asignaturas, rendimiento estudiantil e inscripciones activas.
   ```
3. Aplica formato **Bold** al título.

---

### Paso 3: Añadir la Lista de Materias de la Carrera

El componente principal debe ser el corazón operativo del Director: las materias que gestiona.

1. Arrastra **List View** a la **columna derecha** (la zona principal ancha).
2. En el panel derecho:
   - **Object:** `Materia__c`.
   - **List View:** selecciona `Todas` o `Materias de mi Carrera` (si ya tienes la vista filtrada creada).
   - **Number of Records:** `10`.
   - **Show Header:** activado.
3. Permite al Director hacer clic y editar rápidamente los cupos o profesores asignados (cumpliendo sus permisos de Edición según Guía 07.1).

---

### Paso 4: Añadir el Reporte de Gestión de Profesores

Para cumplir con el **Tablero 2** solicitado por la Dra. Vance, el Director debe auditar qué carga horaria tienen sus docentes o si hay ausentismo.

1. Arrastra **Report Chart** a la **columna izquierda** (la barra lateral estrecha).
2. En el panel derecho:
   - **Report:** selecciona `Materias por Profesor` o `Reporte de Asistencias`.
   - **Show Title:** activado.
3. Da visibilidad inmediata para gestionar la carga laboral del equipo docente de la carrera.

---

### Paso 5: Añadir la Lista de Inscripciones Recientes

1. Arrastra un segundo **List View** a la **columna izquierda**, debajo del gráfico.
2. En el panel derecho:
   - **Object:** `Inscripcion__c` (Application / Enrollment).
   - **List View:** selecciona `Recently Viewed` o una lista de `Recientes`.
   - **Number of Records:** `5`.
   - **Show Header:** activado.
3. Permite monitorear el flujo de nuevos alumnos entering a su programa en la temporada actual.

---

### Paso 6: Guardar y Activar para el perfil Director

1. **Save** > **Activate**.
2. **Assign to Users by Profile** > selecciona `Lumina Director` > **Save**.

---

### ✅ QA Check — Home Director

1. Entra como usuario con perfil `Lumina Director` (Rol: Director de Carrera).
2. Verifica que el banner de Dirección está visible.
3. Verifica que la lista central muestra objetos de tipo `Materia__c`.
4. **Prueba de permisos:** confirma que usando esa lista puede abrir y **editar** un registro de Materia o Carrera. Luego, busca una pestaña de `Cobros` y verifica que **está oculta** (Tab Hidden según Guía 07.1).
5. **Prueba de aislamiento:** un `Lumina Professor` jamás debe llegar a esta Home; el Director es el único con visión panorámica de la carrera sin llegar a nivel Rectorado.
6. **Prueba de seguridad:** entra como un usuario `Lumina Professor` y confirma que **no puede ver** los componentes de dirección ni esta Home Page.

---
---

## 🏠 HOME 5 — Perfil: Administrador Técnico del Sistema
### `Perfil: System Administrator`
> **Objetivo de diseño:** El System Admin tiene visibilidad total del estado técnico de la org: automatizaciones activas, errores de Flows, calidad de datos global, usuarios y todos los procesos en ejecución. Esta es la Home del arquitecto del sistema, no del usuario de negocio.

> [!IMPORTANT]
> El perfil `System Administrator` en Salesforce tiene acceso native a **Setup** y a todas las herramientas de administración. Su Home Page debe ser un **centro de control técnico**, no una réplica de la Home del director o la rectora.

---

### Paso 1: Crear la nueva Home Page

1. En **Lightning App Builder** > **New**.
2. Tipo: **Home Page** > **Next**.
3. **Label:** `Home SysAdmin Lumina`.
4. Plantilla: selecciona **Home page header two columns left side bar**. Haz clic en **Finish**.

---

### Paso 2: Añadir el banner del panel de control técnico

1. Arrastra **Rich Text** al encabezado superior.
2. En el editor, escribe:
   ```
   🛡️ Panel de Control Técnico — Lumina Tech
   System Administrator | Monitoreo de Automatizaciones, Datos y Usuarios
   ```
3. Aplica **Bold** al título.

---

### Paso 3: Añadir el Reporte de Salud de Automatizaciones (Flows con Error)

Este es el componente más crítico del SysAdmin. Si algún Flow falló silenciosamente, este widget lo expone.

1. Crea previamente un **Reporte** de tipo `Flows` o alternativamiente un reporte sobre **Tareas** con filtro `Sujeto contiene 'Error'` o `Asunto = 'Flow Error'` si los errores se registran como tareas. Si tu org tiene **Event Monitoring** activo, usa ese dataset.
   - *(Para orgs sin Event Monitoring: revisa Setup > Flows > Flow Error Emails y considera crear un Custom Report Type sobre el objeto EmailMessage para capturar correos de error de Flow)*.
2. Arrastra **Report Chart** a la **columna izquierda**, parte superior.
3. En el panel derecho:
   - **Report:** selecciona el reporte de errores de Flow o de Tareas abiertas del sistema.
   - **Show Title:** activado.

> [!TIP]
> Si no tienes Event Monitoring, una alternativa efectiva es crear un **List View** del objeto `Task` filtrado por `Asunto contiene Cierre de Acta` y `Estado = Open`, agrupado por `Asignado a`. Esto da visibilidad inmediata de cuántos profesores tienen actas pendientes.

---

### Paso 4: Añadir el Reporte de Calidad de Datos Global

1. Arrastra un segundo **Report Chart** a la **columna izquierda**, debajo del anterior.
2. En el panel derecho:
   - **Report:** selecciona `Alumnos con Datos Incompletos` (sin Email o sin Teléfono, de HU-205C).
   - **Show Title:** activado.
3. Este reporte permite al Admin detectar registros que el equipo de recepción ingresó con campos faltantes, para iniciar un proceso de remediación.

---

### Paso 5: Añadir la Lista de Usuarios Activos del Sistema

1. Arrastra **List View** a la **columna derecha**, parte superior.
2. En el panel derecho:
   - **Object:** `User`.
   - **List View:** selecciona `All Active Users` (vista estándar de Salesforce).
   - **Number of Records:** `10`.
   - **Show Header:** activado.
3. Permite al Admin verificar qué usuarios están activos, detectar usuarios sin licencia o con configuraciones incorrectas sin tener que entrar a Setup > Users.

---

### Paso 6: Añadir la Lista de Contactos Creados en los Últimos 7 Días

1. Arrastra un segundo **List View** a la **columna derecha**, debajo de la lista de usuarios.
2. En el panel derecho:
   - **Object:** `Persona` (Contact).
   - **List View:** selecciona o crea `Creados en los Últimos 7 Días`. *(Filtro: Fecha de Creación >= LAST\_N\_DAYS:7)*.
   - **Number of Records:** `15`.
   - **Show Header:** activado.
3. Permite auditar la actividad de carga del equipo de Recepción en tiempo real.

---

### Paso 7: Añadir los Accesos Rápidos a Setup (Rich Text con links)

1. Arrastra un componente **Rich Text** a la parte inferior de la **columna izquierda**.
2. Escribe los siguientes accesos directos. En el editor Rich Text, puedes seleccionar cada texto y usar el botón **Insert Link** para convertirlos en hipervínculos clickeables con las URLs de Setup de tu org:

   ```
   🔗 Accesos Rápidos del Administrador:

   🧩 Flows          → Setup > Process Automation > Flows
   🔁 Duplicados     → Setup > Data > Duplicate Management
   ⏰ Jobs Programados → Setup > Environments > Scheduled Jobs
   📊 Data Loader    → Descargar desde Setup > Integrations > Data Loader
   👥 Usuarios       → Setup > Users > Users
   📧 Plantillas Email → Setup > Email > Lightning Email Templates
   🚫 Reglas Validación → Setup > Object Manager > Persona > Validation Rules
   ```

> [!TIP]
> Para insertar un link en Rich Text: selecciona el texto (ej: "Flows"), haz clic en el ícono de cadena (🔗) en la barra de herramientas del editor y pega la URL directa de Setup de tu org (ej: `https://[tu-org].lightning.force.com/lightning/setup/Flows/home`).

---

### Paso 8: Guardar y Activar para el perfil System Administrator

1. **Save** > **Activate**.
2. Pestaña **App, Record, Type, and Profile** > **Assign to Users by Profile**.
3. En el selector de perfiles, busca y selecciona **`System Administrator`** (perfil nativo de Salesforce).
4. Haz clic en **Save**.

> [!CAUTION]
> Al asignar esta Home al perfil `System Administrator`, todos los usuarios con ese perfil verán este panel técnico. Si tienes múltiples Admins con diferentes responsabilidades, considera crear sub-perfiles clonados o usar la asignación por **App** en lugar de por **Profile** para mayor granularidad.

---

### ✅ QA Check — Home System Administrator

1. Entra como usuario con perfil `System Administrator`.
2. Verifica que el banner técnico es visible y correctamente formateado.
3. Verifica que el widget de Calidad de Datos muestra los alumnos con campos incompletos.
4. Verifica que la Lista de Usuarios muestra los usuarios activos de la org.
5. **Prueba de links:** haz clic en al menos 2 de los accesos rápidos de Setup y confirma que navegan a la página correcta.
6. **Prueba de aislamiento:** entra como `Lumina Rectorado` y confirma que **no ve** el panel técnico del Admin, sino su propio Home con los dashboards ejecutivos.

---
---

## 🔒 Resumen de Seguridad por Home Page

> [!IMPORTANT]
> Los nombres de perfil en esta tabla son exactamente los implementados en la **Guía 07.1 — Perfiles y Seguridad** más el perfil nativo `System Administrator`. No crear perfiles con nombres distintos.

| Home Page | Perfil asignado | Rol en la Jerarquía | Componentes clave | Enfoque |
|:---|:---|:---|:---|:---|
| Home Rectorado | `Lumina Rectorado` | CEO / Rectora Lumina | Dashboard KPI, Reportes de tendencia | Decisión estratégica |
| Home Registrar | `Lumina Registrar` | Gerencia Académica | Flow embebido, Lista del día | Carga operativa diaria |
| Home Professor | `Lumina Professor` | Profesor | Actas pendientes, Mis Materias | Docencia y evaluación |
| Home Director | `Lumina Director` | Director de Carrera | Materias supervisadas, Rendimiento | Gestión académica media |
| Home SysAdmin | `System Administrator` | Admin Técnico | Errores de Flow, Calidad de datos, Usuarios | Monitoreo técnico total |

> [!CAUTION]
> Si un usuario tiene **más de un perfil** o si los perfiles no están correctamente asignados, Salesforce mostrará la última Home Page activada como "org default". Verifica siempre en **Setup > Lightning App Builder** que cada Home Page tiene su perfil correctamente asignado en la sección **Activation**.

---

## 🔁 Mantenimiento Futuro

- Si se agregan nuevos reportes o dashboards, puedes editarlos desde **Lightning App Builder** seleccionando la Home Page correspondiente y haciendo clic en **Edit**.
- Si se crea un nuevo perfil de usuario (ej. `Lumina Coordinador`), se debe crear una nueva Home Page siguiendo el mismo proceso y asignarla al nuevo perfil en la sección Activation.
- Las Home Pages se versionan automáticamente en Salesforce. Si realizas un cambio y quieres volver a la versión anterior, usa el botón **Save As New Version** en el App Builder.

---
*Guía técnica elaborada por el equipo de implementación Salesforce — Lumina Tech Sprint 2.*  
*Versión 2.0 — Marzo 2026 | 5 Home Pages: 4 perfiles personalizados + System Administrator*

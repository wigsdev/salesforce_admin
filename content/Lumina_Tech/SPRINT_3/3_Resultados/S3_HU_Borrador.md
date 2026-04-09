# HISTORIAS DE USUARIO — SPRINT 3
**Proyecto:** Lumina Tech University
**Sprint:** 3 — Campus Virtual (Experience Cloud)

---

## 🏗️ ÉPICA 0: Pre-requisitos de la Org (Setup Técnico)

**Objetivo:** Activar los interruptores maestros en Salesforce antes de comenzar cualquier configuración de portal. Sin este paso, ningún otro módulo del Sprint funciona.

---

### HU-S3-00: Activación de la Plataforma de Portal (Spike Técnico)
**Estimación:** 🟢 1 SP
**Prioridad:** Crítica (Bloqueante para todas las HUs del Sprint)
**Enlace Req:** `[REQ-EC-000]`
**Etiquetas Trello:** 🔘 `[Gris] Configuración Base` | 🔴 `[Rojo] Seguridad`

**Descripción:**
Como **Administrador Salesforce**, Quiero activar los interruptores maestros de Experience Cloud y Knowledge en la Org, Para habilitar las funcionalidades de portal que el Sprint 3 requiere sin afectar la configuración existente.

**⛔ Pre-requisitos (Dependencias):** Ninguno. Esta HU es el cimiento del Sprint 3 y debe ejecutarse primero.

**💡 Justificación (Business Value):** Un portal sin el interruptor maestro activado es invisible para el sistema. Invertir 20 minutos en este paso evita horas de debugging buscando opciones de menú que no aparecen porque la plataforma nunca fue habilitada.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Activar Digital Experiences (Herramienta: Setup → Digital Experiences):** Buscar "Digital Experiences" en el Setup Quick Find. Hacer clic en **Enable** para activar el interruptor maestro. Sin este paso, el menú "All Sites" no existirá.
2. **Activar Knowledge (Herramienta: Setup → Knowledge Settings):** Buscar "Knowledge" en el Setup Quick Find → Knowledge Settings → marcar el checkbox **Enable Lightning Knowledge** → Save.
3. **Habilitar Knowledge User (Herramienta: Setup → Users):** Ir a `Setup → Users → [Tu propio registro de usuario]`. Hacer clic en Edit y marcar la casilla **Knowledge User** ✅. Sin este paso, la pestaña de Knowledge no aparecerá en la interfaz aunque Knowledge esté activado en la Org.
4. **Verificar licencias disponibles:** Ir a `Setup → Company Information`. Confirmar que existen licencias del tipo **Customer Community** disponibles. Reservar máximo 2 para pruebas de login de alumnos.
5. **Verificar Contacts de prueba:** Confirmar que los Contacts de Lucas Martinez y Ana Vega existen en la Org como Alumnos activos (Rol__c = Alumno). Estos serán los usuarios de prueba del portal privado.

**✅ Criterios de Aceptación (QA Check):**
1. Ir a Setup Quick Find y buscar "All Sites". Verificar que el menú existe y que aparece el botón **New** para crear un sitio.
2. Ir a la pestaña de **Knowledge** en App Launcher. Verificar que la pestaña aparece y carga correctamente.
3. Ir a `Setup → Company Information` y confirmar que hay al menos 1 licencia Customer Community disponible.
4. Buscar el Contact "Lucas Martinez" en Salesforce y confirmar que existe con Rol__c = Alumno.

---

## 🏗️ ÉPICA 1: Portal Público — La Vidriera de Lumina Tech

**Objetivo:** Crear la presencia digital pública de Lumina Tech con identidad de marca y un formulario de captación que convierta visitantes en Leads dentro del CRM.

---

### HU-S3-01: Creación del Sitio Experience Cloud con Branding Lumina
**Estimación:** 🟡 2 SP
**Prioridad:** Alta
**Enlace Req:** `[REQ-EC-001]`
**Etiquetas Trello:** 🟣 `[Morado] Branding` | 🔵 `[Azul] Experience Cloud`

**Descripción:**
Como **Administrador Salesforce**, Quiero crear el sitio de Experience Cloud con la plantilla correcta y aplicar la identidad visual de Lumina Tech (colores, logo), Para que el portal sea reconocible como la plataforma oficial de la universidad y no parezca una instalación genérica de Salesforce.

**⛔ Pre-requisitos (Dependencias):** HU-S3-00 completada (Digital Experiences activado). Contar con los archivos gráficos de Lumina Tech (logo, banner) disponibles en `content/Lumina_Tech/Recursos_Graficos/Theme/`.

**💡 Justificación (Business Value):** La primera impresión de la universidad ante un futuro alumno es este portal. Un sitio con la identidad visual correcta comunica profesionalismo institucional y genera confianza. Un sitio con el logo de Salesforce por defecto genera exactamente lo contrario.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Crear el Sitio (Herramienta: Setup → All Sites → New):** Seleccionar la plantilla **Customer Service** (recomendada por el TL por su estructura de soporte incluida). Asignar el nombre `Campus Virtual Lumina Tech`. Definir la URL del sitio (ej: `luminatech`). Hacer clic en **Create**.
2. **Acceder al Experience Builder (Herramienta: All Sites → Builder):** Una vez creado el sitio, hacer clic en el botón **Builder** para acceder al editor visual.
3. **Aplicar el Theme — Colores (Herramienta: Builder → Theme):** En el panel izquierdo del Builder hacer clic en el ícono de pincel (🎨 Theme). Seleccionar **Edit Theme**. Configurar:
   - **Primary Color:** `#005A9C` (Lumina Blue)
   - **Secondary Color:** `#F2A900` (Tech Gold)
   - **Page Background:** `#F4F6F9` (Neutro)
4. **Subir el Logo (Herramienta: Builder → Header):** En el Builder, hacer clic en el componente de encabezado del sitio. Reemplazar el logo por defecto con el archivo `lumina_logo_header.png` ubicado en `Recursos_Graficos/Theme/`.
5. **Publicar el sitio (Herramienta: Builder → Publish):** Hacer clic en el botón **Publish** en la esquina superior derecha. Confirmar la publicación.
6. **Habilitar acceso público (Herramienta: Builder → Settings → General):** En el Builder ir a **Settings → General** y verificar que la opción **"Guest users can see and interact with the site without logging in"** esté activada.

**✅ Criterios de Aceptación (QA Check):**
1. Abrir el sitio en modo incógnito del navegador usando la URL configurada. Verificar que carga sin requerir login.
2. Verificar visualmente que la barra de navegación muestra el color Lumina Blue (`#005A9C`) y el logo de Lumina Tech en el encabezado.
3. Verificar que el fondo de la página es el tono neutro (`#F4F6F9`) y no el blanco estándar de Salesforce.
4. **Prueba de identidad:** Mostrar el sitio a alguien del equipo sin decirle de qué es. Debe identificarlo como "algo de Lumina Tech" por los colores y el logo.

---

### HU-S3-02: Screen Flow Público para Captación de Futuros Alumnos (Lead)
**Estimación:** 🟡 3 SP
**Prioridad:** Alta
**Enlace Req:** `[REQ-EC-002]`
**Etiquetas Trello:** 🟠 `[Naranja] Automatización (Flows)` | 🔵 `[Azul] Experience Cloud`

**Descripción:**
Como **Futuro Alumno**, Quiero completar un formulario simple en la página pública de la universidad con mi nombre y correo electrónico, Para que el equipo de admisiones de Lumina Tech me contacte con información sobre la carrera que me interesa.

**⛔ Pre-requisitos (Dependencias):** HU-S3-01 completada (Sitio publicado y acceso público activado).

**💡 Justificación (Business Value):** Cada visitante que no puede dejar sus datos es un prospecto perdido. Este formulario convierte el tráfico web en Leads directamente en Salesforce, eliminando el proceso manual de Marta Gómez de transcribir correos y llamadas a registros del sistema.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Crear el Screen Flow (Herramienta: Setup → Flows → New Flow):** Seleccionar **Screen Flow**. Label: `Lumina EC Captación Futuro Alumno`. API Name: `Lumina_EC_Captacion_Futuro_Alumno`.
2. **Pantalla 1 — Datos de Contacto:** Agregar un elemento **Screen**. Label: `Tus Datos`. Componentes a incluir:
   - `Name` — Objeto Nombre (First Name + Last Name) — API: `inputNombre` — Obligatorio ✅
   - `Email` — Email — API: `inputEmail` — Obligatorio ✅
   - `Phone` — Teléfono (Celular) — API: `inputCelular` — Obligatorio ✅
3. **Elemento Create Records:** Crear un registro en el objeto `Lead` mapeando:
   - `FirstName` ← `{!inputNombre.firstName}`
   - `LastName` ← `{!inputNombre.lastName}`
   - `Email` ← `{!inputEmail.value}`
   - `Phone` ← `{!inputCelular.value}`
   - `LeadSource` ← valor literal `Web`
   - `Company` ← valor literal `Lumina Tech - Prospecto` *(campo requerido)*
4. **Elemento Action (Enviar Email Automático):** Agregar un nodo de tipo Action -> Send Email:
   - `Body` ← `¡Hola {!inputNombre.firstName}! Gracias por escribir a Lumina Tech. Recibimos tus datos correctamente y muy pronto un asesor de Admisiones te contactará. Mientras tanto, puedes revisar nuestro Campus Virtual.`
   - `Subject` ← `¡Gracias por tu interés en Lumina Tech!`
   - `Recipient Email Addresses` ← `{!inputEmail.value}`
5. **Pantalla de Éxito:** Agregar una **Screen** final con un componente `Display Text`. Mensaje: `✅ ¡Gracias por tu interés en Lumina Tech! Te hemos enviado un correo de confirmación a {!inputEmail.value}.`
6. **Fault Path:** Conectar el nodo Create Records → Agregar **Fault Path** → Nueva Screen con mensaje amigable: `Ups, ocurrió un problema. Por favor intente nuevamente o contáctenos por teléfono. Detalle técnico: {!$Flow.FaultMessage}`.
7. **Guardar y Activar** el Flow.
8. **Configurar permisos del Guest User Profile (Herramienta: Setup → All Sites → [Sitio] → Guest User Profile):** Ir al perfil del Guest User del sitio. En **Object Permissions** para `Lead`, activar: **Read, Create**. En la sección de **Flows**, agregar el Flow `Lumina_EC_Captacion_Futuro_Alumno` a la lista de Flows ejecutables.
9. **Publicar el Flow en el Sitio (Herramienta: Experience Builder):** En el Builder, navegar a la página pública. Desde el panel de componentes arrastrar el componente estándar **Flow** a la página. En su configuración, seleccionar `Lumina EC Captación Futuro Alumno`. Hacer clic en **Publish**.

**✅ Criterios de Aceptación (QA Check):**
1. Abrir el sitio en modo incógnito. Verificar que el formulario es visible sin necesidad de login.
2. Completar el formulario con datos ficticios (`Test Prospecto` / `test@prueba.com`) y enviarlo. Verificar que aparece la pantalla de éxito con el email ingresado.
3. En Salesforce (sesión de Admin), ir a la pestaña **Leads** y verificar que existe el registro de `Test Prospecto` con `LeadSource = Web`. Además verificar (vía bandeja de entrada en pruebas) que el prospecto recibió su correo de confirmación automático.
4. **Prueba Negativa:** Intentar enviar el formulario con el campo Email o Apellido vacío. Verificar que el Flow bloquea el avance.
5. **Prueba de Seguridad:** Si el formulario presenta error al guardar en modo incógnito, ir directamente al Guest User Profile y verificar los permisos CRUD en Lead — no modificar el Flow.

---

## 🏗️ ÉPICA 2: Portal del Alumno — Mesa de Ayuda Privada

**Objetivo:** Ofrecer a los alumnos activos un espacio seguro con login donde puedan reportar problemas y trámites sin visitar físicamente la oficina, generando Cases que caen directamente en la bandeja de Administración.

---

### HU-S3-03: Habilitación de Alumnos como Usuarios del Portal (Community Users)
**Estimación:** 🟡 2 SP
**Prioridad:** Alta
**Enlace Req:** `[REQ-EC-003]`
**Etiquetas Trello:** 🔴 `[Rojo] Seguridad` | 🟡 `[Amarillo] Usuarios`

**Descripción:**
Como **Administrador Salesforce**, Quiero habilitar a los alumnos activos como usuarios autenticados del portal de Experience Cloud, Para que puedan iniciar sesión de forma segura y acceder al formulario de reclamos y a la base de conocimientos privada.

**⛔ Pre-requisitos (Dependencias):** HU-S3-01 completada. Los Contacts de Lucas Martinez y Ana Vega deben existir en la Org con Rol__c = Alumno (verificado en HU-S3-00).

**💡 Justificación (Business Value):** Sin este paso, el portal privado no existe. Habilitar a un alumno como Community User es el acto técnico que vincula su registro de persona (Contact) con una cuenta de acceso al sistema, habilitando la experiencia de autoservicio que la Rectora Vance solicita.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Navegar al Contact del Alumno (Herramienta: Contacts → Lucas Martinez):** Abrir el registro del Contact de Lucas Martinez.
2. **Habilitar el Portal User:** En el registro del Contact, hacer clic en el botón **Enable Customer User** (o el equivalente en Experience Cloud: **"Manage External User"**). Se abrirá un formulario para crear el usuario.
3. **Configurar el Usuario del Portal:**
   - **Email:** el email del Contact (se usará como username)
   - **Username:** debe ser único en Salesforce (ej: `lucas.martinez@luminatech.edu`)
   - **Profile:** Seleccionar `Customer Community User` (o el perfil asociado al sitio)
   - **Role:** `Customer Portal User` (si aplica)
4. **Guardar y Enviar Email de Confirmación:** Hacer clic en **Save**. El sistema enviará un correo al alumno con el link para establecer su contraseña.
5. **Repetir el proceso para Ana Vega** (segundo usuario de prueba).
6. **Verificar Permisos del Community User Profile (Herramienta: Setup → Profiles → Customer Community User):** En el perfil, confirmar que tiene acceso de lectura al objeto `Case` y permisos para crear nuevos Cases. Ajustar si es necesario.

**✅ Criterios de Aceptación (QA Check):**
1. Verificar en `Setup → Users` que Lucas Martinez aparece como usuario activo con Profile = Customer Community User.
2. Abrir el sitio en modo incógnito e intentar hacer login con las credenciales de Lucas Martinez. Verificar que el acceso es exitoso y que redirige a la página de inicio del portal privado.
3. Verificar que Lucas Martinez **no puede ver** los datos internos de Salesforce (objetos como `Materia__c`, `Inscripcion__c` en modo administrador) — solo ve las páginas del portal.
4. **Prueba de límite de licencias:** Verificar que solo se crearon los 2 usuarios necesarios para pruebas, sin exceder las licencias disponibles de la Developer Edition.

---

### HU-S3-04: Screen Flow Privado para Reclamos y Trámites del Alumno (Case)
**Estimación:** 🔴 5 SP
**Prioridad:** Alta
**Enlace Req:** `[REQ-EC-004]`
**Etiquetas Trello:** 🟠 `[Naranja] Automatización (Flows)` | 🔵 `[Azul] Experience Cloud` | 🟢 `[Verde] Soporte`

**Descripción:**
Como **Alumno activo de Lumina Tech**, Quiero completar un formulario paso a paso dentro del portal para reportar un problema (ej: "No veo mi nota de Algoritmos I") o solicitar un trámite (ej: "Quiero un certificado de alumno regular"), Para que mi solicitud se registre como un ticket en el sistema y el equipo de Administración me responda sin necesidad de ir físicamente a la oficina.

**⛔ Pre-requisitos (Dependencias):** HU-S3-03 completada (Alumnos habilitados como Community Users). El objeto estándar `Case` debe estar visible en la Org.

**💡 Justificación (Business Value):** Cada visita física innecesaria a la oficina consume tiempo del alumno y del personal de Administración. Un formulario estructurado asegura que el ticket llegue con toda la información necesaria, reduce el tiempo de resolución y descongestion la carga operativa de Marta Gómez.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Crear el Screen Flow (Herramienta: Setup → Flows → New Flow):** Seleccionar **Screen Flow**. Label: `Lumina EC Reclamos y Tramites Alumno`. API Name: `Lumina_EC_Reclamos_Tramites_Alumno`.
2. **Paso 1 — Categoría del Trámite:** Agregar elemento **Screen**. Label: `¿Qué necesitás?`. Componente:
   - `Picklist` — Label: `Tipo de solicitud` — API: `inputTipoSolicitud` — Obligatorio ✅ — Valores:
     - `Consulta académica`
     - `Nota o calificación`
     - `Certificado de alumno regular`
     - `Justificación de inasistencia`
     - `Otro`
3. **Paso 2 — Detalle del Problema:** Agregar elemento **Screen**. Label: `Contanos más`. Componentes:
   - `Long Text Area` — Label: `Descripción del problema` — API: `inputDescripcion` — Obligatorio ✅ — Placeholder: `Ej: No veo mi nota de Algoritmos I del parcial del 10/03`
   - `Text` — Label: `Materia involucrada (si aplica)` — API: `inputMateria` — Opcional.
4. **Variable de ID del Alumno (Arquitectura Clave):** Antes del Create Records, agregar una **Assignment** que capture automáticamente el ID del alumno logueado:
   - Si la variable global `{!$User.ContactId}` está disponible usarla directamente.
   - Si no, agregar un `Get Records` sobre el objeto `Contact` filtrando `Id = {!$User.ContactId}` para obtener el Contact completo.
5. **Elemento Create Records (Case):** Crear un registro en el objeto `Case` mapeando:
   - `Subject` ← `{!inputTipoSolicitud}` (resumen del ticket)
   - `Description` ← `{!inputDescripcion}`
   - `ContactId` ← `{!$User.ContactId}` *(vincula el Case al alumno logueado automáticamente — sin que él lo escriba)*
   - `Origin` ← valor literal `Web`
   - `Status` ← valor literal `New`
   - `Priority` ← valor literal `Medium`
6. **Pantalla de Confirmación:** Screen final. Mensaje: `✅ Tu solicitud fue enviada exitosamente. El equipo de Administración revisará tu caso y te responderá por correo. Tu referencia: Tipo — {!inputTipoSolicitud}.`
7. **Fault Path:** Conectar desde Create Records → Screen con mensaje: `Ocurrió un error al registrar tu solicitud. Por favor intenta nuevamente. Si el problema persiste, contacta a Administración directamente.`
8. **Guardar y Activar** el Flow.
9. **Publicar en la Página Privada del Portal (Herramienta: Experience Builder):** En el Builder, navegar a la página que requiere login (o crear una nueva página privada). Arrastrar el componente estándar **Flow** y seleccionar `Lumina EC Reclamos y Tramites Alumno`. Publicar el sitio.

**✅ Criterios de Aceptación (QA Check):**
1. Iniciar sesión en el portal como Lucas Martinez. Verificar que el formulario de reclamos es visible en la página privada.
2. Completar el formulario: seleccionar `Nota o calificación`, describir el problema, y enviarlo. Verificar que aparece la pantalla de confirmación.
3. En la sesión de Admin, ir a la pestaña **Cases** y verificar que existe el Case con `ContactId = Lucas Martinez`, `Origin = Web`, `Status = New`.
4. **Prueba crítica de seguridad:** Abrir el sitio en modo incógnito (sin login) e intentar acceder a la URL de la página de reclamos. Verificar que el portal redirige al login — no debe ser accesible para visitantes anónimos.
5. **Prueba del ContactId automático:** Verificar que el Case creado tiene el campo `Contact` relacionado con Lucas Martinez sin que él haya tenido que escribir su nombre.

---

## 🏗️ ÉPICA 3: Base de Conocimiento — Autogestión del Alumno

**Objetivo:** Publicar artículos de preguntas frecuentes en el portal para que los alumnos encuentren respuestas por su cuenta antes de abrir un ticket, reduciendo la carga de atención de Marta Gómez y Roberto Alonso.

---

### HU-S3-05: Activación de Knowledge y Publicación de Artículos FAQ
**Estimación:** 🟡 3 SP
**Prioridad:** Media
**Enlace Req:** `[REQ-KNW-001]`
**Etiquetas Trello:** 🟤 `[Marrón] Gestión de Contenido` | 🔵 `[Azul] Experience Cloud`

**Descripción:**
Como **Director Académico (Roberto Alonso)**, Quiero publicar al menos 3 artículos con las preguntas más frecuentes de los alumnos en el portal, Para que los estudiantes puedan encontrar respuestas por su cuenta a preguntas como "¿Cuándo son los finales?" sin necesidad de llamar a la oficina.

**⛔ Pre-requisitos (Dependencias):** HU-S3-00 completada (Knowledge activado y Knowledge User marcado). HU-S3-01 completada (Sitio de Experience Cloud publicado).

**💡 Justificación (Business Value):** Roberto Alonso y Marta Gómez responden las mismas 20 preguntas todos los días. Cada artículo publicado es un "empleado digital" disponible 24/7 que deflecta tickets de soporte, reduce la carga operativa del equipo interno y mejora la experiencia del alumno al darle respuestas inmediatas.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Crear Data Categories (Herramienta: Setup → Data Categories):** Crear un grupo de categorías llamado `Lumina Knowledge`. Dentro del grupo, crear al menos las siguientes categorías:
   - `Calendarios y Fechas`
   - `Notas y Evaluaciones`
   - `Trámites y Certificados`
2. **Crear Artículo 1 — Calendario de Finales (Herramienta: App Launcher → Knowledge → New):**
   - **Title:** `¿Cuándo son los exámenes finales?`
   - **URL Name:** `calendario-finales`
   - **Data Category:** `Calendarios y Fechas`
   - **Body:** Incluir el calendario de fechas de finales del ciclo actual. (Solicitar las fechas a Roberto Alonso o usar datos de ejemplo para la demo).
   - **Visibility:** Marcar ✅ **"Visible to Customer"** Y ✅ **"Visible in Public Knowledge Base"**.
   - Hacer clic en **Publish**.
3. **Crear Artículo 2 — Justificación de Asistencia:**
   - **Title:** `¿Cómo justifico una inasistencia?`
   - **URL Name:** `justificar-asistencia`
   - **Data Category:** `Trámites y Certificados`
   - **Body:** Pasos para presentar la justificación (formulario, plazo, documentación requerida).
   - **Visibility:** Marcar ✅ **"Visible to Customer"**.
   - Hacer clic en **Publish**.
4. **Crear Artículo 3 — Escala de Notas:**
   - **Title:** `¿Cuál es la escala de calificaciones de Lumina Tech?`
   - **URL Name:** `escala-de-notas`
   - **Data Category:** `Notas y Evaluaciones`
   - **Body:** `La escala de notas de Lumina Tech va del 0 al 10. La nota mínima de aprobación es 6 (seis). Una calificación de 0 a 5 implica la condición de Desaprobado. Las evaluaciones de recuperatorio siguen la misma escala.`
   - **Visibility:** Marcar ✅ **"Visible to Customer"** Y ✅ **"Visible in Public Knowledge Base"**.
   - Hacer clic en **Publish**.
5. **Publicar el Componente Knowledge en el Portal (Herramienta: Experience Builder):** En el Builder, navegar a la página donde se mostrará la base de conocimiento. Desde el panel de componentes, arrastrar el componente estándar **Knowledge** (o **Article List** / **Search**). Configurarlo para mostrar artículos de la categoría `Lumina Knowledge`. Publicar el sitio.

**✅ Criterios de Aceptación (QA Check):**
1. En la sesión de Admin, ir a `App Launcher → Knowledge` y verificar que los 3 artículos existen con estado **Published**.
2. Abrir el sitio en modo incógnito (sin login) y verificar que los artículos marcados como **"Visible in Public Knowledge Base"** (Art. 1 y Art. 3) son visibles para visitantes anónimos.
3. Iniciar sesión como Lucas Martinez y verificar que los 3 artículos son visibles para el alumno logueado.
4. **Prueba de búsqueda:** Escribir `notas` en el buscador del portal. Verificar que el artículo "¿Cuál es la escala de calificaciones?" aparece entre los resultados.
5. **Prueba crítica de visibilidad:** Crear un artículo de prueba **sin** marcar ninguna casilla de visibilidad y verificar que **NO** aparece en el portal — ni para el público ni para el alumno logueado.

---

## 📊 Resumen del Backlog

| ID | HU | SP | Prioridad | Etiquetas Trello |
|:---:|:---|:---:|:---:|:---|
| HU-S3-00 | Activación de la Plataforma de Portal | 1 | 🔴 Crítica | 🔘 [Gris] Configuración Base, 🔴 [Rojo] Seguridad |
| HU-S3-01 | Creación del Sitio con Branding Lumina | 2 | 🔴 Alta | 🟣 [Morado] Branding, 🔵 [Azul] Experience Cloud |
| HU-S3-02 | Screen Flow Público — Captación de Leads | 3 | 🔴 Alta | 🟠 [Naranja] Automatización, 🔵 [Azul] Experience Cloud |
| HU-S3-03 | Habilitación de Alumnos como Community Users | 2 | 🔴 Alta | 🔴 [Rojo] Seguridad, 🟡 [Amarillo] Usuarios |
| HU-S3-04 | Screen Flow Privado — Reclamos y Cases | 5 | 🔴 Alta | 🟠 [Naranja] Automatización, 🔵 [Azul] Experience Cloud, 🟢 [Verde] Soporte |
| HU-S3-05 | Knowledge — 3 Artículos FAQ Publicados | 3 | 🟡 Media | 🟤 [Marrón] Gestión Contenido, 🔵 [Azul] Experience Cloud |
| **TOTAL** | | **16 SP** | | |

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
2. **Habilitar Knowledge User (Herramienta: Setup → Users):** Ir a `Setup → Users → [Tu propio registro de administrador]`. Hacer clic en Edit y marcar la casilla **Knowledge User** ✅. *(Nota: Sin este paso, el siguiente menú no aparecerá).*
3. **Activar Knowledge (Herramienta: Setup → Knowledge Settings):** Apretar F5 para recargar la página tras el paso 2. Buscar `Knowledge` en el Setup Quick Find → Seleccionar `Knowledge Settings` → Marcar el checkbox **Enable Lightning Knowledge** → Save.
4. **Verificar licencias disponibles:** Ir a `Setup → Company Information`. Confirmar que existen licencias del tipo **Customer Community** disponibles. Reservar máximo 2 para pruebas de login de alumnos.
5. **Verificar interacciones de prueba:** Elegir 1 o 2 contactos de tu base (ej. cualquiera de los 200 alumnos registrados). Confirmar que existen en la Org como Alumnos activos (`Rol__c = Alumno`). Estos serán tus usuarios de prueba del portal privado.

**✅ Criterios de Aceptación (QA Check):**
1. Ir a Setup Quick Find y buscar "All Sites". Verificar que el menú existe y que aparece el botón **New** para crear un sitio.
2. Ir a la pestaña de **Knowledge** en App Launcher. Verificar que la pestaña aparece y carga correctamente.
3. Ir a `Setup → Company Information` y confirmar que hay al menos 1 licencia Customer Community disponible.
4. Buscar y elegir cualquier Contact en Salesforce y confirmar que existe con `Rol__c = Alumno` para uso en los siguientes pasos de la configuración.

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
1. **Crear el Screen Flow Base (Herramienta: Setup → Flows → New Flow):** Seleccionar **Screen Flow** y hacer clic en **Create** *(versión actual de Flow Builder)*.
2. **Pantalla 1 — Datos del Prospecto:** Agregar un elemento **Screen** etiquetado como `Tus Datos`.
   - Incorporar componente `Name` (`inputNombre`) dejando Apellido bloqueado como Obligatorio.
   - Incorporar componentes `Email` (`inputEmail`) y `Phone` (`inputCelular`), pasando el toggle del control nativo "Required" en ambos hacia la afirmación `{!$GlobalConstant.True}`.
3. **Elemento Create Records (Lead Prospecto):** Tras la pantalla agregar el bloque nativo `Create Records`. Etiqueta: `Crear Lead Prospecto`. Activar propiedad para asignación **`Manually`** sobre el objeto `Lead`.
   - Mapear variables nativas de objeto: `FirstName` y `LastName` extraídas desde las opciones expandidas de Screens(`inputNombre > FirstName/LastName`).
   - Mapear `Email` y `Phone` desde sus contrapartes de screen extraídas como `> Value`.
   - Asignar text literales críticos faltantes: `LeadSource` ← `Web` y `Company` ← `Prospecto Web Lumina Tech`.
4. **Pantalla de Éxito:** Adjuntar una pantalla final conteniendo un `Display Text` (`mensajeExito`). Incrustando dinámicamente un agradecimiento y la confirmación vía la variable recolectada: `¡Gracias por tu interés en Lumina Tech! Nos comunicaremos contigo a tu correo {!inputEmail.value}.`
5. **Fault Path y Guardado:** Clicando el nodo "Crear Lead Prospecto", agregar su **Fault Path** respectivo. Que derive a otra **Screen** de error con `Display Text` que rinda y exponga en pantalla el aviso: `Ups, ocurrió un problema técnico... {!$Flow.FaultMessage}`. Finalmente **Save** (Nombre:`Lumina EC Captacion Futuro Alumno`) & **Activate** el Flow.
6. **Configurar el Guest User Profile (Setup → All Sites → Builder ⚙️ Settings → General):** Ir al link inferior "Guest User Profile" del sitio. En las clásicas **Object Permissions** para `Leads`, dotarlo firmemente y activar casillas: **Read✅, Create✅**. Seguidamente, en la sección hipervinculada **Flow Access**, mover explícitamente `Lumina_EC_Captacion_Futuro_Alumno` a la columna central "Enabled".
7. **Publicar en Experience Builder:** Arrastrar componente nativo **Flow** al canvas del publicador (lado Home) asignando dinámicamente al componente el Flow en cuestión. Concluir accionando **Publish**.

**✅ Criterios de Aceptación (QA Check):**
1. La comunidad Experience Cloud presenta dentro de sus configuraciones el User Flow Access del *Captacion Futuro Alumno* como Enabled.
2. Abrir la URL del sitio bajo **Navegación de Incógnito**. Se carga el formulario validándose sin que arroje prompt de Login.
3. Al dejar un campo mandatorio en blanco (Ej: Email o Last Name) el flujo bloquea y exigue cumplimento.
4. Tras llenar correctos valores anónimos (ficticios), presionar siguiente transiciona elegantemente la UX a una confirmación sin errores (Sin un Fault Path enmascarado).
5. Un Admin que asoma al Backend Salesforce (Leads Tab), halla creado el prospecto bajo la Lead Source "Web" y compañía "Prospecto Web Lumina Tech".

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
1. **Configurar el Login del Portal — Members (Herramienta: Setup → All Sites):** Ir a `Setup → All Sites` y hacer clic en **Workspaces** al lado del sitio Campus Virtual. Entrar a **Administration → pestaña Members**. En el buscador desplegable cambiar "Portal" por **"All"**. Pasar el perfil **Customer Community User** a la columna "Selected Profiles". Hacer clic en **Save**. *(Si se omite este paso, el botón Enable Customer User no funcionará correctamente y los alumnos no podrán loguearse).*
2. **Navegar al Contact del Alumno (Herramienta: Contacts → Lucas Martinez):** Abrir el registro del Contact de Lucas Martinez.
3. **Habilitar el Portal User:** En el registro del Contact, hacer clic en el botón **Enable Customer User** (o el equivalente en Experience Cloud: **"Manage External User"**). Se abrirá un formulario para crear el usuario.
4. **Configurar el Usuario del Portal:**
   - **Email:** el email del Contact (se usará como username)
   - **Username:** debe ser único en Salesforce (ej: `lucas.martinez@luminatech.edu`)
   - **Profile:** Seleccionar `Customer Community User` (o el perfil asociado al sitio)
   - **Role:** `Customer Portal User` (si aplica)
5. **Guardar y Enviar Email de Confirmación:** Hacer clic en **Save**. El sistema enviará un correo al alumno con el link para establecer su contraseña.
6. **Repetir el proceso para Ana Vega** (segundo usuario de prueba).
7. **Verificar Permisos del Community User Profile (Herramienta: Setup → Profiles → Customer Community User):** En el perfil, confirmar que tiene acceso de lectura al objeto `Case` y permisos para crear nuevos Cases. Ajustar si es necesario.

**✅ Criterios de Aceptación (QA Check):**
1. Verificar en `Setup → Users` que Lucas Martinez aparece como usuario activo con Profile = Customer Community User.
2. Verificar que se recibió el email de activación en el correo configurado para Lucas Martinez. Hacer clic en el link *"Set Password"* del email, establecer una contraseña que controles. Luego abrir el sitio en **modo incógnito** del navegador, ingresar a la URL del portal, e iniciar sesión con las credenciales (`lucas.martinez@luminatech.edu` + la contraseña establecida). Verificar que el login es exitoso y que redirige a la página de inicio del portal privado.
   > **Alternativa rápida (sin esperar el email):** Abrir el registro del Contact de Lucas Martinez → desplegar el menú de opciones (▼ junto a los botones de acción) → seleccionar **"Log in to Experience as User"**. Esto permite ingresar directamente al portal sin necesidad de contraseña.
3. Verificar que Lucas Martinez **no puede ver** los datos internos de Salesforce (objetos como `Materia__c`, `Inscripcion__c` en modo administrador) — solo ve las páginas del portal.
4. **Prueba de límite de licencias:** Verificar que solo se crearon los 2 usuarios necesarios para pruebas, sin exceder las licencias disponibles de la Developer Edition.

---

### HU-S3-04a: Screen Flow Privado — Construcción del Flow (Parte A)
**Estimación:** 🔴 3 SP
**Prioridad:** Alta
**Enlace Req:** `[REQ-EC-004]`
**Etiquetas Trello:** 🟠 `[Naranja] Automatización (Flows)` | 🟢 `[Verde] Soporte`
**Guía:** `HU-S3-04a_Guia.md`

**Descripción:**
Como **Administrador Salesforce**, Quiero construir y activar el Screen Flow de reclamos en el Flow Builder, Para tener el formulario listo para ser publicado en el portal privado del alumno.

**⛔ Pre-requisitos (Dependencias):** HU-S3-03 completada. El objeto estándar `Case` debe estar visible en la Org.

**💡 Justificación (Business Value):** El Flow es el núcleo funcional de la mesa de ayuda digital. Sin él activo, ninguna otra configuración del portal sirve. Construirlo de forma aislada permite probarlo con el botón Debug antes de exponerlo al alumno.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Crear el Screen Flow (Setup → Flows → New Flow → Screen Flow → Create):** El canvas abre directamente sin formulario de propiedades. El Label y API Name se configuran al guardar (Paso 7).
2. **Pantalla 1 "Que necesitas" — Picklist:** Screen label `Que necesitas`. Componente Picklist: API `inputTipoSolicitud` — Obligatorio ✅. Valores (sin tildes para evitar API Names deformados): `Consulta academica` | `Nota o calificacion` | `Certificado de alumno regular` | `Justificacion de inasistencia` | `Otro`. Agregar cada valor buscando en campo Choice → `+ Create 'texto...'`.
3. **Pantalla 2 "Contanos mas" — Detalle:** Screen label `Contanos mas`. Componentes: Long Text Area API `inputDescripcion` (Obligatorio ✅, Placeholder: `Ej: No veo mi nota de Algoritmos I del parcial del 10 de marzo`) + Text API `inputMateria` (Opcional).
4. **Create Records — Case:** Configuración: Label `Crear Case del Alumno` | How to set: `Manually` | Object: `Case`. Mapeo de campos con `+ Add Field`:
   - `Subject` ← `Que necesitas > Tipo de solicitud`
   - `Description` ← `Contanos mas > Descripcion del problema`
   - `Contact ID` ← `Running User > ContactId` *(buscar "Running User" en el Value picker — es como el Flow Builder expone `$User`)*
   - `Case Origin` ← literal `Web`
   - `Status` ← literal `New`
   - `Priority` ← literal `Medium`
5. **Pantalla de Confirmación "Solicitud enviada":** Display Text API `mensajeConfirmacion`. Mensaje con variable dinámica `{!inputTipoSolicitud}` insertada con el botón `{!}`.
6. **Fault Path desde Create Records:** Screen label `Error al enviar` | API `Pantalla_Error`. Display Text API `mensajeError` con `{!$Flow.FaultMessage}` (buscar "Fault" o "Flow" en el resource picker).
7. **Guardar y Activar:** Al hacer Save → diálogo pide Label: `Lumina EC Reclamos y Tramites Alumno` | API Name: `Lumina_EC_Reclamos_Tramites_Alumno`. Luego clic en **Activate**.

**✅ Criterios de Aceptación (QA Check):**
1. En Setup → Flows, el Flow `Lumina EC Reclamos y Tramites Alumno` existe con Status = **Active**.
2. El canvas del Flow muestra: Pantalla 1 → Pantalla 2 → Create Records → Pantalla OK + rama Fault → Pantalla Error.
3. El Picklist `inputTipoSolicitud` tiene los 5 valores configurados.
4. El campo `Contact ID` en el Create Records muestra `Running User > ContactId` (no un valor literal ni un texto vacío).

---

### HU-S3-04b: Screen Flow Privado — Publicación en el Portal (Parte B)
**Estimación:** 🔴 2 SP
**Prioridad:** Alta
**Enlace Req:** `[REQ-EC-004]`
**Etiquetas Trello:** 🔵 `[Azul] Experience Cloud` | 🟢 `[Verde] Soporte`
**Guía:** `HU-S3-04b_Guia.md`

**Descripción:**
Como **Administrador Salesforce**, Quiero publicar el Flow de reclamos en una página privada del portal y actualizar el menú de navegación, Para que los alumnos logueados puedan acceder al formulario desde el Campus Virtual.

**⛔ Pre-requisitos (Dependencias):** HU-S3-04a completada. El Flow `Lumina EC Reclamos y Tramites Alumno` debe estar en estado **Active**.

**💡 Justificación (Business Value):** Un Flow activo pero no publicado en el portal no existe para el alumno. Esta parte conecta la lógica del Flow con la interfaz visual del campus, cerrando el ciclo completo de la funcionalidad de reclamos.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Verificar permisos del perfil (Setup → Profiles → Customer Community User):** En el objeto `Case`, confirmar que están activos: **Read** ✅ y **Create** ✅. Sin este paso, el Flow fallará silenciosamente al intentar crear el Case.
2. **Crear página privada "Tramites" (Experience Builder → + New Page):** Standard Page → Flexible Layout → Page Name: `Tramites` → URL: `tramites`. Inmediatamente después de crearla: ⚙️ **Settings de la página → Page Access → `Requires Login`**. *(La opción "Default" NO garantiza redirección al login en todos los templates — dejar en Default produce pantalla blanca para visitantes anónimos en lugar de redirigir al login.)*
3. **Agregar el componente Flow a la página:** Panel Components (ícono ⚡ izquierda) → buscar `Flow` → arrastrar a la página → en propiedades seleccionar `Lumina EC Reclamos y Tramites Alumno`. *(El Builder mostrará un marcador de posición en lugar del formulario — esto es normal; el Flow corre solo en el sitio publicado con usuario logueado.)*
4. **Actualizar el menú de navegación:** Clic en la barra de navegación → Edit Default Navigation → `+ Add Menu Item` → Name: `Hacer una consulta` | Type: **`Site Page`** *(NO External URL)* | Page: `Tramites` | Publicly available: ✅ **YES** *(el tab debe ser visible para anónimos — la seguridad la maneja Page Access: Requires Login de la página, no el menú. El patrón correcto es: tab visible → clic → redirige al login → tras login llega al formulario.)*
5. **Publicar el sitio:** Botón **Publish** → confirmar publicación. *(Obligatorio después de cambios en el menú y en el Page Access — sin publicar los cambios no se reflejan en el sitio en vivo.)*

**✅ Criterios de Aceptación (QA Check):**
1. El perfil Customer Community User tiene **Read** y **Create** activos en el objeto Case.
2. La página `Tramites` tiene **Page Access: Requires Login** (verificar en Builder → ⚙️ Settings de la página).
3. La página `Tramites` en el Builder muestra el componente Flow con el marcador de posición de `Lumina EC Reclamos y Tramites Alumno`.
4. Abrir el portal en modo incógnito → navegar a la URL del sitio + `/tramites` → debe **redirigir al login** (no pantalla blanca).
5. Iniciar sesión como Lucas Martinez → clic en "Hacer una consulta" en el menú → el formulario de 2 pasos es visible.
6. Completar el formulario y verificar en Admin → Cases que existe el Case con `Origin = Web`, `Status = New`, `Contact = Lucas Martinez` (sin que él lo haya escrito).
7. El menú del sitio publicado muestra: `Inicio | Hacer una consulta`.

---

### HU-S3-04c: Record-Triggered Flow para Enrutamiento de Casos (Before-Save)
**Estimación:** 🟡 3 SP
**Prioridad:** Alta
**Enlace Req:** `[REQ-EC-004]`
**Etiquetas Trello:** 🟠 `[Naranja] Automatización (Flows)` | 🟢 `[Verde] Soporte`
**Guía:** `HU-S3-04c_Guia.md`

**Descripción:**
Como **Administrador Salesforce**, Quiero construir un Flow que se dispare antes de guardar un Caso (Before-Save), Para asignar automáticamente la Prioridad y el Responsable (Owner) basándose en si la solicitud es académica o administrativa.

**⛔ Pre-requisitos (Dependencias):** HU-S3-04a completada.

**💡 Justificación (Business Value):** Separar la lógica de negocio de la interfaz de usuario (Screen Flow) asegura que los casos siempre se enruten correctamente, independientemente de si el caso se crea a través del portal de Experience Cloud, por correo electrónico, o manualmente. Usar un Flow Before-Save es la mejor práctica arquitectónica porque es más eficiente y no consume límites DML.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Crear Colas (Queues):** En Setup → Queues, crear `Cola_Academica` (añadir a Roberto Alonso) y `Cola_Administrativa` (añadir a Marta Gómez). Asegurarse de que el objeto `Case` esté soportado por ambas colas.
2. **Crear el Record-Triggered Flow:** Object: `Case` | Trigger: `A record is created` | Optimize the Flow for: **`Fast Field Updates`** (Before-Save).
3. **Añadir elemento Decision "Categorizar Solicitud":** 
   - **Ruta 1 (Académica):** Criterios `{!$Record.Subject}` contiene `Nota` OR `Consulta academica`.
   - **Ruta Default (Administrativa):** Todas las demás (ej. inasistencias, certificados).
4. **Obtener IDs de Colas (Get Records):** En cada ruta, usar un elemento "Get Records" sobre el objeto `Group` (Type = 'Queue', DeveloperName = 'Cola_Academica' o 'Cola_Administrativa') para extraer el ID dinámicamente sin hardcodear.
5. **Añadir elementos Assignment:** 
   - **Ruta Académica:** Asignar `{!$Record.Priority}` = `High`. Asignar `{!$Record.OwnerId}` al ID extraído de la Cola Académica.
   - **Ruta Administrativa:** Asignar `{!$Record.Priority}` = `Medium`. Asignar `{!$Record.OwnerId}` al ID extraído de la Cola Administrativa.
6. **Guardar y Activar:** Guardar con el nombre `Lumina Casos Before-Save Routing`. Activar el Flow.

**✅ Criterios de Aceptación (QA Check):**
1. En Setup → Flows, el Flow `Lumina Casos Before-Save Routing` está Activo y su trigger es Fast Field Updates.
2. Iniciar sesión en el portal como Lucas Martinez y solicitar un "Certificado de alumno regular". En Salesforce, el caso creado tiene Prioridad "High" y el Owner es la "Cola Académica".
3. Iniciar sesión como Lucas y solicitar "Justificación de inasistencia". En Salesforce, el caso tiene Prioridad "Medium" y el Owner es la "Cola Administrativa".

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
1. **Configurar Knowledge Setup (Setup → Service Setup):** Buscar "Knowledge Setup" en el asistente, iniciar, elegir autores, crear el grupo de Data Categories `Lumina Knowledge` con sus 3 categorías (Calendarios, Notas, Tramites) y finalizar el asistente.
2. **Crear campo "Cuerpo del Articulo" y ajustar layout:** En Object Manager → Knowledge, crear campo Text Area (Rich). Luego ir al Page Layout y agregar este nuevo campo a la sección Knowledge Detail. *(Las casillas de visibilidad pública aparecen ya nativamente en la sección Properties del modal al crear el registro).*
3. **Mapeo de Data Categories (Setup → Topics for Objects):** Buscar Knowledge y habilitar el check "Enable Topics". (Paso crítico para que el portal lea la base de datos).
4. **Configurar Visibilidad Externa (Setup → Sharing Settings):** Buscar Sharing Settings, editar "Organization-Wide Defaults", buscar el objeto **Knowledge** y cambiar su "Default External Access" a **Public Read Only** (Sólo lectura pública). (Garantiza que usuarios Experience Cloud puedan ver los artículos).
5. **Crear Artículo 1 — Exámenes Finales (App Launcher → Knowledge → New):**
   - **Title:** `Cuando son los examenes finales`
   - **Data Category:** `Lumina Knowledge → Calendarios y Fechas`
   - **Visibilidad (Properties):** ✅ **Visible para el cliente** + ✅ **Visible en base de conocimientos pública**.
   - Hacer clic en **Publish**.
6. **Crear Artículo 2 — Justificación e Inasistencia:**
   - **Title:** `Como justifico una inasistencia`
   - **Data Category:** `Lumina Knowledge → Tramites y Certificados`
   - **Visibilidad (Properties):** ✅ **Visible para el cliente** únicamente (solo alumnos logueados).
   - Hacer clic en **Publish**.
7. **Crear Artículo 3 — Escala de Calificaciones:**
   - **Title:** `Cual es la escala de calificaciones de Lumina Tech`
   - **Data Category:** `Lumina Knowledge → Notas y Evaluaciones`
   - **Visibilidad (Properties):** ✅ **Visible para el cliente** + ✅ **Visible en base de conocimientos pública**.
   - Hacer clic en **Publish**.
8. **Organizar Temas en Experience Cloud (Workspaces → Content Management):** Ir a Topics → Automatic Topic Assignment y activar el puente. Luego ir a **Temas Destacados (Featured Topics)**, adjuntar la Data Category y subir la imagen de portada HD a cada respectiva categoría para que luzca en el Home.
9. **Crear página "Preguntas frecuentes" en Experience Builder:** Crear Standard Page `Preguntas frecuentes` (URL `faqs`). Configurar **Page Access: Public**.
10. **Agregar componente:** Arrastrar el componente **"Trending Articles by Topic"**.
11. **Actualizar menú de navegación:** Agregar pestaña "Preguntas frecuentes" (Site Page, Publicly available: YES). Publicar el sitio.

**✅ Criterios de Aceptación (QA Check):**
1. Setup → Data Category Setup: el grupo `Lumina Knowledge` existe con estado **Active**.
2. App Launcher → Knowledge: existen exactamente **3 artículos publicados**.
3. La página principal Inicio (Home) exhibe una franja visual con los 3 **Temas Destacados** ilustrados con imágenes fotográficas.
4. El menú del sitio publicado muestra: `Inicio | Hacer una consulta | Preguntas frecuentes`.
5. Navegador en incógnito (Anónimo) → clic en "Preguntas frecuentes": Art. 1 (Finales) y Art. 3 (Escala) son visibles sin login. El Art. 2 (Justificación) NO es visible.
6. Iniciar sesión como Lucas Martinez → los **3 artículos** son visibles.
7. Buscador del portal inteligente: Escribir `notas` → aparece el Art. 3 entre los resultados con link al detalle.


---

## 🏗️ ÉPICA 4: Soporte Síncrono Estudiantil — Omni-Channel Chat

**Objetivo:** Habilitar un canal de atención en tiempo real (Live Chat) dentro del Campus Virtual, permitiendo a los alumnos contactar inmediatamente al personal de soporte y a los agentes gestionar la carga conversacional mediante Omni-Channel en su Service Console.

---

### HU-S3-06: Implementación de Soporte en Tiempo Real (Live Chat)
**Estimación:** 🟢 4 SP
**Prioridad:** Alta (Bonus Track Sprint 3)
**Enlace Req:** `[REQ-CHAT-001]`
**Etiquetas Trello:** 🟢 `[Verde] Soporte` | 🔵 `[Azul] Experience Cloud`
**Guía:** `HU-S3-06_Guia.md`

**Descripción:**
Como **Alumno Matriculado (o Visitante Anónimo)**, Quiero hacer clic en un botón flotante de chat en el portal para hablar con un agente en tiempo real, Para resolver mis inquietudes académicas o de inscripción instantáneamente sin tener que escribir un correo o llamar.

**⛔ Pre-requisitos (Dependencias):** HU-S3-01 (Portal creado). App Service Console disponible. Perfiles de Soporte creados (o Admin).

**💡 Justificación (Business Value):** La resolución de dudas síncrona eleva drásticamente la satisfacción de alumnos y prospectos. Un canal de chat embebido deflecta llamadas telefónicas y centraliza la carga de trabajo de Marta Gómez en una cola que Omni-Channel administra inteligentemente.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Fase 1 (Creación de Cola):** Utilizar flujo "Chat with Customers" (Service Setup) para crear grupo, cola de enrutamiento asignando agentes y generar la URL.
2. **Fase 2 (Chat Agent):** Configurar preferencias de agente (Sneak Peek, Notificaciones, Saludo automático).
3. **Fase 3 (Consola):** Agregar "Chat Sessions" y el widget Omni-Channel al App Manager (Service Console).
4. **Fase 4 (Despliegue EC):** Arrastrar "Embedded Service Chat" al Builder. Ajustar configuración de seguridad CSP a Relaxed y Trusted Sites si es necesario.
5. **Fase 5 (Activación):** Desplegar Omni-Channel en Online y verificar cambio de estado del botón a "Chat with an expert".

**✅ Criterios de Aceptación (QA Check):**
1. El Agente puede ponerse en estado Available desde Omni-Channel en la Service Console.
2. El Portal EC muestra el botón flotante en la esquina inferior "Chat with an expert".
3. Al enviar un mensaje desde la web, suena el timbre y entra la sesión a la Service Console del agente.
4. Las políticas CSP no bloquean la renderización del widget en Google Chrome modo incógnito.

---

### HU-S3-07: Implementación de Einstein Bot Básica (LuminaBot)
**Estimación:** 🟢 3 SP
**Prioridad:** Media (Bonus Track Avanzado Sprint 3)
**Enlace Req:** `[REQ-CHAT-002]`
**Etiquetas Trello:** 🟠 `[Naranja] Automatización` | 🤖 `[Magenta] IA & Bots`
**Guía:** `HU-S3-07_Guia.md`

**Descripción:**
Como **Alumno Matriculado (o Visitante Anónimo)**, Quiero interactuar con un asistente digital automatizado al iniciar el chat, Para recibir opciones rápidas de auto-servicio antes de ser transferido a un agente humano, ahorrando tiempo de espera.

**⛔ Pre-requisitos (Dependencias):** HU-S3-06 (Omni-Channel y Live Chat desplegados). Licencias de Einstein Bots aceptadas en la organización.

**💡 Justificación (Business Value):** La implementación de un bot de Nivel 1 (menús) actúa como la principal barrera de contención para la mesa de ayuda. Desvía consultas repetitivas hacia la base de conocimientos y recopila el contexto del usuario (triaje) antes de enrutar el chat a un humano en Omni-Channel, reduciendo el TMO (Tiempo Medio Operativo) de los agentes.

**⚙️ Pasos de Implementación (Admin Task):**
1. **Fase 1 (Asistente de Creación):** Setup → Einstein Bots → Nuevo Bot. Elegir **Bot Estándar** + **Comenzar desde cero** → Nombre `Lumina Bot`, idioma Español → Menú con 3 opciones → Vincular al Embedded Service Deployment `Agentes de chat para soporte web`.
2. **Fase 2 (Diálogo de Carreras):** Agregar Pregunta Estática con 5 botones de carrera. Variable `carreraSeleccionada`. Crear 5 diálogos individuales (`Info_Software`, `Info_Marketing`, `Info_Datos`, `Info_Ciberseguridad`, `Otra_Carrera`) con componente Mensaje + texto y link. Agregar 5 bloques de Reglas para enrutar según `carreraSeleccionada`. En cada diálogo de carrera, agregar pregunta de navegación con botones "Ver otra carrera" / "Volver al menú principal" usando variable `accionMenu` y 2 Reglas de redirección.
3. **Fase 3 (Diálogo Trámites):** Agregar Mensaje con link al formulario `/tramites` del portal.
4. **Fase 4 (Diálogo Agente):** Configurar "Siguiente paso" como "Transferir a un agente" (diálogo nativo del sistema).
5. **Fase 5 (Activación):** Clic en Activar → Probar en portal incógnito con agente Available en Omni-Channel.

**✅ Criterios de Aceptación (QA Check):**
1. El chat del portal abre con el saludo de Lumina Bot (sin ir directo al agente humano).
2. Los 3 botones del menú principal son visibles y clicables.
3. Al elegir una carrera, aparece el mensaje descriptivo con el link al catálogo.
4. Los botones "Ver otra carrera" y "Volver al menú principal" navegan correctamente sin cerrar el chat.
5. "Hablar con un agente" transfiere la sesión a Omni-Channel y activa el timbre en la Service Console.

---

## 📊 Resumen del Backlog

| ID | HU | SP | Prioridad | Etiquetas Trello |
|:---:|:---|:---:|:---:|:---|
| HU-S3-00 | Activación de la Plataforma de Portal | 1 | 🔴 Crítica | 🔘 [Gris] Configuración Base, 🔴 [Rojo] Seguridad |
| HU-S3-01 | Creación del Sitio con Branding Lumina | 2 | 🔴 Alta | 🟣 [Morado] Branding, 🔵 [Azul] Experience Cloud |
| HU-S3-02 | Screen Flow Público — Captación de Leads | 3 | 🔴 Alta | 🟠 [Naranja] Automatización, 🔵 [Azul] Experience Cloud |
| HU-S3-03 | Habilitación de Alumnos como Community Users | 2 | 🔴 Alta | 🔴 [Rojo] Seguridad, 🟡 [Amarillo] Usuarios |
| HU-S3-04a | Screen Flow Privado — Construcción del Flow (Flow Builder) | 3 | 🔴 Alta | 🟠 [Naranja] Automatización, 🔵 [Azul] Experience Cloud, 🟢 [Verde] Soporte |
| HU-S3-04b | Screen Flow Privado — Publicación en el Portal (Builder) | 2 | 🔴 Alta | 🔵 [Azul] Experience Cloud, 🟢 [Verde] Soporte |
| HU-S3-05 | Knowledge — 3 Artículos FAQ Publicados | 3 | 🟡 Media | 🟤 [Marrón] Gestión Contenido, 🔵 [Azul] Experience Cloud |
| HU-S3-06 | Implementación Soporte Tiempo Real (Live Chat) | 4 | 🔴 Alta | 🟢 [Verde] Soporte, 🔵 [Azul] Experience Cloud |
| HU-S3-07 | Implementación de Einstein Bot Básica | 3 | 🟡 Media | 🟠 [Naranja] Automatización, 🤖 [Magenta] IA & Bots |
| **TOTAL** | | **23 SP** | | |

# Guía de Solución: Superbadge Agentforce Service

Esta guía proporciona los pasos detallados para completar cada uno de los 4 desafíos de la Superbadge **Agentforce Service**.

## Desafío 1: Configurar el Agente y la Biblioteca de Datos de Agentforce

### 1. Activar Einstein y Agentforce
*(Si no están habilitados en la organización previamente)*
* Ve a **Setup** > **Einstein Setup** y activa Einstein.
* Ve a **Setup** > **Agentforce** y asegúrate de que Agentforce esté habilitado.

### 2. Crear las Bibliotecas de Datos
1. Desde el **App Launcher** (Lanzador de aplicaciones), busca y selecciona **Data Libraries** (o "Bibliotecas de datos").
   * **Nota:** Si no lo encuentras inmediatamente: haz clic en **View All** (Ver todo) en el App Launcher y usa la barra de búsqueda superior. Alternativamente, puedes ir a **Setup** (Configuración), buscar "Agentforce Data Library" (o "Data Libraries") en la barra de *Quick Find*, o buscar la aplicación **Agentforce** en el App Launcher, la cual suele tener esta pestaña.
2. Crea la primera biblioteca para los artículos de Knowledge:
   * Haz clic en **New**.
   * **Label:** `Coral Cloud Experience Agent Library`
   * **Type:** `Knowledge`
   * **Identifying Fields:** Selecciona `Title` y `Summary`.
   * **Content Fields:** Selecciona `Answer` y `Question`.
   * Guarda y espera a que el estado esté en *Ready* o *In Progress*.
3. Crea la segunda biblioteca para el archivo PDF:
   * Haz clic en **New**.
   * **Label:** `Code of Conduct Agreement`
   * **API Name:** `Code_of_Conduct_Agreement`
   * **Type:** `File`
   * **File:** Sube el archivo proporcionado `CC_User_Agreement.pdf` (puedes encontrarlo en la pestaña *Archivos* (Files) de la App u organizador previamente cargado en la org). No le cambies el nombre.

### 3. Configurar el Agente
1. Ve a **Setup** > **Agents** (o Agentforce).
2. Selecciona **Coral Cloud Experience Agent** y haz clic en **Edit** (o ábrelo en Agent Builder y ve a sus propiedades).
3. Configura los siguientes campos exactamente como se solicita:
   * **Description:** `This is Coral Cloud Resorts' AI agent, designed to help customers discover resort experiences and book sessions seamlessly, particularly during the film festival.`
   * **Role:** `You're an AI concierge at Coral Cloud Resorts. Your role is to assist customers with booking and managing services during the film festival by providing accurate information and resolving inquiries swiftly.`
   * **Company:** `Coral Cloud Resorts offers destination experiences that blend unique, premium activities with unmatched customer care. Our discerning customers value effortless, quality reservation services, where every interaction enhances their journey.`
4. En las fuentes de conocimiento del agente, asegúrate de que la Biblioteca de Conocimiento (`Coral Cloud Experience Agent Library`) y la del Código de Conducta estén vinculadas apropiadamente a través de los **Data Sources** o como parte de los flujos de información del agente si se requiere explícitamente en el primer paso (el Desafío 1 los evalúa por su creación).

---

## Desafío 2: Crear el Tema de Gestión de Reservas

1. Desde **Setup** > **Agents**, abre el **Coral Cloud Experience Agent** en el **Agent Builder** (Constructor de Agente).
2. Ve a la pestaña o sección de **Topics** (Temas) y haz clic en **New Topic**.
3. Configura las propiedades del Tema:
   * **Topic Label:** `Booking Management`
   * **Classification Description:** `This topic handles customer inquiries about booking experiences at Coral Cloud Resorts. It includes making new reservations, modifying existing bookings, and addressing questions about experience details to ensure a smooth and satisfying customer journey.`
   * **Scope:** `Your job is to assist customers with managing their bookings for Coral Cloud Resorts experiences. This includes providing accurate information, resolving booking-related issues, and ensuring every interaction is seamless and stress-free.`
4. Agrega las **Instructions** (Instrucciones) al Tema:
   * **1st Instruction:** `Always request the Booking Record Number, which begins with 'B-', before accessing booking details. Use the 'Get Booking' action to retrieve and share the relevant information with the customer.`
   * **2nd Instruction:** `Prompt the user to specify the action they’d like to take on their booking. Available options include adding and removing guests or canceling the booking.`
   * **3rd Instruction:** `For booking cancellations, confirm the action with the user by displaying the Experience Name. Then call the 'Cancel Booking' action.`
   * **4th Instruction:** `To add guests to a confirmed booking, ask the user for the total number of guests, including the contact, who plan to attend the session. Use the previously provided Booking Record Number (starting with 'B-') to call the 'Adjust Booking' action.`
5. Ve a la sección de **Actions** (dentro del mismo Tema `Booking Management`) y haz clic en **New Action** (Nueva Acción) para agregar los tres flujos requeridos. *Nota: Durante la creación de las acciones te pedirá obligatoriamente un **"Loading Text"** (Texto de carga). Trailhead no evalúa lo que pongas aquí, así que puedes escribir textos descriptivos como "Buscando reserva...", "Ajustando reserva...", etc.*:
   * **Action 1:** Selecciona **Reference Action** > **Flow** y elige el flujo de autolanzado llamado `Get Booking`. En un posible paso de configuración (como el campo Loading Text), escribe `Getting booking details...` y haz clic en **Finish**. Verifica que el Input requiera la variable.
   * **Action 2:** Agrega el flujo `Adjust Booking`. De igual forma, provee un Loading Text (ej. `Adjusting booking...`).
   * **Action 3:** Agrega el flujo `Cancel Booking`. Usa un Loading Text como `Canceling booking...`. Además, asegúrate de habilitar la casilla **"Require confirmation"** (Requerir confirmación del usuario) en la configuración de esta acción, dado que las instrucciones exigen que el agente confirme con el usuario antes de cancelar.
6. Guarda y asegúrate de que el tema esté habilitado.

---

## Desafío 3: Añadir Temas Estándar e Integrar el Prompt

### 1. Configurar la Plantilla de Prompt (Prompt Template)
1. Ve a **Setup** y en la barra de *Quick Find* busca **Prompt Builder**.
2. Haz clic en **Prompt Builder** y busca y edita la plantilla llamada `Film_Festival_Related_Answers`.
3. **Insertar la Pregunta del Usuario:**
   * En el área de texto (Prompt Workspace), localiza exactamente el texto `[Input the customer's question]`.
   * Bórralo con cuidado (incluyendo los corchetes `[ ]`).
   * Manteniendo el cursor allí, ve al panel de recursos a la izquierda, selecciona **Input** y luego haz clic en **Question**. Se debe insertar el bloque `{!$Input.Question}`.
4. **Configurar el primer Recuperador de Datos (Código de Conducta):**
   * Busca el marcador de posición (placeholder) que indica el archivo del código de conducta y bórralo por completo (incluyendo corchetes).
   * Deja el cursor en ese espacio. Haz clic en el botón de **Resource** (barra de herramientas superior del texto) y selecciona **Data Retriever**.
   * Elige el que se llama similar a `File_Code_of_Conduct...`.
   * En el panel derecho de configuración de ese retriever, localiza el campo **Search Text** (Texto de búsqueda) e inserta también **Input > Question**.
5. **Configurar el segundo Recuperador de Datos (Knowledge Articles):**
   * Busca el otro marcador de posición sobre los artículos de Knowledge y bórralo por completo.
   * Añade otro **Data Retriever** en ese sitio y selecciona `KA_Coral_Cloud_Experience...`.
   * En su panel derecho de configuración (**Search Text**), nuevamente inserta **Input > Question**.
6. En la esquina superior derecha, haz clic en **Save** y luego obligatoriamente en **Activate** (Activar).

### 2. Configurar los Temas Estándar en el Agente
1. Ve a **Setup** > **Agents** (o Agentforce) y abre tu **Coral Cloud Experience Agent** en el **Agent Builder**.
2. En la barra lateral izquierda, localiza la sección de **Topics**.
3. Haz clic en la flecha hacia abajo al lado del botón **New** y selecciona **"Add from Asset Library"**. (No elijas "New Topic", ya que eso es para crear uno desde cero).
4. En la ventana que se abre, busca y selecciona **General FAQ** y añádelo.
5. Repite el proceso (New > Add from Asset Library) para añadir el tema estándar **Escalation**.

### 3. Sobrescribir el Tema General FAQ con tu nueva Acción
1. En el **Agent Builder**, haz clic sobre el tema **General FAQ**.
2. En el panel principal del tema, asegúrate de habilitar la opción que dice **Override default behavior** o **Overrides** (que deshabilita el comportamiento por defecto y usa tu propia acción).
3. En la sección inferior de **Actions** de ese tema, haz clic en **New Action**.
4. Elije el tipo de acción: **Prompt Template** y haz clic en *Next*.
5. Selecciona la plantilla que acabas de activar: `Film_Festival_Related_Answers`.
6. En la descripción de la acción pon contexto, y añade un **Loading Text** obligatorio (Ej. `Searching the resort knowledge base...`).
7. Haz clic en **Finish** o **Save**. (Verifica finalmente que no haya otras acciones dentro de *General FAQ* que puedan interferir).

### 4. Revisar la Escalación y Activar
1. En el menú izquierdo, entra al tema de **Escalation** (Escalamiento).
2. Dado que es un tema Estándar, **no necesitas añadir ni ver ninguna acción manual listada** en la pestaña "This Topic's Actions". Su comportamiento predeterminado (transferir al agente) ya funciona internamente de forma automática a través de la configuración de "Connections" del agente. Simplemente asegúrate de que **no esté activada** la opción de anular su comportamiento (No overrides).
3. Si el botón *Activate* del Agente se encuentra disponible arriba a la derecha, presiónalo para re-activar los cambios en el agente. Así podrá derivar adecuadamente los chats no resueltos.
4. **Nota sobre la activación:** Al intentar activar el Agente, es muy probable que te aparezca una ventana de advertencia indicando que hay *"Configuration Issues Detected: One or more topics overlap"*. **Esto es completamente normal** en este ejercicio. Simplemente haz clic en el botón azul **"Ignore & Activate"** para guardar y activar sin problemas. No modifiques tus textos para intentar complacer a la advertencia, o podrías fallar la evaluación en Trailhead.

---

## Desafío 4: Implementar el Agente y Transferir Conversaciones

### 1. Modificar el Flujo de Enrutamiento Inbound (Route to ESA)
1. Ve a **Setup** > **Flows** (Flujos).
2. Abre el flujo llamado `Route to ESA` (que es de tipo Omni-Channel Routing).
3. Haz clic en el elemento **Route Work** del centro (Enrutar trabajo).
4. Cambia el destino del enrutamiento (*Route To* / *Routing Destination*) y asegúrate de elegir que sea dirigido a un Agente e identifica al **Coral Cloud Experience Agent**.
5. Haz clic en **Save As** (Guardar como nueva versión) y luego en **Activate** (Activar).

### 2. Verificar el Flujo de Escalación (Opcional - solo comprobación)
1. Revisa que el flujo de salida `ESA - Route to Queue` que la org provee esté activo y dirija hacia la cola de mensajería correspondiente. Esto se usa en caso de usar el escalamiento configurado en el Desafío 3.

### 3. Activar y Publicar (Preparativos finales)
1. Asegúrate de que el Agente de Agentforce esté activado (*Activated*) en el **Agent Builder**.
2. (Recomendado) Ve a **Setup** > **Digital Experiences** > **All Sites**. Ingresa al workspace de `coral-cloud`, abre el builder (Constructor) y haz clic en **Publish** (Publicar).
3. (Recomendado) Ve a **Setup** > **Embedded Service Deployments**, publica el `ESA Web Deployment` que conecta el chat web. (Aunque el motor de Trailhead no evalúa explícitamente haber apretado Pubish, es un paso crítico para probarlo en el portal).

¡Evalúa tus desafíos en Trailhead y obtendrás la Superbadge Agentforce Service!

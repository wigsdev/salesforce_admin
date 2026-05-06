# Checklist QA de Implementación y Pruebas
# Historia de Usuario: HU-S3-06
## Implementación de Omni-Channel Live Chat

---

### Resumen
Esta guía detalla la implementación acelerada del soporte en tiempo real (Omni-Channel Live Chat) en el portal de Experience Cloud, utilizando el flujo guiado de Salesforce para optimizar la creación de colas y perfiles, culminando con la inserción del widget en la interfaz del alumno.

### Fase 1: Creación de la Cola de Mensajes (Queue) a través del Asistente
El método más eficiente para orquestar los metadatos base.
1. Dirígete a **Service Setup** (Configuración de Servicio).
2. En la lista de flujos recomendados, selecciona **Chat with Customers**.
3. Inicia el flujo:
   - **Nombre de la Cola (Queue Name):** `Web Support`
   - **Nombre del grupo (Group Name):** `Chat Agents`
4. Selecciona a los usuarios que actuarán como agentes de soporte (Ej. Administrador del Sistema).
5. En el paso de URL web, ingresa la URL primaria de tu sitio Experience Cloud.
6. Selecciona el enrutamiento tipo **Service** (esto enlaza los chats con el objeto *Case* para historial).
7. Omite el "Soporte fuera de línea" (Offline Support) si Lumina ya tiene un flujo web nativo de contacto (Lead/Case).

### Fase 2: Configuración del Agente de Chat (Chat Agent Configuration)
Este bloque rige qué capacidades (UX de Agente) tienen los representantes de la universidad en la consola.
1. En el buscador del Setup escribe **Chat Agent Configurations**.
2. Haz clic en **Nueva** y llámala `Web Support Configuration`.
3. Ajusta las preferencias críticas:
   - **Sneak Peek:** Actívalo para que el agente lea lo que el alumno escribe antes de enviar.
   - **Notificaciones:** Activa alertas audibles para *Nuevas solicitudes* y *Pérdida de conexión*.
   - **Auto Greeting:** `Hola, ¿cómo te puedo ayudar hoy con tu consulta en Lumina Tech?`
4. Ve al fondo de la pantalla y asigna esta configuración al perfil `System Administrator` o a tus agentes clave.
5. *(Opcional pero recomendado)* En la sección final relaciona el **Chat Button** generado en la Fase 1.

### Fase 3: Habilitar la Sesión de Chat en la Consola
Los agentes no pueden responder desde el backend tradicional, requieren la Service Console.
1. Ve al Setup y busca **App Manager** (Gestor de Aplicaciones).
2. Localiza la aplicación **Service Console** y pulsa **Edit** (Modificar) con la flecha derecha.
3. Pestaña **Navigation Items**: Busca `Chat Sessions` y pásalo a la columna de elementos seleccionados.
4. *Importante:* Ve a la pestaña **Utility Items** y asegúrate de añadir el componente `Omni-Channel` si no estuviera ya listado para que la barra inferior de presencia exista.

### Fase 4: Integración en Experience Cloud y Conflictos CSP
1. Abre tu portal en **Experience Builder**.
2. Desde el panel de componentes (⚡), arrastra el componente nativo **Embedded Service Chat** a la esquina inferior de tu Default Page.
3. **Resolución de problemas de Seguridad (CSP):** 
   - A menudo el chat no renderiza porque Chrome lo bloquea.
   - Ve a ⚙️ **Settings → Security & Privacy**.
   - Cambia el nivel global de seguridad a `Relaxed CSP`.
   - Si marca un URL bloqueado, cópialo, ve a Salesforce Setup → **Trusted Sites** (Sitios de Confianza) y agrégalo a la lista blanca.

### Fase 5: Activación de Omni-Channel (Prueba Final End-to-End)
1. Con Experience Builder publicado, abre una ventana como Administrador en Salesforce y entra a la App **Service Console**.
2. Haz clic en la barra inferior (Utility Bar) donde dice **Omni-Channel**.
3. Cambia tu estatus de Offline a **Available** (Disponible para resoluciones).
4. Abre el portal Experience Cloud en modo **Incógnito**.
5. Al cargar, el botón que decía "Agent Offline" debería cambiar inmediatamente a **"Chat with an expert"**.
6. Realiza un chat de prueba simulando ser un alumno, y verifica cómo suena y reacciona la Service Console del agente.

---

### Fase 6: Uso del Chat (Guía para la Demo Formal)
Durante la presentación a la Rectora Vance o a los stakeholders administrativos, sigue esta coreografía exacta para demostrar el poder del soporte síncrono:

1. **Preparación del Agente (Service Console):**
   - Abre la ventana del administrador en Salesforce.
   - Ve al App Launcher y abre la **Service Console**.
   - Haz clic en `Omni-Channel` en la barra inferior (Utility bar).
   - Selecciona el estado **Available** (Disponible - Chat).

2. **Preparación del Alumno (Experience Cloud):**
   - Abre el portal del Campus Virtual Lumina Tech en una ventana de **Incógnito**.
   - Haz clic en el botón inferior flotante **"Chat with an expert"** (Chatea con un experto).
   - Llena el *Pre-Chat Form* (si lo tienes configurado) simulando ser un prospecto o alumno con un problema (Ej. "No puedo inscribirme al módulo 3").
   - Haz clic en **Start Chat**.

3. **Demostración de Enrutamiento y *Sneak Peek*:**
   - **Vuelve rápido a tu pantalla de Administrador**. El componente Omni-Channel sonará y la solicitud parpadeará.
   - Presiona **Aceptar (✓)**. Ahora estás conectado con el alumno.
   - **Vuelve a la pantalla de Incógnito** y empieza a escribir una queja como si fueras el alumno, pero **NO la envíes** aún.
   - **Regresa a la pantalla del Administrador** y muestra a los asistentes cómo, gracias al *Sneak Peek*, el agente ya puede leer en tiempo real lo que el alumno está redactando antes de que presione Enter.

4. **Demostración del Cierre (Transcript):**
   - Cruza un par de mensajes entre ambas ventanas.
   - Finaliza el chat desde la pantalla del alumno (Botón End Chat).
   - En la interfaz del Administrador, cierra la pestaña del chat y muestra cómo toda la conversación queda guardada instantáneamente como un **Chat Transcript** adjunto al Caso de soporte, listo para auditorías futuras.

---

### 📌 Nota Técnica: Saludo Automático del Agente con Nombre Dinámico

El campo **"Saludo automático"** en la pantalla **Setup → Configuraciones de agentes de Chat** admite campos de combinación (merge fields) para personalizar el saludo con el nombre real del agente que toma el chat.

**Configuración correcta:**
1. Ir a **Setup → Configuraciones de agentes de Chat** → Editar la configuración `Agentes de Soporte Lumina`.
2. En el campo **"Saludo automático"**, escribir:
   ```
   ¡Hola! Bienvenido al soporte de Lumina Tech. Soy {!User_FirstName}, ¿en qué puedo ayudarte hoy?
   ```
3. Hacer clic en **"Guardar"**.

> ⚠️ **Error frecuente:** La sintaxis correcta usa **guion bajo**: `{!User_FirstName}`. Usar punto (`{!User.FirstName}`) mostrará el texto literalmente sin resolver. Para consultar los campos disponibles, usar el botón **"Campos de combinación disponibles"** en la misma pantalla.

Cuando un alumno es transferido desde el **Lumina Bot** al agente humano, este saludo se envía automáticamente con el nombre real del agente logueado en la Service Console.

---

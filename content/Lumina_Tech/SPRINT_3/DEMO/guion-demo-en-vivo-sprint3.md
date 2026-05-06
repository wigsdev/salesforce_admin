# Guion de Demo en Vivo: Lumina Tech University (Sprint 3)

**Contexto:** Este guion comienza justo después de terminar la presentación en PPT con el Elevator Pitch. Aquí pasas a compartir la pantalla de tu navegador para mostrar el sistema funcionando en tiempo real.

**Preparación técnica antes de empezar (Estrategia de 3 Pestañas para evitar tiempos de carga):**
1. **Pestaña 1 (Navegador A):** Abierta en la URL del portal público (Inicio), sin iniciar sesión.
2. **Pestaña 2 (Navegador B o Modo Incógnito):** Abierta en el portal privado, ya con la sesión iniciada previamente como la alumna Ana Vega.
3. **Pestaña 3 (Salesforce Backend):** Abierta logueado como Administrador en la **Service Console**, con el Omni-Channel en estado "Available" (Disponible).

---

## 🎤 TRANSICIÓN DESDE LA PPT
**Discurso:**
"La solicitud de la Rectora de Lumina Tech fue muy clara: el equipo administrativo no daba abasto con las llamadas telefónicas y los correos perdidos, y los alumnos tenían que venir físicamente a la oficina para resolver sus problemas. Para solucionarlo, nos pidieron tres cosas clave: un portal de autoservicio para los alumnos, automatizar el ingreso de trámites sin intervención manual, y garantizar que cada solicitud llegue al departamento correcto al instante. Pasemos a la plataforma para ver cómo resolvimos esta necesidad."

---

## 🌐 ESCENARIO 1: El Visitante (Portal Público)
*Encuadre: Pestaña en incógnito, página de inicio del Campus Virtual, sin haber iniciado sesión.*

**1. Mostrar la Identidad Visual (Branding)**
*   *(Acción: Mueve el mouse lentamente por el encabezado y el banner central, o redimensiona un poco la ventana para mostrar que es responsiva).*
*   **Discurso:** "Esta es la nueva vidriera digital de Lumina Tech. Como pueden ver, no es una plantilla genérica; respira la identidad de nuestra universidad usando nuestros colores corporativos y es completamente responsiva para móviles. Para un visitante anónimo, este es su primer contacto oficial."

**2. Formulario de Captación (Screen Flow Público)**
*   *(Acción: Haz clic en la sección de captación o navega hacia el formulario de prospectos).*
*   **Discurso:** "Si un prospecto está interesado, facilitamos el contacto. Se implementó este formulario directamente en la página pública para evitar que los interesados deban escribir correos."
*   *(Acción: Llena los datos rápidamente con un nombre inventado, ej: 'María López' y 'maria@correo.com').*
*   **Discurso:** "Al enviar la información, no se genera un correo que alguien debe leer. El sistema lo procesa inmediatamente y crea un Lead cualificado en el CRM, bajo estrictas políticas de seguridad que protegen el resto de nuestra base de datos."

---

## 🔒 ESCENARIO 2: El Alumno (Portal Privado)
*Encuadre: Misma pestaña de incógnito.*

**1. El Login (Community User)**
*   *(Acción: En la Pestaña 1 pública, haz clic en el botón de Login. Mientras hace la animación de cargar, cambia rápidamente a la Pestaña 2 donde Ana ya está logueada).*
*   **Discurso:** "Ahora cambiemos de perspectiva. Nos ponemos en el papel de Ana, una alumna activa. Al iniciar sesión, la plataforma la reconoce instantáneamente, validando su identidad y dándole acceso seguro a su espacio privado."

**2. Autoservicio Comunitario (Knowledge Base)**
*   *(Acción: Navega a la pestaña de Preguntas Frecuentes. En la barra de búsqueda, escribe 'Exámenes' y deja que muestre los resultados sugeridos antes de hacer clic en el artículo de 'Justificación de Inasistencia').*
*   **Discurso:** "Lo primero que nota Ana es nuestra Base de Conocimientos, ubicada en la pestaña de Preguntas Frecuentes. Como equipo, estructuramos esta información mediante categorías, lo que permite que la alumna use el potente buscador nativo para encontrar su tema específico con mayor facilidad, como vemos aquí con los exámenes. Además, configuramos el portal para que no sea estático: al final de cada artículo, Ana puede iniciar una discusión o dejar preguntas adicionales, permitiendo que la comunidad o nuestro equipo le responda directamente allí. Esto fomenta el autoservicio 24/7 y evita llamadas a la oficina para dudas simples."

**3. Trámites Seguros (Screen Flow Privado)**
*   *(Acción: Ve a la página de Trámites y abre el formulario de reclamos).*
*   **Discurso:** "Si Ana necesita escalar un problema, utiliza este proceso guiado. Dado que ya inició sesión, el sistema conoce su identidad. Ella solo indica el motivo de su consulta."
*   *(Acción: Selecciona un motivo en el picklist, escribe "Problema con mi nota" y envíalo).*
*   **Discurso:** "Al enviarlo, su información viaja encriptada y genera un Ticket (Caso) que cae exactamente en la cola de trabajo del departamento correcto."

---

## 🤖 ESCENARIO 3: Soporte en Tiempo Real (Bot y Agente)
*Encuadre: Sigue en la pantalla del portal como Ana.*

**1. Contención con IA (LuminaBot)**
*   *(Acción: Haz clic en el botón flotante de chat en la esquina inferior).*
*   **Discurso:** "Pero, ¿qué pasa si Ana necesita ayuda inmediata en época de exámenes? Lanza el chat, y el primero en responder es LuminaBot, nuestro asistente virtual."
*   *(Acción: Haz clic en una de las opciones del menú del bot, por ejemplo, 'Información de Carreras').*
*   **Discurso:** "El bot está diseñado para resolver las consultas volumétricas más frecuentes en segundos, sin intervención humana."

**2. Derivación Inteligente (Omni-Channel)**
*   *(Acción: En el menú del bot, selecciona 'Hablar con un asesor' o la opción equivalente).*
*   **Discurso:** "Si la consulta es compleja, Ana pide hablar con un agente."
*   *(Acción rápida: Cambia de pestaña a la ventana de Salesforce donde tienes abierta la Service Console. Se escuchará el 'ring' del Omni-Channel. Acepta el chat).*
*   **Discurso:** "En milisegundos, nuestro sistema de enrutamiento mediante Omni-Channel asigna la sesión al agente disponible. Noten la vista que tiene nuestro equipo en la Consola de Servicio: el agente no empieza a ciegas, sino que recibe inmediatamente toda la transcripción previa de lo que la alumna conversó con LuminaBot. Tener este contexto exacto reduce drásticamente el tiempo de atención y asegura una resolución rápida."
*   *(Acción: Escribe "Hola Ana, veo que tienes un problema, te ayudo enseguida" en el chat y envíalo).*
*   *(Acción rápida: Vuelve a la pestaña de incógnito (portal) por un segundo para mostrar cómo Ana recibe el mensaje al instante).*
*   **Discurso:** "Y como vemos, la comunicación es instantánea y bidireccional."

---

## 🏁 EL CIERRE (Final de la Demo)
*Encuadre: Se mantiene la pantalla en la Service Console.*

**Discurso:**
"Este es el ecosistema completo que implementamos. Desde la atracción de prospectos en un portal público, pasando por el autoservicio privado, hasta una arquitectura híbrida de Inteligencia Artificial y agentes humanos operando en una misma consola. Todo integrado de forma segura para escalar las operaciones de Lumina Tech. Muchas gracias."

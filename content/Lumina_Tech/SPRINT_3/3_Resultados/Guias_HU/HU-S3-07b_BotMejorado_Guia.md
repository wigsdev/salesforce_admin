# Guía de Implementación — Bot Mejorado de Einstein
## Lumina Tech University — Nivel Avanzado

---

### ¿Qué es el Bot Mejorado?

El **Bot Mejorado** (Enhanced Bot) es la evolución del Bot Estándar. A diferencia del Bot Estándar que usa diálogos secuenciales y colas de Omni-Channel, el Bot Mejorado usa:

- **Flujos de OmniCanal** para enrutar conversaciones (más flexible)
- **Componentes de mensajería enriquecida** (archivos, carruseles, botones)
- **EinsteinGPT** para responder con IA usando Knowledge Articles
- **Canales avanzados**: WhatsApp, SMS, In-App messaging (además de Web Chat)
- **Topics** (Temas) para organizar intenciones por área temática

---

### Requisitos Previos

Antes de empezar, verifica en **Setup → Einstein Bots → Requisitos previos**:

| Requisito | Cómo verificar |
|---|---|
| ✅ Einstein Bots activado | Setup → Einstein Bots → Interruptor en ON |
| ✅ ChatbotNlp aprovisionado | Se activa automáticamente con Einstein Bots |
| ✅ EinsteinGPT aprovisionado | Setup → Einstein Bots → Requisitos previos |
| ✅ Omni-Channel activado | Setup → Omni-Channel Settings → Enable |
| ⚠️ Canal de Messaging | Setup → Messaging Settings → Activar al menos un canal |

> ⚠️ **Nota importante:** El Bot Mejorado **NO es compatible** con el Legacy Live Chat (Embedded Service clásico). Para probarlo en el portal, necesitas asociarlo a un canal de **Messaging for In-App and Web** o a un canal de WhatsApp/SMS.

---

### Fase 1: Creación del Bot Mejorado

#### Paso 1 — Iniciar el asistente

1. Ve a **Setup → Einstein Bots**.
2. Haz clic en el botón **"Nuevo"** (arriba a la derecha de la lista de bots).
3. En la primera pantalla del asistente, elige el tipo de bot:
   - Selecciona **"Bot mejorado"** *(no Bot estándar)*.
   - Haz clic en **"Siguiente"**.

#### Paso 2 — Configuración básica

4. Completa los campos:
   - **Nombre del bot:** `Lumina Bot Mejorado`
   - **Descripción:** `Asistente virtual avanzado con IA Generativa para Lumina Tech University`
   - **Idioma principal:** `Español`
5. Haz clic en **"Siguiente"**.

#### Paso 3 — Plantilla de inicio

6. Selecciona la plantilla:
   - **"Comenzar desde cero"** → para máximo control sobre los diálogos.
   - O **"Plantilla de servicio al cliente"** → si quieres diálogos pre-construidos de ejemplo.
7. Haz clic en **"Siguiente"**.

#### Paso 4 — Mensaje de bienvenida y menú principal

8. En **"Mensaje de bienvenida"**, escribe:
   ```
   ¡Hola! Soy Lumina Bot, tu asistente virtual inteligente. 
   ¿En qué te puedo ayudar hoy?
   ```
9. En **"Menú principal"**, agrega las opciones (botones):
   - `Información sobre carreras`
   - `Trámites y Reclamos`
   - `Hablar con un agente`
10. Haz clic en **"Siguiente"**.

#### Paso 5 — Canal de mensajería

11. En **"Seleccionar canal"**, el Bot Mejorado te pedirá un canal de Messaging.
    - Si tienes **Messaging for In-App and Web** configurado: Selecciónalo.
    - Si no: Deja en blanco y conéctalo después desde la página de Descripción general del bot.
12. Haz clic en **"Siguiente"**.

#### Paso 6 — Enrutamiento con Flujos de OmniCanal

13. En la pantalla **"Enrutar con flujos"**:
    - Marca el checkbox **"Crear un flujo de OmniCanal entrante para mi bot"** ✅
    - En **"Flujos de OmniCanal saliente"**, selecciona **"Nuevo flujo de OmniCanal saliente"** ← Salesforce lo crea automáticamente.
14. Haz clic en **"Siguiente"**.

#### Paso 7 — Finalizar

15. Revisa el resumen. Salesforce creará automáticamente:
    - ✅ Diálogos personalizados (Bienvenida + Menú)
    - ✅ Diálogos del sistema (Transferir a agente, Finalizar chat, etc.)
    - ✅ Análisis de bot
    - ✅ Flujo de OmniCanal (entrante y saliente)
16. Haz clic en **"Finalizar"**.

---

### Fase 2: Exploración del Bot Builder

Al entrar al Bot Builder del Bot Mejorado, verás el mismo canvas pero con nuevas secciones en la Biblioteca:

#### Nuevos componentes exclusivos del Bot Mejorado:

| Sección | Componente | Función |
|---|---|---|
| **Mensajes** | `Archivo` | Enviar documentos PDF, imágenes al alumno |
| **Mensajes** | `Mensaje` | Texto plano (igual al estándar) |
| **Componentes de mensajería** | `Carrusel` | Mostrar tarjetas deslizables con opciones |
| **Componentes de mensajería** | `Elección` | Botones de selección rápida |
| **Componentes de mensajería** | `Formulario` | Mini-formulario dentro del chat |
| **Acciones** | `Generar respuesta Einstein` | ⭐ IA Generativa con Knowledge Articles |
| **Acciones** | `Resumir transcript` | Resumen automático de la conversación |

---

### Fase 3: Configurar Respuestas con EinsteinGPT (IA Generativa)

Esta es **la diferencia clave** del Bot Mejorado. Permite que el bot responda preguntas complejas automáticamente usando los artículos de Knowledge configurados en HU-S3-05.

#### Prerequisito: Tener artículos de Knowledge publicados

Los artículos de Knowledge deben estar publicados en el canal **"Bot"** para que EinsteinGPT pueda leerlos.

1. Ve a **Setup → Knowledge Settings**.
2. Verifica que el canal **"Bot"** está habilitado en los canales de publicación de artículos.

#### Configurar el componente "Generar respuesta Einstein":

1. En el Bot Builder, crea un nuevo diálogo o abre el diálogo donde quieres agregar IA.
2. Desde la Biblioteca, en la sección **"Acciones"**, arrastra **"Generar respuesta Einstein"** al canvas.
3. En el panel derecho, configura:
   - **Fuente de conocimiento:** `Lumina Tech Knowledge Base` (o el nombre de tu base de Knowledge)
   - **Número máximo de artículos:** `3` *(artículos que consultará para generar la respuesta)*
   - **Guardar respuesta en:** crear variable `respuestaIA` de tipo Text
4. Debajo de este componente, agrega un **Mensaje** que muestre la variable:
   - En el campo de texto del mensaje, inserta la variable `{!respuestaIA}`
5. Haz clic en **Guardar**.

> 💡 **Cómo funciona:** El alumno escribe su pregunta en lenguaje natural (ej. "¿Cuánto duran las clases de Marketing Digital?"). EinsteinGPT busca en los artículos de Knowledge y genera una respuesta coherente en español. El alumno NO necesita hacer clic en botones.

---

### Fase 4: Agregar Componentes de Mensajería Enriquecida

#### 4.1 — Carrusel de Carreras

Ideal para mostrar las 5 carreras de forma visual con tarjetas deslizables.

1. En el diálogo **"Información sobre carreras"**, arrastra **"Carrusel"** al canvas.
2. En el panel derecho, configura cada tarjeta:
   - **Tarjeta 1:**
     - Título: `Ingeniería de Software`
     - Descripción: `4 años | Híbrida | Desarrollador, Arquitecto`
     - Botón: `Ver más` → URL: `https://lumina-tech-university-prod-dev-ed.trailblaze.my.site.com/s/carreras/ingenieria_de_software`
   - **Tarjeta 2:** Marketing Digital (misma estructura)
   - *(Repetir para las 5 carreras)*
3. Haz clic en **Guardar**.

> ⚠️ Los Carruseles solo se renderizarán correctamente en canales de **Messaging for In-App and Web**. En Live Chat Legacy aparecerán como texto plano.

#### 4.2 — Envío de Archivo (PDF del Reglamento)

1. En cualquier diálogo, arrastra el componente **"Archivo"** al canvas.
2. Configura:
   - **URL del archivo:** URL pública del PDF almacenado en Salesforce Files o CDN externo.
   - **Nombre del archivo:** `Reglamento_Lumina_Tech.pdf`
3. El alumno verá el PDF directamente en el chat para descargarlo.

---

### Fase 5: Conectar a un Canal de Messaging

Para ver el bot en acción con todas las capacidades, debes conectarlo a un canal de Messaging.

#### Opción A — Messaging for In-App and Web (recomendado para portal)

1. Ve a **Setup → Messaging Settings**.
2. Haz clic en **"Nuevo canal"** → selecciona **"Messaging for In-App and Web"**.
3. Nómbralo: `Lumina Tech Messaging`
4. Copia el **código de snippet** que genera Salesforce.
5. Ve a **Experience Builder** del portal → busca el componente de chat → reemplaza el Embedded Service clásico por el nuevo widget de Messaging.
6. Vuelve al Bot Builder → **Descripción general del bot** → sección **Canales** → **"+ Agregar"** → selecciona `Lumina Tech Messaging`.
7. Haz clic en **Activar** el bot.

#### Opción B — WhatsApp Business (requiere Meta Business Account)

1. Ve a **Setup → Messaging Settings → Nuevo canal → WhatsApp**.
2. Sigue el proceso de vinculación con Meta Business Manager.
3. Conecta el número de WhatsApp al bot desde la Descripción general.

---

### Fase 6: Activación y Prueba

1. En el Bot Builder, haz clic en **"Activar"** (arriba a la derecha).
2. Abre el canal configurado (portal con nuevo widget, o WhatsApp).
3. Verifica el flujo completo:
   - ¿El bot saluda con el mensaje de bienvenida?
   - ¿Los botones del menú principal funcionan?
   - ¿EinsteinGPT responde preguntas en lenguaje natural desde Knowledge?
   - ¿Los carruseles de carreras se ven correctamente?
   - ¿La transferencia al agente funciona vía Omni-Channel Flow?

---

### ✅ Checklist de QA — Bot Mejorado

| # | Verificación | Resultado |
|---|---|---|
| 1 | El bot se activa sin errores de validación | ☐ |
| 2 | Los flujos de OmniCanal (entrante y saliente) están publicados en Flow Builder | ☐ |
| 3 | El bot saluda correctamente en el canal de Messaging | ☐ |
| 4 | EinsteinGPT responde usando artículos de Knowledge publicados | ☐ |
| 5 | El carrusel de carreras se visualiza en el canal correcto | ☐ |
| 6 | La transferencia a agente funciona via Omni-Channel Flow | ☐ |
| 7 | El agente recibe la sesión en la Service Console | ☐ |

---

### 📌 Diferencias clave vs Bot Estándar — Resumen

| Aspecto | Bot Estándar | Bot Mejorado |
|---|---|---|
| Routing | Colas (Queue) | Flujos de OmniCanal |
| Canal | Legacy Live Chat | Messaging for In-App, WhatsApp, SMS |
| IA Generativa | ❌ | ✅ EinsteinGPT + Knowledge |
| Mensajería enriquecida | Texto + botones simples | Carruseles, archivos, formularios |
| Configuración de reglas | Bloques de Regla manual | Topics + intenciones automáticas |
| Futuro de la plataforma | Legacy (sin nuevas features) | ✅ El camino a Agentforce |

---

### ⚠️ Errores frecuentes

| Error | Causa | Solución |
|---|---|---|
| Bot no aparece en el canal | Bot no activado o canal no vinculado | Activar + vincular en Descripción general |
| Flujo OmniCanal no encontrado | El Flow no está publicado | Flow Builder → Activar el flujo |
| EinsteinGPT no responde | Artículos de Knowledge no publicados en canal "Bot" | Knowledge Settings → Habilitar canal Bot |
| Carrusel no se muestra | Canal no soporta mensajería enriquecida | Usar canal Messaging for In-App and Web |

------

### 🚀 Referencia Futura — Agentforce (Próxima Evolución)

> ⚠️ **Esta sección es solo de referencia.** No aplica al Sprint 3 actual. Se documenta para cuando Lumina Tech escale hacia IA autónoma.

**Agentforce** es el nivel siguiente al Bot Mejorado. En lugar de diálogos predefinidos, un **Agente de Servicio Agentforce** razona autónomamente y decide qué acciones tomar basándose en el contexto de la conversación.

#### Diferencias con el Bot Mejorado:

| Aspecto | Bot Mejorado | Agentforce |
|---|---|---|
| Lógica | Diálogos/Topics pre-configurados | Razonamiento autónomo con LLM |
| Memoria | Por sesión | Persistente entre conversaciones |
| Acciones | Limitadas a componentes configurados | Puede ejecutar Flows, Apex, APIs externas |
| Personalización | Por variable de sesión | Data Cloud + CRM data en tiempo real |
| Licencia | Einstein Bots incluido | Licencia Agentforce (~$2/conversación) |

#### Requisitos para implementar Agentforce:

1. **Licencia:** Edición Enterprise o Unlimited + Add-on de **Agentforce Service Agent**.
2. **Data Cloud:** Conectado con datos del alumno (historial de matrículas, casos abiertos).
3. **Topics y Actions:** Definir qué temas puede manejar el agente y qué acciones puede ejecutar.
4. **Ruta de migración:** Setup → Einstein Bots → *"Crear agente a partir de un bot"* → seleccionar el Bot Mejorado como base.

#### Cuándo considerar la migración:

- Cuando el volumen de conversaciones supere las capacidades del bot basado en diálogos.
- Cuando se necesite personalización profunda por alumno (basada en su historial académico).
- Cuando Lumina Tech quiera resolver casos complejos sin escalar a agentes humanos.
- Cuando se habilite la integración con Data Cloud para segmentación de alumnos.

> 📌 **Referencia oficial:** [Salesforce Agentforce Documentation](https://help.salesforce.com/s/articleView?id=sf.agentforce.htm)

---

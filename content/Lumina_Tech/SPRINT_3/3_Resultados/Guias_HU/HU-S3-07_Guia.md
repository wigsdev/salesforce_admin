# Guía de Implementación Técnica
# Historia de Usuario: HU-S3-07
## Implementación de Einstein Bot (Lumina Bot)

---

### Resumen
Esta guía documenta la configuración paso a paso del asistente conversacional **Lumina Bot** en el portal de Experience Cloud. El bot actúa como primer punto de contacto: presenta un menú de opciones (carreras, trámites, agente humano), responde consultas de información académica de forma automática y transfiere a Omni-Channel cuando el alumno requiere atención personalizada.

**Arquitectura resultante:**
```
Alumno abre el chat (botón "Chat con un experto")
              ↓
        [Lumina Bot]
    ¿En qué te ayudo hoy?
   /          |           \
Carreras   Trámites    Hablar con agente
   ↓          ↓               ↓
Pregunta  Mensaje +       Transferir a
submenú   link form.     Omni-Channel
   ↓
Mensaje con info
+ link carrera +
[Ver otra / Menú]
```

---

### Fase 1: Creación del Bot — Asistente de Configuración

El asistente de Einstein Bots guía la creación en 6 pasos encadenados.

1. Ve a **Setup → Einstein Bots**. Acepta los términos y activa el interruptor maestro.
2. Haz clic en **Nuevo Bot**.
3. **Paso 1 — Tipo de Bot:** Selecciona **Bot estándar** *(compatible con el Chat Heredado/Legacy configurado en HU-S3-06)*. ⚠️ No seleccionar "Bot mejorado" — usa una arquitectura diferente.
4. **Paso 2 — Plantilla:** Selecciona **Comenzar desde cero** *(entrega solo los 5 diálogos del sistema sin ruido extra)*.
5. **Paso 3 — Personalización:**
   - **Nombre del Bot:** `Lumina Bot` *(visible para el alumno en la ventana del chat)*.
   - **Idioma principal:** `Español`.
6. **Paso 4 — Mensaje de bienvenida y Menú principal:**
   - **Mensaje de bienvenida:** `¡Hola! Soy Lumina Bot, tu asistente virtual del Campus. ¿En qué te puedo ayudar hoy?`
   - **Elemento de menú 1:** `Información sobre carreras`
   - **Elemento de menú 2:** `Trámites y Reclamos`
   - **Elemento de menú 3:** `Hablar con un agente`
7. **Paso 5 — Vincular implementación:** En el desplegable **"Implementación de servicios integrados"**, selecciona **`Agentes de chat para soporte web`** *(el Embedded Service Deployment creado en HU-S3-06)*. ⚠️ Esto reemplaza al humano como primer contacto del botón web.
8. **Paso 6 — Finalizar:** Haz clic en **Continuar**. Salesforce crea automáticamente: diálogos personalizados, diálogos del sistema (transferencia, finalizar chat), análisis de bot y el vínculo al canal.

---

### Fase 2: Configuración del Diálogo "Información sobre carreras"

Este diálogo implementa la lógica de asesor académico: pregunta la carrera de interés y muestra información + enlace.

#### 2.1 — Crear la Pregunta de Selección de Carrera

1. En el panel izquierdo del Bot Builder, haz clic en **"Información sobre carreras"**.
2. En la **Biblioteca de componentes de diálogos** (pie del panel izquierdo), arrastra el componente **"Pregunta → Estático"** al canvas.
3. En el panel derecho, configura:
   - **Pregunta:** `¿Sobre cuál carrera deseas información?`
   - **Tipo de elección:** `Estática`
   - **Mostrar opciones como:** `Botones`
4. Haz clic en **"Agregar opción"** 5 veces y escribe:
   - `Ingeniería de Software`
   - `Marketing Digital`
   - `Ciencia de Datos`
   - `Ciberseguridad y Redes`
   - `Otra carrera`
5. **Almacenamiento de respuesta:**
   - **Nombre de entidad:** `[System] Texto (Texto)`
   - **Guardar respuesta en una variable:** Crear nueva variable → Nombre: `carreraSeleccionada` | Tipo: `Text`
   - **Si la variable ya contiene un valor:** Seleccionar **"Formular pregunta y sobrescribir el valor"** ⚠️ *(ver nota crítica abajo)*

> ⚠️ **Error crítico frecuente — Ciclo infinito:** Si se deja la opción por defecto "Omitir pregunta y utilizar valor existente", al usar el botón "Ver otra carrera" el bot regresa al diálogo pero **salta la pregunta** usando el valor anterior, generando un ciclo infinito que termina mostrando "No hay agentes disponibles". Siempre usar **"Formular pregunta y sobrescribir el valor"** en esta pregunta.

#### 2.2 — Crear los Diálogos de Info por Carrera

Usando el **"+"** del panel izquierdo, crear 5 diálogos nuevos (uno por carrera) y en cada uno:
1. Agregar desde la Biblioteca el componente **"Mensaje"**.
2. Pegar el texto correspondiente *(ver tabla abajo — versión compacta por límite de caracteres)*:

| Diálogo | Texto del mensaje |
|---|---|
| `Info_Software` | `💻 Ingeniería de Software` ↵ `Duración: 4 años \| Modalidad: Híbrida` ↵ `Perfil: Desarrollador, Arquitecto, Tech Lead` ↵ `🔗 Ver más: .../carreras/ingenieria_de_software` |
| `Info_Marketing` | `📊 Marketing Digital` ↵ `Duración: 3 años \| Modalidad: Virtual` ↵ `Perfil: Community Manager, SEO Specialist` ↵ `🔗 Ver más: .../carreras/marketing_digital` |
| `Info_Datos` | `🔬 Ciencia de Datos` ↵ `Duración: 4 años \| Modalidad: Híbrida` ↵ `Perfil: Data Analyst, Data Scientist` ↵ `🔗 Ver más: .../carreras/ciencia_de_datos` |
| `Info_Ciberseguridad` | `🛡️ Ciberseguridad y Redes` ↵ `Duración: 4 años \| Modalidad: Presencial` ↵ `Perfil: Ethical Hacker, Security Analyst` ↵ `🔗 Ver más: .../carreras/ciberseguridad_y_redes` |
| `Otra_Carrera` | `🎓 Catálogo de carreras:` ↵ `🔗 .../carreras` ↵ `¿Necesitas asesoría? Escribe: Hablar con un agente` |

> **URL Base:** `https://lumina-tech-university-prod-dev-ed.trailblaze.my.site.com/s/`

#### 2.3 — Agregar Navegación de Regreso al Menú (UX)

Dentro de **cada diálogo de carrera**, después del "Mensaje", agregar para permitir que el alumno navegue sin cerrar el chat:

1. Arrastra una **"Pregunta → Estático"** con botones:
   - `Ver otra carrera`
   - `Volver al menú principal`
2. **Almacenamiento de respuesta:** crear variable `accionMenu` de tipo `Text` *(requerido por el sistema, no se usa en reglas)*.
3. **Si la variable ya contiene un valor:** Seleccionar **"Formular pregunta y sobrescribir el valor"** ⚠️ *(misma razón que `carreraSeleccionada` — evitar el ciclo)*.
3. Agregar 2 bloques **"Redirigir a un diálogo"** de la Biblioteca (sección Reglas):
   - **Regla 1:** Si `accionMenu` = `Ver otra carrera` → Redirigir a `Información sobre carreras`
   - **Regla 2:** Si `accionMenu` = `Volver al menú principal` → Redirigir a `Menú principal`

#### 2.4 — Agregar las 5 Reglas de Enrutamiento por Carrera

De regreso en el diálogo **"Información sobre carreras"**, después de la pregunta, agregar **5 bloques de Reglas** (uno por carrera):

| Bloque | Condición | Acción |
|---|---|---|
| Regla 1 | `carreraSeleccionada = Ingeniería de Software` | Redirigir a `Info_Software` |
| Regla 2 | `carreraSeleccionada = Marketing Digital` | Redirigir a `Info_Marketing` |
| Regla 3 | `carreraSeleccionada = Ciencia de Datos` | Redirigir a `Info_Datos` |
| Regla 4 | `carreraSeleccionada = Ciberseguridad y Redes` | Redirigir a `Info_Ciberseguridad` |
| Regla 5 | `carreraSeleccionada = Otra carrera` | Redirigir a `Otra_Carrera` |

---

### Fase 3: Configuración del Diálogo "Trámites y Reclamos"

1. Haz clic en el diálogo **"Trámites y Reclamos"** en el panel izquierdo.
2. Arrastra un componente **"Mensaje"** al canvas con el siguiente texto:
```
Para gestionar un trámite o reclamo, completa nuestro formulario en línea:

📋 https://lumina-tech-university-prod-dev-ed.trailblaze.my.site.com/s/tramites
```
3. Debajo del Mensaje, arrastra una **"Pregunta → Estático"** con:
   - **Texto:** `¿Necesitas ayuda adicional?`
   - **Botones:** `Hablar con un agente` | `Volver al menú principal`
   - **Variable:** crear `accionTramite` de tipo `Text`
   - **"Si la variable ya contiene un valor":** `Formular pregunta y sobrescribir el valor` ⚠️
4. Agrega **2 bloques de Reglas**:
   - `accionTramite = Hablar con un agente` → Redirigir a `Hablar con un agente`
   - `accionTramite = Volver al menú principal` → Redirigir a `Menú principal`
5. **Siguiente paso:** `Esperar entrada del cliente`
6. Haz clic en **Guardar**.

---

### Fase 4: Configuración del Diálogo "Hablar con un agente"

1. Haz clic en el diálogo **"Hablar con un agente"** en el panel izquierdo.
2. ⚠️ Si existe un bloque "Reglas" con errores (`undefined`), eliminarlo con el ícono 🗑️.
3. Haz clic en el bloque **"Siguiente paso"** del canvas.
4. En el panel derecho, selecciona la opción **"Transferir a un agente"**.
   - *El sistema ya cuenta con el diálogo nativo "Transferir a un agente" que gestiona la lógica de Omni-Channel.*
5. Haz clic en **Guardar**.

---

### Fase 5: Activación y Prueba End-to-End

1. Haz clic en el botón **"Activar"** arriba a la derecha del Bot Builder.
2. Abre la **Service Console** y ponte en estado **Available** en Omni-Channel.
3. Abre el portal Experience Cloud en ventana **Incógnito**.
4. Haz clic en el botón **"Chat con un experto"** *(el nombre del botón no cambia, pero el comportamiento sí)*.
5. Verificar que aparece el saludo de **Lumina Bot** con los 3 botones del menú principal.
6. Navegar por las opciones y verificar el flujo completo.

---

### ✅ Checklist de QA Final

| # | Verificación | Resultado |
|---|---|---|
| 1 | El chat abre con el saludo de Lumina Bot (no va directo al agente) | ☐ |
| 2 | Los 3 botones del menú principal son visibles y clicables | ☐ |
| 3 | "Información sobre carreras" muestra el submenú de 5 carreras | ☐ |
| 4 | Al elegir una carrera, aparece el mensaje con la descripción y el link | ☐ |
| 5 | Los botones "Ver otra carrera" y "Volver al menú principal" funcionan sin cerrar el chat | ☐ |
| 6 | "Trámites y Reclamos" muestra el mensaje con el link al formulario | ☐ |
| 7 | "Hablar con un agente" transfiere correctamente a Omni-Channel | ☐ |
| 8 | El ping de transferencia suena en la Service Console del agente | ☐ |

---

### Fase 1: Creación del Bot Base
El Bot necesita ser instanciado y conectado a la cola creada en HU-S3-06.
1. Habilita los términos en **Einstein Bots** (Setup) y enciende el interruptor maestro.
2. Haz clic en **Nuevo** (New Bot).
3. Selecciona **Empezar desde cero** (Start from Scratch) o elige la plantilla estándar.
4. **Nombre del Bot:** `LuminaBot`.
5. **Idioma Principal:** Selecciona `Español`.
6. En la pantalla donde te pregunte *"What should your bot do when it can't figure out what the customer wants?"* (¿Qué hacer en caso de error o escalamiento?), busca y selecciona la **Cola (Queue)** que configuramos para Chat (Ej. `Web Support` o `Soporte Chat Lumina`).

### Fase 2: Configuración de Diálogos (Menú Principal)
Aquí dotaremos de "voz" al bot y opciones clicables.
1. Entra al editor del Bot (Bot Builder).
2. Selecciona el diálogo **Welcome** o Mensaje de Bienvenida. Modifica el texto: *"¡Hola! Soy LuminaBot, tu asistente virtual. ¿En qué te puedo ayudar hoy?"*.
3. Ve a la pestaña **Main Menu** (Diálogos).
4. Agrega los nodos necesarios para crear **Opciones de Menú** (Questions / Rules):
   - Opción 1: `🎓 Admisiones y Carreras`
   - Opción 2: `📄 Trámites y Certificados`
   - Opción 3: `👤 Hablar con un Humano`
5. Configura la acción derivada de **"Hablar con un Humano"**. Haz que lance la acción del sistema (System Action) llamada **Transfer to Agent**, apuntando directamente a la ruta generada en la Fase 1.

### Fase 3: Conexión al Canal Web (Channel Integration)
La "toma y daca" entre el humano del Sprint pasado y la IA.
1. Sal del Bot Builder haciendo clic en la rueda dentada o yendo hacia atrás.
2. En la página de configuración del bot, ve a la sección **Overview** (Descripción general).
3. Desplázate hacia abajo hasta la sección **Channels** (Conexiones de Canal).
4. Haz clic en **+ Add** (Añadir).
5. Selecciona el canal preexistente **Chat (Embedded Service)**. En la lista desplegable, selecciona el nombre del despliegue que incrustaste en Experience Cloud (Ej. `Web_Support_Deployment`).
6. Este paso sobrescribe el botón web: Ahora los clics irán al bot primero, y luego al agente.

### Fase 4: Activación y Pruebas Reales
1. Activa el bot haciendo clic en el botón superior derecho **Activate**. *(El bot debe compilar su modelo natural, lo cual tomará un instante).*
2. Abre tu sesión de administrador y ponte en estado **Available** en la herramienta inferior **Omni-Channel**.
3. Abre una pestaña en Incógnito de la web Lumina Tech.
4. Abre la ventana de chat y verifica:
   - ¿Aparece el saludo inicial de LuminaBot?
   - ¿Aparecen los botones del menú inicial?
5. Haz clic en **"Hablar con un humano"**.
6. Observa tu Service Console: El chat debería repicar indicando que LuminaBot acaba de enviar una transferencia a la cola.

---

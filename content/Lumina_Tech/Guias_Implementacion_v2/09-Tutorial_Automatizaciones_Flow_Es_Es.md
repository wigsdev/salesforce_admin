# ⚡ Guía Técnica 09: Automatización Core con Flows (PASO A PASO)

**Fase**: Sprint 2 - Análisis de Tickets y Automatizaciones
**Rol Responsable**: ⚙️ **Salesforce Architect / Administrator**
**Público Objetivo**: Administradores Salesforce (Manual de Configuración UI Exacta - Winter/Spring '24)

---

## 🎯 Objetivo General
Implementar los tres flujos requeridos por Rectorado (Historias de Usuario 202, 203 y 204). Este documento certifica las "Best Practices" del ecosistema Salesforce, utilizando elementos nativos del Flow Builder moderno sin recurrir a alertas heredadas o asunciones de UI.

---

## 📧 1. Correo de Bienvenida Automático (HU-202)
Utilizaremos un **Record-Triggered Flow** con la Core Action **Send Email** para mayor profesionalismo, haciendo una búsqueda previa de la plantilla para no quemar ("hardcodear") IDs en el sistema.

### Paso 0: Crear el Campo de Control (Pre-requisito Anti-Spam)
Necesitamos un campo en `Contact` para diferenciar altas manuadas vs. cargas de Data Loader.

1. Ve a **Setup** (ícono de engranaje) > **Object Manager** > **Contact** > **Fields & Relationships**.
2. Haz clic en **New**.
3. **Step 1:** Selecciona **Picklist** y haz clic en **Next**.
4. **Step 2:**
    *   **Field Label:** `Fuente de Origen`
    *   **Values:** Haz clic en *Enter values, with each value separated by a new line*.
    *   Escribe en la caja:
        `Ventanilla`
        `Migración Histórica`
    *   **¡CRÍTICO!:** Marca la casilla `Use first value as default value`. (Esto evitará el uso de recuadros de fórmulas).
    *   **Field Name:** Haz clic para autocompletar (`Fuente_de_Origen`). Clic en **Next**.
5. **Step 3 (FLS) & Step 4 (Layout):** Deja los valores por defecto. Clic en **Save**.

### Paso 1: Crear el Lightning Email Template
1. Abre el **App Launcher** (9 puntos izquierda) y busca `Email Templates`.
2. Haz clic en **New Email Template**.
    *   **Email Template Name:** `Lumina Bienvenida Estudiante`. *(Guarda en un bloc de notas el DeveloperName que se genere, suele ser `Lumina_Bienvenida_Estudiante`).*
    *   **Related Entity Type:** Busca y selecciona `Contact`.
    *   **Folder:** `Public Email Templates`.
    *   **Subject:** `¡Bienvenido a Lumina Tech!`
3. En **HTML Value**, redacta el cuerpo con **diseño institucional (Branding)**:
    *   Incluye el logo de Lumina Tech (insertar imagen desde el botón de imagen del editor).
    *   Aplica los colores corporativos de Lumina Tech en los encabezados.
    *   Usa el ícono `{...}` de merge fields para buscar **Contact** > **First Name** e insertarlo (`{{{Contact.FirstName}}}`) para personalizar el saludo.
    *   *(Nota arquitectónica: Bajo ninguna circunstancia usar Classic Email Templates. Solo Lightning Email Templates permiten HTML moderno y Merge Fields dinámicos).*
4. Clic en **Save**.

### Paso 2: Crear el Record-Triggered Flow
1. Ve a **Setup > Flows** y haz clic en **New Flow**.
2. Elige **Record-Triggered Flow** y haz clic en **Create**.
3. **Configure Start:**
    *   **Object:** Selecciona `Contact`.
    *   **Configure Trigger:** Selecciona `A record is created`.
    *   **Condition Requirements:** `All Conditions Are Met (AND)`.
    *   Filtro 1: Field `Email` | Operator `Is Null` | Value `{!$GlobalConstant.False}`
    *   Filtro 2: Haz clic en `+ Add Condition`. Field `RecordType.DeveloperName` | Operator `Equals` | Value `Alumno`
    *   Filtro 3: Haz clic en `+ Add Condition`. Field `Fuente_de_Origen__c` | Operator `Equals` | Value `Ventanilla`
    *   **Optimize the Flow for:** Selecciona `Actions and Related Records`. Clic en **Done**.

### Paso 3: Obtener el ID de la Plantilla Dinámicamente
*No usaremos IDs fijos por si migramos de Sandbox a Producción.*
1. En el lienzo, haz clic en el símbolo **(+)** debajo de Start y elige **Get Records**.
2. **Label:** `Obtener Plantilla Correo`.
3. **Object:** Escribe y selecciona `EmailTemplate`.
4. **Condition Requirements:** `All Conditions Are Met (AND)`.
    *   Field `DeveloperName` | Operator `Equals` | Value `Lumina_Bienvenida_Estudiante`.
5. **How Many Records to Store:** `Only the first record`. Clic en **Done**.

### Paso 4: Núcleo de la Acción (Send Email Core Action)
1. Haz clic en el **(+)** debajo de Get Records y selecciona **Action**.
2. En la barra superior, busca y selecciona **Send Email** (Asegúrate de no elegir Send Email Alert).
3. **Configuración General:**
    *   **Label:** `Enviar Correo de Bienvenida` (API Name se autogenera).
4. **Abrir panel de Email Content:**
    *   Localiza el Slider (Interruptor) **Use Email Template** y muévelo hacia la derecha (o cambia su valor a "Include").
    *   Aparecerá el parámetro *Email Template ID*. Configúralo mapeando la búsqueda anterior: `{!Obtener_Plantilla_Correo.Id}`.
5. **Abrir panel de Recipient Details:**
    *   Localiza **Recipient ID** y actívalo. (OBLIGATORIO cuando usas Templates).
    *   Mapea al contacto que desencadenó el flow: `{!$Record.Id}`.
6. (Recomendado) Asegúrate de que **Log Email on Send** esté en `{!$GlobalConstant.True}` para dejar registro en el alumno.
7. Haz clic en **Done**. Clic en **Save** (Nombre: `Lumina Correo Bienvenida Ventanilla`) y **Activate**.

---

## 🖥️ 2. Asistente UI para Carga Rápida en Recepción (HU-203)
Flujo guiado para consolidar datos en una sola pantalla, con manejo de excepciones nativo mediante Fault Paths.

### Paso 1: Configurar el Screen Flow y sus Componentes
1. Ve a **Setup** (engranaje) > busca **Flows** en Quick Find > clic en **New Flow**.
2. Selecciona la tarjeta **Screen Flow** (tiene el ícono de pantalla). Clic en **Create**. Se abrirá el lienzo del Flow Builder.
3. En el lienzo, haz clic en el ícono **(+)** que aparece debajo del nodo de inicio azul y selecciona **Screen**. Se abrirá el editor de pantalla.
4. En el **panel derecho** (Properties), en el campo **Label**, escribe: `Carga Rápida de Alumno`. (El API Name se autogenera).
5. En el **panel izquierdo** verás la pestaña **Components**. Aquí están los elementos arrastrables. Localiza y arrastra al área central estos componentes **en este orden exacto**:

    **Componente 1 - Name (Nombre y Apellido)**
    *   Busca `Name` en el buscador de Components y arrástralo al lienzo central.
    *   En el **panel derecho**: `Label` = `Nombre`. En `First Name` verifica que diga `Nombre`. En `Last Name` escribe `Apellido`. Marca `Required`. El **API Name** debe ser `NombreAlumno`.
    *   *(El campo `Fields To Display` debe mostrar `firstName,lastName` para que se vean ambos subcampos)*.

    **Componente 2 - Radio Buttons (Tipo de Documento)**
    *   Busca `Radio` en el buscador de Components y arrástralo **debajo** del componente Name.
    *   En el **panel derecho**: **Label** = `Tipo de Documento`. **API Name** = `TipoDocumento`. Marca la casilla `Require`.
    *   En la sección **Configure Choices**, haz clic en el campo `Choice` (que dice *Select or create a choice resource*) > selecciona **New Resource**.
    *   En el modal **New Choice Resource**, en el dropdown **Resource Type** selecciona **`Picklist Choice Set`** y clic en **Done**.
    *   Se abrirá el formulario del Picklist Choice Set:
        -   **Label:** `Tipo Documento Choices`
        -   **API Name:** Se autogenera como `Tipo_Documento_Choices`.
        -   **Object:** Selecciona `Persona` (Contact renombrado en este entorno).
        -   **Picklist Field:** Selecciona `Tipo de Documento` (`Tipo_de_Documento__c`).
        -   Clic en **Done**. Salesforce cargará automáticamente los 3 valores: DNI, Carnet de Extranjería, Pasaporte.
    *   El campo `Choice` del panel derecho ahora mostrará `Tipo_Documento_Choices`. ✅

    **Componente 3 - Text (Número de Documento)**
    *   Arrastra un **Text**. Panel derecho: `Label` = `Número de Documento`. Marca `Required`.

    **Componente 4 - Email (Correo Electrónico)**
    *   Arrastra un **Email**. Panel derecho: `Label` = `Correo Electrónico`. **API Name** = `InputCorreo`. Marca `Required`.

    **Componente 5 - Teléfono**
    *   Arrastra un **Phone**. Panel derecho: `Label` = `Teléfono`. **API Name** = `InputTelefono`. Marca `Required`.

6. Sin cerrar el editor de pantalla, busca abajo a la derecha el enlace **Configure Footer** y haz clic en él:
    *   *Pause Button* > cambia a `Hide Pause` (Ocultar pausa).
    *   *Previous Button* > cambia a `Hide Previous` (Ocultar anterior). *(El operador de recepción no puede ir atrás en una carga de mostrador)*.
    *   *Next or Finish Button Label* > selecciona `Use a custom label` y escribe: `Guardar Alumno`.
7. Clic en **Done** (esquina inferior derecha del editor de pantalla).

### Paso 2: Consultar RecordType (Best Practice)
> [!NOTE]
> **Lumina Tech no tiene Record Types configurados en Contact.** Este paso es aplicable solo en organizaciones que usen Record Types para diferenciar Alumnos de Profesores dentro del mismo objeto. En este entorno, **omite este paso** y pasa directamente al Paso 3.
> Si en el futuro se configuran Record Types, se deberá añadir un nodo **Get Records** sobre el objeto `RecordType` filtrando por `DeveloperName = Alumno` y `SobjectType = Contact`, y mapear el resultado en el campo `RecordTypeId` del Create Records.

### Paso 3: Función de Creación (Create Records)
> [!NOTE]
> En este entorno, el objeto **Contact fue renombrado a `Persona`**. Al seleccionar el Object en el nodo Create Records, busca `Persona` (no `Contact`). Salesforce internamente lo reconocerá como el mismo objeto estándar.

1. Haz clic en el **(+)** debajo del nodo Screen y selecciona **Create Records**.
2. Panel de configuración:
    *   **Label:** Escribe `Guardar Alumno Base Datos`.
    *   **How Many Records to Create:** Selecciona `One`.
    *   **How to Set the Record Fields:** Selecciona `Use separate resources, and literal values`.
    *   **Object:** Escribe `Persona` y selecciónalo.
3. Ahora aparecerá la sección **Set Field Values for the Persona**. Para cada fila, haz clic en **+ Add Field** y mapea:
    *   Campo `First Name` | Value: pestaña **Screen Components** > `NombreAlumno > First Name`.
    *   Campo `Last Name` | Value: pestaña **Screen Components** > `NombreAlumno > Last Name`.
    *   Campo `Tipo de Documento` | Value: pestaña **Screen Components** > `{!TipoDocumento}` *(el Radio Button que seleccionó el operador)*.
    *   Campo `Numero de Documento` | Value: pestaña **Screen Components** > `Número de Documento`.
    *   Campo `Email` | Value: pestaña **Screen Components** > `InputCorreo` > selecciona `{!InputCorreo.value}`. *(Crucial: siempre seleccionar el sub-atributo `.value`, no el componente en sí)*.
    *   Campo `Phone` (Teléfono / Teléfono del Trabajo) | Value: pestaña **Screen Components** > `InputTelefono` > selecciona `{!InputTelefono.value}`. *(Nota: Salesforce a veces etiqueta este campo nativo como "Teléfono del trabajo" o "Business Phone", búscalo así si no sale como "Phone").*
    *   Campo `Fuente de Origen` | selecciona el tipo `String` y escribe el literal `Ventanilla`. *(Este valor detona automáticamente el correo de bienvenida de HU-202)*.
4. Clic en **Done**.

### Paso 4: Pantalla de Éxito (Success Screen)
> [!TIP]
> Confirmar al operador de recepción que el registro se creó exitosamente evita que intente cargarlo de nuevo por miedo a que el sistema no haya guardado la información.

1. Haz clic en el **(+)** debajo del nodo `Guardar Alumno Base Datos` (sobre la línea azul principal, **NO** sobre la línea roja punteada).
2. Selecciona **Screen** (Pantalla).
3. Panel de configuración:
    *   **Label:** Escribe `Pantalla de Exito`.
    *   **API Name:** `Pantalla_de_Exito`.
    *   Arrastra un componente **Display Text** al centro del área visual.
    *   **API Name:** `MensajeExito`.
    *   En la caja de texto central, escribe y dalea formato verde a voluntad: *"✅ ¡El Alumno se ha registrado exitosamente en el sistema!"*
4. En la configuración de botones (**Configure Footer**):
    *   Oculta los botones *Pause* y *Previous*.
    *   Cambia la etiqueta del botón *Next/Finish* a `Finalizar`.
5. Clic en **Done**.

### Paso 5: Enrutamiento de Fallo (Fault Path)
*¿Para qué sirve? Si el alumno ya existe en BD (DNI duplicado), Salesforce bloqueará el DML y el Flow se romperá con pantalla roja. El Fault Path intercepta ese error y lo convierte en un mensaje amigable.*
1. En el lienzo, haz clic **una sola vez** sobre el nodo `Guardar Alumno Base Datos`. Aparecerá un pequeño menú contextual flotante encima del nodo.
2. En ese menú, selecciona **Add Fault Path**. Verás que del nodo nace una **línea roja punteada** hacia la derecha del lienzo.
3. Al final de esa línea roja, haz clic en el **(+)** y selecciona **Screen**.
4. En el editor de la pantalla de error:
    *   **Label:** Escribe `Pantalla de Error`.
    *   En **Components** (izquierda), arrastra un **Display Text** al centro.
    *   En el panel derecho, **API Name:** `AvisoErrorDNI`.
    *   En la caja de texto del centro, escribe:
        *"⚠️ Error al Guardar: El sistema canceló la operación. Si el Número de Documento ya existe, no puede duplicar al Alumno. Por favor verifique en Bedelía. Detalle: `{!$Flow.FaultMessage}`"*
    *   En **Configure Footer**: oculta Pause y Previous. El botón Next puedes llamarlo `Reintentar`.
5. Clic en **Done**.
6. Clic en **Save** (botón gris superior). En el popup:
    *   **Flow Label:** `Lumina Asistente Carga Recepcion`.
    *   Clic en **Save**.
7. Clic en el botón azul **Activate** para activarlo.
8. **Publicarlo en la App:** Ve a **Setup > Lightning App Builder**, abre la Home Page de la app `Gestión Académica Lumina`, arrastra el componente **Flow** al área deseada, selecciona este flow en el dropdown y guarda la página.

---

## 🕒 3. Auditoría Semanal de Actas (HU-204)
Flujo automatizado desatendido con barrera Anti-Spam (Get Records en Loop) para prevenir generación de Tareas masivas erróneas hacia los Docentes.

### Paso 1: Configurar el Cronómetro (Schedule-Triggered Flow)
1. En **Setup > Flows** > **New Flow**. Elige **Schedule-Triggered Flow**.
2. Ve al panel de Start y haz clic en **Set Schedule**:
    *   **Start Date:** Fecha de hoy.
    *   **Start Time:** `17:00` *(Este es el horario oficial solicitado por Rectorado en la HU-204)*.
    *   **Frequency:** `Weekly`. Clic en **Done**.

    > [!TIP]
    > **Recomendación Consultiva (Performance):** Considera proponer al cliente mover la ejecución a las `23:00 hs`. Un escaneo masivo (Batch) durante el horario administrativo pico puede ralentizar el entorno Salesforce y colisionar con la última hora de carga de los docentes. Esta propuesta debe quedar documentada y aprobada por la Rectora antes de modificarse.

3. **Choose Object:** Déjalo EN BLANCO. (Evitar seleccionar objetos aquí permite obtener registros complejos más adelante con cross-object fields).

### Paso 2: Obtener Actas Retrasadas
1. Clic en **(+)** > **Get Records**.
2. **Label:** `Extraer Inscripciones Sin Nota`. Objeto: `Inscripcion__c`.
3. **Condiciones:**
    *   Filtro 1: `Materia__r.Fecha_de_Cierre__c` | Operator: `Less Than` | Value: `{!$Flow.CurrentDate}`
    *   Filtro 2: `Nota_Final__c` | Operator: `Is Null` | Value: `{!$GlobalConstant.True}`
4. Selecciona **All Records**. Clic en **Done**.

### Paso 3: Loop y la Protección Iterativa (DML Bounds)
1. Clic en **(+)** > **Loop**.
2. **Label:** `Girar sobre cada Inscripcion`.
3. **Collection Variable:** Selecciona `{!Extraer_Inscripciones_Sin_Nota}`. Clic en **Done**.
4. **DENTRO** del ciclo For Each, añade un nodo **Get Records**:
    *   **Label:** `Comprobar Spam Tareas Previas`. Objeto: `Task`.
    *   **Condiciones:** `WhatId` Equals `{!Girar_sobre_cada_Inscripcion.Id}` AND `Status` Equals `Open`.
    *   **Store:** `Only the first record`. Clic **Done**.

### Paso 4: Toma de Decisión Lógica
1. A continuación de comprobar spam, dentro del ciclo, añade **Decision**.
2. **Label:** `¿El profesor ya fue advertido?`.
3. **Outcome 1:** Nombre: `Sí (Existe ID de Tarea)`. 
   Condition: `{!Comprobar_Spam_Tareas_Previas}` | Operator: `Is Null` | Value: `{!$GlobalConstant.False}`.
4. **Default Outcome:** Nombre: `No (Avanzar)`. Clic en **Done**.

### Paso 5: Generación de la Alerta (Creación de Tarea)
1. Acércate a la rama del flujo que dice `No (Avanzar)`. Clic en **(+)** > **Create Records**.
2. **Label:** `Crear Tarea de Aviso al Profesor`. 
3. **How Many:** `One` | **How to Set:** `Use separate resources, and literal values`.
4. **Object:** `Task`.
5. **Configuración de Campos:**
    *   `OwnerId` <- `{!Girar_sobre_cada_Inscripcion.OwnerId}`
    *   `WhatId` <- `{!Girar_sobre_cada_Inscripcion.Id}`
    *   `Status` <- `Not Started` o `Open` (Asegura seleccionar uno del picklist de tu org).
    *   `Subject` <- Escribe el texto exacto definido en la HU-204: `Urgente: Cierre de Acta Pendiente`.
    *   `ActivityDate` <- En el cajón de Value o Variable, selecciona **New Resource** > **Formula**.  
        *   API Name: `PlazoAlerta`. Data Type: `Date`. Fomula Box: `{!$Flow.CurrentDate} + 2`. Clic en Done.
6. Clic en **Done** en el nodo creador.
7. Clic en **Save** como `Lumina Cierre de Actas Viernes Batch` y **Activate**.

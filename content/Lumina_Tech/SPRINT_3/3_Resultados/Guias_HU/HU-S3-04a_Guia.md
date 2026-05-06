# 🎯 GUÍA DE IMPLEMENTACIÓN: HU-S3-04a
**Nombre:** Screen Flow Privado — Construcción del Flow (Parte A)
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce (aprendices)
**Herramienta principal:** Setup → Flow Builder

> [!IMPORTANT]
> **Pre-requisito:** La HU-S3-03 debe estar completada. Lucas Martinez y Ana Vega deben existir como Community Users activos antes de iniciar esta HU.
>
> **Siguiente paso:** Al terminar esta guía, continúa con **HU-S3-04b** para publicar el Flow en el portal.

---

## 🧭 ¿Qué vas a construir en esta parte?

Un **Screen Flow** de 2 pantallas que crea un Case (ticket) en Salesforce vinculado automáticamente al alumno logueado. Al finalizar esta guía el Flow estará **activo y listo** para ser publicado en el portal.

## 🔁 Estructura del Flow

```
[Pantalla 1: Que necesitas]  →  [Pantalla 2: Contanos mas]
        ↓
[Create Records → Case]
   ↓ (éxito)          ↓ (error)
[Solicitud enviada]   [Error al enviar]
```

---

### Paso 1: Crear el Screen Flow en Setup

1. En Salesforce, haz clic en el engranaje ⚙️ de la barra superior → **Setup**.
2. En el Quick Find, escribe `Flows` y haz clic en **Flows**.
3. Haz clic en el botón **New Flow** (arriba a la derecha).
4. En el modal que aparece, selecciona **Screen Flow** y haz clic en **Create**.
5. El sistema te lleva **directamente al canvas** del Flow Builder. Verás un nodo **Screen Flow / Start** y un nodo **End** conectados — esto es el punto de partida.

> [!NOTE]
> En la versión actual del Flow Builder **no hay formulario de propiedades al inicio**. El **Label** y el **API Name** se configuran en el primer **Save**, al terminar de construir (ver Paso 7). Comienza a construir directamente en el canvas.

---

### Paso 2: Crear la Pantalla 1 — "Que necesitas"

Esta es la primera pantalla que verá el alumno: un menú desplegable para categorizar su solicitud.

1. En el canvas del Flow Builder, haz clic en el ícono **+** que aparece entre el nodo Start y el nodo End.
2. En el menú que aparece, selecciona **Screen**.
3. Se abre el **Screen Editor**. En la parte superior del editor, verás el campo **Label** — escribe: `Que necesitas`
   - El campo **API Name** se completa automáticamente — déjalo así.
4. En el **panel izquierdo del Screen Editor** hay una barra de búsqueda de componentes. Escribe `Picklist` en esa barra.
5. Haz clic en el componente **Picklist** — aparece en el área central de la pantalla.
6. Con el Picklist seleccionado, en el **panel derecho** configura:
   - **Label:** `Tipo de solicitud`
   - **API Name:** borra lo generado automáticamente y escribe: `inputTipoSolicitud`
   - **Required:** activa el toggle o casilla **Required** ✅
   - **Let Users Select Multiple Options:** selecciona **No**
7. En el panel derecho baja hasta el campo **Choice**. Este campo funciona como un **buscador** — aquí agregas cada opción del menú una por una. El proceso para cada opción es:
   - Haz clic en el campo de búsqueda de Choice
   - Escribe el texto de la opción
   - Como no existe todavía, aparece la opción **`+ Create 'texto...'`** — haz clic en ella
   - Salesforce crea un recurso de tipo **Choice** y lo agrega al Picklist
   - Luego haz clic en **+ Add Choice** para agregar la siguiente

> [!WARNING]
> **Importante sobre tildes y caracteres especiales:** Salesforce **elimina automáticamente** los tildes del API Name de cada Choice. Por ejemplo, `Consulta Académica` se convierte internamente en `Consulta_Acad_mica`. Para evitar API Names deformados, **escribe los valores sin tildes**. Usa los siguientes textos exactos:
> - `Consulta academica`
> - `Nota o calificacion`
> - `Certificado de alumno regular`
> - `Justificacion de inasistencia`
> - `Otro`
>
> El alumno verá estos textos en el formulario tal como los escribiste. Si en el futuro quieres mostrar un Label con tilde (solo visual), haz clic en el ícono de lápiz ✏️ del Choice ya creado para editar su Label por separado sin afectar el API Name.

8. Agrega los 5 valores indicados arriba uno a uno usando el proceso del punto 7.
9. Haz clic en **Done** (botón en la parte inferior del Screen Editor) para guardar la pantalla y volver al canvas.

---

### Paso 3: Crear la Pantalla 2 — "Contanos mas"

Esta es la segunda pantalla. El alumno describe el problema con detalle.

1. En el canvas, haz clic en el **+** que aparece debajo de la Pantalla 1.
2. Selecciona **Screen**.
3. En el campo **Label** del Screen Editor, escribe: `Contanos mas`
   - **API Name:** déjalo como se genera automáticamente.
4. En la barra de búsqueda de componentes del panel izquierdo, escribe `Long Text`.
5. Haz clic en el componente **Long Text Area** para agregarlo a la pantalla.
6. Con el componente seleccionado, configura en el panel derecho:
   - **Label:** `Descripcion del problema`
   - **API Name:** borra y escribe: `inputDescripcion`
   - **Required:** activa **Required** ✅
   - **Placeholder Text:** `Ej: No veo mi nota de Algoritmos I del parcial del 10 de marzo`
7. Ahora busca en el panel izquierdo el componente **Text** (texto de una sola línea) y agrégalo debajo del componente anterior.
8. Configura el componente Text:
   - **Label:** `Materia involucrada (si aplica)`
   - **API Name:** borra y escribe: `inputMateria`
   - **Required:** ❌ NO lo marques como obligatorio
9. Haz clic en **Done**.

---

### Paso 4: Crear el elemento Create Records (Case)

Este es el elemento que crea el ticket en Salesforce. El campo más importante es `Contact ID` — se obtiene automáticamente del alumno logueado sin que él escriba nada.

1. En el canvas, haz clic en el **+** que aparece debajo de la Pantalla 2.
2. En el menú, selecciona **Create Records**.
3. Se abre el configurador del elemento con los siguientes campos en la parte superior:
   - **Label:** `Crear Case del Alumno`
   - **API Name:** se completa automáticamente como `Crear_Case_del_Alumno` — déjalo.
   - **Description:** puedes dejarlo vacío.
4. En el campo **"How to set record field values"**, selecciona **`Manually`** en el dropdown.
5. En la sección **"Create a Record of This Object"**, en el campo **Object**, escribe `Case` y selecciónalo.
6. Ahora verás la sección **"Set Field Values for the Case"** con el botón **`+ Add Field`** al final. Haz clic en **+ Add Field** y repite para cada campo:

**Campo 1: Subject**
- **Field:** escribe `Subject` y selecciónalo.
- **Value:** haz clic en el ícono de búsqueda 🔍 → escribe `Tipo de solicitud` → selecciona `Que necesitas > Tipo de solicitud` (la variable del Picklist de la Pantalla 1).

**Campo 2: Description**
- Clic en **+ Add Field** → **Field:** `Description`
- **Value:** busca `Descripcion del problema` → selecciona `Contanos mas > Descripcion del problema`.

**Campo 3: Contact ID**
- Clic en **+ Add Field** → **Field:** escribe `Contact` y selecciona `Contact ID`.
- **Value:** haz clic en el ícono de búsqueda 🔍.

> [!IMPORTANT]
> **Cómo encontrar el ContactId del alumno logueado:**
> En el buscador de Value, escribe `Running User`.
> Verás la opción **Running User** — así es como el Flow Builder llama internamente al usuario de sesión (`$User`).
> Expándela haciendo clic en la flecha y selecciona **ContactId**.
> El campo mostrará: `Running User > ContactId`.
> Esto vincula automáticamente el Case al alumno logueado — **sin que él escriba su nombre**.

**Campo 4: Case Origin**
- Clic en **+ Add Field** → **Field:** `Case Origin`
- **Value:** escribe directamente el texto literal `Web`.

**Campo 5: Status**
- Clic en **+ Add Field** → **Field:** `Status`
- **Value:** escribe directamente `New`.

**Campo 6: Priority**
- Clic en **+ Add Field** → **Field:** `Priority`
- **Value:** escribe directamente `Medium`.

7. Al terminar, el panel debe verse con los 6 campos mapeados exactamente así:

| Field | Value |
|:---|:---|
| Subject | `Que necesitas > Tipo de solicitud` |
| Description | `Contanos mas > Descripcion del problema` |
| Contact ID | `Running User > ContactId` |
| Case Origin | `Web` |
| Status | `New` |
| Priority | `Medium` |

8. Haz clic en **Done**.

---

### Paso 5: Crear la Pantalla de Confirmación (éxito)

El alumno verá este mensaje cuando su solicitud se registre correctamente.

1. En el canvas, haz clic en el **+** debajo del elemento Create Records.
2. Selecciona **Screen**.
3. En el campo **Label** del Screen Editor, escribe: `Solicitud enviada`
4. En la búsqueda de componentes del panel izquierdo, escribe `Display Text`.
5. Haz clic en el componente **Display Text** para agregarlo.
6. Con el componente seleccionado, en el panel derecho configura:
   - **API Name:** `mensajeConfirmacion`
7. En el área de texto del componente, escribe el siguiente mensaje:

```
Tu solicitud fue enviada exitosamente.

El equipo de Administracion revisara tu caso y te respondera por correo.

Tu referencia: Tipo de solicitud —
```

8. Para insertar la variable dinámica al final de la línea de referencia:
   - Coloca el cursor al final del texto `Tipo de solicitud —`
   - Haz clic en el botón de insertar recurso (ícono `{!}` que aparece en la barra del editor de texto)
   - En el buscador, escribe `inputTipoSolicitud` y selecciónala
   - Quedará: `Tipo de solicitud — {!inputTipoSolicitud}`
9. Haz clic en **Done**.

---

### Paso 6: Crear el Fault Path (camino de error)

Si el Create Records falla (por ejemplo, por falta de permisos), el alumno verá una pantalla amigable en lugar de un error técnico de Salesforce.

1. En el canvas, haz clic sobre el elemento **Crear Case del Alumno** (Create Records) para seleccionarlo — aparecerá con borde azul.
2. Con el elemento seleccionado, mira el **panel de propiedades de la derecha**. Desplázate hacia abajo hasta encontrar la opción **"Add Fault Path"** o una sección llamada **"Fault Connector"**. Haz clic en ella.

> [!NOTE]
> **Si no encuentras "Add Fault Path" en el panel derecho:** En modo Auto-Layout, también puedes hacer clic en el ícono de **⋮ (tres puntos)** que aparece en la esquina del elemento en el canvas → selecciona **"Add Fault Path"**. Una vez activado, verás un nuevo conector de color **naranja** saliendo del elemento, separado del flujo principal.

3. Haz clic en el **+** al final del conector naranja (camino de error).
4. Selecciona **Screen**.
5. En el Screen Editor, configura la pantalla:
   - **Label:** `Error al enviar`
   - **API Name:** `Pantalla_Error` *(verifica que se complete así o escríbelo manualmente)*
6. En la búsqueda de componentes del panel izquierdo, escribe `Display Text` y haz clic en él para agregarlo.
7. Con el componente Display Text seleccionado, en el panel derecho configura:
   - **API Name:** `mensajeError`
8. En el área de texto del componente, escribe el siguiente mensaje:

```
Ocurrio un error al registrar tu solicitud.

Por favor intenta nuevamente. Si el problema persiste,
contacta a Administracion directamente en la oficina.

Detalle tecnico:
```

9. Para insertar la variable `FaultMessage` al final (después de "Detalle tecnico:"):
   - Coloca el cursor al final del texto
   - Haz clic en el botón de insertar recurso (`{!}` en la barra del editor)
   - En el buscador escribe `Fault`
   - Selecciona **Flow → FaultMessage** (o **$Flow → FaultMessage**)
   - Quedará: `Detalle tecnico: {!$Flow.FaultMessage}`

> [!TIP]
> Si el buscador no encuentra "Fault" directamente, busca `Flow` — la variable de sistema del Flow aparece como **Flow** en el resource picker, similar a como `$User` aparece como "Running User".

10. Haz clic en **Done**.

---

### Paso 7: Guardar el Flow y Activarlo

Ahora que el Flow está construido, guárdalo. **Es en este momento que se configura el Label y API Name.**

1. En la barra superior del Flow Builder, haz clic en el botón **Save**.
2. Aparece un **diálogo de guardado** — complétalos exactamente así:
   - **Flow Label:** `Lumina EC Reclamos y Tramites Alumno`
   - **Flow API Name:** `Lumina_EC_Reclamos_Tramites_Alumno` *(se completa automáticamente al escribir el Label — verifícalo)*
   - **Description:** `Flow privado del portal Campus Virtual. Permite a alumnos logueados crear un Case de reclamo o tramite. El ContactId se mapea automaticamente.`
3. Haz clic en **Save** en el diálogo.
4. Una vez guardado, haz clic en el botón **Activate** que aparece en la barra superior.
5. Confirma la activación en el modal que aparece.

> [!WARNING]
> Un Flow en estado **Draft** (borrador) **no funciona en el portal**. El Flow debe quedar en estado **Active** antes de continuar. Verifica que la barra superior indica "Active" después de activarlo.

---

### ✅ Verificación antes de continuar con HU-S3-04b

| # | Verificación | Cómo comprobar | Resultado esperado |
|:---:|:---|:---|:---|
| 1 | **Flow existe** | Setup → Flows → buscar `Lumina EC Reclamos` | Aparece en la lista |
| 2 | **Flow activo** | Misma pantalla → columna Status | Estado = **Active** ✅ |
| 3 | **Pantallas correctas** | Clic en el nombre del Flow → vista del canvas | Se ven: Que necesitas → Contanos mas → Create Records → Solicitud enviada + rama Error al enviar |
| 4 | **Picklist con 5 opciones** | Abrir Pantalla 1 en el canvas | Picklist `inputTipoSolicitud` con los 5 valores |

> [!IMPORTANT]
> Si el Flow no está **Active**, la HU-S3-04b no tendrá el Flow disponible para publicar en el portal. No avances hasta verificar el estado.

**➡️ Continúa en: `HU-S3-04b_Guia.md`**

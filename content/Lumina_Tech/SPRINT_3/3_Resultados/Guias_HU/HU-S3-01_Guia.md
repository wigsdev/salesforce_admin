# 🌐 GUÍA DE IMPLEMENTACIÓN: HU-S3-01
**Nombre:** Creación del Sitio y Branding Lumina
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce

---

## 📍 Referencia de Dimensiones de Imágenes

> [!IMPORTANT]
> Salesforce Experience Cloud **no impone dimensiones fijas**. El sitio es responsivo, por lo que las imágenes se adaptan a distintas resoluciones. Sin embargo, estas son las dimensiones **recomendadas en campo** para la plantilla **Customer Service** usada en este proyecto. Usar dimensiones fuera de estos rangos causará recortes, desproporción o carga lenta.

| Elemento | Dimensión Recomendada | Formato | Peso Máximo | Nota Clave |
|:---|:---:|:---:|:---:|:---|
| **Logo del Header** | `250 x 60 px` | PNG (fondo transparente) | < 200 KB | Fondo transparente obligatorio para que el color del Header se vea |
| **Hero Banner / Imagen de Fondo** | `1440 x 380 px` | JPG o PNG | < 500 KB | Mantener el contenido importante centrado — los bordes se recortan en móvil |
| **Imagen Login Page** | `1280 x 960 px` | JPG o PNG | < 500 KB | Para la página de inicio de sesión del portal privado |
| **Favicon** | `32 x 32 px` | ICO o PNG | < 50 KB | Aparece en la pestaña del navegador |
| **Imágenes de artículos (Knowledge)** | `800 x 400 px` | JPG o PNG | < 300 KB | Imágenes dentro del contenido de artículos FAQ |

> [!TIP]
> **Zona segura del Banner:** El recorte en móvil afecta los bordes laterales. Ubica el logo, título o elemento principal en el **centro horizontal** de la imagen para garantizar visibilidad en cualquier pantalla.

> [!NOTE]
> **Referencia de colores Lumina Tech — formato para copiar y pegar en el Builder:**
> - Lumina Blue: `rgb(0, 90, 156)`
> - Tech Gold: `rgb(242, 169, 0)`
> - Fondo Neutro: `rgb(244, 246, 249)`
> - Texto Oscuro: `rgb(26, 26, 46)`
> - Footer Oscuro: `rgb(26, 26, 46)`

---

### Paso 1: Crear el portal en blanco
1. En **Setup**, busca `All Sites` en el Quick Find y selecciónalo.
2. Haz clic en el botón **New**.
3. Verás un catálogo de plantillas. Selecciona **Customer Service** y haz clic en **Get Started**.
4. En el campo **Name** escribe: `Campus Virtual Lumina Tech`. En el campo **URL** escribe: `alumnos`.
5. Haz clic en **Create**. Espera unos 30 segundos mientras Salesforce construye el sitio base.

---

### Paso 2: Configurar el Idioma del Portal en Español

> [!IMPORTANT]
> Este paso define el idioma que verán los alumnos al entrar al portal. Debe hacerse **antes** del branding y la publicación, ya que cambiar el idioma por defecto borra el contenido escrito en el idioma anterior.

**Prerrequisito — Activar el idioma en la Org:**
1. Ve a **Setup → Quick Find → Language Settings**.
2. En la sección **Displayed Languages**, verifica que **Spanish** (Español) esté en la lista de idiomas activos. Si no está, agrégalo y guarda.

**Configurar el idioma por defecto en el sitio:**
1. En la pantalla de **Workspaces** del sitio recién creado, haz clic en el mosaico **Builder**.
2. En la barra lateral izquierda del Builder, haz clic en el ícono de engranaje ⚙️ (**Settings**).
3. En el menú lateral de Settings, haz clic en **Languages**.
4. Haz clic en el botón **Add Languages**.
5. Selecciona **Spanish** de la lista y haz clic en **Add**.
6. Una vez agregado, haz clic en el menú de acciones (▼) que aparece junto a **Spanish** en la lista.
7. Selecciona **Set as default site language**. Confirma la acción.
8. Verifica que Spanish aparece ahora con el badge **"Default"** en la lista de idiomas.

**Traducir los textos de la interfaz (componentes de la plantilla):**
1. En la barra de herramientas superior del Builder, busca el **selector de idioma** (aparece como una bandera o el nombre del idioma activo). Cámbialo a **Spanish**.
2. Ahora todos los textos editables de los componentes de la Home pueden ser escritos en español.
3. Haz clic sobre cada componente que tenga texto (banner de bienvenida, botones, texto de sección) y reescríbelo en español directamente.

---

### Paso 3: Aplicar el Branding de Colores (Theme)
1. En la barra lateral izquierda del Builder, haz clic en el ícono del pincel 🎨 (**Theme**).
2. En el panel Theme, haz clic en la sección **Colors**.
3. Para cada campo de color de la tabla de abajo, haz clic en el **cuadro de color** junto a su nombre. Se abrirá el color picker — copia y pega el valor `rgb()` directamente en el campo de texto del picker.

**Sección: General**

| Campo (nombre exacto en el Builder) | Color Lumina | Valor para pegar |
|:---|:---|:---:|
| **Text Color** | Texto principal oscuro | `rgb(26, 26, 46)` |
| **Detail Text Color** | Gris secundario (subtítulos, captions) | `rgb(108, 117, 125)` |
| **Action Color** | Lumina Blue (botones de acción) | `rgb(0, 90, 156)` |
| **Link Color** | Lumina Blue (hipervínculos) | `rgb(0, 90, 156)` |
| **Overlay Text Color** | Blanco (texto sobre imágenes o fondos oscuros) | `rgb(255, 255, 255)` |
| **Border Color** | Gris claro (bordes y separadores) | `rgb(221, 224, 230)` |
| **Page Background Color** | Fondo neutro Lumina | `rgb(244, 246, 249)` |

**Sección: Navigation**

| Campo (nombre exacto en el Builder) | Color Lumina | Valor para pegar |
|:---|:---|:---:|
| **Navigation Background Color** | Lumina Blue (fondo de la barra de navegación) | `rgb(0, 90, 156)` |
| **Navigation Text Color** | Blanco (texto del menú de navegación) | `rgb(255, 255, 255)` |
| **Navigation Bar Background Color** | Azul más oscuro (barra superior) | `rgb(0, 58, 112)` |

**Sección: Login Pages**

| Campo (nombre exacto en el Builder) | Color Lumina | Valor para pegar |
|:---|:---|:---:|
| **Background Color** | Fondo neutro Lumina | `rgb(244, 246, 249)` |
| **Card Background Color** | Blanco (tarjeta del formulario de login) | `rgb(255, 255, 255)` |
| **Error Text Color** | Rojo estándar (no cambiar — es un color funcional) | *Dejar por defecto* |

> [!TIP]
> El **Tech Gold** `rgb(242, 169, 0)` es el color de acento institucional. En el Builder se usa en texto destacado, íconos o elementos decorativos dentro de los componentes de las páginas, **no** en los 11 campos de color base del Theme (ya que como color de texto principal sobre fondo blanco tiene bajo contraste para lectura prolongada).


4. Después de configurar cada color, haz clic fuera del picker para confirmar. No hace falta guardar después de cada uno.

---

### Paso 4: Subir las Imágenes del Portal (Panel Images)
1. En la barra lateral izquierda del Builder, haz clic en el ícono del pincel 🎨 (**Theme**).
2. En el panel Theme, haz clic en la sección **Images**. Verás dos grupos:

**Sección: General**

| Campo | Descripción | Dimensiones | Archivo |
|:---|:---|:---:|:---|
| **Company Logo** | Logo en el encabezado del sitio | `250 x 60 px` PNG | `lumina_logo_header.png` ✅ Ya cargado |
| **Header Image** | Imagen de fondo del banner superior de la Home | `1440 x 380 px` JPG/PNG | `lumina_header_banner.jpg` |

**Sección: Login Pages**

| Campo | Descripción | Dimensiones | Archivo |
|:---|:---|:---:|:---|
| **Background Image** | Fondo de la pantalla de inicio de sesión | `1280 x 960 px` JPG/PNG | `lumina_login_bg.jpg` |

3. Para subir cada imagen: haz clic en el área punteada del campo correspondiente → selecciona **Upload** → elige el archivo desde `content/Lumina_Tech/Recursos_Graficos/Theme/`.
4. Una vez subida, la vista previa del Builder se actualiza en tiempo real.


---

### Paso 5: Configurar la Navegación en Español
1. Haz clic sobre la **barra de navegación** (navigation bar) del Header.
2. En el panel derecho, busca la propiedad **Navigation Menu** y haz clic en el nombre del menú actual para editarlo.
3. En el editor de menú, renombra o elimina los ítems que no correspondan. Los ítems recomendados para el Campus Virtual son:
   - **Inicio** (apunta a la página Home)
   - **Hacer una consulta** (apunta a la página del formulario de reclamos)
   - **Preguntas frecuentes** (apunta a la sección de Knowledge)
4. Guarda los cambios del menú.

---

### Paso 6: Corregir el Link Color (texto en naranja)

> [!IMPORTANT]
> El color naranja que aparece en palabras como "solutions" dentro del texto es el **Link Color** configurado con el Tech Gold. Para texto de cuerpo, los links deben ser Lumina Blue para mantener legibilidad profesional.

1. En el Builder, ve al ícono del pincel 🎨 → **Theme** → **Colors**.
2. Busca el campo **Link Color** y cámbialo a: `rgb(0, 90, 156)` (Lumina Blue).
3. Esto corregirá todos los hipervínculos inline del portal de naranja a azul.


---

### Paso 7: Corregir el Nombre de Usuario en el Header

> El header muestra el *username técnico* de Salesforce (ej: `USER7781...`) en lugar del nombre real del alumno.

1. En Salesforce (fuera del Builder), ve a **Setup → Users** y busca al usuario del portal (Lucas Martinez).
2. Edita el campo **Nickname** y pon el nombre real: `Lucas Martinez`.
3. La mayoría de las plantillas usan el campo **Nickname** para mostrar el nombre en el header del portal.
4. Publica el sitio nuevamente para que el cambio se refleje.

---

### Paso 8: Configurar el Idioma y Editar los Textos de la Home

**8.1 — Establecer el idioma por defecto del sitio:**
1. En la barra lateral izquierda del Builder, haz clic en el ícono de engranaje ⚙️ (**Settings**).
2. En el panel de Settings, haz clic en **Languages**.
3. En el campo **Default Site Language**, selecciona **Spanish** del dropdown.
4. Guarda el cambio. A partir de aquí el sitio toma español como idioma base.

**8.2 — Editar los textos del componente Headline (bienvenida):**
1. Haz clic directamente sobre el área de bienvenida central (el componente se llama **Headline** y el panel derecho lo confirma).
2. El panel derecho mostrará los campos editables:
   - **Title** → escribe: `¡Bienvenido al Campus Virtual de Lumina Tech University!`
   - **Banner Text** → escribe: `Tu espacio para trámites, consultas y recursos académicos.`
3. Haz clic en los tabs `FEATURED`, `DISCUSSIONS`, `MY FEED` y edita sus labels a: `Destacado`, `Discusiones`, `Mi Feed`.
4. Haz clic en el botón azul principal y edita a: `Hacer una consulta`.

> [!NOTE]
> La **Header Image** (`lumina_header_banner.png`) ya quedó configurada en el **Paso 4 (Theme → Images → Header Image)**. No requiere ninguna acción adicional en el componente Headline — se aplica automáticamente a través del Theme.


---

### Paso 10: Configurar la Navegación (Solo Inicio por ahora)

> [!IMPORTANT]
> Los ítems **"Hacer una consulta"** y **"Preguntas frecuentes"** requieren páginas que se crearán en HUs posteriores. Agregarlos ahora con Type `Navigational Topic` hace que **no aparezcan** para el usuario real del portal. Para no generar confusión al administrador, el menú queda solo con **Inicio** en esta HU.

1. Haz clic sobre la **barra de navegación** debajo del header.
2. En el panel derecho, busca **Navigation Menu** y haz clic en editar.
3. En el editor de menú, **elimina** los ítems "Hacer una consulta" y "Preguntas frecuentes (FAQ)" haciendo clic en la **X** de cada uno.
4. Deja únicamente el ítem **`Home`** (renombrado a `Inicio`).
5. Guarda los cambios del menú.

> [!NOTE]
> **Cuándo agregar los ítems restantes:**
> - `Hacer una consulta` → se agregará al implementar **HU-S3-04** (Screen Flow de Reclamos), cambiando el Type a `External URL` apuntando a la página del Flow.
> - `Preguntas frecuentes` → se agregará al implementar **HU-S3-05** (Knowledge Base), apuntando a la página de artículos.

---

### Paso 11: Publicar y Habilitar Acceso Público
1. En el Builder, haz clic en el engranaje ⚙️ (**Settings**).
2. Ve a la pestaña **General**.
3. Activa: **"Let guest users view this site without logging in"**.
4. Haz clic en **Publish** → confirma con **Publish**.
5. Abre la URL en modo incógnito para verificar el resultado final.

---

### ✅ Checklist de Resultado Profesional

| Elemento | Paso | Verificación |
|---|:---:|---|
| Colores del Theme configurados (11 campos: General, Navigation, Login Pages) | Paso 3 | ☐ |
| Company Logo subido (`250 x 60 px`, PNG fondo transparente) | Paso 4 | ☐ |
| Header Image subida (`1440 x 380 px`) via Theme → Images | Paso 4 | ☐ |
| Background Image de Login subida (`1280 x 960 px`) via Theme → Images | Paso 4 | ☐ |
| Nombre del usuario legible en el header (CSS Custom aplicado) | Paso 6 | ☐ |
| Idioma por defecto del sitio en **Spanish** (Settings → Languages) | Paso 8.1 | ☐ |
| Título de bienvenida en español (campo Title del Headline) | Paso 8.2 | ☐ |
| Subtexto en español (campo Banner Text del Headline) | Paso 8.2 | ☐ |
| Tabs renombrados: Destacado / Discusiones / Mi Feed | Paso 8.2 | ☐ |
| Botón principal renombrado a: Hacer una consulta | Paso 8.2 | ☐ |
| Menú de navegación con solo **Inicio** (ítems futuros eliminados) | Paso 10 | ☐ |
| Sitio publicado con Publish sin errores | Paso 11 | ☐ |
| URL del portal abre correctamente en ventana incógnito | Paso 11 | ☐ |

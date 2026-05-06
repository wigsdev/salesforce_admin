# 📚 GUÍA DE IMPLEMENTACIÓN: HU-S3-05
**Nombre:** Knowledge — 3 Artículos FAQ Publicados en el Portal
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce (aprendices)
**Herramientas:** App Launcher → Knowledge + Setup → Data Category Setup + Experience Builder

> [!IMPORTANT]
> **Pre-requisitos:**
> - **HU-S3-00 completada:** Knowledge habilitado y checkbox **"Knowledge User"** activo en el usuario Admin.
> - **Page Layout de Knowledge:** En tu Org (Setup → Object Manager → Knowledge → Page Layouts), asegúrate de haber arrastrado al *Layout* las casillas cuyos nombres de API/Etiqueta exacta son **`Customer`** y **`Public Knowledge Base`**, y de tener creado un campo personalizado de tipo **Rich Text** (ej: `Cuerpo del Articulo` o `Respuesta`) para escribir el contenido. (El layout base viene vacío).
> - **HU-S3-01 completada:** El sitio Campus Virtual debe estar publicado.
> - **HU-S3-04b completada:** El menú ya tiene "Hacer una consulta".

---

## 🧭 ¿Qué vas a construir?

Una base de conocimiento (FAQ) accesible desde el portal del alumno:
1. Organizar los artículos con categorías temáticas (Data Categories)
2. Crear 3 artículos FAQ con contenido y visibilidad correctos
3. Crear la página "Preguntas frecuentes" en el portal
4. Agregar el componente de artículos a esa página
5. Agregar el ítem "Preguntas frecuentes" al menú de navegación
6. Publicar el sitio

---

## 🔁 Estructura a construir

```
[Data Category Group: Lumina Knowledge]
    ├── Calendarios y Fechas
    ├── Notas y Evaluaciones
    └── Tramites y Certificados

[3 Artículos Knowledge publicados]
    ├── Art. 1: ¿Cuando son los examenes finales?       → Calendarios y Fechas
    ├── Art. 2: ¿Como justifico una inasistencia?       → Tramites y Certificados
    └── Art. 3: ¿Cual es la escala de calificaciones?   → Notas y Evaluaciones

[Portal: página "Preguntas frecuentes" con componente Article List]
[Menú: Inicio | Hacer una consulta | Preguntas frecuentes]
```

---

### Paso 1: Verificar que Knowledge esté habilitado

Antes de crear artículos, confirma que Knowledge está activo en tu Org.

1. En Salesforce, haz clic en el engranaje ⚙️ de la barra superior → **Setup**.
2. En el Quick Find, escribe `Knowledge Settings` → haz clic en **Knowledge Settings**.
3. Verifica que la casilla **"Enable Lightning Knowledge"** (o **"Enable Salesforce Knowledge"**) está activa ✅.
4. Si no está activa, actívala y guarda — esto puede tardar unos segundos.

**Verificar que tu usuario tiene Knowledge User activo:**
5. En el Quick Find, escribe `Users` → haz clic en **Users**.
6. Haz clic en el nombre de tu usuario administrador.
7. En el detalle del usuario, busca el campo **"Knowledge User"** — debe estar marcado ✅.
8. Si no está marcado, haz clic en **Edit** → activa **Knowledge User** → **Save**.

> [!NOTE]
> Sin el checkbox **Knowledge User** activo, el App Launcher no mostrará la aplicación Knowledge y no podrás crear artículos.

---

### Paso 2: Configurar Knowledge Setup (Asistente guiado)

1. En Salesforce, haz clic en el engranaje ⚙️ de la barra superior y selecciona **Service Setup** (Configuración de servicio).
2. En la pantalla principal de Service Setup, haz clic en **View All** (Ver todo) en la sección de Recommended Setup.
3. Busca y selecciona **Knowledge Setup**.
4. Haz clic en **Start** (Iniciar).
5. Selecciona los usuarios que serán autores de Lightning Knowledge (asegúrate de marcar tu propio usuario).
6. En "Data Category Group", introduce el nombre: `Lumina Knowledge`.
7. En "Data Categories", introduce las 3 categorías (conecta usando el botón "+"):
   - `Calendarios y Fechas`
   - `Notas y Evaluaciones`
   - `Tramites y Certificados`
8. Haz clic en **Finish** (Finalizar).

> [!NOTE]
> Este asistente no solo habilitará la base de conocimientos y asignará las licencias a los autores, sino que también creará la estructura base de categorías de datos de forma automática.

---

### Paso 3: Crear campo "Cuerpo del Artículo" y añadir al Page Layout

El artículo necesita un espacio de texto para albergar las respuestas largas.

1. Vuelve a la configuración general de Salesforce y haz clic en la pestaña **Object Manager** (Gestor de objetos).
2. Busca y selecciona **Knowledge** en la lista.
3. Selecciona **Fields & Relationships** (Campos y relaciones) a la izquierda.
4. Haz clic en el botón **New** (Nuevo).
5. Selecciona el tipo de dato **Text Area (Rich)** o **Text Area (Long)** y dale a Siguiente. *(Recomendado Rich Text con Longitud 32768).*
6. En Field Label (Nombre del campo) ponle: `Cuerpo del Articulo`. Dale a Siguiente.
7. Asegúrate de que los checkboxes de "Visible" estén activos para los perfiles. Haz clic en Siguiente.
8. En la última pantalla, dale a **Save** (Guardar).

Ahora agreguemos este campo y las casillas de seguridad al formulario visual:
9. En el menú izquierdo del Object Manager de Knowledge, selecciona **Page Layouts** (Formatos de página).
10. Haz clic en el layout **Lightning Knowledge FAQ Layout** (o el que uses por defecto).
11. En la parte superior (paleta de campos), busca el campo que acabamos de crear (`Cuerpo del Articulo` o `Texto`) y arrástralo hacia abajo a la sección **Knowledge Detail**.
12. Haz clic en **Quick Save** (Guardado rápido) y luego en **Save** en la parte superior.

*(Nota: Las casillas de visibilidad "Visible to Customer" y "Visible in Public Knowledge Base" aparecerán automáticamente integradas al final del formulario al momento de crear un artículo en una sección llamada 'Properties').*

---

### Paso 4: Configurar los "Topics for Objects" (Seguridad Crítica)

Salesforce Experience Cloud necesita un "puente" de conexión entre la base de datos de los artículos y el portal web.

1. En el Quick Find de Salesforce Setup, busca y selecciona **Topics for Objects** (Temas para objetos).
2. Verás una lista alfabética de todos los objetos. Baja y haz clic sobre la palabra **Knowledge**.
3. Marca la casilla general que dice **Enable Topics** (Habilitar temas).
4. Haz clic en el botón **Save** (Guardar).

---

### Paso 4.1: Configurar la Visibilidad Externa (OWD) - ¡Muy Importante!

Si usas Lightning Knowledge con la colaboración estándar, el acceso predeterminado de los usuarios externos puede ocultar todos tus artículos sin importar sus categorías.

1. Ve a **Setup** y busca **Sharing Settings** (Configuración de colaboración).
2. Haz clic en el botón **Edit** (Modificar) bajo "Organization-Wide Defaults".
3. Busca el objeto **Knowledge** en la inmensa lista.
4. En la columna **Default External Access** (Acceso externo predeterminado), asegúrate de que diga **`Public Read Only`** (Sólo lectura pública). Si dice "Private", modifícalo.
5. Haz clic en **Save** y espera el recálculo automático.

---

### Paso 5: Crear el Artículo 1 — Exámenes Finales

1. Haz clic en el ícono de puntos (⚡ App Launcher) en la barra superior izquierda.
2. En el buscador del App Launcher, escribe `Knowledge` → haz clic en **Knowledge**.
3. En la aplicación Knowledge, haz clic en el botón **New** (arriba a la derecha).
4. Se abre el editor de artículo. Completa los siguientes campos:

**Información básica:**
- **Title:** `Cuando son los examenes finales`
- **URL Name:** se completa automáticamente — puedes dejarlo o escribir `cuando-son-los-examenes-finales`

**Cuerpo del artículo:**
5. En el área de texto **Body** (o **Summary/Description** según la versión), escribe el siguiente contenido:

```
Los examenes finales del ciclo actual se realizan en las siguientes fechas:

- Algoritmos I: 15 de julio
- Matematica Aplicada: 17 de julio
- Administracion de Empresas: 19 de julio
- Ingles Tecnico: 21 de julio

Para consultar el calendario completo, contacta a la oficina de Administracion.
```

**Data Category:**
6. Busca la sección **Data Categories** en el formulario.
7. Haz clic en **Edit** o en el campo de categorías.
8. Selecciona el grupo **Lumina Knowledge** → selecciona **Calendarios y Fechas**.

**Visibilidad (Properties):**
9. Desplázate hasta la parte inferior del formulario, a la sección **Properties** (Propiedades).
10. Marca las siguientes opciones:
    - ✅ **`Visible para el cliente`** (Visible to Customer) — visible para usuarios logueados en el portal.
    - ✅ **`Visible en base de conocimientos pública`** (Visible In Public Knowledge Base) — visible también para visitantes anónimos.

> [!IMPORTANT]
> **¿Por qué activar "Public Knowledge Base"?** Las FAQ sobre fechas de finales son útiles incluso para personas que aún no son alumnos (por ejemplo, padres o futuros estudiantes). Artículos sin ninguna de estas dos casillas activadas NO aparecen en el portal para nadie.

**Publicar:**
11. Una vez completado, haz clic en el botón **Publish** (en la barra superior del artículo o en el área de acciones).
12. En el modal de confirmación, selecciona publicar **ahora** (not scheduled) → confirma.
13. El estado del artículo debe cambiar a **Published** ✅.

---

### Paso 6: Crear el Artículo 2 — Justificación de Inasistencia

1. En la aplicación **Knowledge**, haz clic en **New**.
2. Completa:

**Información básica:**
- **Title:** `Como justifico una inasistencia`
- **URL Name:** `como-justifico-una-inasistencia`

**Cuerpo del artículo:**
3. En el área **Body**, escribe:

```
Para justificar una inasistencia debes seguir estos pasos:

1. Completar el formulario de Justificacion de Inasistencia disponible en la oficina de Administracion o en el portal.
2. Adjuntar la documentacion que respalde tu ausencia (certificado medico, constancia institucional, etc.).
3. Presentar la solicitud dentro de los 5 dias habiles posteriores a la inasistencia.
4. El equipo de Administracion revisara tu caso y te notificara por correo.

Para casos urgentes, contacta directamente a la oficina de Administracion.
```

**Data Category:**
4. Selecciona **Lumina Knowledge** → **Tramites y Certificados**.

**Visibilidad (Properties):**
5. En la sección inferior **Properties**, activa:
   - ✅ **`Visible para el cliente`** (Visible to Customer) — visible para alumnos logueados

> [!NOTE]
> Este artículo aplica solo a alumnos activos, por lo que no es necesario activar "Public Knowledge Base". Solo alumnos logueados lo verán.

**Publicar:**
6. Haz clic en **Publish** → confirma → verifica estado **Published** ✅.

---

### Paso 7: Crear el Artículo 3 — Escala de Calificaciones

1. En la aplicación **Knowledge**, haz clic en **New**.
2. Completa:

**Información básica:**
- **Title:** `Cual es la escala de calificaciones de Lumina Tech`
- **URL Name:** `escala-de-calificaciones`

**Cuerpo del artículo:**
3. En el área **Body**, escribe:

```
La escala de notas de Lumina Tech University va del 0 al 10.

- Nota minima de aprobacion: 6 (seis)
- Calificacion de 0 a 5: condicion de Desaprobado
- Calificacion de 6 a 10: condicion de Aprobado
- Las evaluaciones de recuperatorio siguen la misma escala.

Para consultas sobre una nota especifica, utiliza el formulario "Hacer una consulta" del portal.
```

**Data Category:**
4. Selecciona **Lumina Knowledge** → **Notas y Evaluaciones**.

**Visibilidad (Properties):**
5. En la sección inferior **Properties**, activa:
   - ✅ **`Visible para el cliente`** (Visible to Customer)
   - ✅ **`Visible en base de conocimientos pública`** (Visible In Public Knowledge Base)

**Publicar:**
6. Haz clic en **Publish** → confirma → verifica estado **Published** ✅.

---

### Paso 8: Crear la Página "Preguntas frecuentes" en Experience Builder

1. En Setup, escribe `All Sites` en el Quick Find → haz clic en **All Sites**.
2. En la fila del sitio **Campus Virtual Lumina Tech**, haz clic en el botón **Builder**.
3. En la barra superior del Builder, haz clic sobre el **nombre de la página actual** (dice "Home" o "Inicio") — se despliega el selector de páginas.
4. En la parte inferior del panel, haz clic en **+ New Page**.
5. Selecciona **Standard Page**.
6. Selecciona el layout **Flexible Layout**.
7. Completa los campos:
   - **Page Name:** `Preguntas frecuentes`
   - **URL:** `faqs`
8. Haz clic en **Create**.

**Configurar el acceso de la página:**
9. Con la página **Preguntas frecuentes** activa, haz clic en el ícono **⚙️ (Settings)** de la barra superior junto al nombre de la página → **Page Settings** o **Page Access**.
10. Para esta página, el acceso puede ser **Public** (accesible para todos, incluyendo visitantes anónimos) — ya que la información de FAQ no requiere login.
11. Guarda la configuración.

---

### Paso 9: Mapear Data Categories a Topics (Paso Crítico del Portal)

Experience Cloud usa "Topics" (Temas) para organizar la vista del usuario en lugar de las Data Categories internas. Debemos conectarlos:

1. En la barra superior izquierda del Builder, haz clic en el menú sándwich (tres líneas horizontales) y selecciona **Salesforce Setup** para volver a Salesforce, o si te da la opción allí mismo selecciona **Workspaces**.
2. Ve a **Setup → All Sites** → haz clic en **Workspaces** al lado de tu sitio Campus Virtual.
3. Haz clic en el recuadro **Content Management** (Gestión de contenido).
4. En la barra superior, haz clic en la pestaña **Topics** (Temas).
5. En el menú lateral elige **Automatic Topic Assignment** (Asignación automática de temas).
6. Activa la opción para asignar temas automáticamente a los artículos.
7. Selecciona tu grupo **Lumina Knowledge**.
8. Mapea cada categoría (Calendarios, Notas, Tramites) a un Topic con el mismo nombre y haz clic en **Save** o **Add**.
*(Alternativamente: Puedes ir a "Article Management" en esa misma pantalla, buscar tus 3 artículos y asignarles un Topic a mano).*

---

### Paso 10: Agregar el Componente de Artículos a la Página

1. Vuelve a tu pestaña del **Experience Builder** y asegúrate de estar en la página **Preguntas frecuentes**.
2. En la **barra lateral izquierda** del Builder, haz clic en el ícono de **Components** (⚡).
3. En el buscador del panel de componentes, escribe `Article`.
4. En la sección **Topics**, busca el componente **"Trending Articles by Topic"** o **"Top Articles by Topic"** — arrástralo al área central de la página.
5. El componente mostrará una vista previa de los artículos que acabas de mapear con sus respectivos temas.

---

### Paso 11: Actualizar el Menú de Navegación

El menú actualmente debe mostrar: `Inicio | Hacer una consulta`. Agrega el nuevo ítem.

1. En el Builder, haz clic sobre la **barra de navegación** (franja azul donde dice "INICIO").
2. En el panel derecho aparece la propiedad **Navigation Menu** — haz clic en el nombre para editarlo.
3. Se abre el editor **Edit Default Navigation**. Haz clic en **+ Add Menu Item**.
4. Configura el nuevo ítem:
   - **Name:** `Preguntas frecuentes`
   - **Type:** selecciona **`Site Page`**
   - **Page:** selecciona `Preguntas frecuentes` del dropdown
   - **Publicly available:** ✅ **YES** — las FAQ son información pública, accesible para todos
5. Haz clic en **Save Menu**.
6. Verifica que el menú muestra: `Inicio | Hacer una consulta | Preguntas frecuentes`.

---

### Paso 12: Publicar el Sitio

1. En la barra superior del Builder, haz clic en el botón **Publish**.
2. En el modal de confirmación, haz clic en **Publish** nuevamente.
3. Espera el mensaje de confirmación de publicación exitosa.

---

### ✅ Checklist de Resultado Profesional — QA

| # | Prueba | Cómo verificar | Resultado Esperado |
|:---:|:---|:---|:---|
| 1 | **Data Categories activas** | Setup → Data Category Setup → Lumina Knowledge | Estado: **Active** ✅ |
| 2 | **3 artículos publicados** | App Launcher → Knowledge → filtrar por Status = Published | 3 artículos con estado **Published** |
| 3 | **Home con Temas Destacados**| Acceder a la comunidad (Inicio) y abrir el contenido "Destacado" | Se aprecian los 3 recuadros gráficos con las portadas HD |
| 4 | **Página FAQ existe** | Builder → página Preguntas frecuentes | El componente "Trending Articles by Topic" divide las columnas |
| 5 | **Menú actualizado** | Sitio publicado → barra de navegación | `Inicio | Hacer una consulta | Preguntas frecuentes` |
| 6 | **Articles visibles anónimo** | Navegador incógnito → clic en "Preguntas frecuentes" | Art. 1 y Art. 3 visibles sin login |
| 7 | **Login y 3 artículos** | Iniciar sesión como Lucas Martinez → Preguntas frecuentes | Los 3 artículos son visibles |
| 8 | **Búsqueda inteligente** | Buscador del portal → escribir `notas` | Aparece el Art. 3 como primer resultado |
| 9 | **Canal Customer funciona** | Iniciar sesión → buscar Art. 2 (Justificación) | Visible solo para logueados, oculto en incógnito |

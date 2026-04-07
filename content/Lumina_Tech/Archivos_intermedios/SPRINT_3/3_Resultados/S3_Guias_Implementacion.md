# GUÍA EXTENDIDA DE IMPLEMENTACIÓN — SPRINT 3
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce
**Objetivo:** Proporcionar un "paso a paso" detallado, estilo tutorial de clics, para implementar cada HU del Sprint 3 sin dejar lugar a confusiones técnicas o errores de UI.

---

## 🛠️ HU-S3-00: Activación de la Plataforma de Portal
*El pre-requisito absoluto. Sigue esto antes de hacer cualquier otra cosa.*

### Paso 1: Activar Digital Experiences
1. Ve al ícono del engranaje (⚙️) arriba a la derecha y selecciona **Setup**.
2. En el buscador rápido (Quick Find) de la izquierda, escribe `Digital Experiences` y haz clic en **Settings**.
3. Verás una casilla que dice **Enable Digital Experiences**. Múrcala (Check ✅).
4. El sistema te pedirá establecer un nombre de dominio (si no tienes uno). Ingresa `luminatech-[tus_iniciales]` y haz clic en **Check Availability**.
5. Haz clic en **Save** y luego en **OK**. *(Salesforce podría refrescar o pedirte iniciar sesión de nuevo; es normal).*

### Paso 2: Activar Knowledge
1. En **Setup**, escribe `Knowledge Settings` en el Quick Find.
2. Marca la casilla **Enable Lightning Knowledge**.
3. Haz clic en **Save**. Aparecerá una advertencia diciendo que no se puede deshacer. Acepta.

### Paso 3: Asignarte el permiso de Knowledge User (Crucial)
1. En **Setup**, busca `Users` en el Quick Find y entra.
2. Haz clic en **Edit** junto a tu propio nombre de usuario (el administrador con el que estás logueado).
3. Busca en la columna derecha una casilla llamada **Knowledge User** y márcala (Check ✅).
4. Haz clic en **Save**. *(Si no haces esto, la pestaña de Knowledge jamás te aparecerá).*

---

## 🌐 HU-S3-01: Creación del Sitio y Branding Lumina

### Paso 1: Crear el portal en blanco
1. En **Setup**, busca `All Sites` dentro de Digital Experiences y entra.
2. Haz clic en el botón nuevo **New**.
3. Verás un catálogo de plantillas. Selecciona **Customer Service** y haz clic en **Get Started**.
4. Nombra el sitio: `Campus Virtual Lumina Tech`. Para la URL al final, escribe `alumnos` o déjalo en blanco.
5. Haz clic en **Create**. Espera unos 30 segundos mientras construye el cascarón.

### Paso 2: Aplicar el Branding (Colores y Logo)
1. En la pantalla que aparece (Workspaces), haz clic en el mosaico **Builder**. Esto te llevará al editor visual del portal.
2. En la barra lateral izquierda, haz clic en el ícono del pincel 🎨 (**Theme**).
3. Haz clic en el menú desplegable junto a la palabra "Colors" y selecciona **Edit**.
   - Cambia el **Action Color / Primary** por `#005A9C`
   - Cambia el **Text Color** u otros bordes aplicables con `#F2A900`
   - Cambia el **Page Background** por `#F4F6F9`
   - Vuelve atrás.
4. Para poner el logo: haz clic en el encabezado (Header) de la página en el centro de tu pantalla. En la ventanita de propiedades que aparece la derecha, busca donde dice "Company Logo", haz clic en el botón de imagen y sube el archivo de logo de Lumina Tech.

### Paso 3: Abrir las puertas al público
1. En el mismo **Experience Builder**, haz clic en el engranaje ⚙️ de la izquierda (**Settings**).
2. En la pestaña **General**, busca la sección *Public Access*.
3. **Marca la casilla:** *"Guest users can see and interact with the site without logging in"*.
4. Haz clic en el botón **Publish** (arriba a la derecha) y luego de nuevo en **Publish**.

---

## 🔄 HU-S3-02: Screen Flow Público (Captación de Leads)

### Paso 1: Construir el Flow
1. **Setup** → Escribe `Flows` → **New Flow** → Selecciona **Screen Flow** → Create.
2. Haz clic en el botón `+` y agrega un elemento **Screen**. Lámalo "Datos".
   - Arrastra el componente **Name** (Nombre). En la derecha, asígnale el API name `inputNombre`.
   - Arrastra el componente **Email** (Correo). En la derecha, asígnale el API name `inputEmail`.
   - Haz clic en **Done**.
3. Haz clic en el `+` después de la pantalla y agrega el elemento de datos **Create Records**.
   - Label: `Crear Lead`.
   - Selecciona "Use separate resources, and literal values".
   - Object: `Lead`.
   - Mapeo de campos:
     - `LastName` → `{!inputNombre.lastName}` (usa variables, si no, usa el output completo de Nombre).
     - `Company` → Escribe el texto directo: `Prospectos Lumina Tech`.
     - `LeadSource` → Escribe el texto directo: `Web`.
     - `Email` → `{!inputEmail.value}`.
4. Agrega una pantalla final con el elemento **Display Text**. Escribe "Gracias por tu interés". Guarda el flow, llámalo `Captacion Futuro Alumno` y dale **Activate**.

### Paso 2: Permisos de Guest User (La Trampa)
1. Ve al **Experience Builder** de tu sitio → Engranaje ⚙️ (Settings) → **General**.
2. Haz clic en el link que dice **Guest User Profile**. Se abrirá el perfil público.
3. Haz clic en **Edit** o ve a "Object Permissions". Mueve el scroll hasta "Leads". Activa las casillas **Read** y **Create**.
4. Retorna a la página general del perfil, busca **Flow Access** → Edit → Pasa tu Flow `Captacion Futuro Alumno` a la columna de Enabled. → Save.

### Paso 3: Poner el Flow en la página
1. Vuelve al **Experience Builder**. En la página "Home", haz clic en el relámpago ⚡ a la izquierda (Components).
2. Busca "Flow", arrástralo y suéltalo en el centro de tu página.
3. A la derecha, elige tu Flow de la lista que aparece.
4. Haz clic en **Publish**.

---

## 👥 HU-S3-03: Habilitación de Alumnos (Community Users)

### Paso 1: Configurar el Login del Portal
1. Ve a **Setup → All Sites** → haz clic en **Workspaces** al lado de tu sitio.
2. Clic en **Administration** → Pestaña **Members**.
3. En la lista desplegable del buscador cambia "Portal" por "All". Pasa el perfil **Customer Community User** a la columna "Selected Profiles". Haz clic en **Save**. *(Si olvidas este paso, los alumnos no podrán loguearse).*

### Paso 2: Convertir al Contacto en Usuario
1. Cierra Setup y abre la aplicación normal Sales. Ve a la pestaña **Contacts**.
2. Abre el registro alumno de "Lucas Martinez".
3. En la esquina superior derecha del registro busca la flecha de opciones y haz clic en **Enable Customer User** (a veces está dentro del menú de botones).
4. El sistema abre la pantalla de creación de usuario:
   - User License: `Customer Community`.
   - Profile: `Customer Community User`.
   - Role (si lo pide): No le des importancia alta o ponlo por defecto.
   - Email: El real de prueba que controles.
   - *Nota:* Asegúrate de que el campo Username (nombre de usuario) sea único (ej: `lucas.mtz@lumina.edu.2024`).
5. **Save.** ¡El alumno ahora puede iniciar sesión!

---

## 🎯 HU-S3-04: Screen Flow Privado (Reclamos - Case)

### Paso 1: Crear el Flow que toma el ID automático
1. **Setup → Flows → New Screen Flow**.
2. Crea tu primer Screen y agrega:
   - Picklist (`inputMotivo`): Ponle de opciones: "Notas", "Certificados". Obligatorio.
   - Text Area (`inputProblema`): Label "Describe tu problema". Obligatorio.
3. Ahora la lógica: Agrega un **Create Records** → Object: `Case`.
4. Mapeo de campos:
   - `Subject` → `{!inputMotivo}`
   - `Description` → `{!inputProblema}`
   - `Origin` → `Web`
   - `Status` → `New`
   - **¡ATENCIÓN A ESTE:!** Busca el campo `ContactId`. En valor, borra y ve buscando: `$User` (Variable Global Usuario) → `ContactId`. Quedará así: `{!$User.ContactId}`. *(Esto vincula al caso con el alumno que tiene sesión iniciada).*
5. Guarda el flow como `Reclamo de Alumnado` y actívalo.

### Paso 2: Publicar en área privada
1. Ve al **Experience Builder**.
2. Dale click al título de la página arriba en el centro, y luego en el menú emergente, abajo dale a **+ New Page** -> Standard Page -> Flexible Layout. Llámala `Trámites`.
3. Notarás que el candado de esa página dice "Page Access: Default". Como es privada por defecto, déjalo así.
4. Arrastra el componente de **Flow**, suéltalo, selecciona tu Flow `Reclamo de Alumnado`.
5. **Publish.**

---

## 📚 HU-S3-05: Gestión de Contenido (Knowledge)

### Paso 1: Armar las carpetas (Data Categories)
1. **Setup** → Quick Find → `Data Category Setup`.
2. Completa los detalles del grupo: Group Name: `Temas Lumina`, Group Unique Name: `Temas_Lumina`. Guarda.
3. Abajo, en Categories, pulsa Actions (Add Child Category) en la de nivel superior ("All"). Crea: `Academico`, `Administrativo`.
4. Arriba del todo, haz clic en **Activate**. *(Si no activas las Data Categories, ningún artículo te las mostrará).*

### Paso 2: Crear el Artículo
1. Ve al **App Launcher** (matriz de puntos a la izquierda) y abre la aplicación normal "Service" o busca **Knowledge**.
2. En la pestaña Knowledge haz clic en **New**.
3. Title: `¿Cuál es la escala de calificaciones?`
4. Escribe la respuesta clara en el cuerpo.
5. **CRÍTICO - Sección de visibilidad:** Busca unas casillas llamadas "Visible In Public Knowledge Base" y "Visible to Customer". **Marca AMBAS.** *(Si omites este check, el portal no mostrará el texto).*
6. Guárdalo y luego a la derecha haz click en **Publish** (¡Publicar!)

### Paso 3: Verlo en el Portal
1. Vuelve al **Experience Builder**.
2. En el panel de componentes (⚡), busca algo llamado "Article List" o "Trending Articles" o "Global Search for Peer-to-Peer Communities". Cualquiera de ellos.
3. Arrástralo a la página de Home. Verás unas barras grises (preview).
4. Dale a **Publish**. ¡Abre el sitio como anónimo y prueba a buscar las FAQ!

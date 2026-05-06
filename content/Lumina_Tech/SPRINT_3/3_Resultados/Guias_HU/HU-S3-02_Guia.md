# 🔄 GUÍA DE IMPLEMENTACIÓN: HU-S3-02
**Nombre:** Screen Flow Público (Captación de Leads)
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce (aprendices)
**Herramientas:** Setup → Flows + Experience Builder (Guest User Profile)

> [!IMPORTANT]
> **Pre-requisitos:**
> - **HU-S3-01 completada:** El sitio de Experience Cloud ("Campus Virtual Lumina Tech") debe estar creado y su nivel de acceso público habilitado (Public can access the site).
> - El objeto estándar `Lead` (Prospectos) debe estar visible/habilitado en la organización.

---

## 🧭 ¿Qué vas a construir?

Un formulario público para que prospectos sin cuenta en el sitio puedan dejar sus datos de forma anónima desde internet. Ese formulario se conectará directamente con Salesforce para crear un Prospecto (`Lead`).
1. Crear un Screen Flow de captura (con configuración manual de variables y pantalla de éxito).
2. Crear un camino de error (Fault Path).
3. Habilitar permisos requeridos en el **Perfil de Usuario Invitado** (Guest User) para que pueda acceder el flujo y guardar los `Leads`.
4. Publicar el Flow en la página de inicio (Home) del sitio abierto al público.

---

### Paso 1: Crear el Screen Flow Base
1. En Setup, escribe `Flows` en el Quick Find → haz clic en **Flows** → botón **New Flow**.
2. Selecciona **Screen Flow** y haz clic en **Create**.
*(En la versión actual de Salesforce, el lienzo de Auto-Layout se abre de forma automática con un punto de inicio `+`).*

---

### Paso 2: Crear la Pantalla 1 — Datos del Prospecto
1. En el lienzo, haz clic en el ícono **+** y selecciona **Screen**.
2. En la propiedad derecha, establece el **Label:** `Tus Datos`.
3. Desde el panel izquierdo de Componentes (⚡), agrega en orden:
   - Componente **Name** (Nombre).
     - **API Name:** `inputNombre`
   - Componente **Email**.
     - **API Name:** `inputEmail`
     - Localiza el toggle de **Required** debajo y pásalo a **`{!$GlobalConstant.True}`**.
   - Componente **Phone** (Teléfono).
     - **API Name:** `inputCelular`
     - Pasa el toggle de **Required** a **`{!$GlobalConstant.True}`**.
4. Haz clic en **Done**.

---

### Paso 3: Crear el Registro en Salesforce (Lead)
1. En el lienzo, haz clic en el **+** debajo del nodo de la Pantalla "Tus Datos" y selecciona el elemento **Create Records**.
2. Configura sus propiedades base de esta forma:
   - **Label:** `Crear Lead Prospecto`
   - **How to set the record fields:** Selecciona **`Manually`** *(la opción obligatoria en versiones modernas, reemplaza al antiguo "Use separate resources")*.
   - **Create a Record of This Object:** Escribe y selecciona `Lead`.
3. Mapeo de campos (usa el botón **+ Add Field**):
   - `LeadSource` ← Valor literal, escribe: `Web`
   - `Company` ← Valor literal, escribe: `Prospecto Web Lumina Tech` *(Campo requerido estándar por Salesforce, sino fallará).*
   - `FirstName` ← Busca la sección Screen Components > clica `inputNombre` > elige `First Name`.
   - `LastName` ← Busca Screen Components > clica `inputNombre` > elige `Last Name`.
   - `Email` ← Busca Screen Components > clica `inputEmail` > elige `Value`.
   - `Phone` ← Busca Screen Components > clica `inputCelular` > elige `Value`.
4. Haz clic en **Done**.

---

### Paso 4: Pantalla de Éxito y de Error (Fault Path)
1. **Éxito:** Haz clic en el **+** debajo del último elemento y selecciona **Screen**.
   - **Label:** `Confirmacion Exitosa`
   - Arrastra un componente **Display Text** y asiga **API Name:** `mensajeExito`.
   - Mensaje: `✅ ¡Gracias por tu interés en Lumina Tech! Nos comunicaremos a la brevedad a tu correo {!inputEmail.value}.` *(Puedes usar el botón "Insert a resource" `{!}` para colocar el valor del email de forma dinámica).*
   - Haz clic en **Done**.

2. **Error (Fault Path):** Haz clic DE NUEVO directamente sobre el elemento rosado `Crear Lead Prospecto` en el lienzo. 
   - Busca el botón o menú de tres puntos `⋮` y selecciona **Add Fault Path**.
   - En la nueva línea punteada paralela, haz clic en el **+** y agrega un **Screen**.
   - **Label:** `Pantalla Error`
   - Arrastra un **Display Text** (API Name: `mensajeError`).
   - Mensaje: `Ups, ocurrió un problema. Por favor intenta nuevamente. Error técnico: {!$Flow.FaultMessage}` *(Busca la var Global de Flow para Fault Message)*.
   - Haz clic en **Done**.

### Paso 5: Guardar y Activar el Flujo
1. Haz clic en el botón superior derecho **Save**.
2. Aparece el modal Properties:
   - **Flow Label:** `Lumina EC Captacion Futuro Alumno`
   - **Flow API Name:** `Lumina_EC_Captacion_Futuro_Alumno`
3. Haz clic en **Save**, y luego fundamentalmente en **Activate**.

---

### Paso 6: Configurar Permisos del Guest User (Crítico de Seguridad)
Los visitantes sin sesión actúan como "Usuario Invitado". Si este usuario no tiene permisos estrictos sobre el Flujo y el Objeto Lead, la integración fallará discretamente.

1. En Setup, escribe `All Sites` → **All Sites**.
2. En la fila de tu sitio, haz clic en el botón **Builder**.
3. En la barra superior izquierda (engranaje), ve a **⚙️ Settings** → pestaña **General**.
4. Haz clic en el link azul que aparece debajo de **Guest User Profile** (usualmente dirá *"Campus Virtual Profile"* o *"Lumina Tech Profile"* con el subtipo Guest).
5. Se abrirá la página clásica de Administración del perfil. Haz clic en **Edit**.
6. Desplázate hacia abajo hasta **Standard Object Permissions**. Busca el objeto **Leads**.
7. Activa las casillas ✅ **Read** y ✅ **Create** para Leads. (Ve hasta el fondo y dale **Save**).
8. En la misma pantalla del perfil visualizando todo el sumario, ve hacia abajo al hipervínculo **Flow Access** (o pon `Ctrl+F` y Flow Access) → haz clic en **Edit**.
9. Mueve el flujo `Lumina_EC_Captacion_Futuro_Alumno` desde la columna "Available" hacia **"Enabled"**. Haz clic en **Save**.

> [!WARNING]
> La falta del permiso **Create en Leads** impedirá grabar los leads en Salesforce, arrojando al usuario ciego a la Pantalla de Error o devolviento un modal en blanco. Esto es siempre la falla N#1 en la captación de Portales. 

---

### Paso 7: Publicar en la Página de Experience Builder
1. Regresa a tu pestaña de **Experience Builder** del sitio.
2. Comprueba que estás en la página predeterminada: **Home** / **Inicio**.
3. Haz clic en el panel superior izquierdo de componentes (el ícono ⚡).
4. Busca `Flow` y arrástralo a voluntad en un área destacada (por ejemplo debajo del encabezado principal).
5. Selecciona el componente posicionado, en el panel de configuración derecho en **Flow**, elige: `Lumina EC Captacion Futuro Alumno`.
6. Presiona el botón derecho superior **Publish** y confírmalo.

---

### ✅ Checklist de Resultado Profesional — QA Completo

| # | Prueba | Cómo verificar | Resultado Esperado |
|:---:|:---|:---|:---|
| 1 | **Permisos Guest User** | Setup → Guest User Profile de la Comunidad | Permisos Objeto Lead: *Read/Create* ✅, Flow Access de Captación: *Enabled* ✅ |
| 2 | **Visible sin Sesión** | Abrir la URL del sitio (`.my.site.com`) en modo navegación de incógnito. | Se carga la página e incluye inmediatamente el Screen de "Tus Datos" listo. |
| 3 | **Prueba negativa/Obligatoriedad** | En incógnito, llena el nombre pero **deja vacío el Apellido o el Email** y pulsa Next. | El Flow no avanza y marca el campo con un aviso rojo pidiendo ser completado. |
| 4 | **Sometimiento Correcto** | En incógnito, llena los datos de ejemplo: "Juan Prospecto" y pulsa Siguiente. | El formulario reemplaza a la Screen Final de Confirmación Exitosa. |
| 5 | **Validación de Base de Datos**| Admin → App Launcher → objeto `Leads` (Prospectos) | Existe "Juan Prospecto". Fuente: `Web`, Compañía: `Prospecto Web Lumina Tech`. |

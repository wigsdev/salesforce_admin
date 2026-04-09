# 🔄 GUÍA DE IMPLEMENTACIÓN: HU-S3-02
**Nombre:** Screen Flow Público (Captación de Leads)
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce

### Paso 1: Construir el Flow
1. **Setup** → Escribe `Flows` → **New Flow** → Selecciona **Screen Flow** → Create.
2. Haz clic en el botón `+` y agrega un elemento **Screen**. Lámalo "Datos".
   - Arrastra el componente **Name** (Nombre y Apellido). API name `inputNombre`.
   - Arrastra el componente **Email** (Correo). API name `inputEmail`.
   - Arrastra el componente **Phone** (Celular). API name `inputCelular`.
   - Haz clic en **Done**.
3. Haz clic en el `+` después de la pantalla y agrega el elemento de datos **Create Records**.
   - Label: `Crear Lead`.
   - Selecciona "Use separate resources, and literal values".
   - Object: `Lead`.
   - Mapeo de campos:
     - `FirstName` → `{!inputNombre.firstName}`
     - `LastName` → `{!inputNombre.lastName}`
     - `Company` → Escribe el texto directo: `Prospecto Web Lumina Tech`.
     - `LeadSource` → Escribe el texto directo: `Web`.
     - `Email` → `{!inputEmail.value}`
     - `Phone` → `{!inputCelular.value}`
4. Agrega una pantalla final con el elemento **Display Text**. Escribe "Gracias por tu interés, nos comunicaremos contigo a la brevedad". Guarda el flow, llámalo `Captacion Futuro Alumno` y dale **Activate**.

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

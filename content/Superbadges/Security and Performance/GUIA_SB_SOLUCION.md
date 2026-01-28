# Guía de Solución: Security and Performance Superbadge

## 🚀 Reto 1: Rastreo de Canciones (Big Objects)
Vamos a crear un "Big Object" para guardar mucha información histórica.

### Paso 1: Crear el Objeto
1. Ve a **Setup** (Configuración).
2. En el buscador rápido (arriba a la izquierda), escribe **Big Objects** y selecciona la opción.
3. Haz clic en el botón **New** (Nuevo).
4. Rellena estos datos:
    * **Label**: Play Tracker
    * **Plural Label**: Play Trackers
    * **Object Name**: Play_Tracker
    * **Description**: Tracks song plays
5. Haz clic en **Save** (Guardar).

### Paso 2: Crear los Campos
Ahora baja a la sección **Custom Fields & Relationships** y crea los siguientes campos uno por uno.

**Campo 1: Song**
* **Tipo**: Lookup Relationship -> Relacionado con: Song.
* **Nombre**: Song
* ⚠️ **Importante**: Marca la casilla **Required** (Obligatorio).
* **Guardar y Nuevo**.

**Campo 2: Account**
* **Tipo**: Lookup Relationship -> Relacionado con: Account.
* **Nombre**: Account
* ⚠️ **Importante**: Marca la casilla **Required** (Obligatorio).
* **Guardar y Nuevo**.

**Campo 3: Play Date**
* **Tipo**: Date/Time.
* **Nombre**: Play_Date
* ⚠️ **Importante**: Marca la casilla **Required** (Obligatorio).
* **Guardar y Nuevo**.

**Campo 4: Start Date**
* **Tipo**: Date/Time.
* **Nombre**: Start_Date
* ⚠️ **Importante**: Marca la casilla **Required** (Obligatorio).
* **Guardar y Nuevo**.

**Campo 5: End Date**
* **Tipo**: Date/Time.
* **Nombre**: End_Date
* ⚠️ **Importante**: Marca la casilla **Required** (Obligatorio).
* **Guardar y Nuevo**.

**Campo 6: Number of Plays**
* **Tipo**: Number.
* **Longitud**: 18, Decimales: 0.
* **Nombre**: Number_of_Plays
* ⚠️ **Importante**: Marca la casilla **Required** (Obligatorio).
* **Guardar y Nuevo**.

**Campo 7: Device**
* **Tipo**: Text.
* **Longitud**: 60.
* **Nombre**: Device.
* (No es obligatorio). **Guardar y Nuevo**.

**Campo 8: OS**
* **Tipo**: Text.
* **Longitud**: 60.
* **Nombre**: OS.
* (No es obligatorio). Haz clic en **Save**.

### Paso 3: Crear el Índice (El orden es vital)
En la misma pantalla del objeto Play Tracker, baja a la sección **Index** y haz clic en **New**.

* **Nombre del índice**: Play_Tracker_Index.

Configura las filas en este orden exacto:
1. **Posición 1**: Selecciona `Song__c` (Dirección: Ascending).
2. **Posición 2**: Selecciona `Account__c` (Dirección: Ascending).
3. **Posición 3**: Selecciona `Play_Date__c` (Dirección: Ascending).

Haz clic en **Save**.

### Paso 4: Activar el Objeto
1. Sube al principio de la página del objeto Play Tracker.
2. Haz clic en **Edit** (al lado del nombre del objeto).
3. Cambia el **Deployment Status** a **Deployed** (Implementado).
4. Haz clic en **Save**.

---

## 🚀 Reto 2: Datos de Ventas de Entradas (External Objects)
Vamos a conectar Salesforce con una base de datos externa.

### Paso 1: Configurar la Conexión
1. Ve a **Setup** y busca **External Data Sources**.
2. Haz clic en **New External Data Source**.
3. Rellena:
    * **Label**: Performances
    * **Name**: Performances
    * **Type**: Salesforce Connect: OData 4.0
    * **URL**: `https://security-performance-33i1n3.5sc6y6-2.usa-e2.cloudhub.io/api`
    * ⚠️ **Casilla "Request Row Counts"**: Asegúrate de que esté **DESMARCADA** (Vacía).
4. Haz clic en **Save**.

### Paso 2: Sincronizar
1. Haz clic en el botón **Validate and Sync**.
2. Marca la casilla ✅ al lado de la tabla **Performances**.
3. Haz clic en el botón **Sync**.

### Paso 3: Configurar el Objeto
1. Ve a **Setup** y busca **External Objects**.
2. Haz clic en el nombre **Performances**.
3. Haz clic en **Edit**.
4. Cambia el **Deployment Status** a **Deployed**.
5. Baja y marca la casilla ✅ **Allow Reports** (Permitir informes).
6. Haz clic en **Save**.

### Paso 4: Crear una Pestaña (Truco para que aparezca)
1. Ve a **Setup** y busca **Tabs**.
2. En "Custom Object Tabs", haz clic en **New**.
3. En "Object", selecciona **Performances**.
4. Elige cualquier icono y dale a **Next**, **Next** y **Save**.

### Paso 5: Dar Permisos
1. Ve a **Setup** y busca **Profiles**.
2. Entra en **System Administrator**.
3. Haz clic en **Object Settings** (o busca permisos de objeto si estás en la vista clásica).
4. Busca **Performances** y asegúrate de que tenga permiso de **Read** (Leer).

### Paso 6: Crear el Informe
1. Ve a la aplicación (**App Launcher**) y entra en la pestaña **Reports**.
2. **Crear Carpeta**: Haz clic en **New Folder**, llámala `Ticketing Reports` y guarda.
3. **Crear Informe**: Haz clic en **New Report**.
4. Busca y selecciona el tipo **Performances**.
5. Dale a **Start Report**.
6. **Configurar**:
    * Pestaña **Filters**: Pon la fecha (Date) en **All Time**.
    * Pestaña **Outline** (Columnas): Agrega **TODOS** los campos que veas en la lista izquierda (City, Venue, Capacity, Tickets Sold, Tickets Available, Performance Name, etc.).
7. **Guardar**:
    * Dale a **Save & Run**.
    * **Nombre**: Ticket Tracking.
    * **Carpeta**: Selecciona `Ticketing Reports`.
8. Guardar.

---

## 🚀 Reto 3: Privacidad del Fan (Seguridad)
Vamos a proteger datos sensibles en el objeto Contacto.

### Paso 1: Crear Campo Encriptado "Fan Number"
1. Ve a **Setup > Object Manager > Contact**.
2. Ve a **Fields & Relationships** y dale a **New**.
3. Elige **Text (Encrypted)** y dale a **Next**.
4. Rellena:
    * **Label**: Fan Number
    * **Length**: 18
    * **Mask Type**: Last 4 characters clear (Los últimos 4 visibles).
    * **Mask Character**: X
    * **Name**: Fan_Number
    * **Description**: Fan ID (Pon cualquier texto).
5. Dale a **Next**.
6. **Permisos (Importante)**:
    * Primero desmarca la casilla "Visible" del encabezado para limpiar todo.
    * Ahora marca "Visible" SOLO para: **System Administrator** y **Standard User**.
7. Dale a **Next** y **Save**.

### Paso 2: Clasificar Datos Confidenciales
Sigue en **Contact > Fields & Relationships**. Tienes que editar 4 campos.

**Campo 1: Email**
* Busca Email, dale a **Edit**.
* En "Data Sensitivity Level" selecciona: **Confidential**.
* En "Compliance Categorization" selecciona: **PII**.
* **Guardar**.

**Campo 2: Birthdate**
* Busca Birthdate, dale a **Edit**.
* En "Data Sensitivity Level" selecciona: **Confidential**.
* En "Compliance Categorization" selecciona: **PII**.
* **Guardar**.

**Campo 3: Gender Identity**
* Busca Gender Identity, dale a **Edit**.
* En "Data Sensitivity Level" selecciona: **Confidential**.
* En "Compliance Categorization" selecciona: **PII**.
* **Guardar**.

**Campo 4: Pronouns**
* Busca Pronouns, dale a **Edit**.
* En "Data Sensitivity Level" selecciona: **Confidential**.
* En "Compliance Categorization" selecciona: **PII**.
* **Guardar**.
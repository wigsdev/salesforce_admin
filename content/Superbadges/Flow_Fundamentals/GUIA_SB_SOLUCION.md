# Guía de Solución Técnica: Flow Fundamentals Superbadge Unit

**Rol:** Salesforce Solution Architect
**Objetivo:** Implementar mejoras de automatización para Dreamscape Bookshops utilizando Salesforce Flow.
**Alcance:** Automatización de tareas de cumplimiento, personalización de comunicaciones y actualización de programas de lealtad.

---

## Reto 1: Automatización de Pedidos (Book Order Giveaway)

**Objetivo de Negocio:**
Modificar el flujo `Book Order` para generar tareas automáticas para el equipo de cumplimiento ("Fulfillment Team") basadas en la cantidad de libros de la orden.

### Paso 1: Configuración de Recursos
1. Abrir el flujo **Book Order**.
2. Crear un **Nuevo Recurso** para la fecha de vencimiento:
   * **Resource Type:** Formula
   * **API Name:** `DueDate`
   * **Data Type:** Date
   * **Formula:** `{!$Flow.CurrentDate} + 1`

### Paso 2: Verificación de Datos (Queue)
*Nota: El elemento `Get Records for Queue` ya debería existir al inicio del flujo. Verificar su configuración:*
* **Element:** Get Records
* **Label:** `Get Records for Queue`
* **Object:** Group
* **Filter:** `Type` Equals `Queue` AND `Name` Equals `Fulfillment Team`
* **Store:** Only the first record.

### Paso 3: Lógica de Decisión
Ubicar el elemento **Decision** al final del flujo (después del subflujo `Create QA Task` o equivalente).

* **Element:** Decision
* **Label:** `How Many Books in the Order?`
* **API Name:** `How_Many_Books_in_the_Order`
* **Outcome 1 Label:** `3 or 4 Books`
   * **Condition Requirements:** **Any Condition is Met (OR)**
   * **Condition A:** `{!Book_Order.Book_Count__c}` Equals `3`
   * **Condition B:** `{!Book_Order.Book_Count__c}` Equals `4`
* **Outcome 2 Label:** `5 or More Books`
   * **Condition Requirements:** **All Conditions Are Met (AND)**
   * **Condition:** `{!Book_Order.Book_Count__c}` Greater Than or Equal `5`
* **Default Outcome:** Renombrar a `Less than 3`.

### Paso 4: Creación de Tareas
Agregar elementos **Create Records** en cada ruta de la decisión.

**Ruta "3 or 4 Books":**
* **Element:** Create Records
* **Label:** `Create Task Bookmark`
* **How to Set Record Fields:** Use separate resources, and literal values.
* **Object:** Task
* **Field Values:**
   * `Subject`: `Add Bookmark`
   * `ActivityDate`: `{!DueDate}`
   * `OwnerId`: `{!Get_Records_for_Queue.Id}`
   * `WhatId`: `{!Book_Order.Id}`

**Ruta "5 or More Books":**
* **Element:** Create Records
* **Label:** `Create Task Bookmark and Sticker`
* **How to Set Record Fields:** Use separate resources, and literal values.
* **Object:** Task
* **Field Values:**
   * `Subject`: `Add Bookmark and Sticker`
   * `ActivityDate`: `{!DueDate}`
   * `OwnerId`: `{!Get_Records_for_Queue.Id}`
   * `WhatId`: `{!Book_Order.Id}`

---

## Reto 2: Personalización de Correo (Recommendation Email)

**Objetivo de Negocio:**
Mejorar el flujo de pantalla `Recommendation Email` para personalizar el contenido y registrar la fecha del último contacto.

### Paso 1: Edición de Plantilla de Texto
1. Abrir el flujo **Recommendation Email**.
2. Ir a la pestaña **Manager** y editar el recurso **Text Template** llamado `EmailBody`.
3. **CRÍTICO:** Cambiar el editor de "View as Rich Text" a **"View as Plain Text"**. Borrar todo el contenido previo.
4. Configurar el cuerpo del mensaje:
   * **Primera línea:** `Hi {!Get_Customer_Info.FirstName},`
   * **Cuerpo:** Agregar detalles del libro usando los recursos `{!Get_Customer_Info.Current_Recommendation__r.Name}`, `Author__c`, y `Summary__c`.

### Paso 2: Actualización del Contacto
Agregar la lógica antes de la acción de envío de correo o inmediatamente después.

1. **Element:** Assignment
   * **Label:** `Set Last Outreach Date`
   * **Set Variable Values:**
     * **Variable:** `{!Get_Customer_Info.Last_Outreach__c}`
     * **Operator:** Equals
     * **Value:** `{!$Flow.CurrentDateTime}`

2. **Element:** Update Records
   * **Label:** `Update Contact`
   * **How to Find Records:** Use the IDs and all field values from a record or record collection.
   * **Select Record:** `{!Get_Customer_Info}`

### Paso 3: Pantalla de Confirmación
Agregar como el **último elemento** del flujo.

* **Element:** Screen
* **Label:** `Confirmation Screen`
* **API Name:** `Confirmation_Screen`
* **Component:** Display Text
   * **Name:** `SuccessMessage`
   * **Content:** `Your email has been sent`

---

## Reto 3: Programa de Lealtad (Birthday Loyalty Points Update)

**Objetivo de Negocio:**
Actualizar el flujo `Birthday Loyalty Points Update` para otorgar puntos de bonificación en cumpleaños basados en el nivel de lealtad.

### Paso 1: Configuración de Fórmula
1. Abrir el flujo **Birthday Loyalty Points Update**.
2. Crear un **Nuevo Recurso**:
   * **Resource Type:** Formula
   * **API Name:** `NewLoyaltyPoints`
   * **Data Type:** Number (0 decimales)
   * **Formula:**
     ```
     Case ({!Loop_Through_Contacts.Loyalty_Status__c},
     'Bronze',{!Loop_Through_Contacts.Loyalty_Points__c} + 100,
     'Silver', {!Loop_Through_Contacts.Loyalty_Points__c} + 250,
     'Gold', {!Loop_Through_Contacts.Loyalty_Points__c} + 500,
     {!Loop_Through_Contacts.Loyalty_Points__c} )
     ```

### Paso 2: Lógica dentro del Bucle (Loop)
Trabajar dentro del bucle existente `Loop_Through_Contacts`.

1. **Element:** Assignment
   * **Label:** `Assign New Points`
   * **Set Variable Values:**
     * **Variable:** `{!Loop_Through_Contacts.Loyalty_Points__c}`
     * **Operator:** Equals
     * **Value:** `{!NewLoyaltyPoints}`

2. **Element:** Update Records
   * **Ubicación:** Dentro del bucle, justo después de la asignación.
   * **Label:** `Update Contact Points`
   * **How to Find Records:** Use the IDs and all field values from a record or record collection.
   * **Select Record:** `{!Loop_Through_Contacts}`

---

**Nota Final:** Recuerda hacer clic en **"Save As New Version"** y luego en **"Activate"** para cada flujo antes de verificar el reto en Trailhead.
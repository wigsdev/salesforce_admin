# Guía de Implementación: HU-S3-04c
## Record-Triggered Flow para Enrutamiento de Casos (Before-Save) con Colas

Esta guía detalla el paso a paso arquitectónicamente correcto (Enterprise Grade) para construir la lógica de enrutamiento automático de los Casos generados por los alumnos en Lumina Tech. Evitaremos el uso de "User IDs" fijos y utilizaremos **Colas (Queues)**.

---

### 👤 Paso 0: Crear los Usuarios Responsables
Antes de crear las colas, asegúrate de tener a los usuarios correspondientes.
1. Ve a **Setup → Users → Users** y haz clic en **New User**.
2. **Crear Secretaría Académica:**
   * **First Name:** `Marta` | **Last Name:** `Gómez`
   * **Email:** *(Usa tu correo con un +, ej. tu_correo+marta@gmail.com)* | **Username:** *(Igual que el email)* | **Nickname:** `mgomez`
   * **User License:** `Salesforce` | **Profile:** `Standard User`
   * Haz clic en **Save & New**.
3. **Crear Director de Carrera:**
   * **First Name:** `Roberto` | **Last Name:** `Alonso`
   * **Email:** *(Usa tu correo con un +, ej. tu_correo+roberto@gmail.com)* | **Username:** *(Igual que el email)* | **Nickname:** `ralonso`
   * **User License:** `Salesforce` | **Profile:** `Standard User`
   * Haz clic en **Save**.

> 💡 **Nota sobre Límites de Licencias (Developer Edition):**  
> Las orgs de desarrollo gratuitas solo incluyen 2 licencias tipo `Salesforce`. Si al intentar crear estos usuarios te aparece un error indicando que no hay licencias disponibles, **es normal**. A modo de práctica, puedes usar los usuarios que ya tengas creados (como el tuyo de Administrador) y asociar esos a ambas Colas para probar el funcionamiento del Flow, o cambiarles el nombre temporalmente a los usuarios existentes.

---

### 🏢 Paso 1: Crear las Colas (Queues)
En lugar de asignar casos a personas, los asignaremos a Colas.
1. Ve a **Setup → Queues** y haz clic en **New**.
2. **Cola Académica:**
   * **Label:** `Cola Academica` | **Queue Name:** `Cola_Academica`
   * **Supported Objects:** Selecciona `Case` y muévelo a "Selected Objects".
   * **Queue Members:** Busca en "Users" y agrega a **Roberto Alonso**.
   * Haz clic en **Save**.
3. **Cola Administrativa:**
   * Haz clic en **New** nuevamente.
   * **Label:** `Cola Administrativa` | **Queue Name:** `Cola_Administrativa`
   * **Supported Objects:** Selecciona `Case`.
   * **Queue Members:** Busca en "Users" y agrega a **Marta Gómez**.
   * Haz clic en **Save**.

---

### ⚙️ Paso 2: Crear el Flow (Before-Save)
1. Ve a **Setup → Flows** y haz clic en **New Flow**.
2. Selecciona **Record-Triggered Flow** y haz clic en **Create**.
3. En el panel inicial:
   * **Object:** `Case`
   * **Trigger the Flow When:** `A record is created`
   * **Optimize the Flow for:** Selecciona **`Fast Field Updates`** (Before-Save).
4. Cierra el panel.

---

### 🔀 Paso 3: El Elemento Decision
1. Bajo el nodo de inicio, haz clic en **`+`** y selecciona **Decision**.
2. **Label:** `¿Es solicitud académica?`
3. En la primera ruta (**Sí, es Académica**):
   * **Condition Requirements:** `Any Condition Is Met (OR)`
   * Condición 1: `{!$Record.Subject}` | `Contains` | `Nota`
   * Condición 2: `{!$Record.Subject}` | `Contains` | `Consulta academica`
4. En **Default Outcome**, cambia el nombre a: `No, es Administrativa`.
5. Haz clic en **Done**.

---

### 🔍 Paso 4: Obtener la Cola Académica (Ruta "Sí")
1. Bajo la ruta **"Sí, es Académica"**, haz clic en **`+`** y selecciona **Get Records**.
2. **Label:** `Obtener Cola Academica`
3. **Object:** `Group` *(En Salesforce, las Queues se almacenan en el objeto Group).*
4. **Filter Group Records:**
   * **Condition Requirements:** `All Conditions Are Met (AND)`
   * Campo: `Type` | Operador: `Equals` | Valor: `Queue`
   * *(Haz clic en Add Condition)*
   * Campo: `DeveloperName` | Operador: `Equals` | Valor: `Cola_Academica`
5. **How Many Records to Store:** `Only the first record`.
6. Haz clic en **Done**.

### 🎯 Paso 5: Asignar Prioridad y Dueño Académico
1. Debajo del elemento "Obtener Cola Academica", haz clic en **`+`** y selecciona **Assignment**.
2. **Label:** `Asignar Alta y Cola Academica`
3. Variables:
   * `{!$Record.Priority}` | `Equals` | `High`
   * `{!$Record.OwnerId}` | `Equals` | `{!Obtener_Cola_Academica.Id}` *(El ID dinámico extraído de la cola)*.
4. Haz clic en **Done**.

---

### 🔍 Paso 6: Obtener la Cola Administrativa (Ruta "No")
1. Bajo la ruta **"No, es Administrativa"**, haz clic en **`+`** y selecciona **Get Records**.
2. **Label:** `Obtener Cola Administrativa`
3. **Object:** `Group`
4. **Filter Group Records:**
   * **Condition Requirements:** `All Conditions Are Met (AND)`
   * Campo: `Type` | Operador: `Equals` | Valor: `Queue`
   * *(Haz clic en Add Condition)*
   * Campo: `DeveloperName` | Operador: `Equals` | Valor: `Cola_Administrativa`
5. Haz clic en **Done**.

### 🎯 Paso 7: Asignar Prioridad y Dueño Administrativo
1. Debajo del elemento "Obtener Cola Administrativa", haz clic en **`+`** y selecciona **Assignment**.
2. **Label:** `Asignar Media y Cola Administrativa`
3. Variables:
   * `{!$Record.Priority}` | `Equals` | `Medium`
   * `{!$Record.OwnerId}` | `Equals` | `{!Obtener_Cola_Administrativa.Id}`
4. Haz clic en **Done**.

---

### 💾 Paso 8: Guardar y Activar
1. Haz clic en **Save**. **Flow Label:** `Lumina Casos Before-Save Routing`.
2. Haz clic en **Activate**.

---

### 🧪 Paso 9: Prueba (QA)
1. Ve a tu portal de Experience Cloud en modo incógnito e inicia sesión como alumno (Lucas).
2. Usa el Screen Flow para enviar un "Certificado de alumno regular".
3. Ve a tu org de Salesforce y busca el Caso.
4. **Validación:** Verifica que la **Priority** dice `High` y que el **Case Owner** es `Cola Academica`. *(Si Roberto inicia sesión, podrá ver el caso en la vista de lista de esa cola y tomar posesión de él).*

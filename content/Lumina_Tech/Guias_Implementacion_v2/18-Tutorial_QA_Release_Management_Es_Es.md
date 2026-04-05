# 🛠️ Guía Técnica: QA & Release Management [SPRINT 2]

**Sprint**: 02 (Estabilización de Entorno y Validación de Datos)
**Rol Responsable**: 🧪 **Tester QA** / 🛡️ **Salesforce Admin**

---

## 🎯 Objetivo

Garantizar que todos los cambios de configuración realizados en el entorno del **Grupo 6** pasen por un ciclo de validación riguroso antes de considerarse "listos para producción". Esta guía cubre el proceso completo de:

1. **Pre-QA Gate** — Verificación del entorno antes de importar datos.
2. **Smoke Testing** — Pruebas rápidas de integridad post-instalación.
3. **Ciclo de QA Funcional** — Validación de cada Historia de Usuario.
4. **Release Management** — Sincronización de entornos y despliegue seguro.
5. **Criterios de Cierre (Definition of Done)** — ¿Cuándo un Sprint está "cerrado"?

---

## ⚙️ Fase 0: Preparación del Entorno QA

*Antes de ejecutar cualquier prueba, el Admin debe confirmar que el entorno está estable.*

**Rol:** 🛡️ Administrador Salesforce  
**Herramienta:** `Salesforce Setup`

### Pasos:

1. **Acceder a Setup:** Haga clic en el ícono ⚙️ (engranaje) en la esquina superior derecha de Salesforce → seleccione **Setup**.
2. **Verificar Entorno Activo:** En el banner superior de Salesforce, verifique que dice **Developer Edition** (NO una Sandbox real). El nombre de la org debe incluir el identificador del equipo (ej: `lumina-grupo6-dev`).
3. **Habilitar Lightning Experience:** Vaya a `Setup > Lightning Experience > Migrar a Lightning`. Si ya está activo, continúe.
4. **Confirmar Límites de Storage:** Navegue a `Setup > Company Information`. En la sección "Storage Usage", valide que el espacio utilizado es **menor al 80%** antes de cualquier carga masiva. Si supera ese umbral, ejecute una limpieza de datos de prueba anteriores.
5. **Verificar que no hay Deploy Jobs activos:** En `Setup > Deployment Settings`, confirme que no hay ningún proceso de despliegue en cola. Si hay uno en estado "Pending", espere a que concluya antes de continuar.

---

## 🔍 Fase 1: Pre-QA Gate (Checklist de Metadatos)

*Antes de mover la configuración al entorno QA oficial, el Tester valida que los metadatos son correctos.*

**Rol:** 🧪 Tester QA  
**Herramienta:** `Salesforce Setup > Object Manager`

### 1.1 Validación de Objetos y Campos Críticos

Para cada objeto listado en la tabla, navegar a `Setup > Object Manager > [Nombre del Objeto] > Fields & Relationships` y verificar que los campos existen con la configuración indicada:

| Objeto | Campo API Name | Tipo | ¿Unique? | ¿External ID? |
|---|---|---|---|---|
| `Contact` | `Numero_Documento__c` | Text(20) | ✅ Sí | ✅ Sí |
| `Carrera__c` | `Abreviatura__c` | Text(10) | ✅ Sí | ✅ Sí |
| `Materia__c` | `Codigo_Materia__c` | Text(20) | ✅ Sí | ✅ Sí |
| `Inscripcion__c` | `ID_Importacion__c` | Text(100) | ✅ Sí | ✅ Sí |
| `Evaluacion__c` | `ID_Evaluacion__c` | Text(150) | ✅ Sí | ✅ Sí |

**Cómo verificar:** En la lista de campos, localice cada campo. En la columna "Field Name" haga clic sobre él. En los atributos, confirme que los checkboxes **Unique** y **External ID** están marcados.

> [!CAUTION]
> Si ANY de estos campos no tiene el tilde de **External ID**, el UPSERT del Data Loader fallará con el error `DUPLICATE_EXTERNAL_ID`. Corrija el campo antes de continuar.

### 1.2 Validación de Relaciones (Estructura Padre-Hijo)

En `Setup > Object Manager`, para cada relación, haga clic en el campo de tipo `Lookup` o `Master-Detail` y verifique que apunta al objeto correcto:

| Objeto Hijo | Campo Relación | Objeto Padre | Tipo Relación |
|---|---|---|---|
| `Materia__c` | `Carrera__c` | `Carrera__c` | Lookup / Master-Detail |
| `Inscripcion__c` | `Alumno__c` | `Contact` | Lookup |
| `Inscripcion__c` | `Materia__c` | `Materia__c` | Lookup |
| `Evaluacion__c` | `Inscripcion__c` | `Inscripcion__c` | Lookup / Master-Detail |
| `Asistencia__c` | `Inscripcion__c` | `Inscripcion__c` | Lookup |
| `Cobro__c` | `Alumno__c` | `Contact` | Lookup |

**⛔ Regla de Oro:** Nunca cargue datos en un objeto **hijo** si el objeto **padre** no contiene registros. El Data Loader arrojará el error: `FIELD_INTEGRITY_EXCEPTION: Contact ID: id value of incorrect type`.

### 1.3 Validación de Perfiles y Permisos

1. Ir a `Setup > Profiles`.
2. Seleccionar el perfil **Standard User** (o el equivalente del Grupo 6).
3. Hacer clic en **Object Settings**.
4. Para cada objeto personalizado (`Carrera__c`, `Materia__c`, `Inscripcion__c`, `Evaluacion__c`, `Asistencia__c`, `Cobro__c`), verificar que el perfil tiene al menos permisos de **Read** y **Create**.

> [!NOTE]
> Si el perfil no tiene permiso de **Create** en un objeto, el Data Loader no podrá insertar registros y arrojará el error `INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY`.

---

## 🧪 Fase 2: Smoke Test (Prueba de Impacto en 10 Registros)

*Antes de importar los miles de registros reales, se carga una muestra controlada de 10 registros por objeto para detectar errores de forma temprana.*

**Rol:** 🧪 Tester QA + 🛡️ Admin Salesforce  
**Herramienta:** `Salesforce Data Loader`

### Pasos:

1. **Preparar el Mini-CSV de Prueba:** Tome el archivo `01_Carga_Contactos.csv` y cree una copia `01_Carga_Contactos_SMOKE.csv` con solo las primeras **10 filas de datos** (excluya el encabezado del conteo).
2. **Abrir Data Loader:** En Windows, busque y abra la aplicación **Salesforce Data Loader**.
3. **Conectarse al Org:** Clic en **Log In** → Seleccione **Production** → Ingrese sus credenciales. Si le pide Security Token, concaténelo al final de su contraseña (ej: `MiPassword123ABCDTOKEN`).
4. **Seleccionar Operación UPSERT:** Clic en el botón **Upsert** (NO Insert ni Update).
5. **Seleccionar el Objeto:** En el menú desplegable, busque y seleccione **Contact**.
6. **Cargar el CSV de Smoke:** Clic en **Browse** → Seleccione `01_Carga_Contactos_SMOKE.csv`.
7. **Configurar el External ID:** En la ventana que aparece, seleccione `Numero_Documento__c` como campo de cruce (External ID).
8. **Mapear los Campos:** Clic en **Next** → **Create or Edit a Map** → Mapear cada columna del CSV con el campo correspondiente de Salesforce (arrastrar columna hacia campo).
9. **Ejecutar:** Clic en **Finish** → Confirmar con **Yes**.
10. **Revisar el Resultado:**
    - El archivo `Success.csv` debe tener exactamente **10 filas** (los 10 registros insertados/actualizados).
    - El archivo `Error.csv` debe estar **vacío** o contener 0 errores.
    - En Salesforce, vaya a la pestaña `Contacts` y busque un DNI del CSV. El registro debe aparecer con todos sus datos correctos.

> [!IMPORTANT]
> Si el `Error.csv` tiene alguna fila, **NO proceda con la carga masiva real**. Analice el campo "Error Message" de cada fila en el CSV de errores. Los errores más comunes se explican en la Sección de Errores Frecuentes al final de esta guía.

### Repetir el Smoke Test para cada objeto en orden:

| Paso # | Objeto | Archivo Smoke (10 filas) | External ID a usar |
|---|---|---|---|
| 1° | `Carrera__c` | `00_Carga_Carreras_SMOKE.csv` | `Abreviatura__c` |
| 2° | `Contact` | `01_Carga_Contactos_SMOKE.csv` | `Numero_Documento__c` |
| 3° | `Materia__c` | `02_Carga_Materias_SMOKE.csv` | `Codigo_Materia__c` |
| 4° | `Inscripcion__c` | `03_Carga_Inscripciones_SMOKE.csv` | `ID_Importacion__c` |
| 5° | `Evaluacion__c` | `04_Carga_Evaluaciones_SMOKE.csv` | `ID_Evaluacion__c` |

---

## ✅ Fase 3: Ciclo de QA Funcional (Validación por Historia de Usuario)

*Una vez aprobados los Smoke Tests, el Tester valida el comportamiento de cada automatización y funcionalidad del Sprint 2.*

**Rol:** 🧪 Tester QA  
**Herramienta:** `Salesforce Lightning UI`

### 3.1 Prueba de HU-202: Correo de Bienvenida

1. Ir a la pestaña **Contacts** → Clic en **New**.
2. Llenar los campos: `First Name`, `Last Name`, `Email` (usar un correo real al que tenga acceso), y `Numero_Documento__c` con un DNI ficticio (ej: `99999999`).
3. Clic en **Save**.
4. **Esperar 5 minutos** (los Flows de tipo Record-Triggered se ejecutan en forma asíncrona).
5. Revisar la bandeja de entrada del correo que ingresó.
6. **Resultado esperado:** Debe haber llegado un correo de bienvenida con el logo de Lumina Tech y el nombre del alumno en el cuerpo.
7. **Si no llega el correo:** Ir a `Setup > Flow` → Buscar el Flow de "Bienvenida" → Verificar que está **Active**. Si está inactivo, activarlo.

### 3.2 Prueba de HU-203: Screen Flow de Recepción

1. Localizar el **Screen Flow** en la pantalla de recepción (puede estar en un Botón de Acción o en la Utility Bar).
2. Ejecutar el Flow e ingresar los datos de un alumno con un DNI que **ya existe** en el sistema.
3. **Resultado esperado (Positive Test):** Pantalla de error amigable que dice "Alumno ya registrado" sin mostrar el error técnico de Salesforce.
4. Ejecutar el Flow con un DNI completamente nuevo.
5. **Resultado esperado (Negative Test):** El registro se crea correctamente y el Flow muestra un mensaje de éxito.

### 3.3 Prueba de HU-204: Flow Schedulado de Auditoría de Notas

1. Ir a `Setup > Scheduled Jobs` y verificar que el Job del Flow de auditoría está en estado **Scheduled** para los viernes a las 17:00.
2. **Simular la ejecución manualmente (para QA):** Ir a `Setup > Process Automation > Flows` → Buscar el Flow de Auditoría → Clic en **Run** (solo si el Flow tiene activada la opción de ejecución manual).
3. Después de la ejecución, ir a la pestaña **Activities** y verificar que se crearon Tareas (`Tasks`) en los Registros de Inscripciones con nota `NULL` (no con nota `0`).
4. **Resultado esperado:** Solo las inscripciones donde el campo `Nota__c` es `NULL` deben tener una Tarea generada. Las inscripciones con nota `0` **NO** deben generar tarea.

### 3.4 Prueba de Folder Sharing (HU-205, 206, 207 - Seguridad de Dashboards)

1. **Prueba Positiva (Admin):** Iniciar sesión como Administrador. Ir a la pestaña **Reports** → Buscar la carpeta `Directorio Lumina Tech`. Los reportes deben ser visibles.
2. **Prueba Negativa (Profesor/Recepcionista):**
   - Ir a `Setup > Users` → Seleccionar un usuario con el perfil "Profesor" o equivalente.
   - Clic en **Login** (para iniciar sesión como ese usuario).
   - Ir a la pestaña **Reports** y buscar la carpeta `Directorio Lumina Tech`.
   - **Resultado esperado:** La carpeta **NO debe aparecer** en los resultados. Si el usuario la puede ver, la prueba **FALLA** y se debe corregir el Folder Sharing.
3. Para volver a su sesión de Admin, haga clic en su nombre de usuario (esquina superior derecha) → **Return to [Usuario Admin]**.

---

## 🔄 Fase 4: Release Management (Sincronización de Entornos)

*Si se realizaron cambios en la org DevQA del equipo y se necesita sincronizarlos a otra org Dev (sin sandbox), siga este proceso.*

**Rol:** 🛡️ Admin Salesforce / Consultor  
**Herramienta:** `VS Code con extensión Salesforce CLI (SFDX)`

### Paso 1: Conectar la Org de Origen (DevQA - donde están los cambios)

1. Abra su proyecto en **VS Code**.
2. Presione `Ctrl + Shift + P` para abrir la paleta de comandos.
3. Escriba y seleccione: **`SFDX: Authorize an Org`**.
4. Seleccione el tipo de org: **`Production`** (las Developer Editions usan el endpoint de producción).
5. Se abrirá una ventana del browser con la pantalla de login de Salesforce. Ingrese las credenciales de la org de origen (DevQA).
6. Asigne el alias: `Lumina_DevQA` (nombre corto para identificarla).
7. Verifique en la **barra inferior de VS Code** que la org activa cambió a `Lumina_DevQA`.

### Paso 2: Recuperar los Metadatos del Código Fuente (Retrieve)

1. En VS Code, haga clic en el ícono de **Salesforce** en la barra lateral izquierda (logo de nube).
2. Se abre el panel **Org Browser**.
3. Expanda la sección **Custom Objects**.
4. Si la lista está vacía, haga clic en el ícono de **Refresh** (🔄) al lado del título.
5. Localice el objeto que fue modificado (ej: `Inscripcion__c`).
6. Haga clic en el ícono de **nube con flecha hacia abajo** (⬇️). Esto descargará el metadato a su proyecto local (carpeta `force-app/`).
7. **Verificación:** Abra el explorador de archivos de VS Code → Navegue a `force-app/main/default/objects/Inscripcion__c/fields`. Debe ver los archivos `.field-meta.xml` de los campos nuevos o modificados.

### Paso 3: Conectar la Org de Destino (Dev - a la que se quieren enviar los cambios)

1. En la barra inferior de VS Code, haga clic sobre el nombre de la org actual (`Lumina_DevQA`).
2. Seleccione **`Authorize an Org`** nuevamente.
3. Ingrese las credenciales de la org de destino (Lumina_Dev).
4. Asigne el alias: `Lumina_Dev`.
5. Verifique que la barra inferior ahora muestra `Lumina_Dev`.

### Paso 4: Desplegar los Cambios a la Org de Destino (Deploy)

1. En el explorador de archivos de VS Code, navegue hasta la carpeta del objeto o campo específico que desea desplegar. Por ejemplo: `force-app/main/default/objects/Inscripcion__c/`.
2. Haga clic derecho sobre la **carpeta del objeto**.
3. Seleccione: **`SFDX: Deploy Source to Org`**.
4. VS Code abrirá la pestaña **Output** (parte inferior). Espere hasta ver el mensaje:
   ```
   Successfully deployed [X] components
   ```
5. Si aparece el mensaje `Deploy failed`, revise los errores en la salida. Los más comunes se listan en la sección de Errores Frecuentes.

### Paso 5 (Opcional): Verificación Post-Deploy

1. Cambie la org activa de vuelta a `Lumina_Dev` si aún no lo hizo.
2. Abra el **Org Browser** → Refresque la lista de objetos.
3. Vaya al objeto que desplegó y verifique que los campos nuevos aparecen en la lista.
4. Si realizó cambios en Page Layouts, acceda a un registro del objeto en la UI de Salesforce y confirme que la nueva disposición de campos se muestra correctamente.

### ¿Por qué este método es el más seguro?

| Característica | Deploy por VS Code (SFDX) | Copia Manual del Setup |
|---|---|---|
| **Control granular** | ✅ Campo por campo | ❌ Todo o nada |
| **Historial de cambios** | ✅ Git guarda el historial | ❌ Sin trazabilidad |
| **Riesgo de pérdida de datos** | ✅ Solo agrega / modifica | ⚠️ Puede sobreescribir |
| **Velocidad en equipo grande** | ✅ Reproducible | ❌ Manual y propenso a error |

---

## 🚨 Errores Frecuentes y Soluciones

| Código de Error | Causa | Solución |
|---|---|---|
| `DUPLICATE_EXTERNAL_ID` | El campo External ID encontró un valor repetido dentro del mismo archivo CSV | Ejecutar la deduplicación del CSV (usar `Remove Duplicates` por esa columna en Excel) |
| `DUPLICATE_VALUE` | Ya existe un registro con ese valor Unique en Salesforce (no en el CSV) | Cambiar la operación de **Insert** a **Upsert** y especificar el External ID como llave de cruce |
| `REQUIRED_FIELD_MISSING` | Una columna requerida no está presente o tiene celdas vacías | Verificar el mapeo en Data Loader y rellenar las celdas vacías en Excel antes de volver a cargar |
| `FIELD_INTEGRITY_EXCEPTION` | Se está intentando insertar un registro hijo antes de que el padre exista | Respetar el orden de carga: Carreras → Contactos → Materias → Inscripciones → Evaluaciones |
| `INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY` | El perfil del usuario de Data Loader no tiene permisos sobre el objeto | Revisar permisos del perfil en `Setup > Profiles > Object Settings` |
| `UNABLE_TO_LOCK_ROW` | El mismo registro fue actualizado por dos procesos simultáneos (ej: dos filas con el mismo DNI en el mismo Batch) | Ejecutar la deduplicación del CSV. Reducir el "Batch Size" de Data Loader a 10. |
| `STRING_TOO_LONG` | Un valor en el CSV supera la longitud máxima del campo en Salesforce | Verificar la longitud máxima del campo en Object Manager y truncar la columna en Excel si es necesario. |

---

## 🏆 Fase 5: Criterios de Cierre del Sprint (Definition of Done)

Un **Sprint 2 puede ser marcado como "Cerrado"** únicamente cuando TODAS las siguientes condiciones se cumplen:

| # | Criterio | Verificado por | Estado |
|---|---|---|---|
| 1 | Todos los Smoke Tests (10 rows) aprobados sin errores en `Error.csv` | 🧪 Tester QA | `[ ]` |
| 2 | Carga masiva real completada con tasa de éxito ≥ 95% (ver `Success.csv`) | 🛡️ Admin | `[ ]` |
| 3 | Flow de Bienvenida (HU-202) genera correo en ≤ 10 minutos | 🧪 Tester QA | `[ ]` |
| 4 | Screen Flow (HU-203) bloquea DNI duplicado con mensaje amigable | 🧪 Tester QA | `[ ]` |
| 5 | Flow de Auditoría (HU-204) solo genera Tareas para notas NULL (no ceros) | 🧪 Tester QA | `[ ]` |
| 6 | Dashboard de Directorio NO visible para perfil Profesor/Recepcionista | 🧪 Tester QA | `[ ]` |
| 7 | Todos los errores del `Error.csv` han sido documentados y comunicados | 🛡️ Admin | `[ ]` |
| 8 | El archivo `HISTORIAS_DE_USUARIO_S2.md` tiene todos los criterios marcados `[x]` | 📊 Consultor | `[ ]` |

> [!IMPORTANT]
> Si algún criterio está marcado como `[ ]` (sin completar), el Sprint **NO** puede cerrarse. El equipo debe levantar un bug ticket en Trello (columna **Bugs / Blockers**) y resolverlo antes del cierre formal.

---

## 🚀 Fase 6: Deploy al Entorno PROD-DEMO (Presentación Final)

*Esta fase se ejecuta una única vez, cuando el entorno Dev y DevQA están estables y aprobados. El objetivo es crear un tercer org "limpio" que funcionará como entorno de producción para la Demo Final ante el cliente/evaluadores.*

**Rol:** 🛡️ Admin Salesforce + 📊 Consultor  
**Herramienta:** `Salesforce Developer Edition Sign-up` + `VS Code SFDX` + `Data Loader`

> [!NOTE]
> En Salesforce, las orgs **Developer Edition** son independientes entre sí. No existe un botón de "Promover a producción". El proceso es: **crear un org nuevo → configurar My Domain → deployar metadatos → cargar datos**. Esto es equivalente a lo que en proyectos reales se llama un "Go-Live".

---

### 6.1 Creación del Org PROD-DEMO

1. **Abrir el navegador** y acceder a: [https://developer.salesforce.com/signup](https://developer.salesforce.com/signup)
2. **Completar el formulario** con los datos del org de producción:
   - **First Name / Last Name:** Nombre del Admin titular del proyecto.
   - **Email:** Usar el correo oficial del equipo (ej: `luminaltech.grupo3@gmail.com`). Debe ser un correo **al que tengan acceso**.
   - **Role:** `Developer`
   - **Company:** `Lumina Tech University`
   - **Country:** `Argentina`
   - **Postal Code:** Cualquier código válido (ej: `1000`).
   - **Username:** Este es el campo más importante. Debe ser **único a nivel global en Salesforce**. Usar el formato:
     ```
     admin@luminatech.prod.demo
     ```
   > **Nota:** El *Username* no es una dirección de email real. Es solo un identificador único. No tiene que existir como casilla de correo.
3. Clic en **Sign me up**.
4. Revisar el email de confirmación. Hacer clic en el enlace **Verify Account** para establecer la contraseña.
5. Iniciar sesión en el nuevo org. La URL por defecto será algo como:
   ```
   https://[aleatorio].my.salesforce.com
   ```

---

### 6.2 Configuración de My Domain (URL Personalizada)

*My Domain permite que la URL del org muestre el nombre del proyecto en lugar de caracteres aleatorios.*

1. Ir a `Setup` → Buscar **"My Domain"** en la barra de búsqueda rápida.
2. En el campo `Enter your domain name`, escribir el nombre deseado. Se recomienda:
   ```
   lumina-tech-university-prod
   ```
3. Clic en **Check Availability** para verificar que el nombre no esté tomado por otro org.
4. Si está disponible, clic en **Register Domain**.
5. **Esperar entre 5 y 30 minutos** mientras Salesforce propaga el nombre de dominio. Recibirá un correo de confirmación cuando esté listo.
6. Una vez recibido el correo, volver a `Setup > My Domain` y hacer clic en **Log In**.
7. La URL del org ahora será:
   ```
   https://lumina-tech-university-prod.my.salesforce.com
   ```
   Esta es la URL que se usará en la Demo Final para que el evaluador vea un entorno con nombre profesional.

> [!CAUTION]
> Una vez que My Domain está activado, **no se puede desactivar ni cambiar**. Elija el nombre con cuidado antes de hacer clic en "Register Domain".

---

### 6.3 Deploy de Metadatos desde Dev/DevQA al Org PROD-DEMO

*Todos los objetos, campos, flows, perfiles y layouts configurados en los orgs actuales se despliegan al org de producción.*

**Herramienta:** VS Code con extensión Salesforce CLI

#### Paso A: Autorizar el Org PROD-DEMO en VS Code

1. En VS Code, presionar `Ctrl + Shift + P`.
2. Seleccionar **`SFDX: Authorize an Org`**.
3. Seleccionar **`Production`** como tipo de org (My Domain no cambia esto).
4. Iniciar sesión con las credenciales del org PROD-DEMO (`admin@luminatech.prod.demo`).
5. Asignar el alias: `Lumina_Prod_Demo`.
6. Verificar en la barra inferior que la org activa cambió.

#### Paso B: Recuperar los Metadatos del Org de Origen (DevQA)

1. Cambiar la org activa a `Lumina_DevQA` (barra inferior de VS Code o `SFDX: Set a Default Org`).
2. Abrir el **Org Browser** (ícono de nube en la barra lateral).
3. Para cada categoría de metadato, recuperar en este orden:

| Orden | Tipo de Metadato | Descripción |
|---|---|---|
| 1° | `Custom Objects` | Todos los objetos personalizados: `Carrera__c`, `Materia__c`, `Inscripcion__c`, `Evaluacion__c`, `Asistencia__c`, `Cobro__c` |
| 2° | `Flows` | Screen Flow de Recepción, Flow de Bienvenida, Flow de Auditoría |
| 3° | `Email Templates` | Lightning Email Template del correo de bienvenida |
| 4° | `Profiles` | Perfil System Administrator y perfiles personalizados del G6 |
| 5° | `Custom Labels` | Si se usan etiquetas personalizadas en los flows |
| 6° | `Lightning Pages` (App Pages) | Home Page con Dashboard incrustado |

   Para cada ítem: clic derecho → **Retrieve Source from Org**. Verificar que los archivos aparecen en `force-app/main/default/`.

#### Paso C: Deploy al Org PROD-DEMO

1. Cambiar la org activa a `Lumina_Prod_Demo` (barra inferior).
2. En el explorador de VS Code, seleccionar la carpeta raíz: `force-app/`
3. Clic derecho → **`SFDX: Deploy Source to Org`**.
4. Observar la pestaña **Output**. El deploy puede tardar entre 2 y 10 minutos según la cantidad de metadatos.
5. Verificar el mensaje final:
   ```
   === Deployed Source
   Successfully deployed [N] components
   ```
6. Si hay errores, leer el mensaje de la columna `Problem`. Los más comunes:
   - **`Unknown user`**: Un Flow o Email Alert referencia a un Usuario que no existe en el org destino. Crear el usuario o actualizar la referencia.
   - **`Custom field not found`**: Un field-reference en un Flow o Layout apunta a un campo que aún no existe. Asegurarse de deployar los Custom Objects **antes** que los Flows.

> [!IMPORTANT]
> El orden correcto de deploy es siempre: **Objetos → Perfiles → Flows → Páginas**. Si se invierte el orden, los Flows fallarán porque referencian campos que todavía no existen en el org destino.

---

### 6.4 Carga de Datos al Org PROD-DEMO (Data Loader)

*Una vez que los metadatos fueron desplegados exitosamente, se cargan los datos reales usando los archivos CSV limpios.*

**Herramienta:** Salesforce Data Loader (conectado al org `admin@luminatech.prod.demo`)

Ejecutar el proceso de carga en el mismo orden que en el Smoke Test, pero ahora con los archivos de datos **completos** (no los de 10 filas):

| Orden | Objeto | Archivo CSV | External ID |
|---|---|---|---|
| 1° | `Carrera__c` | `00_Carga_Carreras_[Año].csv` | `Abreviatura__c` |
| 2° | `Contact` | `01_Carga_Contactos_[Año].csv` | `Numero_Documento__c` |
| 3° | `Materia__c` | `02_Carga_Materias_[Año].csv` | `Codigo_Materia__c` |
| 4° | `Inscripcion__c` | `03_Carga_Inscripciones_[Año].csv` | `ID_Importacion__c` |
| 5° | `Evaluacion__c` | `04_Carga_Evaluaciones_[Año].csv` | `ID_Evaluacion__c` |

Para conectar Data Loader al org PROD-DEMO:
1. Abrir Data Loader → **Log In** → **Production**.
2. Ingresar las credenciales: `admin@luminatech.prod.demo` + contraseña + Security Token.
3. Proceder con el UPSERT de cada objeto en el orden indicado.

---

### 6.5 Configuración Post-Deploy en el Org PROD-DEMO

*Algunas configuraciones no se despliegan automáticamente con SFDX y deben hacerse manualmente en el nuevo org.*

| Tarea | Herramienta | Notas |
|---|---|---|
| Activar los Flows | `Setup > Flows` | Los Flows desplegados llegan en estado "Inactive". Deben activarse manualmente uno a uno. |
| Activar Lightning Experience | `Setup > Lightning Experience` | Verificar que la org está en modo Lightning (no Classic). |
| Configurar la Home Page | `Setup > Lightning App Builder` | Abrir la página Home, verificar que el Dashboard está incrustado, y publicar. |
| Crear las Carpetas de Reportes | `Reports Tab > New Folder` | La estructura de carpetas NO se despliega con SFDX. Recrear las carpetas `Directorio Lumina Tech` y configurar el Folder Sharing manualmente. |
| Crear los Usuarios de Demo | `Setup > Users > New User` | Crear al menos un usuario con perfil "Profesor" y otro con "Recepcionista" para demostrar la seguridad de acceso durante la presentación. |
| Crear los Reportes y Dashboards | `Reports / Dashboards Tab` | Los dashboards pueden haberse desplegado vía SFDX (si se incluyeron en el retrieve), verificar que están vinculados a los reportes correctos. Si no, recrearlos manualmente. |

---

### 6.6 Checklist Pre-Demo (Validación Final del Entorno PROD-DEMO)

Ejecutar este checklist el día **antes** de la presentación:

| # | Verificación | Resultado Esperado | Estado |
|---|---|---|---|
| 1 | La URL del org muestra `lumina-tech-university-prod.my.salesforce.com` | URL personalizada activa | `[ ]` |
| 2 | La org tiene los 6 objetos personalizados con todos sus campos | Visible en Object Manager | `[ ]` |
| 3 | Al menos 500 registros de Contactos (Alumnos) cargados | Confirmar en Reports o List Views | `[ ]` |
| 4 | Los 3 Flows están en estado **Active** | Visible en `Setup > Flows` | `[ ]` |
| 5 | El Dashboard de Directorio es visible para el Admin pero NO para el Profesor | Prueba negativa aprobada | `[ ]` |
| 6 | La Home Page muestra el Dashboard al iniciar sesión como Admin | UX confirmada | `[ ]` |
| 7 | El Screen Flow de Recepción funciona desde la UI sin errores | Prueba desde Utility Bar | `[ ]` |
| 8 | El correo de bienvenida llega al crear un Contacto nuevo manualmente | Email recibido en ≤ 10 min | `[ ]` |

> [!TIP]
> Durante la Demo, usar siempre el perfil **System Administrator** para las demos de configuración y cambiar a un usuario "Alumno/Profesor" solo cuando se quiera demostrar la restricción de seguridad. Esto da mayor impacto visual al evaluador.

# Guía 19: Manual Maestro de Importación Masiva (Data Loader)

**Rol:** Salesforce Data Architect
**Trazabilidad:** HU-201C a HU-201G
**Estrategia:** Normalización de Datos Históricos (Lumina Tech - Argentina)

Esta guía proporciona el procedimiento definitivo, paso a paso, para la migración compleja de datos. No se trata solo de subir archivos, sino de orquestar la integridad relacional de la base de datos.

---

## � Fase 0: Instalación de Data Loader (Windows)

Antes de realizar cualquier carga, debe tener instalada la herramienta oficial de Salesforce. Siga estos pasos:

### 1. Requisito de Java (Indispensable)
Data Loader requiere un entorno de ejecución de Java (JRE). 
1. Descargue e instale el **OpenJDK versión 17 o 21** (ej. de [Zulu](https://www.azul.com/downloads/?package=jdk)).
2. Verifique la instalación abriendo una terminal y ejecutando `java -version`.

### 2. Descarga de Data Loader
1. Inicie sesión en su Org de Salesforce.
2. Vaya a **Setup** (Configuración).
3. En el buscador rápido, escriba **"Data Loader"**.
4. Haga clic en el botón **Download Data Loader for Windows**.

### 3. Instalación
1. Extraiga el archivo `.zip` descargado en una carpeta local (ej: `C:\Data_Loader`).
2. Haga clic derecho sobre el archivo `install.bat` y seleccione **Ejecutar como Administrador**.
3. Siga las instrucciones de la terminal (presione `Enter` para aceptar la ruta por defecto).
4. Cuando pregunte si desea crear un acceso directo en el escritorio, escriba `Yes` y presione `Enter`.

---

## �🛠️ Prerrequisitos Críticos en Salesforce

Antes de abrir Data Loader, verifique que los siguientes campos tengan el check **External ID** y **Unique** activo en el **Object Manager**:

| Objeto | Campo API | Tipo | Función |
| :--- | :--- | :--- | :--- |
| **Carrera** | `Abreviatura__c` | Text(10) | Llave para Materias |
| **Contacto** | `Numero_Documento__c` | Text(20) | Llave para Inscripciones |
| **Materia** | `Codigo_Materia__c` | Text(20) | Llave para Inscripciones |
| **Inscripción**| `ID_Importacion__c` | Text(50) | Llave para Evaluaciones |

---

## 🚀 Fase de Ejecución: Paso a Paso

### Carga 1: Carreras (`00_Carga_Carreras.csv`)
1. **Operación:** `Upsert`.
2. **Step 2: Object:** `Carrera__c`.
3. **Step 2a: External ID:** Seleccionar `Abreviatura__c`.
4. **Step 3: Mapping:**
   - `Name` -> `Name`
   - `Abreviatura__c` -> `Abreviatura__c`
5. **Resultado esperado:** 7 registros maestros creados.

### Carga 2: Contactos (`01_Carga_Contactos.csv`)
1. **Operación:** `Upsert`.
2. **Secretos de Arquitecto:**
   - Desactivar temporalmente las **Duplicate Rules** en `Setup -> Duplicate Management`.
   - Limpiar correos con dominio `@nuevo-email.com` dejándolos en blanco.
3. **Step 2a: External ID:** Seleccionar `Numero_Documento__c`.
4. **Step 3: Mapping:**
   - `Nombre` -> `FirstName`
   - `Apellido` -> `LastName`
   - `Telefono` -> `Phone`
   - `Numero_Documento__c` -> `Numero_Documento__c`

### Carga 3: Materias (`02_Carga_Materias.csv`)
1. **Operación:** `Upsert`.
2. **Step 2: Object:** `Materia__c`.
3. **Step 2a: External ID:** Seleccionar `Codigo_Materia__c`.
4. **Step 2b: Relationship:** En `Carrera__r`, seleccionar `Abreviatura__c`.
5. **Step 3: Mapping:**
   - `Name` -> `Name`
   - `Codigo_Materia__c` -> `Codigo_Materia__c`
   - `Carrera__c` -> `Carrera__r:Carrera__c-Abreviatura__c`

### Carga 4: Inscripciones (`03_Carga_Inscripciones.csv`)
1. **Operación:** `Upsert`.
2. **Secretos de Arquitecto:**
   - **IMPORTANTE:** Desactivar **Lookup Filters** en el objeto Inscripción (Campos `Alumno__c` y `Materia__c`).
3. **Step 2a: External ID:** Seleccionar `ID_Importacion__c`.
4. **Step 2b: Discovering Relationships:**
   - `Alumno__r` -> Seleccionar `Numero_Documento__c`.
   - `Materia__r` -> Seleccionar `Codigo_Materia__c`.
5. **Step 3: Mapping:**
   - `Contact_Numero_Documento__c` -> `Alumno__r:Contact-Numero_Documento__c`
   - `Materia_Codigo__c` -> `Materia__r:Materia__c-Codigo_Materia__c`
   - `ID_Importacion__c` -> `ID_Importacion__c`

### Carga 5: Evaluaciones (`04_Carga_Evaluaciones.csv`)
1. **Operación:** `Insert` (No requiere External ID propio).
2. **Step 2b: Relationship:** En `Inscripcion__r`, seleccionar `ID_Importacion__c`.
3. **Step 3: Mapping:**
   - `Nota` -> `Examen_Final__c` (o el campo Number correspondiente).
   - `Fecha_Examen` -> `Fecha_de_Examen__c`.
   - `Inscripcion_ID_Importacion__c` -> `Inscripcion__r:Inscripcion__c-ID_Importacion__c`.

---

## ⚠️ Procedimiento de Borrado Masivo (Rollback)

Si cometió un error en la carga y necesita eliminar los registros para empezar de cero, siga estos pasos estrictos. **No intente borrar manualmente uno por uno.**

### Paso 1: Localizar el archivo de éxito
1. Al finalizar cualquier carga (Insert/Upsert), Data Loader genera un archivo llamado `success[timestamp].csv`.
2. Abra este archivo. Notará una columna extra a la izquierda llamada **ID**. Este es el Salesforce ID único generado para cada registro.

### Paso 2: Configurar la operación de borrado
1. En Data Loader, haga clic en el botón **Delete**.
2. **Step 2: Object:** Seleccione el objeto que desea limpiar (Ej: `Inscripcion__c`).
3. **CSV Selection:** Elija el archivo `success.csv` del paso anterior.

### Paso 3: Mapeo de ID
1. En el **Step 3 (Mapping)**, solo necesita mapear un campo:
   - `ID` (del CSV) -> `Id` (de Salesforce).
2. Haga clic en **OK** y luego en **Next**.

### Paso 4: Ejecución
1. Haga clic en **Finish**.
2. **Precaución:** Los registros se enviarán a la **Recycle Bin**. Si necesita liberar espacio de almacenamiento inmediatamente (Developer Edition), deberá vaciar la papelera manualmente en Salesforce (`Setup -> Recycle Bin -> Empty Org Recycle Bin`).

### 🕵️ ¿Qué pasa si no tengo el archivo success.csv? (Plan B)
Si perdió el archivo de éxito, puede recuperar los Salesforce IDs necesarios siguiendo este procedimiento de "rescate":

1. **Operación:** Haga clic en el botón **Export** en Data Loader.
2. **Objeto:** Seleccione el objeto que desea borrar (Ej: `Contact`).
3. **SOQL Query:** 
   - Seleccione los campos `Id` y su **External ID** (Ej: `Numero_Documento__c`).
   - Agregue una cláusula `WHERE` si es posible para filtrar solo los registros cargados hoy (Ej: `CreatedDate = TODAY`).
   - Ejemplo: `SELECT Id FROM Contact WHERE CreatedDate = YESTERDAY OR CreatedDate = TODAY`
   - *Tip Pro:* Si quieres borrar todo lo de los últimos días, puedes usar `CreatedDate >= LAST_N_DAYS:1` (esto incluye hoy y ayer).
   - Para borrar **TODO** el objeto (Carga Limpia): `SELECT Id FROM [Nombre_Objeto]`
4. **Archivo Generado:** El CSV resultante tendrá los IDs necesarios. Úselo como base para la operación **Delete** descrita anteriormente, mapeando la columna `Id` del archivo al campo `Id` de Salesforce.

## 🧹 Estrategia "Zero Baseline" (Limpieza Total)
Si su objetivo es dejar la organización "en 0" para realizar una carga 100% limpia y profesional, siga este orden de borrado total. **No use filtros WHERE**, simplemente exporte todos los IDs.

### Orden de Ejecución Directa:
1.  **Export & Delete:** `Evaluacion__c` (o el nombre del objeto de notas).
2.  **Export & Delete:** `Inscripcion__c`.
3.  **Export & Delete:** `Materia__c`.
4.  **Export & Delete:** `Contact`.
5.  **Export & Delete:** `Carrera__c`.

**⚠️ Importante:** Tras completar los 5 pasos, es obligatorio ir a **Setup -> Recycle Bin -> Empty Org Recycle Bin** para que Salesforce libere el espacio de almacenamiento y permita la nueva carga sin errores de límite excedido.

### ⚠️ Orden Crítico de Eliminación (Bottom-Up)
Para evitar errores de "Dependency" o "Lookup", elimine en este orden estricto:
1. **Evaluaciones** (Objeto hijo final).
2. **Inscripciones**.
3. **Materias**.
4. **Contactos** (Alumnos).
5. **Carreras**.

---

## 🚨 Troubleshooting de Élite

### Error de Almacenamiento (Storage Limit Exceeded)
Si la Developer Edition (5MB) se llena:
1. Vacíe la **Recycle Bin** (Papelera).
2. Elimine campos redundantes (Ej: Si un campo `Codigo_Unico__c` repite el valor del `Name` Auto-number).
3. Reduzca el `Batch Size` a 1 para identificar el registro exacto que causa el desborde (aunque el límite suele ser general).

### Error de Filtro de Búsqueda
Si el error dice `Value does not exist or does not match filter criteria`, es porque olvidó desactivar los **Lookup Filters** en la configuración del objeto antes de la carga.

---

## 💡 Recomendaciones de Post-Carga
- Una vez finalizada la carga 5, reactive todas las **Duplicate Rules** y **Lookup Filters**.
- Oculte los campos `ID_Importacion__c` del Page Layout para evitar confusión del usuario final, manteniéndolos solo para auditoría y futuras sincronizaciones.

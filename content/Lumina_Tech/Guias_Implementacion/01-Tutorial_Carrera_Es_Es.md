# 🎓 Guía Técnica: Objeto Carrera (Master Data)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-001](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Dependencia de Inscripción)

---

## 🎯 Objetivo
Crear el objeto `Carrera__c` que almacenará los planes de estudio de la universidad. Este será un objeto "Padre".

## 🛠️ Procedimiento

### Paso 1: Configuración Inicial
1.  Haz clic en el ícono de engranaje ⚙️ (arriba a la derecha) y selecciona **Setup**.
2.  En la barra superior, haz clic en la pestaña **Object Manager**.
3.  Haz clic en el botón **Create** (arriba a la derecha) y selecciona **Custom Object**.

### Paso 2: Definición del Objeto
Complete los campos con EXACTITUD:

1.  **Label**: Escribe `Carrera`.
2.  **Plural Label**: Escribe `Carreras`.
3.  **Object Name**: `Carrera` (API Name: `Carrera__c`).
4.  **Record Name**: Escribe `Nombre de Carrera`.
5.  **Data Type**: Selecciona **Text**.
6.  (Omitir Display Format y Starting Number).
8.  En la sección "Optional Features", marca la casilla: ☑️ **Track Field History**.
10. En la sección "Object Creation Options" (al final), marca: ☑️ **Launch New Custom Tab Wizard after saving custom object**.
11. Haz clic en **Save**.

### Paso 1.1: Definir Estilo de Pestaña (Tab)
*Necesario para ver el objeto en la App.*
1.  **Tab Style**: Haz clic en la lupa y selecciona un ícono representativo (ej: *Building* para Carrera).
2.  Haz clic en **Next**.
3.  **Profiles**: Deja "Apply one tab visibility to all profiles" en **Default On**. Haz clic en **Next**.
4.  **Apps**: Desmarca "Include Tab" (lo haremos manualmente luego) o déjalo marcado. Haz clic en **Save**.

### Paso 3: Crear Campos del Objeto (Business Fields)

#### 3.1 Código Interno (AutoNumber)
*Para mantener un identificador único (ID) del sistema.*
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Auto Number**. Next.
3.  **Field Label**: `Código Interno`.
4.  **Field Name**: `Codigo_Interno`.
5.  **Display Format**: `CAR-{0000}`.
6.  **Starting Number**: `1`.
7.  **Next** > **Next** > **Save & New**.

#### 3.2 Tipo de Título (Picklist)
1.  Data Type: **Picklist**. Next.
2.  **Field Label**: `Tipo de Título`.
3.  **Field Name**: `Tipo_Titulo`.
4.  Values (Enter manually):
    *   `Licenciatura`
    *   `Tecnicatura`
    *   `Posgrado`
5.  **Next** > **Next** > **Save & New**.

#### 3.3 Duración (Picklist) (MODIFICADO)
1.  Data Type: **Picklist**. Next.
2.  **Field Label**: `Duración (Años)`.
3.  **Field Name**: `Duracion_Anios`.
4.  **Values**:
    *   `1`
    *   `2`
    *   `3`
    *   `4`
    *   `5`
5.  ☑️ **Required**.
6.  **Next** > **Next** > **Save & New**.

#### 3.4 Activa (Status)
*Para "borrar" carreras viejas sin perder historia.*
1.  Data Type: **Checkbox**. Next.
2.  **Field Label**: `Activa`.
3.  **Field Name**: `Activa`.
4.  **Default Value**: `Checked`.
5.  **Next** > **Next** > **Save**.

### Paso 3.5: Crear Vista "Todas las Carreras" (All)
*Por defecto Salesforce muestra "Recently Viewed". Crearemos la vista "All".*
1.  Ve a la pestaña **Carreras**.
2.  Haz clic en el ícono de engranaje (List View Controls) > **New**.
3.  Name: `Todas`. API Name: `Todas`.
4.  Who sees this list view?: **All users can see this list view**.
5.  **Save**.
6.  (Opcional) Pincha la chincheta 📌 para dejarla fija.

### Paso 4: Mejorar la Búsqueda (Search Layouts)
*Para ver el nombre "Ingeniería" en lugar de solo "CAR-0001".*
1.  En el Object Manager de **Carrera**, haz clic en **Search Layouts**.
2.  Haz clic en la flecha ▼ al lado de **Search Results** > **Edit**.
3.  En "Available Fields", selecciona **Nombre de la Carrera** y agrégalo a "Selected Fields" con la flecha ▶️.
4.  Haz lo mismo con **Duración (Años)** si deseas.
5.  Haz clic en **Save**.
6.  (Opcional) Repite para **Lookup Dialogs** (si aparece como opción separada en tu edición).

---

## ✅ Verificación de Éxito
1.  Haz clic en el **App Launcher** (9 puntos).
2.  Escribe y selecciona "**Carreras**".
3.  Haz clic en **New**.
4.  Completa la duración (ej: 5) y **Save**.
5.  Verifica que se generó un código como `CAR-0001`.

---

## 📝 Resumen Técnico del Objeto

| Característica | Detalle |
| :--- | :--- |
| **API Name** | `Carrera__c` |
| **Tipo** | Custom Object (Master) |
| **Relaciones** | Ninguna (Es padre de Materia e Inscripción) |

### Campos Clave

| Field Label | API Name | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| **Nombre de Carrera** | `Name` | Text (80) | Nombre oficial (ej: Ingeniería de Software). |
| **Código Interno** | `Codigo_Interno__c` | Auto Number | ID único formateado (CAR-{0000}). |
| **Tipo de Título** | `Tipo_Titulo__c` | Picklist | Licenciatura, Tecnicatura, Posgrado. |
| **Duración (Años)** | `Duracion_Anios__c` | Picklist | 1, 2, 3, 4, 5. |
| **Activa** | `Activa__c` | Checkbox | Indica si la carrera sigue vigente. |

### Validaciones
*No se definieron reglas de validación específicas para este objeto en esta fase.*

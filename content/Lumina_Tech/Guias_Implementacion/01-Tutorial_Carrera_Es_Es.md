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
4.  **Record Name**: Escribe `Código de Carrera`.
5.  **Data Type**: Selecciona **Auto Number** en el menú desplegable.
6.  **Display Format**: Escribe `CAR-{0000}`.
7.  **Starting Number**: Escribe `1`.
8.  En la sección "Optional Features", marca la casilla: ☑️ **Track Field History**.
9.  En la sección "Search Status", marca la casilla: ☑️ **Allow Search**.
10. Haz clic en **Save**.

### Paso 3: Crear Campos del Objeto (Business Fields)

#### 3.1 Nombre de la Carrera
*Aunque tenemos el Código (AutoNumber), necesitamos el nombre real.*
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Text**. Next.
3.  **Field Label**: `Nombre de la Carrera`.
4.  **Field Name**: `Nombre_Carrera`.
5.  Length: `80`.
6.  ☑️ **Required** & ☑️ **Unique** (Case Insensitive).
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

#### 3.3 Duración (Duration)
1.  Data Type: **Number**. Next.
2.  **Field Label**: `Duración (Años)`.
3.  **Field Name**: `Duracion_Anios`.
4.  Length: `2`. Decimals: `0`.
5.  ☑️ **Required**.
6.  **Next** > **Next** > **Save & New**.

#### 3.4 Activa (Status)
*Para "borrar" carreras viejas sin perder historia.*
1.  Data Type: **Checkbox**. Next.
2.  **Field Label**: `Activa`.
3.  **Field Name**: `Activa`.
4.  **Default Value**: `Checked`.
5.  **Next** > **Next** > **Save**.

---

## ✅ Verificación de Éxito
1.  Haz clic en el **App Launcher** (9 puntos).
2.  Escribe y selecciona "**Carreras**".
3.  Haz clic en **New**.
4.  Completa la duración (ej: 5) y **Save**.
5.  Verifica que se generó un código como `CAR-0001`.

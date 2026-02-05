# 🎓 Guía Técnica: Objeto Carrera (Master Data)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-001](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Dependencia de Inscripción)

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

1.  **Label**: Escribe `Career`.
2.  **Plural Label**: Escribe `Careers`.
3.  **Object Name**: `Career` (Se llena automático).
4.  **Record Name**: Escribe `Career Code`.
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
3.  **Field Label**: `Career Name`. Length: `80`.
4.  ☑️ **Required** & ☑️ **Unique** (Case Insensitive).
5.  **Next** > **Next** > **Save & New**.

#### 3.2 Tipo de Título (Picklist)
1.  Data Type: **Picklist**. Next.
2.  **Field Label**: `Degree Type`.
3.  Values (Enter manually):
    *   `Bachelor` (Licenciatura)
    *   `Technician` (Tecnicatura)
    *   `Postgraduate` (Posgrado)
4.  **Next** > **Next** > **Save & New**.

#### 3.3 Duración (Duration)
1.  Data Type: **Number**. Next.
2.  **Field Label**: `Duration (Years)`.
3.  Length: `2`. Decimals: `0`.
4.  ☑️ **Required**.
5.  **Next** > **Next** > **Save & New**.

#### 3.4 Activa (Status)
*Para "borrar" carreras viejas sin perder historia.*
1.  Data Type: **Checkbox**. Next.
2.  **Field Label**: `Active`.
3.  **Default Value**: `Checked`.
4.  **Next** > **Next** > **Save**.

---

## ✅ Verificación de Éxito
1.  Haz clic en el **App Launcher** (9 puntos).
2.  Escribe y selecciona "**Careers**".
3.  Haz clic en **New**.
4.  Completa la duración (ej: 5) y **Save**.
5.  Verifica que se generó un código como `CAR-0001`.

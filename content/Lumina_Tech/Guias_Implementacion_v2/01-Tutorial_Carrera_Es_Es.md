# 🎓 Guía Técnica: Objeto Carrera (Master Data) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Migración de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**

---

## 🎯 Objetivo
Crear el objeto `Carrera__c` que almacenará los planes de estudio. En el Sprint 2, este objeto se refuerza con un **External ID** (`Abreviatura__c`) para permitir que las Materias e Inscripciones se vinculen masivamente sin usar Salesforce IDs.

## 🛠️ Procedimiento

### Paso 1: Configuración Inicial
1.  Haz clic en el ícono de engranaje ⚙️ y selecciona **Setup**.
2.  En la pestaña **Object Manager**, haz clic en **Create** > **Custom Object**.
3.  **Label**: `Carrera`. **Plural Label**: `Carreras`.
4.  **Object Name**: `Carrera`.
5.  **Record Name**: `Nombre de Carrera` (Data Type: **Text**).
6.  En la sección "Optional Features", marca: ☑️ **Track Field History**.
7.  En la sección "Object Creation Options", marca: ☑️ **Launch New Custom Tab Wizard**.
8.  Haz clic en **Save** y selecciona un estilo de pestaña (ej: *Building*).

### Paso 2: [NUEVO S2] Campo Abreviatura (External ID)
*Vital para que el Data Loader pueda cruzar los CSVs.*

1.  **Fields & Relationships** > **New**.
2.  Data Type: **Text**. Next.
3.  **Field Label**: `Abreviatura`.
4.  **Field Name**: `Abreviatura`.
5.  **Length**: `20`.
6.  ☑️ **Unique**: Marca "Case insensitive" para evitar duplicados.
7.  ☑️ **External ID**: **OBLIGATORIO**. Marca esta casilla.
8.  Haz clic en **Save**.

### Paso 3: Campos de Negocio
Siga creando los campos definidos en el Sprint 1:

#### 3.1 Código Interno (AutoNumber)
- **Label**: `Código Interno`. **Name**: `Codigo_Interno`.
- **Format**: `CAR-{0000}`. **Start**: `1`.

#### 3.2 Tipo de Título (Picklist)
- **Label**: `Tipo de Título`. **Name**: `Tipo_Titulo`.
- **Values**: `Licenciatura`, `Tecnicatura`, `Posgrado`.

#### 3.3 Duración (Picklist)
- **Label**: `Duración (Años)`. **Name**: `Duracion_Anios`.
- **Values**: 1, 2, 3, 4, 5. (☑️ **Required**).

---

## ✅ Verificación de Éxito
1.  Ve al **App Launcher** > **Carreras**.
2.  Crea una nueva Carrera (ej: "Ingeniería en Software") con Abreviatura: `DEV`.
3.  Verifica que el campo "Código Interno" se genera como `CAR-0001`.

## 📝 Resumen Técnico del Objeto
| API Name | Tipo | External ID |
| :--- | :--- | :--- |
| `Carrera__c` | Custom Object | - |
| `Abreviatura__c` | Text (20) | ✅ SÍ |
| `Codigo_Interno__c` | Auto Number | - |
| `Duracion_Anios__c` | Picklist | - |

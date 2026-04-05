# 🎓 Guía Técnica: Objeto Materia (Catálogo) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Migración de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**

---

## 🎯 Objetivo
Crear el objeto `Materia__c` y vincularlo fuertemente a una Carrera usando una relación **Master-Detail**. En el Sprint 2, aseguramos que la carga masiva use la **Abreviatura** de la carrera para establecer esta relación.

## 🛠️ Procedimiento

### Paso 1: Configuración Inicial del Objeto
1.  Ve a **Setup** > **Object Manager**.
2.  Haz clic en **Create** > **Custom Object**.
3.  **Label**: `Materia`. **Plural Label**: `Materias`.
4.  **Object Name**: `Materia`.
5.  **Record Name**: `Nombre de Materia` (Data Type: **Text**).
6.  Marca las casillas críticas: 
    *   ☑️ **Track Field History** (Seguimiento de historial).
    *   ☑️ **Allow Search** (Permitir búsqueda) -> **[CRÍTICO]** Si no marcas esto, no aparecerá el menú de Search Layouts.
7.  Haz clic en **Save** y configura la pestaña (ej: *Books*).

### Paso 2: Relación Maestro-Detalle (Carrera)
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Master-Detail Relationship**. Next.
3.  **Related To**: `Carrera`. Next.
4.  **Field Label/Name**: `Carrera`.
5.  ☑️ **Allow Reparenting**: **OBLIGATORIO**. Marca esta casilla (crucial para despliegues y correcciones en la carga masiva).
6.  Haz clic en **Save**.

### Paso 3: Campos de Migración y Negocio
#### 3.1 [CRÍTICO] Código Externo (External ID)
*Para identificar la materia de forma única en los CSVs.*
1.  Data Type: **Text**.
2.  **Label**: `Código Externo`. **Name**: `Codigo_Externo`.
3.  **Length**: `20`.
4.  ☑️ **Unique** & ☑️ **External ID**: Marcados.
5.  **Save**.

#### 3.2 Campos Académicos
- **Código de Materia** (AutoNumber): `MAT-{0000}`.
- **Créditos** (Picklist): 1-10. (☑️ **Required**).
- **Tipo de Materia** (Picklist): `Obligatoria`, `Electiva`.
- **Año del Plan** (Picklist): 1-5.
- **Ciclo** (Picklist): `CBC`, `Segundo Ciclo`, `Electivas`.
- **Capacidad de Almacenamiento**: Mantener campos ligeros.

---

### Paso 4: [OPCIONAL] Mejora de Búsqueda (Search Layouts / Formatos)
*Si al usar el campo de búsqueda ("Lookup") no ves los campos correctos, ajusta la visualización:*

> [!IMPORTANT]
> **Requisito Previo:** Para que esta opción aparezca:
> 1. El objeto debe tener la casilla **`Allow Search`** activada (ver Paso 1.6).
> 2. El objeto debe tener una **Pestaña (Tab)** creada.

1.  Ve a **Object Manager** > **Materia** > **Search Layouts** (en español: **Formatos de búsqueda**).
2.  Busca **Default Layout** y haz clic en la flecha de la derecha -> **Edit**.
3.  Añade los campos de la izquierda a la derecha según este orden:
    - `Nombre de Materia`
    - `Código Externo`
    - `Carrera`
4.  Haz clic en **Save**.

> [!TIP]
> **¿Por qué solo veo registros recientes?**
> Salesforce prioriza lo que has visto últimamente. Para que las materias importadas aparezcan en el buscador de Inscripción sin tener que escribir el nombre completo:
> 1. Ve a la pestaña **Materias** y abre la lista **"All"**.
> 2. Abre 2 o 3 registros. 
> 3. Esto "despierta" el motor de sugerencias del Lookup para tu usuario.

---

## 🚀 Estrategia de Carga (Sprint 2)
Al importar Materias vía Data Loader:
- **JOIN Key**: Use `Carrera__r:Abreviatura__c` para vincular a la Carrera padre sin necesidad de conocer su ID de Salesforce.

## ✅ Verificación de Éxito
1.  Abre el App Launcher > **Materias**.
2.  Crea una Materia vinculada a la Carrera `DEV`.
3.  Asegúrate de que el "Código Externo" sea único (ej: `DEV-101`).

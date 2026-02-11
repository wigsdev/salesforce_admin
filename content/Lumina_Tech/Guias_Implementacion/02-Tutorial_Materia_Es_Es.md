# 🎓 Guía Técnica: Objeto Materia (Catálogo)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-001](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Catálogo), [HU-010](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Visibilidad)

---

## 🎯 Objetivo
Crear el objeto `Materia__c` y vincularlo fuertemente a una Carrera usando una relación Master-Detail.

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto
1.  Ve a **Setup** > **Object Manager**.
2.  Haz clic en **Create** > **Custom Object**.
3.  Completa los detalles:
    *   **Label**: `Materia`
    *   **Plural Label**: `Materias`
    *   **Object Name**: `Materia`
    *   **Record Name**: `Nombre de Materia`
    *   **Data Type**: Selecciona **Text**.
    *   **Allow Search**: ☑️ Marca la casilla.
4.  Haz clic en **Save**.

### Paso 2: Crear Relación Master-Detail (Hijo-Padre)
1.  En el menú izquierdo, ve a **Fields & Relationships**.
2.  Haz clic en **New**.
3.  Selecciona Data Type: **Master-Detail Relationship**. Haz clic en **Next**.
4.  En "Related To", selecciona **Carrera**. Haz clic en **Next**.
5.  **Field Label**: `Carrera`.
6.  **Field Name**: `Carrera`.
7.  **Sharing Setting**: Deja la opción por defecto ("Read/Write...").
8.  **Allow Reparenting**: ☑️ **Marca esta casilla** (Es vital para corregir errores).
9.  Haz clic en **Next**.
10. Haz clic en **Next** (Add to layouts).
11. Haz clic en **Save**.

### Paso 3: Crear Campos del Objeto (Business Fields)

#### 3.1 Subject Code (Código Único)
*Identificador académico (ej: MAT-101).*
1.  **New** > Data Type: **Text**. Next.
2.  **Field Label**: `Código de Materia`.
3.  **Field Name**: `Codigo_Materia`.
4.  **Length**: `20`.
5.  ☑️ **Required** & ☑️ **Unique**.
6.  **Next** > **Next** > **Save & New**.

#### 3.2 Credits (Créditos Horarios)
*Peso académico de la materia.*
1.  Data Type: **Number**. Next.
2.  **Field Label**: `Créditos`.
3.  **Field Name**: `Creditos`.
4.  Length: `2`. Decimals: `0`.
5.  ☑️ **Required**.
6.  **Next** > **Next** > **Save & New**.

#### 3.3 Subject Type (Tipo)
*Obligatoria u Optativa.*
1.  Data Type: **Picklist**. Next.
2.  **Field Label**: `Tipo de Materia`.
3.  **Field Name**: `Tipo_Materia`.
4.  Values:
    *   `Obligatoria`
    *   `Optativa`
5.  **Next** > **Next** > **Save & New**.

#### 3.4 Plan Year (Año del Plan)
*Año sugerido de cursada (1o, 2o, 3o...)*
1.  Data Type: **Number**. Next.
2.  **Field Label**: `Año del Plan`.
3.  **Field Name**: `Anio_Plan` (Usando convención 'ni').
4.  Length: `1`. Decimals: `0`.
5.  **Next** > **Next** > **Save & New**.

#### 3.5 Active (Estado)
1.  Data Type: **Checkbox**. Next.
2.  **Field Label**: `Activa`.
3.  **Field Name**: `Activa`.
4.  **Default Value**: `Checked`.
5.  **Next** > **Next** > **Save**.

---

## ✅ Verificación de Éxito
1.  Abre el App Launcher y busca "**Materias**".
2.  Haz clic en **New**.
3.  Intente guardar sin elegir Carrera.
    *   **Resultado**: Salesforce debe mostrar un error rojo obligando a usar la lupa para buscar una **Carrera**.
4.  Si borras una Carrera (Prueba destructiva), verifica que sus Materias también desaparezcan.

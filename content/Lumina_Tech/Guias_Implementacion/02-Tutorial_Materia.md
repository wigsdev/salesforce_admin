# 🎓 Guía Técnica: Objeto Materia (Catálogo)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-003](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Curricular)

---

## 🎯 Objetivo
Crear el objeto `Materia__c` y vincularlo fuertemente a una Carrera usando una relación Master-Detail.

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto
1.  Ve a **Setup** > **Object Manager**.
2.  Haz clic en **Create** > **Custom Object**.
3.  Completa los detalles:
    *   **Label**: `Materia`
    *   **Plural Label**: `Materias`
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

### Paso 3: Crear Campo "Año del Plan"
1.  Haz clic en **New** (en Fields & Relationships).
2.  Selecciona Data Type: **Number**. Haz clic en **Next**.
3.  **Field Label**: `Año del Plan`.
4.  **Length**: `1`. **Decimal Places**: `0`.
    *   *Nota*: Solo aceptará un dígito (ej: 1, 2, 3).
5.  Haz clic en **Next**.
6.  Haz clic en **Next**.
7.  Haz clic en **Save**.

---

## ✅ Verificación de Éxito
1.  Abre el App Launcher y busca "Materias".
2.  Haz clic en **New**.
3.  Intente guardar sin elegir Carrera.
    *   **Resultado**: Salesforce debe mostrar un error rojo obligando a usar la lupa para buscar una Carrera.
4.  Si borras una Carrera (Prueba destructiva), verifica que sus Materias también desaparezcan.

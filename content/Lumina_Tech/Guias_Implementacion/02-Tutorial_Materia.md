# 🎓 Guía Técnica: Objeto Materia (Catálogo)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-003 (Curricular)

---

## 🎯 Objetivo
Crear el objeto `Materia__c` y vincularlo fuertemente a una Carrera usando una relación Master-Detail.

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Materia`
    *   **Plural Label**: `Materias`
    *   **Record Name**: `Nombre de Materia`
    *   **Data Type**: **Text**
    *   **Deployment Status**: Deployed.
3.  **Save**.

### Paso 2: Crear Relación Master-Detail (Hijo-Padre)
1.  Vaya a **Fields & Relationships** > **New**.
2.  Seleccione Data Type: **Master-Detail Relationship**. Next.
3.  Related To: Seleccione **Carrera**. Next.
4.  **Field Label**: `Carrera`.
5.  **Field Name**: `Carrera`.
6.  **Sharing Setting**: Dejar en "Read/Write: Allows users with at least Read access...".
7.  **Allow Reparenting**: ☑️ Marcar esta casilla (Permite mover una materia de carrera si hubo error).
8.  **Next** > **Next** > **Save**.

### Paso 3: Crear Campo "Año del Plan"
1.  Click **New** en Fields & Relationships.
2.  Tipo: **Number**.
3.  Label: `Año del Plan`.
4.  Length: `1`. (Ej: 1ro, 2do, 3ro).
5.  **Next** > **Save**.

---

## ✅ Verificación de Éxito
1.  Intente crear una **Materia** nueva.
2.  Salesforce debe OBLIGARLO a seleccionar una **Carrera** (lupa).
3.  Si borra la Carrera padre, la Materia debería borrarse automáticamente (Cascade Delete).

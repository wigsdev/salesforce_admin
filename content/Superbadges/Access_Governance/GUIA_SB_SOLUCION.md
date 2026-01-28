# 🏆 Guía Maestra: Access Governance Superbadge

## Reto 1: Access & Permission Sets (El rompecabezas de licencias)
El objetivo era corregir los permisos de María, Tara y Rahul, pero nos encontramos con falta de licencias y permisos "sucios".

### Paso 1: Habilitar Fechas de Caducidad (Prerrequisito)
1.  Ve a **Setup > User Management Settings**.
2.  Activa: **Permission Set & Permission Set Group Assignments with Expiration Dates**.

### Paso 2: Limpieza de Licencias (El "Baile de las Sillas")
El problema principal era que Rahul ocupaba una licencia que necesitaban las vendedoras.

1.  Ve a **Users > Rahul Patel**.
2.  En **Permission Set License Assignments**, elimina la licencia `CRM User`. (Esto libera el asiento).
3.  En **Permission Set Assignments**, elimina cualquier permiso de administrador que tenga (ej. `Customize Application`).

### Paso 3: Limpiar el Grupo "Sales Representative" (El Error Oculto)
El grupo daba permisos de borrar porque estaba "sucio" por dentro.

1.  Ve a **Permission Set Groups > PERSONA: Sales Representative**.
2.  Haz clic en **Permission Sets in Group**.
3.  Selecciona y elimina el conjunto llamado `OPPORTUNITY: Sales - D` (Este era el culpable que daba acceso Delete).
4.  Si aparece la opción, dale a **Recalculate**.

### Paso 4: Asignaciones Correctas
Ahora que hay licencias y el grupo está limpio:

**Maria Gomez**:
1.  Quitar grupo `Sales Manager`.
2.  Agregar grupo `PERSONA: Sales Representative`.

**Tara Jenson**:
1.  Asegurar que tenga asignado `PERSONA: Sales Representative`.

**Rahul Patel (Acceso Temporal)**:
1.  Ve a **Permission Sets > PLATFORM: Customize Application**.
2.  Dale a **Manage Assignments > Add Assignment**.
3.  Selecciona a Rahul Patel.
4.  **IMPORTANTE**: En "Assignment Expiration", elige **Specific Date** (ej. 30 días).

---

## Reto 2: Monitor Data Changes (La fuga de datos)
El objetivo era rastrear cambios y borrar un dato sensible (tarjeta de crédito) usando Data Loader.

### Paso 1: Configurar Rastreo (History Tracking)
1.  **Setup > Object Manager > Opportunity > Fields & Relationships**.
2.  Clic en **Set History Tracking**.
3.  Activa la casilla principal y marca: `Amount`, `Close Date`, `Opportunity Owner`, `Stage`.
4.  **Page Layouts > Opportunity Layout**: Agrega la lista relacionada **Opportunity Field History**.

### Paso 2: El Reporte de Auditoría (Ojo con los filtros)
1.  Crea un nuevo reporte tipo **Opportunity Field History**.
2.  Guárdalo en una carpeta nueva llamada `Compliance Reports`.
3.  Nombre del reporte: `Opp Field History - Last 7 Days`.

**FILTROS (La clave del éxito)**:
*   **Show Me**: All opportunities (Todas).
*   **Date**: Edit Date / Last 7 Days.
*   **Field / New Value / Old Value**: Déjalo en **Any** (Cualquiera). ⚠️ No agregues filtros específicos aquí.

### Paso 3: Permiso para Borrar Historial
1.  **Setup > User Interface**: Activa **Delete from Field History**.
2.  Crea un Permission Set nuevo: `Delete Field History`.
3.  En **System Permissions**, activa `Delete from Field History`.
4.  Asígnatelo a ti mismo con fecha de expiración de **1 día**.

### Paso 4: Borrado Quirúrgico con Data Loader
1.  Obtén el ID de la cuenta "Grand Hotels & Resorts Ltd" desde la URL (ej. `001...`).
2.  En **dataloader.io > Export**:
    *   **Objeto**: `Account History`.
    *   **Filtro**: `Account ID =` (Pega el ID `001...`).
    *   **Campos a exportar**: `Id` (Account History ID), `Changed Field`, `New Value`, `Old Value`.
3.  Descarga el CSV y busca las filas con números de tarjeta de crédito.
4.  Copia los IDs de esas filas (empiezan por `017...`). Deben ser dos registros (uno de creación y otro de borrado).
5.  Crea un CSV simple con una columna `Id` y pega los códigos `017...`.
6.  En **dataloader.io > Delete**:
    *   Sube tu CSV y ejecuta el borrado.

---

## 🚨 Nota de Seguridad: El Filtro de Exportación (Paso Crítico)
En el Reto 2, Paso 4 (Exportación), recuerda este detalle visual para que no te salga el error de "0 resultados":

Cuando pongas el filtro en dataloader.io, verás dos menús desplegables.

*   ❌ **NO selecciones**: `Account History ID = 001...`
*   ✅ **SÍ selecciona**: `Account ID` (o Account) `= 001...`

**¿Por qué?** Porque el código que copiaste de la URL (`001...`) es el DNI de la Cuenta Padre, no del historial. Si le pides al sistema que busque un historial con DNI de cuenta, se confunde.

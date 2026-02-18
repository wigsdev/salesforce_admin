# 📘 GUÍA TÉCNICA: SOLUCIÓN SUPERBADGE DATA QUALITY & VALIDATION

**Módulo:** Data Quality and Validation Superbadge  
**Plataforma:** Salesforce Trailhead  
**Requisito Crítico:** Edición de Desarrollador con Configuración Especial

---

## ⚠️ 1. REQUISITOS PREVIOS (CRÍTICO)

Para completar este Superbadge exitosamente, **no se puede utilizar un Playground estándar**.

1.  **Registro:** Debe registrarse en la [Developer Edition con configuración especial](https://trailhead.salesforce.com/promo/orgs/superbadges-data-quality).
2.  **Conexión:** Conecte esta nueva organización a su cuenta de Trailhead.
3.  **Selección:** Antes de verificar cualquier reto, asegúrese de que esta organización específica esté seleccionada en el menú del reto.

---

## 🏆 RETO 1: ARREGLAR E IMPORTAR DATOS (FIX AND IMPORT DATA)

**Objetivo:** Normalizar los datos del campo `Lead Source` utilizando los datos heredados en `Lead Source Text`.

### 1.1. Exportación de Datos
1.  Navegar a **Setup** > **Dataloader.io** > **Launch Dataloader.io**.
2.  Clic en **New Task** > **Export**.
3.  Objeto: **Lead**.
4.  Seleccionar campos: `Id`, `Lead Source`, `Lead Source Text`.
5.  Clic en **Save & Run** y descargar el archivo CSV.

### 1.2. Limpieza de Datos (Excel/Sheets)
Abrir el CSV y actualizar la columna `Lead Source` basándose en la siguiente tabla de equivalencias:

| Valor en "Lead Source Text" | Valor correcto para "Lead Source" |
| :--- | :--- |
| `Website` | **Web** |
| `Call` _o_ `Phone` | **Phone Inquiry** |
| `RAS Referral` | **Partner Referral** |
| `Tradeshow Scan` | **Purchased List** |
| `SocialMedia` | **Other** |

*Nota: Guardar el archivo resultante como CSV (Delimitado por comas).*

### 1.3. Importación (Actualización)
1.  En Dataloader.io > **New Task** > **Import**.
2.  Operación: **Update** (Actualizar).
3.  Objeto: **Lead**.
4.  Cargar el CSV limpio.
5.  **Mapeo de Campos:**
    * `Lead ID` ➡️ `Lead ID`
    * `Lead Source` ➡️ `Lead Source`
6.  Clic en **Save & Run**.

---

## 🏆 RETO 2: GESTIÓN DE DUPLICADOS (MANAGE DUPLICATES)

**Objetivo:** Configurar reglas de coincidencia aproximada y fusionar registros existentes.

### 2.1. Regla de Coincidencia (Matching Rule)
1.  Ir a **Setup** > **Matching Rules**.
2.  Editar **Custom Contact Matching Rule**.
3.  Modificar criterio:
    * Field: **First Name**
    * Matching Method: **Fuzzy: First Name**
4.  Guardar (**Save**) y Activar (**Activate**).

### 2.2. Regla de Duplicados (Duplicate Rule)
1.  Ir a **Setup** > **Duplicate Rules**.
2.  Editar **Custom Contact Duplicate Rule**.
3.  Configurar acciones:
    * **Action on Create:** Block.
    * **Action on Edit:** Allow (Marcar "Alert" y "Report").
4.  Guardar (**Save**) y Activar (**Activate**).

### 2.3. Fusión de Registros (Merge)
1.  Abrir **App Launcher** > **Duplicate Record Sets**.
2.  Cambiar la vista de lista a **All** (Todos).
3.  Abrir cada registro (`DRS-XXXX`) individualmente.
4.  Ir a la pestaña **Related** > Seleccionar contactos > **Compare and Merge**.
5.  Confirmar la fusión.

---

## 🏆 RETO 3: REGLAS DE VALIDACIÓN (VALIDATION RULES)

**Ubicación:** Setup > Object Manager > **Opportunity** > Validation Rules.

### Regla 3.1: Opportunity_Closed_Stages
*Bloquea la modificación de la etapa si la oportunidad ya está cerrada.*

* **Rule Name:** `Opportunity_Closed_Stages`
* **Active:** ✅
* **Error Location:** Top of Page
* **Fórmula:**
    ```sql
    ISCHANGED(StageName) &&
    (ISPICKVAL(PRIORVALUE(StageName), "Closed Won") ||
    ISPICKVAL(PRIORVALUE(StageName), "Closed Lost"))
    ```
* **Mensaje:** `Cannot change stage once closed.`

### Regla 3.2: Opportunity_Closed_Backdate
*Impide fechas de cierre en el pasado (excepto para Opportunity Managers).*

* **Rule Name:** `Opportunity_Closed_Backdate`
* **Active:** ✅
* **Error Location:** Field: `CloseDate`
* **Fórmula:**
    ```sql
    CloseDate < TODAY() &&
    NOT($Permission.Opportunity_Manager)
    ```
* **Mensaje:** `Close Date cannot be in the past.`

### Regla 3.3: Opportunity_Amount_Owner_or_Admin
*Solo el propietario o un administrador pueden modificar el importe.*

* **Rule Name:** `Opportunity_Amount_Owner_or_Admin`
* **Active:** ✅
* **Error Location:** Field: `Amount`
* **Fórmula:**
    ```sql
    ISCHANGED(Amount) &&
    $User.Id <> OwnerId &&
    $Profile.Name <> "System Administrator"
    ```
* **Mensaje:** `Only Owner or Admin can change Amount.`

---

## 🏆 RETO 4: FLUJO DE AUTOMATIZACIÓN (FLOW)

**Objetivo:** Validar fechas de vencimiento en tareas para casos de alta prioridad.

### 4.1. Configuración General
* **Tipo:** Record-Triggered Flow.
* **Objeto:** Task.
* **Trigger:** A record is created.
* **Optimization:** **Fast Field Updates** (Actualizaciones rápidas de campos).

### 4.2. Recurso de Fórmula
* **Type:** Formula
* **API Name:** `OneWeek`
* **Data Type:** Date
* **Formula:** `{!$Flow.CurrentDate} + 7`

### 4.3. Elementos del Flujo (Paso a Paso)

**Paso A: Get Records (Obtener Caso)**
* **Label:** `Get High Priority Cases`
* **API Name:** `Get_High_Priority_Cases`
* **Object:** Case
* **Filter:** `Id` Equals `{!$Record.WhatId}`
* **Store:** Only the first record.

**Paso B: Decision (Verificar Prioridad)**
* **Label:** `Any High Priority Cases?`
* **API Name:** `Any_High_Priority_Cases`
* **Outcome Label:** `Yes - High Priority Found`
* **Outcome Condition:**
    * Resource: `{!Get_High_Priority_Cases.Priority}`
    * Operator: `Equals`
    * Value: `High`

**Paso C: Decision (Verificar Fecha)**
*(Conectar a la ruta "Yes" del paso anterior)*
* **Label:** `Is The ActivityDate Too Far Into The Future?`
* **API Name:** `Is_The_ActivityDate_Too_Far_Into_The_Future`
* **Outcome Label:** `Yes - Too Far Into The Future`
* **Outcome Condition:**
    * Resource: `{!$Record.ActivityDate}`
    * Operator: `Greater Than`
    * Value: `{!OneWeek}`

**Paso D: Custom Error (Mensaje de Error)**
*(Conectar a la ruta "Yes" del paso de fecha)*
* **Label:** `Error - ActivityDate Should Be Sooner`
* **API Name:** `Error_ActivityDate_Should_Be_Sooner`
* **Location:** Field `Due Date Only` (ActivityDate).
* **Error Message (Copia Exacta):**
    `High Priority cases need to be addressed quickly. Please set the due date no later than {!OneWeek}`

### 4.4. Finalización
1.  **Guardar** como:
    * Label: `Task Due Date`
    * API Name: `Task_Due_Date`
2.  **Activar (Activate)** el flujo.

---
**Fin del Documento.**
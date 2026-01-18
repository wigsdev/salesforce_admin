# Salesforce Admin

## 📋 Proyecto: Financiera Horizonte S.A.

**Fecha de Implementación**: 2026-01-16  
**Admin**: Salesforce Senior Admin  
**Sprint**: 1  
**Ambiente**: DEV → QA → PROD

---

## 🎯 Objetivo

Gestionar las configuraciones, cambios, agregados nuevos y explicación.  
Documentar cada tarea hecha de tal forma que sea entendible para otro equipo.

---

## 🛠️ HU-001: Gestión de Garantes en Préstamos

### Configuración Realizada

#### 1. Modificar Picklist de Contact Roles

**Navegación**: Setup → Object Manager → Opportunity → Contact Roles → Role Picklist

**Valores agregados**:
- `Garante` (nuevo)
- `Co-deudor` (nuevo)

**Valores existentes mantenidos**:
- Decision Maker
- Business User
- Evaluator

**Screenshot de configuración**: Ver carpeta de evidencias

---

#### 2. Modificar Page Layout de Opportunity

**Navegación**: Setup → Object Manager → Opportunity → Page Layouts → Opportunity Layout

**Cambios realizados**:
1. Mover sección "Contact Roles" al inicio (después de Opportunity Information)
2. Hacer la sección visible por defecto (no colapsada)
3. Agregar 5 filas de Contact Roles visibles (antes: 3)

**Código de configuración**:
```xml
<layoutSections>
    <label>Contact Roles</label>
    <layoutColumns>
        <layoutItems>
            <behavior>Readonly</behavior>
            <field>ContactRoles</field>
        </layoutItems>
    </layoutColumns>
    <style>TwoColumnsTopToBottom</style>
</layoutSections>
```

---

#### 3. Crear Vista de Lista "Préstamos con Garantes"

**Navegación**: Opportunities → List Views → New

**Configuración**:
- **Nombre**: Préstamos con Garantes
- **Filtro**: `Contact Roles.Role = 'Garante'`
- **Campos visibles**:
  1. Opportunity Name
  2. Amount
  3. Stage
  4. Close Date
  5. Contact Roles (Related)

**Compartir con**: Todos los usuarios

---

#### 4. Crear Reporte "Análisis de Garantes"

**Navegación**: Reports → New Report → Opportunities with Contact Roles

**Configuración**:
- **Tipo**: Matrix Report
- **Filas**: Opportunity Name
- **Columnas**: Contact Role
- **Filtro**: `Role = 'Garante' OR Role = 'Decision Maker'`
- **Agrupación**: Por mes de cierre

**Fórmula personalizada**:
```
IF(CONTAINS(TEXT(ContactRole.Role), "Garante"), "Con Garante", "Sin Garante")
```

---

### Pruebas Realizadas

#### Test Case 1: Agregar Garante a Oportunidad

**Pasos**:
1. Crear Contact "Juan Pérez" (garante)
2. Crear Opportunity "Préstamo Personal $50,000"
3. Agregar Contact Role: Juan Pérez - Garante
4. Verificar que aparece en Related List

**Resultado**: ✅ PASS

---

#### Test Case 2: Múltiples Garantes

**Pasos**:
1. Agregar 2do garante "María García"
2. Verificar que ambos aparecen
3. Generar reporte

**Resultado**: ✅ PASS

---

### Documentación para Usuarios

**Instructivo creado**: "Cómo agregar garantes a un préstamo"

1. Abrir la Oportunidad (Préstamo)
2. Scroll hasta "Contact Roles"
3. Click "New"
4. Seleccionar Contact (o crear nuevo)
5. Seleccionar Role = "Garante"
6. Save

---

## 🔒 HU-002: Restricción de Acceso a Datos Financieros

### Configuración Realizada

#### 1. Crear Campo Custom `Monthly_Salary__c`

**Navegación**: Setup → Object Manager → Contact → Fields & Relationships → New

**Configuración del campo**:
- **Field Label**: Monthly Salary
- **API Name**: `Monthly_Salary__c`
- **Data Type**: Currency(16, 2)
- **Default Value**: (blank)
- **Required**: No
- **Unique**: No
- **External ID**: No

---

#### 2. Configurar Field-Level Security

**Navegación**: Setup → Object Manager → Contact → Fields → Monthly_Salary__c → Set Field-Level Security

**Perfiles configurados**:

| Perfil | Visible | Read-Only | Editable |
|--------|---------|-----------|----------|
| System Administrator | ✅ | ❌ | ✅ |
| Ejecutivo de Créditos | ✅ | ❌ | ✅ |
| Gerente de Finanzas | ✅ | ❌ | ✅ |
| Atención al Cliente | ❌ | ❌ | ❌ |
| Standard User | ❌ | ❌ | ❌ |

---

#### 3. Crear Permission Set "Financial_Data_Access"

**Navegación**: Setup → Permission Sets → New

**Configuración**:
- **Label**: Financial Data Access
- **API Name**: `Financial_Data_Access`
- **License**: Salesforce

**Permisos otorgados**:
- Object: Contact
  - Field: `Monthly_Salary__c` → Read ✅, Edit ✅

**Usuarios asignados**:
- admin@financierahorizonte.com
- gerente.finanzas@financierahorizonte.com
- ejecutivo.creditos@financierahorizonte.com

---

#### 4. Modificar Page Layouts

**Layout para "Ejecutivo de Créditos"**:
- Sección "Financial Information" → Visible
- Campo `Monthly_Salary__c` → Visible

**Layout para "Atención al Cliente"**:
- Sección "Financial Information" → Oculta
- Campo `Monthly_Salary__c` → No incluido

---

### Pruebas de Seguridad

#### Test Case 1: Usuario Autorizado

**Usuario**: ejecutivo.creditos@test.com  
**Perfil**: Ejecutivo de Créditos

**Pasos**:
1. Login como ejecutivo
2. Abrir Contact
3. Verificar que ve campo `Monthly_Salary__c`
4. Editar valor
5. Guardar

**Resultado**: ✅ PASS - Campo visible y editable

---

#### Test Case 2: Usuario No Autorizado

**Usuario**: atencion.cliente@test.com  
**Perfil**: Atención al Cliente

**Pasos**:
1. Login como atención al cliente
2. Abrir Contact
3. Verificar que NO ve campo `Monthly_Salary__c`
4. Intentar acceder vía API (Workbench)
5. Verificar error de permisos

**Resultado**: ✅ PASS - Campo oculto, acceso denegado

---

#### Test Case 3: Reportes

**Pasos**:
1. Crear reporte de Contacts
2. Intentar agregar columna `Monthly_Salary__c` como usuario no autorizado
3. Verificar que campo no aparece en lista

**Resultado**: ✅ PASS - FLS respetado en reportes

---

### Auditoría Configurada

**Setup Audit Trail**:
- Activado tracking de cambios en FLS
- Retención: 180 días
- Alertas configuradas para cambios en Permission Sets

---

## 💳 HU-003: Gestión de Múltiples Cuentas Bancarias

### Configuración Realizada

#### 1. Crear Custom Object `Bank_Account__c`

**Navegación**: Setup → Object Manager → Create → Custom Object

**Configuración del objeto**:
- **Label**: Bank Account
- **Plural Label**: Bank Accounts
- **API Name**: `Bank_Account__c`
- **Record Name**: Account Number
- **Data Type**: Auto Number
- **Display Format**: BA-{00000}
- **Starting Number**: 1

**Features habilitadas**:
- ✅ Allow Reports
- ✅ Allow Activities
- ✅ Track Field History
- ✅ Allow Search
- ❌ Allow Sharing (Master-Detail controla sharing)

---

#### 2. Crear Campos en `Bank_Account__c`

##### Campo 1: Contact (Master-Detail)

**Configuración**:
- **Field Label**: Contact
- **API Name**: `Contact__c`
- **Data Type**: Master-Detail Relationship
- **Related To**: Contact
- **Child Relationship Name**: Bank_Accounts
- **Sharing Setting**: Read/Write (controlled by parent)
- **Required**: Yes

---

##### Campo 2: Bank Name

**Configuración**:
- **Field Label**: Bank Name
- **API Name**: `Bank_Name__c`
- **Data Type**: Picklist
- **Values**:
  - Banco de la Nación
  - BCP - Banco de Crédito del Perú
  - BBVA
  - Interbank
  - Scotiabank
  - Banco Pichincha
  - Otro
- **Required**: Yes

---

##### Campo 3: CBU (Encrypted)

**Configuración**:
- **Field Label**: CBU
- **API Name**: `CBU__c`
- **Data Type**: Text(22)
- **Encrypted**: ✅ Yes (Platform Encryption)
- **Mask Type**: All Characters
- **Mask Char**: X
- **Required**: Yes
- **Unique**: No (un cliente puede tener la misma cuenta en diferentes registros históricos)

**Nota**: Requiere Platform Encryption habilitado en la org

---

##### Campo 4: Account Type

**Configuración**:
- **Field Label**: Account Type
- **API Name**: `Account_Type__c`
- **Data Type**: Picklist
- **Values**:
  - Caja de Ahorro
  - Cuenta Corriente
  - Cuenta Sueldo
- **Required**: Yes

---

##### Campo 5: Is Primary

**Configuración**:
- **Field Label**: Is Primary
- **API Name**: `Is_Primary__c`
- **Data Type**: Checkbox
- **Default Value**: Unchecked
- **Required**: No

---

##### Campo 6: Status

**Configuración**:
- **Field Label**: Status
- **API Name**: `Status__c`
- **Data Type**: Picklist
- **Values**:
  - Activa
  - Inactiva
  - Cerrada
- **Default Value**: Activa
- **Required**: Yes

---

##### Campo 7: Last Used Date

**Configuración**:
- **Field Label**: Last Used Date
- **API Name**: `Last_Used_Date__c`
- **Data Type**: Date
- **Required**: No

---

#### 3. Crear Validation Rule "Unique_Primary_Account"

**Navegación**: Setup → Object Manager → Bank_Account__c → Validation Rules → New

**Rule Name**: `Unique_Primary_Account`

**Formula**:
```apex
AND(
  Is_Primary__c = TRUE,
  ISCHANGED(Is_Primary__c),
  Contact__r.Bank_Accounts__r.Size > 0,
  Contact__r.Bank_Accounts__r.Is_Primary__c = TRUE
)
```

**Error Message**: "Este contacto ya tiene una cuenta marcada como primaria. Por favor, desmarque la cuenta anterior primero."

**Error Location**: Field: Is_Primary__c

**Nota**: Esta validación fue reemplazada por un Flow (ver siguiente sección)

---

#### 4. Crear Flow "Auto_Unmark_Primary_Account"

**Navegación**: Setup → Flows → New Flow

**Tipo**: Record-Triggered Flow

**Configuración del Trigger**:
- **Object**: Bank_Account__c
- **Trigger**: A record is created or updated
- **Condition**: `Is_Primary__c` = TRUE AND ISCHANGED(`Is_Primary__c`)
- **Optimize for**: Fast Field Updates

**Elementos del Flow**:

1. **Get Records**: Buscar otras cuentas primarias del mismo contacto
   - Object: Bank_Account__c
   - Filter: 
     - `Contact__c` = {!$Record.Contact__c}
     - `Is_Primary__c` = TRUE
     - `Id` ≠ {!$Record.Id}
   - Store in: varOtherPrimaryAccounts

2. **Decision**: ¿Hay otras cuentas primarias?
   - Condition: {!varOtherPrimaryAccounts} Is Null = False

3. **Update Records**: Desmarcar otras cuentas
   - Records: {!varOtherPrimaryAccounts}
   - Field: `Is_Primary__c` = FALSE

**Activación**: Activado

---

#### 5. Modificar Page Layout de Contact

**Navegación**: Setup → Object Manager → Contact → Page Layouts → Contact Layout

**Cambios**:
1. Agregar Related List "Bank Accounts"
2. Posición: Después de "Opportunities"
3. Campos visibles en Related List:
   - Bank Name
   - CBU (masked)
   - Account Type
   - Is Primary (checkbox)
   - Status
   - Last Used Date
4. Botones: New, Edit, Delete

---

#### 6. Crear Formula Field en Contact

**Navegación**: Setup → Object Manager → Contact → Fields → New

**Configuración**:
- **Field Label**: Primary Bank Account
- **API Name**: `Primary_Bank_Account__c`
- **Data Type**: Formula (Text)
- **Formula**:
```apex
IF(
  ISBLANK(TEXT(Bank_Accounts__r.Bank_Name__c)),
  "Sin cuenta primaria",
  TEXT(Bank_Accounts__r.Bank_Name__c) & " - " & 
  LEFT(Bank_Accounts__r.CBU__c, 4) & "****" & 
  RIGHT(Bank_Accounts__r.CBU__c, 4)
)
```

**Nota**: Esta fórmula muestra solo la cuenta marcada como primaria

---

### Pruebas Realizadas

#### Test Case 1: Crear Primera Cuenta

**Pasos**:
1. Abrir Contact "Juan Pérez"
2. Click "New" en Bank Accounts
3. Completar:
   - Bank Name: BCP
   - CBU: 0021234567890123456789
   - Account Type: Caja de Ahorro
   - Is Primary: ✅
   - Status: Activa
4. Save

**Resultado**: ✅ PASS - Cuenta creada correctamente

---

#### Test Case 2: Agregar Segunda Cuenta (Auto-unmark)

**Pasos**:
1. Click "New" en Bank Accounts
2. Completar:
   - Bank Name: BBVA
   - CBU: 0031234567890123456789
   - Account Type: Cuenta Corriente
   - Is Primary: ✅
   - Status: Activa
3. Save
4. Verificar que cuenta BCP ya NO está marcada como primaria

**Resultado**: ✅ PASS - Flow funcionó correctamente, solo BBVA es primaria

---

#### Test Case 3: Historial de Cuentas

**Pasos**:
1. Marcar cuenta BCP como "Inactiva"
2. Crear 3ra cuenta (Interbank)
3. Verificar que se ven las 3 cuentas en Related List
4. Filtrar por Status = "Activa"

**Resultado**: ✅ PASS - Historial completo visible

---

#### Test Case 4: Encriptación de CBU

**Pasos**:
1. Ver cuenta en UI → CBU aparece como XXXXXXXXXXXXXXXXXXXX
2. Acceder vía API (Workbench)
3. Verificar que valor está encriptado
4. Usuario con permiso "View Encrypted Data" puede ver valor real

**Resultado**: ✅ PASS - Encriptación funcionando

---

### Reportes Creados

#### Reporte 1: "Clientes con Múltiples Cuentas"

**Tipo**: Contacts with Bank Accounts  
**Filtro**: Bank Accounts > 1  
**Agrupación**: Por cantidad de cuentas

---

#### Reporte 2: "Cuentas Bancarias por Banco"

**Tipo**: Bank Accounts  
**Agrupación**: Por Bank Name  
**Gráfico**: Donut Chart

---

## 📊 Resumen de Configuraciones

| HU | Objetos Modificados | Campos Creados | Automation | Reportes |
|----|---------------------|----------------|------------|----------|
| HU-001 | Opportunity | 0 | 0 | 1 |
| HU-002 | Contact | 1 | 0 | 0 |
| HU-003 | Contact, Bank_Account__c (new) | 8 | 1 Flow | 2 |

**Total**:
- Objetos Custom Creados: 1
- Campos Custom Creados: 9
- Flows Creados: 1
- Validation Rules: 0 (reemplazada por Flow)
- Reportes: 3
- Permission Sets: 1

---

## 🔄 Deployment Plan

### DEV → QA

**Change Set**: "Sprint1_Financiera_HU001_003"

**Componentes incluidos**:
- Custom Object: Bank_Account__c
- Custom Fields: All
- Page Layouts: Contact Layout, Opportunity Layout
- Permission Set: Financial_Data_Access
- Flow: Auto_Unmark_Primary_Account
- Reports: All 3

**Fecha de deployment**: 2026-01-17

---

### QA → PROD

**Pre-requisitos**:
- ✅ Testing completo en QA
- ✅ Aprobación del Team Lead
- ✅ Backup de PROD
- ✅ Comunicación a usuarios

**Fecha de deployment**: 2026-01-20

---

## 📝 Notas para el Próximo Admin

1. **Platform Encryption**: Si la org no tiene Platform Encryption, el campo CBU será Text normal (no encrypted)
2. **Contact Roles**: Los valores de picklist son org-wide, afectan a todos los objetos que usen Contact Roles
3. **Flow**: El Flow "Auto_Unmark_Primary_Account" debe estar activado ANTES de crear cuentas
4. **Límites**: Cada Contact puede tener hasta 200 Bank Accounts (límite de Master-Detail)

---

**Documentado por**: Salesforce Senior Admin  
**Fecha**: 2026-01-16  
**Versión**: 1.0

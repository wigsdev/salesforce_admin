# 🎓 Guía Técnica: Objeto Contacto (Alumno) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Consolidación Arquitectura G3/G6)
**Rol Responsable**: 🛡️ **Salesforce Admin**

---

## 🎯 Objetivo
Habilitar la gestión de alumnos utilizando el objeto estándar `Contact` de Salesforce. El Sprint 2 consolida esta decisión para aprovechar las herramientas nativas de Salesforce y estandarizar la identidad digital mediante un **External ID**.

## 🛠️ Procedimiento de Configuración

### Paso 1: Tipos de Registro (Record Types)
1.  Ve a **Setup** > **Object Manager** > **Contact**.
2.  **Record Types** > **New**.
    - **Label**: `Alumno`. **Developer Name**: `Alumno`.
    - **Active**: ☑️ SÍ.
3.  Configure el Layout para que muestre los campos académicos definidos abajo.

### Paso 2: Campos de Identidad (Core Alumno)
Añadir al objeto `Contact` los siguientes campos personalizados:

#### 2.1 Número de Documento (DNI/CÉDULA)
1. **New** > Data Type: **Text**.
2. **Field Label**: `Número de Documento`. **Field Name**: `Numero_Documento`.
3. **Length**: `20`.
4. ☑️ **Unique** (Case Insensitive).
5. ☑️ **External ID**: **MANDATORIO**. (Clave para data loader).

#### 2.2 Rol del Contacto (Picklist)
1. Data Type: **Picklist**.
2. **Field Label**: `Rol`. **Field Name**: `Rol`.
3. **Values**: `Alumno`, `Docente`, `Staff`. (☑️ **Required**).

#### 2.3 Estado de Pago (Picklist)
1. Data Type: **Picklist**.
2. **Field Label**: `Estado de Pago`. **Field Name**: `Estado_Pago`.
3. **Values**: `Al día`, `Moroso`.

### Paso 3: Identidad Digital (Fórmulas S2)
1. **Email Institucional**: Fórmula que genera `nombres.apellidos@lumina.edu.ar`.
2. **Usuario Sistema**: Fórmula `Numero_Documento__c & "@lumina.edu.ar"`.

---

## ✅ Verificación de Éxito
1.  Crea un Contacto con Record Type "Alumno".
2.  Verifica que el campo "Número de Documento" impide duplicados.
3.  Valida que el Email Institucional se genera automáticamente sin tildes ni espacios (Sanitizado).

## 📝 Resumen Técnico
| Campo | API Name | Tipo | External ID |
| :--- | :--- | :--- | :--- |
| Documento | `Numero_Documento__c` | Text | ✅ SÍ |
| Rol | `Rol__c` | Picklist | - |
| Email Inst. | `Email_Institucional__c` | Formula | - |

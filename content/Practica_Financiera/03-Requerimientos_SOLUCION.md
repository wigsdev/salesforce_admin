# 📋 Requerimientos - SOLUCIÓN COMPLETA
## Análisis y Soluciones de Salesforce Senior Admin

---

## Requerimiento 1: Los "Garantes"

### 🗣️ Gerente:

> "Tenemos un lío con los préstamos grandes. A veces el cliente principal no tiene ingresos suficientes y trae a un tío o a la esposa para que firmen como garantía. El problema es que hoy en la ficha del préstamo solo puedo poner un nombre. Mis vendedores están anotando los datos del garante en el campo de 'Notas' o 'Comentarios', y después nadie los llama porque no quedan registrados como clientes. Necesito que si viene un garante, quede pegado al préstamo pero que sepamos quién es".

---

### 🧠 Traducción del Consultor (Lo que piensa):

**Análisis del Problema**:
- El modelo de datos actual no soporta múltiples personas relacionadas a un préstamo.
- Los garantes son contactos válidos que deben ser rastreables y contactables.
- Necesitan mantener la relación entre Préstamo → Cliente Principal → Garante(s).

**Solución Técnica en Salesforce**:
1. **Objeto Principal**: `Opportunity` (Oportunidad) representa el préstamo.
2. **Objeto Relacionado**: `Contact` (Contacto) para tanto el cliente como los garantes.
3. **Objeto Junction**: Crear un objeto personalizado `Loan_Contact__c` (Contacto de Préstamo) para relacionar múltiples contactos con roles diferentes.

**Campos del objeto `Loan_Contact__c`**:
- `Loan__c` (Lookup a Opportunity) - Relación al préstamo
- `Contact__c` (Lookup a Contact) - Relación al contacto
- `Role__c` (Picklist) - Valores: "Cliente Principal", "Garante", "Co-deudor"
- `Guarantee_Percentage__c` (Number) - % de garantía si aplica

**Alternativa más simple**:
- Usar **Contact Roles** nativo de Salesforce en Opportunities
- Crear un nuevo valor en el picklist de roles: "Garante"
- Ventaja: No requiere desarrollo custom, es estándar

---

### 📝 Historia de Usuario para Trello:

**ID**: HU-001  
**Título**: Gestión de Garantes en Préstamos

**Como**: Ejecutivo de Créditos  
**Quiero**: Registrar múltiples garantes asociados a un préstamo con sus datos completos  
**Para**: Poder contactarlos cuando sea necesario y tener trazabilidad de quiénes respaldan cada crédito

**Criterios de Aceptación**:
- [ ] Puedo agregar uno o más garantes a una oportunidad de préstamo
- [ ] Cada garante tiene su ficha de contacto completa (teléfono, email, dirección)
- [ ] Puedo diferenciar visualmente quién es el cliente principal y quién es garante
- [ ] Los garantes aparecen en la vista de la oportunidad sin necesidad de buscarlos
- [ ] Puedo generar reportes de "Préstamos con Garantes" vs "Préstamos sin Garantes"

**Épica**: 🔵 Gestión de Clientes  
**Story Points**: 5  
**Prioridad**: Alta

**Notas Técnicas**:
- Usar Contact Roles en Opportunities
- Agregar valor "Garante" al picklist de roles
- Crear Page Layout personalizado para mostrar sección de Contact Roles prominente

---

## Requerimiento 2: El salario oculto

### 🗣️ Gerente:

> "Estoy preocupado por la privacidad. Resulta que cargamos cuánto ganan los clientes para calcular si pueden pagar la cuota. Pero el otro día me di cuenta de que los chicos de 'Atención al Cliente' (que solo deberían actualizar teléfonos o direcciones) pueden ver el sueldo exacto de la gente. Eso es peligroso. Ellos no necesitan saber cuánto gana el cliente para cambiarle el email. Quiero que ese dato solo lo vean los vendedores y nosotros los gerentes".

---

### 🧠 Traducción del Consultor (Lo que piensa):

**Análisis del Problema**:
- Problema de **Field-Level Security (FLS)** - Seguridad a nivel de campo.
- El campo `Annual_Income__c` o `Monthly_Salary__c` es visible para perfiles que no deberían tener acceso.
- Necesitan implementar el principio de "Least Privilege" (Mínimo Privilegio).

**Solución Técnica en Salesforce**:

1. **Field-Level Security**:
   - Ir a Setup → Object Manager → Contact → Fields → `Monthly_Salary__c`
   - Configurar FLS por perfil:
     - ✅ **Visible y Editable**: Perfil "Ejecutivo de Créditos", "Gerente de Finanzas"
     - ❌ **No Visible**: Perfil "Atención al Cliente", "Soporte"

2. **Page Layouts**:
   - Crear Page Layout específico para "Atención al Cliente" sin el campo de salario
   - Asignar Page Layout según perfil

3. **Permission Sets** (Recomendado):
   - Crear Permission Set "View_Financial_Data"
   - Asignar solo a usuarios que necesiten ver información sensible
   - Más flexible que modificar perfiles directamente

**Validación**:
- Probar con usuarios de diferentes perfiles
- Verificar que reportes y vistas de lista también respeten FLS

---

### 📝 Historia de Usuario para Trello:

**ID**: HU-002  
**Título**: Restricción de Acceso a Datos Financieros Sensibles

**Como**: Gerente de Finanzas  
**Quiero**: Que solo los vendedores y gerentes puedan ver el salario de los clientes  
**Para**: Proteger la privacidad de la información financiera y cumplir con políticas de seguridad de datos

**Criterios de Aceptación**:
- [ ] El perfil "Atención al Cliente" NO puede ver el campo `Monthly_Salary__c`
- [ ] El perfil "Ejecutivo de Créditos" SÍ puede ver y editar el campo
- [ ] El perfil "Gerente de Finanzas" SÍ puede ver y editar el campo
- [ ] Los usuarios de Atención al Cliente no ven el campo ni en la página del contacto, ni en reportes, ni en vistas de lista
- [ ] Se documenta qué perfiles tienen acceso a datos financieros

**Épica**: 🔴 Seguridad y Permisos  
**Story Points**: 3  
**Prioridad**: Crítica

**Notas Técnicas**:
- Configurar Field-Level Security en objeto Contact
- Crear Permission Set "Financial_Data_Access"
- Actualizar Page Layouts por perfil
- Documentar matriz de permisos

---

## Requerimiento 3: Las múltiples cuentas

### 🗣️ Gerente:

> "Cada vez que le tenemos que depositar el préstamo a un cliente es un drama. Hoy en la ficha del cliente tenemos un espacio para poner su CBU (número de cuenta bancaria). Pero muchos clientes tienen dos o tres cuentas, o cambian de banco. Cuando pasa eso, mis empleados borran la cuenta vieja y escriben la nueva encima. El problema es que si el pago rebota, no sabemos a qué cuenta anterior intentamos transferir porque ya la borraron. Necesito guardar todas las cuentas que tenga el cliente y marcar cuál es la favorita para usar ahora".

---

### 🧠 Traducción del Consultor (Lo que piensa):

**Análisis del Problema**:
- Relación **1 a Muchos** (Un cliente puede tener múltiples cuentas bancarias).
- Necesitan **historial completo** de cuentas sin perder información.
- Requieren un **flag de "Cuenta Activa/Preferida"**.

**Solución Técnica en Salesforce**:

1. **Crear Objeto Personalizado**: `Bank_Account__c` (Cuenta Bancaria)

**Campos del objeto `Bank_Account__c`**:
- `Contact__c` (Master-Detail a Contact) - Relación al cliente
- `Bank_Name__c` (Picklist) - Banco (Galicia, Santander, BBVA, etc.)
- `Account_Number__c` (Text Encrypted) - Número de cuenta (encriptado por seguridad)
- `CBU__c` (Text 22 caracteres) - Clave Bancaria Uniforme
- `Account_Type__c` (Picklist) - Tipo: "Caja de Ahorro", "Cuenta Corriente"
- `Is_Primary__c` (Checkbox) - Marca la cuenta preferida
- `Status__c` (Picklist) - Estado: "Activa", "Inactiva", "Cerrada"
- `Created_Date__c` (Date) - Fecha de registro
- `Last_Used_Date__c` (Date) - Última vez que se usó

2. **Validation Rule**: Solo una cuenta puede estar marcada como `Is_Primary__c = TRUE` por contacto.

3. **Related List**: Mostrar todas las cuentas bancarias en la página del Contact.

4. **Formula Field en Contact**: `Primary_Bank_Account__c` que muestre la cuenta activa actual.

**Beneficios**:
- Historial completo de cuentas
- Auditoría de cambios
- Trazabilidad de transacciones fallidas

---

### 📝 Historia de Usuario para Trello:

**ID**: HU-003  
**Título**: Gestión de Múltiples Cuentas Bancarias por Cliente

**Como**: Analista de Desembolsos  
**Quiero**: Registrar todas las cuentas bancarias de un cliente y marcar cuál es la activa  
**Para**: Tener historial completo de cuentas y saber a cuál transferir sin perder información histórica

**Criterios de Aceptación**:
- [ ] Puedo agregar múltiples cuentas bancarias a un cliente
- [ ] Cada cuenta tiene: Banco, CBU, Tipo de cuenta, Estado
- [ ] Solo UNA cuenta puede estar marcada como "Preferida" a la vez
- [ ] Puedo ver el historial completo de cuentas (activas e inactivas)
- [ ] Al marcar una nueva cuenta como preferida, la anterior se desmarca automáticamente
- [ ] Puedo generar reportes de "Clientes con múltiples cuentas"
- [ ] El CBU está encriptado por seguridad

**Épica**: 🟢 Automatización de Procesos  
**Story Points**: 8  
**Prioridad**: Alta

**Notas Técnicas**:
- Crear objeto custom `Bank_Account__c`
- Relación Master-Detail con Contact
- Validation Rule para único `Is_Primary__c`
- Usar Platform Encryption para campo CBU
- Flow para auto-desmarcar cuentas anteriores al marcar nueva como primaria

---

## 📊 Resumen de Soluciones

| Requerimiento | Solución Salesforce | Complejidad | Objetos Involucrados |
|---------------|---------------------|-------------|---------------------|
| **Garantes** | Contact Roles en Opportunities | Media | Opportunity, Contact |
| **Salario Oculto** | Field-Level Security + Permission Sets | Baja | Contact (permisos) |
| **Múltiples Cuentas** | Objeto Custom `Bank_Account__c` | Alta | Contact, Bank_Account__c |

---

## 🎯 Épicas Identificadas

- 🔵 **Gestión de Clientes** - HU-001
- 🔴 **Seguridad y Permisos** - HU-002
- 🟢 **Automatización de Procesos** - HU-003

**Total Story Points**: 16 puntos

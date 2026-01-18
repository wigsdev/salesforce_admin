# Business Analyst

## 📋 Proyecto: Financiera Horizonte S.A.

**Fecha de Análisis**: 2026-01-16  
**Analista**: Equipo Salesforce Admin  
**Cliente**: Financiera Horizonte S.A.

---

## 🎯 Objetivo del Análisis

Trasladar las palabras del cliente al ambiente de Salesforce, identificando objetos, campos y relaciones necesarias para resolver sus necesidades de negocio.

---

## 📝 Requerimientos del Cliente (Raw)

### Requerimiento 1: Los "Garantes"

**Palabras del Gerente**:
> "Tenemos un lío con los préstamos grandes. A veces el cliente principal no tiene ingresos suficientes y trae a un tío o a la esposa para que firmen como garantía. El problema es que hoy en la ficha del préstamo solo puedo poner un nombre. Mis vendedores están anotando los datos del garante en el campo de 'Notas' o 'Comentarios', y después nadie los llama porque no quedan registrados como clientes. Necesito que si viene un garante, quede pegado al préstamo pero que sepamos quién es".

**Análisis del Problema**:
- ❌ **Problema actual**: Solo se puede asociar 1 contacto por préstamo
- ❌ **Workaround actual**: Datos en campos de texto libre (Notas/Comentarios)
- ❌ **Consecuencia**: Pérdida de información, garantes no contactables
- ✅ **Necesidad real**: Relación 1:N entre Préstamo y Contactos con roles diferenciados

**Traducción a Salesforce**:
- **Objeto Principal**: `Opportunity` (representa el Préstamo)
- **Objeto Relacionado**: `Contact` (Cliente Principal y Garantes)
- **Funcionalidad**: Contact Roles (nativo de Salesforce)
- **Nuevo valor en Picklist**: "Garante" en Contact Role

**Preguntas de Indagación Realizadas**:
1. ✅ ¿Cuántos garantes puede tener un préstamo? → Respuesta: Hasta 2-3 máximo
2. ✅ ¿Los garantes deben tener ficha completa? → Respuesta: Sí, con teléfono y email
3. ✅ ¿Necesitan reportes de garantes? → Respuesta: Sí, "Préstamos con/sin Garantes"
---

### Requerimiento 2: El Salario Oculto

**Palabras del Gerente**:
> "Estoy preocupado por la privacidad. Resulta que cargamos cuánto ganan los clientes para calcular si pueden pagar la cuota. Pero el otro día me di cuenta de que los chicos de 'Atención al Cliente' (que solo deberían actualizar teléfonos o direcciones) pueden ver el sueldo exacto de la gente. Eso es peligroso. Ellos no necesitan saber cuánto gana el cliente para cambiarle el email. Quiero que ese dato solo lo vean los vendedores y nosotros los gerentes".

**Análisis del Problema**:
- ❌ **Problema actual**: Todos los perfiles ven el campo `Monthly_Salary__c`
- ❌ **Riesgo**: Violación de privacidad, posible fuga de información sensible
- ❌ **Principio violado**: Least Privilege (Mínimo Privilegio)
- ✅ **Necesidad real**: Seguridad a nivel de campo (Field-Level Security)

**Traducción a Salesforce**:
- **Objeto**: `Contact`
- **Campo sensible**: `Monthly_Salary__c` (Currency)
- **Solución**: Field-Level Security (FLS) + Permission Sets
- **Perfiles afectados**:
  - ✅ Visible: "Ejecutivo de Créditos", "Gerente de Finanzas"
  - ❌ No Visible: "Atención al Cliente", "Soporte"

**Preguntas de Indagación Realizadas**:
1. ✅ ¿Qué otros campos son sensibles? → Respuesta: Solo el salario por ahora
2. ✅ ¿Necesitan auditoría de quién ve el campo? → Respuesta: Sí, en el futuro
3. ✅ ¿Hay excepciones temporales? → Respuesta: No, la regla es estricta

---

### Requerimiento 3: Las Múltiples Cuentas

**Palabras del Gerente**:
> "Cada vez que le tenemos que depositar el préstamo a un cliente es un drama. Hoy en la ficha del cliente tenemos un espacio para poner su CBU (número de cuenta bancaria). Pero muchos clientes tienen dos o tres cuentas, o cambian de banco. Cuando pasa eso, mis empleados borran la cuenta vieja y escriben la nueva encima. El problema es que si el pago rebota, no sabemos a qué cuenta anterior intentamos transferir porque ya la borraron. Necesito guardar todas las cuentas que tenga el cliente y marcar cuál es la favorita para usar ahora".

**Análisis del Problema**:
- ❌ **Problema actual**: Solo 1 campo de texto para CBU en Contact
- ❌ **Workaround actual**: Sobrescribir el campo (pérdida de historial)
- ❌ **Consecuencia**: No hay trazabilidad de transacciones fallidas
- ✅ **Necesidad real**: Relación 1:N (Un cliente → Múltiples cuentas bancarias)

**Traducción a Salesforce**:
- **Objeto Principal**: `Contact` (Cliente)
- **Objeto Custom Nuevo**: `Bank_Account__c` (Cuenta Bancaria)
- **Relación**: Master-Detail (Contact → Bank_Account__c)
- **Campos clave**:
  - `Bank_Name__c` (Picklist)
  - `CBU__c` (Text 22, Encrypted)
  - `Is_Primary__c` (Checkbox)
  - `Status__c` (Picklist: Activa, Inactiva, Cerrada)

**Preguntas de Indagación Realizadas**:
1. ✅ ¿Cuántas cuentas máximo por cliente? → Respuesta: No hay límite, pero promedio 2-3
2. ✅ ¿Necesitan historial de cambios? → Respuesta: Sí, fundamental para auditoría
3. ✅ ¿El CBU debe estar encriptado? → Respuesta: Sí, por seguridad

---

## 📊 Resumen de Análisis

| Requerimiento | Objeto Principal | Solución Salesforce | Complejidad |
|---------------|------------------|---------------------|-------------|
| Garantes | Opportunity + Contact | Contact Roles (nativo) | Media |
| Salario Oculto | Contact | Field-Level Security | Baja |
| Múltiples Cuentas | Contact + Bank_Account__c | Custom Object + Master-Detail | Alta |

---

## ✅ Entregables del Análisis

1. ✅ Documento de requerimientos traducidos
2. ✅ Diagrama de modelo de datos (ver carpeta Practica_Financiera)
3. ✅ 3 Historias de Usuario (HU-001, HU-002, HU-003)
4. ✅ Criterios de Aceptación definidos (17 total)
5. ✅ Story Points estimados (16 total)

---

**Próximo paso**: Pasar al Salesforce Consultant para proponer soluciones técnicas detalladas.

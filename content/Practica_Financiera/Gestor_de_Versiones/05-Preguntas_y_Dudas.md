# Preguntas y Dudas

## 📋 Proyecto: Financiera Horizonte S.A.

**Sprint**: 1  
**Última actualización**: 5 Febrero 2026

---

## 🎯 Objetivo

Registrar todas las dudas y preguntas que se tengan sobre los requerimientos o posibles soluciones.

---

## ❓ Preguntas Generales del Proyecto

### P1: ¿Qué edición de Salesforce tiene el cliente?

**Fecha**: 6 Enero 2026  
**Preguntado por**: Salesforce Consultant  
**Dirigido a**: Cliente

**Pregunta**: ¿Qué edición de Salesforce están usando actualmente? (Professional, Enterprise, Unlimited)

**Respuesta**: Enterprise Edition

**Impacto**: 
- ✅ Tenemos acceso a Platform Encryption (necesario para HU-003)
- ✅ Límite de 200 objetos custom (suficiente)
- ✅ API disponible para integraciones futuras

**Estado**: ✅ Resuelta

---

### P2: ¿Tienen ambientes separados (DEV, QA, PROD)?

**Fecha**: 6 Enero 2026  
**Preguntado por**: Salesforce Admin  
**Dirigido a**: Cliente

**Pregunta**: ¿Ya tienen ambientes de desarrollo y testing configurados?

**Respuesta**: No, solo tienen PROD. Necesitan ayuda para crear DEV y QA.

**Impacto**:
- ⚠️ Debemos crear Sandboxes antes de empezar
- ⚠️ Incluir en el alcance del proyecto

**Acción tomada**: 
- Crear Developer Sandbox (DEV)
- Crear Partial Copy Sandbox (QA)
- Documentar credenciales en archivos 11, 12, 13

**Estado**: ✅ Resuelta

---

### P3: ¿Cuántos usuarios tiene la organización?

**Fecha**: 6 Enero 2026  
**Preguntado por**: Business Analyst  
**Dirigido a**: Cliente

**Pregunta**: ¿Cuántos usuarios activos tienen? ¿Cuántos por perfil?

**Respuesta**:
- Ejecutivos de Créditos: 15
- Gerentes de Finanzas: 3
- Atención al Cliente: 8
- Administradores: 2
- **Total**: 28 usuarios

**Impacto**:
- ✅ Dentro de límites de licencias
- ✅ Permission Sets manejables

**Estado**: ✅ Resuelta

---

## ❓ Preguntas sobre HU-001 (Garantes)

### P4: ¿Cuántos garantes máximo por préstamo?

**Fecha**: 8 Enero 2026  
**Preguntado por**: Business Analyst  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: ¿Existe un límite de garantes por préstamo?

**Respuesta**: Normalmente 1-2, máximo 3 en casos excepcionales.

**Impacto**:
- ✅ Contact Roles soporta ilimitados
- ✅ No necesitamos validación de límite

**Estado**: ✅ Resuelta

---

### P5: ¿Los garantes deben firmar documentos?

**Fecha**: 8 Enero 2026  
**Preguntado por**: Salesforce Consultant  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: ¿Necesitan integración con sistema de firma electrónica para garantes?

**Respuesta**: Sí, pero es para Sprint 2. Por ahora solo necesitan registrar quién es el garante.

**Impacto**:
- ✅ Sprint 1: Solo registro de garantes
- ⏭️ Sprint 2: Integración con DocuSign (futuro)

**Estado**: ✅ Resuelta - Fuera del alcance de Sprint 1

---

### P6: ¿Necesitan calcular % de garantía?

**Fecha**: 8 Enero 2026  
**Preguntado por**: Salesforce Consultant  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: ¿Cada garante cubre un porcentaje específico del préstamo?

**Respuesta**: No, por ahora solo necesitan saber quién es garante. El % se calcula en otro sistema.

**Impacto**:
- ✅ Confirma que Contact Roles es suficiente
- ✅ No necesitamos Junction Object con campos adicionales

**Estado**: ✅ Resuelta

---

## ❓ Preguntas sobre HU-002 (Salario Oculto)

### P7: ¿Qué otros campos son sensibles?

**Fecha**: 13 Enero 2026  
**Preguntado por**: Salesforce Admin  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: Además del salario, ¿hay otros campos que deban restringirse?

**Respuesta**: Por ahora solo el salario. En el futuro podrían agregar "Score Crediticio".

**Impacto**:
- ✅ Sprint 1: Solo `Monthly_Salary__c`
- ⏭️ Sprint 2-3: Posible campo `Credit_Score__c`

**Estado**: ✅ Resuelta

---

### P8: ¿Necesitan auditoría de quién accede al campo?

**Fecha**: 13 Enero 2026  
**Preguntado por**: Salesforce Consultant  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: ¿Necesitan saber quién y cuándo accede al campo de salario?

**Respuesta**: Sí, es importante para compliance.

**Impacto**:
- ✅ Activar Field History Tracking en `Monthly_Salary__c`
- ✅ Configurar Setup Audit Trail (ya incluido)

**Acción tomada**:
- Field History Tracking activado
- Retención de 180 días

**Estado**: ✅ Resuelta

---

### P9: ¿Hay excepciones temporales de acceso?

**Fecha**: 13 Enero 2026  
**Preguntado por**: Business Analyst  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: ¿Alguna vez un usuario de Atención al Cliente necesitaría ver el salario temporalmente?

**Respuesta**: No, la regla es estricta. Si necesitan acceso, deben cambiar de perfil.

**Impacto**:
- ✅ No necesitamos lógica de excepciones
- ✅ FLS es suficiente

**Estado**: ✅ Resuelta

---

## ❓ Preguntas sobre HU-003 (Múltiples Cuentas)

### P10: ¿Cuántas cuentas máximo por cliente?

**Fecha**: 20 Enero 2026  
**Preguntado por**: Salesforce Consultant  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: ¿Existe un límite de cuentas bancarias por cliente?

**Respuesta**: No hay límite, pero el promedio es 2-3 cuentas.

**Impacto**:
- ✅ Master-Detail soporta hasta 200 registros relacionados
- ✅ Más que suficiente

**Estado**: ✅ Resuelta

---

### P11: ¿El CBU debe estar encriptado?

**Fecha**: 20 Enero 2026  
**Preguntado por**: Salesforce Admin  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: ¿Es necesario encriptar el CBU por seguridad?

**Respuesta**: Sí, es información financiera sensible.

**Impacto**:
- ✅ Usar Platform Encryption
- ⚠️ Requiere configuración adicional en la org

**Acción tomada**:
- Platform Encryption habilitado
- Campo `CBU__c` configurado como Encrypted

**Estado**: ✅ Resuelta

---

### P12: ¿Qué pasa si marcan 2 cuentas como primarias simultáneamente?

**Fecha**: 20 Enero 2026  
**Preguntado por**: Salesforce Consultant  
**Dirigido a**: Equipo

**Pregunta**: ¿Usamos Validation Rule o Flow para evitar múltiples cuentas primarias?

**Respuesta del equipo**: Flow es mejor porque auto-corrige en lugar de bloquear.

**Impacto**:
- ✅ Flow "Auto_Unmark_Primary_Account" creado
- ✅ Mejor UX (no muestra error, simplemente desmarca la anterior)

**Estado**: ✅ Resuelta

---

### P13: ¿Necesitan historial de transacciones por cuenta?

**Fecha**: 20 Enero 2026  
**Preguntado por**: Business Analyst  
**Dirigido a**: Gerente de Finanzas

**Pregunta**: ¿Necesitan registrar cada vez que se usa una cuenta para un depósito?

**Respuesta**: Sí, pero eso lo maneja su sistema bancario. En Salesforce solo necesitan actualizar `Last_Used_Date__c`.

**Impacto**:
- ✅ Campo `Last_Used_Date__c` incluido
- ⏭️ Integración con sistema bancario (Sprint 3)

**Estado**: ✅ Resuelta

---

## ❓ Preguntas Técnicas del Equipo

### P14: ¿Usamos Change Sets o Metadata API para deployment?

**Fecha**: 27 Enero 2026  
**Preguntado por**: Salesforce Admin  
**Dirigido a**: Equipo

**Pregunta**: ¿Qué método de deployment usamos?

**Respuesta del equipo**: Change Sets para Sprint 1 (más simple). Metadata API para sprints futuros.

**Impacto**:
- ✅ Change Set creado: "Sprint1_Financiera_HU001_003"
- ✅ Documentado en archivo 03-Salesforce_Admin.md

**Estado**: ✅ Resuelta

---

### P15: ¿Necesitamos crear datos de prueba en QA?

**Fecha**: 27 Enero 2026  
**Preguntado por**: Tester QA  
**Dirigido a**: Equipo

**Pregunta**: ¿Usamos datos reales (anonimizados) o creamos datos ficticios?

**Respuesta del equipo**: Datos ficticios para evitar problemas de privacidad.

**Impacto**:
- ✅ Crear script de datos de prueba
- ✅ 50 Contacts, 100 Opportunities, 150 Bank Accounts

**Acción tomada**:
- Data Loader usado para cargar datos de prueba
- CSV files guardados en carpeta de evidencias

**Estado**: ✅ Resuelta

---

## 📊 Resumen de Preguntas

| Categoría | Total | Resueltas | Pendientes |
|-----------|-------|-----------|------------|
| Generales | 3 | 3 | 0 |
| HU-001 | 3 | 3 | 0 |
| HU-002 | 3 | 3 | 0 |
| HU-003 | 4 | 4 | 0 |
| Técnicas | 2 | 2 | 0 |
| **TOTAL** | **15** | **15** | **0** |

---

## ✅ Estado

Todas las preguntas y dudas del Sprint 1 han sido resueltas. No hay bloqueadores pendientes.

---

## 📝 Lecciones Aprendidas

1. **Hacer preguntas tempranas**: Las preguntas P4, P6 y P12 nos ahorraron mucho retrabajo al confirmar que Contact Roles era suficiente.

2. **Documentar respuestas**: Tener este registro ayuda a justificar decisiones técnicas.

3. **Involucrar al cliente**: Las respuestas del Gerente de Finanzas fueron clave para priorizar correctamente.

4. **Preguntas técnicas en equipo**: Las decisiones de deployment y datos de prueba se tomaron rápido por tener al equipo alineado.

---

**Última actualización**: 5 Febrero 2026  
**Próximo Sprint**: Nuevas preguntas se agregarán en archivo 06-Investigaciones.md

# Tester QA

## 📋 Proyecto: Financiera Horizonte S.A.

**Fecha de Testing**: 22 Enero - 5 Febrero 2026  
**QA Tester**: Equipo QA  
**Sprint**: 1  
**Ambiente de Testing**: QA Sandbox

---

## 🎯 Objetivo

Registrar que tarea se testeo, sobre que usuarios y si el requerimiento se cumplió o algo falló y debe volver al backlog como BUG.

---

## 🧪 Plan de Testing

### Estrategia de Testing

1. **Functional Testing**: Verificar que cada funcionalidad cumple con los criterios de aceptación
2. **Security Testing**: Validar permisos y Field-Level Security
3. **Integration Testing**: Verificar que las funcionalidades trabajan juntas
4. **User Acceptance Testing (UAT)**: Simular escenarios reales de usuario

---

## ✅ HU-001: Gestión de Garantes en Préstamos

### Criterios de Aceptación a Verificar

- [ ] Puedo agregar uno o más garantes a una oportunidad de préstamo
- [ ] Cada garante tiene su ficha de contacto completa (teléfono, email, dirección)
- [ ] Puedo diferenciar visualmente quién es el cliente principal y quién es garante
- [ ] Los garantes aparecen en la vista de la oportunidad sin necesidad de buscarlos
- [ ] Puedo generar reportes de "Préstamos con Garantes" vs "Préstamos sin Garantes"

---

### Test Case 1.1: Agregar Un Garante

**ID**: TC-HU001-01  
**Prioridad**: Alta  
**Fecha**: 22 Enero 2026

**Pre-condiciones**:
- Usuario con perfil "Ejecutivo de Créditos"
- Ambiente QA con datos de prueba

**Pasos**:
1. Login como: `ejecutivo.qa@financiera.test`
2. Navegar a Opportunities
3. Abrir "Préstamo Personal - Juan Pérez - $50,000"
4. Scroll a sección "Contact Roles"
5. Click "New"
6. Buscar Contact "María García"
7. Seleccionar Role = "Garante"
8. Click "Save"

**Resultado Esperado**:
- María García aparece en Contact Roles con rol "Garante"
- Juan Pérez aparece como "Decision Maker"

**Resultado Obtenido**: ✅ **PASS**
- María García agregada correctamente
- Ambos contactos visibles en Related List
- Screenshot: `QA_HU001_TC01_PASS.png`

**Testeado por**: Ana Rodríguez (QA)  
**Fecha**: 22 Enero 2026 10:30

---

### Test Case 1.2: Agregar Múltiples Garantes

**ID**: TC-HU001-02  
**Prioridad**: Alta  
**Fecha**: 22 Enero 2026

**Pasos**:
1. Continuar con la oportunidad anterior
2. Agregar 2do garante: "Carlos López"
3. Agregar 3er garante: "Ana Martínez"
4. Verificar que los 3 garantes + cliente principal aparecen

**Resultado Esperado**:
- 4 Contact Roles totales (1 Decision Maker + 3 Garantes)

**Resultado Obtenido**: ✅ **PASS**
- Los 4 contactos visibles
- Roles diferenciados correctamente

**Testeado por**: Ana Rodríguez (QA)  
**Fecha**: 22 Enero 2026 10:45

---

### Test Case 1.3: Reporte de Préstamos con Garantes

**ID**: TC-HU001-03  
**Prioridad**: Media  
**Fecha**: 22 Enero 2026

**Pasos**:
1. Navegar a Reports
2. Abrir "Análisis de Garantes"
3. Ejecutar reporte
4. Verificar que muestra préstamos con y sin garantes

**Resultado Esperado**:
- Reporte muestra columna "Con Garante" / "Sin Garante"
- Datos correctos

**Resultado Obtenido**: ✅ **PASS**
- Reporte funciona correctamente
- 15 préstamos con garantes, 8 sin garantes

**Testeado por**: Ana Rodríguez (QA)  
**Fecha**: 22 Enero 2026 11:00

---

### Test Case 1.4: Editar Garante

**ID**: TC-HU001-04  
**Prioridad**: Baja  
**Fecha**: 22 Enero 2026

**Pasos**:
1. Abrir Contact Role de María García
2. Cambiar Role de "Garante" a "Co-deudor"
3. Guardar
4. Verificar cambio

**Resultado Esperado**:
- Role actualizado correctamente

**Resultado Obtenido**: ✅ **PASS**

**Testeado por**: Ana Rodríguez (QA)  
**Fecha**: 22 Enero 2026 11:15

---

### Test Case 1.5: Eliminar Garante

**ID**: TC-HU001-05  
**Prioridad**: Media  
**Fecha**: 22 Enero 2026

**Pasos**:
1. Seleccionar Contact Role de Ana Martínez
2. Click "Delete"
3. Confirmar eliminación
4. Verificar que ya no aparece

**Resultado Esperado**:
- Contact Role eliminado
- Contact (Ana Martínez) sigue existiendo en el sistema

**Resultado Obtenido**: ✅ **PASS**

**Testeado por**: Ana Rodríguez (QA)  
**Fecha**: 22 Enero 2026 11:30

---

### Resumen HU-001

| Criterio de Aceptación | Estado | Test Cases |
|------------------------|--------|------------|
| Agregar múltiples garantes | ✅ PASS | TC-01, TC-02 |
| Ficha completa de contacto | ✅ PASS | TC-01 |
| Diferenciación visual | ✅ PASS | TC-01, TC-02 |
| Visibilidad en oportunidad | ✅ PASS | TC-01 |
| Reportes | ✅ PASS | TC-03 |

**Total Test Cases**: 5  
**Passed**: 5  
**Failed**: 0  
**Blocked**: 0

**Estado Final**: ✅ **APROBADO PARA PRODUCCIÓN**

---

## 🔒 HU-002: Restricción de Acceso a Datos Financieros

### Criterios de Aceptación a Verificar

- [ ] El perfil "Atención al Cliente" NO puede ver el campo Monthly_Salary__c
- [ ] El perfil "Ejecutivo de Créditos" SÍ puede ver y editar el campo
- [ ] El perfil "Gerente de Finanzas" SÍ puede ver y editar el campo
- [ ] Los usuarios de Atención al Cliente no ven el campo en reportes ni vistas
- [ ] Se documenta qué perfiles tienen acceso a datos financieros

---

### Test Case 2.1: Usuario Autorizado - Ver Campo

**ID**: TC-HU002-01  
**Prioridad**: Crítica  
**Fecha**: 28 Enero 2026

**Usuario de Prueba**: `ejecutivo.qa@financiera.test`  
**Perfil**: Ejecutivo de Créditos

**Pasos**:
1. Login como ejecutivo de créditos
2. Navegar a Contacts
3. Abrir "Juan Pérez"
4. Verificar que campo "Monthly Salary" es visible
5. Verificar valor: $5,000

**Resultado Esperado**:
- Campo visible en sección "Financial Information"
- Valor mostrado correctamente

**Resultado Obtenido**: ✅ **PASS**
- Campo visible
- Valor correcto
- Screenshot: `QA_HU002_TC01_PASS.png`

**Testeado por**: Carlos Méndez (QA)  
**Fecha**: 28 Enero 2026 09:00

---

### Test Case 2.2: Usuario Autorizado - Editar Campo

**ID**: TC-HU002-02  
**Prioridad**: Crítica  
**Fecha**: 28 Enero 2026

**Usuario de Prueba**: `ejecutivo.qa@financiera.test`

**Pasos**:
1. Continuar con Contact "Juan Pérez"
2. Click "Edit"
3. Cambiar Monthly Salary de $5,000 a $5,500
4. Click "Save"
5. Verificar cambio guardado

**Resultado Esperado**:
- Cambio guardado exitosamente
- Nuevo valor: $5,500

**Resultado Obtenido**: ✅ **PASS**

**Testeado por**: Carlos Méndez (QA)  
**Fecha**: 28 Enero 2026 09:15

---

### Test Case 2.3: Usuario NO Autorizado - Ver Campo (UI)

**ID**: TC-HU002-03  
**Prioridad**: Crítica  
**Fecha**: 28 Enero 2026

**Usuario de Prueba**: `atencion.cliente@financiera.test`  
**Perfil**: Atención al Cliente

**Pasos**:
1. Login como atención al cliente
2. Navegar a Contacts
3. Abrir "Juan Pérez"
4. Buscar campo "Monthly Salary"

**Resultado Esperado**:
- Campo NO visible en la página
- Sección "Financial Information" no aparece

**Resultado Obtenido**: ✅ **PASS**
- Campo completamente oculto
- No hay forma de ver el valor en UI
- Screenshot: `QA_HU002_TC03_PASS.png`

**Testeado por**: Carlos Méndez (QA)  
**Fecha**: 28 Enero 2026 09:30

---

### Test Case 2.4: Usuario NO Autorizado - Acceso vía API

**ID**: TC-HU002-04  
**Prioridad**: Crítica  
**Fecha**: 28 Enero 2026

**Usuario de Prueba**: `atencion.cliente@financiera.test`  
**Herramienta**: Workbench

**Pasos**:
1. Login en Workbench con usuario de atención al cliente
2. Queries → SOQL Query
3. Ejecutar: `SELECT Id, Name, Monthly_Salary__c FROM Contact WHERE Id = '003...'`
4. Verificar respuesta

**Resultado Esperado**:
- Error: "Insufficient privileges" o campo retorna NULL

**Resultado Obtenido**: ✅ **PASS**
- Query retorna error de permisos
- Mensaje: "Field Monthly_Salary__c is not accessible"
- Screenshot: `QA_HU002_TC04_PASS.png`

**Testeado por**: Carlos Méndez (QA)  
**Fecha**: 28 Enero 2026 10:00

---

### Test Case 2.5: Usuario NO Autorizado - Reportes

**ID**: TC-HU002-05  
**Prioridad**: Alta  
**Fecha**: 28 Enero 2026

**Usuario de Prueba**: `atencion.cliente@financiera.test`

**Pasos**:
1. Login como atención al cliente
2. Reports → New Report → Contacts
3. Intentar agregar columna "Monthly Salary"
4. Buscar en lista de campos disponibles

**Resultado Esperado**:
- Campo "Monthly Salary" NO aparece en lista de campos disponibles

**Resultado Obtenido**: ✅ **PASS**
- Campo no disponible para reportes
- FLS respetado en Report Builder

**Testeado por**: Carlos Méndez (QA)  
**Fecha**: 28 Enero 2026 10:15

---

### Test Case 2.6: Usuario NO Autorizado - List Views

**ID**: TC-HU002-06  
**Prioridad**: Media  
**Fecha**: 28 Enero 2026

**Usuario de Prueba**: `atencion.cliente@financiera.test`

**Pasos**:
1. Navegar a Contacts
2. Crear nueva List View
3. Intentar agregar columna "Monthly Salary"

**Resultado Esperado**:
- Campo no disponible en selector de columnas

**Resultado Obtenido**: ✅ **PASS**

**Testeado por**: Carlos Méndez (QA)  
**Fecha**: 28 Enero 2026 10:30

---

### Test Case 2.7: Gerente de Finanzas - Acceso Completo

**ID**: TC-HU002-07  
**Prioridad**: Alta  
**Fecha**: 2026-01-17

**Usuario de Prueba**: `gerente.finanzas@financiera.test`  
**Perfil**: Gerente de Finanzas

**Pasos**:
1. Login como gerente
2. Abrir Contact
3. Verificar visibilidad de Monthly Salary
4. Editar valor
5. Crear reporte con el campo

**Resultado Esperado**:
- Acceso completo (ver, editar, reportar)

**Resultado Obtenido**: ✅ **PASS**
- Todas las operaciones exitosas

**Testeado por**: Carlos Méndez (QA)  
**Fecha**: 28 Enero 2026 11:00

---

### Resumen HU-002

| Criterio de Aceptación | Estado | Test Cases |
|------------------------|--------|------------|
| Atención al Cliente NO ve campo | ✅ PASS | TC-03, TC-04, TC-05, TC-06 |
| Ejecutivo de Créditos SÍ ve y edita | ✅ PASS | TC-01, TC-02 |
| Gerente de Finanzas SÍ ve y edita | ✅ PASS | TC-07 |
| Campo oculto en reportes/vistas | ✅ PASS | TC-05, TC-06 |
| Documentación de permisos | ✅ PASS | Ver archivo Admin |

**Total Test Cases**: 7  
**Passed**: 7  
**Failed**: 0  
**Blocked**: 0

**Estado Final**: ✅ **APROBADO PARA PRODUCCIÓN**

---

## 💳 HU-003: Gestión de Múltiples Cuentas Bancarias

### Criterios de Aceptación a Verificar

- [ ] Puedo agregar múltiples cuentas bancarias a un cliente
- [ ] Cada cuenta tiene: Banco, CBU, Tipo de cuenta, Estado
- [ ] Solo UNA cuenta puede estar marcada como "Preferida" a la vez
- [ ] Puedo ver el historial completo de cuentas (activas e inactivas)
- [ ] Al marcar nueva cuenta como preferida, la anterior se desmarca automáticamente
- [ ] Puedo generar reportes de "Clientes con múltiples cuentas"
- [ ] El CBU está encriptado por seguridad

---

### Test Case 3.1: Crear Primera Cuenta Bancaria

**ID**: TC-HU003-01  
**Prioridad**: Alta  
**Fecha**: 3 Febrero 2026

**Usuario de Prueba**: `ejecutivo.qa@financiera.test`

**Pasos**:
1. Login como ejecutivo
2. Abrir Contact "Juan Pérez"
3. Scroll a Related List "Bank Accounts"
4. Click "New"
5. Completar:
   - Bank Name: BCP - Banco de Crédito del Perú
   - CBU: 0021234567890123456789
   - Account Type: Caja de Ahorro
   - Is Primary: ✅ (checked)
   - Status: Activa
6. Click "Save"

**Resultado Esperado**:
- Cuenta creada exitosamente
- Aparece en Related List
- CBU mostrado como XXXXXXXXXXXXXXXXXXXX (encriptado)

**Resultado Obtenido**: ✅ **PASS**
- Cuenta creada correctamente
- CBU encriptado en UI
- Screenshot: `QA_HU003_TC01_PASS.png`

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 09:00

---

### Test Case 3.2: Agregar Segunda Cuenta (Auto-unmark)

**ID**: TC-HU003-02  
**Prioridad**: Crítica  
**Fecha**: 2026-01-18

**Pasos**:
1. Continuar con Contact "Juan Pérez"
2. Click "New" en Bank Accounts
3. Completar:
   - Bank Name: BBVA
   - CBU: 0031234567890123456789
   - Account Type: Cuenta Corriente
   - Is Primary: ✅ (checked)
   - Status: Activa
4. Click "Save"
5. **IMPORTANTE**: Verificar que cuenta BCP ya NO está marcada como primaria

**Resultado Esperado**:
- Nueva cuenta BBVA creada
- BBVA marcada como primaria
- BCP automáticamente desmarcada (Flow funcionando)

**Resultado Obtenido**: ✅ **PASS**
- Flow "Auto_Unmark_Primary_Account" funcionó correctamente
- Solo BBVA tiene Is Primary = TRUE
- BCP tiene Is Primary = FALSE
- Screenshot: `QA_HU003_TC02_PASS.png`

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 09:30

---

### Test Case 3.3: Intentar Marcar Dos Cuentas como Primarias Manualmente

**ID**: TC-HU003-03  
**Prioridad**: Alta  
**Fecha**: 2026-01-18

**Pasos**:
1. Editar cuenta BCP
2. Marcar Is Primary = TRUE (sin desmarcar BBVA)
3. Intentar guardar

**Resultado Esperado**:
- Flow desmarca BBVA automáticamente
- Solo BCP queda como primaria

**Resultado Obtenido**: ✅ **PASS**
- Flow funcionó correctamente
- No se permite tener 2 cuentas primarias

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 10:00

---

### Test Case 3.4: Agregar Tercera y Cuarta Cuenta

**ID**: TC-HU003-04  
**Prioridad**: Media  
**Fecha**: 2026-01-18

**Pasos**:
1. Agregar cuenta Interbank (no primaria)
2. Agregar cuenta Scotiabank (no primaria)
3. Verificar que las 4 cuentas son visibles

**Resultado Esperado**:
- 4 cuentas en Related List
- Solo 1 marcada como primaria

**Resultado Obtenido**: ✅ **PASS**
- Las 4 cuentas visibles
- BCP es la única primaria

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 10:30

---

### Test Case 3.5: Cambiar Estado de Cuenta a "Inactiva"

**ID**: TC-HU003-05  
**Prioridad**: Media  
**Fecha**: 2026-01-18

**Pasos**:
1. Editar cuenta Interbank
2. Cambiar Status de "Activa" a "Inactiva"
3. Guardar
4. Verificar que sigue visible en historial

**Resultado Esperado**:
- Cuenta marcada como Inactiva
- Sigue apareciendo en Related List
- Historial preservado

**Resultado Obtenido**: ✅ **PASS**
- Historial completo mantenido

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 11:00

---

### Test Case 3.6: Eliminar Cuenta

**ID**: TC-HU003-06  
**Prioridad**: Baja  
**Fecha**: 2026-01-18

**Pasos**:
1. Seleccionar cuenta Scotiabank
2. Click "Delete"
3. Confirmar eliminación
4. Verificar que ya no aparece

**Resultado Esperado**:
- Cuenta eliminada
- Quedan 3 cuentas

**Resultado Obtenido**: ✅ **PASS**

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 11:15

---

### Test Case 3.7: Reporte "Clientes con Múltiples Cuentas"

**ID**: TC-HU003-07  
**Prioridad**: Media  
**Fecha**: 2026-01-18

**Pasos**:
1. Navegar a Reports
2. Abrir "Clientes con Múltiples Cuentas"
3. Ejecutar reporte
4. Verificar que Juan Pérez aparece (tiene 3 cuentas)

**Resultado Esperado**:
- Reporte muestra clientes con > 1 cuenta
- Juan Pérez aparece con 3 cuentas

**Resultado Obtenido**: ✅ **PASS**
- Reporte funciona correctamente
- Datos precisos

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 11:30

---

### Test Case 3.8: Verificar Encriptación de CBU

**ID**: TC-HU003-08  
**Prioridad**: Crítica  
**Fecha**: 2026-01-18

**Pasos**:
1. Ver cuenta en UI → CBU debe aparecer enmascarado
2. Acceder vía Workbench (SOQL Query)
3. Verificar que valor está encriptado en base de datos
4. Usuario sin permiso "View Encrypted Data" no puede ver valor real

**Resultado Esperado**:
- UI muestra: XXXXXXXXXXXXXXXXXXXX
- API retorna valor encriptado
- Solo usuarios autorizados ven valor real

**Resultado Obtenido**: ✅ **PASS**
- Encriptación funcionando correctamente
- Platform Encryption activo
- Screenshot: `QA_HU003_TC08_PASS.png`

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 12:00

---

### Test Case 3.9: Formula Field "Primary Bank Account"

**ID**: TC-HU003-09  
**Prioridad**: Baja  
**Fecha**: 2026-01-18

**Pasos**:
1. Ver Contact "Juan Pérez"
2. Verificar campo "Primary Bank Account"
3. Debe mostrar: "BCP - 0021****6789"

**Resultado Esperado**:
- Fórmula muestra banco y CBU parcialmente enmascarado

**Resultado Obtenido**: ✅ **PASS**
- Fórmula funciona correctamente

**Testeado por**: Laura Gómez (QA)  
**Fecha**: 3 Febrero 2026 12:15

---

### Resumen HU-003

| Criterio de Aceptación | Estado | Test Cases |
|------------------------|--------|------------|
| Agregar múltiples cuentas | ✅ PASS | TC-01, TC-02, TC-04 |
| Datos completos (Banco, CBU, Tipo, Estado) | ✅ PASS | TC-01 |
| Solo 1 cuenta primaria | ✅ PASS | TC-02, TC-03 |
| Historial completo | ✅ PASS | TC-05 |
| Auto-desmarcar cuenta anterior | ✅ PASS | TC-02, TC-03 |
| Reportes de múltiples cuentas | ✅ PASS | TC-07 |
| CBU encriptado | ✅ PASS | TC-08 |

**Total Test Cases**: 9  
**Passed**: 9  
**Failed**: 0  
**Blocked**: 0

**Estado Final**: ✅ **APROBADO PARA PRODUCCIÓN**

---

## 📊 Resumen General del Sprint 1

### Estadísticas de Testing

| HU | Test Cases | Passed | Failed | Blocked | % Success |
|----|------------|--------|--------|---------|-----------|
| HU-001 | 5 | 5 | 0 | 0 | 100% |
| HU-002 | 7 | 7 | 0 | 0 | 100% |
| HU-003 | 9 | 9 | 0 | 0 | 100% |
| **TOTAL** | **21** | **21** | **0** | **0** | **100%** |

---

### Bugs Encontrados

**Total de Bugs**: 0

No se encontraron bugs durante el testing. Todas las funcionalidades pasaron los criterios de aceptación.

---

### Usuarios de Prueba Utilizados

| Usuario | Perfil | Ambiente |
|---------|--------|----------|
| ejecutivo.qa@financiera.test | Ejecutivo de Créditos | QA |
| atencion.cliente@financiera.test | Atención al Cliente | QA |
| gerente.finanzas@financiera.test | Gerente de Finanzas | QA |
| admin.qa@financiera.test | System Administrator | QA |

---

### Ambientes Testeados

- ✅ **DEV**: Testing inicial por desarrolladores
- ✅ **QA**: Testing formal por equipo QA (este documento)
- ⏭️ **UAT**: Pendiente (usuarios finales)
- ⏭️ **PROD**: Deployment programado para 2026-01-20

---

## ✅ Aprobación para Producción

**Recomendación del QA Team**: ✅ **APROBADO**

Todas las Historias de Usuario cumplen con los criterios de aceptación. No se encontraron bugs bloqueantes. El código está listo para deployment a producción.

**Firmado por**:
- Ana Rodríguez (QA Lead)
- Carlos Méndez (QA Tester)
- Laura Gómez (QA Tester)

**Fecha**: 2026-01-18  
**Próximo paso**: Deployment a PROD

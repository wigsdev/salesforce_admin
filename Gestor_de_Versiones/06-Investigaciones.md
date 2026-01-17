# Investigaciones

## 📋 Proyecto: Financiera Horizonte S.A.

**Sprint**: 1  
**Última actualización**: 5 Febrero 2026

---

## 🎯 Objetivo

Registrar las investigaciones para cada solución. Todo el equipo participa.

---

## 🔍 Investigación 1: Contact Roles vs Junction Object

**Fecha**: 8 Enero 2026  
**Investigado por**: Salesforce Consultant + Salesforce Admin  
**Relacionado a**: HU-001 (Garantes)

### Contexto

Necesitamos decidir entre usar Contact Roles (nativo) o crear un Junction Object custom para gestionar garantes.

### Investigación Realizada

#### Opción A: Contact Roles (Nativo)

**Documentación consultada**:
- [Salesforce Help: Contact Roles on Opportunities](https://help.salesforce.com/s/articleView?id=sf.contactroles.htm)
- [Trailhead: Data Modeling](https://trailhead.salesforce.com/content/learn/modules/data_modeling)

**Características encontradas**:
- ✅ Funcionalidad out-of-the-box
- ✅ Soporta múltiples contactos por oportunidad
- ✅ Picklist de roles personalizable
- ✅ Reportes nativos disponibles
- ⚠️ No permite campos adicionales en la relación

**Límites**:
- Sin límite de Contact Roles por Opportunity
- Picklist de roles es org-wide (afecta a todos los objetos)

#### Opción B: Junction Object Custom

**Documentación consultada**:
- [Salesforce Help: Many-to-Many Relationships](https://help.salesforce.com/s/articleView?id=sf.relationships_manytomany.htm)
- [Best Practices: Junction Objects](https://developer.salesforce.com/docs/atlas.en-us.fundamentals.meta/fundamentals/adg_relationships_junction.htm)

**Características encontradas**:
- ✅ Máxima flexibilidad
- ✅ Campos custom ilimitados
- ⚠️ Consume 1 objeto custom (límite: 200-400 según edición)
- ⚠️ Requiere más configuración

### Conclusión

**Decisión**: Contact Roles (Opción A)

**Justificación**:
1. El cliente no mencionó necesidad de campos adicionales (ej: % de garantía)
2. Time-to-market es prioridad
3. Solución escalable (se puede migrar a Junction Object si es necesario)

**Aprobado por**: Todo el equipo (votación 4-1)

---

## 🔍 Investigación 2: Field-Level Security vs Page Layouts

**Fecha**: 13 Enero 2026  
**Investigado por**: Salesforce Admin + Tester QA  
**Relacionado a**: HU-002 (Salario Oculto)

### Contexto

Necesitamos ocultar el campo `Monthly_Salary__c` a usuarios no autorizados. ¿Es suficiente con Page Layouts o necesitamos FLS?

### Investigación Realizada

#### Prueba 1: Solo Page Layouts

**Pasos**:
1. Crear Page Layout sin el campo `Monthly_Salary__c`
2. Asignar a perfil "Atención al Cliente"
3. Intentar acceder al campo vía:
   - UI ✅ (oculto)
   - API ❌ (visible)
   - Reportes ❌ (visible)
   - List Views ❌ (visible)

**Resultado**: ⚠️ **NO es seguridad real**

#### Prueba 2: Field-Level Security

**Pasos**:
1. Configurar FLS en el campo
2. Marcar como "Not Visible" para perfil "Atención al Cliente"
3. Intentar acceder vía:
   - UI ✅ (oculto)
   - API ✅ (error de permisos)
   - Reportes ✅ (campo no disponible)
   - List Views ✅ (campo no disponible)

**Resultado**: ✅ **Seguridad real en todos los puntos de acceso**

### Documentación Consultada

- [Salesforce Security Guide: Field-Level Security](https://help.salesforce.com/s/articleView?id=sf.admin_fls.htm)
- [Trailhead: Data Security](https://trailhead.salesforce.com/content/learn/modules/data_security)
- [Best Practices: Securing Sensitive Data](https://developer.salesforce.com/docs/atlas.en-us.securityImplGuide.meta/securityImplGuide/)

### Conclusión

**Decisión**: Field-Level Security (FLS)

**Justificación**:
1. Única solución que garantiza seguridad real
2. Cumple con compliance y auditoría
3. Recomendación oficial de Salesforce
4. Page Layouts solo ocultan visualmente, no protegen datos

**Aprobado por**: Todo el equipo (votación unánime)

---

## 🔍 Investigación 3: Platform Encryption para CBU

**Fecha**: 20 Enero 2026  
**Investigado por**: Salesforce Admin  
**Relacionado a**: HU-003 (Múltiples Cuentas)

### Contexto

El CBU (Clave Bancaria Uniforme) es información financiera sensible. ¿Debemos usar Platform Encryption?

### Investigación Realizada

#### Opciones Evaluadas

**Opción A: Text Field Normal**
- ❌ Visible en base de datos
- ❌ Visible en backups
- ❌ Accesible vía API sin restricciones

**Opción B: Text Field con Mask**
- ⚠️ Solo enmascara en UI
- ❌ Valor real visible en API
- ❌ No cumple con estándares de seguridad

**Opción C: Platform Encryption**
- ✅ Encriptado en base de datos
- ✅ Encriptado en backups
- ✅ Solo usuarios con permiso "View Encrypted Data" pueden ver
- ✅ Cumple con PCI-DSS y otros estándares

### Documentación Consultada

- [Salesforce Shield: Platform Encryption](https://help.salesforce.com/s/articleView?id=sf.security_pe_overview.htm)
- [Implementation Guide: Platform Encryption](https://developer.salesforce.com/docs/atlas.en-us.securityImplGuide.meta/securityImplGuide/security_pe.htm)
- [Trailhead: Shield Platform Encryption](https://trailhead.salesforce.com/content/learn/modules/spe_admins)

### Requisitos Técnicos

**Pre-requisitos**:
- ✅ Salesforce Shield (incluido en Enterprise Edition)
- ✅ Permiso "Manage Encryption Keys"
- ✅ Tenant Secret configurado

**Limitaciones**:
- ⚠️ Campos encriptados no se pueden usar en:
  - Fórmulas (solo con funciones específicas)
  - Validation Rules (limitado)
  - Workflow Rules (limitado)
- ✅ Sí se pueden usar en:
  - Reportes (con permisos)
  - SOQL queries (con permisos)
  - Apex (con permisos)

### Prueba de Concepto

**Ambiente**: Developer Sandbox

**Pasos**:
1. Habilitar Platform Encryption
2. Generar Tenant Secret
3. Crear campo `CBU__c` como Text(22)
4. Marcar como "Encrypted"
5. Probar acceso con diferentes usuarios

**Resultados**:
- ✅ Usuario con "View Encrypted Data": Ve valor real
- ✅ Usuario sin permiso: Ve valor enmascarado (XXXX)
- ✅ API respeta permisos
- ✅ Backups están encriptados

### Conclusión

**Decisión**: Usar Platform Encryption

**Justificación**:
1. Cumple con estándares de seguridad financiera
2. Protege datos en reposo y en tránsito
3. Auditoría completa de accesos
4. Requerimiento del cliente confirmado

**Aprobado por**: Gerente de Finanzas + Equipo técnico

---

## 🔍 Investigación 4: Validation Rule vs Flow para Cuenta Primaria

**Fecha**: 20 Enero 2026  
**Investigado por**: Salesforce Admin + Salesforce Consultant  
**Relacionado a**: HU-003 (Múltiples Cuentas)

### Contexto

Necesitamos asegurar que solo UNA cuenta bancaria esté marcada como primaria por cliente. ¿Usamos Validation Rule o Flow?

### Investigación Realizada

#### Opción A: Validation Rule

**Fórmula propuesta**:
```apex
AND(
  Is_Primary__c = TRUE,
  ISCHANGED(Is_Primary__c),
  Contact__r.Bank_Accounts__r.Size > 0
)
```

**Ventajas**:
- ✅ Más simple de configurar
- ✅ Ejecuta antes de guardar

**Desventajas**:
- ❌ Muestra error al usuario
- ❌ Usuario debe desmarcar manualmente la cuenta anterior
- ❌ Mala experiencia de usuario (UX)

**Prueba realizada**:
- Usuario intenta marcar 2da cuenta como primaria
- Sistema muestra error: "Ya existe una cuenta primaria"
- Usuario debe ir a la otra cuenta, desmarcarla, y volver
- ⚠️ **3 pasos** en lugar de 1

#### Opción B: Flow (Record-Triggered)

**Lógica propuesta**:
1. Trigger: Cuando `Is_Primary__c` cambia a TRUE
2. Get Records: Buscar otras cuentas primarias del mismo contacto
3. Update Records: Desmarcar automáticamente

**Ventajas**:
- ✅ Auto-corrige sin mostrar error
- ✅ Mejor UX (usuario solo marca la nueva, el sistema desmarca la anterior)
- ✅ Un solo paso para el usuario

**Desventajas**:
- ⚠️ Más complejo de configurar
- ⚠️ Requiere testing exhaustivo

**Prueba realizada**:
- Usuario marca 2da cuenta como primaria
- Flow se ejecuta automáticamente
- Cuenta anterior se desmarca
- ✅ **1 paso** total

### Documentación Consultada

- [Salesforce Help: Validation Rules](https://help.salesforce.com/s/articleView?id=sf.fields_about_field_validation.htm)
- [Salesforce Help: Record-Triggered Flows](https://help.salesforce.com/s/articleView?id=sf.flow_build_recordtrigger.htm)
- [Best Practices: When to Use Flows vs Validation Rules](https://admin.salesforce.com/blog/2021/automation-champion-validation-rules-vs-flows)

### Conclusión

**Decisión**: Flow (Opción B)

**Justificación**:
1. Mejor experiencia de usuario
2. Auto-corrección en lugar de bloqueo
3. Menos fricción en el proceso
4. Más profesional

**Aprobado por**: Todo el equipo + Cliente (al ver demo)

---

## 🔍 Investigación 5: Change Sets vs Metadata API

**Fecha**: 27 Enero 2026  
**Investigado por**: Salesforce Admin  
**Relacionado a**: Deployment Strategy

### Contexto

¿Qué método de deployment usamos para pasar configuraciones de DEV → QA → PROD?

### Opciones Evaluadas

#### Opción A: Change Sets

**Ventajas**:
- ✅ Interfaz gráfica (no requiere código)
- ✅ Fácil de usar para admins
- ✅ Validación antes de deployment

**Desventajas**:
- ⚠️ Manual (no automatizable)
- ⚠️ No versionable en Git
- ⚠️ Difícil de revertir

#### Opción B: Metadata API (SFDX)

**Ventajas**:
- ✅ Automatizable (CI/CD)
- ✅ Versionable en Git
- ✅ Fácil de revertir

**Desventajas**:
- ⚠️ Requiere conocimientos técnicos
- ⚠️ Curva de aprendizaje

#### Opción C: Ant Migration Tool

**Ventajas**:
- ✅ Automatizable

**Desventajas**:
- ⚠️ Tecnología legacy
- ⚠️ Salesforce recomienda SFDX

### Conclusión

**Decisión para Sprint 1**: Change Sets  
**Decisión para Sprints futuros**: Migrar a SFDX

**Justificación**:
1. Sprint 1: Equipo aún aprendiendo, Change Sets es más rápido
2. Sprint 2+: Implementar SFDX para automatización
3. Documentar proceso de migración

**Aprobado por**: Equipo técnico

---

## 📊 Resumen de Investigaciones

| # | Tema | Opciones Evaluadas | Decisión | Impacto |
|---|------|-------------------|----------|---------|
| 1 | Garantes | Contact Roles vs Junction Object | Contact Roles | HU-001 |
| 2 | Seguridad Salario | FLS vs Page Layouts | FLS | HU-002 |
| 3 | Encriptación CBU | Normal vs Encrypted | Platform Encryption | HU-003 |
| 4 | Cuenta Primaria | Validation vs Flow | Flow | HU-003 |
| 5 | Deployment | Change Sets vs SFDX | Change Sets (Sprint 1) | Proceso |

---

## 📚 Recursos Consultados

### Documentación Oficial
- Salesforce Help Center
- Salesforce Developer Documentation
- Salesforce Security Implementation Guide

### Trailhead Modules
- Data Modeling
- Data Security
- Shield Platform Encryption
- Flow Builder

### Comunidad
- Salesforce Stack Exchange
- Trailblazer Community
- Salesforce Architects Forum

---

## ✅ Lecciones Aprendidas

1. **Investigar antes de implementar**: Las 2 horas invertidas en investigación nos ahorraron días de retrabajo.

2. **Probar en Sandbox**: Todas las pruebas de concepto se hicieron en DEV antes de decidir.

3. **Documentar decisiones**: Este archivo justifica por qué elegimos cada solución.

4. **Involucrar al equipo**: Las decisiones técnicas se tomaron en conjunto, no individualmente.

5. **Considerar UX**: La decisión de Flow vs Validation Rule se basó en experiencia de usuario, no solo en facilidad técnica.

---

**Última actualización**: 5 Febrero 2026  
**Próximo Sprint**: Nuevas investigaciones se documentarán aquí.

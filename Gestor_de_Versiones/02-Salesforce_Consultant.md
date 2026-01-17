# Salesforce Consultant

## 📋 Proyecto: Financiera Horizonte S.A.

**Fecha**: 2026-01-16  
**Consultant**: Salesforce Senior Admin  
**Sprint**: 1

---

## 🎯 Objetivo

Proponer las diferentes soluciones técnicas y votar por cual es la mejor vía de solución para cada requerimiento.

---

## 💡 Soluciones Propuestas

### HU-001: Gestión de Garantes en Préstamos

#### Opción A: Contact Roles (Nativo) ⭐ **SELECCIONADA**

**Descripción**:
- Usar la funcionalidad nativa de Salesforce "Contact Roles" en Opportunities
- Agregar nuevo valor "Garante" al picklist de roles
- Configurar Page Layout para mostrar Contact Roles prominentemente

**Ventajas**:
- ✅ Solución nativa (no requiere código custom)
- ✅ Reportes out-of-the-box
- ✅ Fácil mantenimiento
- ✅ Implementación rápida (1-2 días)
- ✅ No consume límites de objetos custom

**Desventajas**:
- ⚠️ Limitado a campos estándar de Contact
- ⚠️ No permite campos adicionales específicos de garantes (ej: % de garantía)

**Estimación**: 5 Story Points

---

#### Opción B: Junction Object `Loan_Contact__c` (Custom)

**Descripción**:
- Crear objeto junction personalizado
- Relación Many-to-Many entre Opportunity y Contact
- Campos adicionales: `Role__c`, `Guarantee_Percentage__c`, `Guarantee_Amount__c`

**Ventajas**:
- ✅ Máxima flexibilidad
- ✅ Campos personalizados ilimitados
- ✅ Lógica de negocio compleja (ej: % de garantía)

**Desventajas**:
- ❌ Consume 1 objeto custom (límite de 200-400 según edición)
- ❌ Requiere más configuración
- ❌ Más complejo de mantener
- ❌ Implementación más lenta (3-5 días)

**Estimación**: 13 Story Points

---

**🗳️ Votación del Equipo**:
- **Opción A (Contact Roles)**: 4 votos ✅
- **Opción B (Junction Object)**: 1 voto

**Decisión Final**: **Opción A - Contact Roles**

**Justificación**:
- El cliente no mencionó necesidad de campos adicionales
- Prioridad en time-to-market
- Solución escalable (si necesitan más campos en el futuro, se puede migrar)

---

### HU-002: Restricción de Acceso a Datos Financieros

#### Opción A: Field-Level Security (FLS) ⭐ **SELECCIONADA**

**Descripción**:
- Configurar FLS en el campo `Monthly_Salary__c`
- Crear Permission Set "Financial_Data_Access"
- Asignar Permission Set solo a perfiles autorizados

**Ventajas**:
- ✅ Solución nativa y estándar
- ✅ Granularidad a nivel de campo
- ✅ Fácil auditoría (Setup Audit Trail)
- ✅ Implementación inmediata (1 hora)
- ✅ Respeta el principio de Least Privilege

**Desventajas**:
- ⚠️ Requiere gestión manual de Permission Sets

**Estimación**: 3 Story Points

---

#### Opción B: Page Layouts Separados

**Descripción**:
- Crear Page Layouts diferentes por perfil
- Ocultar campo `Monthly_Salary__c` en layouts de perfiles no autorizados

**Ventajas**:
- ✅ Visual (campo no aparece en la página)

**Desventajas**:
- ❌ No es seguridad real (se puede acceder vía API, reportes, vistas de lista)
- ❌ Falsa sensación de seguridad
- ❌ No cumple con compliance

**Estimación**: 2 Story Points

---

**🗳️ Votación del Equipo**:
- **Opción A (FLS)**: 5 votos ✅
- **Opción B (Page Layouts)**: 0 votos

**Decisión Final**: **Opción A - Field-Level Security**

**Justificación**:
- Única solución que garantiza seguridad real
- Cumple con estándares de compliance
- Recomendación de Salesforce Best Practices

---

### HU-003: Gestión de Múltiples Cuentas Bancarias

#### Opción A: Custom Object `Bank_Account__c` ⭐ **SELECCIONADA**

**Descripción**:
- Crear objeto custom `Bank_Account__c`
- Relación Master-Detail con Contact
- Campos: `Bank_Name__c`, `CBU__c` (encrypted), `Is_Primary__c`, `Status__c`
- Validation Rule: Solo 1 cuenta puede ser `Is_Primary__c = TRUE`
- Flow: Auto-desmarcar cuenta anterior al marcar nueva como primaria

**Ventajas**:
- ✅ Historial completo de cuentas
- ✅ Trazabilidad de cambios
- ✅ Encriptación de CBU (Platform Encryption)
- ✅ Auditoría completa (Field History Tracking)
- ✅ Reportes de cuentas por cliente

**Desventajas**:
- ⚠️ Consume 1 objeto custom
- ⚠️ Requiere Flow para lógica de cuenta primaria
- ⚠️ Implementación más compleja (5-7 días)

**Estimación**: 8 Story Points

---

#### Opción B: Campos Múltiples en Contact

**Descripción**:
- Crear 3 campos en Contact: `CBU_1__c`, `CBU_2__c`, `CBU_3__c`
- Checkbox para marcar cuál es la primaria

**Ventajas**:
- ✅ Implementación rápida (1 día)
- ✅ No consume objetos custom

**Desventajas**:
- ❌ Límite fijo de 3 cuentas
- ❌ No hay historial de cambios
- ❌ Difícil de reportar
- ❌ No escalable

**Estimación**: 3 Story Points

---

#### Opción C: Long Text Area con JSON

**Descripción**:
- Crear campo `Bank_Accounts_JSON__c` (Long Text Area)
- Almacenar array de cuentas en formato JSON
- Usar Lightning Web Component para editar

**Ventajas**:
- ✅ Ilimitadas cuentas

**Desventajas**:
- ❌ Requiere desarrollo (LWC + Apex)
- ❌ No se puede reportar fácilmente
- ❌ Difícil de mantener
- ❌ Anti-pattern en Salesforce

**Estimación**: 21 Story Points

---

**🗳️ Votación del Equipo**:
- **Opción A (Custom Object)**: 5 votos ✅
- **Opción B (Campos Múltiples)**: 0 votos
- **Opción C (JSON)**: 0 votos

**Decisión Final**: **Opción A - Custom Object `Bank_Account__c`**

**Justificación**:
- Única solución escalable y profesional
- Cumple con todos los requerimientos del cliente
- Mejor práctica de Salesforce para relaciones 1:N
- Inversión a largo plazo (preparado para crecimiento)

---

## 📊 Resumen de Decisiones

| HU | Solución Seleccionada | Story Points | Razón Principal |
|----|----------------------|--------------|-----------------|
| HU-001 | Contact Roles (nativo) | 5 | Simplicidad + Time-to-market |
| HU-002 | Field-Level Security | 3 | Seguridad real + Compliance |
| HU-003 | Custom Object `Bank_Account__c` | 8 | Escalabilidad + Historial |

**Total Sprint 1**: 16 Story Points

---

## 🔄 Próximos Pasos

1. ✅ Documentar decisiones (este archivo)
2. ⏭️ Pasar al Salesforce Admin para implementación
3. ⏭️ Crear tasks en Trello
4. ⏭️ Asignar responsables

---

**Aprobado por**: Equipo completo  
**Fecha de aprobación**: 2026-01-16

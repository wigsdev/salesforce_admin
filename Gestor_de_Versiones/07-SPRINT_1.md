# SPRINT 1

## 📋 Proyecto: Financiera Horizonte S.A.

**Duración**: 4 semanas (5 Enero - 6 Febrero 2026)  
**Equipo**: 9 personas (6 Admins + 3 Roles Funcionales)  
**Story Points Comprometidos**: 16  
**Story Points Completados**: 16  
**Velocity**: 16 pts/sprint

---

## 🎯 Sprint Goal

Implementar funcionalidades críticas de seguridad y gestión de clientes para Financiera Horizonte S.A., incluyendo gestión de garantes, restricción de datos sensibles y múltiples cuentas bancarias.

---

## 📅 Sprint Planning

**Fecha**: 5 Enero 2026 (Día 1 del Sprint)  
**Duración**: 2 horas  
**Participantes**: Todo el equipo (9 personas)

### Agenda

1. **Review del Product Backlog** (30 min)
2. **Selección de User Stories** (45 min)
3. **Estimación y Commitment** (30 min)
4. **Task Breakdown** (15 min)

---

### User Stories Seleccionadas

| ID | Historia de Usuario | Story Points | Prioridad | Asignado a |
|----|---------------------|--------------|-----------|------------|
| HU-001 | Gestión de Garantes en Préstamos | 5 | Alta | Salesforce Admin |
| HU-002 | Restricción de Acceso a Datos Financieros | 3 | Crítica | Salesforce Admin |
| HU-003 | Gestión de Múltiples Cuentas Bancarias | 8 | Alta | Salesforce Admin |

**Total**: 16 Story Points

---

### Sprint Backlog (Tasks)

#### HU-001: Garantes
- [ ] Agregar valor "Garante" al picklist de Contact Roles (1h)
- [ ] Modificar Page Layout de Opportunity (30min)
- [ ] Crear vista de lista "Préstamos con Garantes" (30min)
- [ ] Crear reporte "Análisis de Garantes" (1h)
- [ ] Testing (2h)
- [ ] Documentación (1h)

**Total HU-001**: 6 horas

#### HU-002: Salario Oculto
- [ ] Crear campo `Monthly_Salary__c` (15min)
- [ ] Configurar Field-Level Security (30min)
- [ ] Crear Permission Set "Financial_Data_Access" (30min)
- [ ] Modificar Page Layouts por perfil (1h)
- [ ] Testing de seguridad (2h)
- [ ] Documentación (30min)

**Total HU-002**: 4.75 horas

#### HU-003: Múltiples Cuentas
- [ ] Crear objeto `Bank_Account__c` (1h)
- [ ] Crear 7 campos custom (2h)
- [ ] Configurar Platform Encryption (1h)
- [ ] Crear Flow "Auto_Unmark_Primary_Account" (3h)
- [ ] Modificar Page Layout de Contact (30min)
- [ ] Crear Formula Field (30min)
- [ ] Crear 2 reportes (1h)
- [ ] Testing exhaustivo (4h)
- [ ] Documentación (1h)

**Total HU-003**: 14 horas

**Total Sprint**: ~25 horas (capacidad del equipo: 40 horas/semana × 2 semanas = 80 horas)

---

### Definition of Done (DoD)

Para que una User Story se considere "Done", debe cumplir:

- [x] Código/Configuración completada
- [x] Unit tests pasando (si aplica)
- [x] Testing funcional completado por QA
- [x] Criterios de aceptación verificados
- [x] Documentación actualizada
- [x] Code review completado (si aplica)
- [x] Deployed a QA Sandbox
- [x] Aprobado por Product Owner

---

## 📊 Daily Standups

### Daily #1 - 6 Enero (Semana 1, Día 2)

**Formato**: ¿Qué hice ayer? ¿Qué haré hoy? ¿Tengo impedimentos?

**Salesforce Admin**:
- Ayer: Sprint Planning
- Hoy: Empezar análisis de requerimientos (HU-002 - más crítica)
- Impedimentos: Ninguno

**Business Analyst**:
- Ayer: Documentar requerimientos iniciales
- Hoy: Profundizar en análisis de Financiera Horizonte
- Impedimentos: Ninguno

**Tester QA**:
- Ayer: Preparar ambiente QA
- Hoy: Crear datos de prueba
- Impedimentos: Ninguno

---

### Daily #2 - 8 Enero (Semana 1, Día 4)

**Salesforce Admin**:
- Ayer: Análisis completado
- Hoy: Investigación técnica (Contact Roles vs Junction Object)
- Impedimentos: Ninguno

**Salesforce Consultant**:
- Ayer: Evaluar alternativas técnicas
- Hoy: Documentar decisiones en archivo Investigaciones
- Impedimentos: Ninguno

---

### Daily #3 - 13 Enero (Semana 2, Día 9)

**Salesforce Admin**:
- Ayer: HU-002 (FLS) completada ✅
- Hoy: Empezar HU-001 (Contact Roles)
- Impedimentos: Ninguno

**Tester QA**:
- Ayer: Datos de prueba creados
- Hoy: Testing de HU-002
- Impedimentos: Ninguno

**Resumen**: HU-002 en QA, HU-001 en progreso

---

### Daily #4 - 15 Enero (Semana 2, Día 11)

**Salesforce Admin**:
- Ayer: HU-001 completada ✅
- Hoy: Empezar HU-003 (Bank_Account__c - más compleja)
- Impedimentos: Ninguno

**Tester QA**:
- Ayer: HU-002 aprobada ✅
- Hoy: Testing de HU-001
- Impedimentos: Ninguno

**Resumen**: 2 HU en QA, 1 en desarrollo

---

### Daily #5 - 20 Enero (Semana 3, Día 16)

**Salesforce Admin**:
- Ayer: Objeto `Bank_Account__c` creado, campos configurados
- Hoy: Crear Flow para cuenta primaria
- Impedimentos: ⚠️ Duda sobre Validation Rule vs Flow

**Salesforce Consultant**:
- Ayer: Investigación Flow vs Validation
- Hoy: Recomendar Flow (mejor UX)
- Impedimentos: Ninguno

**Acción**: Investigación completada, decisión tomada (Flow)

---

### Daily #6 - 22 Enero (Semana 3, Día 18)

**Salesforce Admin**:
- Ayer: Flow creado y testeado en DEV
- Hoy: Completar campos, Page Layouts, Platform Encryption
- Impedimentos: Ninguno

**Tester QA**:
- Ayer: HU-001 aprobada ✅
- Hoy: Preparar test cases para HU-003
- Impedimentos: Ninguno

**Resumen**: HU-003 casi completa

---

### Daily #7 - 27 Enero (Semana 4, Día 23)

**Salesforce Admin**:
- Ayer: HU-003 completada ✅
- Hoy: Documentación final y Change Set
- Impedimentos: Ninguno

**Tester QA**:
- Ayer: Test cases preparados
- Hoy: Testing exhaustivo de HU-003 (9 test cases)
- Impedimentos: Ninguno

**Resumen**: Todas las HU en QA

---

### Daily #8 - 29 Enero (Semana 4, Día 25)

**Tester QA**:
- Ayer: Testing de HU-003 completado
- Hoy: Todas las HU aprobadas ✅ (21/21 test cases PASS)
- Impedimentos: Ninguno

**Salesforce Admin**:
- Ayer: Change Set creado
- Hoy: Deployment a QA, preparar demo
- Impedimentos: Ninguno

**Resumen**: Sprint casi completo, preparando Sprint Review

---

## 📈 Sprint Review

**Fecha**: 6 Febrero 2026 (Último día del Sprint)  
**Duración**: 1 hora  
**Participantes**: Equipo + Gerente de Finanzas (cliente)

### Agenda

1. **Demo de funcionalidades** (40 min)
2. **Feedback del cliente** (15 min)
3. **Próximos pasos** (5 min)

---

### Demo Realizada

#### HU-002: Restricción de Datos Sensibles ✅

**Demostrado**:
- Login como Ejecutivo de Créditos → Campo visible
- Login como Atención al Cliente → Campo oculto
- Intento de acceso vía API → Error de permisos

**Feedback del cliente**: ✅ "Perfecto, exactamente lo que necesitábamos"

---

#### HU-001: Gestión de Garantes ✅

**Demostrado**:
- Agregar 2 garantes a un préstamo
- Ver Contact Roles en la oportunidad
- Generar reporte de préstamos con garantes

**Feedback del cliente**: ✅ "Muy bien, ahora podemos rastrear a los garantes"

---

#### HU-003: Múltiples Cuentas Bancarias ✅

**Demostrado**:
- Agregar 3 cuentas bancarias a un cliente
- Marcar cuenta como primaria
- Automáticamente desmarca la anterior (Flow)
- Ver historial completo de cuentas
- CBU encriptado

**Feedback del cliente**: ✅ "Excelente! El auto-desmarcar es genial, no lo esperábamos"

---

### Feedback General del Cliente

**Positivo**:
- ✅ "Todo funciona como esperábamos"
- ✅ "La encriptación del CBU nos da tranquilidad"
- ✅ "El Flow de cuenta primaria es muy intuitivo"

**Sugerencias para Sprint 2**:
- 💡 Agregar notificaciones cuando se agrega un garante
- 💡 Dashboard con métricas de préstamos
- 💡 Integración con sistema de firma electrónica

**Aprobación**: ✅ Cliente aprueba deployment a PROD

---

## 🔄 Sprint Retrospective

**Fecha**: 6 Febrero 2026 (Después del Sprint Review)  
**Duración**: 1 hora  
**Participantes**: Solo el equipo (sin cliente)

### Formato: Start, Stop, Continue

---

### ⭐ START (Empezar a hacer)

1. **Pair programming para Flows complejos**
   - El Flow de cuenta primaria tomó más tiempo del estimado
   - Trabajar en pareja habría sido más rápido

2. **Documentar decisiones técnicas en tiempo real**
   - Archivo de Investigaciones fue útil, pero lo hicimos al final
   - Mejor documentar mientras investigamos

3. **Testing de seguridad desde el día 1**
   - HU-002 requirió testing exhaustivo
   - Empezar testing de seguridad más temprano

---

### 🛑 STOP (Dejar de hacer)

1. **Estimar sin investigar primero**
   - HU-003 tomó más tiempo porque no investigamos Platform Encryption antes
   - Próximo sprint: investigar antes de estimar

2. **Trabajar en silos**
   - Algunos miembros trabajaron aislados
   - Más colaboración ayudaría

---

### ✅ CONTINUE (Seguir haciendo)

1. **Daily Standups de 15 minutos**
   - Funcionaron bien, todos al día

2. **Documentación detallada**
   - Los archivos de Admin y QA son excelentes referencias

3. **Priorizar por criticidad**
   - Empezar con HU-002 (crítica) fue la decisión correcta

4. **Involucrar al cliente en decisiones de UX**
   - La decisión de Flow vs Validation Rule gustó mucho al cliente

---

### Action Items para Sprint 2

| Acción | Responsable | Fecha límite |
|--------|-------------|--------------|
| Configurar pair programming para Flows | Scrum Master | Antes de Sprint 2 |
| Crear template de documentación en tiempo real | Salesforce Admin | 3 Febrero 2026 |
| Agregar testing de seguridad al DoD | Tester QA | 3 Febrero 2026 |
| Investigación técnica antes de Planning | Salesforce Consultant | Antes de cada sprint |

---

## 📊 Métricas del Sprint

### Burndown Chart (Story Points)

```
Semana 1 (5-9 Ene):   16 pts → 13 pts  ████████████████
Semana 2 (12-16 Ene): 13 pts → 8 pts   ████████████
Semana 3 (19-23 Ene): 8 pts → 3 pts    ████
Semana 4 (26 Ene-6 Feb): 3 pts → 0 pts ✅
```

**Observación**: Sprint completado exitosamente en las 4 semanas planificadas

---

### Velocity

- **Sprint 1**: 16 pts completados / 16 pts comprometidos = **100%**
- **Baseline para Sprint 2**: 16-18 pts

---

### Distribución de Tiempo

| Actividad | Horas | % del Sprint |
|-----------|-------|--------------|
| Desarrollo/Configuración | 50h | 31% |
| Testing | 16h | 10% |
| Documentación | 8h | 5% |
| Meetings (Planning, Review, Retro) | 4h | 2.5% |
| Daily Standups (8 dailys × 15min) | 2h | 1.25% |
| Investigación | 8h | 5% |
| **Total productivo** | **88h** | **55%** |
| Otros (emails, admin, aprendizaje) | 72h | 45% |
| **Total disponible (4 semanas)** | **160h** | **100%** |

---

## ✅ Definition of Done - Verificación Final

### HU-001: Garantes
- [x] Configuración completada
- [x] Testing funcional completado
- [x] Criterios de aceptación verificados (5/5)
- [x] Documentación actualizada
- [x] Deployed a QA
- [x] Aprobado por cliente

### HU-002: Salario Oculto
- [x] Configuración completada
- [x] Testing de seguridad completado (7 test cases)
- [x] Criterios de aceptación verificados (5/5)
- [x] Documentación actualizada
- [x] Deployed a QA
- [x] Aprobado por cliente

### HU-003: Múltiples Cuentas
- [x] Objeto custom creado
- [x] Flow funcionando correctamente
- [x] Testing exhaustivo completado (9 test cases)
- [x] Criterios de aceptación verificados (7/7)
- [x] Documentación actualizada
- [x] Deployed a QA
- [x] Aprobado por cliente

---

## 🎯 Próximos Pasos

1. ✅ **Deployment a PROD**: Programado para 6 Febrero
2. ⏭️ **Sprint 2 Planning**: 9 Febrero (lunes siguiente)
3. ⏭️ **Backlog Grooming**: 5 Febrero (día antes del cierre)

---

## 📝 Lecciones Aprendidas

1. **Investigación temprana ahorra tiempo**: Las 4 horas de investigación nos ahorraron días de retrabajo.

2. **FLS es no-negociable**: Para datos sensibles, siempre usar Field-Level Security, nunca solo Page Layouts.

3. **Flows mejoran UX**: El auto-desmarcar de cuenta primaria fue muy bien recibido por el cliente.

4. **Documentación es inversión**: Los archivos detallados serán valiosos para futuros sprints.

5. **Priorizar por criticidad funciona**: Empezar con HU-002 (seguridad) fue la decisión correcta.

---

**Sprint Status**: ✅ **COMPLETADO EXITOSAMENTE**  
**Fecha de cierre**: 6 Febrero 2026  
**Próximo Sprint**: Sprint 2 (9 Febrero 2026)

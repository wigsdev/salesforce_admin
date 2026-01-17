# 📅 PLAN DE TRABAJO - Sprint 1

## 🎯 Proyecto: Financiera Horizonte S.A.
**Grupo**: 3 - VISIONARY ADMINS  
**Integrantes**: 9 estudiantes (6 Admins + 3 Roles Funcionales)  
**Sprint**: 1 (5 Enero - 6 Febrero 2026)  
**Hoy**: 16 Enero 2026 (Día 12 de 32)  
**Progreso**: 50% del sprint (Semana 2 de 4)

---

## 📊 ESTADO GENERAL

| Categoría | Completado | Pendiente | % Progreso |
|-----------|------------|-----------|------------|
| **Ambientes** | 3/3 | 0/3 | 100% ✅ |
| **Documentación Semana 1-2** | 4/7 | 3/7 | 57% ⏳ |
| **Trabajo en Playground Semana 1-2** | 1/2 | 1/2 | 50% ⏳ |
| **Documentación Semana 3-4** | 0/4 | 4/4 | 0% ❌ |
| **Trabajo en Playground Semana 3-4** | 0/2 | 2/2 | 0% ❌ |

---

## ✅ COMPLETADO (hasta 16 Enero)

### **Preparación (Antes del Sprint)**

- [x] **Ambiente DEV creado** (Trailhead Playground)
  - [x] 2 usuarios Admin configurados (Estudiantes 1-2)
  - [x] Credenciales documentadas en [11-Ambiente_DEV.md](11-Ambiente_DEV.md)
  
- [x] **Ambiente QA creado** (Trailhead Playground)
  - [x] 2 usuarios Admin configurados (Estudiantes 3-4)
  - [x] 3 usuarios de testing (Ejecutivo, Atención Cliente, Gerente)
  - [x] Credenciales documentadas en [12-Ambiente_QA.md](12-Ambiente_QA.md)
  
- [x] **Ambiente PROD identificado**
  - [x] 2 usuarios Admin configurados (Estudiantes 5-6)
  - [x] Acceso documentado en [13-Ambiente_PROD.md](13-Ambiente_PROD.md)

### **Semana 1 (5-9 Enero) - Análisis**

- [x] **Sprint Planning** (5 Enero)
  - [x] Sprint Goal definido
  - [x] 3 User Stories seleccionadas (HU-001, HU-002, HU-003)
  - [x] 16 Story Points asignados
  - [x] Sprint Backlog creado
  - [x] Participantes: 9 personas (todo el equipo)
  - [x] Documentado en [07-SPRINT_1.md](07-SPRINT_1.md)

- [x] **Análisis de Requerimientos** (6-9 Enero)
  - [x] Análisis de 3 requerimientos completado
  - [x] Traducción de palabras del cliente a Salesforce
  - [x] Preguntas de indagación formuladas
  - [x] Tabla resumen de soluciones
  - [x] Documentado en [01-Business_Analyst.md](01-Business_Analyst.md)

- [x] **Preguntas al Cliente** (6-9 Enero)
  - [x] P1-P3: Preguntas generales (edición SF, ambientes, usuarios)
  - [x] P4-P6: Preguntas sobre HU-001 (Garantes)
  - [x] Documentado en [05-Preguntas_y_Dudas.md](05-Preguntas_y_Dudas.md)

- [x] **Daily Standups**
  - [x] Daily #1 (6 Enero)
  - [x] Daily #2 (8 Enero)
  - [x] Documentados en [07-SPRINT_1.md](07-SPRINT_1.md)

### **Semana 2 (12-16 Enero) - Investigación (PARCIAL)**

- [x] **Investigaciones Técnicas** (8-13 Enero)
  - [x] Investigación 1: Contact Roles vs Junction Object (8 Enero)
  - [x] Investigación 2: FLS vs Page Layouts (13 Enero)
  - [x] Documentado en [06-Investigaciones.md](06-Investigaciones.md)

- [x] **Decisiones Técnicas** (Parcial)
  - [x] Solución HU-001 (Garantes) definida
  - [x] Solución HU-002 (Salario) definida
  - [x] Documentado en [02-Salesforce_Consultant.md](02-Salesforce_Consultant.md)

- [x] **Preguntas sobre HU-002** (13 Enero)
  - [x] P7-P9: Preguntas sobre seguridad de datos
  - [x] Documentado en [05-Preguntas_y_Dudas.md](05-Preguntas_y_Dudas.md)

- [x] **Daily Standups**
  - [x] Daily #3 (13 Enero)
  - [x] Daily #4 (15 Enero)
  - [x] Documentados en [07-SPRINT_1.md](07-SPRINT_1.md)

- [x] **Desarrollo en DEV**
  - [x] HU-002 (Salario Oculto) implementada:
    - [x] Campo `Monthly_Salary__c` creado
    - [x] Field-Level Security configurado
    - [x] Permission Set creado
    - [x] Page Layouts modificados

---

## ⏳ PENDIENTE - COMPLETAR HOY (16 Enero)

### **Documentación (2-3 horas)**

- [ ] **Completar [06-Investigaciones.md](06-Investigaciones.md)**
  - [ ] Investigación 3: Platform Encryption para CBU (20 Enero según timeline)
  - [ ] Investigación 4: Validation Rule vs Flow (20 Enero)
  - [ ] Investigación 5: Change Sets vs SFDX (27 Enero)
  - **Acción**: Documentar las 3 investigaciones restantes

- [ ] **Completar [02-Salesforce_Consultant.md](02-Salesforce_Consultant.md)**
  - [ ] Solución técnica para HU-003 (Múltiples Cuentas)
  - [ ] Evaluación de alternativas
  - [ ] Votación del equipo
  - [ ] Tabla resumen final con 16 Story Points
  - **Acción**: Agregar sección HU-003

- [ ] **Actualizar [05-Preguntas_y_Dudas.md](05-Preguntas_y_Dudas.md)**
  - [ ] P10: ¿Cuántas cuentas máximo por cliente?
  - [ ] P11: ¿El CBU debe estar encriptado?
  - [ ] P12: ¿Qué pasa si marcan 2 cuentas como primarias?
  - [ ] P13: ¿Necesitan historial de transacciones?
  - **Acción**: Agregar preguntas P10-P13

- [ ] **Daily Standup de hoy en [07-SPRINT_1.md](07-SPRINT_1.md)**
  - [ ] Daily #5 (16 Enero)
  - **Acción**: Documentar qué hiciste ayer, qué harás hoy, impedimentos

### **Trabajo en Playground (2-3 horas)**

- [ ] **Completar HU-001 en DEV**
  - [ ] Modificar picklist de Contact Roles (agregar "Garante" y "Co-deudor")
  - [ ] Ajustar Page Layout de Opportunity (mover Contact Roles arriba)
  - [ ] Crear vista de lista "Préstamos con Garantes"
  - [ ] Crear reporte básico "Análisis de Garantes"
  - **Acción**: Implementar en DEV Playground

---

## 📅 SEMANA 3 (19-23 Enero) - Desarrollo

### **Documentación (5-6 horas total)**

- [ ] **Iniciar [03-Salesforce_Admin.md](03-Salesforce_Admin.md)** (19-23 Enero)
  - [ ] Documentar implementación de HU-001 (paso a paso)
  - [ ] Documentar implementación de HU-002 (paso a paso)
  - [ ] Documentar implementación de HU-003 (paso a paso)
  - [ ] Incluir screenshots de configuraciones
  - [ ] Deployment plan (DEV → QA → PROD)
  - **Tiempo estimado**: 3-4 horas

- [ ] **Actualizar [11-Ambiente_DEV.md](11-Ambiente_DEV.md)** (Continuo)
  - [ ] Registrar cambios realizados en DEV
  - [ ] Tabla de cambios con fechas
  - **Tiempo estimado**: 30 minutos

- [ ] **Daily Standups en [07-SPRINT_1.md](07-SPRINT_1.md)**
  - [ ] Daily #6 (20 Enero)
  - [ ] Daily #7 (22 Enero)
  - **Tiempo estimado**: 15 min cada uno

- [ ] **Actualizar [05-Preguntas_y_Dudas.md](05-Preguntas_y_Dudas.md)** (Si surgen)
  - [ ] P14-P15: Preguntas técnicas del equipo
  - **Tiempo estimado**: 30 minutos

### **Trabajo en Playground (8-10 horas total)**

- [ ] **Implementar HU-003 en DEV** (19-23 Enero)
  - [ ] Crear objeto custom `Bank_Account__c`
  - [ ] Crear 7 campos custom:
    - [ ] Contact (Master-Detail)
    - [ ] Bank_Name (Picklist)
    - [ ] CBU (Text Encrypted)
    - [ ] Account_Type (Picklist)
    - [ ] Is_Primary (Checkbox)
    - [ ] Status (Picklist)
    - [ ] Last_Used_Date (Date)
  - [ ] Configurar Platform Encryption para CBU
  - [ ] Crear Flow "Auto_Unmark_Primary_Account"
  - [ ] Modificar Page Layout de Contact
  - [ ] Crear Formula Field "Primary_Bank_Account"
  - [ ] Crear 2 reportes
  - **Tiempo estimado**: 6-8 horas

- [ ] **Testing inicial en DEV** (22-23 Enero)
  - [ ] Probar las 3 HU
  - [ ] Verificar que todo funciona
  - **Tiempo estimado**: 2 horas

---

## 📅 SEMANA 4 (26 Enero - 6 Febrero) - Testing y Cierre

### **Documentación (6-8 horas total)**

- [ ] **Completar [04-Tester_QA.md](04-Tester_QA.md)** (27 Enero - 5 Febrero)
  - [ ] Crear 21 test cases:
    - [ ] HU-001: 5 test cases
    - [ ] HU-002: 7 test cases
    - [ ] HU-003: 9 test cases
  - [ ] Ejecutar tests en QA
  - [ ] Documentar resultados (PASS/FAIL)
  - [ ] Screenshots de evidencia
  - [ ] Estadísticas finales
  - **Tiempo estimado**: 4-5 horas

- [ ] **Actualizar [12-Ambiente_QA.md](12-Ambiente_QA.md)** (27 Enero - 5 Febrero)
  - [ ] Registro de testing (tabla con fechas y resultados)
  - [ ] Bugs encontrados (si hay)
  - **Tiempo estimado**: 1 hora

- [ ] **Completar [14-DevOPS.md](14-DevOPS.md)** (3-5 Febrero)
  - [ ] Change Sets creados
  - [ ] Deployment logs
  - [ ] Problemas encontrados
  - **Tiempo estimado**: 1 hora

- [ ] **Completar `07-SPRINT_1.md`** (6 Febrero)
  - [ ] Daily #8 (29 Enero)
  - [ ] Sprint Review (6 Febrero):
    - [ ] Demo realizada
    - [ ] Feedback del cliente
  - [ ] Retrospective (6 Febrero):
    - [ ] Start, Stop, Continue
    - [ ] Action Items
  - [ ] Métricas:
    - [ ] Burndown chart
    - [ ] Velocity
    - [ ] Distribución de tiempo
  - **Tiempo estimado**: 2 horas

### **Trabajo en Playground (8-10 horas total)**

- [ ] **Deployment DEV → QA** (27 Enero)
  - [ ] Crear Change Set en DEV
  - [ ] Upload a QA
  - [ ] Deploy en QA
  - **Tiempo estimado**: 2 horas

- [ ] **Testing exhaustivo en QA** (28 Enero - 3 Febrero)
  - [ ] Ejecutar 21 test cases
  - [ ] Documentar resultados
  - [ ] Corregir bugs si hay
  - **Tiempo estimado**: 4-5 horas

- [ ] **Deployment QA → PROD** (5-6 Febrero)
  - [ ] Crear Change Set en QA
  - [ ] Upload a PROD
  - [ ] Deploy en PROD
  - [ ] Smoke testing
  - **Tiempo estimado**: 2 horas

- [ ] **Demo Final** (6 Febrero)
  - [ ] Preparar demo
  - [ ] Presentar al cliente
  - **Tiempo estimado**: 1 hora

---

## 🎯 RESUMEN DE HORAS ESTIMADAS

### **Semanas 1-2 (Completadas + Pendientes)**
- ✅ Completado: ~12 horas
- ⏳ Pendiente HOY: ~5 horas

### **Semana 3 (19-23 Enero)**
- Documentación: 5-6 horas
- Playground: 8-10 horas
- **Total**: 13-16 horas

### **Semana 4 (26 Enero - 6 Febrero)**
- Documentación: 6-8 horas
- Playground: 8-10 horas
- **Total**: 14-18 horas

### **TOTAL SPRINT 1**
- **Estimado**: 44-51 horas
- **Completado**: ~12 horas (24%)
- **Pendiente**: ~37 horas (76%)

---

## 📋 CHECKLIST DIARIO

### **HOY - 16 Enero (Viernes)**

**Documentación** (2-3 horas):
- [ ] Investigaciones 3, 4, 5 en [06-Investigaciones.md](06-Investigaciones.md)
- [ ] HU-003 en [02-Salesforce_Consultant.md](02-Salesforce_Consultant.md)
- [ ] Preguntas P10-P13 en [05-Preguntas_y_Dudas.md](05-Preguntas_y_Dudas.md)
- [ ] Daily #5 en [07-SPRINT_1.md](07-SPRINT_1.md)

**Playground** (2-3 horas):
- [ ] HU-001 completa en DEV

---

### **Lunes 19 Enero (Inicio Semana 3)**

**Documentación** (1 hora):
- [ ] Iniciar [03-Salesforce_Admin.md](03-Salesforce_Admin.md)
- [ ] Daily #6 en [07-SPRINT_1.md](07-SPRINT_1.md)

**Playground** (3-4 horas):
- [ ] Empezar HU-003: Crear objeto `Bank_Account__c`
- [ ] Crear primeros 3 campos

---

### **Martes 20 Enero**

**Documentación** (1 hora):
- [ ] Continuar [03-Salesforce_Admin.md](03-Salesforce_Admin.md) (HU-003)

**Playground** (3-4 horas):
- [ ] Completar campos de HU-003
- [ ] Configurar Platform Encryption

---

### **Miércoles 22 Enero**

**Documentación** (1 hora):
- [ ] Daily #7 en [07-SPRINT_1.md](07-SPRINT_1.md)
- [ ] Continuar [03-Salesforce_Admin.md](03-Salesforce_Admin.md)

**Playground** (3-4 horas):
- [ ] Crear Flow "Auto_Unmark_Primary_Account"
- [ ] Modificar Page Layout de Contact

---

### **Jueves 23 Enero**

**Documentación** (1 hora):
- [ ] Finalizar [03-Salesforce_Admin.md](03-Salesforce_Admin.md)

**Playground** (2-3 horas):
- [ ] Crear Formula Field y Reportes
- [ ] Testing inicial en DEV

---

## 💡 CONSEJOS PARA MANTENERTE AL DÍA

### **1. Documenta mientras trabajas**
❌ No hagas: Implementar todo y documentar al final  
✅ Haz: Cada vez que configures algo, documéntalo inmediatamente

### **2. Usa los ejemplos como guía**
- Los archivos actuales tienen ejemplos detallados
- Copia la estructura, adapta el contenido a TU trabajo real

### **3. Prioriza lo crítico**
Si vas con poco tiempo:
1. **Primero**: Trabajo en Playground (implementación)
2. **Segundo**: Documentación en [03-Salesforce_Admin.md](03-Salesforce_Admin.md)
3. **Tercero**: Resto de documentación

### **4. Toma screenshots**
- Cada configuración importante
- Resultados de tests
- Guárdalos en una carpeta organizada

### **5. Daily Standups de 5 minutos**
- No te toma más de 5 minutos
- Te ayuda a reflexionar sobre tu progreso

---

## 🚨 ALERTAS Y RECORDATORIOS

### **⚠️ Fechas Críticas**

| Fecha | Evento | Acción Requerida |
|-------|--------|------------------|
| **16 Enero (HOY)** | Fin Semana 2 | Completar investigaciones y HU-001 |
| **19 Enero** | Inicio Semana 3 | Empezar desarrollo HU-003 |
| **23 Enero** | Fin Semana 3 | HU-003 completa en DEV |
| **27 Enero** | Inicio Testing | Deployment a QA |
| **6 Febrero** | Fin Sprint 1 | Sprint Review y Retro |

### **📌 No Olvides**

- [ ] Guardar credenciales de ambientes de forma segura
- [ ] Hacer backup antes de deployments
- [ ] Tomar screenshots de configuraciones
- [ ] Actualizar [05-Preguntas_y_Dudas.md](05-Preguntas_y_Dudas.md) cuando surjan dudas
- [ ] Daily Standups cada día laborable

---

## 📞 SOPORTE

**Si tienes dudas**:
1. Revisa [00-GUIA_DE_USO.md](00-GUIA_DE_USO.md) (guía completa)
2. Revisa los archivos de ejemplo (tienen contenido detallado)
3. Consulta con tu equipo
4. Pregunta al instructor

---

**Última actualización**: 16 Enero 2026 22:10  
**Próxima revisión**: 19 Enero 2026  
**Grupo**: 3 - VISIONARY ADMINS

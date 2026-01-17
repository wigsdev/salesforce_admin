# 📘 GUÍA DE USO - Gestor de Versiones

## 🎯 Propósito de este Documento

Esta guía te indica **CUÁNDO y CÓMO** llenar cada archivo del Gestor de Versiones durante el desarrollo de tu proyecto Salesforce. Los archivos actuales contienen **ejemplos detallados** que debes usar como referencia para redactar tu documentación oficial.

---

## 📋 Índice Rápido

1. [Flujo General del Sprint](#flujo-general-del-sprint)
2. [Cronología de Llenado](#cronología-de-llenado)
3. [Guía por Archivo](#guía-por-archivo)
4. [Interrelaciones entre Archivos](#interrelaciones-entre-archivos)
5. [Checklist de Documentación](#checklist-de-documentación)

---

## 🔄 Flujo General del Sprint

```
┌─────────────────────────────────────────────────────────────────────┐
│                        FLUJO DEL SPRINT 1                           │
└─────────────────────────────────────────────────────────────────────┘

DÍA 1: Sprint Planning
   │
   ├─→ Crear Tablero Trello
   │   └─→ [Trello Board]
   │
   ↓
SEMANA 1: Análisis de Requerimientos
   │
   ├─→ Documentar análisis
   │   └─→ [01-Business_Analyst.md]
   │
   ├─→ Registrar preguntas
   │   └─→ [05-Preguntas_y_Dudas.md]
   │
   ├─→ Crear Historias de Usuario en Trello
   │   └─→ [Trello: 3 tarjetas en "To Do"]
   │
   ↓
SEMANA 2: Investigación Técnica
   │
   ├─→ Investigar alternativas
   │   └─→ [06-Investigaciones.md]
   │
   ├─→ Decidir soluciones
   │   └─→ [02-Salesforce_Consultant.md]
   │
   ↓
SEMANA 3: Desarrollo
   │
   ├─→ Mover tarjetas en Trello: "To Do" → "In Progress"
   │   └─→ [Trello: Actualizar estado]
   │
   ├─→ Implementar en DEV
   │   └─→ [03-Salesforce_Admin.md]
   │
   ├─→ Mover tarjetas en Trello: "In Progress" → "Testing"
   │   └─→ [Trello: Listo para QA]
   │
   ↓
SEMANA 4: Testing y Cierre
   │
   ├─→ Ejecutar tests en QA
   │   └─→ [04-Tester_QA.md]
   │
   ├─→ Mover tarjetas en Trello: "Testing" → "Done"
   │   └─→ [Trello: Completado]
   │
   ├─→ Sprint Review
   │   └─→ [07-SPRINT_1.md - Review]
   │
   └─→ Retrospective
       └─→ [07-SPRINT_1.md - Retro]
```

### **Herramientas Clave del Sprint**

1. **Trello**: Gestión visual de tareas (Historias de Usuario)
2. **Gestor de Versiones**: Documentación detallada del trabajo
3. **Salesforce Playgrounds**: Ambientes DEV, QA, PROD

**Relación**: 
- Trello = **QUÉ** hacer (tarjetas de HU)
- Gestor de Versiones = **CÓMO** se hizo (documentación detallada)
- Playgrounds = **DÓNDE** se hace (ambientes)

---

## ⏰ Cronología de Llenado

### **ANTES del Sprint (Preparación)**

| Archivo | Cuándo | Responsable | Acción |
|---------|--------|-------------|--------|
| `11-Ambiente_DEV.md` | Antes de empezar | Admin | Crear ambiente DEV y documentar credenciales |
| `12-Ambiente_QA.md` | Antes de empezar | Admin | Crear ambiente QA y documentar credenciales |
| `13-Ambiente_PROD.md` | Antes de empezar | Admin | Documentar acceso a PROD |

---

### **DÍA 1: Sprint Planning (Ej: 5 Enero)**

| Archivo/Herramienta | Momento | Responsable | Qué Documentar |
|---------------------|---------|-------------|----------------|
| **Trello** | Durante Planning | Scrum Master | - Crear tablero "Equipo 3 - Sprint 1"<br>- Crear 8 columnas: Backlog, To Do, In Progress, Code Review, Testing, QA Approved, Done, Blocked<br>- Crear etiquetas de Épicas (🔵 Gestión Clientes, 🔴 Seguridad, 🟢 Automatización)<br>- Invitar a los 9 miembros del equipo |
| `07-SPRINT_1.md` | Durante Planning | Scrum Master | - Sprint Goal<br>- User Stories seleccionadas<br>- Story Points<br>- Sprint Backlog (tasks) |

**📋 Referencia**: Ver `Practica_Financiera/04-Guia_Trello_Paso_a_Paso.md` para instrucciones detalladas de configuración de Trello.

---

### **SEMANA 1: Análisis (Ej: 6-9 Enero)**

| Archivo/Herramienta | Momento | Responsable | Qué Documentar |
|---------------------|---------|-------------|----------------|
| `01-Business_Analyst.md` | Al analizar cada requerimiento | Business Analyst | - Traducción de palabras del cliente a Salesforce<br>- Preguntas de indagación<br>- Problemas identificados<br>- Tabla resumen de soluciones |
| **Trello** | Después del análisis | Business Analyst + Scrum Master | - Crear 3 tarjetas (HU-001, HU-002, HU-003)<br>- Título: "[HU-XXX] [Título] (X pts)"<br>- Descripción: Problema, solución, criterios de aceptación<br>- Etiquetas: Épica correspondiente<br>- Checklist: Criterios de Aceptación<br>- Mover a columna "To Do" |
| `05-Preguntas_y_Dudas.md` | Cuando surjan dudas | Cualquier miembro | - Preguntas al cliente<br>- Preguntas técnicas<br>- Respuestas recibidas<br>- Decisiones tomadas |

**💡 Tip**: Actualiza `05-Preguntas_y_Dudas.md` **en tiempo real** cada vez que alguien haga una pregunta.

**📋 Referencia**: Las Historias de Usuario ya están redactadas en `Practica_Financiera/03-Requerimientos_SOLUCION.md`. Úsalas como base para crear las tarjetas en Trello.

---

### **SEMANA 2: Investigación y Decisiones (Ej: 12-16 Enero)**

| Archivo | Momento | Responsable | Qué Documentar |
|---------|---------|-------------|----------------|
| `06-Investigaciones.md` | Al evaluar alternativas técnicas | Consultant + Admin | - Opciones evaluadas (A vs B)<br>- Documentación consultada<br>- Pruebas realizadas<br>- Decisión final y justificación |
| `02-Salesforce_Consultant.md` | Después de investigar | Salesforce Consultant | - Soluciones propuestas para cada HU<br>- Alternativas evaluadas<br>- Votaciones del equipo<br>- Story Points asignados<br>- Tabla resumen de decisiones |
| `07-SPRINT_1.md` | Diariamente (15 min) | Scrum Master | - Daily Standups (¿Qué hice? ¿Qué haré? ¿Impedimentos?) |

**💡 Tip**: Documenta las investigaciones **ANTES** de empezar a desarrollar. Esto justifica tus decisiones técnicas.

---

### **SEMANA 3: Desarrollo (Ej: 19-23 Enero)**

| Archivo/Herramienta | Momento | Responsable | Qué Documentar |
|---------------------|---------|-------------|----------------|
| **Trello** | Al empezar cada HU | DEV Admins | - Mover tarjeta de "To Do" a "In Progress"<br>- Asignarse la tarjeta<br>- Actualizar comentarios con progreso |
| `03-Salesforce_Admin.md` | Al implementar cada HU | Salesforce Admin | - Configuración paso a paso<br>- Campos creados<br>- Flows/Validation Rules<br>- Page Layouts modificados<br>- Screenshots de configuración<br>- Notas para futuros admins |
| **Trello** | Al terminar desarrollo | DEV Admins | - Mover tarjeta a "Testing"<br>- Agregar comentario: "Listo para QA" |
| `07-SPRINT_1.md` | Diariamente | Scrum Master | - Daily Standups (actualizar progreso) |

**💡 Tip**: Documenta **mientras desarrollas**, no al final. Es más fácil recordar qué hiciste.

---

### **SEMANA 4: Testing y Cierre (Ej: 26 Enero - 6 Febrero)**

| Archivo/Herramienta | Momento | Responsable | Qué Documentar |
|---------------------|---------|-------------|----------------|
| **Trello** | Al empezar testing | QA Admins | - Asignarse la tarjeta<br>- Agregar comentario: "Iniciando testing" |
| `04-Tester_QA.md` | Al ejecutar cada test case | Tester QA | - Test cases con pasos detallados<br>- Resultados (PASS/FAIL)<br>- Screenshots de evidencia<br>- Bugs encontrados<br>- Estadísticas finales |
| **Trello** | Si test PASS | QA Admins | - Marcar checklist items como completados<br>- Mover tarjeta a "QA Approved" |
| **Trello** | Si test FAIL | QA Admins | - Mover tarjeta a "Blocked"<br>- Agregar etiqueta roja "Bug"<br>- Comentar qué falló<br>- Notificar a DEV Admins |
| `12-Ambiente_QA.md` | Durante testing | Tester QA | - Registro de testing (fecha, HU, resultado)<br>- Bugs reportados |
| **Trello** | Después de deployment a PROD | PROD Admins | - Mover tarjeta a "Done"<br>- Agregar comentario: "Deployed to PROD" |
| `14-DevOPS.md` | Al hacer deployment | Admin | - Change Sets creados<br>- Deployment logs<br>- Problemas encontrados |
| `07-SPRINT_1.md` | Al final del sprint | Scrum Master | - Sprint Review (demo, feedback)<br>- Retrospective (Start, Stop, Continue)<br>- Métricas (burndown, velocity) |

---

### **DESPUÉS del Sprint (Opcional para Sprints 2-3)**

| Archivo | Cuándo | Responsable | Acción |
|---------|--------|-------------|--------|
| `08-SPRINT_2.md` | Sprint 2 | Scrum Master | Usar como plantilla, llenar igual que Sprint 1 |
| `09-SPRINT_3.md` | Sprint 3 | Scrum Master | Usar como plantilla, llenar igual que Sprint 1 |
| `10-DEMO_FINAL.md` | Antes de demo final | Todo el equipo | - Guión de presentación<br>- Slides preparados<br>- Checklist de demo |

---

## 📂 Guía por Archivo

### **01-Business_Analyst.md**

**📅 Cuándo llenar**: Semana 1 (Análisis de requerimientos)  
**👤 Responsable**: Business Analyst  
**🔗 Se relaciona con**: `02-Salesforce_Consultant.md`, `05-Preguntas_y_Dudas.md`

**Qué documentar**:
1. **Por cada requerimiento del cliente**:
   - Traducción de palabras del cliente a términos Salesforce
   - Preguntas de indagación realizadas
   - Problemas identificados
   - Solución propuesta (alto nivel)

2. **Tabla resumen final**: Todos los requerimientos con su solución

**Ejemplo de uso**:
```
Cliente dice: "Necesito registrar garantes"
Tú documentas:
- Palabra cliente: "Garante"
- Traducción Salesforce: "Contact Role en Opportunity"
- Pregunta: ¿Cuántos garantes máximo?
- Respuesta: 1-3 garantes
```

---

### **02-Salesforce_Consultant.md**

**📅 Cuándo llenar**: Semana 2 (Después de investigar)  
**👤 Responsable**: Salesforce Consultant  
**🔗 Se relaciona con**: `01-Business_Analyst.md`, `06-Investigaciones.md`

**Qué documentar**:
1. **Por cada HU**:
   - Solución técnica propuesta
   - Alternativas evaluadas (Opción A vs B vs C)
   - Votación del equipo (quién votó por qué)
   - Decisión final y justificación
   - Story Points asignados

2. **Tabla resumen**: Todas las HU con decisiones y Story Points

**Flujo**:
1. Business Analyst identifica problema → 
2. Consultant investiga soluciones → 
3. Equipo vota → 
4. Consultant documenta decisión aquí

---

### **03-Salesforce_Admin.md**

**📅 Cuándo llenar**: Semana 3 (Durante desarrollo)  
**👤 Responsable**: Salesforce Admin  
**🔗 Se relaciona con**: `02-Salesforce_Consultant.md`, `04-Tester_QA.md`

**Qué documentar**:
1. **Por cada HU implementada**:
   - Configuración paso a paso (Setup → Object Manager → ...)
   - Campos creados (nombre, tipo, configuración)
   - Flows/Validation Rules (fórmulas completas)
   - Page Layouts modificados
   - Permission Sets creados
   - Reportes creados
   - Screenshots de configuración

2. **Deployment plan**: DEV → QA → PROD

3. **Notas para futuros admins**: Limitaciones, consideraciones

**💡 Tip**: Este es el archivo MÁS IMPORTANTE. Debe ser tan detallado que otro admin pueda replicar tu trabajo sin preguntar.

---

### **04-Tester_QA.md**

**📅 Cuándo llenar**: Semana 4 (Durante testing)  
**👤 Responsable**: Tester QA  
**🔗 Se relaciona con**: `03-Salesforce_Admin.md`, `12-Ambiente_QA.md`

**Qué documentar**:
1. **Por cada test case**:
   - ID único (TC-HU001-01)
   - Pasos para reproducir
   - Resultado esperado
   - Resultado obtenido (PASS/FAIL)
   - Screenshots de evidencia
   - Fecha y tester

2. **Resumen por HU**: Estadísticas (X/Y tests PASS)

3. **Bugs encontrados**: Si hay, documentar en detalle

**Flujo**:
1. Admin implementa HU → 
2. QA crea test cases → 
3. QA ejecuta tests → 
4. QA documenta resultados aquí

---

### **05-Preguntas_y_Dudas.md**

**📅 Cuándo llenar**: TODO EL SPRINT (en tiempo real)  
**👤 Responsable**: Cualquier miembro del equipo  
**🔗 Se relaciona con**: Todos los archivos

**Qué documentar**:
1. **Por cada pregunta**:
   - Fecha
   - Quién pregunta
   - A quién se dirige (cliente, equipo, etc.)
   - La pregunta
   - La respuesta
   - Impacto de la respuesta
   - Estado (Resuelta/Pendiente)

**💡 Tip**: Este archivo se llena **continuamente**. No esperes al final del sprint.

---

### **06-Investigaciones.md**

**📅 Cuándo llenar**: Semana 2 (Al evaluar alternativas)  
**👤 Responsable**: Consultant + Admin (trabajo en equipo)  
**🔗 Se relaciona con**: `02-Salesforce_Consultant.md`, `05-Preguntas_y_Dudas.md`

**Qué documentar**:
1. **Por cada investigación**:
   - Fecha
   - Contexto (¿Por qué investigamos?)
   - Opciones evaluadas (A vs B)
   - Documentación consultada (links)
   - Pruebas realizadas (con resultados)
   - Conclusión y decisión
   - Aprobación del equipo

**Ejemplo**:
```
Investigación: Contact Roles vs Junction Object
Opción A: Contact Roles (nativo)
  - Ventajas: Rápido, sin código
  - Desventajas: No permite campos custom
Opción B: Junction Object
  - Ventajas: Flexible
  - Desventajas: Consume objeto custom
Decisión: Opción A (Contact Roles)
Justificación: Cliente no necesita campos adicionales
```

---

### **07-SPRINT_1.md**

**📅 Cuándo llenar**: TODO EL SPRINT  
**👤 Responsable**: Scrum Master  
**🔗 Se relaciona con**: Todos los archivos (es el resumen del sprint)

**Qué documentar**:

**Día 1 (Planning)**:
- Sprint Goal
- User Stories seleccionadas
- Story Points
- Sprint Backlog (tasks)

**Diariamente (Daily Standups)**:
- ¿Qué hice ayer?
- ¿Qué haré hoy?
- ¿Impedimentos?

**Último día (Review + Retro)**:
- Demo realizada
- Feedback del cliente
- Start, Stop, Continue
- Métricas (burndown, velocity)

---

### **08-SPRINT_2.md, 09-SPRINT_3.md**

**📅 Cuándo llenar**: Durante Sprint 2 y 3  
**👤 Responsable**: Scrum Master  
**🔗 Se relaciona con**: `07-SPRINT_1.md` (misma estructura)

**Qué hacer**:
- Copiar la estructura de `07-SPRINT_1.md`
- Llenar con la información del nuevo sprint
- Mantener el mismo formato

---

### **10-DEMO_FINAL.md**

**📅 Cuándo llenar**: Antes de la demo final (último sprint)  
**👤 Responsable**: Todo el equipo  
**🔗 Se relaciona con**: Todos los archivos (resume todo el proyecto)

**Qué documentar**:
1. **Guión de presentación**: Qué mostrar, en qué orden
2. **Slides preparados**: Estructura de la presentación
3. **Checklist pre-demo**: Verificar que todo funciona
4. **Preguntas frecuentes**: Con respuestas preparadas
5. **Plan B**: Qué hacer si algo falla

---

### **11-Ambiente_DEV.md**

**📅 Cuándo llenar**: ANTES del sprint (preparación)  
**👤 Responsable**: Salesforce Admin  
**🔗 Se relaciona con**: `12-Ambiente_QA.md`, `13-Ambiente_PROD.md`

**Qué documentar**:
1. **Información de acceso**:
   - URL del ambiente
   - Usernames de los 2 admins
   - Emails de contacto
   - Responsables

2. **Registro de cambios**: Qué se configuró en DEV

**💡 Tip**: Actualiza este archivo cada vez que hagas un cambio importante en DEV.

---

### **12-Ambiente_QA.md**

**📅 Cuándo llenar**: Durante testing (Semana 4)  
**👤 Responsable**: Tester QA  
**🔗 Se relaciona con**: `04-Tester_QA.md`, `11-Ambiente_DEV.md`

**Qué documentar**:
1. **Información de acceso**: URLs, users
2. **Usuarios de testing**: Por cada perfil
3. **Datos de prueba**: Cómo se cargaron
4. **Registro de testing**: Tabla con fecha, HU, resultado

---

### **13-Ambiente_PROD.md**

**📅 Cuándo llenar**: Al hacer deployment a PROD  
**👤 Responsable**: Salesforce Admin  
**🔗 Se relaciona con**: `14-DevOPS.md`

**Qué documentar**:
1. **Información de acceso**: URLs, users (¡CONFIDENCIAL!)
2. **Historial de deployments**: Tabla con fecha, componentes, resultado
3. **Plan de rollback**: Qué hacer si algo falla

**⚠️ IMPORTANTE**: Este archivo contiene información sensible. Mantener seguro.

---

### **14-DevOPS.md**

**📅 Cuándo llenar**: Al hacer deployments  
**👤 Responsable**: Salesforce Admin  
**🔗 Se relaciona con**: `13-Ambiente_PROD.md`

**Qué documentar**:
1. **Change Sets creados**: Nombre, componentes
2. **Deployment logs**: Éxito/Fallo
3. **Problemas encontrados**: Y cómo se resolvieron
4. **Roadmap de automatización**: Planes futuros (SFDX, CI/CD)

---

## 🔗 Interrelaciones entre Archivos

### **Flujo de Información**

```
01-Business_Analyst.md (Análisis)
    ↓
05-Preguntas_y_Dudas.md (Preguntas al cliente)
    ↓
06-Investigaciones.md (Evaluar opciones técnicas)
    ↓
02-Salesforce_Consultant.md (Decisión técnica)
    ↓
03-Salesforce_Admin.md (Implementación)
    ↓
04-Tester_QA.md (Testing)
    ↓
07-SPRINT_1.md (Resumen del sprint)
```

### **Archivos que se Actualizan Continuamente**

- `05-Preguntas_y_Dudas.md`: TODO EL SPRINT
- `07-SPRINT_1.md`: TODO EL SPRINT (Daily Standups)
- `11-Ambiente_DEV.md`: Cada vez que cambies algo en DEV

### **Archivos que se Llenan una Sola Vez**

- `01-Business_Analyst.md`: Semana 1
- `02-Salesforce_Consultant.md`: Semana 2
- `03-Salesforce_Admin.md`: Semana 3
- `04-Tester_QA.md`: Semana 4

---

## ✅ Checklist de Documentación

### **Antes de Empezar el Sprint**

- [ ] Crear ambientes DEV, QA, PROD
- [ ] Documentar credenciales en archivos 11, 12, 13
- [ ] Leer el caso de estudio
- [ ] Preparar Trello

### **Semana 1: Análisis**

- [ ] Llenar `01-Business_Analyst.md` con análisis de cada requerimiento
- [ ] Documentar preguntas en `05-Preguntas_y_Dudas.md`
- [ ] Completar Sprint Planning en `07-SPRINT_1.md`
- [ ] Empezar Daily Standups en `07-SPRINT_1.md`

### **Semana 2: Investigación**

- [ ] Documentar investigaciones en `06-Investigaciones.md`
- [ ] Llenar `02-Salesforce_Consultant.md` con decisiones técnicas
- [ ] Continuar Daily Standups
- [ ] Actualizar `05-Preguntas_y_Dudas.md` si surgen dudas

### **Semana 3: Desarrollo**

- [ ] Documentar implementación en `03-Salesforce_Admin.md` (paso a paso)
- [ ] Actualizar `11-Ambiente_DEV.md` con cambios realizados
- [ ] Continuar Daily Standups
- [ ] Tomar screenshots de configuraciones

### **Semana 4: Testing y Cierre**

- [ ] Ejecutar tests y documentar en `04-Tester_QA.md`
- [ ] Actualizar `12-Ambiente_QA.md` con resultados de testing
- [ ] Hacer deployment y documentar en `14-DevOPS.md`
- [ ] Completar Sprint Review en `07-SPRINT_1.md`
- [ ] Completar Retrospective en `07-SPRINT_1.md`
- [ ] Calcular métricas (burndown, velocity)

### **Al Finalizar el Sprint**

- [ ] Revisar que todos los archivos estén completos
- [ ] Verificar que las fechas sean coherentes
- [ ] Asegurar que hay evidencia (screenshots)
- [ ] Preparar para demo final (si aplica)

---

## 💡 Consejos Prácticos

### **1. Documenta en Tiempo Real**
❌ **No hagas**: Esperar al final del sprint para documentar todo  
✅ **Haz**: Documenta cada día lo que hiciste

### **2. Usa los Ejemplos como Referencia**
❌ **No hagas**: Copiar y pegar los ejemplos tal cual  
✅ **Haz**: Usa los ejemplos para entender QUÉ documentar, luego escribe tu propia versión

### **3. Sé Específico**
❌ **No hagas**: "Configuré un campo"  
✅ **Haz**: "Creé el campo Monthly_Salary__c (Currency, 16,2) en Contact con FLS restringido a perfil Ejecutivo de Créditos"

### **4. Incluye Screenshots**
- Configuraciones importantes
- Resultados de tests
- Errores encontrados

### **5. Mantén Consistencia de Fechas**
- Usa el mismo formato en todos los archivos
- Asegúrate de que las fechas sean coherentes con el calendario del sprint

---

## 🎯 Resumen Ejecutivo

| Archivo | Cuándo | Quién | Para Qué |
|---------|--------|-------|----------|
| 01-Business_Analyst | Semana 1 | BA | Análisis de requerimientos |
| 02-Salesforce_Consultant | Semana 2 | Consultant | Decisiones técnicas |
| 03-Salesforce_Admin | Semana 3 | Admin | Implementación detallada |
| 04-Tester_QA | Semana 4 | QA | Testing y evidencia |
| 05-Preguntas_y_Dudas | Todo el sprint | Todos | Registro de Q&A |
| 06-Investigaciones | Semana 2 | Consultant+Admin | Justificar decisiones |
| 07-SPRINT_1 | Todo el sprint | Scrum Master | Ceremonias Agile |
| 08-SPRINT_2 | Sprint 2 | Scrum Master | Plantilla Sprint 2 |
| 09-SPRINT_3 | Sprint 3 | Scrum Master | Plantilla Sprint 3 |
| 10-DEMO_FINAL | Antes de demo | Todos | Guión de presentación |
| 11-Ambiente_DEV | Antes + durante | Admin | Credenciales DEV |
| 12-Ambiente_QA | Semana 4 | QA | Credenciales QA + testing log |
| 13-Ambiente_PROD | Al deployar | Admin | Credenciales PROD + deployments |
| 14-DevOPS | Al deployar | Admin | Change Sets y deployment logs |

---

## 📞 ¿Dudas?

Si tienes dudas sobre qué documentar en algún archivo:

1. **Revisa el ejemplo**: Los archivos actuales tienen ejemplos detallados
2. **Pregunta a tu equipo**: Especialmente al Scrum Master
3. **Consulta esta guía**: Busca el archivo en la sección "Guía por Archivo"

---

**Última actualización**: 16 Enero 2026  
**Versión**: 1.0  
**Autor**: Equipo 3 - Wilmer Gulcochia Sanchez

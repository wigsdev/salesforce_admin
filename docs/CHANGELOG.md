# 📝 CHANGELOG - Prácticas Sprint 1

Registro cronológico de todas las actividades de resolución de prácticas del Sprint 1.

---

## [2.1.0] - 2026-01-16

### 🎉 Práctica Clase 5 - Consolidación - COMPLETADA

#### ✅ Validado

**Clase 5 - Práctica**: Clase de consolidación y validación

La Clase 5 NO requiere archivos adicionales. Es una clase donde los estudiantes validan que tienen:

1. ✅ **Trello configurado** (completado en Clase 3)
   - Tablero con 8 columnas Agile
   - 3 tarjetas (HU-001, HU-002, HU-003)
   - Etiquetas de Épicas y Prioridades
   - Checklists de Criterios de Aceptación

2. ✅ **Gestor de Versiones completo** (completado en Clase 4)
   - 15 archivos (14 documentos + 1 README)
   - Documentación de roles (Business Analyst, Consultant, Admin, QA)
   - Documentación de Sprint 1 completo
   - Plantillas para Sprints 2-3 y Demo Final
   - Guías de ambientes (DEV, QA, PROD)
   - Guía de DevOPS

3. ✅ **Ambientes creados** (plantillas en Clase 4)
   - Instrucciones de creación de DEV, QA, PROD
   - Nomenclatura de usernames
   - Checklists de configuración

4. ✅ **Historias de Usuario** (completadas en Clase 3)
   - 3 HU con 16 Story Points
   - 17 Criterios de Aceptación
   - Soluciones técnicas documentadas

#### 📝 Actualizado

**Archivos actualizados**:

1. **`Gestor_de_Versiones/07-SPRINT_1.md`**
   - ✅ Duración corregida: **4 semanas** (5 Enero - 6 Febrero 2026)
   - ✅ Sprint Planning: 5 Enero (Día 1)
   - ✅ Daily Standups: 8 dailys distribuidos en 4 semanas
   - ✅ Sprint Review: 6 Febrero (último día)
   - ✅ Retrospective: 6 Febrero
   - ✅ Burndown chart: Por semanas (no por días)
   - ✅ Distribución de tiempo: 160 horas (4 semanas)
   - ✅ Próximos pasos: Deployment 6 Feb, Sprint 2 Planning 9 Feb

2. **`docs/TASK_LIST.md`**
   - ✅ Estado actualizado: 5/5 prácticas (100%) 🎉
   - ✅ Clase 5 marcada como completa
   - ✅ Métricas actualizadas
   - ✅ Próximas acciones: Solo Superbadges pendientes

#### 📊 Métricas

- **Prácticas completadas**: 5/5 (100%)
- **Archivos totales generados**: 24 archivos
- **Páginas de documentación**: ~200+ páginas
- **Story Points**: 16
- **Test Cases**: 21 (100% PASS)
- **Sprint ajustado**: 4 semanas (5 Enero - 6 Febrero)

#### 🎯 Estado del Sprint 1

**Semanas completadas**: 2 de 4 (50%)
- ✅ Semana 1 (5-9 Enero): Fundamentos, Modelado de Datos
- ✅ Semana 2 (12-16 Enero): Superbadge, Gestión Usuarios, Fórmulas
- ⏳ Semana 3 (19-23 Enero): Seguridad I, II, III
- ⏳ Semana 4 (26 Enero - 6 Febrero): Reportes, Service Cloud, Superbadges finales

**Prácticas**: 5/5 completadas ✅  
**Superbadges**: 0/3 completados (programados para Semanas 3-4)

---

## [2.0.0] - 2026-01-16

### 🎉 Práctica Clase 4 - Gestor de Versiones - COMPLETADA

#### ✅ Agregado

**Carpeta**: `Gestor_de_Versiones/`

1. **`README.md`** (1.5 KB)
   - Índice de navegación de los 14 archivos
   - Descripción de cada sección (Roles, Sprints, Ambientes, DevOPS)
   - Estado y métricas del proyecto

2. **`01-Business_Analyst.md`** (9.2 KB)
   - Análisis completo de 3 requerimientos de Financiera Horizonte
   - Traducción de palabras del cliente a Salesforce
   - Preguntas de indagación realizadas (9 preguntas)
   - Tabla resumen de soluciones
   - Entregables del análisis

3. **`02-Salesforce_Consultant.md`** (11.5 KB)
   - Soluciones técnicas propuestas para cada HU
   - Evaluación de alternativas (Contact Roles vs Junction Object, FLS vs Page Layouts, etc.)
   - Votaciones del equipo documentadas
   - Justificación de decisiones técnicas
   - Tabla resumen de decisiones (16 Story Points)

4. **`03-Salesforce_Admin.md`** (28.7 KB) ⭐
   - Implementación técnica detallada de las 3 HU
   - **HU-001**: Contact Roles configuration (5 test cases)
   - **HU-002**: Field-Level Security setup (7 test cases)
   - **HU-003**: Custom Object `Bank_Account__c` (9 test cases)
   - Configuración paso a paso de:
     - 8 campos custom
     - 1 Flow (Auto_Unmark_Primary_Account)
     - Platform Encryption
     - Page Layouts
     - Permission Sets
     - 3 Reportes
   - Deployment plan (DEV → QA → PROD)
   - Notas para futuros administradores

5. **`04-Tester_QA.md`** (18.3 KB)
   - Plan de testing completo
   - **21 test cases** documentados:
     - HU-001: 5 test cases (100% PASS)
     - HU-002: 7 test cases (100% PASS)
     - HU-003: 9 test cases (100% PASS)
   - Testing de seguridad (FLS, API, reportes)
   - Testing de encriptación (Platform Encryption)
   - Testing de Flow (auto-desmarcar cuenta primaria)
   - 4 usuarios de prueba utilizados
   - Estadísticas: 21/21 PASS, 0 bugs

6. **`05-Preguntas_y_Dudas.md`** (7.8 KB)
   - **15 preguntas** resueltas:
     - 3 preguntas generales del proyecto
     - 3 preguntas sobre HU-001 (Garantes)
     - 3 preguntas sobre HU-002 (Salario)
     - 4 preguntas sobre HU-003 (Cuentas)
     - 2 preguntas técnicas del equipo
   - Todas las preguntas con respuestas y decisiones tomadas
   - Lecciones aprendidas

7. **`06-Investigaciones.md`** (11.2 KB)
   - **5 investigaciones técnicas** documentadas:
     - Contact Roles vs Junction Object
     - FLS vs Page Layouts (con pruebas)
     - Platform Encryption para CBU
     - Validation Rule vs Flow
     - Change Sets vs SFDX
   - Documentación oficial consultada
   - Trailhead modules referenciados
   - Tabla resumen de decisiones

8. **`07-SPRINT_1.md`** (14.6 KB)
   - Sprint Planning completo (16 Story Points)
   - 7 Daily Standups documentados
   - Sprint Review con demo al cliente
   - Sprint Retrospective (Start, Stop, Continue)
   - Burndown chart
   - Velocity: 16 pts (100% completado)
   - Métricas de tiempo (46.25h productivas)
   - Lecciones aprendidas

9. **`08-SPRINT_2.md`** (3.2 KB) - PLANTILLA
   - Estructura completa para Sprint 2
   - Secciones: Planning, Daily Standups, Review, Retrospective
   - Métricas y Definition of Done
   - Listo para que estudiantes completen

10. **`09-SPRINT_3.md`** (2.8 KB) - PLANTILLA
    - Estructura completa para Sprint 3
    - Incluye velocity acumulada
    - Listo para que estudiantes completen

11. **`10-DEMO_FINAL.md`** (12.4 KB) - GUÍA
    - Guión completo de presentación (45 minutos)
    - 3 secciones de demo (Garantes, Seguridad, Cuentas)
    - Estructura de slides sugerida (8 slides)
    - Preguntas frecuentes con respuestas
    - Checklist pre/durante/post demo
    - Plan B en caso de fallas técnicas

12. **`11-Ambiente_DEV.md`** (9.8 KB) - GUÍA
    - Instrucciones paso a paso para crear Developer Sandbox
    - Cómo crear 2 usuarios Admin
    - Configuración de My Domain
    - Nomenclatura de usernames: `nombre.apellido@equipo[X].com.dev`
    - Checklist de configuración inicial
    - Buenas prácticas de seguridad
    - Troubleshooting de problemas comunes

13. **`12-Ambiente_QA.md`** (11.2 KB) - GUÍA
    - Instrucciones para crear Partial Copy Sandbox
    - Crear usuarios de testing (diferentes perfiles)
    - Estrategia de datos de prueba
    - Cómo cargar datos (Data Loader, Import Wizard, Apex)
    - Proceso de testing en QA
    - Sincronización con DEV (Change Sets, SFDX)
    - Gestión de bugs

14. **`13-Ambiente_PROD.md`** (13.7 KB) - GUÍA
    - **REGLAS CRÍTICAS** para PROD (qué NUNCA hacer)
    - Instrucciones de configuración de acceso
    - Proceso completo de deployment (Change Sets, SFDX)
    - Pre/Post deployment checklists
    - Plan de rollback detallado
    - Estrategia de backup
    - Seguridad y auditoría
    - Monitoreo de PROD

15. **`14-DevOPS.md`** (10.9 KB) - GUÍA
    - Flujo de trabajo DevOPS (DEV → QA → PROD)
    - Herramientas actuales vs recomendadas
    - Proceso detallado de Change Sets
    - Guía de migración a SFDX:
      - Instalación (Windows, Mac, Linux)
      - Comandos básicos (retrieve, deploy, open)
    - Control de versiones con Git
    - CI/CD con GitHub Actions (ejemplo de workflow)
    - Métricas de DevOPS
    - Roadmap de automatización

#### 📊 Métricas

- **Archivos creados**: 15 (14 documentos + 1 README)
- **Tamaño total**: ~150 KB
- **Páginas de documentación**: ~150+ páginas
- **Test cases documentados**: 21
- **Preguntas resueltas**: 15
- **Investigaciones técnicas**: 5
- **Ceremonias Agile**: 4 (Planning, Daily, Review, Retro)
- **Daily Standups**: 7
- **Story Points**: 16

#### 🎯 Cobertura

- ✅ Documentación completa del Sprint 1 (archivos 01-07)
- ✅ Plantillas para Sprints futuros (archivos 08-10)
- ✅ Guías de ambientes Salesforce (archivos 11-13)
- ✅ Guía de DevOPS y automatización (archivo 14)
- ✅ Análisis de Business Analyst
- ✅ Soluciones de Salesforce Consultant
- ✅ Implementación de Salesforce Admin
- ✅ Testing de QA (21 test cases, 100% PASS)
- ✅ Preguntas y dudas resueltas
- ✅ Investigaciones técnicas documentadas
- ✅ Ceremonias Agile completas
- ✅ Instrucciones de creación de ambientes
- ✅ Procesos de deployment
- ✅ Roadmap de DevOPS

#### 🔗 Relación con Práctica Clase 3

El Gestor de Versiones documenta la **implementación real** del caso Financiera Horizonte (Clase 3):
- Mismo proyecto (Financiera Horizonte S.A.)
- Mismas 3 HU (Garantes, Salario, Cuentas)
- Documentación de TODO el ciclo de vida del proyecto
- Desde análisis hasta deployment a PROD

---

## [1.0.0] - 2026-01-16

### 🎉 Práctica Clase 3 - Financiera Horizonte S.A. - COMPLETADA

#### ✅ Agregado

**Carpeta**: `Practica_Financiera/`

1. **`README.md`** (3.0 KB)
   - Índice de navegación de todos los archivos
   - Resumen de Story Points y Épicas
   - Instrucciones de uso para estudiantes

2. **`01-Caso_de_Estudio.md`** (2.8 KB)
   - Descripción completa de Financiera Horizonte S.A.
   - Objetivos estratégicos 2026
   - Objetivos dentro de Salesforce
   - 3 Requerimientos del Gerente de Finanzas (A, B, C)

3. **`02-Guia_Alumnos.md`** (2.2 KB)
   - Metodología de indagación (rol del Consultor)
   - Formato de Historias de Usuario (Agile)
   - Ejemplo completo de redacción de HU
   - Criterios de Aceptación (Definition of Done)
   - Estructura de tablero Trello

4. **`03-Requerimientos_SOLUCION.md`** (9.9 KB)
   - **Requerimiento 1: Garantes**
     - Análisis técnico del problema
     - Solución: Contact Roles en Opportunities
     - Historia de Usuario HU-001 completa
     - 5 Criterios de Aceptación
     - Story Points: 5 | Épica: 🔵 Gestión de Clientes
   
   - **Requerimiento 2: Salario Oculto**
     - Análisis de seguridad (Field-Level Security)
     - Solución: FLS + Permission Sets
     - Historia de Usuario HU-002 completa
     - 5 Criterios de Aceptación
     - Story Points: 3 | Épica: 🔴 Seguridad y Permisos
   
   - **Requerimiento 3: Múltiples Cuentas Bancarias**
     - Análisis de modelo de datos (relación 1:N)
     - Solución: Objeto Custom `Bank_Account__c`
     - Historia de Usuario HU-003 completa
     - 7 Criterios de Aceptación
     - Story Points: 8 | Épica: 🟢 Automatización
   
   - Tabla resumen de soluciones
   - Total: 16 Story Points

5. **`04-Guia_Trello_Paso_a_Paso.md`** (12.8 KB)
   - **Parte 1**: Crear y configurar tablero (8 columnas Agile)
   - **Parte 2**: Crear etiquetas (Épicas: Azul, Rojo, Verde + Prioridades)
   - **Parte 3**: Crear las 3 tarjetas (HU-001, HU-002, HU-003)
     - Títulos con Story Points
     - Descripciones completas con soluciones técnicas
     - Checklists de Criterios de Aceptación
   - **Parte 4**: Personalización avanzada (Power-Ups, Custom Fields)
   - **Parte 5**: Organizar Sprint (mover tarjetas, Sprint Goal)
   - **Parte 6**: Filtros y atajos de teclado
   - **Parte 7**: Verificación final (checklist)
   - **Parte 8**: Compartir con equipo
   - **Parte 9**: Buenas prácticas (WIP limits, regla de oro)
   - Tiempo estimado: 20-30 minutos

6. **`05-Resumen_Visual.md`** (11.9 KB)
   - Vista rápida del Sprint 1
   - Tarjetas visuales de las 3 HU
   - Diagrama de arquitectura (Mermaid)
   - Gráfico de distribución de Story Points
   - Tabla de Épicas y distribución
   - Flujo de trabajo en Trello (diagrama ASCII)
   - Lista completa de Criterios de Aceptación
   - Configuración técnica requerida en Salesforce
   - Timeline sugerido (2 semanas)
   - Objetivos de negocio impactados
   - Próximos pasos

#### 📊 Métricas

- **Archivos creados**: 6
- **Tamaño total**: ~43 KB
- **Historias de Usuario**: 3
- **Story Points totales**: 16
- **Criterios de Aceptación**: 17
- **Épicas**: 3
- **Objetos Salesforce involucrados**: 4 (Contact, Opportunity, Bank_Account__c custom, Contact Roles)

#### 🎯 Cobertura

- ✅ Caso de negocio completo
- ✅ Metodología Agile para estudiantes
- ✅ Análisis técnico de Salesforce Senior Admin
- ✅ Soluciones con objetos, campos y configuración
- ✅ Historias de Usuario profesionales
- ✅ Guía paso a paso para Trello (9 partes)
- ✅ Resumen visual con diagramas
- ✅ Validation Rules, Flows, FLS explicados
- ✅ Timeline y próximos pasos

---

## [0.3.0] - 2026-01-16

### 🧹 Limpieza de Contenido Duplicado

#### ✅ Corregido

1. **`05-clase_3_teoria.md`**
   - Eliminada sección duplicada "Estructuración de la información"
   - Limpiada tabla "Diferencias entre objetos Estándar y Custom" (filas redundantes)
   - Limpiada tabla "Diferencias entre campos Estándar y Custom" (filas redundantes)
   - Eliminada sección duplicada "Relacionales y textuales avanzados"
   - **Total**: 4 duplicaciones eliminadas

2. **`08_10-clase_4_practica.md`**
   - Eliminada sección duplicada "Equipo Salesforce" completa
   - **Total**: 1 duplicación eliminada

3. **`10_12-clase_5_practica.md`**
   - Eliminada sección duplicada "Equipo Salesforce" completa
   - **Total**: 1 duplicación eliminada

4. **`13-clase_8_superbadge.md`**
   - Eliminada sección duplicada "¿Por qué son vitales para tu carrera?"
   - **Total**: 1 duplicación eliminada

#### 📊 Métricas de Limpieza

- **Archivos analizados**: 13
- **Archivos con duplicados**: 4
- **Duplicaciones eliminadas**: 7
- **Archivos limpios**: 13/13 (100%)

---

## [0.2.0] - 2026-01-16

### 📁 Reestructuración de Archivos

#### ✅ Agregado

- Carpeta `curriculum/sprint_01/semana_01/` con clases 1-4
- Carpeta `curriculum/sprint_01/semana_02/` con clases 5-8
- Carpeta `raw_data/` con archivos `.pptx.txt` originales
- Carpeta `schedules/` con cronogramas

#### 🔄 Movido

- Todos los archivos `.md` de clases a `curriculum/`
- Archivos raw a `raw_data/`
- Cronogramas a `schedules/`

#### 📝 Actualizado

- `course_structure.md` con enlaces corregidos
- Estructura de 2 semanas (4 clases por semana)

---

## [0.1.0] - 2026-01-16

### 🎬 Inicio del Proyecto

#### ✅ Agregado

1. **Conversión de archivos raw a Markdown**
   - 13 archivos `.pptx.txt` convertidos a `.md`
   - Formato Markdown aplicado (headings, listas, tablas)
   - Contenido original preservado al 100%

2. **Documentos de planificación**
   - `sprint1_schedule.md` - Cronograma completo
   - `course_structure.md` - Estructura del curso
   - `task.md` - Lista de tareas

3. **Análisis inicial**
   - `salesforce_course_analysis.md` - Análisis de contenido

#### 📊 Métricas Iniciales

- **Archivos raw procesados**: 13
- **Archivos Markdown generados**: 13
- **Clases teóricas**: 7
- **Clases prácticas**: 4
- **Superbadges**: 2

---

## 📋 Leyenda de Cambios

- **✅ Agregado**: Nuevos archivos o funcionalidades
- **🔄 Movido**: Archivos reubicados
- **📝 Actualizado**: Archivos modificados
- **🧹 Corregido**: Errores o duplicados eliminados
- **🗑️ Eliminado**: Archivos o contenido removido
- **📊 Métricas**: Estadísticas de cambios

---

## 🔮 Próximas Versiones

### [3.0.0] - Planificado (Semanas 3-4)
- Clase 4 - Superbadge (Object Relationships)
- Clase 8 - Superbadge (Fórmulas + User Authentication)

---

**Formato de versiones**: [MAJOR.MINOR.PATCH]
- **MAJOR**: Práctica completa nueva
- **MINOR**: Actualizaciones significativas
- **PATCH**: Correcciones menores

**Última actualización**: 2026-01-16 21:35  
**Proyecto**: Admin Salesforce + Agent Force - Sprint 1

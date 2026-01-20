# 00-ORGANIZACION_EQUIPO.md - Estructura de Proyecto

## 📋 Proyecto: Universidad Lumina Tech
**Grupo**: 3 - VISIONARY ADMINS  
**Total Miembros**: 9 estudiantes activos

---

## 🎯 Distribución de Roles

### **Administradores de Ambientes (6 personas)**

#### **Ambiente DEV (2 Admins)**
| # | Rol | Responsabilidad Principal |
|---|-----|---------------------------|
| 1 | **Salesforce Admin DEV 1** | Desarrollo de Objetos (Carrera, Materia) |
| 2 | **Salesforce Admin DEV 2** | Desarrollo de Seguridad y Validaciones |

**Tareas**:
- Implementar las Historias de Usuario (HU) en DEV.
- Documentar en [03-Salesforce_Admin.md](03-Salesforce_Admin.md).
- Actualizar [11-Ambiente_DEV.md](11-Ambiente_DEV.md).

---

#### **Ambiente QA (2 Admins)**
| # | Rol | Responsabilidad Principal |
|---|-----|---------------------------|
| 3 | **QA Tester 1** | Testing de Seguridad (HUs de Privacidad) |
| 4 | **QA Tester 2** | Testing de Datos (HUs de Calidad) |

**Tareas**:
- Ejecutar test cases y reportar bugs.
- Documentar en [04-Tester_QA.md](04-Tester_QA.md).
- Actualizar [12-Ambiente_QA.md](12-Ambiente_QA.md).

---

#### **Ambiente PROD (2 Admins)**
| # | Rol | Responsabilidad Principal |
|---|-----|---------------------------|
| 5 | **Deployment Manager** | Gestión de Change Sets y Deployments |
| 6 | **Release Manager** | Validación final y Demo al Cliente |

**Tareas**:
- Desplegar cambios a PROD.
- Documentar en [14-DevOPS.md](14-DevOPS.md).
- Actualizar [13-Ambiente_PROD.md](13-Ambiente_PROD.md).

---

### **Roles Funcionales (3 personas)**

#### **Business Analyst (BA)**
| # | Rol | Responsabilidad |
|---|-----|-----------------|
| 7 | **Business Analyst** | Análisis de Requerimientos y Q&A |

**Tareas**:
- Traducir `SPRINT 1.md` a requerimientos técnicos.
- Mantener [01-Business_Analyst.md](01-Business_Analyst.md).
- Gestionar [05-Preguntas_y_Dudas.md](05-Preguntas_y_Dudas.md).

---

#### **Salesforce Consultant**
| # | Rol | Responsabilidad |
|---|-----|-----------------|
| 8 | **Consultant** | Arquitectura y Decisiones Técnicas |

**Tareas**:
- Diseñar el Modelo de Datos (ERD).
- Documentar decisiones en [02-Salesforce_Consultant.md](02-Salesforce_Consultant.md).
- Realizar investigaciones [06-Investigaciones.md](06-Investigaciones.md).

---

#### **Scrum Master**
| # | Rol | Responsabilidad |
|---|-----|-----------------|
| 9 | **Scrum Master** | Facilitador, Trello y Documentación General |

**Tareas**:
- Mantener [07-SPRINT_1.md](07-SPRINT_1.md) actualizado.
- Coordinar Daily Standups.
- Gestionar el tablero Trello.

---

## 🔄 Matriz de Responsabilidad por Archivo

| Archivo | Responsable(s) |
|---------|----------------|
| `00-PLAN/EQUIPO/TRELLO` | Scrum Master |
| `01-Business_Analyst` | BA |
| `02-Salesforce_Consultant` | Consultant |
| `03-Salesforce_Admin` | Dev Admins |
| `04-Tester_QA` | QA Testers |
| `05-Preguntas` | BA (Coordina) |
| `06-Investigaciones` | Consultant |
| `07-SPRINT_1` | Scrum Master |
| `11-DEV` | Dev Admins |
| `12-QA` | QA Testers |
| `13-PROD` | Prod Admins |
| `14-DevOPS` | Prod Admins |

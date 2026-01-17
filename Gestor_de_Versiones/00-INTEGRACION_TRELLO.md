# 📋 INTEGRACIÓN: Trello + Gestor de Versiones

## 🎯 Objetivo

Este documento explica cómo **Trello** y el **Gestor de Versiones** trabajan juntos para gestionar el proyecto Salesforce.

---

## 🔗 Relación entre Herramientas

### **Trello (Gestión Visual)**
- **QUÉ** hacer: Tarjetas de Historias de Usuario
- **ESTADO** de cada tarea: To Do, In Progress, Testing, Done
- **QUIÉN** está trabajando en qué: Asignaciones
- **Actualización**: Diaria (mover tarjetas, comentarios)

### **Gestor de Versiones (Documentación Detallada)**
- **CÓMO** se hizo: Pasos técnicos detallados
- **POR QUÉ** se tomaron decisiones: Investigaciones, alternativas
- **EVIDENCIA**: Screenshots, test cases, resultados
- **Actualización**: Continua (mientras trabajas)

### **Carpeta Practica_Financiera (Referencia)**
- **Historias de Usuario**: Ya redactadas en [03-Requerimientos_SOLUCION.md](../Practica_Financiera/03-Requerimientos_SOLUCION.md)
- **Guía de Trello**: Paso a paso en [04-Guia_Trello_Paso_a_Paso.md](../Practica_Financiera/04-Guia_Trello_Paso_a_Paso.md)
- **Caso de estudio**: Contexto en [01-Caso_de_Estudio.md](../Practica_Financiera/01-Caso_de_Estudio.md)

---

## 📊 Flujo de Trabajo Integrado

```
┌──────────────────────────────────────────────────────────────────────────┐
│           FLUJO INTEGRADO: Practica → Trello → Gestor                   │
└──────────────────────────────────────────────────────────────────────────┘

PASO 1: Leer Historias de Usuario
   │
   └─→ Practica_Financiera/03-Requerimientos_SOLUCION.md
       (HU-001, HU-002, HU-003 ya redactadas)
       │
       ↓
PASO 2: Crear Tarjetas en Trello
   │
   └─→ Trello: Crear 3 tarjetas
       └─→ Mover a columna "To Do"
       │
       ↓
PASO 3: Investigar Solución
   │
   └─→ Gestor_de_Versiones/06-Investigaciones.md
       (Documentar alternativas evaluadas)
       │
       ↓
PASO 4: Empezar Desarrollo
   │
   ├─→ Trello: Mover tarjeta a "In Progress"
   │
   └─→ Salesforce DEV: Implementar configuración
       │
       ↓
PASO 5: Documentar Implementación
   │
   └─→ Gestor_de_Versiones/03-Salesforce_Admin.md
       (Paso a paso de configuración)
       │
       ↓
PASO 6: Listo para Testing
   │
   └─→ Trello: Mover tarjeta a "Testing"
       │
       ↓
PASO 7: Ejecutar Tests
   │
   ├─→ Salesforce QA: Ejecutar test cases
   │
   └─→ Gestor_de_Versiones/04-Tester_QA.md
       (Documentar resultados)
       │
       ↓
PASO 8: ¿Test PASS?
   │
   ├─→ SÍ → Trello: Mover a "Done"
   │        └─→ Deployment a PROD
   │             └─→ Gestor_de_Versiones/14-DevOPS.md
   │
   └─→ NO → Trello: Mover a "Blocked"
             └─→ Volver a PASO 4 (corregir)
```

---

## 📅 Cronología de Uso

### **Día 1 (5 Enero): Sprint Planning**

**Paso 1: Crear Tablero Trello**
1. Ir a [Trello](https://trello.com)
2. Crear tablero: "Equipo 3 - Sprint 1 - Financiera Horizonte"
3. Crear 8 columnas:
   - 📋 Backlog
   - ✅ To Do
   - 🔄 In Progress
   - 👀 Code Review
   - 🧪 Testing
   - ✔️ QA Approved
   - ✅ Done
   - 🚫 Blocked

4. Crear etiquetas:
   - 🔵 Gestión de Clientes (azul)
   - 🔴 Seguridad y Permisos (rojo)
   - 🟢 Automatización (verde)
   - 🟡 Alta Prioridad (amarillo)
   - 🟠 Media Prioridad (naranja)

**Paso 2: Invitar al Equipo**
- Invitar a los 9 miembros del equipo
- Asignar permisos de edición a todos

**Referencia**: [Practica_Financiera/04-Guia_Trello_Paso_a_Paso.md](../Practica_Financiera/04-Guia_Trello_Paso_a_Paso.md) (Partes 1-2)

---

### **Semana 1 (6-9 Enero): Crear Historias de Usuario**

**Paso 3: Leer Historias de Usuario**
- Abrir [Practica_Financiera/03-Requerimientos_SOLUCION.md](../Practica_Financiera/03-Requerimientos_SOLUCION.md)
- Leer HU-001, HU-002, HU-003 completas

**Paso 4: Crear Tarjetas en Trello**

#### **Tarjeta 1: HU-001 (Garantes)**

**Título**: `[HU-001] Registrar Garantes en Préstamos (5 pts)`

**Descripción**:
```
**Como** Ejecutivo de Créditos
**Quiero** registrar hasta 3 garantes por préstamo
**Para** tener respaldo en caso de impago

**Solución Técnica**:
- Contact Roles en Opportunity
- Picklist con roles: Garante, Co-deudor
- Page Layout modificado
- Reporte de análisis

**Épica**: 🔵 Gestión de Clientes
**Story Points**: 5
```

**Checklist** (Criterios de Aceptación):
- [ ] CA-1: Agregar hasta 3 garantes por préstamo
- [ ] CA-2: Roles diferenciados (Garante vs Co-deudor)
- [ ] CA-3: Reporte de préstamos con/sin garantes
- [ ] CA-4: Editar información de garantes
- [ ] CA-5: Eliminar garantes si préstamo no está aprobado

**Etiquetas**: 🔵 Gestión de Clientes, 🟡 Alta Prioridad

**Asignar a**: Estudiantes 1-2 (DEV Admins)

**Mover a**: "To Do"

---

#### **Tarjeta 2: HU-002 (Salario Oculto)**

**Título**: `[HU-002] Ocultar Salario a Atención al Cliente (3 pts)`

**Descripción**:
```
**Como** Gerente de Finanzas
**Quiero** que Atención al Cliente NO vea el salario
**Para** proteger información sensible

**Solución Técnica**:
- Field-Level Security en Monthly_Salary__c
- Permission Set "Financial_Data_Access"
- Page Layouts diferenciados

**Épica**: 🔴 Seguridad y Permisos
**Story Points**: 3
```

**Checklist** (Criterios de Aceptación):
- [ ] CA-1: Atención al Cliente NO ve salario en UI
- [ ] CA-2: Ejecutivos SÍ ven salario
- [ ] CA-3: Atención al Cliente NO ve salario en API
- [ ] CA-4: Atención al Cliente NO ve salario en reportes
- [ ] CA-5: Permission Set funciona correctamente

**Etiquetas**: 🔴 Seguridad y Permisos, 🟡 Alta Prioridad

**Asignar a**: Estudiantes 1-2 (DEV Admins)

**Mover a**: "To Do"

---

#### **Tarjeta 3: HU-003 (Múltiples Cuentas)**

**Título**: `[HU-003] Registrar Múltiples Cuentas Bancarias (8 pts)`

**Descripción**:
```
**Como** Ejecutivo de Créditos
**Quiero** registrar múltiples cuentas bancarias por cliente
**Para** tener opciones de desembolso

**Solución Técnica**:
- Objeto custom Bank_Account__c
- 7 campos (CBU encriptado, Is_Primary, etc.)
- Flow para auto-desmarcar cuenta primaria
- Formula Field en Contact

**Épica**: 🟢 Automatización
**Story Points**: 8
```

**Checklist** (Criterios de Aceptación):
- [ ] CA-1: Crear múltiples cuentas por cliente
- [ ] CA-2: Solo 1 cuenta primaria a la vez
- [ ] CA-3: CBU encriptado con Platform Encryption
- [ ] CA-4: Auto-desmarcar cuenta primaria (Flow)
- [ ] CA-5: Editar cuentas existentes
- [ ] CA-6: Inactivar cuentas (no eliminar)
- [ ] CA-7: Reporte de cuentas por banco

**Etiquetas**: 🟢 Automatización, 🟠 Media Prioridad

**Asignar a**: Estudiantes 1-2 (DEV Admins)

**Mover a**: "To Do"

---

**Referencia**: [Practica_Financiera/04-Guia_Trello_Paso_a_Paso.md](../Practica_Financiera/04-Guia_Trello_Paso_a_Paso.md) (Parte 3)

---

### **Semana 2 (12-16 Enero): Investigación**

**Acción en Trello**: Ninguna (las tarjetas siguen en "To Do")

**Acción en Gestor de Versiones**:
- Documentar investigaciones en [06-Investigaciones.md](06-Investigaciones.md)
- Documentar decisiones en [02-Salesforce_Consultant.md](02-Salesforce_Consultant.md)

---

### **Semana 3 (19-23 Enero): Desarrollo**

**Al empezar HU-001**:
1. Mover tarjeta HU-001 a "In Progress"
2. Asignarte la tarjeta
3. Agregar comentario: "Iniciando desarrollo - [Tu nombre]"

**Mientras desarrollas**:
- Documentar en [03-Salesforce_Admin.md](03-Salesforce_Admin.md)
- Actualizar comentarios en Trello con progreso diario

**Al terminar HU-001**:
1. Marcar algunos checklist items como completados
2. Mover tarjeta a "Testing"
3. Agregar comentario: "Listo para QA - deployed to QA"
4. Notificar a QA Admins (Estudiantes 3-4)

**Repetir para HU-002 y HU-003**

---

### **Semana 4 (26 Enero - 6 Febrero): Testing**

**Al empezar testing de HU-001**:
1. QA Admin se asigna la tarjeta
2. Agregar comentario: "Iniciando testing - [Nombre QA]"

**Durante testing**:
- Ejecutar test cases
- Documentar en [04-Tester_QA.md](04-Tester_QA.md)

**Si test PASS**:
1. Marcar TODOS los checklist items como completados ✅
2. Mover tarjeta a "QA Approved"
3. Agregar comentario: "Testing completo - 5/5 tests PASS"

**Si test FAIL**:
1. Mover tarjeta a "Blocked"
2. Agregar etiqueta roja "Bug"
3. Agregar comentario detallando qué falló
4. Notificar a DEV Admins

**Después de deployment a PROD**:
1. Mover tarjeta a "Done"
2. Agregar comentario: "Deployed to PROD - [Fecha]"

---

## 📋 Checklist de Integración

### **Configuración Inicial (Día 1)**
- [ ] Tablero Trello creado
- [ ] 8 columnas configuradas
- [ ] Etiquetas de Épicas creadas
- [ ] 9 miembros invitados
- [ ] 3 tarjetas de HU creadas
- [ ] Checklists de Criterios de Aceptación agregados

### **Durante el Sprint**
- [ ] Mover tarjetas según progreso
- [ ] Actualizar comentarios diariamente
- [ ] Marcar checklist items al completarlos
- [ ] Documentar en Gestor de Versiones paralelamente

### **Al Final del Sprint**
- [ ] Todas las tarjetas en "Done"
- [ ] Todos los checklist items marcados ✅
- [ ] Comentarios finales agregados
- [ ] Screenshots del tablero final guardados

---

## 💡 Mejores Prácticas

### **1. Sincronización Diaria**
- **Mañana**: Revisar Trello, ver qué hacer hoy
- **Tarde**: Actualizar Trello con progreso, documentar en Gestor de Versiones

### **2. Comentarios Útiles**
❌ **No hagas**: "Trabajando en esto"  
✅ **Haz**: "Creado campo Monthly_Salary__c, configurando FLS ahora"

### **3. Checklist Items**
- Marca items al completarlos, no todos al final
- Esto ayuda al equipo a ver progreso real

### **4. Etiquetas**
- Usa etiquetas de Épicas para filtrar tarjetas
- Usa etiqueta "Bug" para problemas

### **5. Asignaciones**
- Asígnate las tarjetas en las que trabajas
- Esto evita duplicación de trabajo

---

## 📊 Ejemplo de Ciclo Completo: HU-001

| Fecha | Acción en Trello | Acción en Gestor de Versiones |
|-------|------------------|-------------------------------|
| **5 Ene** | Crear tarjeta HU-001 en "To Do" | Documentar en [01-Business_Analyst.md](01-Business_Analyst.md) |
| **8 Ene** | (Tarjeta sigue en "To Do") | Investigar en [06-Investigaciones.md](06-Investigaciones.md) |
| **13 Ene** | (Tarjeta sigue en "To Do") | Decidir en [02-Salesforce_Consultant.md](02-Salesforce_Consultant.md) |
| **19 Ene** | Mover a "In Progress", asignar | Empezar [03-Salesforce_Admin.md](03-Salesforce_Admin.md) |
| **20 Ene** | Comentar progreso | Continuar documentando |
| **21 Ene** | Marcar 2/5 checklist items | Continuar documentando |
| **22 Ene** | Mover a "Testing", notificar QA | Finalizar documentación |
| **28 Ene** | QA se asigna, comenta inicio | Empezar [04-Tester_QA.md](04-Tester_QA.md) |
| **29 Ene** | Marcar 5/5 checklist items ✅ | Completar test cases |
| **30 Ene** | Mover a "QA Approved" | Documentar resultados |
| **5 Feb** | Mover a "Done", comentar deployment | Actualizar [14-DevOPS.md](14-DevOPS.md) |

---

## 🎯 Resumen

**Trello** y **Gestor de Versiones** son **complementarios**:

- **Trello**: Vista rápida del estado del proyecto (dashboard)
- **Gestor de Versiones**: Documentación detallada del trabajo (archivo histórico)

**Ambos son necesarios**:
- Trello para gestión diaria
- Gestor de Versiones para documentación profesional

**Referencias**:
- Historias de Usuario: [Practica_Financiera/03-Requerimientos_SOLUCION.md](../Practica_Financiera/03-Requerimientos_SOLUCION.md)
- Guía de Trello: [Practica_Financiera/04-Guia_Trello_Paso_a_Paso.md](../Practica_Financiera/04-Guia_Trello_Paso_a_Paso.md)
- Guía de Uso: [Gestor_de_Versiones/00-GUIA_DE_USO.md](00-GUIA_DE_USO.md)

---

**Última actualización**: 16 Enero 2026  
**Grupo**: 3 - VISIONARY ADMINS  
**Integrantes**: 9 estudiantes

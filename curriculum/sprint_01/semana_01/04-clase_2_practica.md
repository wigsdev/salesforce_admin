# Salesforce Admin - Práctica Clase 2

## 🎯 Incorporar ceremonias ágiles

**¿En qué vamos a trabajar hoy?**

Repasemos 2 roles importantes.

---

## Project Manager (PM)

> **"No es un Jefe, es un Facilitador y Escudo."**

### 1. Facilitador (Servant Leader)
Su trabajo no es dar órdenes, es asegurar que el equipo tenga todo para trabajar:
*   Accesos
*   Claridad en las tareas
*   Ambiente sin distracciones

### 2. Removedor de Bloqueos
Si un desarrollador dice "No tengo acceso al Sandbox", el PM es quien lo soluciona para que el Dev siga programando.

### 3. Guardián del Alcance
Protege al equipo de los cambios constantes del cliente durante el Sprint. "Si no está en el Sprint Backlog, queda para el próximo".

---

## Product Owner (PO)

> **La Voz del Cliente y Dueño del "Qué"**

1. ¿Quién es PO?
    - Es la persona que representa al Negocio (Ventas, Marketing, Atención al Cliente).
    - Su Misión: Maximizar el valor del producto (Salesforce). Se asegura de que el equipo esté trabajando en lo más importante.
    - La Diferencia Clave:
        - El Equipo decide CÓMO se construye (Técnico).
        - El PM facilita CUÁNDO y el ritmo (Proceso).
        - El PO decide QUÉ se construye (Negocio).

2. Responsabilidades Principales
    - Gestión del Product Backlog: Es el único que puede agregar, borrar o reordenar las tarjetas en la columna de "Backlog".
    - Priorización Implacable: Decide qué es urgente (Sprint 1) y qué puede esperar (Sprint 4).
    - Claridad en los Requerimientos: Explica el "Para qué" de una Historia de Usuario. Si el equipo tiene dudas sobre el negocio, preguntan al PO.
    - Juez Final (Aceptación): En la Demo, es quien dice "Aprobado" o "Rechazado". Si no cumple con lo que pidió, no pasa a Producción.

3. La Regla de Oro del PO
    "Lo que no aporta valor, se descarta." (El PO evita que el equipo pierda tiempo haciendo cosas bonitas pero inútiles).

---

## Ceremonias de la Metodología Ágil

### ¿Qué es la Metodología Ágil?

**Objetivo:** Entrega de Valor y Adaptabilidad
### Iterativo e Incremental (Sprints):
- No construimos todo de una sola vez. Trabajamos en ciclos cortos (1-2 semanas) llamados Sprints. Al final de cada ciclo, algo tiene que funcionar.
### Enfoque en Valor (Priorización):
- No hacemos lo más fácil primero, hacemos lo más valioso primero. Si el cliente necesita vender hoy, configuramos Ventas antes que Marketing.
### Adaptabilidad (Abrazar el Cambio):
- El plan no está escrito en piedra. Si el mercado cambia o el cliente cambia de opinión a mitad de camino, nosotros giramos el timón sin drama. El cambio es bienvenido, no un problema.

---

### 1. Daily (Reunión Diaria) - 10min

**Objetivo:** Alineación rápida. No es para resolver problemas técnicos.

#### Las 3 Preguntas Clave:
1. ¿Qué hice ayer para ayudar al Sprint?
2. ¿Qué haré hoy?
3. ¿Tengo algún bloqueo o impedimento? (Lo más importante).

**Regla:** Ser breve y al punto

---

### 2. Sprint Planning (El Compromiso) - 15min

**Objetivo:** Definir QUÉ vamos a entregar y CÓMO lo haremos.

**Acción:** El equipo mueve las tarjetas de "Backlog" a "Sprint Backlog" (Por Hacer).

**Compromiso:** Nadie impone tareas; el equipo decide cuántas historias de usuario es capaz de completar en este ciclo.

---

### 3. Sprint Review (Inspección) - 15min

**Objetivo:** Analizar el "Incremento de Producto" (lo que se construyó).

**Acción:** Se revisan las métricas y el cumplimiento de la "Definition of Done" (DoD).

**Pregunta:** ¿Cumplimos con el objetivo del Sprint? ¿Qué quedó pendiente?

---

### 4. DEMO (Show Time)

**Objetivo:** Mostrar funcionalidad real al Cliente (Stakeholders).\
**Regla de Oro:** "Prohibido PowerPoint".\
**Acción:** Se navega en Salesforce en vivo. Se muestra el Flujo funcionando, el Reporte creado o la Página diseñada.

**Feedback:** Es el momento donde el cliente dice "Me gusta" o "Esto no es lo que pedí".

---

### 5. Sprint Retrospective (Afilando el hacha)

**1. ¿Qué es la Retro?**
- Es una reunión **SOLO para el equipo** (Admins + PM). A veces el PO no participa para que el equipo hable con total libertad.
- **Objetivo:** Inspeccionar el **PROCESO** y las **RELACIONES**, no el producto. No hablamos de Salesforce, hablamos de cómo trabajamos juntos.
- **La Regla de las Vegas:** "Lo que se dice en la Retro, se queda en la Retro". Es un espacio seguro para ventilar frustraciones y proponer mejoras sin miedo a represalias.

Dinámica de la RETRO

**La Dinámica: Start - Stop - Continue (15 min)** El equipo responde 3 preguntas simples sobre el Sprint que terminó:
- 🟢 **Start (Empezar a hacer):** ¿Qué idea nueva deberíamos probar?
Ejemplo: "Empecemos a poner la etiqueta roja a los bugs urgentes".
- 🔴 **Stop (Dejar de hacer):** ¿Qué nos está frenando o molestando?
Ejemplo: "Dejemos de llegar 5 minutos tarde a la Daily".
- 🟡 **Continue (Seguir haciendo):** ¿Qué funcionó bien y debemos mantener?
Ejemplo: "El pair-programming (programar en parejas) para los Flows difíciles funcionó genial".

RESULTADOS DE LAS RETRO

**El Resultado: Action Items**
- De la queja se pasa a la acción.
- Se elige **1 mejora concreta** para aplicar en el próximo Sprint.
- Ejemplo: "Para el Sprint 2, todos actualizaremos el estado de las tarjetas en Trello antes de las 18:00 hs".

---

## ¡Manos a la obra!

## retro

- ¿Cómo nos fue? 
- ¿Qué cosas no quedaron claras y necesitamos repasar la próxima?

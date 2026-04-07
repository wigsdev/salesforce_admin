# Análisis BA — `S3_BA_Analisis.md`
**Sprint:** 3 — Campus Virtual (Experience Cloud)
**Fecha de análisis:** 2026-04-06
**Rol:** Business Analyst
**Fuente:** Comunicación directa de la Dra. Elena Vance (Rectora Lumina Tech)

---

## 1. Problema de Negocio Identificado

El canal de comunicación actual (teléfono + correo) es ineficiente y genera un cuello de botella operativo en dos personas clave:

- **Marta Gómez** (Secretaria General): recibe y gestiona todos los contactos externos e internos sin herramientas digitales.
- **Roberto Alonso** (Director Académico): responde manualmente las mismas preguntas frecuentes todos los días.

**Impacto:** Tiempo desperdiciado, riesgo de pérdida de prospectos, y baja satisfacción del alumno activo.

---

## 2. Requerimientos Funcionales

### REQ-01 — Identidad Visual del Portal
> *"Tiene que tener nuestro logo, el color Lumina Blue y el Tech Gold. Debe sentirse como Lumina Tech."*

- **Tipo:** No funcional (Branding)
- **Componente Salesforce:** Theme en Experience Builder
- **Estado:** ✅ **Sin gaps** — Colores confirmados en `Identidad_Colores_enunciado.md`:
  - 🔵 Lumina Blue: `#005A9C`
  - 🟡 Tech Gold: `#F2A900`
  - ⚪ Neutro/Fondo: `#F4F6F9`

---

### REQ-02 — Formulario Público de Captación de Interesados
> *"Un formulario simple de 'Solicitar Información'. Al completarlo, esos datos deben caer directamente en nuestro sistema para que Marta los contacte."*

- **Tipo:** Funcional
- **Actor:** Futuro alumno (visitante anónimo — sin cuenta en el sistema)
- **Objeto Salesforce destino:** `Lead`
- **Campos mínimos mencionados:** Nombre, Correo electrónico
- **Tipo de acceso:** Público (Guest User Profile)
- **Estado:** ⚠️ **Gap G2 abierto** — No se especifican campos adicionales (ej. Teléfono, Carrera de interés). Pendiente confirmar con Marta Gómez qué datos necesita para el seguimiento comercial.

---

### REQ-03 — Portal Privado para Alumnos Activos
> *"Alumnos que ya existen en nuestro sistema (como Lucas Martinez o Ana Vega) deberían poder iniciar sesión en este portal."*

- **Tipo:** Funcional
- **Actor:** Alumno activo (Contact con Rol__c = Alumno, ya existente en Salesforce)
- **Tipo de acceso:** Privado (requiere login — Community User)
- **Estado:** ✅ **Sin gaps críticos** — Se asume Customer Community User estándar. Los alumnos ya existen como Contacts en la org (Sprint 1/2).

---

### REQ-04 — Formulario de Reclamos y Trámites (Paso a Paso)
> *"Un formulario interactivo paso a paso donde el alumno pueda reportar un problema. Tiene que generarse un ticket de atención directamente en la bandeja de entrada de Administración."*

- **Tipo:** Funcional
- **Actor:** Alumno logueado en el portal
- **Objeto Salesforce destino:** `Case`
- **Ejemplos de casos:** "No veo mi nota de Algoritmos I" / "Quiero un certificado de alumno regular"
- **Receptor interno:** Administración (implica una Cola de Cases o usuario asignado — pendiente definir)
- **Estado:** ⚠️ **Gap G3 abierto** — No se definen las categorías/tipos de reclamo disponibles. Esto impacta el diseño del Screen Flow y el routing del Case.

---

### REQ-05 — Base de Artículos de Autogestión (FAQ)
> *"Biblioteca de Artículos dentro del portal. Al menos 3 artículos básicos."*

- **Tipo:** Funcional
- **Objeto Salesforce:** `Knowledge Article`
- **Contenido mínimo requerido (ejemplos citados):**
  1. ¿Cuándo son los finales?
  2. ¿Cómo justifico la asistencia?
  3. ¿Cuál es la escala de notas?
- **Estado:** ⚠️ **Gap G4 abierto** — No se especifica si los artículos son visibles para el público general o solo para alumnos logueados. Cambia la configuración de visibilidad en Knowledge y el componente en Experience Builder.

---

## 3. Stakeholders Identificados

| Stakeholder | Rol en el Portal | Tipo de Acceso |
|:---|:---|:---:|
| Dra. Elena Vance | Rectora / Tomadora de decisión | — |
| Marta Gómez | Secretaria General — recepciona Leads y Cases | Interno (Salesforce) |
| Roberto Alonso | Director Académico — referente de contenido para FAQ | Interno (Salesforce) |
| Futuro alumno | Visitante anónimo — completa formulario de captación | Público (Guest User) |
| Alumno activo (Lucas M., Ana V.) | Registra reclamos, consulta FAQ | Autenticado (Community User) |

---

## 4. Matriz de Gaps

| ID | Pregunta Abierta | Impacta | Quién responde |
|:---:|:---|:---|:---|
| G1 | Códigos HEX de los colores corporativos | REQ-01, Theme del portal | ✅ Cerrado — `#005A9C` / `#F2A900` / `#F4F6F9` |
| G2 | ¿Qué campos adicionales necesita Marta en el formulario de Lead? | REQ-02, Screen Flow público | Marta Gómez / TL |
| G3 | ¿Cuáles son las categorías de reclamos/trámites disponibles? | REQ-04, Screen Flow privado + routing de Cases | Roberto Alonso / TL |
| G4 | ¿Los artículos de Knowledge son visibles para el público o solo alumnos logueados? | REQ-05, visibilidad de Knowledge | Dra. Vance / TL |

---

## 5. Módulos Derivados para el Sprint

| Módulo | Requerimientos que cubre | Prioridad |
|:---|:---|:---:|
| **A — Portal Público (Vidriera)** | REQ-01, REQ-02 | 🔴 Alta |
| **B — Portal del Alumno (Mesa de Ayuda)** | REQ-03, REQ-04 | 🔴 Alta |
| **C — Base de Conocimiento (FAQ)** | REQ-05 | 🟡 Media |

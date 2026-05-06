# Análisis TL — `S3_TL_Indicaciones.md`
**Sprint:** 3 — Campus Virtual (Experience Cloud)
**Fecha de análisis:** 2026-04-06
**Rol:** Solution Architect / Salesforce Technical Consultant
**Fuente:** Hoja de Ruta Técnica del Tech Lead — Módulos + Sección OJO

---

## 1. Módulos Técnicos Definidos

### MÓD-01 — Captación de Futuros Alumnos (Guest User)

| Elemento | Especificación |
|:---|:---|
| **Plantilla del sitio** | Customer Service **o** Build Your Own |
| **Tipo de formulario** | Screen Flow en página pública |
| **Objeto destino** | `Lead` |
| **Perfil requerido** | Guest User Profile |
| **Riesgo principal** | Si el formulario no guarda → problema de permisos en Guest Profile, no del Flow |
| **Permisos críticos** | CRUD en `Lead` + acceso a ejecutar el Flow específico |

---

### MÓD-02 — Portal del Alumno (Authenticated Users)

| Elemento | Especificación |
|:---|:---|
| **Tipo de acceso** | Login requerido |
| **Habilitación de usuarios** | Contacts (Alumnos) → Customer Portal Users |
| **Tipo de formulario** | Screen Flow — generación de Cases |
| **Objeto destino** | `Case` |
| **Lógica clave** | Usar `{!$User.ContactId}` para asociar el Case al alumno logueado automáticamente — sin intervención manual del usuario |

---

### MÓD-03 — Base de Conocimiento (Knowledge)

| Elemento | Especificación |
|:---|:---|
| **Activación** | Manual en la Org + definir Data Categories |
| **Mínimo de artículos** | 3 artículos básicos |
| **Visibilidad crítica** | Marcar **"Visible in Public Knowledge Base"** o **"Visible to Customer"** |
| **Advertencia** | Sin marcar visibilidad, el artículo no aparece en el portal aunque esté publicado |
| **Implementación** | Componente estándar Knowledge en Experience Builder |

---

### MÓD-04 — Chat, Omnicanalidad y Bot (Superación de Expectativas)

| Elemento | Especificación |
|:---|:---|
| **Herramienta** | Embedded Service Deployment + Einstein Bots + Omni-Channel |
| **Estado TL inicial** | "Viable, pero laborioso" (Sugerido como fuera de alcance) |
| **Decisión Final** | **Implementado con éxito** como Bonus Track Avanzado |
| **Valor aportado** | Contención de Nivel 1 con IA (LuminaBot) y derivación inteligente a agente humano en Service Console |

---

## 2. Advertencias Técnicas Críticas (Sección OJO)

Requisitos previos que deben ejecutarse en orden — si se saltan, bloquean todo:

| # | Advertencia | Acción | Bloqueante |
|:---:|:---|:---|:---:|
| A1 | **Digital Experiences** no activado | `Setup → Digital Experiences → Enable` | 🔴 Sí |
| A2 | Licencias Developer Edition limitadas | Máximo 1-2 Community Users de prueba | 🟡 Limitante |
| A3 | Error en formulario público | Revisar `Guest User Profile → Object Permissions → Lead` — no tocar el Flow | 🔴 Condicional |
| A4 | Knowledge no aparece | `Setup → Users → [Tu usuario] → Knowledge User ✅` | 🔴 Sí |
| A5 | Chat requiere Omni-Channel completo | Se configuró exitosamente cola y presencia | 🟢 Resuelto |

---

## 3. Gaps Cerrados por este Documento

| ID | Gap | Resolución |
|:---:|:---|:---|
| G3 | Objeto destino del formulario de reclamos del alumno | ✅ `Case` — las categorías específicas siguen como decisión pendiente |
| G4 | Visibilidad de artículos de Knowledge | ✅ "Visible to Customer" (portal privado) + "Visible in Public Knowledge Base" (página pública) |
| G5 | "Soporte en tiempo real" | ✅ Implementado: Live Chat + Einstein Bot (LuminaBot) enrutado a Omni-Channel |

---

## 4. Aporte al Sprint

| Decisión | Estado |
|:---|:---:|
| Plantilla del sitio: Customer Service o Build Your Own | ✅ Definido |
| Formulario público → `Lead` via Guest User | ✅ Definido |
| Formulario privado → `Case` via `{!$User.ContactId}` | ✅ Definido |
| Knowledge: 3 artículos + visibilidad marcada | ✅ Definido |
| Chat / Omnicanalidad + IA (Bot) | ✅ Implementado con éxito (Bonus Track) |
| A1-A4: Pre-requisitos de configuración de la Org | ✅ Documentados como checklist de arranque |

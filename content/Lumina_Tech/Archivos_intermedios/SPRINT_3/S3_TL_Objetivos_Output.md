# Análisis TL — `S3_TL_Objetivos_Alcance.md`
**Sprint:** 3 — Campus Virtual (Experience Cloud)
**Fecha de análisis:** 2026-04-06
**Rol:** Solution Architect / Tech Lead Review
**Fuente:** Nota informativa del Tech Lead — Objetivos y Alcance del Sprint

---

## 1. Decisiones Técnicas Oficializadas

### DEC-01 — Herramienta Central: Experience Cloud
> *"Dejen de ver a Salesforce como una base de datos interna y lo transformen en un portal interactivo."*

- El TL **oficializa Experience Cloud** como la tecnología mandatoria del Sprint.
- **Impacto inmediato:** Requiere activar **Digital Experiences** en Setup como **paso cero** antes de cualquier otra configuración.

---

### DEC-02 — Tres Capacidades Obligatorias del Portal

| Capacidad requerida | Tecnología Salesforce |
|:---|:---|
| Exponer datos del CRM de forma segura | Experience Cloud + Perfiles y Permisos |
| Autoservicio mediante base de conocimiento | Salesforce Knowledge |
| Soporte en tiempo real | ⚠️ Ambiguo — pendiente definir (ver G5) |
| Identidad visual de marca | Experience Builder — Themes |

---

### DEC-03 — Caso de Uso Oficial para Lumina Tech
> *"Partner Central / Help Desk: Registro de leads por distribuidores o levantamiento de tickets técnicos."*

- **Nota:** Esta descripción usa terminología genérica (distribuidores, software). El contexto real de Lumina Tech es educativo.
- **Decisión de Arquitectura:** El requerimiento del BA (`S3_BA_Analisis.md`) prevalece sobre esta descripción genérica. El portal es para **prospectos y alumnos**, no distribuidores.

---

### DEC-04 — Arquitectura Mandatoria: Orden de Construcción de Screen Flows

El TL define un orden de ejecución obligatorio:

```
Paso 1 — Backend:   Diseñar y probar el Screen Flow en Salesforce puro.
Paso 2 — Seguridad: Definir audiencia (Público / Privado) y configurar permisos.
Paso 3 — Frontend:  Publicar en Experience Builder con el componente estándar "Flow".
```

**Alineación con requerimientos del BA:**

| Formulario | Audiencia | Perfil requerido | Objeto destino |
|:---|:---:|:---|:---:|
| Captación de interesados (REQ-02) | Público | Guest User Profile | `Lead` |
| Reclamos y Trámites (REQ-04) | Privado | Community User (Alumno) | `Case` |

---

## 2. Gaps / Observaciones Nuevas

| ID | Observación | Impacta | Estado |
|:---:|:---|:---|:---:|
| G5 | "Soporte en tiempo real" es ambiguo — ¿Chat (Embedded Service) o Cases con respuesta rápida? | Alcance del Sprint, estimación de esfuerzo | ⚠️ Abierto |
| G6 | Descripción de caso de uso (distribuidores/software) no coincide con el contexto universitario | Vocabulario del equipo — no es bloqueante, prevalece el BA | ✅ No bloqueante |

---

## 3. Aporte al Sprint

| Decisión | Origen | Estado |
|:---|:---:|:---:|
| Experience Cloud es la tecnología del Sprint | DEC-01 | ✅ Confirmado |
| Digital Experiences debe activarse como paso cero | DEC-01 | ✅ Requisito previo claro |
| Screen Flows son el patrón de formularios del portal | DEC-04 | ✅ Confirmado |
| Orden: Backend → Seguridad → Frontend | DEC-04 | ✅ Guía de construcción |
| "Soporte en tiempo real" requiere definición | DEC-02 | ⚠️ Pendiente G5 |

---

## 4. Relación con Otros Documentos

| Documento | Relación |
|:---|:---|
| `S3_BA_Analisis.md` | Este TL valida y oficializa lo pedido por el BA. El BA prevalece en caso de conflicto de terminología. |
| `S3_TL_Indicaciones.md` | Complementa — contiene los detalles técnicos y advertencias de implementación. |
| `S3_HU_Borrador.md` | DEC-04 define el patrón de construcción que se aplicará en cada HU de formulario. |

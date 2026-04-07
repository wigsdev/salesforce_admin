# Análisis Consolidado — Sprint 3
**Proyecto:** Lumina Tech University
**Sprint:** 3 — Campus Virtual (Experience Cloud)
**Fecha:** 2026-04-06
**Fuentes analizadas:**
- `S3_BA_Analisis.md` — Requerimientos del cliente (Rectora Vance)
- `S3_TL_Objetivos_Alcance.md` — Objetivos y alcance del Tech Lead
- `S3_TL_Indicaciones.md` — Hoja de ruta técnica + advertencias de la Org
- `S3_Documentacion.md` — Estándares de documentación del equipo

---

## 1. Problema de Negocio

El canal de comunicación actual de Lumina Tech (teléfono + correo) genera un cuello de botella operativo. Dos personas concentran toda la demanda:

- **Marta Gómez** (Secretaria General): gestiona todos los contactos externos sin herramientas digitales.
- **Roberto Alonso** (Director Académico): responde manualmente las mismas preguntas todos los días.

**Solución aprobada:** Construir el **Campus Virtual** de Lumina Tech usando **Experience Cloud**, transformando Salesforce en un portal interactivo accesible desde internet.

---

## 2. Alcance del Sprint

### En alcance ✅

| Módulo | Descripción |
|:---|:---|
| **A — Portal Público** | Sitio web con identidad Lumina Tech + formulario de captación de interesados (Leads) |
| **B — Portal del Alumno** | Portal privado con login para alumnos activos + formulario de reclamos/trámites (Cases) |
| **C — Base de Conocimiento** | Librería de artículos FAQ publicados en el portal (Knowledge) |

### Fuera de alcance ❌

| Elemento | Razón |
|:---|:---|
| Chat en tiempo real (Embedded Service) | Marcado por el TL como "laborioso" — no prioritario para este Sprint |

---

## 3. Decisiones de Arquitectura Confirmadas

| ID | Decisión | Fuente |
|:---:|:---|:---:|
| DEC-01 | **Experience Cloud** es la tecnología central del Sprint | TL |
| DEC-02 | **Digital Experiences** debe activarse en Setup como **paso cero** | TL |
| DEC-03 | **Screen Flows** son el patrón de formularios (Backend → Seguridad → Frontend) | TL |
| DEC-04 | Formulario público → objeto `Lead`, perfil **Guest User** | TL + BA |
| DEC-05 | Formulario privado → objeto `Case`, perfil **Community User (Alumno)** | TL + BA |
| DEC-06 | El Flow privado captura `{!$User.ContactId}` para asociar el Case automáticamente | TL |
| DEC-07 | Artículos Knowledge: marcar **"Visible to Customer"** o **"Visible in Public Knowledge Base"** | TL |
| DEC-08 | Plantilla del sitio: **Customer Service** o **Build Your Own** | TL |
| DEC-09 | Máximo 1-2 Community Users de prueba (límite de licencias Developer Edition) | TL |

---

## 4. Identidad Visual del Portal

| Token | HEX | Uso |
|:---|:---:|:---|
| **Lumina Blue** | `#005A9C` | Barra de navegación, botones principales |
| **Tech Gold** | `#F2A900` | Alertas, bordes, logo |
| **Neutro/Fondo** | `#F4F6F9` | Fondo general de lectura de datos |

*Fuente: `Identidad_Colores_enunciado.md`*

---

## 5. Stakeholders y Tipos de Acceso

| Stakeholder | Rol | Tipo de acceso al portal |
|:---|:---|:---:|
| Dra. Elena Vance | Rectora / Tomadora de decisión | — |
| Marta Gómez | Secretaria General — recepciona Leads y Cases | Interno (Salesforce) |
| Roberto Alonso | Director Académico — autor de contenido FAQ | Interno (Salesforce) |
| Futuro alumno | Visitante anónimo — completa formulario Lead | Público (Guest User) |
| Alumno activo (Lucas M., Ana V.) | Registra reclamos, consulta FAQ | Autenticado (Community User) |

---

## 6. Requerimientos Funcionales Consolidados

| ID | Requerimiento | Módulo | Objeto SF | Actor |
|:---:|:---|:---:|:---:|:---:|
| REQ-01 | Identidad visual: logo, Lumina Blue, Tech Gold | A | Theme | — |
| REQ-02 | Formulario público "Solicitar Información" → crea Lead | A | `Lead` | Futuro alumno |
| REQ-03 | Portal privado con login para alumnos activos | B | Community User | Alumno |
| REQ-04 | Formulario paso a paso de reclamos → crea Case | B | `Case` | Alumno logueado |
| REQ-05 | Biblioteca de artículos FAQ (mín. 3 artículos) | C | `Knowledge` | Alumno / Público |

---

## 7. Checklist de Pre-requisitos de la Org

Estos pasos deben completarse **antes de cualquier configuración** del Sprint:

- [ ] **A1** — Activar `Setup → Digital Experiences` (interruptor maestro)
- [ ] **A2** — Marcar `Setup → Users → [Tu usuario] → Knowledge User ✅`
- [ ] **A3** — Reservar máximo 2 licencias Customer Community para pruebas de login
- [ ] **A4** — Confirmar que los Contacts de Lucas M. y Ana V. existen en la Org

---

## 8. Gaps Pendientes al Inicio del Sprint

| ID | Gap | Impacta | Estado |
|:---:|:---|:---|:---:|
| G2 | ¿Qué campos adicionales necesita Marta en el formulario de Lead (además de Nombre y Correo)? | REQ-02 / Screen Flow público | ⚠️ Abierto |
| G3 | ¿Cuáles son las categorías/tipos de reclamo disponibles para el alumno? | REQ-04 / Screen Flow privado | ⚠️ Abierto |

> **Nota:** G2 y G3 se pueden resolver en paralelo durante la construcción. No son bloqueantes para iniciar — se pueden usar valores por defecto y refinar después.

---

## 9. Módulos → Historias de Usuario (Mapeo)

| Módulo | HUs previstas |
|:---|:---|
| **A — Portal Público** | HU-S3-01: Configurar sitio Experience Cloud con branding Lumina |
| | HU-S3-02: Screen Flow público para captación de Leads |
| **B — Portal del Alumno** | HU-S3-03: Habilitar alumnos como Community Users |
| | HU-S3-04: Screen Flow privado para generación de Cases |
| **C — Base de Conocimiento** | HU-S3-05: Activar Knowledge y publicar 3 artículos FAQ |

---

## 10. Orden de Ejecución Recomendado

```
DÍA 1 (HOY): Análisis completo + este documento consolidado ✅
DÍA 2:       Pre-requisitos de la Org (A1-A4) + Crear sitio EC + Branding
DÍA 3:       HU-S3-01 + HU-S3-02 (Módulo A — Portal Público)
DÍA 4:       HU-S3-03 + HU-S3-04 (Módulo B — Portal del Alumno)
DÍA 5:       HU-S3-05 (Módulo C — Knowledge + 3 artículos)
DÍA 6:       Testing end-to-end + Documentación en S3_Documentacion.md
```

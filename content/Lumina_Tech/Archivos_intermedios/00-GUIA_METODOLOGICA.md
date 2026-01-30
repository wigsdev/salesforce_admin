# 📘 Guía Metodológica: Proyecto Lumina Tech (Standard v2.0)
**Estado**: Actualizado post-consolidación de Sprint 1.
**Objetivo**: Estandarizar la documentación del ciclo de vida del proyecto (SDLC) alineado con la estructura final de carpetas.

---

## 🧭 Estructura del Proyecto (El "Nuevo Orden")

La documentación ya no está dispersa. Todo tiene su lugar:

1.  📂 **`Gestor_de_Versiones`** (La Biblia): Aquí vive la historia oficial.
    *   Archivos `00` a `14`.
    *   **Regla**: Solo se toca para agregar hitos completados o logs de ejecución.
    
2.  📂 **`Archivos_intermedios`** (El Archivo):
    *   Índices, borradores, enunciados y guías paso a paso.
    *   Si buscas un manual o el requerimiento original, busca aquí.

3.  📂 **`Tutoriales_por_Rol`** (Entrenamiento):
    *   Guías específicas para cada sombrero (Dev, Admin, QA).

---

## 🔄 El Ciclo de Vida "Lumina" (Daily Workflow)

Hemos adaptado el flujo semanal a un ritmo diario intenso para el MVP.

### 📅 Día 0: Estrategia y Roles (BA & PO)
*Objetivo: Entender el dolor de la Rectora Vance.*
1.  **Input**: `Archivos_intermedios/Enunciados_y_Requerimientos/SPRINT 1.md`.
2.  **Acción**: Traducir quejas en 11 Historias de Usuario.
3.  **Output**: `Gestor_de_Versiones/01-Business_Analyst.md`.

### 📅 Día 1: Cimientos de Datos (Consultant)
*Objetivo: Diseñar el ERD.*
1.  **Decisión**: Definir Junction Objects (Inscripción) y External IDs (DNI).
2.  **Output**: `Gestor_de_Versiones/02-Salesforce_Consultant.md`.

### 📅 Día 2 y 3: Construcción (Salesforce Admin)
*Objetivo: Configurar sin código.*
1.  **Acción**:
    *   Crear Objetos y Campos.
    *   Configurar Branding (`#005A9C`).
    *   Activar Reglas de Validación.
2.  **Log**: Registrar todo en `Gestor_de_Versiones/03-Salesforce_Admin.md` (Bitácora Diaria).

### 📅 Día 4: Seguridad y Validación (QA & Security)
*Objetivo: Zero Trust.*
1.  **Acción**:
    *   Configurar OWD Private.
    *   Testear "Sad Path" (intentar romperlo).
    *   Activar MFA.
2.  **Output**: `Gestor_de_Versiones/04-Tester_QA.md` y `14-DevOPS.md`.

---

## 🧩 Matriz de Responsabilidades (RACI) Actualizada

| Archivo "Vivo" | Responsable | Uso Principal |
|---|---|---|
| `Gestor_de_Versiones/*` | **Team Lead** | Fuente de verdad para auditoría. |
| `00-MASTER_INDEX` | Todos | Mapa de navegación (en Archivos Intermedios). |
| `HISTORIAS_DE_USUARIO` | PO / BA | Control de alcance y Sprint Backlog. |
| `Bitácoras (03/04)` | Admin / QA | Evidencia de trabajo diario. |

---

## 💡 Reglas de Oro para la Documentación

1.  **La Evidencia es Rey**:
    *   Si el QA probó un fallo, debe haber log en el archivo `04`.
    *   Si el Admin creó una App, debe estar listada en el archivo `03`.

2.  **Traza la Historia (Traceability)**:
    *   El Requisito (`01`) -> Se diseñó (`02`) -> Se construyó (`03`) -> Se probó (`04`).
    *   *Si falta un eslabón, la cadena se rompe.*

3.  **Higiene del Root**:
    *   No dejes archivos sueltos en `content/Lumina_Tech`.
    *   Si es borrador, va a `Archivos_intermedios`.
    *   Si es oficial, va a `Gestor_de_Versiones`.

---
**Siguiente Paso**: Revisa el `00-MASTER_INDEX.md` en Archivos Intermedios para navegar esta estructura. 🚀

# 🔗 Protocolo de Sincronización: Trello & Documentación (Sprint 1)
**Proyecto**: Lumina Tech  
**Objetivo**: Definir "Quién hace qué" y cómo se refleja en Trello siguiendo la **Estructura Estricta (8 columnas)**.

---

## 🚦 Reglas de Movimiento (Workflow Agresivo 4 Días)

El tablero no es un adorno. Es un radiador de información.

### 1. ➡️ Backlog / Sprint Backlog -> En Progreso
*   **Quién**: Admin / BA / PO.
*   **Acción**: El PO prioriza las **12 HUs** del Sprint 1.
*   **Condición**: Estás listo para configurar. (WIP Limit: 1 tarjeta por persona).

### 2. ➡️ En Progreso -> SF Desarrollo (Config)
*   **Quién**: Salesforce Admin.
*   **Acción**: Configuración en Sandbox (Objetos, Campos, App).
*   **Entregable (DoD Parcial)**: 
    - Actualizar [03-Salesforce_Admin.md](../Gestor_de_Versiones/03-Salesforce_Admin.md) con los pasos.
    - Subir Screenshot de la configuración a la tarjeta.

### 3. ➡️ SF Desarrollo -> DevOps - Dev (Checkpoint) 🚨
*   **Quién**: DevOps.
*   **Acción**: Backup del Sandbox y verificación de límites.
*   **Condición**: Si falla, vuelve a "En Progreso".

### 4. ➡️ DevOps - Dev -> SF QA (Testing Interno)
*   **Quién**: Admin (Self-Check) o Tester.
*   **Acción**: Ejecutar "Smoke Test" rápido.
*   **Notificación**: Mueves la tarjeta y alertas "@QA Listo para romper".

### 5. ➡️ SF QA -> DevOps - QA (Integración) 🚨
*   **Quién**: DevOps.
*   **Acción**: Migración a ambiente de QA (si existe) o preparación de datos de prueba.

### 6. ➡️ DevOps - QA -> Aprobación TL (Code Review)
*   **Quién**: QA Tester.
*   **Acción**: Ejecutar casos de prueba de [04-Tester_QA.md](../Gestor_de_Versiones/04-Tester_QA.md).
    - ✅ **Pasa**: Adjunta evidencia y mueve a "Aprobación TL".
    - ❌ **Falla**: Crea etiqueta 🐞 BUG y bloquea la tarjeta.

### 7. ➡️ Aprobación TL -> DevOps - Prod (Staging) 🚨
*   **Quién**: Team Lead.
*   **Acción**: Validar estándares (Naming Conventions).
*   **Condición**: Si aprueba, autoriza al Release Manager.

### 8. ➡️ DevOps - Prod -> SF Producción (Deploy)
*   **Quién**: Release Manager / DevOps.
*   **Acción**: Ejecutar Change Set o Metadata Deploy a PROD.
*   **Validación**: Smoke Test en vivo ([13-Ambiente_PROD.md](../Gestor_de_Versiones/13-Ambiente_PROD.md)).

### 9. ➡️ SF Producción -> Terminado (Closed)
*   **Quién**: PO.
*   **Acción**: Aceptación final. La tarjeta muere aquí.

---

## 🏷️ Estándar de Etiquetas (Taxonomía Sprint 1)

Alineado con [Guia_Trello_Paso_a_Paso.md](00-Guia_Trello_Paso_a_Paso.md) (Usamos cuadrados para evitar errores de visualización):

| Color | Etiqueta | Significado | Días |
|---|---|---|---|
| 🔵 | **Modelado / Académico** | Core (Objetos, ERD). | Día 1 |
| 🟢 | **Branding / UI** | Look & Feel, Apps. | Día 2 |
| 🟣 | **Data Quality** | Validaciones, Regex. | Día 3 |
| 🔴 | **Seguridad** | OWD, Perfiles, MFA. | Día 4 |
| 🐞 | **BUG** | Error crítico en construcción. | - |

---

## 📋 Definition of Done (DoD) Global
Una tarjeta **NO** cruza a "Terminado" hasta que:

1.  [ ] **Configuración**: Funciona en el ambiente objetivo.
2.  **Evidencia**: Screenshot adjunta en Trello.
3.  **Documentación**: [03-Admin](../Gestor_de_Versiones/03-Salesforce_Admin.md) actualizado (Qué se hizo).
4.  **Calidad**: [04-QA](../Gestor_de_Versiones/04-Tester_QA.md) actualizado (Qué se probó).
5.  **Aceptación**: El PO dijo "Sí".

> **Nota**: Si falta un paso, la tarjeta vuelve atrás. Sin piedad.

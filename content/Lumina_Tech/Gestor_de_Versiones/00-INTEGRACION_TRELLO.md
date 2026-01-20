# 🔗 Protocolo de Sincronización: Trello & Documentación
**Proyecto**: Lumina Tech  
**Objetivo**: Definir "Quién hace qué" y cómo se refleja en Trello.

---

## 🚦 Reglas de Movimiento (Workflow)

Solo se puede mover una tarjeta si se cumple la condición de entrada.

### 1. ➡️ Backlog -> Sprint Backlog
*   **Quién**: Product Owner / Team Lead.
*   **Condición**: La Historia de Usuario (HU) tiene Criterios de Aceptación claros en `HISTORIAS_DE_USUARIO.md`.

### 2. ➡️ Sprint Backlog -> En Progreso (Doing)
*   **Quién**: Salesforce Admin / Developer.
*   **Condición**: 
    1.  Te asignas la tarjeta ("Join Card").
    2.  Verificas que no tienes más de 2 tarjetas activas (WIP Limit).

### 3. ➡️ En Progreso -> SF Desarrollo (Unit Testing)
*   **Quién**: Salesforce Admin / Developer.
*   **Acción**: Configuras la solución en Sandbox.
*   **Entregable Obligatorio**: 
    - Actualizar `03-Salesforce_Admin.md` con los pasos realizados.
    - Subir Screenshot de configuración a la tarjeta.

### 4. ➡️ SF Desarrollo -> SF QA (Testing)
*   **Quién**: Salesforce Admin.
*   **Condición**: Has verificado tu propio trabajo (Self-QA).
*   **Notificación**: Mencionas al Tester en un comentario ("@QA Listo para revisión").

### 5. ➡️ SF QA -> Aprobación TL (Review)
*   **Quién**: Tester QA.
*   **Acción**: Ejecutar casos de prueba de `04-Tester_QA.md`.
    - ✅ **Pasa**: Adjunta evidencia de éxito y mueve a "Aprobación TL".
    - ❌ **Falla**: Mueve a "Blocked" y comenta el Bug.

### 6. ➡️ Aprobación TL -> Terminado (Done)
*   **Quién**: Team Lead / Release Manager.
*   **Condición**: 
    - El código cumple estándares (Naming Conventions).
    - La documentación está al día.
    - Listo para Deploy (`14-DevOPS.md`).

---

## 🏷️ Estándar de Etiquetas (Taxonomía)

| Color | Etiqueta | Significado |
|---|---|---|
| 🔴 | **Seguridad** | Afecta perfiles, roles o visibilidad (Prioridad Alta). |
| 🔵 | **Académico** | Funcionalidad core (Materias, Cursadas). |
| 🟢 | **Calidad de Datos** | Validaciones (DNI, Email). |
| 🟣 | **Documentación** | Tareas de escritura técnica. |
| 🐞 | **BUG** | Error detectado en QA que detiene el flujo. |

---

## 📋 Definition of Done (DoD) Global
Una tarjeta **NO** está terminada hasta que:
1.  [ ] Configuración funcional en Sandbox.
2.  [ ] Screenshot de evidencia en Trello.
3.  [ ] Documento `03-Admin` actualizado.
4.  [ ] Documento `04-QA` validado.

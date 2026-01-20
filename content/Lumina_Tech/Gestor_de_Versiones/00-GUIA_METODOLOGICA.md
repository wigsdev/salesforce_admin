# 📘 Guía Metodológica: Proyecto Lumina Tech
**Rol**: Líder de Metodología / Documentation Manager
**Objetivo**: Estandarizar la documentación del ciclo de vida del proyecto (SDLC).

---

## 🧭 Tu Mapa de Ruta (Ciclo de Vida)

Este proyecto no es solo "hacer click". Es **documentar valor**.
Sigue este flujo cronológico para asegurar que tu simulación sea realista.

### 📅 Semana 1: El Diagnóstico (Role: Business Analyst)
*Objetivo: Entender el dolor de la Rectora Vance.*

1.  **Input**: Lee `SPRINT 1.md` (Tu contrato).
2.  **Acción**: Traduce "quejas" en **Requerimientos**.
3.  **Output**: `01-Business_Analyst.md`.
    *   *Ejemplo*: Si ella dice "no quiero líos legales", tú escribes "REQ-002: Field Level Security para Notas".
4.  **Trello**: Crea las tarjetas (`HU-00X`) en la columna **Backlog**.

### 📅 Semana 2: La Arquitectura (Role: Consultant)
*Objetivo: Diseñar antes de construir.*

1.  **Input**: Los Requerimientos de la Semana 1.
2.  **Investigación (`06-Investigaciones.md`)**:
    *   ¿Cómo conecto Alumnos y Materias?
    *   *Opción A*: Lookup directa (Mal).
    *   *Opción B*: Junction Object (Bien - Escalable).
3.  **Consulta (`05-Preguntas_y_Dudas.md`)**:
    *   "¿Rectora, necesitamos historial de recursantes?" -> "Sí".
4.  **Output**: `02-Salesforce_Consultant.md` (Tus planos de obra).

### 📅 Semana 3: La Construcción (Role: Admin)
*Objetivo: Configurar sin romper nada.*

1.  **Input**: El diseño técnico (`02`).
2.  **Acción (Trello)**: Mueve tarjeta a **En Progreso**.
3.  **Configuración**:
    *   Crea Objetos (`Carrera`, `Materia`).
    *   Configura Reglas (`Nota 1-10`).
4.  **Output**: `03-Salesforce_Admin.md`.
    *   ⚠️ **Obligatorio**: Captura de pantalla de cada Regla de Validación y Schema Builder.

### 📅 Semana 4: La Validación (Role: QA Tester)
*Objetivo: Destruir (constructivamente) el trabajo del Admin.*

1.  **Input**: La configuración terminada.
2.  **Acción (Trello)**: Mueve tarjeta a **SF QA**.
3.  **Testing**:
    *   Intenta poner nota "11".
    *   Intenta guardar email "juan,perez".
4.  **Output**: `04-Tester_QA.md`.
    *   Si pasa: ✅ Approved.
    *   Si falla: 🐞 Bug Report (Mover a Blocked).

---

## 🧩 Matriz de Responsabilidades (RACI)

| Archivo | Responsable | Cuándo se toca |
|---|---|---|
| `SPRINT 1.md` | Scrum Master | Al inicio (Lectura) y final (Review). |
| `01-BA` | Business Analyst | Semana 1 (Definición inmutable). |
| `02-Consultant` | Arquitecto | Semana 2 (Diseño). |
| `03-Admin` | Implementador | Semana 3 (Día a día). |
| `04-QA` | Tester | Semana 4 (Validación). |
| `00-Trello` | **TODOS** | **DIARIAMENTE**. |

---

## 💡 Reglas de Oro para Lumina Tech

1.  **La Evidencia es Rey**: Si configuraste el bloqueo de notas, **muestra** el mensaje de error. Si no hay foto, no sucedió.
2.  **Traza la Historia**:
    *   La Rectora pidió privacidad (`01`) ->
    *   El Arquitecto diseñó OWD Privado (`02`) ->
    *   El Admin configuró Sharing Rules (`03`) ->
    *   El Tester verificó que el Profe A no vea al Alumno B (`04`).
    *   *¡Eso es trazabilidad!*

---
**Siguiente Paso**: Abre `00-INTEGRACION_TRELLO.md` y empieza a mover tus tarjetas. 🚀

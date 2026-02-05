# 🏗️ Consultant - Arquitectura y Solución
**Proyecto**: Lumina Tech
**Sprint**: 01 (Fundamentos)

---

## 📅 DIA 0 - Estrategia de Arquitectura

### Decisiones de Diseño (ADR)
**Fuente**: [Tarea 3 - Generar preguntas](../Bitacoras_Sprint_1/dia_0/3_Generar_preguntas_en_el_documento_para_evacuar_dudas.md)

1.  **ADR-001: Duplicación de Materias para MVP**
    *   *Contexto*: Compartir registros de "Subject" complicaría las Sharing Rules Private.
    *   *Decisión*: Crear registros separados `Math 1 - ENG` y `Math 1 - ADM`.
    *   *Justificación*: Simplifica la seguridad (OWD Private) en la fase 1.

2.  **ADR-002: Modelo de Inscripción (Junction)**
    *   *Contexto*: Necesidad de historial de recursantes y notas.
    *   *Decisión*: Objeto personalizado `Enrollment` que une `Student` + `Subject` + `Cycle`.

3.  **ADR-003: Calidad de Datos en Origen**
    *   *Decisión*: Uso de tipos de datos estrictos (Auto-Number, Number(4,2)) y reglas de validación.

---

## 📅 DIA 1 - Diseño Técnico (ERD)
**Estado**: ✅ Definido y Validado.

### Diagrama de Relación de Entidades
Este esquema responde a **[REQ-DATA-002] Historial Académico**.

> **[Ver Diagrama Visual Renderizado (Mermaid)](../Bitacoras_Sprint_1/dia_1/2_Relacion_entre_Objetos.md)**

### Especificación de Relaciones
1.  **Enrollment (Junction Object)**:
    *   Actúa como tabla puente para manejar la relación **M:N** entre `Student` y `Subject`.
    *   *Configuración*: Master-Detail (x2). Si eliminas al `Student`, se borra su historial.

2.  **Jerarquía de Career**:
    *   `Subject` tiene una relación Lookup hacia `Career`.
    *   *Nota*: Permite flexibilidad si una materia cambia de plan de estudios (Loosely coupled).

3.  **Evaluación Continua**:
    *   `Exam` es hijo (Child) de `Enrollment`.
    *   *Propósito*: Permite calcular promedios directamente en la inscripción usando Roll-Up Summaries.

---

## 📅 DIA 2 - Identidad Visual y App
**Fuente**: [Identidad_Colores.md](../Archivos_intermedios/Enunciados_y_Requerimientos/Identidad_Colores.md)

### Estrategia de Branding
Para evitar la apariencia "genérica" de Salesforce y fomentar la adopción de los docentes:

*   **Paleta Académica**:
    *   `#005A9C` (Lumina Blue): Confianza. Usado en Headers.
    *   `#F2A900` (Tech Gold): Excelencia. Usado en Acentos.
    *   `#F3F3F3` (Soft Grey): Usabilidad. Fondo para reducir fatiga visual.
*   **Logo**: Isotipo de libro abierto con haces de luz (conocimiento).

---

## 📅 DIA 3 - Consistencia de Datos
**Fuente**: [03-Salesforce_Admin.md](03-Salesforce_Admin.md)

### Estrategia de Calidad
1.  **Validación en Capa de Datos**: Reglas de validación (VR) implementadas para `Email__c` y `Final_Grade__c`.
2.  **Denormalización Visual**: Uso de Formula Fields (`Subject_Display__c`) para mejorar reportes sin código.

---

## 📅 DIA 4 - Arquitectura de Seguridad
**Fuente**: [03-Salesforce_Admin.md](03-Salesforce_Admin.md)

### Modelo de Seguridad (Layered Security)
1.  **OWD (Organization-Wide Defaults)**: `Private` para `Student`. (Base restrictiva).
2.  **Permission Set Groups vs Profiles**:
    *   **Decisión**: Usar "Minimum Access - Salesforce" como perfil base y sumar capacidades vía PSG.
    *   *Beneficio*: Mayor flexibilidad y menor deuda técnica.
3.  **FLS (Field Level Security)**:
    *   Protección a nivel atributo. `Final_Grade__c` es Read-Only para administrativos.

# 📖 Backlog de Historias de Usuario: Refactorización y Mejoras

**Proyecto**: Universidad Lumina Tech
**Sprint**: 02 y 03 (Refactorización Arquitectónica y UX)
**Enfoque**: Deuda Técnica, Escalabilidad y Alineación con `Solicitud.md`.

> **⚠️ Contexto de este Documento**
> Este archivo detalla las historias de usuario (HU-013 en adelante) que justifican las decisiones técnicas aplicadas en la **"Parte 2" (To-Be)** de los manuales de implementación. No modifica las historias de la línea base del Sprint 1, sino que documenta su refactorización.

---

## 📅 SPRINT 2: Refactorización Arquitectónica
*Objetivo: Solucionar límites técnicos de Salesforce (Junction Objects) e incorporar los módulos omitidos en el MVP.*

### HU-013: Módulo de Tesorería Integrada (Cobros)
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Crítica
*   **Origen**: Solicitud de Rectora ("equipo de Administración... cobran las cuotas").
*   **Descripción**:
    > **Como** Personal de Administración,
    > **Quiero** registrar los pagos de cuotas y auditar morosidad,
    > **Para** gestionar financieramente a la institución.
*   **⚙️ Pasos de Implementación (Refactorización - Guía 07)**:
    - [x] 1. Crear Custom Object: **Cobro** (`Cobro__c`).
    - [x] 2. Configurar Relación **Master-Detail** fuerte apuntando hacia el objeto estándar **`Contact`** (Alumno).
    - [x] 3. Habilitar **Roll-Up Summary** en `Contact` llamado `Total_Deuda_Vencida__c` que sume los Cobros en estado "Pendiente".
    - [x] 4. Configurar **FLS** y **Object Settings** para que los Profesores NO tengan acceso de lectura a este objeto (Privacidad financiera).

### HU-014: Escalabilidad del Core (Bypass Límite Junction)
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Crack (Bloqueante Técnico)
*   **Origen**: Límite técnico de Salesforce (Un Junction Object no puede ser Master de terceros).
*   **Descripción**:
    > **Como** Arquitecto del Sistema,
    > **Quiero** transformar las relaciones de los objetos transaccionales a Lookups obligatorios,
    > **Para** evitar el colapso del esquema cuando queramos agregar registros de notas o faltas a la Inscripción.
*   **⚙️ Pasos de Implementación (Refactorización - Guías 05 y 12)**:
    - [x] 1. Modificar Objeto **`Asistencia__c`**: Cambiar relación a la `Inscripcion__c` de Master-Detail a **Lookup (Required)**.
    - [x] 2. Modificar Objeto **`Evaluacion__c`** (ex-Nota): Cambiar relación de Master-Detail a **Lookup (Required)**.
    - [x] 3. Ajustar el OWD (Sharing Settings) de ambos objetos a **Private** de forma manual para asegurar la matriz de visibilidad de la HU-010.

---

## 📅 SPRINT 3: Mejoras UX y Automatización Lógica
*Objetivo: Optimizar el tiempo del usuario (Profesores) mediante interfaces de carga masiva y automatizar el reglamento académico.*

### HU-015: Planilla de Asistencia Masiva
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Origen**: Mejora operativa (Evitar carga 1 a 1).
*   **Descripción**:
    > **Como** Profesor,
    > **Quiero** crear un solo registro para la clase de hoy y que el sistema despliegue mi lista de alumnos,
    > **Para** tomar asistencia con solo dos clics por alumno.
*   **⚙️ Pasos de Implementación (Refactorización - Guía 13)**:
    - [x] 1. Crear Objeto Header: **Sesión de Clase** (`Sesion_de_Clase__c`). Master-Detail a Materia.
    - [x] 2. Conectar el registro `Asistencia__c` a esta Sesión (Master-Detail).
    - [x] 3. Crear **Record-Triggered Flow** (After Save) en la Sesión de Clase que obtenga todos los inscriptos de la materia y genere las Asistencias pre-rellenadas en "Presente".

### HU-016: Actas de Examen Automáticas
*   **Estimación**: 🔴 **5 SP**
*   **Prioridad**: Alta
*   **Origen**: Mejora operativa (Planillas de calificación).
*   **Descripción**:
    > **Como** Profesor,
    > **Quiero** crear una única "Acta de Examen" que herede su peso porcentual a todos mis alumnos,
    > **Para** cargar todas las calificaciones rápidamente usando Inline Editing.
*   **⚙️ Pasos de Implementación (Refactorización - Guía 15)**:
    - [x] 1. Crear Objeto Header: **Instancia de Evaluación** (`Instancia_Evaluacion__c`). Master-Detail a Materia.
    - [x] 2. Conectar el registro `Evaluacion__c` a esta Instancia (Master-Detail).
    - [x] 3. Crear **Record-Triggered Flow** (After Save) que obtenga a los inscriptos y cree las Evaluaciones en blanco, asignándoles el `Tipo` y `Peso` de la Instancia padre.

### HU-017: Motor Estricto de Correlatividades
*   **Estimación**: 🟡 **3 SP**
*   **Prioridad**: Media
*   **Origen**: Solicitud de Rectora (Control lógico de trayectorias).
*   **Descripción**:
    > **Como** Administrativo,
    > **Quiero** que el sistema bloquee automáticamente cualquier inscripción que no cumpla los prerrequisitos,
    > **Para** evitar violaciones al reglamento académico.
*   **⚙️ Pasos de Implementación (Refactorización - Guía 14)**:
    - [x] 1. Crear Objeto **Correlativa** (`Correlativa__c`). Master-Detail hacia `Materia_Destino`, Lookup hacia `Materia_Requisito`.
    - [x] 2. Desarrollar **Before-Save Flow** en `Inscripcion__c` que busque el historial del `Contact`.
    - [x] 3. Configurar elemento **Custom Error** para detener la transacción y notificar qué materia falta.

### HU-018: Aplicación de Identidad Institucional
*   **Estimación**: 🟢 **1 SP**
*   **Prioridad**: Alta
*   **Origen**: Documento `Identidad_Colores_enunciado.md`.
*   **Descripción**:
    > **Como** Rectora,
    > **Quiero** que la aplicación refleje fielmente los colores institucionales para generar pertenencia,
    > **Para** que la comunidad educativa no sienta que usa una base de datos estándar.
*   **⚙️ Pasos de Implementación (Refactorización - Guía 08 y Setup)**:
    - [x] 1. Renombrar la Lightning App a **"Gestión Académica Lumina"**.
    - [x] 2. Configurar el menú estricto: Contactos, Carreras, Materias, Inscripciones, Asistencias, Evaluaciones, Cobros.
    - [x] 3. Aplicar Paleta en Themes & Branding:
        *   **Primario (Brand Color)**: `#005A9C` (Lumina Blue)
        *   **Secundario (Highlight/Page Background)**: `#F2A900` (Tech Gold)
        *   **Fondo Neutro**: `#F4F6F9`
    - [x] 4. Incorporar logo conceptual de institución educativa moderna.

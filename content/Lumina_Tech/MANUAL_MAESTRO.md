# 🦅 MANUAL MAESTRO DE EJECUCIÓN INTEGRAL: Proyecto Lumina Tech

**Rol**: Project Manager & Scrum Master  
**Proyecto**: Implementación Salesforce - Universidad Lumina Tech  
**Versión**: 3.1 (Links Activos)

---

## 🎯 Objetivo
Este manual es la "Biblia" del equipo. Cubre desde que te unes al proyecto hasta que entregas la funcionalidad terminada en producción.

---

## 📚 FASE 0: Tu Armería (Recursos Obligatorios)
*Antes de mover un dedo, equípate.*

### 1. Conoce tu Rol (Tutoriales Personales)
No intentes hacer todo. Lee tu guía específica para saber qué se espera de ti:
*   📂 [Tutoriales por Rol](Tutoriales_por_Rol/)
    *   🛡️ **Admin**: [Leer Guía](Tutoriales_por_Rol/05-Rol_Salesforce_Admin.md)
    *   🕵️ **BA**: [Leer Guía](Tutoriales_por_Rol/01-Rol_Business_Analyst.md)
    *   🧪 **QA**: [Leer Guía](Tutoriales_por_Rol/03-Rol_QA_Tester.md)
    *   *(Busca el tuyo en la carpeta)*

### 2. Guías de Implementación Técnica
Cuando te toque configurar Salesforce, **NO adivines**. Sigue los tutoriales paso-a-paso:
*   📂 [Guías Técnicas](Guias_Implementacion/)
    *   *Ejemplo*: Si estás creando el Objeto "Carrera", abre `01-Tutorial_Carrera.md`.

---

## 🌊 FASE 1: El Flujo de Trabajo (The Trello Lifecycle)
*Así movemos las tareas desde "Idea" hasta "Realidad".*

### 1. 📋 Backlog (Planning)
*   **Quién**: Product Owner / BA.
*   **Qué sucede**: Las tareas del "Checklist Diario" (ver abajo) se convierten en tarjetas de Trello.
*   *Condición de Salida*: La tarjeta tiene Título y Descripción clara.

### 2. 🏗️ En Progreso (Development)
*   **Quién**: Salesforce Admin / Consultant.
*   **Acción**:
    1.  Toma la tarjeta y muévela a "En Progreso".
    2.  **Consulta la Guía de Implementación** correspondiente (enlazada abajo).
    3.  Construye la solución en tu **Sandbox (Entorno Dev)**.

### 3. 🧪 QA / Testing (Validación)
*   **Quién**: QA Tester.
*   **Acción**:
    1.  Lee los "Criterios de Aceptación" en la tarjeta.
    2.  Intenta "romper" lo que construyó el Admin.
    3.  Si falla -> Vuelve a "En Progreso". Si pasa -> Mover a "Aprobado".

### 4. ✅ Terminado (Deployment)
*   **Quién**: Release Manager.
*   **Acción**: Registra la tarea en el **Gestor de Versiones** y despliega a Producción.

---

## 📅 FASE 2: Cronograma de Ejecución (Sprint 1)

Sigue este orden. Cada día desbloquea el siguiente. Haz clic en "Recurso Clave" para ver cómo hacerlo.

### Día 0: Análisis y Seteo Inicial 🏁
*   **Foco**: Entender el negocio.
*   **Recurso Clave**: [Tutorial BA](Tutoriales_por_Rol/01-Rol_Business_Analyst.md).
*   **Tareas**:
    1.  [Leer caso de negocio](dia_0/1_Leer_juntos_y_conocer_la_Empresa.md)
    2.  [Definir Roles](dia_0/2_Definir_Roles.md)

### Día 1: Arquitectura de Datos 🏛️
*   **Foco**: Crear Objetos y Relaciones.
*   **Recursos Claves**: 
    *   [01-Tutorial_Carrera.md](Guias_Implementacion/01-Tutorial_Carrera.md)
    *   [02-Tutorial_Materia.md](Guias_Implementacion/02-Tutorial_Materia.md)
*   **Tareas**:
    1.  [Crear Objetos Custom](dia_1/1_Creacion_de_objetos_Custom_Standard.md)
    2.  [Relacionar Objetos](dia_1/2_Relacion_entre_Objetos.md)
    3.  **Acción Trello**: Crear tarjetas para "Objeto Carrera", "Objeto Materia".

### Día 2: Branding y UI 🎨
*   **Foco**: Look & Feel.
*   **Recurso Clave**: [07-Tutorial_App_Builder.md](Guias_Implementacion/07-Tutorial_App_Builder.md).
*   **Tareas**:
    1.  [Configurar Dominio y Logo](dia_2/2_Lograr_hacer_el_dominio_personalizado.md).
    2.  **Acción Trello**: Crear tarjeta "Configurar Tema Visual".

### Día 3: Lógica y Calidad 🧠
*   **Foco**: Validaciones y Automatización.
*   **Recurso Clave**: [05-Tutorial_Validaciones.md](Guias_Implementacion/05-Tutorial_Validaciones.md).
*   **Tareas**:
    1.  [Crear Reglas de Validación](dia_3/2_Reglas_de_validacion_y_campos_formula.md).
    2.  [Crear Fórmulas](dia_3/1_Campos_adicionales.md).
    3.  **Acción Trello**: Mover tarjeta a QA para testear validaciones.

### Día 4: Seguridad Blindada 🛡️
*   **Foco**: Permisos.
*   **Recurso Clave**: [06-Tutorial_Seguridad.md](Guias_Implementacion/06-Tutorial_Seguridad.md).
*   **Tareas**:
    1.  [Configurar Permission Sets](dia_4/1_Configuracion_Permission_Sets.md).
    2.  [Definir OWD (Sharing)](dia_4/3_Visibilidad_Objetos_Campos.md).

---

> **Mantra del Equipo**: "Si no está en Trello, no existe. Si no seguiste la Guía de Implementación, probablemente habrá que rehacerlo."

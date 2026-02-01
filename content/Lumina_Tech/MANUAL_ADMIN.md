# 🛡️ Manual de Ejecución: Salesforce Admin

**Tu Misión**: Construir. Eres el dueño de las columnas **3. En Progreso** y **4. SF Desarrollo**.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **2. Sprint Backlog** | Tomas trabajo aprobado por el PO. |
| 🔨 **BUILD** | **3. En Progreso** | Configuración activa en Sandbox. |
| 👋 **HANDOFF** | **4. SF Desarrollo** | Terminado en Sandbox. Listo para QA. |

---

## 📚 Tu Arsenal Técnico (Todas las Guías)
*Ten estas a mano. Son tu "Cómo se hace".*

*   **Objetos y Datos**:
    *   [01-Tutorial_Carrera.md](../Guias_Implementacion/01-Tutorial_Carrera.md)
    *   [02-Tutorial_Materia.md](../Guias_Implementacion/02-Tutorial_Materia.md)
    *   [03-Tutorial_Alumno.md](../Guias_Implementacion/03-Tutorial_Alumno.md)
    *   [04-Tutorial_Inscripcion.md](../Guias_Implementacion/04-Tutorial_Inscripcion.md)
    *   [09-Tutorial_Schema_Builder.md](../Guias_Implementacion/09-Tutorial_Schema_Builder.md)
*   **Lógica y Calidad**:
    *   [05-Tutorial_Validaciones.md](../Guias_Implementacion/05-Tutorial_Validaciones.md)
    *   [05b-Tutorial_Campos_Formula.md](../Guias_Implementacion/05b-Tutorial_Campos_Formula.md)
*   **Seguridad**:
    *   [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md)
*   **Visual**:
    *   [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md)

---

## 📅 CRONOGRAMA DE EJECUCIÓN (Sprint 1)

### Día 1: Objetos y Estructura
1.  **Modelo de Datos**
    *   **Contexto**: Crear los cimientos de la app.
    *   🔨 **Ejecución**:
        *   Crea `Carrera` usando [Guía 01](../Guias_Implementacion/01-Tutorial_Carrera.md).
        *   Crea `Materia` usando [Guía 02](../Guias_Implementacion/02-Tutorial_Materia.md).
        *   Crea `Alumno` usando [Guía 03](../Guias_Implementacion/03-Tutorial_Alumno.md).
    *   👋 **Handover**: Mueve a **4. SF Desarrollo** y avisa a QA.

### Día 2: Branding y UI
1.  **Configuración Visual**
    *   **Contexto**: Que se vea corporativo.
    *   🔨 **Ejecución**: Configura temas y logos.
    *   📘 **Guía**: [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md).

### Día 3: Reglas y Automatización
1.  **Blindar la App**
    *   **Contexto**: Evitar datos basura.
    *   🔨 **Ejecución**:
        *   Reglas de Validación: [Guía 05](../Guias_Implementacion/05-Tutorial_Validaciones.md).
        *   Fórmulas: [Guía 05b](../Guias_Implementacion/05b-Tutorial_Campos_Formula.md).

### Día 4: Seguridad (El Final Boss)
1.  **Permisos y Accesos**
    *   **Contexto**: Quién ve qué.
    *   🔨 **Ejecución**: Configura Perfiles y OWD.
    *   📘 **Guía**: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md).
    *   👋 **Handover**: "Sistema seguro. QA, intenta hackearme".

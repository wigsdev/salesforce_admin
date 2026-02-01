# 🛡️ Manual de Ejecución: Salesforce Admin

**Tu Misión**: Eres el Constructor. Transformas requisitos en configuración tangible dentro de Salesforce.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Antes de empezar** | Verifica que la tarjeta en Trello tenga especificaciones claras del BA. Si no entiendes algo, **bloquea la tarea**. |
| 🔨 **EXEC** | **Tu Turno** | Configura en el entorno de desarrollo (Sandbox). Usa las Guías Técnicas. |
| 👋 **HANDOFF** | **Al terminar** | Mueve la tarjeta a la columna "QA" y etiqueta al **QA Tester** para validación. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN (Sprint 1)

### Día 1: El Corazón (Objetos y Datos)
*   🛑 **PRE-REQ**: El BA debe haber definido el modelo de datos (Qué objetos necesitamos).

1.  **Crear Objetos Custom (Carrera, Materia)**
    *   🔨 **EXEC**: Configura los objetos base.
    *   📘 **Guía**: [01-Tutorial_Carrera.md](../Guias_Implementacion/01-Tutorial_Carrera.md)
    *   📘 **Guía**: [02-Tutorial_Materia.md](../Guias_Implementacion/02-Tutorial_Materia.md)

2.  **Relacionar Objetos (Lookups/Master-Detail)**
    *   🔨 **EXEC**: Crea la relación "Materia pertenece a Carrera".
    *   📘 **Guía**: [01-Tutorial_Carrera.md](../Guias_Implementacion/01-Tutorial_Carrera.md) (Sección Relaciones)

*   👋 **HANDOFF**: Avisa al QA. "Modelo de datos base listo".

---

### Día 2: La Cara de la App (Branding)
*   🛑 **PRE-REQ**: El UX/UI (Consultant) debe haber definido el Logo y Colores.

1.  **Configurar My Domain y Temas**
    *   🔨 **EXEC**: Sube el logo de Lumina y ajusta los colores corporativos.
    *   📘 **Guía**: [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md)

*   👋 **HANDOFF**: Avisa al QA. "Entorno visual configurado".

---

### Día 3: Calidad de Datos (Validaciones)
*   🛑 **PRE-REQ**: El BA definió las reglas de negocio (ej. "No emails duplicados").

1.  **Crear Reglas de Validación**
    *   🔨 **EXEC**: Impide guardar registros "sucios".
    *   📘 **Guía**: [05-Tutorial_Validaciones.md](../Guias_Implementacion/05-Tutorial_Validaciones.md)

2.  **Campos Fórmula**
    *   🔨 **EXEC**: Automatiza cálculos (Promedios, Estados).
    *   📘 **Guía**: [05b-Tutorial_Campos_Formula.md](../Guias_Implementacion/05b-Tutorial_Campos_Formula.md)

*   👋 **HANDOFF**: Avisa al QA. "Reglas de negocio activas".

---

### Día 4: Seguridad (Acceso)
*   🛑 **PRE-REQ**: El Architect definió la Matriz de Seguridad (Quién ve qué).

1.  **Configurar Permission Sets**
    *   🔨 **EXEC**: Crea permisos granulares.
    *   📘 **Guía**: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md)

*   👋 **HANDOFF**: Avisa al QA. "Seguridad configurada. Intenta acceder con diferentes usuarios".

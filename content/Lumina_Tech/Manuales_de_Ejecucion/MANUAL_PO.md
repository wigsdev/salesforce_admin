# 👔 Manual de Ejecución: Product Owner (PO)

**Tu Misión**: Alimentar la máquina. Eres el dueño de las columnas **1. Backlog** y **2. Sprint Backlog**.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **(Externo)** | Recibes requerimientos del Negocio. |
| 💎 **VALUE** | **1. Backlog** | Creas y priorizas las historias con ayuda del BA. |
| 🏁 **COMMIT** | **2. Sprint Backlog** | Decides qué entra al Sprint. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN

### Día 0: Definición del Alcance
*   🛑 **PRE-REQ**: Leer el caso de negocio.

1.  **Refinar el Backlog**
    *   💎 **Acción en Columna 1**:
        *   Revisa cards creadas por el BA.
        *   Ordénalas por prioridad (Arriba = Más importante).
    *   📘 **Guía**: [06-Rol_Product_Owner.md](../Tutoriales_por_Rol/06-Rol_Product_Owner.md)

2.  **Sprint Planning**
    *   🏁 **Movimiento (1 -> 2)**:
        *   Mueve las historias elegidas de **1. Backlog** a **2. Sprint Backlog**.
        *   *Mensaje al equipo*: "Esto es lo que vamos a construir".

---

### Día 1: Definición de Datos
*   🛑 **PRE-REQ**: BA ha analizado el modelo académico.

1.  **Refinar HUs de Modelado**
    *   💎 **VALUE**: Trabajas con el BA para crear HU-001, HU-002, HU-003 (Objetos y Relaciones).
    *   *Acción*: Priorizas estas HUs en **2. Sprint Backlog** para que el Admin comience la construcción.

*   👋 **HANDOFF**: "HUs de modelado priorizadas. Admin puede comenzar".

---

### Día 2: Branding
*   🛑 **PRE-REQ**: BA ha definido los requerimientos visuales.

1.  **Refinar HUs de Branding**
    *   💎 **VALUE**: Trabajas con el BA para crear HU-004, HU-005, HU-006 (Dominio, Logo, App).
    *   *Acción*: Priorizas estas HUs en **2. Sprint Backlog**.
    *   📘 **Guía**: [5_Crear_las_HU_en_TRELLO.md](../Bitacoras_Sprint_1/dia_2/5_Crear_las_HU_en_TRELLO.md)

*   👋 **HANDOFF**: "HUs de branding priorizadas. Admin puede implementar identidad visual".

---

### Día 3: Calidad de Datos
*   🛑 **PRE-REQ**: BA ha definido las reglas de validación.

1.  **Refinar HUs de Validaciones**
    *   💎 **VALUE**: Trabajas con el BA para crear HU-007, HU-008 (Email, Notas).
    *   *Acción*: Priorizas estas HUs en **2. Sprint Backlog**.

*   👋 **HANDOFF**: "HUs de validaciones priorizadas. Admin puede implementar reglas".

---

### Día 4: Seguridad
*   🛑 **PRE-REQ**: BA ha definido los requerimientos de seguridad.

1.  **Refinar HUs de Seguridad**
    *   💎 **VALUE**: Trabajas con el BA para crear HU-009, HU-010, HU-011 (Privacidad, MFA, SoD).
    *   *Acción*: Priorizas estas HUs en **2. Sprint Backlog**.
    *   📘 **Guía**: [5_Crear_HU_Trello.md](../Bitacoras_Sprint_1/dia_4/5_Crear_HU_Trello.md)

*   👋 **HANDOFF**: "HUs de seguridad priorizadas. Admin y QA deben trabajar juntos en permisos".

---

### Fin del Sprint: La Demo
*   🛑 **PRE-REQ**: Tarjetas llegan a **7. SF Producción**.

1.  **Acceptance**
    *   Verifica el resultado final en Producción.
    *   Si está aprobado, el Release Manager mueve a **8. Terminado**.

# 🧪 Manual de Ejecución: QA Tester

**Tu Misión**: Romper cosas. Eres el dueño de la columna **5. SF QA**.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **4. SF Desarrollo** | El Admin terminó de construir en Sandbox. |
| 💥 **TEST** | **5. SF QA** | Ejecución de pruebas en entorno QA/Dev. |
| 👋 **HANDOFF** | **6. Aprobación TL** | Validado funcionalmente. Listo para revisión técnica. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN

### Rutina de Pruebas
1.  **Tomar la Tarea**
    *   **Movimiento (4 -> 5)**: Mueve la tarjeta desde **4. SF Desarrollo** a **5. SF QA**.
    *   *Acción*: Lee los Criterios de Aceptación.

2.  **Ejecutar Tests**
    *   💥 **Testing**:
        *   Usa el Sandbox para verificar la funcionalidad.
        *   Si falla: Devuelve la tarjeta a **3. En Progreso** y comenta el error.
        *   Si pasa: Continúa.
    *   📘 **Guía**: [03-Rol_QA_Tester.md](../../Tutoriales_por_Rol/03-Rol_QA_Tester.md)

3.  **Aprobación**
    *   **Movimiento (5 -> 6)**: Mueve la tarjeta a **6. Aprobación TL**.
    *   👋 **Handover**: @menciona al **Team Lead**. "Funcionalidad validada. Pase a revisión de código".

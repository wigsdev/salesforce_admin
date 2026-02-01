# 🚀 Manual de Ejecución: Release Manager

**Tu Misión**: Despliegue. Eres el dueño de las columnas **7. SF Producción** y **8. Terminado**.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **7. SF Producción** | El TL aprobó técnicamente. La tarjeta espera deploy. |
| 📦 **DEPLOY** | **(Proceso)** | Ejecutas Change Sets / Metadata API hacia Prod. |
| 🏁 **DONE** | **8. Terminado** | Está vivo en Producción. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN

### Rutina de Despliegue
1.  **Preparar Release**
    *   **Contexto**: Acumula tarjetas en **7. SF Producción** hasta la ventana de mantenimiento (ej. Viernes).
    *   📘 **Guía**: [04-Rol_Release_Manager.md](../Tutoriales_por_Rol/04-Rol_Release_Manager.md)

2.  **Ejecutar Deploy**
    *   📦 **Acción**: Sube los cambios de Sandbox a Producción.

3.  **Cierre de Tarea**
    *   **Movimiento (7 -> 8)**: Mueve las tarjetas desplegadas a **8. Terminado**.
    *   🏁 **Celebración**: Avisa al equipo: "La funcionalidad X está en vivo".

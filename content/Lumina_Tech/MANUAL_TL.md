# 🏗️ Manual de Ejecución: Team Lead (TL)

**Tu Misión**: Calidad Técnica. Eres el dueño de la columna **6. Aprobación TL**.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **5. SF QA** | El QA dice que funciona funcionalmente. |
| 🔍 **REVIEW** | **6. Aprobación TL** | Revisas calidad, nomenclatura y seguridad. |
| 👋 **HANDOFF** | **7. SF Producción** | Todo limpio. Listo para despliegue. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN

### Rutina de Revisión
1.  **Auditoría**
    *   **Contexto**: La tarjeta está en **6. Aprobación TL**.
    *   🔍 **Review**:
        *   Entra al Sandbox.
        *   Verifica nombres de API (`Nombre__c`).
        *   Verifica que no hay permisos excesivos.

2.  **Aprobación Final**
    *   **Movimiento (6 -> 7)**: Mueve la tarjeta a **7. SF Producción**.
    *   👋 **Handover**: @menciona al **Release Manager**. "Código limpio. Autorizado para Deploy".

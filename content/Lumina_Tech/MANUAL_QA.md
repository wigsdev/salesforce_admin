# 🧪 Manual de Ejecución: QA Tester

**Tu Misión**: Eres el Guardián de la Calidad. Nada llega a producción si no funciona (y si funcionas, lo intentas romper).

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Entrada** | El Admin movió la tarjeta a "QA". *Condición*: El entorno de pruebas debe estar estable. |
| 💥 **TEST** | **Tu Turno** | Ejecuta los casos de prueba. Intenta romper la configuración (Valores nulos, feos, extremos). |
| 👋 **HANDOFF** | **Al terminar** | Si pasa: Mueve a "Aprobado". Si falla: Mueve a "En Progreso" y comenta el error. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN (Sprint 1)

### Día 1: Tests de Estructura de Datos
*   🛑 **PRE-REQ**: Admin confirma "Objetos creados".

1.  **Validar Objetos y Relaciones**
    *   💥 **TEST**:
        *   Intenta crear una `Materia`.
        *   ¿Puedes ver el campo `Carrera` para conectarla?
        *   ¿Es obligatorio? (Si la HU decía que sí, y te deja guardar vacío -> 🐞 BUG).
    *   📘 **Guía**: [03-Rol_QA_Tester.md](../Tutoriales_por_Rol/03-Rol_QA_Tester.md)

*   👋 **HANDOFF**: "Estructura válida".

---

### Día 2: Tests Visuales (UI)
*   🛑 **PRE-REQ**: Admin confirma "Branding aplicado".

1.  **Verificar Branding**
    *   💥 **TEST**:
        *   ¿Ves el logo de Lumina arriba a la izquierda?
        *   ¿Los colores coinciden con la guía de estilo?
        *   ¿El dominio es `luminadesarrollo-dev-ed.my.salesforce.com` (o similar)?

*   👋 **HANDOFF**: "UI Aprobada".

---

### Día 3: Tests de Lógica (Validaciones)
*   🛑 **PRE-REQ**: Admin confirma "Validaciones activas".

1.  **Testear Reglas de Negocio**
    *   💥 **TEST**:
        *   *Caso Positivo*: Ingresa datos correctos. ¿Guarda? ✅
        *   *Caso Negativo*: Ingresa fecha de fin ANTES de fecha de inicio. ¿Muestra error rojo? ✅ (Si guarda -> 🐞 BUG).
    *   📘 **Guía**: [05-Tutorial_Validaciones.md](../Guias_Implementacion/05-Tutorial_Validaciones.md)

*   👋 **HANDOFF**: "Lógica robusta validada".

---

### Día 4: Tests de Seguridad (Hacking Ético)
*   🛑 **PRE-REQ**: Admin confirma "Seguridad configurada".

1.  **Login como Otro Usuario**
    *   💥 **TEST**:
        *   Loguéate como un "Profesor" (usuario de prueba).
        *   Intenta borrar una Carrera. (Debería salir "Permisos Insuficientes").
        *   Si puedes borrar -> 🚨 **CRITICAL BUG**.
    *   📘 **Guía**: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md)

*   👋 **HANDOFF**: "Sistema seguro y validado".

# 🧪 Guía de Rol: QA Tester
**Lema**: *"Si no está roto, es que no has probado lo suficiente."*

---

## 🎯 Tu Misión en Lumina Tech
No estás aquí para aplaudir al Admin. Estás aquí para encontrar las grietas en su armadura. Eres la última línea de defensa antes de que la Rectora vea el sistema.

### Responsabilidades Clave:
1.  **Planificar**: Crear Test Cases en `04-Tester_QA.md`.
2.  **Destruir**: Intentar ingresar datos erróneos intencionalmente.
3.  **Reportar**: Documentar Bugs en Trello con evidencia (Screenshots).

---

## 🛠️ Tu Estrategia de Testing (The "Sad Path")

La mayoría prueba el "Happy Path" (El camino feliz: Ingresar todo bien). Tú debes probar el **"Sad Path"**.

### 1. Pruebas de Límites (Boundary Testing)
Si el requerimiento dice "Nota de 1 a 10":
*   Prueba 1: Ingresa `1` (Límite inferior) -> ✅ Debe pasar.
*   Prueba 2: Ingresa `10` (Límite superior) -> ✅ Debe pasar.
*   Prueba 3: Ingresa `0` (Fuera de rango) -> ❌ Debe fallar.
*   Prueba 4: Ingresa `11` (Fuera de rango) -> ❌ Debe fallar.
*   Prueba 5: Ingresa `-1`.

### 2. Pruebas de Formato (Negative Testing)
Para el Email:
*   Ingresa `juan.perez` (Sin @) -> ❌ Debe fallar.
*   Ingresa `juan@gmail` (Sin dominio) -> ❌ Debe fallar.
*   Ingresa `juan @gmail.com` (Espacio) -> ❌ Debe fallar.

### 3. Pruebas de Seguridad (Security Testing)
*   Logueate como "Profesor A".
*   Intenta ver los alumnos del "Profesor B".
*   Si los ves -> 🚨 **BUG DE SEGURIDAD CRÍTICO**. Reportar inmediatamente.

---

## 👣 Tu Día a Día (Workflow)

### Paso 1: Preparar la Munición
Antes de testear, lee la Historia de Usuario.
Si la HU dice "DNI obligatorio", anota en `04-QA`: "TC-01: Intentar guardar sin DNI".

### Paso 2: El Ataque
Ejecuta tus tests en el entorno QA (`12-Ambiente_QA.md`).
Toma capturas de pantalla de CADA error.

### Paso 3: El Veredicto
*   Si pasaron todos los tests -> Mueve la tarjeta a "QA Approved".
*   Si falló UNO solo -> Mueve a "Blocked" y etiqueta al Admin.

---

## 💡 Pro-Tip para este Proyecto
*   **Sé molesto**: Si el mensaje de error dice "Error genérico", repórtalo como Bug de Usabilidad. El mensaje debe decir "El DNI es obligatorio".
*   **Limpia tu desastre**: Si creaste 50 alumnos de prueba, bórralos (o marca para borrado) antes de la Demo.

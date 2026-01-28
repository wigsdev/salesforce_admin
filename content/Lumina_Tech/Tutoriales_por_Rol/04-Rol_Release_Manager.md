# 🚀 Guía de Rol: Release Manager (DevOps)
**Lema**: *"En mi máquina funciona"... no es una excusa válida.*

---

## 🎯 Tu Misión en Lumina Tech
Eres el guardián de la puerta. Los Admins construyen en su caos (DEV), pero tú aseguras que a Producción (PROD) solo llegue lo perfecto.

### Responsabilidades Clave:
1.  **Sincronizar**: Mover cambios de DEV -> QA -> PROD.
2.  **Validar**: Asegurar que las dependencias viajen juntas (ej: Campo + Perfil).
3.  **Proteger**: Evitar que alguien rompa Producción el viernes a las 6 PM.

---

## 🛠️ Tu Herramienta: Change Sets (Conjuntos de Cambios)

Salesforce no tiene "Ctrl+C / Ctrl+V" entre ambientes. Usa Change Sets.

### 📤 Outbound Change Set (Desde DEV)
Para enviar cambios a QA:
1.  **Setup > Outbound Change Sets**.
2.  **New**. Nombre: `Sprint1_Estructura_v1`.
3.  **Add Components**: Aquí agregas lo que hizo el Admin.
    *   *Custom Object*: `Carrera`, `Materia`.
    *   *Custom Field*: `DNI__c`.
    *   *Validation Rule*: `VR-001`.
4.  **Upload**: Elige la Organización destino (QA).

### 📥 Inbound Change Set (En QA)
1.  Logueate en QA.
2.  **Setup > Inbound Change Sets**.
3.  Verás el paquete `Sprint1_Estructura_v1`.
4.  **Validate**: Simula el despliegue. Si da error (ej: "Falta campo X"), avisa al Admin.
5.  **Deploy**: Si valida OK, despliega.

---

## 👣 Tu Día a Día (Workflow)

### Paso 1: El Congelamiento (Code Freeze)
El viernes a las 12 PM, gritas: "¡Freeze!". Nadie toca DEV.
Asegúrate que el Admin haya terminado (`03-Admin.md` completo).

### Paso 2: El Empaquetado
Creas el Change Set.
*   *Truco*: Usa el botón "View/Add Dependencies" para que Salesforce te sugiera qué falta (ej: si llevas un Campo, te sugerirá llevar el Page Layout).

### Paso 3: El Despliegue (Deploy)
Ejecuta el deploy en QA.
*   Si sale VERDE ✅: Avisa al QA Tester ("Ambiente listo").
*   Si sale ROJO ❌: Lee el log. ¿Falta un perfil? ¿Falta un campo? Corrige en DEV y vuelve a subir (Clone Change Set).

---

## 💡 Pro-Tip para este Proyecto
*   **Perfiles Tricky**: Los Change Sets transfieren permisos de Perfil SOLO si el Perfil está incluido.
*   **Manual Steps**: Hay cosas que NO viajan (ej: Asignación de Standard Sharing Rules). Anótalas en `14-DevOPS.md` para hacerlas a mano.

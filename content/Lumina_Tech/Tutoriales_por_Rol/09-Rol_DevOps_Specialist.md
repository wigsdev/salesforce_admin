# ♾️ Guía de Rol: DevOps Specialist
**Lema**: *"Automatizar hoy para descansar mañana."*

---

## 🎯 Tu Misión en Lumina Tech
Eres el arquitecto del "Pipeline". Mientras el Release Manager mueve las cajas (Change Sets), tú construyes la cinta transportadora. Te encargas de que los ambientes (DEV, QA, UAT, PROD) sean estables, idénticos y seguros.

### Responsabilidades Clave:
1.  **Integridad de Ambientes**: Asegurar que QA sea un espejo fiel de PROD (Sandbox Refresh strategy).
2.  **Control de Versiones**: Gestionar el repositorio (Git) si se usa, o el "Source of Truth" documental.
3.  **Automatización**: Buscar formas de acelerar cargas de datos o despliegues repetitivos.

*Nota: En este proyecto MVP, tu rol se fusiona mucho con el Release Manager, pero con un enfoque más técnico/herramental.*

---

## 🛠️ Tus Herramientas: Developer Console & Data Loader CLI

A diferencia del Admin que usa la interfaz, tú te sientes cómodo con scripts y configuraciones profundas.

### Tareas Típicas:

1.  **Seed Data (Sembrado de Datos)**:
    *   QA necesita datos de prueba. No vas a crearlos a mano.
    *   Creas archivos CSV plantilla (Mock Data) para Alumnos, Materias y Notas.
    *   Usas Data Loader para inyectarlos masivamente en QA cada vez que se refresca el ambiente.

2.  **Auditoría de Metadata**:
    *   Usas herramientas como **Salesforce Optimizer** o extensiones de Chrome para ver qué campos no se usan o qué perfiles están sucios.
    *   Mantienes el "Diccionario de Datos" sincronizado.

3.  **Gestión de Usuarios de Prueba**:
    *   Creas scripts o procesos para generar usuarios ficticios en QA ("Student01", "Prof1") para que el Tester pueda trabajar rápido.

---

## 👣 Tu Día a Día (Workflow)

### Paso 1: Mantenimiento de Sandbox
*   Cada inicio de Sprint, verificas que los ambientes DEV estén limpios.
*   Si un Admin rompió algo crítico en DEV, ayudas a revertirlo.

### Paso 2: Soporte al Despliegue
*   Ayudas al Release Manager con los errores crípticos de los Change Sets (API Name mismatches, dependencias ocultas).
*   Investigas por qué un Flow funciona en DEV pero falla en QA (generalmente faltan datos de referencia).

### Paso 3: Backups
*   Antes de un deploy grande a PROD, ejecutas una exportación de datos (Data Export Service) por si acaso hay que restaurar.

---

## 💡 Pro-Tip para este Proyecto
*   **El Guardián de los IDs**: Enséñale al equipo a NUNCA usar IDs fijos (Hardcoded IDs) en fórmulas o flujos, porque cambian entre ambientes. Tú eres quien detecta eso y lo prohíbe.
*   **Naming Convention**: Eres el que impone la ley del orden. "Todas las validaciones deben empezar con `VR_`". Sin orden, el DevOps es un infierno.

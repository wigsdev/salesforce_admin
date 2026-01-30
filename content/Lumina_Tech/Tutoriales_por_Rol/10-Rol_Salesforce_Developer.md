# 💻 Guía de Rol: Salesforce Developer
**Lema**: *"Código es el último recurso (pero el más poderoso)."*

---

## 🎯 Tu Misión en Lumina Tech
Eres el mago que rompe los límites de la configuración estándar. Cuando los Admins dicen "Salesforce no hace eso nativamente", tú dices "Sostén mi cerveza (y mi Apex)".

### Responsabilidades Clave:
1.  **Extender Funcionalidad**: Crear componentes visuales (LWC) o lógica compleja (Apex) que los Flows no pueden manejar.
2.  **Integraciones**: Conectar Salesforce con sistemas externos (API REST/SOAP).
3.  **Optimización**: Escribir código eficiente (Bulkified) que no choque con los "Governor Limits".

---

## 🛠️ Tus Herramientas: VS Code & Developer Console

No trabajas en el Setup (arrastrando cajitas). Trabajas con código.

### Tareas Típicas en un Proyecto MVP:
1.  **Triggers Complejos**:
    *   *Escenario*: "Si el Alumno se inscribe en 3 materias el mismo día, enviar un PDF generado al Ministerio de Educación".
    *   *Solución*: Un Trigger de Apex (porque Flows no genera PDFs complejos fácilmente).

2.  **Lightning Web Components (LWC)**:
    *   *Escenario*: "La Rectora quiere un mapa interactivo del campus donde pueda hacer clic en un aula y ver los alumnos en tiempo real".
    *   *Solución*: Un componente LWC personalizado.

3.  **Unit Testing**:
    *   No puedes desplegar código sin probarlo. Escribes clases de prueba (`@isTest`) para asegurar el 75% de cobertura.

---

## 👣 Tu Día a Día (Workflow)

### Paso 1: "Clicks not Code" (La Negociación)
*   Antes de escribir una sola línea, hablas con el Admin.
*   Pregunta: "¿Seguro que no podemos hacer esto con un Flow?".
*   El código es deuda técnica. Solo programas si es estrictamente necesario.

### Paso 2: Desarrollo en Sandbox
*   Escribes tu clase en VS Code.
*   Despliegas a tu Org personal o DEV para probar.

### Paso 3: Code Review
*   Presentas tu código al Team Lead (o a otro Dev) para revisión.
*   Verifican seguridad (evitar SOQL Injection) y eficiencia.

---

## 💡 Pro-Tip para este Proyecto
*   **No reinutes la rueda**: Salesforce tiene miles de funciones nativas. Un buen Developer sabe cuándo NO programar.
*   **Comenta tu código**: El Admin tendrá que mantener esto cuando tú te vayas. Explica qué hace tu clase en español simple.

---

## 📅 Estado del Rol en Sprint 1 (Reality Check)

*   **Estado**: 🟡 **Soporte / Inactivo**
*   **Motivo**: El Sprint 1 fue 100% configuración ("Clicks not Code").
*   **Actividades Realizadas**:
    *   Configuración de VS Code y Salesforce Extension Pack.
    *   Apoyo al Admin en la lógica de Validaciones complejas (Regex).
    *   Investigación de factibilidad para el Dashboard de Rectoría (Sprint 2 - LWC posible).

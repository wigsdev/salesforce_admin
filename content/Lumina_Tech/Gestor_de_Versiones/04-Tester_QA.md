# 🧪 Tester QA - Plan de Pruebas
**Proyecto**: Lumina Tech
**Sprint**: 01

---

## 📅 Definición de Casos de Prueba
(Pendiente de Ejecución - Se definirá junto con las Historias de Usuario)

## 📅 DIA 1 - Pruebas de Modelo de Datos
*   **Estado**: Pendiente
*   **Casos de Prueba**:
    *   Verificar existencia de objetos: `Carrera`, `Materia`, `Alumno`, `Inscripción`.
    *   Validar Schema Builder: Que las relaciones (Lookup/Master-Detail) sean correctas.
    *   Verificar tipos de datos: Que "Legajo" sea Texto/Número según definición, que Fechas sean Date.

---

## 📅 DIA 2 - Pruebas de Aplicación
*   **Estado**: Pendiente
*   **Casos de Prueba**:
    *   Verificar Branding: Logo y Colores de Lumina Tech visibles.
    *   Verificar Navegación: Que las pestañas (Tabs) estén en el orden correcto.
    *   Prueba de Acceso: Que la App sea visible para el perfil System Administrator.

---

## 📅 DIA 3 - Pruebas de Calidad de Datos
*   **Estado**: Pendiente
*   **Casos de Prueba**:
    *   **Validaciones**: Intentar guardar emails sin `@lumina.edu` (Debe fallar). Intentar notas < 0 o > 10.
    *   **Fórmulas**: Verificar que `Materia_Display__c` concatene bien el nombre y código.
    *   **Integridad**: Verificar que no se puedan borrar registros "Hijos" si la relación es Master-Detail.

---

## 📅 DIA 4 - Pruebas de Seguridad
*   **Estado**: Pendiente
*   **Casos de Prueba**:
    *   **OWD**: Loguearse como Profesor A y verificar que NO ve alumnos de Profesor B (si aplica).
    *   **Permission Sets**: Verificar que el usuario con `Permission Set Group: Lumina Admin` tenga acceso total.
    *   **MFA**: Verificar que se pida doble factor al iniciar sesión (si está activo).
    *   **FLS**: Verificar que un usuario estándar solo pueda LEER la nota final, no editarla.

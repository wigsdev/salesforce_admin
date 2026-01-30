# 10-DEMO_FINAL.md - Guión de Presentación (Sprint Review)
**Audiencia**: Dra. Vance (Rectora), Consejo Académico
**Duración**: 15 min
**Presentador**: Product Owner

---

## 🎭 Guión paso a paso

### 1. Introducción (2 min)
*   **Narrativa**: "Hoy les mostraremos cómo hemos digitalizado el legajo de los alumnos, eliminando las planillas de excel y garantizando la seguridad de las notas."
*   **Login**: Ingresar como `System Admin` (para mostrar todo) y luego switch a `Profesor`.

### 2. El "Happy Path" (5 min)
*   **Acción**: Crear una Carrera ("Ingeniería").
*   **Acción**: Crear una Materia ("Algoritmos").
*   **Acción**: Matricular un Alumno ("Juan Perez").
    *   *Highlight*: Mostrar que el DNI es obligatorio. Intentar dejarlo vacío -> **Error**.
*   **Acción**: Inscribir a Juan en Algoritmos.

### 3. La Prueba de Fuego: Seguridad (5 min)
*   **Switch User**: "Login As" -> Seleccionar usuario `Profesor Garcia`.
*   **Acción**: Ir a la pestaña "Alumnos".
*   **Validación**: Mostrar que la lista "All" solo muestra los alumnos de Garcia, no los de todo el colegio.
*   **Acción**: Intentar cambiar la nota de una materia cerrada.
    *   *Resultado*: Campo bloqueado o Error de validación.

### 4. Preguntas y Cierre (3 min)
*   Mostrar Dashboard simple (si se creó) o Reporte de "Inscripciones por Materia".
*   Anunciar alcance del Sprint 2: "Reportes Avanzados y Migración de Datos".

---

## 🎒 Checklist de Preparación
*   [ ] Limpiar datos de prueba "basura" (ej: "asd asd").
*   [ ] Tener abiertas las pestañas necesarias (evitar tiempos de carga).
*   [ ] Verificar que el usuario "Profesor Demo" esté activo.
*   [ ] Resolución de pantalla al 110% (Zoom) para mejor visibilidad.

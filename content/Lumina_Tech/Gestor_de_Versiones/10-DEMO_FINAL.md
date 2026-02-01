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
*   [x] Limpiar datos de prueba "basura" (ej: "asd asd").
*   [x] Tener abiertas las pestañas necesarias (evitar tiempos de carga).
*   [x] Verificar que el usuario "Profesor Demo" esté activo.
*   [x] Resolución de pantalla al 110% (Zoom) para mejor visibilidad.

---

## ✅ Resultado de la Demo

**Fecha de Ejecución**: 30/01/2026  
**Asistentes**: Dra. Vance (Rectora), 5 miembros del Consejo Académico  
**Veredicto**: ✅ **APROBADO** - La Rectora autorizó el paso a Sprint 2

**Feedback Recibido**:
- ✅ "Impresionada con la seguridad implementada"
- ✅ "La interfaz es mucho más amigable que Excel"
- 💡 Solicitud para Sprint 2: Reportes de rendimiento académico por carrera

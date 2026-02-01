# 🎓 Guía Técnica: Visualización (Schema Builder)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado - Revisión)
**Rol Responsable**: 🏗️ **Salesforce Consultant**
**HUs Relacionadas**: [HU-003](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md), [HU-004](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)

---

## 🎯 Objetivo
Ver "cómo se conectan las tablas" visualmente (ERD). Validar que la arquitectura Alumno-Inscripción-Materia sea correcta.

## 🛠️ Procedimiento

### Paso 1: Abrir la "Pizarra"
1.  Haz clic en el ícono de engranaje ⚙️ y selecciona **Setup**.
2.  En el cuadro de búsqueda (Quick Find), escribe: `Schema Builder`.
3.  Selecciona **Schema Builder** en el menú desplegable.

### Paso 2: Limpiar el Ruido
Por defecto, verás cientos de objetos estándar.
1.  En el panel izquierdo, haz clic en el enlace **Clear All**.
    *   *Resultado*: La pizarra central quedará vacía.

### Paso 3: Seleccionar tus Objetos
En el panel izquierdo ("Select from"), usa el buscador o las casillas para marcar SOLO tus 4 objetos:
1.  Marca ☑️ `Carrera`
2.  Marca ☑️ `Materia`
3.  Marca ☑️ `Alumno`
4.  Marca ☑️ `Inscripción`
    *   *(Si no aparece, revisa si escribiste Inscripcion sin tilde)*.

### Paso 4: Interpretar las Conexiones
Verás 4 cajas flotando. Arrástralas con el mouse para ordenarlas.

**Validación Visual (La Prueba de Fuego):**
1.  Verifica que sale una línea de **Materia** y toca a **Carrera**.
2.  Verifica el "Triángulo":
    *   Una línea sale de **Inscripción** y toca a **Alumno**.
    *   Otra línea sale de **Inscripción** y toca a **Materia**.

> **Referencia de Colores**:
> *   **Rojo/Rosado**: Relación Master-Detail (Si borras el padre, se borra el hijo).
> *   **Azul**: Relación Lookup (Relación débil).

---

## ✅ Verificación de Éxito
1.  Organiza las cajas para que `Inscripción` quede visualmente al medio de `Alumno` y `Materia`.
2.  Toma una **Captura de Pantalla**.
3.  ¡Ese es tu **Diagrama Entidad-Relación (ERD)** oficial para la documentación! 🗺️

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
### Paso 3: Seleccionar tus Objetos
En el panel izquierdo ("Select from"), usa el buscador o las casillas para marcar SOLO tus 5 objetos:
1.  Marca ☑️ `Career`
2.  Marca ☑️ `Subject`
3.  Marca ☑️ `Student`
4.  Marca ☑️ `Enrollment`
5.  Marca ☑️ `Exam` *(If you already completed Guide 10)*

### Paso 4: Interpretar las Conexiones
Verás 5 cajas flotando. Arrástralas con el mouse para ordenarlas.

**Validación Visual (La Prueba de Fuego):**
1.  Verifica que sale una línea de **Subject** y toca a **Career**.
2.  Verifica el "Triángulo":
    *   Una línea sale de **Enrollment** y toca a **Student**.
    *   Otra línea sale de **Enrollment** y toca a **Subject**.
3.  Verify that **Exam** hangs from **Enrollment** (Master-Detail Relationship).

> **Referencia de Colores**:
> *   **Rojo/Rosado**: Relación Master-Detail (Si borras el padre, se borra el hijo).
> *   **Azul**: Relación Lookup (Relación débil).

---

## ✅ Verificación de Éxito
1.  Organiza las cajas para que `Enrollment` quede visualmente al medio de `Student` y `Subject`.
2.  Toma una **Captura de Pantalla**.
3.  ¡Ese es tu **Diagrama Entidad-Relación (ERD)** oficial para la documentación! 🗺️

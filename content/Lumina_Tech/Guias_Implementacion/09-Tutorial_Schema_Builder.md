# 🎓 Guía Técnica: Visualización (Schema Builder)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado - Revisión)
**Rol Responsable**: 🏗️ **Salesforce Consultant**
**HUs Relacionadas**: HU-003, HU-004

---vo**: Ver "cómo se conectan las tablas" visualmente (ERD).

---

## 🎯 ¿Por qué esto es vital?
Hasta ahora has creado objetos "a ciegas" usando menús.
El **Schema Builder** es la herramienta gráfica que te muestra la arquitectura real. Es como pasar de leer las instrucciones de Lego a ver el modelo 3D terminado.

## 🛠️ Procedimiento

### Paso 1: Abrir la "Pizarra"
1.  Ve a **Setup** (Engranaje ⚙️).
2.  En el cuadro de búsqueda (Quick Find), escribe: `Schema Builder`.
3.  Selecciona **Schema Builder**.

### Paso 2: Limpiar el Ruido
Por defecto, verás cientos de objetos estándar que no nos importan ahora.
1.  En el panel izquierdo, haz clic en **Clear All**.
2.  Ahora tu pizarra central debería estar vacía.

### Paso 3: Seleccionar tus Órganos (Objetos)
En el panel izquierdo (Select from), busca y marca SOLO tus 4 objetos:
1.  ☑️ `Carrera`
2.  ☑️ `Materia`
3.  ☑️ `Alumno`
4.  ☑️ `Inscripción` (Ojo: puede aparecer como `Inscripcion` sin tilde según cómo la nombraste).

### Paso 4: Interpretar las Líneas (The Connections)
Verás 4 cajitas flotando. Arrástralas para ordenarlas lógicamente.

**Lo que debes ver (La Verdadera Prueba):**
*   🟢 **Línea 1**: Sale de `Materia` y toca `Carrera`.
    *   *Significado*: Una Materia pertenece a una Carrera.
*   🔴 **Líneas 2 y 3 (El Triángulo)**:
    *   Una línea sale de `Inscripción` y toca `Alumno`.
    *   Otra línea sale de `Inscripción` y toca `Materia`.
    *   *Significado*: La `Inscripción` es el punto de unión (Junction) entre Alumno y Materia.

> **Colores de Líneas**:
> *   **Rojo/Rosado**: Relación Master-Detail (Fuerte). Si borras el padre, adiós hijo.
> *   **Azul**: Relación Lookup (Débil).

---

## ✅ Verificación de Éxito
1.  Organiza las cajitas para que `Inscripción` quede al medio de `Alumno` y `Materia`.
2.  Toma una **Captura de Pantalla**.
3.  ¡Ese es tu **Diagrama Entidad-Relación (ERD)** oficial! 🗺️

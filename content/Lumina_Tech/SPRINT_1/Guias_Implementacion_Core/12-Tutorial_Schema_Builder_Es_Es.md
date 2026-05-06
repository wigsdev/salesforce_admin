# 🎓 Guía Técnica: Visualización de Arquitectura (Schema Builder) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Validación de Refactorización)
**Rol Responsable**: 🏗️ **Salesforce Consultant / Architect**

---

## 🎯 Objetivo
Ver "cómo se conectan las tablas" visualmente (ERD - Entity Relationship Diagram) para confirmar que la refactorización Enterprise se aplicó correctamente. Esta herramienta es vital para validar la integridad del modelo (Master-Detail vs Lookups) antes de migrar datos.

## 🛠️ Procedimiento

### Paso 1: Abrir la "Pizarra"
1.  Haz clic en el ícono de engranaje ⚙️ y selecciona **Setup**.
2.  En el cuadro de búsqueda (Quick Find), escribe: `Schema Builder`.
3.  Selecciona **Schema Builder** en el menú desplegable.

### Paso 2: Limpiar el Ruido
Por defecto, verás cientos de objetos estándar.
1.  En el panel izquierdo, haz clic en el enlace **Clear All**.
    *   *Resultado*: La pizarra central quedará vacía.

### Paso 3: Seleccionar tus Objetos (Arquitectura Final)
En el panel izquierdo ("Select from"), asegúrate de tener marcado "All Objects" y usa el buscador para marcar SOLO los **7 objetos principales** de nuestra arquitectura refactorizada:
1.  Marca ☑️ `Contact` *(Es el objeto estándar que usamos para Alumnos y Profesores).*
2.  Marca ☑️ `Carrera`
3.  Marca ☑️ `Materia`
4.  Marca ☑️ `Inscripción`
5.  Marca ☑️ `Evaluación` *(Antes llamado Nota).*
6.  Marca ☑️ `Asistencia`
7.  Marca ☑️ `Cobro` *(El módulo de Tesorería).*

### Paso 4: Interpretar las Conexiones (La Prueba de Fuego)
Verás 7 cajas flotando. Arrástralas con el mouse para ordenarlas y validar las relaciones:

> **Referencia de Colores de Líneas**:
> *   🔴 **Rojo/Rosado**: Relación **Master-Detail** (Padre estricto. Si borras el padre, se borra el hijo. Habilita Roll-Up Summaries).
> *   🔵 **Azul**: Relación **Lookup** (Relación débil, aunque en nuestro diseño la hicimos "Obligatoria" vía Required field).

**Validación Visual:**
1.  **Catálogo:** Verifica que sale una línea ROJA de **Materia** apuntando hacia **Carrera**.
2.  **El Triángulo Académico (Junction Object):**
    *   Sale una línea ROJA de **Inscripción** apuntando hacia **Contact**.
    *   Sale otra línea ROJA de **Inscripción** apuntando hacia **Materia**.
3.  **Límites de Arquitectura:**
    *   Como Inscripción ya tiene dos líneas Rojas (Master-Detail), Salesforce bloquea que sea padre Master-Detail de otros. Por eso...
    *   Verifica que de **Evaluación** sale una línea AZUL (Lookup) hacia **Inscripción**.
    *   Verifica que de **Asistencia** sale una línea AZUL (Lookup) hacia **Inscripción**.
4.  **Tesorería y Morosidad:**
    *   Verifica que de **Cobro** sale una línea ROJA hacia **Contact**. *(Esto es lo que permitió habilitar el Roll-Up Summary de 'Deuda Vencida' en la ficha del Alumno).*

---

## ✅ Verificación de Éxito
1.  Organiza las cajas para que `Inscripción` quede visualmente al medio de `Contact` y `Materia`.
2.  Pon `Cobro` al lado de `Contact`.
3.  Pon `Asistencia` y `Evaluación` debajo de `Inscripción`.
4.  Toma una **Captura de Pantalla**.
5.  ¡Ese es tu **Diagrama Entidad-Relación (ERD)** oficial que respalda todo el esfuerzo de refactorización! 🗺️

# 📚 Índice de Implementación: Sprint 1 (Fundamentos) - Localizado 🇪🇸

Bienvenido al Sprint 1 de **Lumina Tech**. En esta fase, construiremos el núcleo del sistema de Gestión Académica totalmente localizado al español (Frontend y Backend).

## 📋 Documentación de Referencia
*   **Historias de Usuario (Backlog)**: [HISTORIAS_DE_USUARIO_ES.md](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md)

---

## 🚀 Ruta de Implementación (Paso a Paso)

Sigue estas guías en orden estricto para garantizar que las dependencias entre objetos (Relaciones Padre-Hijo) se resuelvan correctamente.

### 🧱 Fase 1: Modelado de Datos (Arquitectura)
1.  **[01 - Carreras](./01-Tutorial_Carrera_Es_Es.md)**
    *   *Objetivo*: Crear la oferta académica (Objeto: `Carrera`).
2.  **[02 - Materias](./02-Tutorial_Materia_Es_Es.md)**
    *   *Objetivo*: Crear el plan de estudios (Objeto: `Materia`).
3.  **[03 - Alumnos](./03-Tutorial_Alumno_Es_Es.md)**
    *   *Objetivo*: Crear el registro de personas con DNI y validaciones (Objeto: `Alumno`).
4.  **[04 - Inscripciones](./04-Tutorial_Inscripcion_Es_Es.md)**
    *   *Objetivo*: El "Junction Object" que une al Alumno con la Materia (Objeto: `Inscripción`).
5.  **[10 - Exámenes](./10-Tutorial_Examen_Es_Es.md)**
    *   *Objetivo*: Cargas de notas vinculadas a la Inscripción (Objeto: `Examen`).

---

### 🛡️ Fase 2: Calidad y Seguridad
6.  **[05 - Reglas de Validación](./05-Tutorial_Validaciones_Es_Es.md)**
    *   *Objetivo*: "Blindar" el sistema (Formatos de Email, Rangos de Nota, DNI numérico).
7.  **[06 - Seguridad y Permisos](./06-Tutorial_Seguridad_Es_Es.md)**
    *   *Objetivo*: Configurar quién ve qué (OWD, Perfiles, MFA).

---

### 🎨 Fase 3: Experiencia de Usuario (UI/UX)
8.  **[07 - Lightning App Builder](./07-Tutorial_App_Builder_Es_Es.md)**
    *   *Objetivo*: Crear la App "Gestión Académica Lumina".

---

### 💾 Fase 4: Operación
9.  **[08 - Carga de Datos](./08-Tutorial_Carga_Datos_Es_Es.md)**
    *   *Objetivo*: Importar alumnos masivamente desde CSV.

---

### ✅ Fase 5: Verificación Final
10. **[09 - Visualización (Schema Builder)](./09-Tutorial_Schema_Builder_Es_Es.md)**
    *   *Objetivo*: Validar visualmente el modelo de datos (ERD).

---

## 💡 Glosario de Localización (Técnico)
Para este proyecto, se ha definido una política de **Nombres API en Español** (con sanitización de caracteres especiales):

| Concepto | API Name (Backend) | Label (Frontend) | Nota Técnica |
| :--- | :--- | :--- | :--- |
| **Carrera** | `Carrera__c` | `Carrera` | Objeto Maestro. |
| **Materia** | `Materia__c` | `Materia` | Depende de Carrera. |
| **Alumno** | `Alumno__c` | `Alumno` | AutoNumber ID (`A-{0000}`). |
| **Inscripción** | `Inscripcion__c` | `Inscripción` | Junction Object. |
| **Examen** | `Examen__c` | `Examen` | Lookup Required. |
| **Año** | `Anio` | `Año` | `ñ` -> `ni`. |
| **Teléfono** | `Telefono` | `Teléfono` | Sin tilde. |

# 06-Investigaciones.md - Decisiones de Diseño (ADR)
**Rol**: Solutions Architect
**Tema**: Diseño de Base de Datos y Seguridad

---

## 🔬 Investigación 1: Modelo Relacional de Inscripciones

### Contexto
Necesitamos conectar `Alumnos` con `Materias`. Un alumno tiene muchas materias, y una materia tiene muchos alumnos (N:N).

### Opciones Analizadas

#### ❌ Opción A: Master-Detail Directo
*   **Concepto**: Poner un campo `Materia__c` en el objeto Alumno.
*   **Problema**: Un alumno solo podría cursar UNA materia a la vez. No escala.

#### ❌ Opción B: Multi-Select Picklist
*   **Concepto**: Una lista desplegable en Alumno con las materias.
*   **Problema**: Pesadilla de reportes. No permite guardar "Nota" ni "Estado" por materia. Límites de caracteres.

#### ✅ Opción C: Junction Object (`Inscripcion__c`)
*   **Concepto**: Crear un tercer objeto que tenga dos Master-Details (uno a Alumno, uno a Materia).
*   **Ventajas**:
    *   Permite atributos propios de la relación ("Nota Final", "Fecha Inscripción").
    *   Integridad referencial total (si borras al alumno, se borran sus inscripciones).
    *   Reportes nativos "Alumnos con Inscripciones y Materias".
*   **Decisión**: APROBADA.

---

## 🔬 Investigación 2: Validación de Integridad de Datos

### Contexto
Evitar "Data Pollution" (basura en la base de datos) desde el día 1.

### Estrategia: "Swiss Cheese Model" (Capas de defensa)

1.  **Capa 1: UI (Page Layouts)**
    *   Marcar campos como Required en la pantalla.
    *   *Debilidad*: Se puede saltar por API/Data Loader.

2.  **Capa 2: Metadata (Schema)**
    *   Marcar campos como `Required` y `Unique` a nivel definición de objeto.
    *   *Fortaleza*: Inviolable. Si no hay DNI, no hay registro.

3.  **Capa 3: Lógica (Validation Rules)**
    *   Para reglas complejas (Rango 0-10, Regex de Email).
    *   *Decisión*: Implementar VRs para todo lo que no sea binario.

---

## 🔬 Investigación 3: Naming Conventions

Para mantener el orden en una Org que crecerá:
*   **Objetos**: Singular, PascalCase (`Alumno__c`, no `Alumnos__c`).
*   **Campos**: Explícitos (`Fecha_Nacimiento__c`, no `Fecha__c`).
*   **Triggers**: `ObjetoTrigger` (e.g., `AlumnoTrigger`).

# 06-Investigaciones.md - Análisis de Arquitectura

**Proyecto**: Universidad Lumina Tech
**Responsable**: Salesforce Consultant
**Fecha**: 19 Enero 2026

---

## 🔬 Investigación 1: Modelado de Inscripciones (Muchos a Muchos)

### ❓ El Problema
Un `Alumno` puede cursar muchas `Materias`. Una `Materia` tiene muchos `Alumnos`.
Salesforce no tiene una relación "Many-to-Many" directa.

### 🧪 Alternativas Evaluadas

#### Opción A: Lookup en Alumno
- Crear campo `Materia__c` en Objeto Alumno.
- **Pros**: Fácil de hacer.
- **Contras**: Un alumno solo podría cursar UNA materia a la vez. **Inviable**.

#### Opción B: Multi-Select Picklist
- Crear picklist "Materias Cursadas" en Alumno.
- **Pros**: Rápido.
- **Contras**: No se puede guardar nota, ni estado, ni fecha. Límite de 100 valores. Reportes imposibles. **Descartado**.

#### Opción C: Objeto de Unión (Junction Object) 🏆
- Crear objeto custom `Inscripcion__c`.
- Master-Detail a `Alumno__c`.
- Master-Detail a `Materia__c`.
- **Pros**:
    - Permite guardar atributos de la relación (`Nota_Final`, `Estado`, `Ciclo`).
    - Permite "Cascade Delete" (si borro Alumno, se borran sus inscripciones).
    - Reportes nativos "Alumnos con Inscripciones con Materias".
- **Contras**: Requiere crear un objeto extra.

### ✅ Decisión Final
Implementar **Opción C**. Es el estándar de arquitectura Salesforce para este caso de uso.

---

## 🔬 Investigación 2: Seguridad de Notas (FLS vs Page Layouts)

### ❓ El Problema
El Administrativo debe poder ver los datos del alumno, pero **NO** debe poder editar las notas de los exámenes.

### 🧪 Alternativas Evaluadas

#### Opción A: Page Layouts (Solo visual)
- Crear un Layout "Admin" y poner el campo Nota como "Read-Only" en la UI.
- **Riesgo**: Si el admin sabe usar Data Loader o API, puede editar la nota igual. Es inseguro a nivel backend.

#### Opción B: Validation Rule
- Regla: `AND($Profile.Name = "Administrativo", ISCHANGED(Nota__c))`.
- **Pros**: Funciona en backend.
- **Contras**: El usuario se entera que no puede editar *después* de intentar guardar (mala UX).

#### Opción C: Field Level Security (FLS) 🏆
- Quitar permiso "Edit" al perfil Administrativo a nivel de metadatos.
- **Pros**: El campo aparece grisado o invisible en todos lados (UI, API, Reportes). Es la seguridad más robusta.

### ✅ Decisión Final
Usar **Field Level Security (FLS)** como mecanismo principal.
Opción C es la práctica recomendada de seguridad ("Defense in Depth").

---

## 🔬 Investigación 3: Validación de Datos (Email)

### ❓ El Problema
Necesitamos asegurar que el campo `Email__c` en Alumno tenga formato válido, pero sin escribir código complejo (Apex) si es evitable.

### 🧪 Alternativas Evaluadas

#### Opción A: Campo tipo "Email" Estándar
- Crear campo `Email__c` seleccionando el tipo "Email".
- **Pros**: Validación nativa de Salesforce.
- **Contras**: La validación es muy laxa (acepta `a@b`). No previene dominios falsos.

#### Opción B: Regla de Validación (Regex) 🏆
- Usar función `REGEX(Email__c, "[a-zA-Z0-9._-]+@[a-z]+\\.edu")`.
- **Pros**:
    - Control total del patrón.
    - Mensaje de error personalizado en UI.
    - Funciona en cargas masivas (Data Loader).
- **Contras**: Requiere saber sintaxis Regex.

#### Opción C: Trigger Apex (before insert/update)
- Escribir clase Apex que parsee el string.
- **Pros**: Lógica infinita (podría verificar si el dominio existe via API).
- **Contras**: Code maintenance. Requiere Test Class coverage. Overkill para este sprint.

### ✅ Decisión Final
Implementar **Opción B (Regex Validation Rule)**.
Es el balance perfecto entre robustez y mantenibilidad (Low Code).

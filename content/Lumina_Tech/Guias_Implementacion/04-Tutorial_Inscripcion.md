# 🎓 Guía Técnica: Objeto Inscripción (Junction)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-003 (Historial Académico)

---

## 🎯 Objetivo
Relacionar "Muchos Alumnos" con "Muchas Materias" mediante un objeto intermedio (Junction Object).

## 🛠️ Procedimiento

### Paso 1: Crear el Objeto Conector
1.  **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  Definición:
    *   **Label**: `Inscripción`
    *   **Plural Label**: `Inscripciones`
    *   **Record Name**: `ID Inscripción`
    *   **Data Type**: **Auto Number** (`INS-{000000}`)
3.  **Save**.

### Paso 2: Crear Pata 1 (Hacia Alumno)
1.  **Fields & Relationships** > **New**.
2.  Tipo: **Master-Detail Relationship**.
3.  Related To: **Alumno**.
4.  Label: `Alumno`.
5.  **Next** > **Next** > **Save & New**.

### Paso 3: Crear Pata 2 (Hacia Materia)
1.  Tipo: **Master-Detail Relationship**.
2.  Related To: **Materia**.
3.  Label: `Materia`.
4.  **Next** > **Next** > **Save**.

### Paso 4: Crear Atributos de la Relación (Estado)
1.  **New** > Tipo: **Picklist**.
2.  Label: `Estado`.
3.  Valores (Enter values manually):
    *   Cursando
    *   Aprobado
    *   Desaprobado
4.  **Use first value as default**: ☑️ (Cursando).
5.  **Next** > **Save**.

---

## 🚀 Resultado Final (Efecto Many-to-Many)
Ahora, si vas al registro de un **Alumno**, verás una lista relacionada "Inscripciones".
Si vas al registro de una **Materia**, verás una lista relacionada "Inscripciones".

Esto permite que:
*   Juan curse Matemática.
*   Juan curse Historia.
*   María curse Matemática.

¡Has creado una arquitectura escalable! 🏛️

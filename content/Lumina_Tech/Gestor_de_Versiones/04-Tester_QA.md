# 04-Tester_QA.md - Plan de Pruebas y Resultados

**Proyecto**: Universidad Lumina Tech
**Responsable**: QA Team (Estudiantes 3 & 4)
**Ciclo**: Sprint 1

---

## 🧪 Estrategia de Pruebas
El objetivo es validar que las restricciones de seguridad y calidad de datos funcionan ANTES de pasar a Producción.

### Test Suite 1: Seguridad (Perfiles)

#### TC-SEC-01: Privacidad de Notas (Administrativo)
*   **Pre-condición**: Existir un Examen con Nota 8.
*   **Actor**: Usuario con perfil `Lumina_Administrativo`.
*   **Pasos**:
    1.  Loguear como Administrativo.
    2.  Navegar al registro del Examen.
    3.  Intentar editar el campo `Nota`.
*   **Resultado Esperado**: El campo aparece como texto plano (sin lápiz de edición) o arroja error "Insufficient Privileges".
*   **Status**: ⚪ Pending

#### TC-SEC-02: Visibilidad de Alumnos (Profesor)
*   **Pre-condición**: OWD Alumno = Private.
*   **Actor**: Usuario con perfil `Lumina_Profesor` (Profesor A).
*   **Pasos**:
    1.  Loguear como Profesor A.
    2.  Ir a tab "Alumnos".
    3.  Seleccionar vista "All Records".
*   **Resultado Esperado**: Solo debe ver los alumnos que están inscritos en SUS materias (o ninguno si no se corrió Sharing Rule). NO debe ver a todos los alumnos de la universidad.
*   **Status**: ⚪ Pending

---

### Test Suite 2: Calidad de Datos (Validaciones)

#### TC-DATA-01: Rango de Notas Invalido (Superior)
*   **Actor**: Profesor.
*   **Pasos**:
    1.  Crear nuevo examen.
    2.  Ingresar Nota = `11`.
    3.  Guardar.
*   **Resultado Esperado**: Error en pantalla: "La nota debe ser un valor entre 0 y 10". No guarda.
*   **Status**: ⚪ Pending

#### TC-DATA-02: Rango de Notas Invalido (Negativo)
*   **Actor**: Profesor.
*   **Pasos**:
    1.  Crear nuevo examen.
    2.  Ingresar Nota = `-5`.
    3.  Guardar.
*   **Resultado Esperado**: Error en pantalla: "La nota debe ser un valor entre 0 y 10". No guarda.
*   **Status**: ⚪ Pending

#### TC-DATA-03: Integridad de DNI
*   **Actor**: Admin.
*   **Pasos**:
    1.  Crear Alumno A con DNI "123".
    2.  Crear Alumno B con DNI "123".
*   **Resultado Esperado**: Error de duplicado al guardar el segundo registro.
*   **Status**: ⚪ Pending

#### TC-DATA-04: Formato de Email (Sintaxis)
*   **Actor**: Admin/Profesor.
*   **Pasos**:
    1.  Intentar crear un alumno con Email = `juan,perez@gmail`.
    2.  Intentar con Email = `usuario_sin_arroba`.
    3.  Intentar con Email = `correcto@lumina.edu`.
*   **Resultado Esperado**:
    *   Casos 1 y 2: Bloqueo de guardado con mensaje "Formato inválido".
    *   Caso 3: Guardado exitoso.
*   **Status**: ⚪ Pending

---

## 🐞 Reporte de Defectos (Bugs)

| ID | Título | Severidad | Estado |
|----|--------|-----------|--------|
| BUG-001 | (Ejemplo) El mensaje de error de Nota está en inglés | Baja | Open |


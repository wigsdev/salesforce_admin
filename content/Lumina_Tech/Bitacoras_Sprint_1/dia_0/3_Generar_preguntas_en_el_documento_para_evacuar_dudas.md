# 📝 Tarea: Generar preguntas en el documento para evacuar dudas

**Fuente**: [05-Preguntas_y_Dudas.md](../../Gestor_de_Versiones/05-Preguntas_y_Dudas.md)
**Fecha de Análisis**: 20 Enero 2026 (Sprint 1)

## Análisis Técnico-Funcional (Simulación Real)

Este documento registra el proceso mental y diálogo entre el **Business Analyst (BA)** y el **Salesforce Consultant** tras la entrevista con el cliente (Dra. Vance).

---

### 1. Dilema de Arquitectura: "Materias Compartidas"
**🙋‍♂️ Pregunta del BA**: Dra. Vance, notamos que "Matemática 1" se dicta tanto en Ingeniería como en Administración. ¿Es la misma materia o son distintas?
*   **Respuesta Cliente**: "Es el mismo contenido y el mismo profesor."

**🏗️ Análisis del Consultant (Escenario Real)**:
*   *Situación*: Si usamos un solo registro de `Materia` ("Matemática 1"), y queremos cumplir con la **Privacidad Estricta** (que el profesor de Administración no vea alumnos de Ingeniería), la seguridad se complica.
*   *Problema*: Las reglas de compartición (Sharing Rules) estándar funcionan mejor cuando los datos están segmentados claramente.
*   *Decisión de Arquitectura (ADR-Sprint1)*: Para el MVP, **duplicaremos la materia** (`Matemática 1 - ING` y `Matemática 1 - ADM`).
*   *Justificación*: Permite asignar el registro de materia a una "Carrera" específica y simplifica el modelo de seguridad OWD Private sin requerir Apex Managed Sharing complejo en esta etapa.

### 2. Integridad de Datos: "Historial de Cursada"
**🙋‍♂️ Pregunta del BA**: ¿Qué sucede si un alumno recursa?
*   **Respuesta Cliente**: "Necesito ver todo el historial, no sobrescribir."

**🏗️ Análisis del Consultant**:
*   *Impacto en Diseño*: No podemos usar un campo "Nota" en el objeto Alumno o Materia directamente.
*   *Solución*: Se confirma la necesidad de un **Junction Object** (`Inscripción`) con clave compuesta lógica: `Alumno + Materia + Ciclo Lectivo`.
*   *Validación*: Esto permite que Juan Perez tenga "Matemática 1" en 2025 (Reprobado) y "Matemática 1" en 2026 (Cursando).

### 3. Calidad de Datos: "Formato de Notas"
**🙋‍♂️ Pregunta del BA**: ¿Las notas son enteros (1-10) o decimales?
*   **Respuesta Cliente**: "Decimales, ejemplo 7.50."

**🏗️ Análisis del Admin/Consultant**:
*   *Configuración*: Campo tipo `Number(4, 2)`.
*   *Riesgo*: Si usáramos Currency o Percent, confundiría al usuario.
*   *Validación*: Regla de validación `Nota <= 10.00` y `Nota >= 1.00`.

### 4. Identificadores Únicos
**🙋‍♂️ Pregunta del BA**: ¿Quién define el Legajo?
*   **Respuesta Cliente**: "Que el sistema lo genere."

**🏗️ Análisis del Consultant**:
*   *Solución*: Campo **Auto-Number** `A-{YYYY}-{0000}`.
*   *Justificación*: Garantiza unicidad absoluta e inmutable, sirviendo como `External ID` eficiente para cargas masivas (Data Import).

---
**Conclusión para el Día 1**:
El equipo de desarrollo tiene luz verde para crear el modelo con **Inscripción** como objeto central y **Alumnos** con Legajo autogenerado. Se asume duplicidad controlada de Materias por Carrera para robustecer la seguridad.

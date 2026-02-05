# 05-Preguntas_y_Dudas.md - Bitácora de Consultoría
**Rol**: Business Analyst / Consultant
**Estado**: 🟢 Resuelto con Cliente

---

## 🏛️ Respuestas Oficiales (Base: Equipo 3)
**De**: Dra. Elena Vance (Rectora Lumina Tech)
**Para**: Equipo 3

*"Estimados del Equipo 3, qué buenas preguntas. Van directo al hueso de la operación diaria. Aquí tienen mis definiciones:*

### 1. ¿Puede un alumno cursar la misma materia dos veces? (Recursantes)
**¡Absolutamente SÍ!** Lamentablemente, no todos aprueban a la primera.

*   **El Requerimiento**: Necesito que el sistema permita que 'Juan' se anote en 'Matemática' en el primer cuatrimestre y le vaya mal (o abandone). Y que al cuatrimestre siguiente, se pueda volver a anotar en la misma materia para intentarlo de nuevo.
*   **La Restricción**: Lo que NO puede pasar es que esté anotado dos veces en la misma materia en el mismo cuatrimestre. (No puede estar en la clase de la mañana y en la de la noche a la vez). Pero si es en fechas distintas, sí. El sistema debe guardar todo su historial: las veces que le fue mal y la vez que finalmente aprobó.

### 2. Sobre los "Problemas Legales" (Seguridad)
Cuando hablo de problemas legales, me refiero principalmente a **Riesgos Internos (Auditoría y Privacidad)**.

*   No tengo miedo de que nos hackee la NASA. Tengo miedo de que un administrativo, por error o mala fe, cambie una nota de un '2' a un '9' sin que quede rastro. Eso es fraude académico.
*   También me refiero a la **Privacidad de Datos**: Un profesor de Derecho no tiene por qué ver el DNI, la dirección o el teléfono de una alumna de Ingeniería que no es su alumna. Si esos datos se filtran, la responsabilidad es nuestra.

### 3. ¿DNI o Código Único?
**¡Necesito los dos!**

*   **El DNI**: Es obligatorio porque es el documento nacional. Nos sirve para asegurarnos de que es una persona real y única (no puedo tener dos alumnos con el mismo DNI).
*   **El Legajo (Código de Alumno)**: Nosotros usamos un número interno (ej: A-2025-001). Quiero que el sistema genere o me deje cargar ese número, porque es el que usamos para los expedientes físicos.
*   **Resumen**: Usen el DNI para validar que no existan duplicados, pero el 'Legajo' es el número con el que identificamos al alumno en la universidad.

### 4. Decimales en las notas
Sí. Utilizamos escala del 1 al 10, pero con centésimos si hace falta.
*   Ejemplo válido: `7.50`
*   Ejemplo válido: `6.33`
*   Asegúrense de que el sistema soporte hasta 2 decimales."

---

## 🏛️ Respuestas Oficiales (Complemento: Equipo 6)
**De**: Dra. Elena Vance (Rectora Lumina Tech)
**Para**: Equipo 6

*"Estimados, gracias por las preguntas puntuales. Me sirve mucho que aclaremos esto ahora antes de configurar nada. Vamos punto por punto:*

### 5. Sistema de Calificación (Notas) - Aclaración
Aquí en Lumina Tech somos exigentes pero tradicionales.
*   **Escala**: Usamos una escala numérica del **1 al 10**. (Corrección sobre el 0-10 anterior).
*   **Decimales**: Sí, permitimos hasta 2 decimales (ejemplo: 7.50).
*   **Aprobación**: Se aprueba la cursada con **6 (seis)** o más.
*   **Requerimiento**: Necesito que el sistema no permita cargar notas menores a 1 ni mayores a 10. Si un profesor intenta poner un 11 o un -5, quiero que les aparezca un error en rojo gigante.

### 6. Régimen de Asistencias
La presencialidad es fundamental para nosotros.
*   **Mínimo**: El alumno debe cumplir con el **75% de asistencia** sobre el total de clases dadas en el cuatrimestre.
*   **Sanción**: No cobramos multas ni nada por el estilo. La sanción es Académica.
    *   Si el alumno tiene menos del 75%, pierde la condición de 'Regular' y pasa a estado **'Libre'**.
    *   Esto significa que reprueba la cursada y tiene que volver a inscribirse el año que viene (Recursar). Necesito que el sistema calcule esto automáticamente si es posible, o que al menos nos alerte.

### 7. ¡Cuidado con el término "Comisiones"! (Aclaración Vital)
Aquí creo que hubo una confusión de términos. Cuando dije 'Comisiones', NO me refiero a dinero, ni a pagos, ni a porcentajes de venta. ¡Por favor no mezclen las finanzas aquí!
*   **Definición**: En el mundo universitario, una 'Comisión' es un **Curso o Grupo de alumnos**.
    *   *Ejemplo*: La materia 'Matemática I' tiene 100 inscritos. No entran todos en un aula. Entonces abrimos la 'Comisión A' (Turno Mañana) y la 'Comisión B' (Turno Noche).
*   **Seguridad**: Cuando digo que 'El profesor solo debe ver sus comisiones', me refiero a que si yo dicto clases en el Turno Mañana (Comisión A), no debo poder ver ni editar las notas de los alumnos del Turno Noche (Comisión B), aunque la materia se llame igual.

Espero haber aclarado el pánico financiero. Avancen con estos parámetros.
---

## 🛠️ NOTA TÉCNICA (Especificaciones Consolidadas)

### 1. Modelo de Datos (Data Model)
*   **Identidad Estudiante**:
    *   **DNI**: `Text(Unique, External ID)`. Validación dura de duplicados.
    *   **Legajo**: `Auto-Number` (ej. A-2025-001). Identificador interno para expedientes.
*   **Gestión de Recursantes**:
    *   **Desafío**: Permitir múltiples inscripciones a la misma materia (historial).
    *   **Restricción**: No permitir duplicados en el *mismo* cuatrimestre.
    *   **Solución**: Junction Object `Enrollment` con llave compuesta: `Student + Subject + Cycle`.

### 2. Seguridad y Auditoría (Security)
*   **Integridad de Notas**:
    *   Activar **Field History Tracking** en `Final_Grade__c` obligatoriamente.
*   **Privacidad (FLS)**:
    *   Profesor solo ve datos académicos. Ocultar DNI/Teléfono/Dirección a perfiles docentes ajenos.
*   **Visibilidad de Comisiones (OWD)**:
    *   **Definición**: Comisión = Instancia de materia (Turno/Grupo).
    *   **Configuración**: `Enrollment` y `Course` deben ser **Private**.
    *   **Acceso**: Usar Criteria-Based Sharing Rules o asignar Owner para que el profesor solo vea *sus* registros. (Si no hay objeto Comisión, cada registro de Materia debe tener un Owner profesor distinto).

### 3. Calidad de Datos (Validation Rules)
*   **Rango de Calificación**:
    *   Escala 1 a 10.
    *   **Rule Name**: `Grade_Range_1_10`
    *   **Fórmula**: `Final_Grade__c < 1 || Final_Grade__c > 10`
*   **Precisión**:
    *   Campo `Number(4, 2)` (Soporta 7.50, 6.33).

### 4. Automatización (Process/Flow)
*   **Lógica de Asistencia**:
    *   Requisito: 75% mínimo para Regularidad.
    *   **Implementación**: `Roll-Up Summary` (Máster-Detail) contando "Clases Totales" vs "Clases Presente".
    *   **Estado**: Campo fórmula "Semáforo" o Flow que marque status "Libre" si `(Presentes / Totales) < 0.75`.

---

## 📝 Dudas Pendientes (Nuevas)
8.  **Volumen de Datos**: ¿Cuántas comisiones tienen por año estimado? (Para sizing).
9.  ¿Necesitamos migrar datos históricos de Excel? (Sprint 2).
10. ¿Se integrará con algún sistema contable para las cuotas? (Sprint 3).

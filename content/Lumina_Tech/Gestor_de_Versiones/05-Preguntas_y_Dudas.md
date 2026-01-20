# 05-Preguntas_y_Dudas.md - Log de Comunicación con Cliente

**Interlocutor**: Dra. Elena Vance (Rectora)
**Estado**: 🟢 Dudas Críticas Resueltas

---

## ❓ Historial de Consultas - Sprint 1

### Bloque 1: Estructura de Cursada
**Fecha**: 20 Enero 2026

*   **P1: ¿Una misma materia se dicta en varias carreras?**
    *   *Contexto*: "Matemática 1" en Ingeniería vs Administración.
    *   *R (Dra. Vance)*: "Sí, es el mismo contenido y el mismo profesor."
    *   *Impacto*: `Materia__c` no debería ser hijo exclusivo de `Carrera__c`. Pero para Sprint 1 (MVP), asumiremos que se crean duplicadas ("Matemática Ing", "Matemática Adm") para simplificar la seguridad.

*   **P2: ¿Qué pasa si un alumno recursa?**
    *   *Contexto*: ¿Se sobrescribe la inscripción vieja?
    *   *R (Dra. Vance)*: "No, necesito ver el historial. Que cursó en 2025 y quedó libre, y volvió a cursar en 2026."
    *   *Impacto*: El ID de la inscripción es el `Ciclo_Lectivo`. Un alumno puede tener N inscripciones a la misma materia si son ciclos distintos.

---

### Bloque 2: Calificaciones
**Fecha**: 21 Enero 2026

*   **P3: ¿Las notas son números enteros o decimales?**
    *   *Contexto*: Configuración del campo Number.
    *   *R*: "Dos decimales. Ejemplo: 7.50, 6.33."
    *   *Acción*: Campo `Number(2, 2)`.

*   **P4: ¿Cuál es la nota mínima de aprobación?**
    *   *Contexto*: Para flujos automáticos.
    *   *R*: "Se aprueba con 4 (cuatro). Menos de eso es desaprobado."
    *   *Acción*: Validation Rule / Formula Field `Estado_Aprobacion`.

---

### Bloque 3: Datos de Personas
**Fecha**: 22 Enero 2026

*   **P5: ¿El Legajo lo generan ustedes o Salesforce?**
    *   *Contexto*: Campo Auto-Number vs Text.
    *   *R*: "Que el sistema genere uno nuevo. Formato `L-0000`."
    *   *Acción*: Auto-Number field.

*   **P6: ¿Email Personal o Institucional?**
    *   *R*: "Por ahora usen el personal (Gmail/Hotmail), no tenemos dominio educativo implementado para alumnos aún."
    *   *Acción*: No restringir dominio en la validación de Email, solo formato.

---

## ⏳ Dudas Pendientes (Sprint 2)
1.  ¿Necesitan portal de autogestión para que los alumnos se anoten solos? (Autoservicio).
2.  ¿Cómo manejamos las inasistencias? ¿Diarias o por porcentaje?

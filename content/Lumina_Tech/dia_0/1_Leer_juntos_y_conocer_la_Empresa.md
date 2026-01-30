# 📝 Tarea: Leer juntos y conocer la Empresa

**Fuentes**: 
*   [Solicitud.md](../../Solicitud.md)
*   [SPRINT 1.md](../../SPRINT%201.md)

## 1. Análisis de Dolores (Pain Points)
1.  **Administración Caótica**: Hojas de cálculo rotas.
2.  **Falta de Privacidad**: Profesores viendo datos de otras carreras.
3.  **Riesgo Legal**: Administrativos editando notas cerradas.
4.  **Mala Calidad de Datos**: Emails inválidos y notas ilógicas.

---

## 2. Listado de Requerimientos Detallado (Backlog)

### 👮 Seguridad y Perfiles (Security)
*   **[REQ-SEC-001] Perfiles de Usuario**: El sistema debe distinguir entre "Equipo Administración", "Profesores" y "Directores/Rectora".
*   **[REQ-SEC-002] Privacidad Cruzada (Zero Trust)**: Un profesor NO debe poder ver datos de alumnos que no estén en su cátedra.
*   **[REQ-SEC-003] Protección de Calificaciones**: El equipo Administrativo debe ver datos de contacto pero tener **prohibido** editar campos de notas.

### 🏛️ Arquitectura Académica (Data Model)
*   **[REQ-DATA-001] Entidades Core**: El sistema debe gestionar "Carreras" y "Materias" como activos de la universidad.
*   **[REQ-DATA-002] Historial Académico (M:N)**: Un Alumno cursa muchas materias y una Materia tiene muchos alumnos. Se debe preservar el historial de intentos pasados.

### 💎 Calidad de Datos (Data Quality)
*   **[REQ-QUAL-001] Validación de Contacto**: El sistema debe rechazar emails con formatos inválidos (ej. comas en vez de puntos).
*   **[REQ-QUAL-002] Consistencia de Notas**: El sistema debe impedir guardar notas fuera del rango 1.00 a 10.00.
*   **[REQ-QUAL-003] Identidad Obligatoria**: No se puede crear un legajo de alumno sin su DNI/Cédula.

### ⚙️ Funcionalidad Operativa (Business Logic)
*   **[REQ-FUNC-001] Ciclo de Exámenes**: Registro de fechas y notas de Parciales/Finales.
*   **[REQ-FUNC-002] Registro de Asistencia**: Dejar constancia si el alumno "Faltó" a un examen.

---

## 3. Estrategia del Sprint 1
*   **Foco**: Resolver REQ-SEC (Seguridad) y REQ-DATA (Estructura) primero. Sin esto, la app no es viable.

---
**Responsables**: 🕵️ **Business Analyst**, 👑 **Product Owner**.

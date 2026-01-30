# 05-Preguntas_y_Dudas.md - Bitácora de Consultoría
**Rol**: Business Analyst / Consultant
**Estado**: 🟢 Resuelto

---

## ❓ Sesión 1: Entendimiento del Negocio (Kick-off)
**Fecha**: 15/01/2026
**Interlocutor**: Dra. Vance (Rectora)

### Q1: Estructura de Cursada
*   **Pregunta**: *¿Un alumno puede cursar la misma materia más de una vez? (Recursantes)*
*   **Respuesta Cliente**: *"Sí, lamentablemente muchos recursan. Necesito ver el historial completo, no solo la última nota."*
*   **Impacto Técnica**: Descarta relación Directa (Lookup). Confirma necesidad de **Junction Object** (`Inscripcion__c`) para manejar múltiples registros por par Alumno-Materia.

### Q2: Seguridad de Calificaciones
*   **Pregunta**: *Usted mencionó "problemas legales". ¿Se refiere a acceso externo o interno?*
*   **Respuesta Cliente**: *"Interno. Tuvimos un caso de un administrativo que 'vendía' notas. Necesito que solo los profesores puedan poner la nota final."*
*   **Impacto Técnica**: Requiere **Field-Level Security (FLS)**. El perfil `Admin` debe tener Read-Only en `Nota__c`.

---

## ❓ Sesión 2: Definiciones de Datos
**Fecha**: 20/01/2026
**Interlocutor**: Director de Carreras

### Q3: Identificación de Alumnos
*   **Pregunta**: *¿Usamos DNI o generamos un Legajo interno?*
*   **Respuesta Cliente**: *"El DNI es obligatorio por ley, pero el Legajo es lo que usamos en el día a día."*
*   **Impacto Técnica**:
    *   `DNI__c`: Campo Texto (Unique, External ID).
    *   `Name` (del objeto Alumno): Auto-Number formato `A-{00000}` (Legajo).

### Q4: Escala de Notas
*   **Pregunta**: *¿Usan decimales? ¿0 a 10 o 1 a 100?*
*   **Respuesta Cliente**: *"0 a 10, con dos decimales. Se aprueba con 4."*
*   **Impacto Técnica**: Campo `Number(2, 2)`. Validation Rule para rango `0.00 - 10.00`.

---

## 📝 Dudas Pendientes (Parking Lot)
1.  ¿Necesitamos migrar datos históricos de Excel? (Sprint 2).
2.  ¿Se integrará con algún sistema contable para las cuotas? (Sprint 3).

# SPRINT 1: Fundamentos Académicos y Seguridad

## 📋 Ficha Técnica
*   **Proyecto**: Universidad Lumina Tech
*   **Sprint Goal**: Implementar el núcleo académico (Carrera-Materia-Alumno) y asegurar que las notas sean inviolables.
*   **Estado**: 🟢 En Curso (Semana 4 - Cierre)
*   **Total Story Points**: 13 SP

---

## 📅 Sprint Backlog y Estimación

| ID | Historia de Usuario | Story Points | Responsable | Estado |
|----|---------------------|--------------|-------------|--------|
| **HU-001** | Visibilidad de Profesores (Seguridad) | 3 | Admin 1 | ✅ Done |
| **HU-002** | Restricción Edición Notas (Admin) | 3 | Admin 2 | ✅ Done |
| **HU-003** | Historial Académico (Inscripciones) | 5 | Admin 1 | ✅ Done |
| **HU-006** | Integridad de Notas (Validaciones) | 2 | Admin 2 | ✅ Done |

---

## 🏗️ Definition of Done (DoD)
Para dar por cerrada una Historia de Usuario, debe cumplir:
1.  [x] **Configuración**: Objetos y campos creados en DEV.
2.  [x] **Seguridad**: Perfiles y OWD configurados según [02-Consultant](02-Salesforce_Consultant.md).
3.  [x] **Documentación**: Pasos registrados en [03-Admin](03-Salesforce_Admin.md).
4.  [x] **Testing**: TC ejecutado y aprobado en [04-QA](04-Tester_QA.md).
5.  [ ] **Deployment**: Desplegado a PROD (Pendiente para Viernes).

---

## 📝 Bitácora Diaria (Daily Standups)

### Daily #1 - Inicio (Lunes, Semana 2)
*   **Equipo**: Todos presentes.
*   **Updates**:
    *   *BA*: Requerimientos cerrados con la Dra. Vance.
    *   *Consultant*: Decidimos ir con Junction Object (Inscripción).
*   **Blockers**: Ninguno.

### Daily #5 - Mitad de Sprint (Viernes, Semana 2)
*   **Admin 1**: Terminé creación de objetos Carrera y Materia. Luchando con Master-Detail en Inscripción.
*   **Admin 2**: Configurando perfiles. Duda: ¿El preceptor es "Admin" o "Profesor"? -> *R: Admin*.
*   **Consultant**: Ayudando a Admin 1 con el reparenting.

### Daily #10 - Cierre (Miércoles, Semana 3)
*   **QA Team**: Terminamos pruebas de seguridad. Encontramos BUG-001 (Error mensaje en inglés).
*   **Admin 2**: Fixeando el BUG-001 ahora mismo (Traduar Custom Label).
*   **Scrum Master**: Preparando la demo para el viernes.

---

## 📊 Retrospectiva (Pre-llenado)
*   **Start**: Usar más herramientas de generación de data (Mockaroo) para no cargar datos a mano.
*   **Stop**: Dejar la documentación para el viernes a última hora.
*   **Continue**: Las reuniones de diseño técnico antes de tocar el teclado. ¡Funcionaron genial!

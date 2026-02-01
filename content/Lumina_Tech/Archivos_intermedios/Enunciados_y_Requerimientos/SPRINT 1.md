# 🏛️ Proyecto: Universidad Lumina Tech
**Documento Maestro: Sprint 1 "Core Académico"**

**Estado**: 🟢 Aprobado para Inicio
**Referencia**: Entrevista Dra. Vance (19/01/2026)

---

## 🧭 Visión del Sprint (Business Perspective)
*Basado en el análisis de Negocio ([01-Business_Analyst.md](../../Gestor_de_Versiones/01-Business_Analyst.md))*

El objetivo de este Sprint no es solo "crear campos", es **mitigar riesgos legales y operativos** críticos para la Universidad.
1.  **Riesgo Legal**: Si un administrativo adultera una nota, la universidad puede ser demandada. 
    *   *Solución*: "Si no es tu alumno, no lo tocas." (Modelo Zero Trust).
2.  **Riesgo Operativo**: Datos basura ("gmail,com") impiden la comunicación.
    *   *Solución*: "Si el dato no es válido, no entra." (Calidad en Origen).

## 🏗️ Estrategia Técnica (Architect Perspective)
*Basado en el diseño técnico ([02-Salesforce_Consultant.md](../../Gestor_de_Versiones/02-Salesforce_Consultant.md))*

Para sostener la visión, implementaremos una arquitectura **Scalable & Secure**:
1.  **Normalización (3NF)**:
    *   `Alumno` es la entidad maestra (Golden Record).
    *   `Inscripcion` es la entidad transaccional (Junction).
    *   *Resultado*: Juan Perez se carga 1 sola vez, no 20.
2.  **Defense in Depth**:
    *   Capa 1 (UI): Page Layouts separados.
    *   Capa 2 (Schema): Validation Rules (`Nota 1-10`).
    *   Capa 3 (DB): Field-Level Security (Admin Read-Only).

## 📋 Plan de Ejecución (Admin/Agile Perspective)
*Basado en la guía de implementación ([03-Salesforce_Admin.md](../../Gestor_de_Versiones/03-Salesforce_Admin.md))*

### Backlog Priorizado
1.  **[P0] Integridad Legal (DNI/Email)**: Configurar campos `Unique` y `Required` en Alumno.
2.  **[P0] Estructura Base**: Crear Objetos `Carrera`, `Materia`, `Inscripcion`.
3.  **[P1] Motor de Seguridad**: Configurar Perfiles (Profesor/Admin) y OWD (Private).
4.  **[P1] Gestión de Exámenes**: Implementar objeto `Examen` con bloqueo de notas.

### Definition of Done (DoD)
Un ítem se considera terminado solo si:
*   [ ] El Profesor puede cargar notas corre y el Admin **NO**.
*   [ ] No se pueden ingresar notas "11" ni emails rotos.
*   [ ] Un alumno inscrito en "Matemática" aparece en los reportes de esa materia.

---
**Siguiente Paso**: Distribuir tareas en Trello según la [00-Guia_Trello_Paso_a_Paso.md](../00-Guia_Trello_Paso_a_Paso.md).
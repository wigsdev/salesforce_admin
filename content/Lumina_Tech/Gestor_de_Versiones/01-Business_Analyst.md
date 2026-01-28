# 01-Business_Analyst.md - Documento de Discovery y Análisis

**Cliente**: Universidad Lumina Tech
**Interlocutor**: Dra. Elena Vance (Rectora)
**Fecha de Relevamiento**: 19/01/2026
**Rol Analista**: Senior Salesforce Business Analyst

---

## 🕵️ 1. Matriz de Trazabilidad (Discovery Matrix)

En esta sección traducimos los "dolores" literales del cliente en requerimientos funcionales formales del ecosistema Salesforce.

### Bloque A: Seguridad y Compliance ("Nuestra Gente")

| Cita Textual | Dolor / Riesgo | Requerimiento Funcional | Solución Propuesta |
|---|---|---|---|
| *"El problema es que hoy en día todos ven todo."* | **Data Leak**: Falta de segregación de datos. | Implementar un modelo de seguridad restrictivo ("Least Privilege"). | **OWD (Organization-Wide Defaults)** configurados en `Private` para Alumnos. |
| *"No quiero que un Profesor de Marketing vea notas de Ingeniería."* | **Privacidad**: Acceso cruzado no autorizado. | Los registros deben ser visibles solo por su propietario o equipo asignado. | **Sharing Rules** basadas en Criterios (Carrera) o Asignación Manual. |
| *"Si un administrativo cambia una nota, tenemos un problema legal grave."* | **Legal/Compliance**: Riesgo de fraude académico y demandas. | Segregación de funciones (SoD) a nivel de campo. Auditoría de cambios. | **Field-Level Security (FLS)**: Campo `Nota` en *Read-Only* para perfil Admin. |

### Bloque B: Arquitectura de Datos ("La Estructura")

| Cita Textual | Dolor / Riesgo | Requerimiento Funcional | Solución Propuesta |
|---|---|---|---|
| *"No quiero tener que escribir 'Juan Perez' veinte veces manuales."* | **Redundancia**: Datos duplicados e inconsistencia. | Normalización de Base de Datos. Principio "Golden Record". | Objeto Maestro `Alumno` único. Relación **Many-to-Many** con Materias. |
| *"Un alumno cursa muchas materias."* | **Escalabilidad**: El modelo plano (Excel) no soporta la realidad. | Sistema relacional capaz de manejar historia académica. | Objeto de Unión **`Inscripcion__c`** (Junction Object). |

### Bloque C: Calidad de Datos ("Calidad de Información")

| Cita Textual | Dolor / Riesgo | Requerimiento Funcional | Solución Propuesta |
|---|---|---|---|
| *"Escribió 'gmail,com' con coma... y rebotó."* | **Operativo**: Fallo en comunicaciones críticas. | Validación de formato (Syntactic Validation) en punto de entrada. | Campo tipo **Email** (valida @ y dominio) + Regex si es necesario. |
| *"Un profesor tipeó mal y le puso '11' o '-5'."* | **Integridad**: Corrupción de estadísticas y promedios. | Validación lógica de rango numérico (Business Logic Validation). | **Validation Rule**: `OR(Nota < 0, Nota > 10)`. |
| *"No podemos inscribir si no tiene su DNI."* | **Legal**: Requisito mandatorio de matriculación. | Completitud de datos obligatorios. | Campo `DNI` marcado como **Required** en el Schema. |

---

## 📝 2. Definición de Perfiles (Roles)

Basado en la entrevista, identificamos los siguientes actores del sistema:

1.  **Rectora / Directores** (Stakeholders): Necesitan reportes y visión general. (Posible rol: `Read Only` o `Executive Dashboard`).
2.  **Equipo de Administración** (Operativos): Inscriben y cobran. (Rol: `Lumina_Administrativo`).
    *   *Permisos*: CRUD en Alumnos, Create en Inscripciones, **READ ONLY en Notas**.
3.  **Profesores** (Docentes): Dictan y evalúan. (Rol: `Lumina_Profesor`).
    *   *Permisos*: READ en Alumnos (Propios), **EDIT en Notas**.

---

## 🎯 3. Objetivo del MVP (Sprint 1)
*"Construir la base (...) para arrancar el primer cuatrimestre ordenados."*

El entregable mínimo viable debe permitir:
1.  Dar de alta un Alumno (con validación de DNI/Email).
2.  Inscribirlo en una Materia (`Inscripcion__c`).
3.  Que el Profesor le cargue una nota de examen (`Examen__c`).
4.  Que el Administrativo **NO** pueda cambiar esa nota.



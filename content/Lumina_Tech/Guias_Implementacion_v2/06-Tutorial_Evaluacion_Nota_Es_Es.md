# 🎓 Guía Técnica: Objeto Evaluación (Refactorizado) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Lógica de Rendimiento)
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Profesor**

---

## 🎯 Objetivo
Unificar la carga de calificaciones académicas en el objeto `Evaluacion__c`. En el Sprint 2, este objeto consolida tanto notas parciales como exámenes finales para simplificar el análisis de aprobación y optimizar el almacenamiento.

## 🛠️ Procedimiento de Configuración

### Paso 1: Configuración Inicial del Objeto
1.  **Setup** > **Object Manager** > **Evaluacion__c**.
3.  **External ID**: Cree el campo `ID_Evaluacion__c` (Texto, 80, Único y External ID) para habilitar Upsert.
4.  **Search Settings**: Asegúrese de que el objeto sea indexable por el buscador.

### Paso 2: El Vínculo con la Inscripción (Lookup)
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Lookup Relationship**.
3.  **Related To**: `Inscripcion__c`.
4.  ☑️ **Always require a value**: **OBLIGATORIO**.
5.  **Lookup Filter**: Sugerido filtrar solo por inscripciones "Activas" o del ciclo actual.

### Paso 3: Diccionario de Campos Real (Object Manager)
Asegúrese de que el objeto `Evaluacion__c` cuenta con los siguientes campos activos:

| Etiqueta (Label) | Nombre API | Tipo | Detalle / Regla |
| :--- | :--- | :--- | :--- |
| **Examen Parcial 1** | `Examen_Parcial_1__c` | Number(2, 0) | Nota del primer parcial. |
| **Examen Parcial 2** | `Examen_Parcial_2__c` | Number(2, 0) | Nota del segundo parcial. |
| **Examen Final** | `Examen_Final__c` | Number(2, 0) | Nota del examen final. |
| **Peso de Evaluación**| `Peso_de_Evaluacion__c`| Percent(3, 0) | Incidencia en el promedio final. |
| **Estado** | `Estado__c` | Picklist | **Aprobado**, **Desaprobado**. |
| **Fecha de Examen** | `Fecha_de_Examen__c` | Date | Fecha del registro. |
| **Alumno (F)** | `Alumno_F__c` | Formula (T) | `Inscripcion__r.Alumno__r.FirstName & " " & Inscripcion__r.Alumno__r.LastName` |
| **Materia (F)** | `Materia_F__c` | Formula (T) | `Inscripcion__r.Materia__r.Name` |
| **DNI** | `DNI__c` | Formula (T) | `Inscripcion__r.Alumno__r.Numero_Documento__c` |
| **Email** | `Email__c` | Formula (T) | `Inscripcion__r.Alumno__r.Email` |
| **Promedio Final** | `Promedio_Final__c` | Formula (N) | Cálculo del promedio ponderado. |
| **Condición** | `Condicion__c` | Formula (T) | (Ver lógica de escala abajo). |

> [!IMPORTANT]
> **Requerimiento Client (Sprint Review):** Los campos **DNI** y **Email** son críticos para el reporte "Alumnos Reprobados del Mes". Al ser fórmulas cruzadas, permiten que el reporte de Evaluación muestre datos del Alumno sin necesidad de un Report Type personalizado complejo.

#### 3.1 Lógica de Condición (Escala Argentina)
El campo **Condición** determina el resultado académico siguiendo la escala de calificación estándar:
- **Formula**:
    ```sql
    IF(Promedio_Final__c >= 9, "Sobresaliente",
       IF(Promedio_Final__c >= 7, "Distinguido",
          IF(Promedio_Final__c >= 4, "Aprobado", "Desaprobado")
       )
    )
    ```

---

## 🚀 Estrategia de Carga (Sprint 2)
Al importar Evaluaciones (CSV-04):
1.  **Clave de Cruce (Parent)**: Use `Inscripcion__r:ID_Importacion__c` vinculando la columna `ID_Inscripcion`.
2.  **Identificador Único (Self)**: Use `ID_Evaluacion__c` como External ID (columna `ID_Evaluacion`).
3.  **Mapeo de Campos**:
    - `ID_Evaluacion` -> `ID_Evaluacion__c` (External ID)
    - `ID_Inscripcion` -> `Inscripcion__r:ID_Importacion__c`
    - `Fecha_Lista` -> `Fecha_de_Examen__c`
    - `Nota` -> `Examen_Final__c`
    - `Estado` -> `Estado__c`

## ✅ Verificación de Éxito
1.  Carga un registro con Promedio Final = 10. La condición debe ser **"Sobresaliente"**.
2.  Carga un registro con Promedio Final = 2. La condición debe ser **"Desaprobado"**.
3.  Carga un registro con Promedio Final = 7. La condición debe ser **"Distinguido"**.

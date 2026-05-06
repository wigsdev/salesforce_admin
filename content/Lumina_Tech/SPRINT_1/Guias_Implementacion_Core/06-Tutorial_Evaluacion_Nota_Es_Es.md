# 🎓 Guía Técnica: Objeto Evaluación (Gestión de Notas) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Lógica de Rendimiento) / **Refactorización G3/G6**
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Profesor**

---

## 🔍 Parte 1: Implementación Original (As-Is)

*La siguiente sección documenta el diseño original (Flattened) que agrupó las notas en un solo registro para optimizar almacenamiento.*

### 🎯 Objetivo Original
Unificar la carga de calificaciones académicas en el objeto `Evaluacion__c`. En el Sprint 2, este objeto consolida tanto notas parciales como exámenes finales para simplificar el análisis de aprobación y optimizar el almacenamiento.

### 🛠️ Procedimiento de Configuración Original

#### Paso 1: Configuración Inicial del Objeto
1.  **Setup** > **Object Manager** > **Evaluacion__c**.
2.  **External ID**: Cree el campo `ID_Evaluacion__c` (Texto, 80, Único y External ID) para habilitar Upsert.

#### Paso 2: El Vínculo con la Inscripción (Lookup)
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Lookup Relationship**.
3.  **Related To**: `Inscripcion__c`.
4.  ☑️ **Always require a value**: **OBLIGATORIO**.

#### Paso 3: Diccionario de Campos Original
| Etiqueta | Nombre API | Tipo | Detalle |
| :--- | :--- | :--- | :--- |
| **Examen Parcial 1** | `Examen_Parcial_1__c` | Number(2, 0) | Nota del primer parcial. |
| **Examen Parcial 2** | `Examen_Parcial_2__c` | Number(2, 0) | Nota del segundo parcial. |
| **Examen Final** | `Examen_Final__c` | Number(2, 0) | Nota del examen final. |
| **Estado** | `Estado__c` | Picklist | **Aprobado**, **Desaprobado**. |
| **Promedio Final** | `Promedio_Final__c` | Formula (N) | Cálculo del promedio ponderado. |
| **DNI** | `DNI__c` | Formula (T) | `Inscripcion__r.Alumno__r.Numero_Documento__c` |

## 🛠️ Parte 2: Refactorización y Mejoras (To-Be)

*Basándonos en la auditoría técnica y en discusiones arquitectónicas, el diseño original (Flattened) presenta graves limitaciones de escalabilidad. Si un profesor decide tomar un "Parcial 3" o un "Trabajo Práctico", habría que crear nuevos campos en el objeto.*

### 🚨 Diagnóstico de Arquitectura
1.  **Falta de Escalabilidad (Modelo Plano):** Almacenar todas las notas en un solo registro impide crecer. **Solución:** Pasar a un modelo relacional donde **Un Registro = Un Examen**.
2.  **Limitación de Junction Object:** La `Inscripcion__c` no puede actuar como "Master" (límite de Salesforce). **Por ende, la relación con Evaluación se mantiene como Lookup fuerte**, y los promedios se calcularán vía Flow.

### Paso 1: Reestructuración de Campos (El Nuevo Modelo Escalable)
Ejecuta las siguientes modificaciones en el Object Manager de `Evaluacion__c`:

1.  **Limpieza de Campos Antiguos:** Elimina o desactiva (si la org lo permite) los campos `Examen_Parcial_1__c`, `Examen_Parcial_2__c`, `Examen_Final__c` y `Promedio_Final__c`.
2.  **Creación del Nuevo Set Escalable:**
    *   **Tipo de Examen (Nuevo):** Tipo: **Picklist**. Name: `Tipo_Examen__c`. Valores: `Parcial 1`, `Parcial 2`, `Trabajo Práctico`, `Final`.
    *   **Calificación (Nuevo):** Tipo: **Number(2,0)**. Name: `Nota__c`.
    *   **Peso de Evaluación (Nuevo):** Tipo: **Percent(3,0)**. Name: `Peso__c`. *(Ej: 30% para Parcial 1, 70% para Final).*
    *   **Nota Ponderada (Fórmula):** Tipo: **Formula (Number)**. `Nota__c * Peso__c`.
3.  **Control de Asistencia a Examen:**
    *   Tipo: **Checkbox**. Name: `Asistio_al_Examen__c`. Default: **Checked**.

### Paso 2: Implementación de Reglas de Validación (Data Quality)
1.  Ve a **Validation Rules** > **New**.
2.  **Rule Name**: `Rango_Nota_Examen`
3.  **Error Condition Formula**: `OR(Nota__c < 0, Nota__c > 10)`
4.  **Error Message**: "Solo se aceptan notas en la escala del 0 al 10."

### Paso 3: Seguridad y Permisos (Zero Trust)
Para garantizar que nadie salvo los docentes puedan ingresar calificaciones y que nadie más pueda verlas por defecto:

1.  **Visibilidad Global (OWD)**:
    *   Ve a **Setup** > **Sharing Settings**.
    *   Establece el **Default Internal Access** de **Evaluacion__c** en **Private**.
2.  **Seguridad a Nivel de Objeto (SoD)**:
    *   Ve a **Setup** > **Profiles**.
    *   Entra al perfil **Lumina Registrar** (Personal administrativo).
    *   Ve a **Object Settings** > **Evaluaciones** y asegura que tengan permisos estrictos de **Solo Lectura (Read Only)**. No deben tener permisos de Create, Edit o Delete sobre las notas.

### Paso 4: Acumulación de Promedio en Inscripción (Flujo)
Para ver el promedio final, **se debe crear un campo en el objeto `Inscripcion__c`**:
1.  Ve a `Inscripcion__c` > Fields & Relationships > Crea `Promedio_Acumulado__c` (Number 4,2).
2.  *Nota Arquitectónica:* Ya que la relación es Lookup, se construirá un **Record-Triggered Flow** (ver Guía de Automatizaciones) que sume todas las "Notas Ponderadas" de las evaluaciones hijas y actualice este campo de la Inscripción automáticamente cada vez que un profesor ingrese una nueva nota.

---

## ✅ Verificación de Éxito de Refactorización
1.  Abre la Inscripción de un alumno.
2.  Crea un registro de Evaluación: Tipo = "Parcial 1", Nota = 8, Peso = 50%.
3.  Crea otro registro de Evaluación: Tipo = "Final", Nota = 6, Peso = 50%.
4.  Comprueba que la regla de validación impida ingresar un "11" en el campo Nota.

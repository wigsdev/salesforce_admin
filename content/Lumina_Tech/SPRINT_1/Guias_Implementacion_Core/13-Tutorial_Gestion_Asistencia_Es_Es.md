# 🎓 Guía Técnica: Gestión Masiva de Asistencia (Modelo Clase) [MODIFICADO SPRINT 2/3]

**Sprint**: 03 (Automatización y UX)
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Developer**
**HUs Relacionadas**: Asistencia Masiva (UX).

---

## 🔍 Parte 1: Implementación Original (As-Is / Sprint 1)

*En el Core (Guía 05), diseñamos el objeto Asistencia de forma transaccional. Esto significa que si un profesor tiene 40 alumnos, debe crear 40 registros de Asistencia uno por uno cada día. Esto funciona a nivel de base de datos, pero es una pesadilla de usabilidad (UX) para el docente.*

### 🎯 Objetivo de la Mejora
Implementar un modelo de "Planilla de Asistencia" (Header-Detail) donde el profesor simplemente crea una **Clase** (El Header) y el sistema (Salesforce Flow) genera automáticamente la lista de alumnos inscriptos para pasar lista fácilmente ("Presente/Ausente").

---

## 🛠️ Parte 2: Refactorización a Modelo Planilla (To-Be / Sprint 3)

### 🧩 Arquitectura Requerida
*   **Materia** (Abuelo): La asignatura (ej: Matemática).
*   **Sesión de Clase** (Padre Header - *NUEVO OBJETO*): La sesión del día (ej: Clase del 12/03).
*   **Asistencia** (Hijo Detail): El registro individual del alumno. Mantiene su Lookup hacia `Inscripción` para que las inasistencias sigan impactando en el legajo del alumno.

### Paso 1: Crear el Objeto "Sesión de Clase" (Header)
1.  Ve a **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  **Label**: `Sesión de Clase`. **Plural**: `Sesiones de Clase`. **API Name**: `Sesion_de_Clase__c`.
3.  **Record Name**: `ID Clase` (Auto Number: `CLS-{00000}`).
4.  Marca **Allow Reports**.
5.  **Save**.

### Paso 2: Relacionar Sesión con Materia
1.  En `Sesion_de_Clase__c` > **Fields & Relationships** > **New** > **Master-Detail Relationship**.
2.  Related To: **Materia**.
3.  Field Name: `Materia__c`.

### Paso 3: Campos de la Sesión de Clase
1.  **Fecha** (Date): Required. Default = `Today`. API: `Fecha__c`.
2.  **Tema Dictado** (Text 255): Opcional. API: `Tema__c`.
3.  **Estado** (Picklist): `Planificada`, `Realizada`, `Cancelada`. Default = `Planificada`. API: `Estado__c`.

### Paso 4: Ajustar el Objeto Asistencia Existente
*Para conectar la Asistencia transaccional a esta nueva Planilla.*
1.  Ve al objeto **Asistencia** (`Asistencia__c`).
2.  **Fields & Relationships** > **New** > **Master-Detail Relationship**.
    *   *Nota Arquitectónica:* Como Asistencia solo tiene un Lookup a Inscripción (por el límite del Junction Object), ¡**SÍ** podemos crearle un Master-Detail hacia Sesión de Clase!
3.  Related To: **Sesión de Clase**.
4.  Field Name: `Sesion_de_Clase__c`.

### Paso 5: Automatización "Generar Planilla" (Record-Triggered Flow)
*Cuando el profesor crea la cabecera, el Flow crea el detalle.*

1.  Ve a **Setup** > **Flows** > **New Flow** > **Record-Triggered Flow**.
2.  **Object**: `Sesion_de_Clase__c`. **Trigger**: *A record is created*.
3.  **Optimization**: *Actions and Related Records* (After Save).
4.  **Elemento Get Records**: `Obtener_Inscripciones`.
    *   Object: `Inscripcion__c`.
    *   Condition: `Materia__c` Equals `{!$Record.Materia__c}` AND `Estado__c` Equals `Activo`.
    *   Store All Records.
5.  **Elemento Loop**: `Iterar_Alumnos` (Itera sobre la colección de Inscripciones obtenida).
6.  **Elemento Assignment 1**: `Mapear_Asistencia_Individual`.
    *   Crea una variable `var_Asistencia_Individual` (Record Type: Asistencia).
    *   Asigna: `Sesion_de_Clase__c` = `{!$Record.Id}`.
    *   Asigna: `Inscripcion__c` = `{!Iterar_Alumnos.Id}`.
    *   Asigna: `Estado__c` = "Presente". *(Por defecto todos están presentes, el profesor solo marca a los ausentes).*
    *   Asigna: `Fecha__c` = `{!$Record.Fecha__c}`.
7.  **Elemento Assignment 2**: `Agregar_a_Lista`.
    *   Crea una variable `coll_Asistencias_Nuevas` (Record Collection Type: Asistencia).
    *   Action: Add `var_Asistencia_Individual` a `coll_Asistencias_Nuevas`.
8.  **Elemento Create Records**: `Insertar_Planilla_Masiva`.
    *   Crea múltiples registros usando la colección `coll_Asistencias_Nuevas`.
9.  **Save** (Nombre: `Clase: Generar Planilla Asistencias`) y **Activate**.

### Paso 6: Configuración de la Interfaz (UX del Docente)
1.  Ve a un registro de **Materia** y edita el *Page Layout*. Añade la Related List de "Sesiones de Clase".
2.  Ve a un registro de **Sesión de Clase** y edita el *Page Layout*. Añade la Related List de "Asistencias".
3.  Configura la Related List de Asistencias para que muestre las columnas: `Alumno (Fórmula)`, `Estado` y `Observaciones`.

---

## 🚀 Verificación de Éxito
1.  Entra a una Materia que tenga 3 alumnos inscriptos.
2.  Ve a la pestaña Relacionado y crea una nueva **Sesión de Clase**.
3.  Guarda el registro.
4.  Abre la Sesión de Clase recién creada. En su lista relacionada de "Asistencias", ¡deberían aparecer automáticamente los 3 alumnos marcados como "Presente"!
5.  El profesor simplemente debe editar la lista (Inline Editing) y cambiar a "Ausente" al que haya faltado.

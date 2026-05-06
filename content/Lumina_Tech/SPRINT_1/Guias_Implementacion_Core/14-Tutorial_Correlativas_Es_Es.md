# 🎓 Guía Técnica: Módulo de Correlatividades (Prerrequisitos) [MODIFICADO SPRINT 2/3]

**Sprint**: 03 (Lógica Académica Avanzada)
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Developer**
**HUs Relacionadas**: Validación de Correlativas.

---

## 🔍 Parte 1: Implementación Original (As-Is / Sprint 1)

*En la concepción original, se planteó la necesidad de impedir que un alumno se inscriba en una materia avanzada si no aprobó las anteriores (Ej: No cursar Análisis II sin Análisis I). El diseño inicial sugería crear un nuevo campo "Estado Académico" en la Inscripción para trackear esto.*

### 🎯 Objetivo Original
Construir un motor de validación que bloquee la creación de una `Inscripcion__c` si no se cumplen los requisitos previos.

---

## 🛠️ Parte 2: Refactorización y Mejoras (To-Be / Sprint 3)

*Basándonos en la refactorización del Core Académico (Sprint 2), ya contamos con el campo `Estado__c` en el objeto Inscripción (Activo, Regular, Aprobado). No necesitamos crear campos redundantes. Implementaremos la lógica apoyándonos en esta arquitectura sólida.*

### Paso 1: Crear el Objeto Conector "Correlativa"
*Este objeto actúa como el mapa de rutas de la carrera. Define qué materia bloquea a cuál.*

1.  Ve a **Setup** > **Object Manager** > **Create** > **Custom Object**.
2.  **Label**: `Correlativa`. **Plural**: `Correlativas`. **API Name**: `Correlativa__c`.
3.  **Record Name**: `ID Regla` (Tipo: Auto Number. Format: `CORR-{0000}`).
4.  **Save**.

### Paso 2: Configurar las Relaciones del Mapa
1.  **Relación 1: Materia Destino (La que el alumno quiere cursar)**
    *   Fields & Relationships > **New** > **Master-Detail Relationship**.
    *   Related To: **Materia**.
    *   Field Label: `Materia Destino`. Name: `Materia_Destino__c`.
2.  **Relación 2: Materia Requisito (La que el alumno DEBE tener)**
    *   Fields & Relationships > **New** > **Lookup Relationship** *(Debe ser Lookup para evitar referencias circulares o límites de Master)*.
    *   Related To: **Materia**.
    *   Field Label: `Materia Requisito`. Name: `Materia_Requisito__c`.
    *   ☑️ Marca "Always require a value in this field".
3.  **Tipo de Requisito (Condición)**
    *   Fields & Relationships > **New** > **Picklist**.
    *   Label: `Tipo de Requisito`. Name: `Tipo_Requisito__c`.
    *   Values: `Final Aprobado`, `Cursada Regular`.

### Paso 3: El Motor de Validación (Record-Triggered Flow)
*Sustituiremos las viejas y complejas reglas de validación (Validation Rules) por un Flow moderno que dispare un "Custom Error" antes de guardar la base de datos.*

1.  Ve a **Setup** > **Flows** > **New Flow** > **Record-Triggered Flow**.
2.  **Configuración del Trigger**:
    *   **Object**: `Inscripcion__c`.
    *   **Trigger**: *A record is created*.
    *   **Optimization**: *Fast Field Updates (Before Save)*.
3.  **Elemento Get Records 1**: `Buscar_Reglas_Correlativas`.
    *   Object: `Correlativa__c`.
    *   Condition: `Materia_Destino__c` Equals `{!$Record.Materia__c}`.
    *   *Store All Records*.
4.  **Elemento Decision**: `Tiene_Correlativas?`
    *   Valida si la colección del Get Records anterior es nula o tiene registros. Si es nula, el Flow termina (permite la inscripción).
5.  **Elemento Loop**: `Iterar_Requisitos`.
    *   Itera sobre las reglas correlativas encontradas.
6.  **Elemento Get Records 2 (Dentro del Loop)**: `Buscar_Historia_Academica`.
    *   Object: `Inscripcion__c`.
    *   Condition: `Contacto__c` Equals `{!$Record.Contacto__c}` AND `Materia__c` Equals `{!Iterar_Requisitos.Materia_Requisito__c}` AND `Estado__c` Equals `Aprobado`.
7.  **Elemento Decision (Dentro del Loop)**: `Cumple_Requisito?`
    *   Si el *Get Records 2* NO encontró nada (is Null = True), significa que le falta la materia.
    *   **Camino "Falta Materia"**: Agrega el nombre de la materia faltante a una variable de texto `var_MensajeError` y asigna `var_Falla = True`.
8.  **Elemento Custom Error (Fuera del Loop)**:
    *   Agrega un elemento **Custom Error**.
    *   Condición de ejecución: `var_Falla == True`.
    *   **Error Message**: `"No puedes inscribirte a esta materia. Te faltan las siguientes correlativas aprobadas: " + {!var_MensajeError}`.
9.  **Guarda** y **Activa** el Flow.

---

## 🚀 Verificación de Éxito
1.  Ve al catálogo y crea la materia "Matemática I" y "Matemática II".
2.  Ve al objeto **Correlativas** y crea un registro:
    *   Materia Destino: Matemática II.
    *   Materia Requisito: Matemática I.
3.  Toma a un Alumno nuevo (que no cursó nada) e intenta inscribirlo en "Matemática II".
    *   **Resultado**: El sistema debe bloquear la pantalla con un mensaje rojo que diga: ❌ *No puedes inscribirte a esta materia. Te faltan las siguientes correlativas aprobadas: Matemática I*.
4.  Inscríbelo en "Matemática I", cambia el Estado de esa inscripción a "Aprobado".
5.  Intenta inscribirlo de nuevo en "Matemática II".
    *   **Resultado**: ✅ La inscripción se guarda con éxito.

# 🎓 Guía Técnica: Objeto Materia (Catálogo) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Migración de Datos) / **Refactorización G3/G6**
**Rol Responsable**: 🛡️ **Salesforce Admin / Architect**

---

## 🔍 Parte 1: Implementación Original (As-Is)

*La siguiente sección documenta los pasos de configuración originales para mantener la trazabilidad histórica de las decisiones de diseño.*

### 🎯 Objetivo Original
Crear el objeto `Materia__c` y vincularlo fuertemente a una Carrera usando una relación **Master-Detail**. En el Sprint 2, aseguramos que la carga masiva use la **Abreviatura** de la carrera para establecer esta relación.

### 🛠️ Procedimiento Original

#### Paso 1: Configuración Inicial del Objeto
1.  Ve a **Setup** > **Object Manager**.
2.  Haz clic en **Create** > **Custom Object**.
3.  **Label**: `Materia`. **Plural Label**: `Materias`.
4.  **Object Name**: `Materia`.
5.  **Record Name**: `Nombre de Materia` (Data Type: **Text**).
6.  Marca las casillas críticas: 
    *   ☑️ **Track Field History** (Seguimiento de historial).
    *   ☑️ **Allow Search** (Permitir búsqueda) -> **[CRÍTICO]** Si no marcas esto, no aparecerá el menú de Search Layouts.
7.  Haz clic en **Save** y configura la pestaña (ej: *Books*).

#### Paso 2: Relación Maestro-Detalle (Carrera)
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Master-Detail Relationship**. Next.
3.  **Related To**: `Carrera`. Next.
4.  **Field Label/Name**: `Carrera`.
5.  ☑️ **Allow Reparenting**: **OBLIGATORIO**. Marca esta casilla (crucial para despliegues y correcciones en la carga masiva).
6.  Haz clic en **Save**.

#### Paso 3: Campos de Migración y Negocio (Antiguos)
1.  **Código Externo (External ID)**: `Codigo_Externo` (Text 20, Unique).
2.  **Código de Materia (AutoNumber)**: `MAT-{0000}`.
3.  **Créditos (Picklist)**: 1-10.
4.  **Tipo de Materia (Picklist)**: `Obligatoria`, `Electiva`.
5.  **Año del Plan (Picklist)**: 1-5.
6.  **Ciclo (Picklist)**: `CBC`, `Segundo Ciclo`, `Electivas`.

---

## 🛠️ Parte 2: Refactorización y Mejoras (To-Be)

*Basado en la auditoría de la org `LuminaRT`, el diseño original tenía problemas de escalabilidad (Ej: Créditos como lista de selección en lugar de número impide sumarizaciones futuras). A continuación, los ajustes requeridos para la arquitectura final.*

### 🚨 Diagnóstico
El esquema de `Materia__c` debe simplificarse y alinearse con la granularidad de la `Carrera__c`. Vamos a cambiar el tipo de dato de Créditos y consolidar la ubicación temporal de la materia en un solo campo (`Cuatrimestre__c`).

### Paso 1: Ajustes de Tipos de Dato
Asegúrate de que los siguientes campos existan con el tipo de dato correcto (si existen como Picklist, elimínalos y recréalos o ajusta según aplique):

1.  **Créditos Académicos (Modificación Crítica):**
    *   Tipo: **Number(2, 0)**. Name: `Creditos__c`. *(Debe ser número para permitir cálculos y fórmulas de aprobación).*
2.  **Ubicación Temporal (Reemplaza a Año y Ciclo):**
    *   Tipo: **Picklist** (o Number). Name: `Cuatrimestre__c`.
    *   Valores sugeridos: `1er Cuatrimestre`, `2do Cuatrimestre`, `3er Cuatrimestre`, etc.

### Paso 2: Nuevos Campos de Negocio
Para que la materia coincida con la modalidad de la carrera, añadiremos este campo vital:

1.  **Modalidad de Cursada:**
    *   Tipo: **Picklist**. Name: `Modalidad__c`.
    *   Valores: `Presencial`, `Virtual`, `Híbrida`.
2.  **Tipo de Materia (Se mantiene de la v1):**
    *   Tipo: **Picklist**. Name: `Tipo_Materia__c`.
    *   Valores: `Obligatoria`, `Electiva`, `Taller`.

### Paso 3: Calidad de Datos (Validation Rules)
Para evitar que se carguen materias con peso nulo, implementaremos una regla de validación estricta.

1.  En el Object Manager de `Materia__c`, ve a **Validation Rules** > **New**.
2.  **Rule Name**: `Validar_Creditos_Positivos`
3.  **Active**: ☑️ SÍ.
4.  **Error Condition Formula**:
    ```sql
    Creditos__c <= 0
    ```
5.  **Error Message**: "La materia debe tener un valor de créditos mayor a cero."
6.  **Error Location**: Selecciona el campo *Creditos*.

### Paso 4: Seguridad y Visibilidad (Zero Trust)
Para asegurar que los docentes solo vean sus materias asignadas:

1.  Ve a **Setup** > **Sharing Settings**.
2.  Haz clic en **Edit**.
3.  Busca el objeto **Materia** y configura su **Default Internal Access** a **Private**.
4.  Haz clic en **Save**.

### Paso 5: Mejora de Búsqueda (Search Layouts)
Para facilitar la vida del administrativo al inscribir alumnos, ajustaremos el buscador:
1.  Ve a **Object Manager** > **Materia** > **Search Layouts**.
2.  Edita el **Default Layout**.
3.  Añade las columnas: `Nombre de Materia`, `Carrera`, `Cuatrimestre__c` y `Modalidad__c`.
4.  Guarda.

---

## 🚀 Estrategia de Carga (Data Loader)
*   **JOIN Key**: Al importar Materias, asegúrate de mapear la columna de la carrera en el CSV contra el campo `Carrera__r:Abreviatura__c` (El External ID que creamos en el objeto Carrera).

## ✅ Verificación de Éxito de Refactorización
1.  Abre el App Launcher > **Materias**.
2.  Crea una Materia vinculada a la Carrera `Ingeniería`.
3.  Verifica que el campo "Créditos" te permita tipear un número (ej. 4) y no te obligue a elegir de una lista.
4.  Comprueba que al hacer una búsqueda (Lookup) de materias desde otra pantalla, el Search Layout te muestre en qué Cuatrimestre y Modalidad se dicta.

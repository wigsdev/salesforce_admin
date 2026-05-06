# 🎓 Guía Técnica: Objeto Carrera (Master Data) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Migración de Datos) / **Refactorización G3/G6**
**Rol Responsable**: 🛡️ **Salesforce Admin / Architect**

---

## 🔍 Parte 1: Implementación Original (As-Is)

*La siguiente sección documenta los pasos que se ejecutaron originalmente en la org. No borrar para mantener el historial de decisiones.*

### 🎯 Objetivo Original
Crear el objeto `Carrera__c` que almacenará los planes de estudio. En el Sprint 2, este objeto se refuerza con un **External ID** (`Abreviatura__c`) para permitir que las Materias e Inscripciones se vinculen masivamente sin usar Salesforce IDs.

### 🛠️ Procedimiento Original

#### Paso 1: Configuración Inicial
1.  Haz clic en el ícono de engranaje ⚙️ y selecciona **Setup**.
2.  En la pestaña **Object Manager**, haz clic en **Create** > **Custom Object**.
3.  **Label**: `Carrera`. **Plural Label**: `Carreras`.
4.  **Object Name**: `Carrera`.
5.  **Record Name**: `Nombre de Carrera` (Data Type: **Text**).
6.  En la sección "Optional Features", marca: ☑️ **Track Field History**.
7.  En la sección "Object Creation Options", marca: ☑️ **Launch New Custom Tab Wizard**.
8.  Haz clic en **Save** y selecciona un estilo de pestaña (ej: *Building*).

#### Paso 2: [NUEVO S2] Campo Abreviatura (External ID)
*Vital para que el Data Loader pueda cruzar los CSVs.*
1.  **Fields & Relationships** > **New**.
2.  Data Type: **Text**. Next.
3.  **Field Label**: `Abreviatura`. **Field Name**: `Abreviatura`.
4.  **Length**: `20`.
5.  ☑️ **Unique**: Marca "Case insensitive" para evitar duplicados.
6.  ☑️ **External ID**: **OBLIGATORIO**. Marca esta casilla.
7.  Haz clic en **Save**.

#### Paso 3: Campos de Negocio (Implementación Antigua)
1.  **Código Interno (AutoNumber)**: `CAR-{0000}`.
2.  **Tipo de Título (Picklist)**: `Licenciatura`, `Tecnicatura`, `Posgrado`.
3.  **Duración (Años) (Picklist)**: 1, 2, 3, 4, 5.

---

## 🛠️ Parte 2: Refactorización y Mejoras (To-Be)

*Esta sección detalla las modificaciones y nuevos campos requeridos para alinear el objeto a la arquitectura consolidada (LuminaRT + LuminaFinal).*

### 🚨 Diagnóstico
Tras auditar la org, determinamos que la implementación original carecía de campos esenciales para gestionar la oferta educativa real (Turno, Modalidad) y requería reglas estrictas de calidad de datos. Además, la duración debe medirse en meses, no en años, para soportar cursos cortos.

### Paso 1: Actualización de Campos de Negocio
Crear/modificar los siguientes campos personalizados:

1.  **Tipo de Carrera (Reemplaza a Tipo de Título):**
    *   Tipo: **Picklist**. Name: `Tipo_Carrera__c`.
    *   Valores: `Licenciatura`, `Ingeniería`, `Tecnicatura`, `Posgrado`, `Curso Corto`.
2.  **Modalidad de Cursada (Nuevo):**
    *   Tipo: **Picklist**. Name: `Modalidad__c`.
    *   Valores: `Presencial`, `Virtual`, `Híbrida`.
3.  **Turno Habilitado (Nuevo):**
    *   Tipo: **Picklist**. Name: `Turno__c`.
    *   Valores: `Mañana`, `Tarde`, `Noche`.
4.  **Duración Exacta (Nuevo):**
    *   Tipo: **Number(3, 0)**. Name: `Duracion_Meses__c`.
5.  **Plan de Estudio Oficial (Nuevo):**
    *   Tipo: **URL**. Name: `Plan_de_Estudio__c`.
6.  **Disponibilidad (Nuevo):**
    *   Tipo: **Picklist**. Name: `Estado__c`.
    *   Valores: `Activa`, `En Cierre`, `Inactiva`.

### Paso 2: Calidad de Datos (Validation Rules)
Para evitar errores de tipeo, implementaremos la regla maestra de validación extraída de Producción.

1.  En el Object Manager de `Carrera__c`, ve a **Validation Rules** > **New**.
2.  **Rule Name**: `Nombre_Carrera_Solo_Letras`
3.  **Active**: ☑️ SÍ.
4.  **Error Condition Formula**:
    ```sql
    NOT(REGEX(Name, "^[a-zA-Z áéíóúÁÉÍÓÚñÑ]+$"))
    ```
5.  **Error Message**: "El nombre de la carrera solo debe contener letras. No se permiten números ni caracteres especiales."
6.  **Error Location**: Selecciona el campo *Nombre de Carrera*.

---

## ✅ Verificación de Éxito de Refactorización
1.  Intenta modificar una Carrera y ponerle de nombre `Licenciatura 2024`. El sistema **debe bloquearte** (por contener el número).
2.  Verifica en el Page Layout que los campos de Modalidad, Turno y Duración en Meses estén visibles y funcionales.

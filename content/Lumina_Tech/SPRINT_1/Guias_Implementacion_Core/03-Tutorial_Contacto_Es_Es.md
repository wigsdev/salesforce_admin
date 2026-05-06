# 🎓 Guía de Arquitectura e Implementación: Objeto Persona (Contact)

**Fase**: Sprint 1 (Refactorización Arquitectónica Enterprise)
**Rol Responsable**: 🛡️ **Salesforce Admin / Architect**

---

## 🔍 Parte 1: Implementación Original (As-Is)

*La siguiente sección documenta los pasos de configuración que se establecieron en la primera iteración del Sprint 2. Se conserva por trazabilidad histórica.*

### 🎯 Objetivo Original
Habilitar la gestión de alumnos utilizando el objeto estándar `Contact` de Salesforce. El Sprint 2 consolida esta decisión para aprovechar las herramientas nativas de Salesforce y estandarizar la identidad digital mediante un **External ID**.

### 🛠️ Procedimiento de Configuración Original

#### Paso 1: Tipos de Registro (Record Types) Originales
1.  Ve a **Setup** > **Object Manager** > **Contact**.
2.  **Record Types** > **New**.
    - **Label**: `Alumno`. **Developer Name**: `Alumno`.
    - **Active**: ☑️ SÍ.
3.  Configure el Layout para que muestre los campos académicos.

#### Paso 2: Campos de Identidad (Core Alumno)
Añadir al objeto `Contact` los siguientes campos personalizados:

1.  **Número de Documento (DNI/CÉDULA)**
    *   **New** > Data Type: **Text**. **Field Name**: `Numero_Documento`.
    *   **Length**: `20`. ☑️ **Unique**. ☑️ **External ID**.
2.  **Rol del Contacto (Picklist)**
    *   Data Type: **Picklist**. **Field Name**: `Rol`.
    *   **Values**: `Alumno`, `Docente`, `Staff`. (☑️ **Required**).
3.  **Estado de Pago (Picklist)**
    *   Data Type: **Picklist**. **Field Name**: `Estado_Pago`.
    *   **Values**: `Al día`, `Moroso`.

#### Paso 3: Identidad Digital (Fórmulas S2)
1. **Email Institucional**: Fórmula que genera `nombres.apellidos@lumina.edu.ar`.
2. **Usuario Sistema**: Fórmula `Numero_Documento__c & "@lumina.edu.ar"`.

---

## 🛠️ Parte 2: Plan de Refactorización (To-Be)

*En base a la auditoría técnica reciente de los entornos `LuminaRT` y `LuminaFinal`, se ha determinado que la implementación original padece de deuda técnica (dispersión de campos y uso del picklist Rol). El siguiente bloque detalla las acciones para elevar el objeto a una estructura Enterprise (EDA).*

### 🚨 Diagnóstico y Ajustes Requeridos
El uso de un campo Picklist (`Rol__c`) para diferenciar alumnos de docentes provoca que usuarios de todos los perfiles vean campos irrelevantes. La solución definitiva es expandir los Record Types y crear Page Layouts dedicados, además de fusionar campos financieros y administrativos.

### Bloque 1: Expansión de Campos y Fórmulas
Asegura que el objeto contenga esta batería de campos unificada:

1.  **Sección Identidad Global:** `Numero_Documento__c` (Texto, Ext ID), `Tipo_Documento__c` (Picklist).
2.  **Sección de Sistema (LuminaRT):**
    *   Asegúrate de que las fórmulas de Email Institucional y Usuario Sistema (creadas en la Parte 1) funcionen correctamente para todos los roles.
3.  **Sección Alumno:**
    *   Crea `Legajo__c` (Auto Numérico), `Fecha_Ingreso__c` (Date), `Carrera__c` (Lookup).
    *   Mantén las fórmulas financieras: `Deudas_Vencidas__c` (Roll-up) y `Asistencia__c`.
4.  **Sección Docentes / Staff:**
    *   Ajusta la etiqueta del campo `Level__c` a "Escalafón Docente".
    *   Crea `Turno_Laboral__c` (Picklist) y `Carrera_a_Cargo__c` (Lookup, para Directores).

### Bloque 2: Segregación de Interfaz (Page Layouts)
Crea layouts específicos para no cruzar información:

1.  **`Persona - Alumno Layout`:** Incluye todos los campos académicos, asistencia y sección financiera.
2.  **`Persona - Docente Layout`:** **Oculta** estrictamente todos los campos de pagos y asistencia. Muestra solo idiomas y nivel docente.
3.  **`Persona - Staff Layout`:** Muestra Turno Laboral y Departamento.

### Bloque 3: Estructura Definitiva de Tipos de Registro (Record Types)
Expande la configuración del Paso 1 original, creando **4 perfiles maestros**:

1.  **Alumno**: Asigna el `Persona - Alumno Layout`.
2.  **Profesor**: Asigna el `Persona - Docente Layout`.
3.  **Administrativo**: Asigna el `Persona - Staff Layout`.
4.  **Director**: Asigna un layout que incluya `Carrera_a_Cargo__c`.

### Bloque 4: Reglas de Calidad de Datos (Validation Rules)
Aplica estas reglas extraídas de la auditoría de Producción para mantener la integridad de las personas:

1.  **DNI Numérico (`Formato_DNI_Numerico`)**:
    *   `NOT(REGEX(Numero_Documento__c, "^[0-9]{8,9}$"))`
2.  **Validación de Email (`Formato_Email_Valido`)**:
    *   `NOT(REGEX(Email, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$"))`
3.  **Mayoría de Edad (`Mayoria_de_Edad_Requerida`)**:
    *   `(TODAY() - Fecha_Nacimiento__c) / 365.2425 < 18`
4.  **Nombres sin Números (`No_numbers_in_names`)**:
    *   `NOT(REGEX(FirstName, "^[a-zA-Z áéíóúÁÉÍÓÚñÑ]+$"))`

### Bloque 5: Seguridad y Privacidad (Zero Trust)
Para cumplir con los requerimientos de privacidad de la Rectora:

1.  **Visibilidad Global (OWD)**:
    *   Ve a **Setup** > **Sharing Settings**.
    *   Establece el **Default Internal Access** de **Contact** a **Private**.
2.  **Seguridad a Nivel de Campo (FLS)**:
    *   Ve al perfil **Lumina Professor** > **Object Settings** > **Contacts**.
    *   Desmarca la casilla **Read Access** para el campo `Numero_Documento__c` (DNI). Así evitamos que los docentes vean datos sensibles.

## ✅ Verificación de Éxito de Refactorización
1.  Haz clic en la pestaña "Contactos" y crea un **Nuevo Contacto**. El sistema debe forzarte a elegir uno de los 4 Record Types.
2.  Selecciona "Profesor". Verifica visualmente que no existan campos de "Deudas Vencidas".
3.  Intenta poner un número en el nombre de la persona y valida que el sistema lo bloquee.

# ⚙️ Guía Técnica: App, Validaciones y Seguridad [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Hardening de Seguridad)
**Rol Responsable**: 🛡️ **Salesforce Admin**

---

## 🎯 Objetivo
Dar forma final a la aplicación "Gestión Académica Lumina" configurando tres pilares críticos: la **Lightning App** que integra visualmente todos los objetos, las **Validation Rules** que protegen la integridad de los datos, y el modelo de **Seguridad por Capas** (OWD + Profiles + Permission Sets) que garantiza que cada usuario solo vea lo que le corresponde.

---

## Parte 1: La Lightning App ("Gestión Académica Lumina")

La Lightning App es el "envoltorio" que presenta todos los objetos al usuario de forma ordenada y con la identidad visual de la universidad.

### Paso 1.1: Crear (o Verificar) la Lightning App

El Grupo 6 ya tiene creada una App llamada `Gestion_Academica_Lumina`. Verificamos que esté correctamente configurada:

1. Ve a **Setup** (⚙️) > **App Manager**.
2. Busca la aplicación **Gestión Académica Lumina** en la lista.
3. Haz clic en el menú desplegable (▼) > **Edit** (Editar).
4. Revisa que en la sección **Navigation Items** (Pestañas de Navegación) estén presentes, en este orden:
   - 🏠 **Home** (Inicio)
   - 👥 **Contactos** (Alumnos y Profesores)
   - 🎓 **Carreras**
   - 📚 **Materias**
   - 📄 **Inscripciones**
   - ✅ **Asistencia**
   - 📊 **Evaluaciones**
   - 💰 **Cobros**
   - 📈 **Reportes**
   - 📋 **Dashboards**
5. En la sección **Assigned Profiles**, verifica que los perfiles de Rectorado, Secretaría Académica y Tesorería tengan acceso.
6. Haz clic en **Save**.

### Paso 1.2: Verificar el Branding (Tema de Lumina Tech)

1. Ve a **Setup** > **Themes and Branding**.
2. Confirma que el tema **Lumina Oficial** (`LEXTHEMINGLuminaOficial`) está como **Active** (Activo).
3. Si no está activo, haz clic en **Activate** en el menú de ese tema.

---

## Parte 2: Validation Rules (Reglas de Validación)

Las reglas de validación son el "guardián de la puerta": impiden que se guarden datos inválidos, inconsistentes o peligrosos en la base de datos.

### Paso 2.1: Coherencia Carrera-Materia (Objeto Inscripción)

**Problema que resuelve**: Evitar que un alumno de Ingeniería en Sistemas se inscriba en la materia "Anatomía" (de Medicina).

1. Ve a **Object Manager** > **Inscripción** > **Validation Rules** > **New**.
2. **Rule Name**: `Coherencia_Carrera_Materia`
3. **Error Condition Formula**:
   ```
   Materia__r.Carrera__c != Alumno__r.Carrera__c
   ```
   > ⚠️ **Limitación técnica de Salesforce**: Los Lookup Filters nativos en el formulario no pueden filtrar a 3 niveles (Inscripción → Alumno → Carrera). Por eso colocamos la barrera como Validation Rule al momento de GUARDAR. El usuario podrá ver todas las materias al buscar, pero si elige una incorrecta, el sistema bloqueará el guardado con un mensaje claro.
4. **Error Message**: `"¡Error de Carrera! La materia seleccionada pertenece a otra carrera. Solo puedes inscribir al alumno en materias de su propia carrera."`
5. **Error Location**: Field → `Materia__c`
6. Haz clic en **Save**.

### Paso 2.2: Formato de Número de Documento (Objeto Contact)

**Problema que resuelve**: Evitar que ingresen un DNI con letras, puntos, guiones o con el número de dígitos incorrecto.

1. Ve a **Object Manager** > **Contact** > **Validation Rules** > **New**.
2. **Rule Name**: `Validar_Formato_DNI`
3. **Error Condition Formula**:
   ```
   AND(
     NOT(ISBLANK(Numero_Documento__c)),
     OR(
       LEN(Numero_Documento__c) < 7,
       LEN(Numero_Documento__c) > 9,
       NOT(ISNUMBER(Numero_Documento__c))
     )
   )
   ```
4. **Error Message**: `"El Número de Documento debe contener entre 7 y 9 dígitos numéricos sin puntos ni guiones. Ejemplo: 45147679"`
5. Haz clic en **Save**.

### Paso 2.3: Rango de Notas (Objeto Evaluación) — Del Grupo 6

El Grupo 6 ya tiene la regla `Rango_Notas_Examenes`. Confirmamos que está activa:

1. Ve a **Object Manager** > **Evaluación** > **Validation Rules**.
2. Verifica que `Rango_Notas_Examenes` exista y esté activa (Activo = ✅).
3. Confirma que su fórmula bloquee notas fuera del rango 0-10.

---

## Parte 3: Modelo de Seguridad por Capas

La seguridad en Salesforce funciona como una cebolla: cuantas más capas tiene, más protegida está la data. Implementamos 3 capas.

### Capa 1: Organization-Wide Defaults (OWD)

Define qué puede ver UN usuario de LOS REGISTROS DE OTROS por defecto.

1. Ve a **Setup** > **Sharing Settings**.
2. Configura los OWD de los objetos críticos:

   | Objeto | OWD Recomendado | Justificación |
   | :--- | :--- | :--- |
   | `Contact` | **Private** | Un docente no debe ver los datos personales de otro docente ni de alumnos de otras carreras. |
   | `Cobro__c` | **Private** | La información financiera es estrictamente confidencial. |
   | `Evaluacion__c` | **Private** | Un docente solo debería ver las notas de sus propias materias. |
   | `Inscripcion__c` | **Public Read Only** | La Secretaría necesita ver todas las inscripciones para gestión. |
   | `Carrera__c` | **Public Read Only** | El catálogo de carreras es visible para todos, pero solo Admin puede modificarlo. |
   | `Materia__c` | **Public Read Only** | Ídem Carrera. |

3. Haz clic en **Save**.

### Capa 2: Profiles (Perfiles de Usuario)

Define qué objetos y qué campos puede ver/crear/editar/borrar cada tipo de usuario. El perfil es la "llave maestra" del usuario.

La arquitectura completa de perfiles está documentada en la **Guía 07.1 (Tutorial de Perfiles)**.

**Resumen de los 6 perfiles core de Lumina Tech**:

| Perfil (Label) | Clonado de | Acceso Core |
| :--- | :--- | :--- |
| `Lumina Rectorado` | Standard Platform User | Read-Only Global. Solo ve, no edita. |
| `Lumina Secretaria` | Standard Platform User | Full CRUD en Inscripción, Asistencia, Evaluación. Sin acceso a Cobro. |
| `Lumina Admisiones` | Standard Platform User | Create en Contact solamente. Sin acceso a notas ni finanzas. |
| `Lumina Professor` | Standard Platform User | Create/Edit en Asistencia y Evaluación de sus propias materias. |
| `Lumina Tesoreria` | Standard Platform User | Full CRUD en Cobro. Sin acceso a Evaluaciones ni Asistencias. |
| `Lumina Admin` | System Administrator | Acceso total. Solo para el equipo técnico. |

### Capa 3: Field-Level Security (FLS) — Seguridad a Nivel de Campo

Incluso si un usuario puede ver el objeto Contact, algunos campos deben ser invisibles para ciertos perfiles.

**Campos sensibles a proteger**:

1. Ve a **Setup** > **Object Manager** > **Contact** > **Fields & Relationships**.
2. Selecciona el campo **Número de Documento** (`Numero_Documento__c`).
3. Haz clic en **Set Field-Level Security**.
4. Desmarca **Visible** para el perfil **Lumina Professor**. El DNI de un alumno es un dato sensible que un docente no necesita bajo ningún concepto.
5. Repite para los campos: `Email`, `Phone` y `Deudas_Vencidas__c`.

---

## ✅ Verificación de Éxito (Prueba de Seguridad End-to-End)

1. **Prueba como Profesor**: Loguéate con un usuario de perfil `Lumina Professor`.
   - ¿Puedes ver la pestaña de Cobros? **Resultado esperado**: NO debe aparecer.
   - ¿Puedes ver el DNI de un alumno? **Resultado esperado**: El campo debe estar oculto/en blanco.
2. **Prueba como Tesorería**: Loguéate con un usuario de perfil `Lumina Tesoreria`.
   - ¿Puedes ver la pestaña de Evaluaciones? **Resultado esperado**: NO debe aparecer.
3. **Prueba de Validación**: Intenta inscribir un alumno de Ingeniería en una materia de Medicina.
   - **Resultado esperado**: Al guardar, aparece el mensaje de error de la regla `Coherencia_Carrera_Materia`.

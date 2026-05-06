# 🎓 Guía Técnica: Objeto Asistencia [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Consolidación Arquitectura G3+G6) / **Refactorización Core**
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Docente Titular**

---

## 🔍 Parte 1: Implementación Original (As-Is)

*La siguiente sección documenta el diseño original (Grupo 6) para mantener la trazabilidad de las decisiones de diseño tempranas.*

### 🎯 Objetivo Original
Registrar y auditar la presencia de cada alumno en cada sesión de clase. Este objeto es el termómetro de permanencia: si un alumno acumula más del 25% de faltas, se dispara una alerta.

### 🛠️ Procedimiento de Configuración Original

#### Situación Actual (Modelo Grupo 6)
El Grupo 6 implementó el objeto `Asistencia__c` con la siguiente estructura:
- **Relación padre**: Lookup a `Inscripcion__c`. *(Justificado para que el borrado de una inscripción no borre el histórico de clases).*
- **Record Types**: `Asistencia por Alumno` y `Asistencia por Inscripcion` (Para distinguir formas de carga masiva/manual).
- **Campos clave del Grupo 6**:
  - `Estado` (Checkbox o Picklist).
  - `Fecha y Hora de Sesión`: Date/Time de la clase.
  - `Código Único de Asistencia`: External ID.
  - `Alumno (Auto)` y `Materia (Auto)`: Fórmulas de visualización.

#### Regla de Validación
- `Solo_Fecha_Actual`: Impedir que un docente cargue asistencia de una clase futura (`Fecha__c > TODAY()`).

---

## 🛠️ Parte 2: Refactorización y Mejoras (To-Be)

*Basado en la auditoría técnica de los entornos `LuminaRT`, el diseño original (G6) generó una deuda técnica enorme al usar una relación "Lookup" e implementar Record Types innecesarios, lo que impide calcular el porcentaje de ausentismo de forma nativa.*

### 🚨 Diagnóstico de Arquitectura
1.  **Limitación de Junction Object:** La intención ideal sería usar un Master-Detail para habilitar automatizaciones. Sin embargo, Salesforce prohíbe que un objeto Junction (como Inscripción, que ya tiene dos Masters) actúe como "Master" de un tercer objeto. **Solución:** Debemos mantener la relación como **Lookup**. Para suplir la falta de Roll-Up Summaries nativos, se utilizará un Flow automatizado (ver Guía de Automatizaciones).
2.  **Complejidad Innecesaria:** Los dos Record Types solo confunden al usuario. El objeto debe ser simple: Una clase, un presentismo.
3.  **Tipos de Datos Inexactos:** Registrar la "Hora" de la sesión en cada presentismo gasta almacenamiento y es irrelevante; lo que importa es la fecha.

### Paso 1: Mantenimiento de Relación Lookup (Obligatoria)
1.  **Control de Integridad:** 
    *   Ve a **Setup** > **Object Manager** > **Asistencia** > **Fields & Relationships**.
    *   Verifica que el campo `Inscripcion__c` sea de tipo **Lookup**.
    *   Asegúrate de marcar la casilla **"Always require a value in this field in order to save a record"**. Esto previene crear asistencias sin un alumno vinculado.

### Paso 2: Limpieza de Record Types
1.  Ve a **Record Types** y **desactiva/elimina** los tipos `Asistencia por Alumno` y `Asistencia por Inscripcion`.
2.  Mantén un único Layout estándar (`Asistencia Layout`).

### Paso 3: Estructura Definitiva de Campos (LuminaRT)
Asegúrate de que el objeto contenga estrictamente estos campos operativos:

1.  **Estado Asistencia:**
    *   Tipo: **Picklist**. Name: `Estado__c`.
    *   Valores OBLIGATORIOS: `Presente`, `Ausente`, `Justificado`.
2.  **Tipo de Clase (Nuevo):**
    *   Tipo: **Picklist**. Name: `Tipo_de_Clase__c`.
    *   Valores: `Teórica`, `Práctica`, `Laboratorio`.
3.  **Fecha de Clase (Reemplaza a Date/Time):**
    *   Tipo: **Date** (No Date/Time). Name: `Fecha__c`.
4.  **Observaciones (Nuevo):**
    *   Tipo: **Text Area**. Name: `Observaciones__c`. *(Útil cuando el estado es Justificado).*
5.  Mantener las Fórmulas Cruzadas: `Alumno_F__c` y `Materia_F__c` (para facilitar el armado de reportes sin crear Custom Report Types).

### Paso 4: Seguridad y Reglas de Validación (Zero Trust)
Para garantizar la integridad de los registros de asistencia:

1.  **Regla de Validación (`Solo_Fecha_Actual`)**:
    *   Ve a Validation Rules > New.
    *   Fórmula: `Fecha__c > TODAY()`
    *   Mensaje: "La fecha de asistencia no puede ser futura. Verifique su calendario."
2.  **Seguridad de Visibilidad (OWD)**:
    *   Ve a **Setup** > **Sharing Settings**.
    *   Establece el **Default Internal Access** de **Asistencia__c** en **Private**.

### Paso 5: Automatización de Presentismo (Record-Triggered Flow)
Al no poder usar Roll-Up Summaries nativos, la automatización del conteo de faltas y presencias se delega a un **Record-Triggered Flow**.
*Nota: La construcción exacta de este flujo se documentará en la guía de Automatizaciones, pero a nivel objeto, asegúrate de que existan los campos numéricos `Total_Clases_Dictadas__c`, `Clases_Presentes__c` y `Faltas__c` en el objeto Inscripción para recibir los datos del flujo.*

---

## ✅ Verificación de Éxito de Refactorización
1.  Intenta registrar una asistencia con fecha de mañana. El sistema **debe bloquearte** por la regla `Solo_Fecha_Actual`.
2.  Intenta guardar una Asistencia sin rellenar el campo Inscripción. El sistema debe bloquearte gracias a la validación estricta del Lookup.

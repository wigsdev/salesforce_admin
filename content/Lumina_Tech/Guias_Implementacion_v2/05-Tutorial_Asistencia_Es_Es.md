# 🎓 Guía Técnica: Objeto Asistencia [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Consolidación G3+G6)
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Docente Titular**

---

## 🎯 Objetivo
Registrar y auditar la presencia de cada alumno en cada sesión de clase. Este objeto es el termómetro de permanencia: si un alumno acumula más del 25% de faltas, se dispara una alerta antes de que pierda la regularidad. En el Sprint 2, consolidamos la arquitectura del Grupo 6 con las mejores prácticas del Grupo 3.

---

## 📋 Situación Actual (Modelo Grupo 6)

El Grupo 6 implementó el objeto `Asistencia__c` con la siguiente estructura:

- **Relación padre**: `Inscripcion__c` (Inscripción del Alumno)
- **Record Types**: `Asistencia por Alumno` y `Asistencia por Inscripcion`
- **Campos clave del Grupo 6**:
  - `Estado` (Checkbox o Picklist): Marca si el alumno estuvo presente.
  - `Fecha y Hora de Sesión`: Date/Time de la clase.
  - `Código Único de Asistencia`: External ID.
  - `Alumno (Auto)` y `Materia (Auto)`: Campos de resumen automático (Roll-Up o Formula).
  - `Inscripción` (Lookup) y `Inscripcion_Alumno_Materia` (campos de cruce).

---

## 🚀 ACTUALIZACIÓN / REFACTORIZACIÓN (Estándar Grupo 3)

### Paso 1: Configuración Inicial del Objeto

1. Ve a **Setup** (⚙️) > **Object Manager** y busca el objeto **Asistencia**.
2. Verifica que el objeto ya tenga una **Pestaña (Tab)** activa en la aplicación `Gestión Académica Lumina`.
3. Confirma que la opción **Allow Reports** esté habilitada. Si no lo está:
   - Haz clic en **Edit** en el objeto.
   - Marca la casilla ☑️ **Allow Reports**.
   - Haz clic en **Save**.

### Paso 2: Verificar la Relación con Inscripción (Lookup Obligatorio)

El objeto `Asistencia` debe estar vinculado a `Inscripcion__c` mediante una **relación Lookup**. Esta relación es el núcleo: una Asistencia sin Inscripción es un dato huérfano sin valor.

1. Ve a **Fields & Relationships** del objeto Asistencia.
2. Busca el campo llamado `Inscripción` (Tipo: Lookup Relationship).
3. Confirma que apunta al objeto `Inscripcion__c` y que tiene la marca **Always require a value** (Obligatorio).

> 💡 **¿Por qué Lookup y no Master-Detail?** Una relación Master-Detail borraría las Asistencias si se borra la Inscripción. Con Lookup, Salesforce bloquea el borrado de la Inscripción si tiene Asistencias hijas, protegiendo el historial académico del alumno.

### Paso 3: Diccionario de Campos Recomendado

Asegúrate de que el objeto `Asistencia__c` cuente con los siguientes campos. Crea los que no existan:

| Etiqueta (Label) | Nombre API | Tipo | Detalle |
| :--- | :--- | :--- | :--- |
| **Estado Asistencia** | `Estado_Asistencia__c` | Picklist | Valores: **Presente**, **Ausente**, **Justificado** |
| **Fecha de Clase** | `Fecha__c` | Date | Fecha de la sesión _(el Grupo 6 lo llama "Fecha y Hora de Sesión")_ |
| **Código Único** | `Codigo_Unico_Asistencia__c` | Text(50) | External ID + Unique para evitar duplicados en carga masiva |
| **Alumno (F)** | `Alumno_F__c` | Formula (Text) | `Inscripcion__r.Alumno__r.FirstName & " " & Inscripcion__r.Alumno__r.LastName` |
| **Materia (F)** | `Materia_F__c` | Formula (Text) | `Inscripcion__r.Materia__r.Name` |

#### 3.1 ¿Por qué los campos de Fórmula (F)?

Los campos `Alumno (F)` y `Materia (F)` no almacenan datos; calculan y muestran la información de objetos "abuelos" (Contact y Materia) directamente en la ficha de Asistencia. Esto permite crear **Reportes de Asistencia** que muestren el nombre del alumno y la materia sin navegar niveles de relación manualmente.

### Paso 4: Validación Anti-Fecha Futura (Regla de Validación)

El Grupo 6 ya tiene la regla `Solo_Fecha_Actual`. Confirmamos que debe conservarse.

**Objetivo**: Impedir que un docente cargue asistencia de una clase futura o con fecha incorrecta.

1. En el objeto Asistencia > **Validation Rules** > busca `Solo_Fecha_Actual`.
2. Si existe, verifica que su fórmula sea similar a:
   ```
   Fecha__c > TODAY()
   ```
3. Si no existe, créala con ese nombre. El mensaje de error debe ser:
   *"No se puede registrar asistencia con una fecha futura. Por favor, verifique la fecha de la sesión."*

### Paso 5: Automatización en la Inscripción (Roll-Up Summary)

Para que la Inscripción sepa automáticamente cuántas clases presenció un alumno, necesitamos un campo de resumen en `Inscripcion__c`.

> ⚠️ **Nota**: Este paso solo aplica si la relación Asistencia → Inscripción es **Master-Detail**. Si es Lookup (recomendado), este Roll-Up no es posible nativamente y el cálculo debe hacerse mediante un **Before-Save Flow**.

**Configuración sugerida en la Inscripción:**
- `Clases_Presentes__c` (Roll-Up: COUNT de Asistencias donde Estado = "Presente")
- `Total_Clases__c` (Roll-Up: COUNT de todas las Asistencias)
- `% Asistencia (F)`: Fórmula → `Clases_Presentes__c / Total_Clases__c * 100`

---

## ✅ Verificación de Éxito

1. Abre una Inscripción activa y crea 4 Asistencias: 3 con estado **Presente** y 1 con **Ausente**.
2. Verifica que el campo `% Asistencia` en la Inscripción muestre **75%**.
3. Intenta crear una Asistencia con una fecha de mañana. **Resultado esperado**: El sistema debe bloquear el guardado con el mensaje de error de la regla de validación.
4. Intenta crear dos asistencias con el mismo Código Único. **Resultado esperado**: Error de duplicado.

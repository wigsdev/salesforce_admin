# 💰 Guía Técnica: Objeto Cobro (Gestión de Pagos) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Consolidación Arquitectura G3+G6) / **Refactorización Core**
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Tesorería / Cobranzas**

---

## 🔍 Parte 1: Implementación Original (As-Is)

*La siguiente sección documenta el diseño original (Grupo 6) para mantener la trazabilidad de las decisiones de diseño tempranas.*

### 🎯 Objetivo Original
Registrar los pagos de cuotas académicas de cada alumno. Este objeto es la columna vertebral financiera de Lumina Tech: permite detectar alumnos morosos y disparar alertas de deuda sin mezclar la información financiera con datos académicos (notas, asistencias).

### 🛠️ Procedimiento de Configuración Original

#### Situación Actual (Modelo Grupo 6)
El Grupo 6 implementó el objeto `Cobro__c` con la siguiente estructura:
- **Relación padre**: Lookup a `Contact` (Alumno).
- **Campos implementados**:
  - `Monto` (Currency).
  - `Estado` (Picklist): Pendiente, Pagado, Vencido.
  - `Concepto` (Text).
  - `Período Académico` (Picklist).
  - `Cuota Vencida` (Checkbox).
  - `Método de Pago` (Picklist).
  - `Código Único` (Text, External ID).
- **Seguridad**: Se indicó quitar el acceso "Read" a este objeto para el perfil "Profesor", evitando que docentes vean pagos.

#### Regla de Validación
- `Prevent_Null_Payment_Data`: Impedía guardar un cobro sin monto.

---

## 🛠️ Parte 2: Refactorización y Mejoras (To-Be)

*Basándonos en la auditoría técnica de la org `LuminaFinal`, el diseño original tenía una relación Lookup débil con el Contacto. Al ser `Contact` un objeto estándar, permite ser el "Master" de objetos personalizados sin el límite de los Junction Objects. Elevaremos la relación a Master-Detail para habilitar Roll-up Summaries de deuda directamente en la ficha del Alumno.*

### 🚨 Diagnóstico de Arquitectura
1.  **Vínculo Débil:** Al usar Lookup, no podíamos sumar la deuda total del alumno nativamente. **Solución:** Pasar la relación con Contacto a Master-Detail.
2.  **Campos Desactualizados:** La nomenclatura original difería del modelo final auditado en Producción (`Monto_Admin__c`, `ID_Transaccion_Exterma__c`).

### Paso 1: Fortalecimiento de la Relación (Master-Detail)
1.  Ve a **Setup** > **Object Manager** > **Cobro** > **Fields & Relationships**.
2.  Cambia el tipo de campo `Alumno__c` (que apunta a `Contact`) de **Lookup** a **Master-Detail Relationship**.
    *   *Nota: Esto habilita que si se borra el Contacto, sus cobros se eliminen automáticamente en cascada, limpiando la base de datos de tesorería.*

### Paso 2: Alineación del Diccionario de Campos (LuminaFinal)
Asegúrate de que los campos coincidan exactamente con la estructura de Producción:

1.  **Monto a Cobrar (Modificado):**
    *   Tipo: **Currency(12, 2)**. Name: `Monto_Admin__c`.
2.  **ID de Transacción (Modificado):**
    *   Tipo: **Text(50)**. Name: `ID_Transaccion_Exterma__c`. *(Debe estar marcado como **Unique** y **External ID**).*
3.  **Tipo de Cobro (Nuevo):**
    *   Tipo: **Picklist**. Name: `Tipo_de_Cobro__c`.
    *   Valores: `Matrícula`, `Cuota Mensual`, `Derecho a Examen`, `Certificado`.
4.  **Fecha de Pago:**
    *   Tipo: **Date**. Name: `Fecha_de_Pago__c`.
5.  Mantén los campos: `Estado__c`, `Metodo_Pago__c`, `Periodo_Academico__c` y `Cuota_Vencida__c`.

### Paso 3: Regla de Validación de Datos Financieros
1.  Ve a **Object Manager** > **Cobro** > **Validation Rules** > **New**.
2.  **Nombre**: `Prevenir_Datos_Invalidos_Cobro`.
3.  **Fórmula**:
    ```sql
    OR(
       ISNULL(Monto_Admin__c),
       Monto_Admin__c <= 0
    )
    ```
4.  **Mensaje**: "El campo Monto es obligatorio y debe ser mayor a cero."

### Paso 4: Automatización de Morosidad (Roll-Up Summary en Contact)
Al haber convertido la relación en Master-Detail, ya no necesitas un flujo complejo para saber cuánto debe el alumno.
1.  Ve al objeto **Contact** > Fields & Relationships > New.
2.  Data Type: **Roll-Up Summary**.
3.  **Field Label**: `Total Deuda Vencida`.
4.  **Summarized Object**: `Cobros`.
8.  **Roll-Up Type**: **SUM** sobre el campo `Monto_Admin__c`.
6.  **Filter Criteria**: Selecciona "Only records meeting certain criteria" y agrega la condición: `Estado__c EQUALS Vencido`.

### Paso 5: Seguridad y Privacidad Financiera (Zero Trust)
Asegura que el personal docente jamás vea información financiera:

1.  **Visibilidad Global (OWD)**:
    *   Al ser Master-Detail de Contacto, su OWD es **Controlled by Parent**. Automáticamente adopta la seguridad del alumno.
2.  **Seguridad de Objeto (SoD)**:
    *   Ve a **Setup** > **Profiles** > **Lumina Professor** > **Object Settings** > **Cobros**.
    *   **Desmarca** la casilla **Read** y **View All**.
    *   Cambia la pestaña a **Tab Hidden**.

---

## ✅ Verificación de Éxito de Refactorización
1.  Crea un Alumno de prueba.
2.  Créale un Cobro por $5000 con estado `Pagado`.
3.  Créale un Cobro por $2000 con estado `Vencido`.
4.  Ve a la ficha del Alumno y verifica que el campo `Total Deuda Vencida` muestre automáticamente `$2000` (sin necesidad de flujos de actualización).
5.  Inicia sesión como Profesor e intenta buscar la pestaña de Cobros. El sistema no te lo debe permitir (FLS).

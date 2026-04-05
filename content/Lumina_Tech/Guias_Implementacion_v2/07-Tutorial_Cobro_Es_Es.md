# 💰 Guía Técnica: Objeto Cobro (Pagos) [MODIFICADO SPRINT 2]

**Sprint**: 01 (Fundamentos) / **Sprint 02** (Consolidación G3+G6)
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Tesorería / Cobranzas**

---

## 🎯 Objetivo
Registrar los pagos de cuotas académicas de cada alumno. Este objeto es la columna vertebral financiera de Lumina Tech: permite detectar alumnos morosos, disparar alertas de deuda y mantener una auditoría completa de cobros sin mezclar la información financiera con datos académicos (notas, asistencias).

---

## 📋 Situación Actual (Modelo Grupo 6)

El Grupo 6 implementó el objeto `Cobro__c` con la siguiente estructura, la cual ya está bien alineada con las prácticas del Grupo 3:

- **Relación padre**: `Contact` (Alumno)
- **Campos implementados**:
  - `Alumno` (Lookup → Contact): El pagador.
  - `Monto` (Currency): El valor de la cuota.
  - `Estado` (Picklist): Estado del cobro (Pendiente, Pagado, Vencido).
  - `Concepto` (Text): Descripción del cobro (Ej: "Cuota Marzo 2025").
  - `Período Académico` (Text/Picklist): Ciclo al que corresponde.
  - `Cuota Vencida` (Checkbox): Marca si la cuota pasó su fecha límite.
  - `Método de Pago` (Picklist): Transferencia, Efectivo, Tarjeta.
  - `Código Único` (Text, External ID): Para evitar duplicados en carga masiva.

---

## 🚀 ACTUALIZACIÓN / REFACTORIZACIÓN (Estándar Grupo 3)

### Paso 1: Confirmar la Relación con el Alumno (Lookup a Contact)

La relación fundamental del Cobro es saber **quién paga**.

1. Ve a **Setup** (⚙️) > **Object Manager** > **Cobro**.
2. Ve a **Fields & Relationships** y busca el campo **Alumno** (o similar).
3. Confirma que es un **Lookup Relationship** hacia el objeto `Contact`.
4. ☑️ Asegúrate de que tenga configurado un **Lookup Filter** para mostrar solo Contactos con Record Type `Alumno`. Esto evita que Tesorería registre un pago a nombre de un Profesor por error.
   - **Filter**: `Contact: Record Type` | `Equals` | `Alumno`

### Paso 2: Diccionario de Campos Recomendado

Verifica que `Cobro__c` cuente con los siguientes campos. Crea los que no existan:

| Etiqueta (Label) | Nombre API | Tipo | Detalle |
| :--- | :--- | :--- | :--- |
| **Alumno** | `Alumno__c` | Lookup (Contact) | Quién paga. Obligatorio. |
| **Monto** | `Monto__c` | Currency(12, 2) | Valor de la cuota en ARS. |
| **Estado** | `Estado__c` | Picklist | **Pendiente**, **Pagado**, **Vencido** |
| **Fecha de Vencimiento** | `Fecha_Vencimiento__c` | Date | Cuándo vence la cuota. |
| **Fecha de Pago** | `Fecha_Pago__c` | Date | Cuándo se realizó el pago efectivo. |
| **Concepto** | `Concepto__c` | Text(200) | Ej: "Cuota 3 - Ciclo 2025-1" |
| **Período Académico** | `Periodo_Academico__c` | Picklist | 2024-1, 2024-2, 2025-1, etc. |
| **Método de Pago** | `Metodo_de_Pago__c` | Picklist | Transferencia, Efectivo, Tarjeta |
| **Cuota Vencida** | `Cuota_Vencida__c` | Checkbox | Auto-marcado por automatización |
| **Código Único** | `Codigo_Unico__c` | Text(50) | External ID + Unique |

### Paso 3: Regla de Validación Anti-Datos Incoherentes

El Grupo 6 ya tiene la regla `Prevent_Null_Payment_Data`. Confirmamos que debe conservarse y reforzarse.

**Objetivo**: Nunca permitir guardar un Cobro con Monto vacío o negativo.

1. Ve a **Object Manager** > **Cobro** > **Validation Rules**.
2. Busca `Prevent_Null_Payment_Data`. Si existe, verifica su fórmula. Si no existe, créala:
   - **Nombre**: `Prevenir_Datos_Invalidos_Cobro`
   - **Fórmula**:
     ```
     OR(
        ISNULL(Monto__c),
        Monto__c <= 0,
        ISNULL(Fecha_Vencimiento__c)
     )
     ```
   - **Mensaje de Error**: *"Los campos Monto y Fecha de Vencimiento son obligatorios y el monto debe ser mayor a cero."*

### Paso 4: Campo de Resumen en el Alumno (Deudas Vencidas)

Para que la Rectora pueda ver en la ficha del Alumno si tiene deudas pendientes, necesitamos actualizar automáticamente un campo en el Contacto.

> ⚠️ **Importante**: Un campo Roll-Up en `Contact` desde `Cobro` no es posible nativamente (porque la relación no es Master-Detail). Esta lógica debe implementarse mediante un **Record-Triggered Flow**.

**Lógica del Flow (For Admin - Nivel Avanzado)**:
- **Trigger**: Cuando se crea o modifica un `Cobro__c`.
- **Condición**: Si el `Estado__c` cambia a `Vencido`.
- **Acción**: Actualizar el campo `Deudas_Vencidas__c` en el `Contact` vinculado, cambiando su valor a `TRUE`.

Si el estado del Cobro vuelve a `Pagado`, un segundo camino del Flow actualiza el campo a `FALSE` (si no quedan más cobros vencidos).

### Paso 5: Configurar Acceso de Seguridad (Field-Level Security)

Los campos financieros de este objeto deben ser **invisibles** para los perfiles académicos.

1. Ve a **Setup** > **Profiles** > Perfil **Lumina Director** (Ej: Profesor, Bedelía).
2. Busca el objeto **Cobro** en la lista de permisos del perfil.
3. Desmarca **Read** (Lectura). Un Profesor **nunca** debe ver ni la existencia de un registro de pago.

---

## 🚀 Estrategia de Carga Masiva (Sprint 2)

Si se importa un histórico de Cobros:
1. **Clave de Cruce (Alumno)**: Use `Alumno__r:Numero_Documento__c` como External ID del Contact.
2. **Identificador Único (Self)**: Use `Codigo_Unico__c` como External ID del Cobro para operaciones UPSERT.

---

## ✅ Verificación de Éxito

1. Crea un Cobro con un Monto en cero (0). **Resultado esperado**: La Validation Rule debe bloquear el guardado.
2. Crea un Cobro válido (Monto > 0, con Fecha de Vencimiento) para un Alumno. Cambia el Estado a **Vencido**.
3. Verifica que el campo `Deudas_Vencidas__c` en el perfil del Alumno (Contacto) se marque automáticamente.
4. Intente acceder al objeto Cobro logueándote como un usuario con perfil **Lumina Profesor**. **Resultado esperado**: El objeto no debe ser visible.

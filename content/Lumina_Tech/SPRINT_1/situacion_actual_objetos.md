# Situación Actual de los Objetos (LuminaFinal - Equipo 6)

Este documento detalla la estructura real de los objetos y campos en la org de Salesforce actual (LuminaFinal), identificando las deficiencias y diferencias con el modelo teórico inicial, para servir como base en la reescritura de las guías de implementación.

## 1. Objetos Estándar Personalizados

### `Contact` (Renombrado a "Persona")
El objeto estándar `Contact` fue adaptado para manejar toda la información de los usuarios del sistema (tanto alumnos como potenciales deudores/leads). 

**Campos Personalizados Detectados:**
*   `Numero_Documento__c` (Texto - Id Externo, Único)
*   `Tipo_Documento__c` (Lista de selección)
*   `Rol__c` (Lista de selección) - *Se usa en lugar de Record Types.*
*   `Activo__c` (Casilla de verificación)
*   `Asistencia__c` (Porcentaje)
*   `Deudas_Vencidas__c` (Resumen/Roll-up Summary - COUNT Cobro)
*   `Estado_de_Pago_Alumno__c` (Fórmula)
*   `Fuente_de_Origen__c` (Lista de selección)
*   `Languages__c` y `Level__c`

**Deficiencias a Mejorar (Mejoras Propuestas):**
*   **Falta de Record Types:** El uso del picklist `Rol__c` debe ser reemplazado (o complementado fuertemente) por Record Types (`Alumno`, `Docente`, `Administrativo`) para poder asignar Page Layouts distintos. Actualmente, todos los roles ven los mismos campos (ej. "Deudas Vencidas" visible para Docentes).

---

## 2. Objetos Personalizados (Custom Objects)

El esquema de objetos personalizados fue implementado completamente en español, difiriendo del modelo inicial en inglés (Career/Subject/etc.).

**Listado de Objetos Personalizados Detectados:**
1.  **`Carrera__c`**
2.  **`Materia__c`**
3.  **`Inscripcion__c`** 
4.  **`Evaluacion__c`** *(Reemplaza al concepto de Exam__c)*
5.  **`Cobro__c`** *(Nuevo objeto relacionado con facturación/pagos, no contemplado en el ERD original)*

**Nota:** El objeto `Alumno__c` **no existe** en esta org. La arquitectura actual centraliza correctamente la identidad en el objeto `Contact`.

---

### Detalle de Campos por Objeto Personalizado

#### 1. `Carrera__c`
Objeto principal del catálogo académico.
*   `Codigo_de_carrera__c` *(Numeración automática - Id. externo)*
*   `Abreviatura__c` *(Texto - Id. externo, Único)*
*   `Facultad__c` *(Lista de selección)*
*   `Duracion_de_la_carrera__c` *(Lista de selección)*
*   `Habilitada_para_inscripciones__c` *(Casilla de verificación)*

#### 2. `Materia__c`
Asignaturas que pertenecen a una Carrera.
*   `Carrera__c` *(Relación Principal-Detalle a Carrera__c)*
*   `Codigo_Materia__c` *(Texto - Id. externo, Único)*
*   `Persona__c` *(Búsqueda a Contacto)* - *Nota: Probablemente usado para asignar un Profesor titular.*
*   `Estado__c` *(Casilla de verificación)*

#### 3. `Inscripcion__c`
Objeto de unión (Junction) entre el Alumno y la Materia.
*   `Alumno__c` *(Búsqueda a Contacto)*
*   `Materia__c` *(Búsqueda a Materia__c)*
*   `Periodo_Academico__c` y `Anio_Lectivo__c` *(Listas de selección)*
*   `Concepto__c` *(Lista de selección)*
*   `Estado__c` *(Casilla de verificación)*
*   **Asistencia:** `Present_Sessions__c`, `Total_Sessions__c` *(Resúmenes)* y `Porcentaje_de_Asistencia__c` *(Fórmula)*.
*   **Campos de auditoría/integración:** `Codigo_Unico__c`, `ID_Importacion__c`.

#### 4. `Evaluacion__c` (Reemplaza al concepto antiguo de Exam__c)
Maneja las calificaciones asociadas a una inscripción.
*   `Inscripci_n__c` *(Búsqueda a Inscripcion__c)*
*   **Notas:** `Examen_Parcial_1__c`, `Examen_Parcial_2__c`, `Examen_Final__c`, `Promedio_Final__c` *(Fórmula)*.
*   `Fecha_de_Examen__c` *(Fecha)*
*   `Tipo_de_Instancia__c` *(Lista de selección)*
*   `Peso_de_Evaluacion__c` *(Porcentaje)*
*   `Estado__c` *(Lista de selección)* y `Condicion__c` *(Fórmula)*.
*   *Posee múltiples campos fórmula para traer datos del estudiante (DNI, Email) y de la cursada (Materia, Profesor).*

#### 5. `Cobro__c`
Nuevo objeto para la gestión de tesorería/pagos.
*   `Alumno__c` *(Relación Principal-Detalle a Contacto)*
*   `Monto_Admin__c` *(Divisa)*
*   `Fecha_de_Pago__c` *(Fecha)*
*   `Cuota_Vencida__c` *(Casilla de verificación)*
*   `Metodo_Pago__c`, `Tipo_de_Cobro__c`, `Periodo_Academico__c` *(Listas de selección)*
*   `ID_Transaccion_Exterma__c` *(Texto - Id. externo)*

---

## 3. Reglas de Validación Detectadas (Data Quality)
Se extrajeron las validaciones activas en `LuminaFinal` mediante el Tooling API, demostrando un alto control de calidad de datos en español:

**En `Contact` (Identidad):**
*   `Validar_Formato_DNI`: El DNI debe contener 7 u 8 dígitos numéricos.
*   `Validar_Formato_CE`: La Cédula/Identidad Extranjera debe contener entre 6 y 12 caracteres.
*   `Validar_Formato_Pasaporte`: El Pasaporte debe tener entre 6 y 15 caracteres.
*   `No_numbers_in_names`: Los nombres y apellidos no pueden contener números.
*   `Validar_Mayoria_Edad`: La persona debe ser mayor de 18 años.

**En `Carrera__c`:**
*   `Nombre_Carrera_Solo_Letras`: El nombre de la carrera solo debe contener letras.

**En `Inscripcion__c`:**
*   `Materia_Obligatoria_Ciclo_Univ`: Debe seleccionar una Materia cuando el concepto es Ciclo universitario.

**En `Evaluacion__c`:**
*   `Rango_Notas_Examenes`: Solo se acepta notas del 0 al 10.

---

## 3. Conclusión Arquitectónica
El modelo real de `LuminaFinal` está muy avanzado y orientado a la madurez operativa (incluye control de pagos y ausentismo). 
Para las nuevas guías, el enfoque debe ser **adoptar este modelo como la fuente oficial de verdad**, actualizando el ERD y aplicando las mejores prácticas faltantes (específicamente la implementación de *Record Types* en `Contact` para reemplazar el picklist `Rol__c`).

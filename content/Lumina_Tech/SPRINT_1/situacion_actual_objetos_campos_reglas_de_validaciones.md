# Auditoría Técnica Integral (Org: LuminaRT - Grupo 3)
*Metadata extraída mediante Salesforce CLI / Tooling API*

Este documento consolida el análisis exhaustivo de la arquitectura implementada en la organización de prueba (`LuminaRT`). Cubre no solo la gestión de identidades, sino **todos los objetos personalizados** que componen el modelo académico, incluyendo sus campos y reglas de validación (Data Quality).

---

## 1. Objeto Estándar: Contacto (Persona)
*Gestiona la identidad digital unificada.*

### 🔹 Tipos de Registro (Record Types)
*   `Alumno`, `Profesor`, `Administrativo`, `Director`.

### 🔹 Campos Personalizados
*   `DNI__c` (Texto)
*   `Legajo__c` (Auto Numérico)
*   `Carrera__c` (Lookup a Carrera)
*   `Fecha_Ingreso__c` (Fecha)
*   `Estado_Academico__c` (Picklist)
*   `Email_Personal__c` (Email Único)
*   `Email_Institucional__c` (Fórmula de Texto)
*   `Usuario_Sistema__c` (Fórmula de Texto)
*   `Ciclo_Ingreso__c` (Fórmula de Texto)
*   `Level__c` (Picklist - Nivel Docente)
*   `Languages__c` (Texto - Idiomas Docente)

### 🚨 Reglas de Validación
1.  **`Carrera_Requerida_Alumno_Director`**: "La Carrera es obligatoria para alumnos y directores de carrera."
2.  **`Fecha_Ingreso_Requerida_Alumno`**: "La Fecha de Ingreso es obligatoria para alumnos."

---

## 2. Objeto: Carrera (`Carrera__c`)
*Objeto maestro (Master Data) para la oferta educativa.*

### 🔹 Campos Personalizados
*   `Abreviatura__c` (Texto - External ID)
*   `Tipo_Carrera__c` (Picklist)
*   `Modalidad__c` (Picklist)
*   `Turno__c` (Picklist)
*   `Duracion_Meses__c` (Número)
*   `Plan_de_Estudio__c` (URL)
*   `Estado__c` (Picklist)

---

## 3. Objeto: Materia (`Materia__c`)
*Asignaturas asociadas a las carreras.*

### 🔹 Campos Personalizados
*   `Carrera__c` (Master-Detail a Carrera)
*   `Tipo_Materia__c` (Picklist)
*   `Modalidad__c` (Picklist)
*   `Cuatrimestre__c` (Picklist o Número)
*   `Creditos__c` (Número)

---

## 4. Objeto: Alumno (`Alumno__c`) 
*(Nota: Este objeto custom fue implementado en esta org, aunque nuestra arquitectura final lo unificará en Contacto).*

### 🔹 Campos Personalizados
*   `DNI__c` (Texto - External ID)
*   `Carrera__c` (Lookup a Carrera)
*   `Estado_Academico__c` (Picklist)
*   `Fecha_Ingreso__c` (Fecha)
*   `Email_Personal__c` (Email Único)
*   `Ciclo_Ingreso__c` (Fórmula de Texto)

### 🚨 Reglas de Validación
1.  **`DNI_Numerico_8`**: "El DNI debe tener exactamente 8 dígitos numéricos."
2.  **`Formato_Email_Valido`**: "El formato del email es inválido (ej: nombre@dominio.com)."

---

## 5. Objeto: Inscripción (`Inscripcion__c`)
*Objeto de unión (Junction) entre Alumno y Materia.*

### 🔹 Campos Personalizados
*   `Alumno__c` (Master-Detail a Alumno)
*   `Materia__c` (Master-Detail a Materia)
*   `Carrera__c` (Fórmula o Lookup referencial)
*   `Fecha_de_Inscripcion__c` (Fecha/Hora)
*   `Tipo_Inscripcion__c` (Picklist)
*   `Estado__c` (Picklist)
*   `Observaciones__c` (Área de Texto)

### 🚨 Reglas de Validación
1.  **`Alumno_Activo_Para_Inscribir`**: "El alumno debe estar en estado Activo para inscribirse. Verifique que tenga la Matrícula y Cuota Mes 1 pagadas." *(Excelente validación financiera-académica).*
2.  **`Coherencia_Carrera_Materia`**: "La materia no pertenece a la carrera del alumno." *(Validación crítica de negocio).*

---

## 6. Objeto: Nota (`Nota__c`)
*Registro de evaluaciones.*

### 🔹 Campos Personalizados
*   `Inscripcion__c` (Master-Detail a Inscripción)
*   `Tipo__c` (Picklist: Parcial, Final, TP)
*   `Fecha__c` (Fecha)
*   `Asistio__c` (Checkbox)
*   `Calificacion__c` (Número 4,2)
*   `Ponderacion__c` (Porcentaje)
*   `Nota_Ponderada__c` (Fórmula Numérica: Calificacion * Ponderacion)
*   `Escala_Calificacion__c` (Fórmula de Texto: Aprobado/Reprobado)
*   `Observaciones__c` (Área de Texto)

### 🚨 Reglas de Validación
1.  **`Rango_Nota_Valida`**: "Calificación inválida. Debe ser entre 1 y 10."

---

## 7. Objeto: Asistencia (`Asistencia__c`)
*Control de presentismo.*

### 🔹 Campos Personalizados
*   `Inscripcion__c` (Lookup/Master-Detail a Inscripción)
*   `Fecha__c` (Fecha)
*   `Tipo_de_Clase__c` (Picklist: Teórica, Práctica)
*   `Estado__c` (Picklist: Presente, Ausente, Justificado)
*   `Observaciones__c` (Área de Texto)

---

## 💡 Conclusión Estratégica
El modelo de datos extraído de `LuminaRT` es extremadamente maduro. El uso intensivo de **Fórmulas** (para generar emails, usuarios y notas ponderadas) y la robustez de las **Reglas de Validación** (especialmente `Coherencia_Carrera_Materia` y `Alumno_Activo_Para_Inscribir`) demuestran una implementación de alta calidad técnica que servirá como pilar fundamental para reescribir nuestras guías de implementación.

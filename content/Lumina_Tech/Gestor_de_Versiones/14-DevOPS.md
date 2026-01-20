# 14-DevOPS.md - Control de Despliegues

**Origen**: DEV (`lumina-dev`)
**Destino**: QA (`lumina-qa`)
**Herramienta**: Change Sets (Simulado)

---

## 📦 Change Set: "Sprint1_Core_Academic"

**Estado**: Uploaded & Deployed
**Fecha**: 23 Enero 2026

### Componentes Incluidos

#### Custom Objects (5)
*   `Carrera__c`
*   `Materia__c`
*   `Alumno__c`
*   `Inscripcion__c`
*   `Examen__c`

#### Custom Fields (15+)
*   `Alumno__c.DNI__c`
*   `Alumno__c.Email__c`
*   `Examen__c.Nota__c`
*   `Inscripcion__c.Nota_Final__c`
*   ... (Todos los campos custom)

#### Profiles (2)
*   `Lumina_Profesor`
*   `Lumina_Administrativo`

#### Validation Rules (2)
*   `Examen__c.Nota_Rango_0_10`
*   `Alumno__c.DNI_Unico` (Field Property)

#### Apps / Tabs
*   App: `Gestión Académica Lumina`
*   Tabs: `Carreras`, `Materias`, `Alumnos`, `Inscripciones`

---

## ⚠️ Post-Deployment Steps (Manuales)
1.  **Activar App**: Verificar que la App sea visible para los perfiles clonados.
2.  **Cargar Datos Semilla**: Subir CSV de Carreras y Materias base (ya que los datos no viajan en Change Sets).

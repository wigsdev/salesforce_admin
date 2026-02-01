# 📚 Glosario de Términos Salesforce

**Propósito**: Referencia rápida de conceptos técnicos utilizados en el proyecto Lumina Tech.

---

## A

### API Name
Nombre único interno de un objeto, campo o componente en Salesforce. Siempre termina en `__c` para elementos personalizados.
- **Ejemplo**: `Carrera__c`, `Nota_Final__c`

---

## C

### Change Set
Paquete de metadatos que permite migrar configuraciones entre ambientes (Sandbox → Producción).
- **Ventaja**: No requiere código
- **Limitación**: Solo funciona entre orgs conectadas

### CRUD
Acrónimo de **Create, Read, Update, Delete**. Permisos básicos sobre objetos.
- **Nivel**: Perfil o Permission Set
- **Ejemplo**: Un Bedel tiene CRUD en Alumno, pero solo Read en Nota

---

## F

### FLS (Field-Level Security)
Control de visibilidad y edición a nivel de campo individual.
- **Opciones**: Visible, Read-Only, Hidden
- **Ejemplo**: El campo `Nota_Final__c` es Read-Only para Bedel, Edit para Profesor

### Formula Field
Campo calculado automáticamente mediante una expresión.
- **Tipos**: Text, Number, Date, Checkbox
- **Ejemplo**: `Estado_Cursada__c = IF(Nota_Final__c >= 6, "Aprobado", "Desaprobado")`

---

## G

### Governor Limits
Límites de ejecución impuestos por Salesforce para garantizar multi-tenancy.
- **Ejemplos**:
  - 100 consultas SOQL por transacción
  - 10 MB de heap size
  - 10,000 registros procesados por DML

---

## J

### Junction Object
Objeto que conecta dos objetos en una relación muchos-a-muchos mediante dos Master-Detail.
- **Ejemplo**: `Inscripcion__c` conecta `Alumno__c` con `Materia__c`

---

## L

### Lightning App
Aplicación personalizada con navegación, branding y pestañas específicas.
- **Componentes**: Logo, colores, tabs, perfiles asignados
- **Ejemplo**: "Gestión Académica Lumina"

### Lookup Relationship
Relación "floja" entre objetos. Si eliminas el padre, el hijo sobrevive.
- **Uso**: Relaciones opcionales o independientes
- **Ejemplo**: `Alumno__c` → `Biblioteca__c` (opcional)

---

## M

### Master-Detail Relationship
Relación "fuerte" entre objetos. Si eliminas el padre, el hijo se elimina automáticamente.
- **Características**:
  - Hereda seguridad del padre
  - Permite Roll-Up Summary Fields
  - Máximo 2 Master-Detail por objeto (para Junction)
- **Ejemplo**: `Materia__c` → `Carrera__c` (una materia no existe sin carrera)

### Metadata API
API que permite desplegar configuraciones mediante código (alternativa a Change Sets).
- **Herramientas**: SFDX, Ant Migration Tool
- **Ventaja**: Automatización y control de versiones

### MFA (Multi-Factor Authentication)
Autenticación de dos factores para reforzar seguridad de login.
- **Implementación**: Salesforce Authenticator App
- **Gestión**: Permission Set `Lumina_MFA_Access`

### My Domain
URL personalizada de la organización Salesforce.
- **Formato**: `https://lumina-university.my.salesforce.com`
- **Requisito**: Obligatorio para Lightning Web Components

---

## O

### OWD (Organization-Wide Defaults)
Configuración de seguridad base para cada objeto.
- **Opciones**:
  - **Private**: Solo el dueño ve el registro
  - **Public Read Only**: Todos ven, solo el dueño edita
  - **Public Read/Write**: Todos ven y editan
- **Ejemplo Lumina**: `Alumno__c = Private`, `Carrera__c = Public Read Only`

---

## P

### Permission Set
Conjunto de permisos adicionales que se asignan a usuarios sin modificar su perfil.
- **Ventaja**: Reutilizable y granular
- **Ejemplo**: `Lumina_MFA_Access` para habilitar MFA

### Profile
Conjunto base de permisos asignado a cada usuario.
- **Incluye**: CRUD, FLS, acceso a apps, permisos de sistema
- **Ejemplo**: Perfil "Bedel" vs Perfil "Profesor"

---

## R

### Roll-Up Summary Field
Campo en el objeto padre que calcula valores agregados de los hijos (solo en Master-Detail).
- **Funciones**: SUM, COUNT, MIN, MAX, AVG
- **Ejemplo**: `Total_Alumnos__c` en `Carrera__c` cuenta las inscripciones

---

## S

### Sandbox
Copia del ambiente de producción para desarrollo y pruebas.
- **Tipos**:
  - **Developer**: Solo metadata, sin datos
  - **Developer Pro**: Metadata + datos limitados
  - **Partial Copy**: Metadata + muestra de datos
  - **Full**: Copia completa (solo Enterprise+)

### Schema Builder
Herramienta visual para diseñar y visualizar el modelo de datos.
- **Uso**: Crear objetos, ver relaciones, exportar diagrama

### SoD (Segregation of Duties)
Principio de seguridad que separa responsabilidades críticas.
- **Ejemplo Lumina**: Bedel inscribe alumnos, Profesor califica (no pueden hacer ambas)

---

## V

### Validation Rule
Regla que impide guardar un registro si no cumple una condición.
- **Sintaxis**: Fórmula booleana (TRUE = error)
- **Ejemplo**: `OR(Nota_Final__c < 0, Nota_Final__c > 10)` → "Nota debe estar entre 0 y 10"

---

## Referencias Cruzadas

- **Guías de Implementación**: [../Guias_Implementacion/](../Guias_Implementacion/)
- **Manuales de Ejecución**: [../Manuales_de_Ejecucion/](../Manuales_de_Ejecucion/)
- **Tutoriales por Rol**: [../Tutoriales_por_Rol/](../Tutoriales_por_Rol/)

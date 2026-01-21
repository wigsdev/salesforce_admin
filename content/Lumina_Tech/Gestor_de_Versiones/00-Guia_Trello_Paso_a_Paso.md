# 📋 Guía Passo a Paso: Configuración de Trello - Sprint 1

Esta guía te ayudará a configurar el tablero de gestión de proyectos para **Lumina Tech**, alineado con la metodología ágil y las mejores prácticas de Salesforce.

---

## 🎯 Objetivo
Configurar un tablero profesional para simular el ciclo de vida de desarrollo (SDLC) y cargar las 7 Historias de Usuario del MVP.

---

## 🏗️ Paso 1: Configuración del Tablero

### 1.1 Crear Tablero
*   **Título**: `Proyecto Lumina Tech - [Tu Nombre]`.
*   **Visibilidad**: Espacio de Trabajo.
*   **Fondo**: Elige uno profesional (Oficina/Tecnología).

### 1.2 Definir Columnas (Organización Estricta)
Configura tu tablero con las siguientes 8 columnas, en este orden exacto:

1.  **Backlog** - Todas las historias de usuario identificadas
2.  **Sprint Backlog** - HU seleccionadas para el sprint actual
3.  **En Progreso** - Trabajo activo
4.  **SF Desarrollo** - Configuración en Sandbox
5.  **SF QA** - Pruebas internas
6.  **Aprobación TL** - Revisión del Team Lead
7.  **SF Producción** - Despliegue final
8.  **Terminado** - Completado y validado

---

## 🏷️ Paso 2: Etiquetas (Categorías)

Usa etiquetas para identificar el tipo de requerimiento visualmente:
*   🔴 **Seguridad** (Permisos, Acceso, Roles).
*   🔵 **Académico** (Funcionalidad Core del negocio).
*   🟣 **Data Quality** (Validaciones, Reglas).

---

## � Paso 3: Carga de Historias de Usuario (Sprint 1)

Copia y pega el siguiente contenido en tarjetas individuales dentro de la columna **Sprint Backlog**.

> **💡 Tip**: El título de la tarjeta debe ser el código (HU-XXX) y un resumen breve.

### HU-001: Privacidad de Alumnos
**Título en Trello**: `HU-001 - Visibilidad Privada de Alumnos`
**Etiqueta**: 🔴 Seguridad

**Descripción (Copia y pega esto)**:
```markdown
**Como**: Profesor de la Universidad.
**Quiero**: Ver únicamente los alumnos de mis propios cursos.
**Para**: Proteger la privacidad de los estudiantes y evitar confusiones con otras materias.

---
### Criterios de Aceptación:
- [ ] La configuración de OWD (Organization-Wide Defaults) para el objeto Alumno__c es "Private".
- [ ] Un usuario con perfil "Lumina_Profesor" NO puede ver alumnos que no le fueron asignados.
- [ ] El Administrador del sistema mantiene acceso total a todos los registros.
```

### HU-002: Integridad de Notas
**Título en Trello**: `HU-002 - Bloqueo de Edición de Notas`
**Etiqueta**: 🔴 Seguridad

**Descripción**:
```markdown
**Como**: Administrativo de Lumina.
**Quiero**: Poder ver el historial académico pero NO modificar las notas.
**Para**: Evitar fraudes académicos o errores de tipeo involuntarios.

---
### Criterios de Aceptación:
- [ ] El campo "Nota" (Examen__c) es de Solo Lectura para el perfil "Lumina_Administrativo".
- [ ] El perfil "Lumina_Profesor" tiene permisos de Escritura sobre el campo Nota.
- [ ] Se verificó usando "Login As" (Iniciar sesión como otro usuario).
```

### HU-003: Gestión de Inscripciones
**Título en Trello**: `HU-003 - Relación Alumno-Materia`
**Etiqueta**: 🔵 Académico

**Descripción**:
```markdown
**Como**: Secretario Académico.
**Quiero**: Inscribir a un alumno existente en una materia ofertada.
**Para**: Registrar formalmente su cursada y generar el acta.

---
### Criterios de Aceptación:
- [ ] Existe el objeto "Inscripcion__c" como conector (Junction Object).
- [ ] No se puede crear una inscripción sin seleccionar un Alumno y una Materia (Master-Detail).
- [ ] El nombre de la inscripción se autogenera o sigue un formato lógico.
```

### HU-004: Registro de Exámenes
**Título en Trello**: `HU-004 - Carga de Notas Parciales`
**Etiqueta**: 🔵 Académico

**Descripción**:
```markdown
**Como**: Profesor Titular.
**Quiero**: Registrar la nota de un examen parcial asociado a una inscripción.
**Para**: Evaluar el desempeño del alumno durante el cuatrimestre.

---
### Criterios de Aceptación:
- [ ] El objeto "Examen__c" es hijo de "Inscripcion__c".
- [ ] Se puede registrar la fecha del examen.
- [ ] El sistema permite diferenciar entre "Parcial" y "Final" (Picklist).
```

### HU-005: Calidad de Email
**Título en Trello**: `HU-005 - Validación de Email`
**Etiqueta**: 🟣 Data Quality

**Descripción**:
```markdown
**Como**: Equipo de Marketing.
**Quiero**: Que el sistema rechace correos electrónicos con formato inválido.
**Para**: Asegurar que las comunicaciones oficiales lleguen a los alumnos.

---
### Criterios de Aceptación:
- [ ] El campo Email usa el tipo de dato "Email" estándar de Salesforce.
- [ ] Al intentar guardar "juan.perez" (sin @) el sistema arroja error.
- [ ] Se permiten dominios corporativos (@lumina.edu).
```

### HU-006: Rango de Notas Lógico
**Título en Trello**: `HU-006 - Validación de Rango de Notas`
**Etiqueta**: 🟣 Data Quality

**Descripción**:
```markdown
**Como**: Rectoría.
**Quiero**: Impedir la carga de notas negativas o mayores a 10.
**Para**: Mantener la consistencia estadística de los promedios.

---
### Criterios de Aceptación:
- [ ] Existe una Regla de Validación (Validation Rule) activa.
- [ ] Al ingresar "-1" el sistema muestra el error: "La nota debe estar entre 0 y 10".
- [ ] Al ingresar "11" el sistema bloquea el guardado.
```

### HU-007: Identidad Obligatoria
**Título en Trello**: `HU-007 - DNI Obligatorio`
**Etiqueta**: 🟣 Data Quality

**Descripción**:
```markdown
**Como**: Departamento Legal.
**Quiero**: Que sea imposible crear un legajo de alumno sin su número de documento.
**Para**: Cumplir con las normativas ministeriales de identificación.

---
### Criterios de Aceptación:
- [ ] El campo DNI está marcado como "Required" a nivel de objeto o Page Layout.
- [ ] Al intentar guardar un alumno vacío, aparece el error estándar de campo obligatorio.
```

---

## 🚀 Protip: Metodología de Trabajo

1.  Mueve **solo 1 o 2 tarjetas** a la columna **Doing**. (No hagas todo a la vez).
2.  Cuando termines la configuración en Salesforce, mueve la tarjeta a **QA**.
3.  Imagina que eres el Tester: ¿Cumple los "Criterios de Aceptación"?
4.  Si sí -> Mover a **Done**. ¡Felicidades! �

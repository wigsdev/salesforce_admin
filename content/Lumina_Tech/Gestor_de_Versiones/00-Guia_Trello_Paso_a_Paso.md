# 📋 Guía Paso a Paso: Gestión del Sprint 1 en Trello

Esta guía te acompañará para configurar el tablero de Trello del proyecto **Universidad Lumina Tech**, simulando el entorno de trabajo real de un equipo Salesforce.

---

## 🎯 Objetivo
Al finalizar esta guía tendrás:
- ✅ Un tablero llamado `Universidad Lumina Tech - Sprint 1`.
- ✅ 3 Tarjetas de Historias de Usuario (HU-001, HU-002, HU-003) cargadas.
- ✅ Etiquetas de Épicas (Seguridad, Académico) configuradas.

**Tiempo estimado**: 20 minutos.

---

## 📝 PARTE 1: Configuración del Tablero

### Paso 1.1: Crear el tablero
1.  En Trello, haz clic en **"Crear nuevo tablero"**.
2.  **Título**: `Universidad Lumina Tech - Sprint 1`.
3.  **Fondo**: Elige un color sólido (ej: Violeta/Azul) o foto de oficina.
4.  **Visibilidad**: Privado o Espacio de Trabajo.

### Paso 1.2: Definir Columnas (Flujo Agile Completo)
Elimina las listas por defecto y crea estas 7 columnas en orden:

1.  **Backlog** (Historias de Usuario Identificadas)
2.  **Sprint Backlog** (Seleccionadas para el Sprint)
3.  **En Progreso** (Diseño y Configuración)
4.  **SF Desarrollo** (Ya en Sandbox, listo para pruebas unitarias)
5.  **SF QA** (Tester validando Criterios de Aceptación)
6.  **Aprobación TL** (Revisión de Estándares - Naming Conventions)
7.  **Terminado** (Listo para Demo / Producción)

---

## 🏷️ PARTE 2: Etiquetas (Épicas)
Vamos a categorizar las tareas por "Módulo Funcional".

1.  Abre el menú > **Etiquetas**.
2.  Crea o edita las siguientes:
    *   🔴 **Seguridad** (Para HU-001 y HU-002)
    *   🔵 **Académico** (Para HU-003)
    *   🟣 **Calidad de Datos** (Para Validaciones)

---

## 📌 PARTE 3: Carga de Historias de Usuario

Vamos a crear las tarjetas reales del proyecto Lumina.

### 🔴 HU-001: Visibilidad de Alumnos (Seguridad)

1.  En la columna **Backlog**, click en "+ Añadir tarjeta".
2.  **Título**: `(3) HU-001 - Visibilidad Privada de Alumnos`.
3.  Entra a la tarjeta y en **Descripción** pega esto:

```markdown
**Como**: Profesor de Lumina Tech.
**Quiero**: Ver únicamente los alumnos de mis cursos asignados.
**Para**: Proteger la privacidad de los estudiantes y no viciar las listas.

---
### 🔧 Solución Técnica
- **Objeto**: Alumno__c
- **Configuración**: OWD (Organization-Wide Defaults) en "Private".
- **Sharing**: Reglas de compartición basadas en asignación de materia.
```

4.  **Checklist (Criterios de Aceptación)**:
    *   [ ] OWD de Alumno está en Private.
    *   [ ] Un Profesor no ve alumnos de otros colegas.
    *   [ ] Un Admin puede ver todos los alumnos.

### 🔴 HU-002: Restricción de Notas (Seguridad)

1.  Nueva Tarjeta: `(3) HU-002 - Bloqueo de Edición de Notas`.
2.  **Etiquetas**: 🔴 Seguridad.
3.  **Descripción**:

```markdown
**Como**: Administrativo.
**Quiero**: Ver el legajo del alumno pero NO poder modificar sus notas.
**Para**: Evitar fraudes o errores involuntarios.

---
### 🔧 Solución Técnica
- **Herramienta**: FLS (Field-Level Security).
- **Campo**: Examen__c.Nota__c
- **Perfil**: Lumina_Administrativo (Read-Only).
```

4.  **Checklist**:
    *   [ ] Perfil Administrativo ve el campo Nota "Grisado" (Solo lectura).
    *   [ ] Perfil Profesor puede editar la Nota.

### 🔵 HU-003: Estructura de Cursada (Académico)

1.  Nueva Tarjeta: `(5) HU-003 - Gestión de Inscripciones`.
2.  **Etiquetas**: 🔵 Académico.
3.  **Descripción**:

```markdown
**Como**: Secretario Académico.
**Quiero**: Inscribir un alumno a una materia y guardar su estado (Cursando/Aprobado).
**Para**: Tener la historia académica completa.

---
### 🔧 Solución Técnica
- **Objeto**: Inscripcion__c (Junction Object).
- **Relaciones**: Master-Detail a Alumno y Materia.
- **Campos**: Ciclo Lectivo, Estado, Nota Final.
```

### 🔵 HU-004: Gestión de Exámenes (Académico)

1.  Nueva Tarjeta: `(5) HU-004 - Registro de Parciales`.
2.  **Etiquetas**: 🔵 Académico.
3.  **Descripción**:

```markdown
**Como**: Profesor.
**Quiero**: Cargar la nota de un parcial a un alumno inscrito.
**Para**: Evaluar su desempeño en el cuatrimestre.

---
### 🔧 Solución Técnica
- **Objeto**: Examen__c (Detail de Inscripción).
- **Campos**: Nota (0-10), Fecha, Tipo (Parcial/Final).
```

### 🟣 HU-005: Calidad de Email (Data Quality)

1.  Nueva Tarjeta: `(2) HU-005 - Validación de Correo`.
2.  **Etiquetas**: 🟣 Calidad de Datos.
3.  **Descripción**:

```markdown
**Como**: Admisión.
**Quiero**: Que el sistema rechace emails sin arroba o con comas.
**Para**: Evitar rebotes en notificaciones.

---
### 🔧 Solución Técnica
- **Campo**: Email estándar.
- **Validación Manual**: Probar inputs inválidos ("juan,perez").
```

### 🟣 HU-006: Integridad de Notas (Data Quality)

1.  Nueva Tarjeta: `(2) HU-006 - Rango de Notas Lógico`.
2.  **Etiquetas**: 🟣 Calidad de Datos.
3.  **Descripción**:

```markdown
**Como**: Rectoría.
**Quiero**: Impedir que se carguen notas menores a 0 o mayores a 10.
**Para**: Mantener la consistencia estadística.

---
### 🔧 Solución Técnica
- **Validation Rule**: Nota < 0 || Nota > 10.
- **Error Message**: "La nota debe ser entre 0 y 10".
```

### 🟣 HU-007: Identidad Obligatoria (Data Quality)

1.  Nueva Tarjeta: `(1) HU-007 - DNI Obligatorio`.
2.  **Etiquetas**: 🟣 Calidad de Datos.
3.  **Descripción**:

```markdown
**Como**: Legal.
**Quiero**: Que Alumno requiera DNI para guardarse.
**Para**: Cumplir normativa.

---
### 🔧 Solución Técnica
- **Schema**: Field DNI Required = System Level.
```

---

## 🚀 PARTE 4: Lanzamiento del Sprint

Simulemos que empieza la semana de trabajo.

1.  Mueve las tarjetas **HU-001** y **HU-002** de "Backlog" a **"Sprint Backlog"**.
2.  Arrastra la **HU-001** a **"Doing"**. ¡Has empezado a trabajar!

### Reglas de Oro del Profesor
*   **WIP Limit**: No tengas más de 2 tarjetas en "Doing" a la vez.
*   **Evidencia**: Cuando termines una tarea, adjunta una captura de pantalla de Salesforce en la tarjeta antes de pasarla a "QA".

---

## 📊 Glosario Trello-Salesforce
*   **Card (Tarjeta)** = User Story (Requerimiento).
*   **Checklist** = Acceptance Criteria (Lo que prueba el QA).
*   **Description** = Análisis Funcional y Técnico.
*   **Member** = Quién lo está configurando en Salesforce.

¡Listo! Ya tienes tu entorno de gestión profesional configurado. 🎓

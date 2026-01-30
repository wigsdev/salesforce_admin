# 📋 Guía Passo a Paso: Configuración de Trello - Sprint 1 (Full Scope)

Esta guía te ayudará a configurar el tablero de gestión de proyectos para **Lumina Tech**, garantizando que refleje el 100% del trabajo realizado en los 4 días del Sprint Inicial.

---

## 🎯 Objetivo
Visualizar el flujo de trabajo completo, desde el Modelado de Datos (Día 1) hasta la Seguridad Avanzada (Día 4), totalizando **11 Historias de Usuario**.

---

## 🏗️ Paso 1: Configuración del Tablero

### 1.1 Crear Tablero
*   **Título**: `Lumina Tech - Sprint 1 (MVP)`.
*   **Visibilidad**: Espacio de Trabajo.

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

## 🏷️ Paso 2: Etiquetas (Categorías) - Semáforo
*   🔵 **Modelado** (Datos Core - Día 1)
*   🟢 **Branding** (UI/UX - Día 2)
*   🟣 **Data Quality** (Validaciones - Día 3)
*   🔴 **Seguridad** (Accesos - Día 4)

---

## 🃏 Paso 3: Carga de Historias de Usuario (Backlog Consolidado)

Copia estas tarjetas en tu columna **Sprint Backlog**.

### 📅 DÍA 1: Cimientos de Datos (🔵 Modelado)

**HU-001: Gestión de Inscripciones**
```markdown
**Como**: Director de Carrera.
**Quiero**: Vincular Alumnos con Materias usando una fecha y estado.
**Para**: Tener la trazabilidad del historial académico.
---
**Criterios (DoD)**:
- [ ] Objeto `Inscripción` creado (Master-Detail).
- [ ] No permite huérfanos (Borrar Alumno borra Inscripción).
```

**HU-002: Unicidad de Identidad**
```markdown
**Como**: Sistema.
**Quiero**: Impedir la carga de dos alumnos con el mismo DNI.
**Para**: Mantener la integridad de la base.
---
**Criterios**:
- [ ] Campo `DNI` marcado como Unique (Case Insensitive).
- [ ] Campo `DNI` marcado como External ID.
```

**HU-003: Integridad de Notas**
```markdown
**Como**: Administrativo.
**Quiero**: Cargar notas con precisión decimal (Ej: 7.50).
**Para**: Calcular promedios exactos.
---
**Criterios**:
- [ ] Campo `Nota` tipo Number(2,2).
- [ ] Validación básica de tipo de dato.
```

### 📅 DÍA 2: Identidad Visual (🟢 Branding)

**HU-004: Dominio Institucional**
```markdown
**Como**: Usuario de Negocio.
**Quiero**: Ver `lumina-university` en la URL.
**Para**: Sentir confianza en el sitio.
---
**Criterios**:
- [ ] My Domain desplegado y activo.
- [ ] Login screen personalizado.
```

**HU-005: Look & Feel**
```markdown
**Como**: Equipo de Marketing.
**Quiero**: Ver el azul corporativo (`#005A9C`) en el encabezado.
**Para**: Reforzar la marca.
---
**Criterios**:
- [ ] Theme creado y activado.
- [ ] Logo cargado en la barra de navegación.
```

**HU-006: App Central**
```markdown
**Como**: Profesor.
**Quiero**: Un acceso directo "Gestión Académica" en el lanzador.
**Para**: No perder tiempo buscando objetos sueltos.
---
**Criterios**:
- [ ] Lightning App creada.
- [ ] Tabs: Alumnos, Materias, Inscripciones.
```

### 📅 DÍA 3: Calidad de Datos (🟣 Data Quality)

**HU-007: Validación de Email**
```markdown
**Como**: Sistema de Notificaciones.
**Quiero**: Rechazar correos sin "@" o dominio incompleto.
**Para**: Evitar rebotes (Hard Bounce).
---
**Criterios**:
- [ ] Regex activa: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$`.
```

**HU-008: Lógica de Notas**
```markdown
**Como**: Rectoría.
**Quiero**: Bloquear notas menores a 0 o mayores a 10.
**Para**: Evitar errores de dedo críticos.
---
**Criterios**:
- [ ] Validation Rule activa.
- [ ] Mensaje de error amigable: "La nota debe estar entre 0 y 10".
```

### 📅 DÍA 4: Seguridad Zero Trust (🔴 Seguridad)

**HU-009: Matriz de Privacidad (OWD)**
```markdown
**Como**: Oficial de Privacidad.
**Quiero**: Que los alumnos sean privados por defecto.
**Para**: Cumplir leyes de protección de datos.
---
**Criterios**:
- [ ] OWD Alumno = Private.
- [ ] Test con usuario Profesor (No debe ver nada al inicio).
```

**HU-010: Acceso MFA**
```markdown
**Como**: CISO.
**Quiero**: Exigir autenticador en el login.
**Para**: Prevenir robo de credenciales.
---
**Criterios**:
- [ ] Permission Set "MFA" creado.
- [ ] Asignado a usuarios de prueba.
```

**HU-011: Segregación de Perfiles (FLS)**
```markdown
**Como**: Auditoría.
**Quiero**: Que Bedelía vea notas pero NO las toque.
**Para**: Evitar corrupción académica.
---
**Criterios**:
- [ ] Perfil Bedel: Read-Only en `Nota__c`.
- [ ] Perfil Profe: Edit en `Nota__c`.
```

---

## 🚀 Protip: Simulación de Sprint
Al cargar estas tarjetas, mueve todas a **Sprint Backlog**.
Luego, simula el paso de los días moviendo de a 3 tarjetas a **Done**.
¡Así verás cómo "quema" el Sprint (Burndown Chart)!

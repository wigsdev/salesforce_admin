# 🗓️ Plan de Trabajo: Sprint 1 (Lumina Tech)
**Objetivo**: "Zero-to-Strategy" - Implementación del Core Académico.
**Referencia Metodológica**: `00-GUIA_METODOLOGICA.md`

---

## 🗺️ Roadmap de Ejecución (4 Semanas)

### 🚩 Semana 1: Definición Estratégica
*Focus: Entender el problema legal de la Rectora.*
- [x] **Kick-off**: Lectura de `SPRINT 1.md`.
- [x] **Ingeniería de Requerimientos**:
    - Generar `01-Business_Analyst.md` (Matriz de Trazabilidad).
    - Detectar HU críticas: `HU-001` (Privacidad) y `HU-007` (DNI Obligatorio).
- [x] **Setup de Herramientas**:
    - Configurar Trello según `00-Guia_Trello_Paso_a_Paso.md`.

### 🛠️ Semana 2: Arquitectura y Diseño
*Focus: Evitar deuda técnica.*
- [ ] **Diseño de Datos (`02-Consultant`)**:
    - Decidir Junction Object (`Inscripcion__c`) vs Lookup directo.
    - Definir Naming Conventions (ej: `Ciclo_Lectivo__c`).
- [ ] **Investigación (`06-Investigaciones`)**:
    - Prototipar validación de email (Regex).

### ⚙️ Semana 3: Construcción (Salesforce)
*Focus: Configuración robusta.*
- [ ] **Data Model**:
    - Crear Objetos: `Carrera`, `Materia`, `Alumno`.
    - **Hito Crítico**: Crear Junction Object `Inscripción`.
- [ ] **Calidad de Datos (`HU-005`, `HU-006`)**:
    - Activar Reglas de Validación: "Nota 1-10" y "Email Format".
- [ ] **Seguridad (`HU-001`)**:
    - Configurar OWD = Private.
    - Crear Perfiles Custom: `Lumina_Profesor`, `Lumina_Admin`.

### 🧪 Semana 4: Aseguramiento de Calidad
*Focus: Romper la app.*
- [ ] **Validación Funcional (`04-QA`)**:
    - Ejecutar `TC-DATA-04` (Email inválido).
    - Verificar visibilidad cruzada entre profesores.
- [ ] **Entrega**:
    - Generar `GUIA_USUARIO.md` en PDF.
    - Demo Final a Dra. Vance.

---

## 🚦 Semáforo de Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| **Modelo de Datos Erróneo** | Media | Crítico | Validación temprana del ERD en Semana 2. |
| **Fuga de Datos (Privacidad)** | Alta | Legal | Testing intensivo de Sharing Rules (Semana 4). |
| **Resistencia al Cambio** | Media | Medio | Entregar una `GUIA_USUARIO.md` muy clara. |

---

## 📊 Definition of Done (DoD) del Sprint
1.  [ ] Todos los objetos core creados y relacionados.
2.  [ ] Validaciones activas impidiendo datos basura.
3.  [ ] Al menos 1 caso de prueba fallido y corregido (evidencia de QA).
4.  [ ] Documentación `01` a `04` completa y sincronizada.

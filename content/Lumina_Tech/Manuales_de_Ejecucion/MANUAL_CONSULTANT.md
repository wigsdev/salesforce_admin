# 🏗️ Manual de Ejecución: Salesforce Consultant

**Tu Misión**: Diseñar antes de construir. Eres el arquitecto de la solución. El Admin ejecuta, pero tú defines el "cómo". Transformas Requerimientos (BA) en Soluciones Técnicas (Admin).

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Input (BA)** | Recibes el "Qué" (HU: "Quiero seguridad"). |
| 🎨 **DESIGN** | **Tu Turno** | Diseñas el modelo (ERD), relaciones y seguridad (OWD). |
| 👋 **HANDOFF** | **Output (Admin)** | Entregas el diseño técnico listo para configurar. |

---

## 📅 CRONOGRAMA DE ARQUITECTURA (Sprint 1)

### 📅 DÍA 0: Análisis & Estrategia
*Objetivo: Definir los cimientos antes de poner el primer ladrillo.*

1.  **Definición de Entidades Core**
    *   🎨 **DESIGN**: Identifica los objetos necesarios.
        *   `Carrera` (Padre)
        *   `Materia` (Master-Detail de Carrera)
        *   `Alumno` (Entidad Principal)
        *   `Inscripcion` (Junction Object: Alumno <-> Materia)
        *   `Nota` y `Asistencia` (Hijos de Inscripcion)
    *   *Decisión*: Usar Master-Detail para heredar seguridad y permitir Roll-Up Summaries.

2.  **Estrategia de Seguridad (Zero Trust)**
    *   🎨 **DESIGN**: Define el nivel base (OWD).
        *   `Alumno` = **Private** (Nadie ve nada).
        *   `Inscripcion` = **Controlled by Parent** (Hereda de Alumno/Materia).
        *   `Carrera` = **Public Read Only** (Catálogo visible).

---

### 📅 DÍA 1: Diseño de Datos
*Misión: Estructurar la base de datos.*

#### 🎨 Diseño: Modelo Académico (HU-001, HU-002, HU-003)
*   **Decisiones Técnicas**:
    *   **Identidad**: Usar `Auto-Number` para ID interno y `DNI__c` (Unique, External ID) como ID legal.
    *   **Inscripción**: Campo `Comision__c` debe ser **Picklist** (Mañana A/B, etc.) para evitar "data irrelevante".
    *   **Notas**: Objetos `Nota__c` y `Asistencia__c` con Lookup obligatorio a `Inscripcion__c`.

---

### 📅 DÍA 2: Diseño de Experiencia (UX)
*Misión: Branding y Usabilidad.*

#### 🎨 Diseño: Look & Feel (HU-004, HU-005, HU-006)
*   **Decisiones Técnicas**:
    *   **Dominio**: `lumina-tech-university`. Es requisito para componentes custom futuros.
    *   **App**: "Gestión Académica Lumina". Solo dejar objetos Core (Alumnos, Carreras, Materias, Inscripciones, Notas, Asistencias).
    *   **Theme**: Color Azul `#005A9C`. Logo de alta resolución en Login.

---

### 📅 DÍA 3: Diseño de Calidad (Data Quality)
*Misión: Blindaje de datos.*

#### 🎨 Diseño: Validaciones (HU-007, HU-008, HU-009)
*   **Decisiones Técnicas**:
    *   **Email**: Usar Regex `^[a-zA-Z0-9._%+-]+@lumina\\.edu$` para forzar dominio institucional.
    *   **Notas**: Validation Rule `OR(Grade < 1, Grade > 10)`. No usar Triggers (Keep it simple).
    *   **Asistencia**: Calcular `% Asistencia` con fórmula y usar otra fórmula texto para el "Semáforo" (Libre/Regular).

---

### 📅 DÍA 4: Diseño de Seguridad Avanzada
*Misión: Permisos y Auditoría.*

#### 🎨 Diseño: Matriz de Acceso (HU-010, HU-011, HU-012)
*   **Decisiones Técnicas**:
    *   **Perfiles**:
        *   `Lumina_Professor`: Puede editar `Nota_Final__c`, pero NO ve `DNI__c` (FLS).
        *   `Lumina_Registrar`: Puede ver `DNI__c`, pero `Nota_Final__c` es Read-Only.
    *   **MFA**: Usar **Permission Set** `Lumina_MFA_Required` en lugar de activarlo en el perfil (mayor flexibilidad).
    *   **Visibilidad**: OWD `Private` para `Alumno`. Sharing Rules basadas en Owner.

---

## 💡 Pro-Tips de Consultoría

1.  **Clicks not Code**: Siempre prioriza configuración (Validation Rules, Flows) sobre código (Apex). Es más barato de mantener.
2.  **Escalabilidad**: `Asistencia__c` ya implementado como hijo de `Inscripcion__c`. En el futuro se pueden agregar tipos de clase y automatizaciones adicionales.
3.  **Documentación**: Tu entregable no es la configuración, es el **Diseño**. El Admin solo sigue tus planos.

---

## 📚 Recursos Relacionados
- 📘 **Tutorial de Rol**: [02-Rol_Salesforce_Consultant.md](../Tutoriales_por_Rol/02-Rol_Salesforce_Consultant.md)
- 📘 **Gestor de Versiones**: [02-Salesforce_Consultant.md](../Gestor_de_Versiones/02-Salesforce_Consultant.md)
- 📘 **Glosario**: [GLOSARIO.md](../GLOSARIO.md)
- 📊 **Diagrama ERD**: [DIAGRAMA_ERD.md](../DIAGRAMA_ERD.md)
- 🛡️ **Diagrama Seguridad**: [DIAGRAMA_SEGURIDAD.md](../DIAGRAMA_SEGURIDAD.md)

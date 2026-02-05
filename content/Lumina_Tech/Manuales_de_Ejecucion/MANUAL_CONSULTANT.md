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
        *   `Career` (Padre)
        *   `Subject` (Hijo de Career)
        *   `Student` (Entidad Principal)
        *   `Enrollment` (Junction Object: Student <-> Subject)
    *   *Decisión*: Usar Master-Detail para heredar seguridad y permitir Roll-Up Summaries.

2.  **Estrategia de Seguridad (Zero Trust)**
    *   🎨 **DESIGN**: Define el nivel base (OWD).
        *   `Student` = **Private** (Nadie ve nada).
        *   `Enrollment` = **Controlled by Parent** (Hereda de Student/Subject).
        *   `Career` = **Public Read Only** (Catálogo visible).

---

### 📅 DÍA 1: Diseño de Datos
*Misión: Estructurar la base de datos.*

#### 🎨 Diseño: Modelo Académico (HU-001, HU-002, HU-003)
*   **Decisiones Técnicas**:
    *   **Identidad**: Usar `Auto-Number` para ID interno y `National_ID__c` (8 dígitos, Unique) como ID legal.
    *   **Inscripción**: Campo `Commission` debe ser **Picklist** (Morning A/B, etc.) para evitar "data irrelevante".
    *   **Notas**: Campo `Final_Grade__c` requiere History Tracking para auditoría.

---

### 📅 DÍA 2: Diseño de Experiencia (UX)
*Misión: Branding y Usabilidad.*

#### 🎨 Diseño: Look & Feel (HU-004, HU-005, HU-006)
*   **Decisiones Técnicas**:
    *   **Dominio**: `lumina-university`. Es requisito para componentes custom futuros.
    *   **App**: "Gestión Académica". Limpiar Tabs irrelevantes (Tasks, Notes). Solo dejar objetos Core.
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
        *   `Lumina Professor`: Puede editar `Final_Grade__c`, pero NO ve `National_ID__c` (FLS).
        *   `Lumina Registrar`: Puede ver `National_ID__c`, pero `Final_Grade__c` es Read-Only.
    *   **MFA**: Usar **Permission Set** `Lumina_MFA_Access` en lugar de activarlo en el perfil (mayor flexibilidad).
    *   **Visibilidad**: Crear **Sharing Rule** basada en criterios: "Si soy el Owner de la Materia, ver sus Inscripciones".

---

## 💡 Pro-Tips de Consultoría

1.  **Clicks not Code**: Siempre prioriza configuración (Validation Rules, Flows) sobre código (Apex). Es más barato de mantener.
2.  **Escalabilidad**: Al diseñar `Enrollment` como Junction, permitimos un futuro objeto `Attendance` (Asistencia diaria) vinculado a la misma inscripción.
3.  **Documentación**: Tu entregable no es la configuración, es el **Diseño**. El Admin solo sigue tus planos.

---

## 📚 Recursos Relacionados
- 📘 **Tutorial de Rol**: [02-Rol_Salesforce_Consultant.md](../Tutoriales_por_Rol/02-Rol_Salesforce_Consultant.md)
- 📘 **Gestor de Versiones**: [02-Salesforce_Consultant.md](../Gestor_de_Versiones/02-Salesforce_Consultant.md)
- 📘 **Glosario**: [GLOSARIO.md](../GLOSARIO.md)
- 📊 **Diagrama ERD**: [DIAGRAMA_ERD.md](../DIAGRAMA_ERD.md)
- 🛡️ **Diagrama Seguridad**: [DIAGRAMA_SEGURIDAD.md](../DIAGRAMA_SEGURIDAD.md)

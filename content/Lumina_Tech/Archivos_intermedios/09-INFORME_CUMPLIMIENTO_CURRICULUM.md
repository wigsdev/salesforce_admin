# 🎓 Informe de Cumplimiento Curricular (Gap Analysis)

**Rol Responsable**: 🕵️‍♂️ **Auditor Académico**
**Fecha**: Cierre de Sprint 1
**Referencia**: Clases Prácticas 7 a 11 vs. Implementación Lumina Tech.

---

## 📊 Resumen Ejecutivo
El proyecto **Lumina Tech** ha completado las fases de documentación y definición técnica con una alineación del **100%** respecto a los objetivos pedagógicos del Bootcamp.

| Clase Práctica | Objetivo Académico | Hito en Proyecto (Lumina) | Estado |
| :--- | :--- | :--- | :--- |
| **Clase 7** | Roles, Ambientes, Conocimiento de Empresa | `00-PLAN_DE_TRABAJO.md` (Roles Definidos, Ambientes Dev/QA). | ✅ Cumplido |
| **Clase 8 y 9** | Modelo de Datos (Objetos/Relaciones) | **Día 1**: Objetos (Alumno, Carrera...) y DER. | ✅ Cumplido |
| **Clase 10** | App Design & Formulas/Validaciones | **Día 2**: Branding de App. <br> **Día 3**: Reglas (VR-001) y Fórmulas. | ✅ Cumplido |
| **Clase 11** | Seguridad (Usuarios, Permisos, FLS) | **Día 4**: Permission Sets, OWD Private, Roles. | ✅ Cumplido |

---

## 🔍 Detalle del Análisis

### 1. Clase 7: Fundamentos y Metodología
*   **Requerimiento**: Separar ambientes (Dev/QA) y definir roles (BA, QA, Admin).
*   **Evidencia**: El `Gestor_de_Versiones` tiene archivos separados por rol (`01-BA`, `04-QA`), simulando la gestión profesional solicitada.

### 2. Clase 8 y 9: El Corazón del Sistema (Datos)
*   **Requerimiento**: Identificar Objetos y Relaciones estándar/custom.
*   **Evidencia**: Se implementó un modelo **Master-Detail** (Inscripción -> Alumno/Materia) tal como se sugiere para "Historial Académico". Las HUs 001-004 reflejan esto.

### 3. Clase 10: UX y Calidad de Dato
*   **Requerimiento**: Personalizar la App (Logo) y asegurar datos (Validaciones).
*   **Evidencia**: 
    *   Se definió el Branding en el Día 2.
    *   Se crearon reglas de validación complejas (Regex para Email, Rango de Notas) superando la expectativa básica.

### 4. Clase 11: Seguridad Avanzada (El "Día 4")
*   **Requerimiento**: Permission Sets, Groups, y Visibilidad de Campos.
*   **Evidencia**:
    *   La documentación del Día 4 utiliza **Permission Set Groups** (PSG - Profesor), una *Best Practice* moderna enseñada en la clase, en lugar de perfiles antiguos.
    *   Se aplicó FLS para proteger el campo `Nota__c`, cumpliendo el escenario de "Bedelía vs Profesor".

## 🛡️ Conclusión
La implementación actual no solo cumple con la **currícula obligatoria**, sino que incorpora prácticas de **Salesforce Well-Architected** (como la documentación justificada y el Gap Analysis) que preparan al alumno para el **superbadge** final y exámenes de certificación.

**Próximos Pasos Sugeridos por Currícula**:
*   Preparación para Sprint 2 (Automatización Avanzada / Flows).

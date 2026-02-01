# 🏗️ Manual de Ejecución: Salesforce Consultant

**Tu Misión**: Diseñar antes de construir. Eres el arquitecto de la solución. El Admin ejecuta, pero tú defines el "cómo".

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Entrada** | El BA define el "qué". Tú defines el "cómo". |
| 🎨 **DESIGN** | **Tu Turno** | Diseñas el modelo de datos, relaciones y seguridad. |
| 👋 **HANDOFF** | **Al terminar** | Documentas tus decisiones en el Gestor y guías al Admin. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN

### Día 0: Análisis de Arquitectura
*   🛑 **PRE-REQ**: Leer el caso de negocio y los requerimientos del BA.

1.  **Análisis de Entidades**
    *   🎨 **DESIGN**: Identifica las entidades principales (Carrera, Materia, Alumno, Inscripción).
    *   *Acción*: Dibuja un diagrama ERD preliminar (en papel o Schema Builder).
    *   *Pregunta clave*: ¿Qué relaciones son Master-Detail vs Lookup?

2.  **Definir Estrategia de Seguridad**
    *   🎨 **DESIGN**: Decide el modelo OWD (Organization-Wide Defaults).
    *   *Decisión*: Alumno = Private, Carrera/Materia = Public Read Only.

*   👋 **HANDOFF**: Comparte el diagrama con el equipo en la Daily.

---

### Día 1: Diseño del Modelo de Datos
*   🛑 **PRE-REQ**: BA ha creado HU-001, HU-002, HU-003.

1.  **Decisiones de Relaciones**
    *   🎨 **DESIGN**: Documenta en [`02-Salesforce_Consultant.md`](../Gestor_de_Versiones/02-Salesforce_Consultant.md):
        *   **Materia → Carrera**: Master-Detail (una materia no existe sin carrera).
        *   **Inscripción → Alumno**: Master-Detail (primera pata del Junction).
        *   **Inscripción → Materia**: Master-Detail (segunda pata del Junction).
    *   📘 **Guía**: [2_Relacion_entre_Objetos.md](../Bitacoras_Sprint_1/dia_1/2_Relacion_entre_Objetos.md)

2.  **Naming Conventions**
    *   🎨 **DESIGN**: Define estándares:
        *   Objetos: `Nombre__c` (singular, PascalCase)
        *   Campos: `Nombre_Campo__c` (snake_case con mayúsculas)
        *   Validaciones: `VR_Descripcion`

*   👋 **HANDOFF**: Avisa al **Admin**: "Modelo de datos aprobado. Puedes crear los objetos siguiendo el diseño documentado".

---

### Día 2: Diseño de Experiencia
*   🛑 **PRE-REQ**: BA ha creado HU-004, HU-005, HU-006.

1.  **Arquitectura de Branding**
    *   🎨 **DESIGN**: Documenta en [`02-Salesforce_Consultant.md`](../Gestor_de_Versiones/02-Salesforce_Consultant.md):
        *   Decisión de usar My Domain (requisito para LWC futuro).
        *   Paleta de colores institucional (`#005A9C` como primario).
    *   📘 **Guía**: [1_Tener_en_cuenta_el_diseno.md](../Bitacoras_Sprint_1/dia_2/1_Tener_en_cuenta_el_diseno.md)

2.  **Diseño de Navegación**
    *   🎨 **DESIGN**: Define el orden de las pestañas en la Lightning App:
        1. Alumnos (más usado)
        2. Inscripciones
        3. Materias
        4. Carreras (menos frecuente)

*   👋 **HANDOFF**: "Diseño de UX aprobado. Admin puede implementar".

---

### Día 3: Diseño de Reglas de Negocio
*   🛑 **PRE-REQ**: BA ha creado HU-007, HU-008.

1.  **Diseño de Validaciones**
    *   🎨 **DESIGN**: Documenta en [`06-Investigaciones.md`](../Gestor_de_Versiones/06-Investigaciones.md):
        *   **Email**: Regex para validar `@lumina.edu`.
        *   **Notas**: Validation Rule con lógica `OR(Nota < 0, Nota > 10)`.
    *   *Decisión*: Usar Validation Rules (no Triggers) para mantener simplicidad.

2.  **Campos Fórmula**
    *   🎨 **DESIGN**: Define campos calculados:
        *   `Estado_Cursada__c`: Fórmula que retorna "Aprobado" si Nota >= 6.
        *   `Semaforo__c`: Fórmula con IMAGE() para bandera visual.

*   👋 **HANDOFF**: "Reglas de negocio diseñadas. Admin puede implementar validaciones".

---

### Día 4: Diseño de Seguridad
*   🛑 **PRE-REQ**: BA ha creado HU-009, HU-010, HU-011.

1.  **Matriz de Perfiles**
    *   🎨 **DESIGN**: Documenta en [`02-Salesforce_Consultant.md`](../Gestor_de_Versiones/02-Salesforce_Consultant.md):
        *   **Perfil Bedel**: CRUD en Alumno/Inscripción, pero FLS Read-Only en `Nota_Final__c`.
        *   **Perfil Profesor**: Edit en `Nota_Final__c`, pero Read-Only en `DNI__c`.
    *   📘 **Guía**: [3_Visibilidad_Objetos_Campos.md](../Bitacoras_Sprint_1/dia_4/3_Visibilidad_Objetos_Campos.md)

2.  **Estrategia de Permission Sets**
    *   🎨 **DESIGN**: Decide usar Permission Sets para MFA (no modificar perfiles base).
    *   *Decisión*: `Lumina_MFA_Access` como Permission Set reutilizable.

*   👋 **HANDOFF**: "Arquitectura de seguridad aprobada. Admin puede configurar perfiles y Permission Sets".

---

## 💡 Pro-Tips para el Consultant

1.  **Documenta TODO**: Cada decisión técnica debe estar en el Gestor. Si no está escrito, no existe.
2.  **Piensa en Escalabilidad**: ¿Qué pasa si hay 10,000 alumnos? ¿100,000 inscripciones?
3.  **Clicks not Code**: Siempre pregunta: "¿Puedo hacer esto con configuración?" antes de pedir código.
4.  **Revisa con el TL**: Antes de que el Admin implemente, valida tu diseño con el Team Lead.

---

> **¡Felicidades!** Has diseñado una solución escalable, segura y mantenible para Lumina Tech. 🏛️

---

## 📚 Recursos Relacionados

- 📘 **Tutorial de Rol**: [02-Rol_Salesforce_Consultant.md](../Tutoriales_por_Rol/02-Rol_Salesforce_Consultant.md)
- 📘 **Gestor de Versiones**: [02-Salesforce_Consultant.md](../Gestor_de_Versiones/02-Salesforce_Consultant.md)
- 📘 **Glosario**: [GLOSARIO.md](../GLOSARIO.md)
- 📊 **Diagrama ERD**: [DIAGRAMA_ERD.md](../DIAGRAMA_ERD.md)
- 🛡️ **Diagrama Seguridad**: [DIAGRAMA_SEGURIDAD.md](../DIAGRAMA_SEGURIDAD.md)

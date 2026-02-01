# 🕵️ Manual de Ejecución: Business Analyst (BA)

**Tu Misión**: Eres el Estratega. Defines QUÉ se va a construir antes de que nadie escriba una línea de código.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Entrada** | Recibes necesidades vagas del cliente (Lumina Tech). Tu trabajo es clarificarlas. |
| 📝 **SPEC** | **Tu Turno** | Escribe Historias de Usuario (HU) y Criterios de Aceptación claros en Trello. |
| 👋 **HANDOFF** | **Al terminar** | Mueve la tarjeta a "To Do" (Ready for Dev) y avisa al **Salesforce Admin**. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN (Sprint 1)

### Día 0: Entendimiento del Negocio
*   🛑 **PRE-REQ**: Leer el caso de estudio de Lumina Tech.

1.  **Analizar Requisitos**
    *   📝 **SPEC**: Identifica los actores (Alumnos, Profesores) y sus dolores.
    *   📘 **Guía**: [01-Rol_Business_Analyst.md](../Tutoriales_por_Rol/01-Rol_Business_Analyst.md)

2.  **Generar Preguntas Q&A**
    *   📝 **SPEC**: Si algo no está claro ("¿La matrícula es anual o semestral?"), documéntalo para preguntar al PO.
    *   📘 **Guía**: [3_Generar_preguntas_en_el_documento_para_evacuar_dudas.md](../Bitacoras_Sprint_1/dia_0/3_Generar_preguntas_en_el_documento_para_evacuar_dudas.md)

*   👋 **HANDOFF**: Avisa al equipo: "Conocimiento del dominio completado".

---

### Día 1: Definición de Historia de Usuarios (Datos)
*   🛑 **PRE-REQ**: Comprender las entidades "Carrera" y "Materia".

1.  **Crear Historias de Usuario en Trello**
    *   📝 **SPEC**:
        *   Título: "Como [Admin], quiero [crear Carreras], para [organizar la oferta académica]".
        *   Criterios: "Debe tener Nombre, Duración y Tipo".
    *   📘 **Guía**: [5_Crear_las_HU_en_TRELLO.md](../Bitacoras_Sprint_1/dia_1/5_Crear_las_HU_en_TRELLO.md)

*   👋 **HANDOFF**: Mueve Tarjetas a "To Do". Avisa al **Admin**: "Modelo de datos listo para construir".

---

### Día 2: Branding y UX
*   🛑 **PRE-REQ**: Comprender los requerimientos visuales de la universidad.

1.  **Crear Historias de Usuario en Trello (Branding)**
    *   📝 **SPEC**:
        *   **HU-004**: Dominio Seguro (My Domain)
        *   **HU-005**: Identidad Institucional (Logo y Colores)
        *   **HU-006**: App de Gestión Central
    *   *Criterios*: Cada HU debe tener criterios de aceptación visuales medibles.
    *   📘 **Guía**: [5_Crear_las_HU_en_TRELLO.md](../Bitacoras_Sprint_1/dia_2/5_Crear_las_HU_en_TRELLO.md)

*   👋 **HANDOFF**: Mueve Tarjetas a "To Do". Avisa al **Admin**: "HUs de branding listas para implementar".

---

### Día 3: Reglas de Negocio
*   🛑 **PRE-REQ**: Admin reporta que los objetos existen.

1.  **Definir Validaciones**
    *   📝 **SPEC**: Escribe reglas lógicas. Ejemplo: "Fecha de Fin no puede ser menor a Fecha de Inicio".
    *   📘 **Guía**: [4_Crear_las_HU_en_TRELLO.md](../Bitacoras_Sprint_1/dia_3/4_Crear_las_HU_en_TRELLO.md)

*   👋 **HANDOFF**: Mueve Tarjeta a "To Do". Avisa al **Admin**: "Reglas de validación listas para implementar".

---

### Día 4: Seguridad
*   🛑 **PRE-REQ**: Comprender los requerimientos de seguridad y compliance.

1.  **Crear Historias de Usuario en Trello (Seguridad)**
    *   📝 **SPEC**:
        *   **HU-009**: Matriz de Visibilidad (Privacidad por defecto)
        *   **HU-010**: Acceso Seguro (MFA)
        *   **HU-011**: Segregación de Funciones (SoD)
    *   *Criterios*: Cada HU debe incluir tests negativos y positivos para validación de permisos.
    *   📘 **Guía**: [5_Crear_HU_Trello.md](../Bitacoras_Sprint_1/dia_4/5_Crear_HU_Trello.md)

*   👋 **HANDOFF**: Mueve Tarjetas a "To Do". Avisa al **Admin** y **QA**: "HUs de seguridad listas. Requieren pruebas exhaustivas de permisos".

---

## 📚 Recursos Relacionados

- 📘 **Tutorial de Rol**: [01-Rol_Business_Analyst.md](../Tutoriales_por_Rol/01-Rol_Business_Analyst.md)
- 📘 **Gestor de Versiones**: [01-Business_Analyst.md](../Gestor_de_Versiones/01-Business_Analyst.md)
- 📘 **Glosario**: [GLOSARIO.md](../GLOSARIO.md)
- 🔄 **Diagrama Trello**: [DIAGRAMA_FLUJO_TRELLO.md](../DIAGRAMA_FLUJO_TRELLO.md)


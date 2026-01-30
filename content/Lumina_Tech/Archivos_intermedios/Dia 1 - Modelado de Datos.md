# Guía: ROLES (BA, PO, Consultant)

**Objetivo**: Traducir las necesidades de la "Empresa Cliente" en un esquema de datos sólido dentro de Salesforce.

---

## Paso 1: Business Analyst (BA) - "El Detective"
Tu misión en esta fase es entender el problema actual sin pensar en la solución técnica todavía.

### Acciones Clave:
*   **Auditoría de "Herramientas"**: Revisen el material que les dio la empresa (excels, formularios viejos, reportes en papel).
*   **Identificación de Entidades**: ¿De qué "cosas" habla la empresa? (Ej. "Candidatos", "Vehículos", "Pólizas", "Inmuebles").

**Preguntas de Negocio**:
*   *"¿Un Cliente puede tener muchos Contratos o solo uno?"* (Esto definirá la relación 1:N).
*   *"¿Si borramos al Cliente, se debe borrar el Contrato?"* (Esto definirá si es Master-Detail o Lookup).

> **Entregable mental del BA**: "La empresa necesita una forma de guardar información sobre 'Proyectos' y saber qué 'Empleados' están asignados a cada uno."

---

## Paso 2: Product Owner (PO) - "El Visionario"
Tu misión es priorizar y definir el VALOR. ¿Por qué esto es importante para el negocio?

### Acciones Clave:
*   **Definir el "Para qué"**: No creamos objetos porque sí. Los creamos para reportar, automatizar o visualizar.
*   **Priorización**: ¿Qué es vital para que la empresa arranque el lunes? (MVP).
*   **Redacción de la Historia (Formato Estándar)**: Usen la estructura: `Como [Rol de Negocio], quiero [Necesidad], para [Beneficio]`.
*   **Trampa común**: Eviten decir "Como Administrador...". El usuario final es el Gerente de Ventas, el Recruiter o el Agente de Soporte.

---

## Paso 3: Salesforce Consultant - "El Arquitecto"
Tu misión es traducir el deseo del PO en metadata de Salesforce.

### Acciones Clave:
1.  **Mapeo Estándar vs. Personalizado**:
    *   ¿Lo que pide el BA ya existe? (¿Es una Cuenta? ¿Es una Oportunidad?).
    *   **Regla de Oro**: Nunca creen un Objeto Personalizado si un Objeto Estándar puede hacer el trabajo (con un cambio de etiqueta).
2.  **Diseño del Esquema (Schema Builder Mental)**:
    *   Definir tipos de datos (Picklists, Checkbox, Fechas).
    *   Definir relaciones (Lookup vs. Master-Detail).

---

## Paso 4: EJEMPLOS
Aquí tienen un ejemplo de cómo transformar un requerimiento vago en una Historia de Usuario de Modelado de Datos profesional:

**Escenario**: La empresa les dio un Excel donde anotan las "Visitas Técnicas" que hacen a los clientes.

### 1. Análisis (BA)
> "Vemos que anotan fecha, hora, técnico y resultado. Esto no cabe en el objeto 'Cuenta' porque una cuenta tiene muchas visitas."

### 2. Definición (PO) - La Historia de Usuario
*   **Título**: Creación de Objeto de Visitas Técnicas
*   **Historia**: "Como Gerente de Servicios, Quiero registrar cada visita técnica asociada a la cuenta del cliente, Para poder medir cuántas visitas necesitamos antes de cerrar una venta."

### 3. Criterios de Aceptación (Consultant)
Aquí es donde el Junior Admin brilla. Los criterios deben ser técnicos:
*   [ ] Crear un Objeto Personalizado llamado "Visita Técnica" (API: `Visita_Tecnica__c`).
*   [ ] Crear relación Master-Detail hacia el objeto "Cuenta" (Si se borra la cuenta, se borran las visitas).
*   [ ] Crear campo de tipo Picklist para "Estado de la Visita" (Valores: Programada, Realizada, Cancelada).
*   [ ] Crear campo de tipo Date/Time para "Fecha de Visita".
*   [ ] Habilitar la pestaña (Tab) para el perfil de Ventas.

### Checklist
Antes de dar por terminada una historia, el equipo debe verificar:
*   ¿Estamos reinventando la rueda? (¿Ya existía este objeto?).
*   ¿El "Para qué" justifica el esfuerzo de configuración?
*   ¿Los Criterios de Aceptación son lo suficientemente claros para que otro admin lo configure sin preguntarnos?

---

# Dia 2 - Análisis de creación de la App
**Estilo - Diseño - Dominio, Personalización e identidad de la empresa**

Crear Historias de usuario con respecto a este tema.

## Branding y UX (El Diseñador)
**Objetivo**: Creación de App, diseño, personalización e identidad de la empresa.

### ⏱️ TIP de Gestión del Tiempo:
"Reutilización de Recursos". Ten a mano los códigos Hex (colores) y el logo de la empresa en una carpeta antes de abrir Trello.

### ⚡ Daily (5 min): Enfoque: Navegación.
Pregunta clave:
*"¿Es intuitivo moverse entre pestañas? ¿La App tiene demasiadas cosas innecesarias?"*

### 👥 Roles:
*   **BA**: Define qué pestañas son esenciales para el flujo diario del usuario.
*   **PO**: Valida que el logo y colores representen fielmente la marca.
*   **Consultant**: Configura la "Utility Bar" (Barra de utilidades) para acciones rápidas.
*   **QA**: Verifica que la App se vea bien en diferentes resoluciones.

### ✅ Tareas del día (Admin):
*   Usar el App Manager para crear la Lightning App (Branding y Navegación).
*   Configurar Temas y Branding (Themes).
*   Organizar el Menú de Navegación (Tabs).
*   Personalizar la Home Page con componentes útiles.

Crear todas las historias de usuario necesarias para poder crear esto durante el SPRINT 1.

# ♟️ Estrategia de Distribución de Roles (Squad de 6)

## 📋 Premisa del Equipo
*   **Base Común**: Todos los 6 integrantes son **Salesforce Admins**. Todos configuran, todos construyen en Salesforce.
*   **Sombreros Especiales**: Además de construir, cada uno asume una responsabilidad específica para garantizar el orden del proyecto.

## 🎯 Estructura de Roles del Proyecto

**Total de Roles**: 10 roles en el ecosistema Salesforce
*   **Rol Base (Transversal)**: 🛡️ **Salesforce Admin** - Los 6 integrantes tienen esta capacidad
*   **Roles Especializados (Activos en Sprint 1)**: 8 roles distribuidos entre los 6 integrantes
    1. Product Owner
    2. Business Analyst
    3. Salesforce Consultant
    4. Team Lead
    5. Scrum Master
    6. QA Tester
    7. Release Manager
    8. DevOps Specialist
*   **Rol Futuro (Inactivo en Sprint 1)**: 💻 **Salesforce Developer** - Reservado para mejoras con código personalizado

---

## 🗺️ Matriz de Asignación (Propuesta)

Para distribuir los **8 roles especializados** entre **6 personas**, aplicamos la lógica de "Sinergia de Funciones". Agrupamos roles compatibles en una misma persona.

### 👤 Integrante 1: El Estratega de Negocio
**Roles**: 👔 **Product Owner (PO)** + 🕵️ **Business Analyst (BA)**
*   **¿Por qué juntos?**: Ambas funciones miran hacia "Afuera" (hacia el cliente).
*   **Responsabilidad**: Es quien habla con la Rectora, entiende el problema (BA) y decide qué es prioritario construir primero (PO). Es la fuente de la verdad para los requerimientos.

### 👤 Integrante 2: El Líder Técnico
**Roles**: 🛡️ **Team Lead (TL)** + 🏗️ **Salesforce Consultant**
*   **¿Por qué juntos?**: Ambas funciones miran hacia "Adentro" (hacia la solución).
*   **Responsabilidad**: Diseña el modelo de datos (Consultant) y tiene la última palabra técnica antes de aprobar una tarea (TL). Garantiza que no se construyan "Frankensteins".

### 👤 Integrante 3: El Facilitador
**Roles**: ⏱️ **Scrum Master**
*   **Responsabilidad**: Cuida el proceso. Mantiene el tablero Trello actualizado, cronometra las Dailies y desbloquea al equipo cuando se traban. (Al tener un solo rol de gestión, se espera que este integrante dedique más tiempo a construir como Admin).

### 👤 Integrante 4: Calidad (QA)
**Roles**: 🧪 **QA Tester**
*   **Responsabilidad**: Es el "Abogado del Diablo". Intenta romper lo que construyeron los demás. Su aprobación es obligatoria para pasar a Producción.

### 👤 Integrante 5: Guardián de Producción
**Roles**: 🚀 **Release Manager**
*   **Responsabilidad**: El dueño de los Change Sets. Nadie toca el ambiente PROD sin su permiso. Coordina los despliegues de los viernes.

### 👤 Integrante 6: Infraestructura y Datos
**Roles**: ♾️ **DevOps Specialist**
*   **Responsabilidad**: Mantiene los ambientes sincronizados. Se encarga de cargar los datos de prueba masivos (Alumnos ficticios, Materias) para que el QA tenga con qué trabajar.

---

## 🔄 Resumen Visual

| Integrante | Rol Primario (Foco) | Rol Secundario (Soporte) | Responsabilidad Principal |
| :--- | :--- | :--- | :--- |
| **#1** | **Product Owner** | Business Analyst | Definir QUÉ hacer. |
| **#2** | **Team Lead** | Consultant | Definir CÓMO hacerlo. |
| **#3** | **Scrum Master** | *(Admin Builder)* | Cuidar el PROCESO. |
| **#4** | **QA Tester** | - | Validar que FUNCIONE. |
| **#5** | **Release Manager** | - | Llevarlo a PROD (Despliegue). |
| **#6** | **DevOps Specialist** | - | Preparar el TERRENO (Datos/Ambientes). |

---

## 💡 Notas de Implementación
*   **Rotación**: Se sugiere mantener estos roles fijos durante el **Sprint 1** para evitar confusiones. En el Sprint 2, pueden rotar (ej: El QA pasa a ser Release Manager) para que todos aprendan todas las habilidades.
*   **Colaboración**: Que el Integrante 1 sea el "Dueño del Negocio" no significa que los demás no puedan hablar con el cliente, pero el Integrante 1 es quien toma la decisión final de qué se incluye en el Backlog.

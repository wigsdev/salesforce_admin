# 🧭 MASTER INDEX: Proyecto Lumina Tech
**Versión**: Standard v3.0 (Agile Core)
**Objetivo**: Este documento es el **Mapa Central**. Conecta todas las guías, tutoriales y documentos del proyecto en un orden lógico de ejecución.

---

## 📑 Navegación Rápida

| Fase | Descripción | Ir a |
|------|-------------|------|
| 🏗️ **Fase 1** | Entendimiento y Estrategia | [Ver Fase 1](#%EF%B8%8F-fase-1-entendimiento-y-estrategia) |
| 👥 **Fase 2** | Roles y Responsabilidades | [Ver Fase 2](#-fase-2-roles-y-responsabilidades) |
| ⚙️ **Fase 3** | Infraestructura y Diseño | [Ver Fase 3](#%EF%B8%8F-fase-3-infraestructura-y-diseño) |
| 🛠️ **Fase 4** | Implementación (Construcción) | [Ver Fase 4](#%EF%B8%8F-fase-4-implementación-construcción) |
| 🏁 **Fase 5** | Entrega y Cierre | [Ver Fase 5](#-fase-5-entrega-y-cierre) |

**💡 Tip**: Si es tu primera vez, comienza por [Fase 1](#%EF%B8%8F-fase-1-entendimiento-y-estrategia). Si ya conoces el proyecto, salta directamente a tu fase.

---

## 🏗️ Fase 1: Entendimiento y Estrategia
*Antes de tocar Salesforce, entiende qué vas a construir.*

1.  **📜 ¿Qué vamos a hacer?**
    *   [SPRINT 1 (Requerimientos)](Enunciados_y_Requerimientos/SPRINT%201.md): Lee esto primero. Define el problema de la Rectora Vance.
    *   [Backlog de Historias (12 HUs)](HISTORIAS_DE_USUARIO.md): El alcance detallado en formato Gherkin.
    *   [Identidad Visual](Enunciados_y_Requerimientos/Identidad_Colores.md): Conoce los colores (`#005A9C`) y el logo.

2.  **🧠 ¿Cómo trabajamos?**
    *   [Guía Metodológica](00-GUIA_METODOLOGICA.md): Las reglas del juego (Semanas, Entregables).
    *   [Integración Trello](00-INTEGRACION_TRELLO.md): Cómo mover las tarjetas (11 Columnas).

---

## 👥 Fase 2: Roles y Responsabilidades
*Define quién eres y qué debes hacer.*

*   ♟️ **MATRIZ DE EQUIPO (6 Integrantes)**: [Ver Distribución Recomendada](../Tutoriales_por_Rol/00-MATRIZ_ROLES_EQUIPO.md). 👈 **(¡Empieza Aquí!)**
*   🕵️ **Business Analyst**: [Tu Guía Aquí](../Tutoriales_por_Rol/01-Rol_Business_Analyst.md). (Traduce necesidades).

*   👔 **Product Owner (PO)**: [Tu Guía Aquí](../Tutoriales_por_Rol/06-Rol_Product_Owner.md). (Prioriza valor).
*   🏗️ **Consultant / Architect**: [Tu Guía Aquí](../Tutoriales_por_Rol/02-Rol_Salesforce_Consultant.md). (Diseña los datos).
*   🛡️ **Team Lead (TL)**: [Tu Guía Aquí](../Tutoriales_por_Rol/07-Rol_Team_Lead.md). (Calidad técnica).
*   ⏱️ **Scrum Master**: [Tu Guía Aquí](../Tutoriales_por_Rol/08-Rol_Scrum_Master.md). (Ritmo y procesos).
*   ⚙️ **Salesforce Admin**: [Tu Guía Aquí](../Tutoriales_por_Rol/05-Rol_Salesforce_Admin.md). (Construye la solución).
*   🧪 **QA Tester**: [Tu Guía Aquí](../Tutoriales_por_Rol/03-Rol_QA_Tester.md). (Rompe el sistema).
*   🚀 **Release Manager**: [Tu Guía Aquí](../Tutoriales_por_Rol/04-Rol_Release_Manager.md). (Cuida Producción).
*   ♾️ **DevOps Specialist**: [Tu Guía Aquí](../Tutoriales_por_Rol/09-Rol_DevOps_Specialist.md). (Automatización).
*   💻 **Salesforce Developer**: [Tu Guía Aquí](../Tutoriales_por_Rol/10-Rol_Salesforce_Developer.md). (Código avanzado).



---

## ⚙️ Fase 3: Infraestructura y Diseño
*Configurando el terreno.*

1.  **🗺️ Ambientes (Simulados)**
    *   [DEV (Desarrollo)](../Gestor_de_Versiones/11-Ambiente_DEV.md)
    *   [QA (Testing)](../Gestor_de_Versiones/12-Ambiente_QA.md)
    *   [PROD (Producción)](../Gestor_de_Versiones/13-Ambiente_PROD.md)

2.  **📐 Diseño de Solución**
    *   [Arquitectura y Solución (ERD)](../Gestor_de_Versiones/02-Salesforce_Consultant.md): Decisiones de diseño y diagramas.
    *   [Config Workbook (Diccionario de Datos)](../Gestor_de_Versiones/03-Salesforce_Admin.md): La "Receta" de los objetos.
    *   [Investigaciones Técnicas](../Gestor_de_Versiones/06-Investigaciones.md): Por qué elegimos Junction Object, FLS y Regex.

---

## 🛠️ Fase 4: Implementación (Construcción)
*Manos a la obra. Sigue estos tutoriales EN ORDEN.*

1.  **🧱 Estructura de Datos**
    *   [1. Tutorial Carrera](../Guias_Implementacion/01-Tutorial_Carrera.md)
    *   [2. Tutorial Materia](../Guias_Implementacion/02-Tutorial_Materia.md)
    *   [3. Tutorial Alumno](../Guias_Implementacion/03-Tutorial_Alumno.md)
    *   [4. Tutorial Inscripción](../Guias_Implementacion/04-Tutorial_Inscripcion.md)
    *   [**9. VERIFICACIÓN VISUAL (Schema Builder)**](../Guias_Implementacion/09-Tutorial_Schema_Builder.md)

2.  **�️ Lógica y Seguridad**
    *   [5. Validaciones (Email y Notas)](../Guias_Implementacion/05-Tutorial_Validaciones.md)
    *   [**5b. Automatización (Fórmulas)**](../Guias_Implementacion/05b-Tutorial_Campos_Formula.md) 🆕
    *   [6. Seguridad (OWD y Perfiles)](../Guias_Implementacion/06-Tutorial_Seguridad.md)

3.  **🎨 Interfaz de Usuario**
    *   [7. App Builder (Branding)](../Guias_Implementacion/07-Tutorial_App_Builder.md)

4.  **💾 Datos**
    *   [8. Carga Masiva (Data Loader)](../Guias_Implementacion/08-Tutorial_Carga_Datos.md)

---

## 🏁 Fase 5: Entrega y Cierre
*El moño final.*

1.  **🧪 Aseguramiento de Calidad**
    *   [Plan de Pruebas (Casos y Bugs)](../Gestor_de_Versiones/04-Tester_QA.md).

2.  **📘 Manual para el Cliente**
    *   [Guía de Usuario Final](GUIA_USUARIO.md): Entregable para la Rectora y Profesores.

---

> **Nota**: Si te pierdes, vuelve siempre a este índice. ¡Éxito equipo! 🚀

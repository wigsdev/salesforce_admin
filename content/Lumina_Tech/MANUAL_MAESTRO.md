# 🦅 manual Maestro de Ejecución: Proyecto Lumina Tech

**Rol**: Project Manager & Scrum Master  
**Proyecto**: Implementación Salesforce - Universidad Lumina Tech  
**Versión**: 2.0 (Autónoma)

---

## 🎯 ¿Cómo usar este Manual?

Bienvenido al equipo. Este documento es tu **hoja de ruta**. No necesitas preguntar "¿qué hago ahora?"; este archivo te lo dice paso a paso.

### 1. Identifica tu Rol 🎭
Antes de empezar, busca qué sombrero llevas puesto hoy:

*   **🕵️ Business Analyst (BA)**: Lees requisitos, traduces necesidades a historias de usuario.
*   **🛡️ Salesforce Admin**: Configuras la plataforma (Objetos, Campos, Flows). Metes las manos en la masa.
*   **🏗️ Salesforce Consultant/Architect**: Diseñas la solución. Decides "¿Cómo se conecta esto con aquello?".
*   **🚀 Release Manager**: Controlas el Gestor de Versiones. Decides cuándo se pasa a la siguiente etapa.
*   **👑 Product Owner (PO)**: Apruebas el trabajo final. La voz del cliente.

### 2. El Flujo de Trabajo (The Flow) 🌊
Para cada día del Sprint:
1.  Ve a la sección correspondiente (ej. **Día 1**).
2.  Busca las tareas marcadas con tu **Icono de Rol**.
3.  Haz clic en el enlace `[Ver Tarea]` para ver el paso a paso detallado.
4.  Ejecuta la tarea en tu Salesforce Dev Org.
5.  Actualiza el estado en Trello/Jira.

---

## 📅 Día 0: Análisis y Conocimiento
**Objetivo**: Entender el negocio y preparar el terreno.

1.  **Leer juntos y conocer la Empresa**.
    *   *Responsables*: 🕵️ BA, 👑 PO.
    *   *Acción*: [Leer Documento de Inicio](dia_0/1_Leer_juntos_y_conocer_la_Empresa.md)
2.  **Definir Roles del Equipo**.
    *   *Responsables*: 🤝 Team Lead.
    *   *Acción*: [Asignar responsabilidades](dia_0/2_Definir_Roles.md)
3.  **Generar preguntas (Q&A)**.
    *   *Responsables*: 🕵️ BA, 🏗️ Consultant.
    *   *Acción*: [Crear cuestionario para el cliente](dia_0/3_Generar_preguntas_en_el_documento_para_evacuar_dudas.md)
4.  **Inicializar Gestor de Versiones**.
    *   *Responsables*: 🚀 Release Manager.
    *   *Acción*: [Crear documento de control](dia_0/4_Registrar_en_el_Doc_gestor_de_versiones.md)

---

## 📅 Día 1: El Corazón del Sistema (Modelo de Datos)
**Objetivo**: Crear la estructura base donde vivirán los datos.

1.  **Creación de Objetos (Custom & Standard)**.
    *   *Responsables*: 🛡️ Admin.
    *   *Tarea*: Crear objetos `Carrera`, `Materia`, `Alumno`.
    *   *Guía*: [Ver Paso a Paso](dia_1/1_Creacion_de_objetos_Custom_Standard.md)
2.  **Definir Relaciones (Modelo ERD)**.
    *   *Responsables*: 🏗️ Consultant (Diseño), 🛡️ Admin (Ejecución).
    *   *Tarea*: Conectar Materias con Carreras (Lookup/Master-Detail).
    *   *Guía*: [Ver Paso a Paso](dia_1/2_Relacion_entre_Objetos.md)
3.  **Crear Campos Personalizados**.
    *   *Responsables*: 🛡️ Admin.
    *   *Tarea*: Añadir campos de fecha, texto, picklists.
    *   *Guía*: [Ver Paso a Paso](dia_1/3_Campos_personalizados.md)
4.  **Bitácora de Versiones**.
    *   *Responsables*: 🚀 Release Manager.
    *   *Guía*: [Ver Paso a Paso](dia_1/4_Registrar_en_el_Doc_gestor_de_versiones.md)

---

## 📅 Día 2: Identidad y Marca (App Builder)
**Objetivo**: Que la app se vea profesional y alineada con Lumina Tech.

1.  **Diseño de UX/UI**.
    *   *Responsables*: 🎨 UX Consultant.
    *   *Tarea*: Definir paleta de colores y logo.
    *   *Guía*: [Ver Tarea](dia_2/1_Tener_en_cuenta_el_diseno.md)
2.  **Configurar Dominio (My Domain)**.
    *   *Responsables*: 🛡️ Admin.
    *   *Guía*: [Ver Configuración](dia_2/2_Lograr_hacer_el_dominio_personalizado.md)
3.  **Branding (Themes & Branding)**.
    *   *Responsables*: 🛡️ Admin.
    *   *Tarea*: Subir logo y aplicar colores corporativos.
    *   *Guía*: [Ver Tarea](dia_2/3_Agregar_el_Logo_y_colores.md)

---

## 📅 Día 3: Calidad de Datos (Formularios Inteligentes)
**Objetivo**: Asegurar que los datos ingresados sean válidos y útiles.

1.  **Reglas de Validación**.
    *   *Responsables*: 🛡️ Admin.
    *   *Tarea*: Impedir fechas futuras, validar formatos de email.
    *   *Guía*: [Ver Lógica](dia_3/2_Reglas_de_validacion_y_campos_formula.md)
2.  **Campos Fórmula**.
    *   *Responsables*: 🏗️ Consultant.
    *   *Tarea*: Calcular promedios, estados automáticos.
    *   *Guía*: [Ver Fórmulas](dia_3/2_Reglas_de_validacion_y_campos_formula.md)
3.  **Page Layouts**.
    *   *Responsables*: 🛡️ Admin.
    *   *Tarea*: Organizar los campos de forma lógica para el usuario.
    *   *Guía*: [Ver Tarea](dia_3/1_Campos_adicionales.md)

---

## 📅 Día 4: Seguridad y Accesos
**Objetivo**: ¿Quién puede ver qué? (Modelo de Seguridad).

1.  **Permission Sets**.
    *   *Responsables*: 🛡️ Admin.
    *   *Tarea*: Crear permisos especiales para profesores/directores.
    *   *Guía*: [Ver Configuración](dia_4/1_Configuracion_Permission_Sets.md)
2.  **Sharing Rules (OWD)**.
    *   *Responsables*: 🏗️ Architect.
    *   *Tarea*: Definir si los alumnos ven datos de otros (Privado/Público).
    *   *Guía*: [Ver Estrategia](dia_4/3_Visibilidad_Objetos_Campos.md)

---

> **Nota Final**: Este documento es el *cerebro* del proyecto. Si te pierdes, vuelve aquí. ¡Éxito en la implementación! 🚀

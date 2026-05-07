# 📚 Technical Q&A Bank - Lumina Tech University (100% Coverage)

Este documento es la referencia técnica final para la defensa del proyecto, organizada secuencialmente por Historia de Usuario (HU).

---

## 🏛️ SPRINT 1: Foundation Académica (HUs 001-009)

**Q [HU-001]: ¿Cómo aseguraron la privacidad de los datos sensibles (DNI) frente a los docentes?**
*   **A:** Implementamos **Field-Level Security (FLS)** en el objeto Persona (Contact). Para el perfil *Lumina Professor*, ocultamos el campo `Numero_Documento__c`, asegurando que el docente vea al alumno pero no su información de identidad privada.

**Q [HU-003]: ¿Por qué usaron una relación Master-Detail entre Materia y Carrera?**
*   **A:** Para establecer una jerarquía fuerte. Esto permite que la visibilidad de la materia sea heredada y habilita campos de **Roll-up Summary** en Carrera para totalizar créditos o cantidad de asignaturas automáticamente.

**Q [HU-004]: ¿Qué lógica técnica aplicaron para que un alumno no se inscriba en materias de otra carrera?**
*   **A:** Implementamos una **Validation Rule** de coherencia académica. La regla cruza el ID de la carrera del alumno con el ID de la carrera de la materia; si no coinciden, el sistema bloquea la inscripción con un mensaje de error personalizado.

**Q [HU-006]: ¿Cómo evitaron que los administrativos alteren las notas de los profesores?**
*   **A:** Mediante **Segregation of Duties (SoD)**. El perfil *Lumina Registrar* tiene acceso de **Read Only** a nivel de objeto para `Evaluacion__c`, permitiendo la auditoría pero bloqueando cualquier edición manual de calificaciones.

**Q [HU-008]: ¿Cuál es la importancia técnica de desplegar My Domain y MFA?**
*   **A:** **My Domain** es un requisito obligatorio para habilitar *Experience Cloud* y brinda una identidad de marca profesional. El **Multi-Factor Authentication (MFA)** fue activado para cumplir con los estándares de seguridad obligatorios de Salesforce, protegiendo el acceso administrativo contra ingresos no autorizados.

---

## ⚙️ SPRINT 2: Automatización y Migración (HUs 201-208)

**Q [HU-201]: ¿Cómo manejaron la duplicidad durante la carga de 1.000 registros históricos?**
*   **A:** Configuramos el campo `Numero_Documento__c` como **External ID** y **Unique**. Esto permitió usar la función **Upsert** de **Data Loader**, vinculando registros por DNI y bloqueando cualquier intento de creación de registros clonados desde la base de datos.

**Q [HU-204]: ¿Por qué el flujo de auditoría de actas es un Scheduled Flow y no Record-Triggered?**
*   **A:** Porque la revisión debe ser periódica (Viernes 17:00hs). Un **Scheduled Flow** permite procesar por lotes (*Batch*) todos los registros de evaluaciones vacías en un momento específico, algo que un flujo disparado por registro no podría hacer de forma eficiente.

**Q [HU-207]: ¿Cómo garantizaron que el personal operativo no vea los tableros de la Rectora?**
*   **A:** Usamos **Folder Sharing**. Las carpetas de *Reports* y *Dashboards* estratégicos se configuraron con acceso "View" exclusivo para el **Role** de "Rectoría" y "Gerentes", ocultándolas por completo para el resto de los perfiles.

**Q [HU-208]: ¿Cuál es la diferencia técnica entre Perfiles y Roles en este proyecto?**
*   **A:** Los **Profiles** controlan los permisos sobre objetos y campos (qué puede hacer el usuario). Los **Roles** controlan la visibilidad de los registros (qué datos puede ver) mediante la jerarquía de la organización.

---

## 🌐 SPRINT 3: Campus Virtual y Soporte (HUs S3-00 a S3-07)

**Q [HU-S3-00]: ¿Cuál es el pre-requisito crítico para que un Admin pueda crear artículos de Knowledge?**
*   **A:** El administrador debe tener marcado el checkbox **"Knowledge User"** en su registro de usuario (`Setup → Users`). Sin este permiso de licencia, la pestaña de Knowledge no aparecerá aunque la función esté activada en la Org.

**Q [HU-S3-02]: ¿Cómo habilitaron la captación de prospectos para usuarios anónimos de forma segura?**
*   **A:** Configuramos el **Guest User Profile** del sitio. Le otorgamos permisos de "Read" y "Create" sobre el objeto **Lead** y habilitamos el acceso a la ejecución del **Screen Flow** público en el Experience Builder.

**Q [HU-S3-04a]: ¿Cómo asocian automáticamente un ticket de soporte al alumno correcto en el portal privado?**
*   **A:** Dentro del **Screen Flow**, mapeamos el campo `ContactId` del caso utilizando la variable global **`Running User > ContactId`** (que Salesforce expone como `$User.ContactId`). Esto vincula el ticket al alumno logueado sin pedirle sus datos nuevamente.

**Q [HU-S3-04c]: ¿Cómo automatizaron el enrutamiento de casos a la cola correcta?**
*   **A:** Implementamos un **Record-Triggered Flow (Before-Save)** optimizado para *Fast Field Updates*. El flujo evalúa el asunto del caso; si contiene palabras como "Nota" o "Académica", asigna automáticamente el caso a la **Cola Académica** y sube la prioridad a **High**.

**Q [HU-S3-05]: ¿Qué paso es vital para que los artículos de Knowledge aparezcan en el portal?**
*   **A:** Deben habilitarse los **Topics for Objects** para Knowledge y configurar los **Featured Topics** en el Builder. Además, el artículo debe estar publicado con la visibilidad **"Visible to Customer"** activada.

**Q [HU-S3-06]: ¿Cuál es la función del Omni-Channel en la Mesa de Ayuda?**
*   **A:** Distribuye la carga de trabajo de forma inteligente. Los casos y chats llegan a los agentes basándose en sus **Queues** de especialización y su capacidad disponible (*Routing Configuration*), eliminando la asignación manual y los cuellos de botella.

**Q [HU-S3-07]: ¿Cuál es la función del Einstein Bot frente al soporte humano?**
*   **A:** El bot actúa como filtro de **Nivel 1 (Contención)**. Resuelve dudas mediante menús y artículos FAQ; solo cuando el alumno solicita "Hablar con un agente", el bot transfiere la sesión al **Omni-Channel**, disparando la alerta en la consola del personal humano.

# Hoja de Ruta Técnica del Tech Lead — Sprint 3

Hola, equipo! Como su Tech Lead, he trazado la hoja de ruta técnica para este Sprint 3. Vamos a transformar Salesforce en el portal interactivo que la Rectora Vance necesita para Lumina Tech. Aquí tienen las especificaciones exactas de lo que espero ver implementado:

📚 **Trails de apoyo:** https://trailhead.salesforce.com/es/content/learn/trails/communities

---

## 1. Captación de Futuros Alumnos (Experience Cloud + Guest User)

Necesitamos un punto de entrada para los interesados antes de que sean parte de la institución.

- **Herramienta:** Creen el sitio en Experience Cloud utilizando la plantilla **Customer Service** o **Build Your Own**. No olviden aplicar el Branding/Theme corporativo.
- **El Flujo:** Insertar un Screen Flow en una página pública para captar "Futuros Alumnos" (registros de **Leads**).
- **El Reto de Seguridad (Ojo aquí):** Tendrán que habilitar el acceso público en el Builder y configurar el **Guest User Profile**. Si el formulario no guarda, es porque no le dieron permisos al perfil anónimo para crear registros en el objeto Lead/Contact o no le dieron acceso a ejecutar ese Flow específico.

---

## 2. Portal del Alumno (Authenticated Users + Flujo Privado)

Este es el entorno seguro para quienes ya cursan con nosotros.

- **Configuración:** Implementen un portal autenticado. Recuerden que para esto, los Contactos (Alumnos) deben ser habilitados como **Customer Portal Users**, vinculando el registro de persona con su usuario de sistema.
- **El Flujo de Soporte:** Creen un Screen Flow para la generación de tickets de ayuda (**Cases**).
- **Lógica Dinámica:** El flujo debe vivir en una página privada (requiere login) y debe ser capaz de tomar automáticamente el ID del usuario logueado para asociar el ticket al alumno correcto sin que él tenga que volver a cargar sus datos.

---

## 3. Base de Conocimientos (Salesforce Knowledge)

Queremos que los alumnos encuentren respuestas solos antes de abrir un ticket.

- **Habilitación:** Activen Knowledge en la organización y definan las **Data Categories** pertinentes.
- **Acción:** Deben publicar al menos **3 artículos básicos**. Punto clave: Asegúrense de marcar las casillas **"Visible in Public Knowledge Base"** o **"Visible to Customer"**, de lo contrario, aunque el artículo esté publicado, no se verá en el portal.
- **Implementación:** Arrastren el componente estándar de Knowledge al Experience Builder y configuren la búsqueda.

---

Equipo, la clave de este sprint es la transición de "usuario interno" a "usuario final". Presten especial atención a los permisos de los perfiles; la mayoría de los errores en este nivel son de visibilidad, no de lógica.

---

## ⚠️ OJO — Configuración de la Org (Hoja de Ruta Anti-Rebote)

Aquí tienen su hoja de ruta de configuración para que la Org no les rebote los requerimientos:

### 1. Experience Cloud (Portales y Sitios)

- **Estado:** Totalmente viable.
- **El "Truco":** Primero deben ir a Setup y activar el "interruptor" maestro: **Digital Experiences**. Sin eso, no verán ninguna de las opciones de portal.
- **Ojo con las Licencias:** Las Orgs de Developer tienen licencias de comunidad limitadas (Customer Community). No creen usuarios a lo loco; usen uno o dos para probar el login y el resto manéjenlo con el **Guest User** (Público).

### 2. Screen Flows (Formularios Web)

- **Estado:** 100% funcional.
- **Punto de dolor:** En estas Orgs, los perfiles vienen muy restrictivos. Si su formulario público tira error al guardar, no toquen el Flow; vayan directo a revisar los **permisos de objeto en el Guest User Profile**. Es el error número uno en esta etapa.

### 3. Salesforce Knowledge (Base de Conocimientos)

- **Estado:** Viable, pero requiere un paso previo manual.
- **Configuración Crítica:** Para poder crear artículos, deben ir a su propio registro de Usuario (`Setup → Users`) y marcar el checkbox que dice **"Knowledge User"**. Si no lo hacen, la pestaña de Knowledge simplemente no aparecerá, aunque la hayan activado en la Org.

### 4. Chat y Omnicanalidad

- **Estado:** Viable, pero laborioso.
- **Recomendación:** Usen **Embedded Service Deployment**. Es la forma más limpia de meter el chat en el portal de Trailhead. Requiere configurar el canal, la presencia del usuario y la cola de atención en **Omni-Channel**.

---

> **Resumen para el equipo:** "La Developer Edition es un Porsche en miniatura: tiene todas las funciones, pero menos espacio (licencias)."

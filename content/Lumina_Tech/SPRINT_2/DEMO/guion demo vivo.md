# Guion de Demo en Vivo: Lumina Tech (Sprint 2)
**Tiempo asignado:** 4 Minutos.
**Estrategia:** Demo ejecutada como Administrador, mostrando el uso de las herramientas sin exageraciones.

**Preparación técnica antes de empezar:**
1. Tener abierta la Lightning App "Gestión Académica Lumina".
2. Tener lista la *Utility Bar* inferior para acceder al Screen Flow de Carga.
3. Tener un registro de Evaluación sin nota ("Null") preparado, que muestre la Tarea generada.
4. Tener la pestaña Dashboards lista para mostrar.

---

## 🎤 TRANSICIÓN DESDE LA PPT
**Discurso:**
"Pasemos a la plataforma de Salesforce para visualizar estas tres implementaciones trabajando en conjunto."

---

## ⚙️ ESCENARIO 1: Carga Rápida y Correo de Bienvenida (1.5 Minutos)
*Objetivo: Demostrar la solución al pedido de una pantalla simplificada para recepción y la automatización del correo.*

**1. El Asistente de Recepción (Screen Flow)**
*   *(Acción: Haz clic en la barra inferior para abrir el flujo "Lumina Asistente Carga Recepcion").*
*   **Discurso:** "Para solucionar la queja del personal de recepción sobre la complejidad de la pantalla estándar, implementamos este asistente en la barra de utilidades. Contiene solo los campos estrictamente necesarios para registrar a un alumno."
*   *(Acción: Ingresa un Nombre, Apellido, DNI y Email de prueba, y presiona Guardar).*
*   **Discurso:** "Al guardar, el alumno queda registrado en la base de datos. Además, esto activa nuestro segundo flujo en segundo plano: el sistema le envía automáticamente el correo de bienvenida al estudiante, eliminando la necesidad de que el personal lo redacte manualmente."

---

## 📅 ESCENARIO 2: Auditoría de Cierre de Actas (1 Minuto)
*Objetivo: Demostrar la automatización para gestionar a los profesores que no cargan notas.*

**1. Tarea Automática (Schedule-Triggered Flow)**
*   *(Acción: Cierra el asistente y abre el registro de Evaluación que tienes preparado. Señala la Tarea asignada en la lista de actividades).*
*   **Discurso:** "Respecto al seguimiento de los profesores, aquí tenemos una Evaluación pasada que aún no tiene calificación. En lugar de revisión manual, configuramos un Flujo Programado. Todos los viernes a las 17:00 hs, el sistema busca estos registros vacíos y genera automáticamente esta Tarea, notificando al profesor responsable que debe cerrar el acta."

---

## 📊 ESCENARIO 3: Tableros de Control (1.5 Minutos)
*Objetivo: Mostrar la visibilidad de datos solicitada por la Rectora.*

**1. Dashboards Directivos**
*   *(Acción: Ve a la pestaña Dashboards y abre la carpeta de reportes directivos. Muestra el Tablero 1 y luego el Tablero 3).*
*   **Discurso:** "Finalmente, para la toma de decisiones, hemos procesado los 1000 registros históricos y los hemos consolidado en estos Tableros. Por ejemplo, en el Tablero Académico la Rectora puede ver la distribución de alumnos por carrera. Y en el Tablero de Calidad de Datos, puede auditar fácilmente cuántos alumnos tienen información de contacto incompleta para solicitar su corrección. Estos tableros están configurados con seguridad de carpetas, por lo que solo la alta dirección tiene acceso a ellos."

---

## 🏁 EL CIERRE (Final de la Demo Sprint 2)
**Discurso:**
"De esta manera, hemos cubierto los requerimientos de migración, automatización de procesos clave y visibilidad gerencial solicitados para este Sprint. Muchas gracias."

# Guion de Presentación PPT: Lumina Tech University (Sprint 2)
## Formato: Presentación Ejecutiva (3 Minutos)
**Objetivo:** Exponer de forma clara y directa cómo las funcionalidades implementadas resuelven las solicitudes de la Rectora (Carga histórica, Automatizaciones y Reportes).

---

## 🎬 PARTE 1: EL REQUERIMIENTO (45 segundos)
*Encuadre: Slide con el resumen de la solicitud del Sprint 2.*

**Discurso:**
"Buenos días. Durante este segundo sprint, la Rectora nos planteó tres necesidades operativas claras para complementar la base de datos que ya construimos:
1. Necesitaban cargar 1000 registros históricos de un archivo Excel antiguo sin generar trabajo manual de meses.
2. Necesitaban agilizar tareas rutinarias: el envío de correos de bienvenida, facilitar la carga de datos en recepción y controlar el cierre de actas de los profesores.
3. Requerían visibilidad mediante tableros de control para tomar decisiones basadas en datos."

---

## 🎬 PARTE 2: LA IMPLEMENTACIÓN (1.5 minutos)
*Encuadre: Slide listando las soluciones: Data Loader, Flows y Dashboards.*

**Discurso:**
"Para cumplir con estos objetivos, implementamos tres grupos de soluciones técnicas en Salesforce:

Primero, para la **Carga Masiva**, utilizamos la herramienta Data Loader. Antes de importar los 1000 alumnos, configuramos reglas de coincidencia (Matching Rules) y usamos IDs Externos. Esto aseguró que los datos subieran correctamente sin generar registros duplicados.

Segundo, para las **Automatizaciones**, implementamos tres Flujos (Flows):
*   Un 'Screen Flow' que funciona como un asistente rápido en pantalla para la recepcionista.
*   Un flujo de registro que envía automáticamente un correo de bienvenida institucional cada vez que se inscribe a un alumno nuevo.
*   Un flujo programado (Scheduled Flow) que revisa el sistema los días viernes y genera automáticamente una Tarea de recordatorio al profesor si olvidó cargar una nota.

Tercero, configuramos los **Tableros de Control**. Construimos tres Dashboards específicos para la Dirección que consolidan: datos académicos, gestión de profesores y calidad de datos (como detectar registros sin email)."

---

## 🎬 PARTE 3: CONCLUSIÓN (45 segundos)
*Encuadre: Slide de transición a la demo en vivo.*

**Discurso:**
"Como resultado, hemos logrado reducir significativamente el tiempo operativo del personal administrativo y hemos brindado a la dirección los reportes necesarios para su gestión. Todo esto construido sobre la misma plataforma, sin necesidad de herramientas externas. A continuación, veremos directamente en el sistema cómo funcionan estas automatizaciones. Gracias."

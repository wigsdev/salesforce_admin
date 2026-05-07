# Guion de Demo en Vivo: Lumina Tech (Sprint 1)
**Tiempo asignado:** 4 Minutos.
**Enfoque:** "Mostrar lo implementado". No llenamos formularios para ahorrar tiempo. Mostramos evidencia de seguridad, estructura y calidad.

---

## 🎤 APERTURA
**Discurso:**
"Pasemos a la plataforma para ver cómo Salesforce resuelve los problemas de desorden y seguridad que planteó la Rectora. En este Sprint 1, nos enfocamos en construir los cimientos: una base de datos segura, organizada y con control de calidad automático."

---

## 🏛️ ESCENARIO 1: Estructura y Relaciones (1.5 Minutos)
*Objetivo: Mostrar la solución a la redundancia manual y la relación Alumno-Materia.*
*Encuadre: Registro de un Alumno (Contacto).*

**1. La Ficha Única del Alumno**
*   *(Acción: Abre el registro de un Alumno y muestra la información básica).*
*   **Discurso:** "La primera solicitud fue eliminar la redundancia. Aquí vemos la ficha central del alumno. Gracias al modelo relacional, los datos del estudiante se cargan una sola vez. No hay que repetir su nombre en cada proceso."
*   *(Acción: Haz clic en la pestaña 'Relacionado' y muestra la lista de 'Inscripciones').*
*   **Discurso:** "Aquí respondemos al dolor de cabeza de la Rectora: ¿Qué está cursando este alumno? En una sola mirada vemos todas sus **Inscripciones**. Si entro a una materia, puedo ver de inmediato su historial de **Evaluaciones**. La relación 'muchos a muchos' entre alumnos y materias está resuelta y es navegable con un solo clic."

---

## 🛡️ ESCENARIO 2: Calidad de Datos y Seguridad (1.5 Minutos)
*Objetivo: Mostrar las reglas de validación y la protección de información.*
*Encuadre: Registro de Alumno y Registro de Evaluación.*

**1. El Sistema como Filtro (Validaciones)**
*   *(Acción: Muestra el campo Email y el campo DNI en el Alumno).*
*   **Discurso:** "Para evitar los 'errores de dedo' que mencionaba la Rectora, el sistema ahora actúa como un filtro. Hemos configurado reglas que impiden guardar correos sin formato válido o alumnos sin su identificación legal (DNI). Ya no hay lugar para el olvido."
*   *(Acción: Abre una Evaluación y señala el campo 'Nota').*
*   **Discurso:** "Lo mismo ocurre con las calificaciones. El sistema bloquea físicamente cualquier nota fuera del rango de 1 a 10. Ya no es posible que un error de tipeo arruine los promedios institucionales."

**2. Privacidad de la Información**
*   **Discurso:** "En cuanto a la privacidad, hemos aplicado perfiles de seguridad. Aunque ahora lo vemos como administradores, un docente no puede ver los datos financieros de este alumno, y el personal administrativo no tiene permisos para alterar estas notas de examen. La integridad legal está garantizada."

---

## 📅 ESCENARIO 3: Gestión de Exámenes y Ciclos (1 Minuto)
*Objetivo: Mostrar el registro de notas y asistencias.*
*Encuadre: Lista Relacionada de Evaluaciones dentro de una Inscripción.*

**1. El Registro Académico**
*   *(Acción: Muestra una lista de Evaluaciones con sus fechas y estados).*
*   **Discurso:** "Finalmente, organizamos el ciclo de exámenes. Cada evaluación queda registrada con su fecha exacta y, como solicitó la dirección, incluimos el estado de asistencia. Si un alumno falta, queda constancia en su historial de forma permanente. Con esto, Lumina Tech tiene ahora el control total de su vida académica."

---

## 🏁 CIERRE
**Discurso:**
"Con esta base estructurada y segura, estamos listos para pasar al Sprint 2, donde veremos cómo automatizamos y cargamos los datos masivos sobre estos cimientos."

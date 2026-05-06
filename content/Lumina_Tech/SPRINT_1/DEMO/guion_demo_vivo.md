# Guion de Demo en Vivo: Lumina Tech (Sprint 1)
**Tiempo asignado:** 4 Minutos.
**Estrategia:** Demo ejecutada 100% como Administrador. Respondemos directamente a las peticiones de la `Solicitud.md` sin cambiar de usuario, explicando de forma narrativa las restricciones.

**Preparación técnica antes de empezar:**
1. Tener abierta la Lightning App "Gestión Académica Lumina".
2. Tener abierta la ficha de un Alumno de prueba con una Materia asociada, y listo para crearle un Examen y modificar su email.

---

## 🎤 TRANSICIÓN DESDE LA PPT
**Discurso:**
"Pasemos a la plataforma. La Rectora nos pidió profesionalizar la operación y atacar errores específicos. Veamos cómo esta base de datos resuelve esos dolores de cabeza cotidianos."

---

## 🏗️ ESCENARIO 1: La Estructura Académica (1.5 Minutos)
*Responde a la solicitud: "No quiero tener que escribir 'Juan Perez' veinte veces manuales... quiero abrir su ficha y ver su historial".*
*Encuadre: Pestaña Personas > Ficha de un Alumno.*

**1. Navegación y Relaciones**
*   *(Acción: Abre el registro de un Alumno. Muévete hacia la pestaña "Relacionado" o muestra las Related Lists).*
*   **Discurso:** "La primera queja de la dirección era la redundancia manual. Aquí estamos en la ficha central del alumno. Fíjense que gracias a la estructura relacional que construimos en este Sprint, ya no hay que tipear nada veinte veces. En esta misma pantalla vemos todas las **Inscripciones** a sus materias y, si hacemos un clic, vemos su historial exacto de **Evaluaciones** y **Asistencias**. Toda su vida académica está interconectada de forma automática."

---

## 🛡️ ESCENARIO 2: Calidad de la Información (1.5 Minutos)
*Responde a la solicitud: "Alguien escribió 'gmail,com'... le puso un '11' o '-5'... no podemos inscribir sin DNI".*
*Encuadre: Edición del Alumno y creación de una Evaluación.*

**1. Errores de Dedo (Email y DNI)**
*   *(Acción: Edita el correo del alumno, borra el punto y pon una coma `alumno@gmail,com` y haz clic en Guardar).*
*   **Discurso:** "La Rectora mencionó que los correos rebotaban por errores de dedo. Miren qué ocurre si alguien en administración escribe 'gmail con coma'. *(Muestra el error rojo)*. El sistema lo bloquea de inmediato. Lo mismo ocurre si intentan dejar el DNI vacío o ponerle letras."

**2. Rango de Notas**
*   *(Acción: Ve a la lista relacionada de Evaluaciones, haz clic en Nueva o edita una existente. Intenta poner un `11` en la nota y guarda).*
*   **Discurso:** "Y sobre las calificaciones que arruinaban los promedios... Si un profesor se equivoca y tipea un '11' o un número negativo en un examen, nuestro motor de validación salta al rescate. El dato corrupto jamás ingresa a la base de datos."

---

## 🔒 ESCENARIO 3: Privacidad de Roles (1 Minuto)
*Responde a la solicitud: "Si un administrativo cambia una nota, tenemos un problema legal grave".*
*Encuadre: Se mantiene en la pantalla del Examen (Evaluacion).*

**1. Seguridad Zero Trust (SoD)**
*   *(Acción: Señala con el mouse el botón 'Guardar' o el campo 'Nota').*
*   **Discurso:** "Finalmente, para resolver el riesgo legal. Como Administrador del Sistema, yo tengo acceso total. Pero hemos configurado los Permisos de Perfil (Zero Trust) de tal forma que, si la persona de Admisiones o Cobranzas entra a esta pantalla de Examen, el botón de editar y modificar notas está desactivado por completo para ellos. 

Con esta estructura interconectada, limpia y segura, hemos cumplido con los requisitos de la Rectora y dejado el terreno fértil para el Sprint 2."

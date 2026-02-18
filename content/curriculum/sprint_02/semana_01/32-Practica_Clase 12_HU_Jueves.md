# Salesforce Admin + Agent Force

**Guia:** Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol

---

# SUPERBADGE Y PROYECTO

**Guia:** Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol

## Superbadges: La Prueba de Fuego del Administrador

### ¿Qué es un Superbadge?
*   **No es un módulo normal.** Es una Credencial basada en Habilidades.
*   **Adiós a las instrucciones:** Aquí no existe el "Paso 1, haz clic aquí". Salesforce te da un Caso de Negocio (un problema real de una empresa ficticia) y tú debes decidir cómo resolverlo.
*   **Evaluación Automática:** Un "robot" entra a tu organización de Salesforce y verifica si la configuración funciona correctamente según los requisitos del cliente.

### ¿Por qué son vitales para tu carrera?
*   **El Puente Teórico-Práctico:** Los módulos te enseñan a usar el martillo; los Superbadges te piden construir una casa.
*   **Resume Booster (CV):** Los reclutadores saben que un Superbadge no se consigue leyendo, se consigue haciendo. Valen mucho más que 100 badges normales.
*   **Prerrequisito de Certificación:** Para algunas certificaciones avanzadas, debes tener ciertos Superbadges completados.

### ¿Qué camino voy a hacer hoy?

**PRIORIDADES:**
1.  Trails atrasados
2.  Superbadge obligatorios atrasados
3.  Proyecto tickets

**ORGANIZAR QUIÉN TRABAJA LOS JUEVES:** Los que estén menos atrasados

**¡Manos a la obra!**
Avanzamos con los trails.

---

## LINK de SP Flows

### Domina los Fundamentos de Flow
**Concepto Clave:** Flow es la herramienta definitiva de automatización "no-code" (sin código). Permite automatizar procesos de negocio complejos simplemente dibujando un diagrama de flujo.

**Puntos Importantes:**
*   Es el sucesor de Workflow Rules y Process Builder.
*   Permite interactuar con la base de datos (Crear, Leer, Actualizar y Borrar registros).
*   Funciona con lógica de "Si pasa esto, entonces haz esto".

### Los Dos Protagonistas del Superbadge
**Concepto Clave:** En este Superbadge, se evaluarán principalmente dos tipos de flujos. Es vital saber cuándo usar cuál.

#### Elementos de Datos (La Caja de Herramientas)
**Concepto Clave:** Para aprobar, el alumno debe saber manipular la base de datos. Estos son los elementos de color rosa en el Flow Builder.
*   **Get Records (Obtener Registros):** Buscar información que ya existe en Salesforce (Ej: "Búscame el ID de la cuenta asociada a este contacto").
*   **Create Records (Crear Registros):** Guardar información nueva.
*   **Update Records (Actualizar Registros):** Modificar algo que ya existe.
*   **Tip para el Junior:** En el Superbadge, presta mucha atención a los filtros dentro del elemento "Get Records". Si filtras mal, traes el dato equivocado.

#### Variables y Recursos (El "Cerebro" del Flow)
**Concepto Clave:** ¿Dónde guardamos la información mientras el flujo corre? En las Variables.
*   **¿Qué es una Variable?** Imagina una caja vacía donde guardas un valor (un texto, un número, una fecha) para usarlo más adelante en el flujo.
*   **Variable de Registro (Record Variable):** Una caja más grande que guarda toda la información de un registro (Ej: Todo el contacto, no solo el nombre).
*   **Fórmulas:** Se usan para calcular valores dinámicos (Ej: Calcular una fecha de vencimiento sumando 30 días a "hoy").

#### Debugging (Depuración)
**Concepto Clave:** Nunca actives un Flow sin probarlo. El Superbadge evalúa tu capacidad para encontrar errores.
*   **El botón "Debug":** Permite correr el flujo en modo simulado.
*   **Líneas Naranjas:** Muestran el camino que tomó el flujo. Si el flujo falló, la línea se detendrá donde hubo el error.
*   **Lectura de errores:** Enseña a no tener miedo a los mensajes de error; suelen decirte exactamente qué campo falta o qué filtro falló.

## LINK de SP Flows

### Flow Interactions: UX y Reusabilidad

#### Más allá de la Lógica (UX en Flow)
**Concepto Clave:** Un Flow puede funcionar perfectamente en el "Debug", pero si es difícil de usar para el usuario final, fracasará. Este módulo se centra en pulir la Experiencia de Usuario (UX).

**Puntos Importantes:**
*   Los Screen Flows no son estáticos; deben reaccionar a lo que hace el usuario.
*   Debemos evitar errores humanos antes de que sucedan (Validación).
*   Debemos evitar repetir trabajo (Reusabilidad).

#### Pantallas Dinámicas (Visibilidad y Validación)
**Concepto Clave:** No muestres campos que el usuario no necesita ver. Haz que el formulario sea inteligente.
*   **Visibilidad de Componentes:** Mostrar u ocultar campos según una respuesta previa.
    *   *Ejemplo:* Si marcas "Tiene mascota", aparece el campo "¿Qué tipo de mascota?". Si no, se oculta.
*   **Validación de Entrada (Input Validation):** Reglas para asegurar la calidad del dato mientras se escribe.
    *   *Ejemplo:* Impedir que alguien ponga una fecha de nacimiento futura con un mensaje de error personalizado.

#### Subflows (El poder de "Lego")
**Concepto Clave:** No reinventes la rueda. Si tienes una lógica que usas mucho (ej: enviar un correo de bienvenida o calcular un descuento), crea un flujo pequeño y llámalo desde otros flujos.
*   **¿Qué es un Subflow?** Es un flujo dentro de otro flujo (Flujo Padre y Flujo Hijo).
*   **Variables de Entrada/Salida:** Para que funcionen, el "Padre" debe enviarle datos al "Hijo" (Input), y el "Hijo" debe devolver resultados al "Padre" (Output).
*   **Beneficio:** Si necesitas cambiar la lógica, solo la cambias en un lugar (el Subflow) y se actualiza en todos lados.

#### Acciones Externas (Actions)
**Concepto Clave:** Flow no vive en una isla. Necesita comunicarse con herramientas estándar de Salesforce.
*   **Core Actions:** Son acciones preconstruidas que Flow puede ejecutar.
    *   **La más importante para el examen:** Send Email (Enviar Correo).
    *   Configurar el cuerpo del correo (Body), el asunto (Subject) y los destinatarios (Recipients) usando variables dentro del flujo.
*   **Otras acciones:** Postear en Chatter, Enviar notificaciones personalizadas, o Submit for Approval (Enviar para aprobación).

#### Distribución (¿Dónde vive el Flow?)
**Concepto Clave:** Has creado el Flow, pero... ¿cómo lo encuentra el usuario? Activar el flow no es suficiente.
*   **Lightning Pages (App Builder):** Arrastrar el componente "Flow" dentro de una página de registro (Record Page) o página de inicio (Home Page).
    *   *¡Ojo!:* Recuerda pasar el recordId al flujo para que sepa en qué registro está trabajando.
*   **Botones (Actions):** Crear un botón ("Quick Action") que lance el Flow en una ventana emergente.
*   **Utility Bar:** Poner el flow en la barra inferior fija de la aplicación.

---

# Práctica Profesional - PROYECTO

## EQUIPOS
**Proyecto - Práctica**

## DAILY

**⚡ Daily (5 min):**

**Enfoque: Integridad de Datos.**
*   **Pregunta clave:** "¿La relación debe ser Master-Detail (fuerte) o Lookup (flexible)? ¿Cómo afecta esto?"

**Enfoque: Navegación.**
*   **Pregunta clave:** "¿Es intuitivo moverse entre pestañas? ¿La App tiene demasiadas cosas innecesarias?"

## AMBIENTES
✅ 2 Usuarios

**PRIORIDAD:**
**Trello:**
1.  Tickets Atrasados
2.  Tickets de HOY
3.  Una vez listos se deja en la pestaña DevOps Dev

## DEV
✅ **POR DIA**
*   Tickets del día (2 personas en Dev)

**El resto del equipo:**
1.  Trails
2.  SuperBadge
3.  Análisis de Tickets
4.  Preguntas y dudas
5.  Bloqueos

**NO RECARGAR A LAS MISMAS PERSONAS POR DIA**

---

# JUEVES - ETAPA 3

## OBJETIVO
Creación de formularios (Page Layouts), Fórmulas y Validaciones.

**⏱️ TIP de Gestión del Tiempo:** "Prueba Unitaria Inmediata". Cada vez que crees una Regla de Validación, intenta romperla inmediatamente. No esperes al final.

**⚡ Daily (5 min): Enfoque: Bloqueo de Errores.**
*   **Pregunta clave:** "¿Estamos frustrando al usuario con demasiadas validaciones o protegiendo la base de datos?"

## ROLES
**👥 Roles:**
*   **BA:** Define las reglas de negocio (ej. "No se puede cerrar una venta sin fecha").
*   **PO:** Decide qué campos son obligatorios en el Page Layout.
*   **Consultant:** Escribe las fórmulas complejas para evitar trabajo manual.
*   **QA:** Crea una lista de "Datos Sucios" para intentar ingresarlos y ver si el sistema los bloquea.

## SALESFORCE ADMINISTRATOR
✅ **Tareas del día (Admin):**
1.  Diseñar Page Layouts y Lightning Record Pages (Dynamic Forms si aplica).
2.  Crear Campos de Fórmula (Calculados).
3.  Configurar Reglas de Validación (Validation Rules).
4.  Crear List Views útiles para cada perfil.

---

# VIERNES

✅ **TRABAJAR EN**
1.  Proyecto
2.  Trails atrasados o adelantar
3.  Estudiar conceptos

## BLOQUEOS
**📢 Comunicación con TL:** Reportar inmediatamente si hay problemas de licencias o acceso al entorno. DUDAS

**¡Manos a la obra!**

Vamos ingresar para mostrarles cómo se crea una organización práctica y que todos puedan crear una.
Indiquemos que investiguen la organización, que entren y revisen
**link:** https://trailhead.salesforce.com/es/users/profiles/orgs
Compartir pantalla para que vean como se hace el proceso

**¿Cómo nos fué? ¿Qué cosas no quedaron claras y necesitamos repasar la próxima?**
retro

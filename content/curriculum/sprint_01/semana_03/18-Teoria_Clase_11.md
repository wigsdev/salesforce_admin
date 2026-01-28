# Salesforce Admin + Agent Force (Teoría Clase 11)

**Daily**
*   Del 1 al 10 ¿cómo te sentís?
*   ¿Qué te proponés para hoy?

---

> *Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN*

## Skills Técnicas (El "Qué" haces)
*   **Gestión de Usuarios y Seguridad**: El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
*   **Gestión de Datos (Data Management)**: Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
*   **Automatización Básica (Flows)**: Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
*   **Reportes y Dashboards**: Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.
*   **AgentForce**: puedas familiarizarte con la configuración de agentes dentro de Salesforce.

> *Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN*

## Skills Blandas (El "Cómo" lo haces)
*   **Comunicación Traducida**: Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
*   **Resolución de Problemas (Google-Fu)**: No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
*   **Mentalidad de Aprendiz (Learner's Mindset)**: Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
*   **Atención al Detalle**: Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.

> *Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN*

---

## Colaboración
*   Aprender con y de otras personas

### Ausencias
*   Seguir con la planilla y actividades

### MIC o CHAT
*   Comunicación

### Errores / Atrasados
*   **JUEVES**: Preguntas al final de la clase Teórica.

### Para una buena clase…
*   **Autonomía**: Utilizar las herramientas.

---

## Conjunto de Permisos y seguridad basados en sesiones
*vamos a ver la segunda parte de modelado de datos…*

### El Concepto:
"Romper el vidrio en caso de emergencia"

### El Mecanismo: Activación vía Flow
Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:
*   La **Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
*   La **Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

### El Caso de Uso Real: Contexto y Expiración
**¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
Usamos la herramienta de **Merge (Fusionar)**. Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
*Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## Seguridad con Flow
LINK

### Crear un conjunto de permisos basado en sesión

#### 1. El Concepto (Qué es)
Es un conjunto de permisos que no está activo todo el tiempo. A diferencia de los permisos normales (que el usuario tiene siempre), estos solo funcionan durante una sesión específica activada. Es como una "llave temporal".

#### 2. La Diferencia Técnica (Cómo se crea)
El proceso de creación es idéntico al de un Conjunto de Permisos estándar, con una única excepción crucial:
*   Debes marcar la casilla: **"Activación de sesión requerida" (Session Activation Required)**.

#### 3. El Propósito (Por qué usarlo)
Sirve para proteger datos sensibles y limitar la exposición al riesgo. Se usa cuando un usuario necesita derechos poderosos o acceso a datos confidenciales, pero solo por momentos breves, no permanentemente.

#### 4. El Ejemplo Práctico (Caso de Uso)
**Escenario**: Un Gerente de Contratación necesita ver contratos de trabajo (datos confidenciales).
**Funcionamiento**:
1.  El gerente activa la sesión (obtiene el permiso).
2.  Revisa los contratos.
3.  Al terminar (o cerrar sesión), el permiso se desactiva.
4.  Si necesita verlos de nuevo mañana, debe reactivar la sesión.

---

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## Pasos Importantes

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## Pasos Importantes

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## CHALLENGE

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## CHALLENGE

### ⚠️ Puntos Críticos (Donde suelen fallar)
1.  **El Perfil Base (¡Ojo aquí!)**:
    *   La instrucción pide clonar el perfil "Minimum Access - Salesforce".
    *   *El error común*: Muchos clonan el "Standard User" por costumbre. Asegúrate de que busquen el de "Minimum Access" para que Lynda empiece con cero permisos (principio de menor privilegio).
2.  **La Licencia del Conjunto de Permisos**:
    *   La imagen pide explícitamente **License: None** en el Permission Set.
    *   *El error común*: Seleccionar "Salesforce" en el desplegable de licencia. Si eligen una específica, se limitan a futuro. Dejarlo en "None" lo hace más flexible.
3.  **El Permiso "Modificar Todo" (Modify All)**:
    *   No basta con dar acceso de lectura o edición. La instrucción pide "Modify All" en el objeto Cuenta (Account).
    *   *El error común*: Marcar solo "Edit" y "Create". Deben buscar la casilla específica de "Modify All" (que auto-selecciona las demás).
4.  **Nombres de API exactos**:
    *   Salesforce corrige automáticamente, pero recuérdales que `Temporary Account Edit` debe tener el API Name `Temporary_Account_Edit`. Un espacio o guion bajo extra puede hacer fallar el validador automático.

---

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## Activar conjuntos de permisos basados ​​en sesiones sin código

### 1. El Modelo de Datos (Backend)
Para que el permiso funcione, interactúan dos objetos clave en la API:
*   **PermissionSet**: Contiene la definición del permiso. El campo booleano `HasActivationRequired` está en `true`, lo que impide su asignación pasiva estándar.
*   **SessionPermSetActivation**: Es el objeto de intersección que gestiona la activación en tiempo real.

### 2. La Lógica de Activación (Runtime)
La activación no es más que una operación DML de inserción. Para activar el permiso, el sistema debe crear un registro en el objeto `SessionPermSetActivation` con dos parámetros obligatorios:
*   `AuthSessionId` (El ID de la sesión actual del usuario).
*   `PermissionSetId` (El ID del conjunto de permisos a activar).

### 3. Métodos de Implementación
*   **Vía Programática (API SOAP)**: Se escribe código para insertar manualmente el registro en `SessionPermSetActivation`.
*   **Vía Declarativa (Flow Builder)**: Se utiliza un Flow que ejecuta la acción de activación (por debajo, el Flow realiza la inserción en el objeto `SessionPermSetActivation` sin que el usuario toque código).

---

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## PARA EMPEZAR

### 1. La Herramienta: Screen Flow (Flujo de Pantalla)
No usaremos código, sino un Flujo de Pantalla simple.

### 2. La Lógica (El "Motor")
Dentro del Flow, se usa una Acción Core específica llamada: "**Activar conjunto de permisos basado en sesión**".
*   **Parámetro clave**: Esta acción pide un Input obligatorio: el API Name exacto del Conjunto de Permisos (ej. `Employment_Contracts_Access`).

### 3. El Requisito de Arquitectura (Donde falla la mayoría)
Para que el Flow funcione, el Conjunto de Permisos debe estar **pre-asignado** al usuario.
*   **El Error**: Si el usuario ejecuta el Flow sin tener el permiso asignado previamente, Salesforce lanza un error de "Falta de asignación". No se puede activar lo que no se tiene asignado.

### 4. Permisos del Usuario (Lynda)
Para que el usuario pueda "auto-activarse" este permiso ejecutando el Flow, necesita en su perfil base:
*   `Lightning Experience User` (para acceder a la interfaz).
*   `Manage Flow` (o Ejecutar Flujos) para poder lanzar la automatización.
*   **Resultado**: Al hacer clic en "Ejecutar" en el Flow, la inyección de permisos es inmediata (aparece el botón "Nuevo" en Contratos) sin necesidad de cerrar sesión.

---

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## RETO

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## Crear un acceso fácil al flujo de activación

### 1. El Problema (Experiencia de Usuario)
"Pedirle a un Gerente de Contratación que entre a la configuración para ejecutar un Flow es una mala práctica. Es confuso, poco profesional y requeriría darles permisos técnicos que no deberían tener."

### 2. La Alternativa Difícil (Visualforce)
"Podríamos crear una pestaña con código (Visualforce), pero eso implica escribir markup (código). Para un Admin Junior, esto añade complejidad innecesaria."

### 3. La Solución Ideal (Lightning App Page)
"Usamos una Página de Aplicación Lightning porque es la solución 100% No-Code."
*   **Ventaja**: Arrastras y sueltas el componente del Flow en una pantalla bonita.
*   **Resultado**: El usuario ve una interfaz limpia y moderna, y nosotros nos ahorramos programar. Es la forma más rápida y elegante de poner ese 'botón de activación' en manos del usuario final."

---

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## Crear un acceso fácil al flujo de activación

### 1. El Contenedor (Lightning App Page)
Utilizamos Lightning App Builder para crear una Página de Aplicación (App Page) de una sola región. Esto nos da un lienzo en blanco dentro de la interfaz de usuario.

### 2. La Integración del Flow
Arrastramos el componente estándar Flow al lienzo y lo vinculamos al flujo que creamos antes (`Activate Contracts Access...`).
*   **Técnicamente**: Esto convierte la lógica de backend (el Flow) en un elemento visual accesible en el frontend.

### 3. Despliegue (Activación)
En el paso de Activación, añadimos esta página específicamente a la Aplicación "Ventas" (Sales).
*   **Resultado**: Se crea automáticamente una nueva pestaña de navegación en la barra superior de la App de Ventas.

### 4. Validación (Test)
*   **Estado Inicial**: El usuario (Lynda) entra y no ve el botón "Nuevo" en Contratos (solo lectura).
*   **El Disparador**: Lynda hace clic en la nueva pestaña creada. El Flow se ejecuta automáticamente al cargar el componente.
*   **Estado Final**: Al volver a Contratos, el permiso de sesión ya está inyectado y aparecen las opciones CRUD (Crear/Editar).

---

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## RETO

> **¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
> Usamos la herramienta de Merge (Fusionar). Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## ¡Manos a la obra!
Avanzamos con los trails.

**Guia**: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol.

---

### Leer Con Atención
Las prácticas previas al challenge son importantes para entender el challenge. **NO DEJARLAS PASAR**.

**ATENCIÓN / ERRORES**
*   Agotar herramientas.
*   Consultar con su grupo.
*   Hacer una nueva ORG.
*   Recién consultar a los profesores.

**CONSULTAS**
*   Haber agotado todas las instancias de herramientas.
*   Contexto: **SB-Jueves**.

### Pair Programming
*   Compartir pantalla.
*   Hablar sobre el proceso del Trailhead.
*   Ir rotando.
*   No se puede estar en silencio.
*   El trabajo individual es fuera de la cursada.

### Seguridad
*   LINK

---

## Posibles Preguntas

### 1. La pregunta de Cenicienta: ¿Cuándo se acaba el encanto?
**Alumno**: "Profe, si activo el permiso a las 10:00 AM, ¿tengo que volver a activarlo a las 11:00 AM?"
**Respuesta**: "Depende de tu Sesión. El permiso dura mientras mantengas la sesión activa.
*   Si cierras el navegador: Se pierde.
*   Si le das a 'Cerrar Sesión' (Logout): Se pierde.
*   Si te vas a almorzar y Salesforce te expulsa por inactividad (Timeout): Se pierde. Mientras estés trabajando activamente, el permiso sigue vivo. No tiene un cronómetro fijo (como '1 hora'), está atado a tu conexión".

### 2. ¿Puedo desactivarlo manualmente?
**Alumno**: "Ya terminé de borrar los datos sensibles. ¿Puedo apagar el permiso yo mismo para estar seguro, sin cerrar sesión?"
**Respuesta**: "¡Excelente pregunta de seguridad! Sí, pero necesitas construir otro mecanismo (otro Flow) que ejecute la acción inversa: '**Deactivate Session-Based Permission Set**'. En la práctica, la mayoría de las empresas confían en que expire solo, pero para casos muy críticos, se crea un botón de 'Terminar Modo Admin'".

> "¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path. No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'. Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

### 3. El error clásico del Checkbox
**Alumno**: "Creé el Permission Set, le puse los permisos, se lo asigné al usuario... pero el usuario ya tiene los permisos activos sin correr el Flow. ¿Qué hice mal?"
**Respuesta**: "Te olvidaste del paso más importante: La casilla mágica. Dentro del Permission Set, hay una opción que dice '**Session Activation Required**'.
*   **Sin marcar**: Es un permiso normal y corriente (siempre activo).
*   **Marcada**: El permiso se vuelve 'invisible' y espera a ser activado. Si el usuario lo tiene siempre, es porque olvidaste marcar esa casilla".

### 4. ¿Por qué Flow? ¿No hay otra forma?
**Alumno**: "No soy bueno con los Flows todavía. ¿No puedo activarlo con una regla o un botón simple?"
**Respuesta**: "Nativamente (sin código), Flow es la única llave. Salesforce necesita una lógica que diga 'Haz esto AHORA'. Los programadores (Developers) pueden hacerlo con código Apex, pero como Administradores, Flow es nuestra herramienta. ¡Es una buena excusa para perderle el miedo a los flujos!".

> "¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path. No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'. Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

### 5. El usuario "híbrido" (Conflicto de permisos)
**Alumno**: "Tengo un usuario que tiene el permiso de 'Editar Contratos' en su Perfil (fijo) y también en un Session-Based Set (temporal). ¿Qué pasa?"
**Respuesta**: "Gana el permiso más abierto/permanente. Si ya lo tiene en su Perfil, el Session-Based Set es irrelevante. No puedes 'restringir' u ocultar algo que el Perfil ya da. Para que esto funcione: Debes quitarle el permiso del Perfil y dejárselo solo en el Session-Based Set".

### 6. La doble autenticación (MFA)
**Alumno**: "¿Puedo hacer que el Flow pida contraseña de nuevo antes de activar el permiso?"
**Respuesta**: "¡Sí! Y es una práctica 'Pro'. En el Flow, antes de la acción de activar permiso, puedes poner un paso que verifique si el usuario inició sesión con Alta Seguridad (High Assurance) o pedirle que confirme su identidad. Así te aseguras de que sea él y no alguien que encontró su PC desbloqueada".

> "¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path. No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'. Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

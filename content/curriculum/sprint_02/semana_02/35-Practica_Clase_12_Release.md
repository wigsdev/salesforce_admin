# Salesforce Admin + Agent Force

## DevOps
**Como pasar los cambios de Dev a QA a PROD**

## El Arte del Release: Llevando valor a Producción

Hoy vamos a entender por qué fallan los proyectos. No fallan por código, fallan por comunicación. El cliente habla de 'dolores' y 'dinero', y Salesforce habla de 'Objetos' y 'Flows'. Nuestro trabajo es ser el puente entre esos dos mundos. Vamos a ver los roles que hacen esto posible.

### ¿Qué es un Release?
**No es solo código, es una solución empaquetada.**

*   **Un Release es un paquete de valor.**
*   Es un conjunto de funcionalidades (nuevos campos, flujos, permisos) que han sido probados y aprobados, listos para que el usuario final los use.
*   Piensen en esto como un envío de Amazon: no enviamos los productos sueltos; los empaquetamos, los sellamos y los entregamos juntos para asegurar que lleguen bien.

### ¿Por qué un día específico?
**Estabilidad y Disponibilidad.**
¿Por qué no hacemos deploy a Producción un martes a las 11 de la mañana o un viernes a las 6 de la tarde?

1.  **Estabilidad:** Necesitamos un momento donde los usuarios no estén trabajando activamente para evitar interrumpir sus ventas o servicios.
2.  **Capacidad de Reacción:** Si hacemos un Release un viernes y algo falla, pasaremos el fin de semana arreglándolo. Si lo hacemos un jueves por la tarde/noche, tenemos todo el viernes para dar soporte con el equipo completo.
3.  **Hábito:** El negocio debe saber cuándo esperar cambios. A esto le llamamos 'Ventana de Mantenimiento'.

### El Ciclo de Vida
**El camino de la confianza.**
La teoría dicta que un cambio debe ganar 'confianza' a medida que avanza.

1.  En **Dev**, el cambio es inestable (borrador).
2.  En **QA**, verificamos que no rompa nada técnico.
3.  **Pero el paso crítico es antes del Release: la aprobación en PROD.** Solo lo que funciona perfectamente y está aprobado por el negocio merece llegar a Producción. Nunca, bajo ninguna circunstancia, se pasa algo directo de Dev a Prod.

### ¿Cómo se hace?
**Selección, Validación y Despliegue.**
En la práctica, ustedes como Admins harán esto:

1.  **Selección (Bundling):** Agrupan los Work Items (sus tickets de Jira/Trello asociados a los cambios) que van al Release.
2.  **Validación:** Antes de empujar, el sistema hace una 'simulación' contra Producción. Verifica si faltan dependencias (ej. intentas pasar un Flow pero olvidaste pasar el Campo que usa ese Flow).
3.  **Despliegue (Promotion):** Si la validación es exitosa, ejecutan el despliegue.
4.  **Post-Deployment:** Pasos manuales (ej. asignar un Permission Set a un usuario específico).

### El Rol del DevOps Specialist
**El guardián de la integridad.**
Quizás piensen: 'Si la herramienta lo hace solo, ¿para qué está el especialista?'.

*   **El DevOps Specialist no es solo quien aprieta el botón. Es el Guardián de Producción.**
*   **Resuelve Conflictos de Merge:** Cuando dos Admins tocan el mismo campo y el sistema no sabe con cuál quedarse.
*   **Mantiene los ambientes sincronizados (Back-promotion):** Asegura que lo que está en Prod, también regrese a los entornos de Dev para que todos trabajen sobre la última versión.
*   **Es quien dice 'NO'** si un Release no pasó las pruebas.

---

**¡Manos a la obra!**

Vamos ingresar para mostrarles cómo se crea una organización práctica y que todos puedan crear una.
Indiquemos que investiguen la organización, que entren y revisen
**link:** https://trailhead.salesforce.com/es/users/profiles/orgs
Compartir pantalla para que vean como se hace el proceso

**Elegir fecha**
1
Elegir fecha para el Release y debe estar presente los TL

**Tener la cuenta de Github.**
Conectar a DevOps
El responsable tiene que hacerlo con un TL

**¿Cómo nos fué? ¿Qué cosas no quedaron claras y necesitamos repasar la próxima?**
retro

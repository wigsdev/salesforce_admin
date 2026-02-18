# Superbadge: Fundamentos de Flow (Flow Fundamentals)

## Lo que harás para ganar este Superbadge
*   Actualizar flujos existentes para mejorar la automatización.
*   Usar flujos para enviar correos electrónicos, calcular valores y actualizar registros.

## Conceptos puestos a prueba en este Superbadge
*   Configurar elementos de Acción y Crear Registro.
*   Usar Recursos y Acciones de Flujo para guardar un registro en una variable de registro.
*   Usar elementos Obtener (Get), Actualizar (Update), Decisión (Decision), Asignación (Assignment) y Bucle (Loop) en un flujo.
*   Crear una fórmula en un flujo.

## Nota
Estamos trabajando duro para traerte contenido de superbadge actualizado que refleje las mejoras del producto y las mejores prácticas de la industria. Para completar este superbadge, trabajarás con bucles en flujos, pero te recomendamos revisar también el elemento de transformación (Transform element) que ahora está disponible con flujos. Para más información, consulta esta documentación de Ayuda.

## Trabajo Previo y Notas

### Regístrate para una Developer Edition Org con Configuración Especial
Para completar este superbadge, necesitas una Developer Edition org especial que contiene una configuración especial y datos de muestra. Ten en cuenta que esta Developer Edition org está diseñada para funcionar con los desafíos de este superbadge.

1.  Regístrate para una [Developer Edition org gratuita con configuración especial](https://developer.salesforce.com/promotions/orgs/superbadge-flow-fundamentals).
2.  Completa el formulario. Para la dirección de correo electrónico, ingresa una dirección de correo electrónico activa.
3.  Después de completar el formulario, haz clic en **Sign me up**.
4.  Cuando recibas el correo electrónico de activación (esto puede tardar unos minutos), ábrelo y haz clic en **Verify Account**.
5.  Completa tu registro configurando tu contraseña y pregunta de desafío. **Consejo:** Guarda tu nombre de usuario, contraseña y URL de inicio de sesión en un lugar seguro (como un administrador de contraseñas) para acceder fácilmente más tarde.
6.  Ya has iniciado sesión en tu Developer Edition org de la superbadge.

### Ahora, conecta tu nueva Developer Edition org a Trailhead.
1.  Asegúrate de haber iniciado sesión en tu cuenta de Trailhead.
2.  En la sección de Desafío al final de esta página, selecciona **Connect Org** de la lista desplegable.
3.  En la pantalla de inicio de sesión, ingresa el nombre de usuario y la contraseña de la Developer Edition org que acabas de configurar.
4.  En la página **Allow Access?**, haz clic en **Allow**.
5.  En la página **Want to connect this org for hands-on challenges?**, haz clic en **Yes! Save it**. Serás redirigido de nuevo a la página del Desafío y estarás listo para usar tu nueva Developer Edition org para ganar este superbadge.

Ahora que tienes una organización de Salesforce con una configuración especial para este superbadge, estás listo para comenzar.

### Consejos
*   Ingresa todas las etiquetas (labels) exactamente como se describen en las instrucciones. Las etiquetas distinguen entre mayúsculas y minúsculas y la ortografía cuenta.
*   Cuando sea posible, copia y pega los nombres de las etiquetas de las instrucciones del superbadge en lugar de escribirlos.
*   Si no se especifican los nombres de las etiquetas, puedes usar cualquier nombre que elijas; esto se aplica a algunos elementos de Asignación y fórmulas.
*   Los superbadges se centran en objetivos muy específicos; algunas mejores prácticas o enfoques típicos pueden no ser necesarios en los desafíos.
*   Asegúrate de guardar tu trabajo antes de ejecutar la verificación del desafío.
*   Asegúrate de no crear registros duplicados, etiquetas, conjuntos de permisos, etc., como parte de cualquier desafío.
*   Construye tu solución de acuerdo con los requisitos; agregar más acciones o pasos puede hacer que las verificaciones del desafío fallen.

### Nota
Antes de comenzar los desafíos, revisa **Flow Elements and Resources Superbadges: Trailhead Challenge Help**. Consulta la sección de accesibilidad para obtener más información sobre el lector de pantalla y la accesibilidad del teclado dentro de Flow Builder.

Si has completado el **Superbadge: Flow Optimization** o el **Superbadge: Flow Administration**, puedes usar la misma Developer Edition org para completar los desafíos en este superbadge. Si no, asegúrate de estar utilizando una nueva Developer Edition org desde este enlace de registro. Si usas una org que ha sido utilizada para otros trabajos, no aprobarás los desafíos en este superbadge.

## Caso de Uso
**Dreamscape Bookshops** ha florecido en los últimos años por una razón: el servicio al cliente. Como una red global de librerías locales, Dreamscape ha encontrado una manera de conectar a los lectores con nuevos libros de los que probablemente nunca hayan oído hablar. Eso es porque Dreamscape trabaja con editoriales independientes y autores para identificar nuevas obras que a los lectores les encantarán. Su personal proporciona un compromiso de nivel de conserje para conectar a los lectores con nuevas obras.

Este innovador servicio de coincidencia libro-lector es lo que ayudó a Dreamscape a crecer, y el servicio al cliente personalizado ha mantenido su crecimiento. Dreamscape también tiene un programa de fidelización que está tratando de maximizar, para dar realmente una atención de primer nivel a sus lectores más leales.

Actualmente, cada librería pasa varias horas al día emparejando cuidadosamente a los lectores con nuevos libros. Los equipos de la tienda luego envían correos electrónicos a los lectores para informarles sobre nuevas coincidencias, eventos y otros acontecimientos divertidos. Como fanático desde hace mucho tiempo de Dreamscape Bookshops, estás encantado de estar en el equipo que ayudará a automatizar este proceso y ahorrar al personal mucho tiempo. Revisa los requisitos de automatización de Dreamscape e identifica formas de simplificar su trabajo. Luego, ¡siéntate y disfruta de nuevas recomendaciones de libros!

## Requisitos de Negocio

### Regalo de Pedido de Libros (Book Order Giveaway)
Los pedidos personalizados también mantienen satisfechos a los lectores leales. Un flujo existente llamado **Book Order** ayuda al equipo de cumplimiento (fulfillment team) a asegurar que los libros estén rápidamente en camino, creando tareas para que los equipos verifiquen los pedidos de libros.

El equipo quiere agregar un nuevo paso a este proceso para agregar un artículo gratis a ciertos pedidos. Los pedidos con tres o más libros deben incluir un marcador gratuito, y los pedidos con cinco o más libros deben recibir un marcador y una pegatina.

Ajusta el flujo existente llamado **Book Order** para crear tareas relacionadas con ciertos pedidos.

1.  Usa un elemento de Decisión llamado `How Many Books in the Order?`.
2.  Si el pedido tiene tres o cuatro libros, crea una tarea con el asunto `Add Bookmark`. Usa la lógica `Equals 3 OR 4` en el elemento de Decisión.
3.  Si el pedido tiene cinco o más libros, crea una tarea con el asunto `Add Bookmark and Sticker` usando la lógica `Greater Than or Equal to 5`.
4.  Usa el elemento **Get Records** para la Cola (Queue) para asociar las tareas a la cola del Equipo de Cumplimiento (**Fulfillment Team queue**).
5.  Asegúrate de que las tareas estén relacionadas con la venta actual. **Consejo:** Establece los campos `OwnerId` y `WhatId`.
6.  Establece el tiempo de respuesta para completar la tarea en 24 horas usando un recurso de fórmula llamado `DueDate` para el campo `ActivityDate`. Usa la fórmula `{!$Flow.CurrentDate}+1`.

**Nota:** Es posible configurar este desafío de múltiples maneras, pero por el bien de configurar tu solución, configúralo con múltiples elementos **Create Records** y sin elementos de **Assignment**. Puedes probar tu automatización con el flujo llamado **Book Order**, disponible en el registro de Contacto. Como confirmación opcional de tu trabajo, usa el flujo para crear rápidamente un registro de Pedido de Libro con partidas de libros.

### Correo Electrónico de Recomendación (Recommendation Email)
Cada semana, el equipo de contenido revisa un informe de nuevos libros en el sistema y prepara resúmenes rápidos destacando nuevos libros. El equipo de contenido también se comunica individualmente con los lectores leales con recomendaciones personalizadas. Un campo personalizado en el objeto **Book** llamado `Recommendation` permite al equipo de contenido describir cómo un nuevo libro podría intrigar a los lectores con ciertos intereses. Un campo de fórmula existente, `Why should you read this book?`, rellena esa información en el registro de contacto.

Un flujo de pantalla (Screen Flow) en el registro de Contacto, **Recommendation Email**, debería permitir al equipo de contenido enviar un correo electrónico a un lector desde ese registro de Contacto después de cualquier actualización que realicen. El administrador anterior se fue antes de que este flujo estuviera terminado.

1.  Ajusta el recurso Plantilla de Texto (**Text Template**) `EmailBody` para incluir información sobre el libro en el campo `Current Recommendation` del cliente, incluyendo el título, autor y resumen. Asegúrate de que el primer nombre del lector se rellene en la primera línea del correo electrónico.
2.  Asegúrate de que el flujo también actualice el registro de Contacto para agregar la fecha y hora de esta comunicación en el campo `Last Outreach`.

**Nota:** Es posible configurar este desafío de múltiples maneras, pero por el bien de configurar tu solución, actualiza el contacto usando la variable de registro del elemento **Get Records** llamado `Get Customer Info`, y usa una variable global `$Flow` para la fecha y hora.

El flujo existente es genial, pero confunde a parte del equipo. Agrega un elemento de pantalla al flujo **Recommendation Email** llamado `Confirmation Screen` con nombre de API `Confirmation_Screen`. El nuevo elemento de pantalla debe mostrar el texto `Your email has been sent`. El elemento **Confirmation Screen** debe ser el elemento final en el flujo **Recommendation Email**.

**Consejo:** Puedes probar este flujo para revisar tu trabajo; debes configurar la Dirección de Correo Electrónico del Usuario de Proceso Automatizado en la página de Configuración de Automatización de Procesos para hacerlo. No estamos comprobando si el flujo está activo o la configuración relacionada en este superbadge.

### Programa de Fidelización Dreamscape (Dreamscape Loyalty Program)
Los lectores de Dreamscape son lectores leales. El programa de fidelización recompensa a los lectores por sus compras, reseñas en línea y más. El flujo **Birthday Loyalty Points Update** envía un correo electrónico a un lector en su cumpleaños. Una nueva característica del programa de fidelización será popular: ¡puntos gratis asignados en el cumpleaños del lector!

| Nivel (Level) | Puntos Necesarios para Alcanzar el Nivel |
| :--- | :--- |
| **Gold** | 10,000 |
| **Silver** | 5,000 |
| **Bronze** | 2,000 |

Ajusta el flujo **Birthday Loyalty Points Update** para acomodar este cambio. Obtén el estado de fidelización actual del lector del campo `Loyalty Status`, y los puntos actuales del campo `Loyalty Points` en el registro de Contacto. Asigna puntos de bonificación de cumpleaños basados en lo siguiente:

*   **Gold**: 500
*   **Silver**: 250
*   **Bronze**: 100

Usa la siguiente lógica en el flujo para actualizar el valor de puntos en Contacto con puntos especiales de cumpleaños.

```sql
Case ({!Loop_Through_Contacts.Loyalty_Status__c},
    'Bronze', {!Loop_Through_Contacts.Loyalty_Points__c} + 100,
    'Silver', {!Loop_Through_Contacts.Loyalty_Points__c} + 250,
    'Gold', {!Loop_Through_Contacts.Loyalty_Points__c} + 500,
    {!Loop_Through_Contacts.Loyalty_Points__c}
)
```

¡Guau, realmente has mejorado las automatizaciones para Dreamscape! Considera continuar con el **Superbadge: Flow Optimization** para seguir entregando tanta funcionalidad adicional.

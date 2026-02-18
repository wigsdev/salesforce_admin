# Superbadge: Data Quality and Validation

## Lo que tendrás que hacer para ganar esta Superbadge
*   Identificar y abordar los campos afectados por problemas de calidad de datos.
*   Implementar una solución para limpiar y prevenir registros de contactos duplicados.
*   Construir reglas de validación para proteger la calidad de los datos de ventas.
*   Hacer cumplir los procesos de negocio con Flow.

## Conceptos puestos a prueba en esta Superbadge
*   Calidad de Datos (Data Quality)
*   Validación de Datos (Data Validation)

## Trabajo Previo y Notas

### Regístrate para una Developer Edition Org con Configuración Especial
Para completar esta superbadge, necesitas una Developer Edition org especial que contiene una configuración especial y datos de muestra. Ten en cuenta que esta Developer Edition org está diseñada para funcionar con los desafíos de esta superbadge.

1.  Regístrate para una [Developer Edition org gratuita con configuración especial](https://developer.salesforce.com/promotions/orgs/superbadge-data-quality).
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
5.  En la página **Want to connect this org for hands-on challenges?**, haz clic en **Yes! Save it**. Serás redirigido de nuevo a la página del Desafío y estarás listo para usar tu nueva Developer Edition org para ganar esta superbadge.

Ahora que tienes una organización de Salesforce con una configuración especial para esta superbadge, estás listo para comenzar.

### Nota
Antes de comenzar los desafíos, por favor revisa **Data Quality and Validation Superbadge: Trailhead Challenge Help**.

Asegúrate de estar utilizando una nueva Developer Edition org desde este enlace de registro para completar los desafíos en esta superbadge. Si utilizas una org que ha sido utilizada para otros trabajos, no aprobarás los desafíos en esta superbadge.

Recomendamos seguir las mejores prácticas y siempre incluir descripciones al configurar reglas de validación, reglas de duplicados y elementos de flujo. Sin embargo, no estamos comprobando las descripciones a menos que se especifique en esta superbadge.

## Caso de Uso
Las empresas necesitan datos precisos para prosperar. En la era de la IA, eso es aún más cierto. La calidad de los datos juega un papel crucial en la formación de los resultados y la fiabilidad de los sistemas de IA porque las organizaciones dependen de los datos existentes para integrar agentes de IA e informar a la IA generativa. En esta superbadge, demuestras habilidades en la importación de datos, reglas de duplicados y validación, y mantenimiento de la integridad de los datos utilizando flujos.

Trabajando con el equipo de **Cloud Kicks**, has escuchado muchos juegos de palabras sobre zapatillas, pero mantener las cosas funcionando sin problemas como administrador de Salesforce es un trabajo que te tomas muy en serio. Cloud Kicks fabrica zapatillas personalizadas con estilo, y el negocio nunca se detiene. En serio. Toma la reciente adquisición del minorista de moda de moda, **Rambunctious Armadillo Socks (RAS)**. El equipo de RAS aporta mucha energía, ideas creativas y una gran cantidad de datos a la mezcla. Se necesitan tus habilidades de gestión de datos para conseguir que los dos sistemas CRM funcionen juntos como uno solo.

## Requisitos de Negocio
Has dado los pasos iniciales para integrar los datos de RAS y Cloud Kicks. Pero el negocio está experimentando problemas de calidad de datos en todo Salesforce, debido a formatos de entrada inconsistentes, registros duplicados y validación limitada. Esto afecta la precisión de los informes, la productividad del usuario y la experiencia del cliente.

Tu objetivo es implementar soluciones de calidad de datos escalables y automatizadas para el equipo de Cloud Kicks. En cada desafío, te centrarás en áreas específicas de datos, aplicarás tu experiencia e implementarás cambios para asegurar la calidad de los datos. Como mejor práctica, primero has verificado que ninguna actualización planificada activará ninguna automatización en la org, como flujos o triggers de Apex, que podrían causar efectos secundarios no deseados. Con eso confirmado, tienes vía libre para proceder con la mejora de los datos.

## Arreglar e Importar Datos (Fix and Import Data)
En tu primer desafío, ayuda a Cloud Kicks a limpiar algunos datos que fueron importados de RAS en el campo de texto `Lead Source Text`. Tu panel de **Data Quality Analysis** incluye muchos candidatos (Leads) sin una fuente de candidato. Usa el informe **Lead Data Quality** para revisar los leads afectados.

Los valores de texto abierto se han guardado en el campo `Lead Source Text` en los registros de Lead en la org de Cloud Kicks. Tu gerente de ventas, José Figueroa, proporcionó una tabla para el mapeo de la lista de selección (picklist). Parece que RAS usó un campo de texto abierto en el formulario de su sitio web, pero Cloud Kicks usa una lista de selección. José ha proporcionado el mapeo de valores de la lista de selección de `Lead Source` aquí.

| Lead Source Picklist Values | Lead Source Text Values |
| :--- | :--- |
| **Web** | Website |
| **Phone Inquiry** | Call |
| | Phone |
| **Partner Referral** | RAS Referral |
| **Purchased List** | Tradeshow Scan |
| **Other** | SocialMedia |

Utiliza este mapeo y el informe **Lead Data Quality** para importar el valor adecuado para el campo de lista de selección `Lead Source` en los leads de RAS.

¡Buen trabajo! Puedes abrir el panel **Data Quality Analysis** para examinar los cambios resultantes y admirar tu trabajo.

## Gestionar Duplicados y Refinar Reglas (Manage Duplicates and Refine Rules)
Con la reciente adquisición de RAS, Cloud Kicks trajo un gran volumen de nuevos datos de clientes. Desde la integración, ha habido un aumento notable en los registros de contactos duplicados dentro de Salesforce. Estos duplicados están causando ineficiencias importantes. El Gerente de Ventas José ha informado que los representantes de ventas están gastando tiempo extra revisando múltiples registros de contactos para encontrar el correcto. Aún más preocupante, ha habido algunos casos en los que diferentes representantes han contactado sin saberlo al mismo cliente sobre la misma oportunidad, creando confusión y arriesgando la confianza del cliente.

José te pide que tomes medidas inmediatas para controlar los duplicados y limpiar los registros de contactos. Sabes que hay una regla de duplicados llamada **Custom Contact Duplicate Rule** que ya está configurada en la org. Investiga por qué no se está activando y haz la actualización apropiada. Configura los ajustes para que bloquee a los usuarios de crear contactos duplicados. Asegúrate de que la alerta informe al usuario sobre un duplicado y le pida que use el registro de contacto existente en su lugar. Deja la casilla de verificación de informe habilitada para la edición.

Revisa la lógica utilizada para identificar duplicados en la **Custom Contact Matching Rule**. Estás satisfecho con la configuración para una coincidencia exacta tanto en el correo electrónico como en el apellido. Sin embargo, dado que los nombres válidos pueden variar bastante, decides agregar una regla de nombre para permitir coincidencias aproximadas (Fuzzy Match).

Finalmente, utiliza el informe **Duplicate Record Set Report** para encontrar y fusionar registros duplicados.

## Mejorar la Validación de Datos para Oportunidades (Enhance Data Validation for Opportunities)
A medida que Cloud Kicks madura su proceso de ventas, el departamento de Sales Ops se centra en ajustar la precisión de las previsiones y mejorar la integridad de los cronogramas de ventas. Te han alertado de que los representantes de ventas ocasionalmente cambian la etapa de la oportunidad en oportunidades cerradas, ya sea por error o en un intento de "revivir" tratos que ya estaban cerrados. Crea una regla de validación llamada `Opportunity_Closed_Stages`, y agrega una fórmula que impida cambiar el `Stage` cuando está establecido en **Closed Won** o **Closed Lost**. Asegúrate de que el usuario vea un mensaje de error relevante en la parte superior de la página explicando por qué no pueden cambiar la etapa de la oportunidad una vez que la etapa está establecida en Closed Won o Closed Lost.

Otra área a mejorar es asegurar que las Fechas de Cierre (`Close Dates`) en las oportunidades reflejen la actividad actual o futura, en lugar de establecerse en fechas pasadas. Para apoyar este objetivo, crea una regla de validación llamada `Opportunity_Closed_Backdate` que impida a los usuarios ingresar una `Close Date` anterior a hoy. Asegúrate de incluir un mensaje de error relevante en el campo que explique por qué no pueden guardar el registro. Para mantener la flexibilidad, asegúrate de que la regla de validación sea omitida (bypassed) si el usuario que la ejecuta tiene el permiso personalizado **Opportunity Manager** que ya existe en la org.

Finalmente, crea una regla de validación llamada `Opportunity_Amount_Owner_or_Admin` que asegure que el Monto de la oportunidad (`Amount`) no pueda ser cambiado por nadie excepto un administrador o el propietario del registro. Asegúrate de que el usuario vea un mensaje de error en el campo `Amount` especificando quién puede cambiar el monto.

## Hacer cumplir las Restricciones de Fecha de Vencimiento de Tareas con Flujos (Enforce Task Due Date Constraints with Flows)
La gente está rebosante de entusiasmo por el calzado elegante y cómodo de Cloud Kicks. Los aportes de vanguardia del equipo de RAS han energizado al grupo creativo con algunos diseños frescos e innovadores. Los representantes de ventas están ingresando más tratos que nunca en el pipeline. Ansiosos por mantenerse al día con los nuevos negocios, los equipos de procesamiento de pedidos y entregas están automatizando más tareas que nunca.

Desafortunadamente, los agentes de soporte a veces han creado tareas de seguimiento en casos de alta prioridad con una fecha de vencimiento posterior al acuerdo de nivel de servicio (SLA) del caso, lo que lleva a ineficiencias, errores y perspectivas defectuosas. Es hora de aplicar tus estándares de alta calidad para la gestión de datos para ayudar a estructurar los flujos de trabajo. Configura un flujo para mantener los casos en marcha y establecer reglas para las tareas de seguimiento oportunas. Asegúrate de que las tareas en casos de alta prioridad se creen con una fecha de vencimiento no mayor a 7 días.

Crea un nuevo flujo con la etiqueta `Task Due Date` y el API Name `Task_Due_Date`, que se ejecutará cuando se cree una nueva tarea. Utiliza el elemento **Get Records** etiquetado `Get High Priority Cases` con el API name `Get_High_Priority_Cases` para consultar los casos abiertos relacionados y comprobar si el campo del caso `Priority` = **High**. Crea un elemento de decisión etiquetado `Any High Priority Cases?` con el API name `Any_High_Priority_Cases`. Asegúrate de incluir un resultado (outcome) para si se encuentran casos de alta prioridad etiquetado `Yes - High Priority Found`. Deja el resultado predeterminado para cuando no haya casos de alta prioridad, asegurando que el flujo continúe a lo largo de la ruta de procesamiento estándar.

Introduce otra decisión para comprobar si la fecha de vencimiento de la tarea se extiende más de 7 días en el futuro. Si es así, impide que la tarea se guarde y emite un mensaje de error al usuario para que seleccione una fecha de vencimiento válida dentro del plazo permitido. Etiqueta este elemento de decisión `Is The ActivityDate Too Far Into The Future?` con el API name `Is_The_ActivityDate_Too_Far_Into_The_Future`. Comparará la fecha de la tarea contra una fórmula llamada `OneWeek` para determinar si la fecha de vencimiento de la tarea está establecida más de 7 días. Asegúrate de incluir un resultado para si la fecha está demasiado lejos en el futuro, etiquetado `Yes - Too Far Into The Future`. Deja el resultado predeterminado para cuando la fecha esté dentro del umbral de 7 días, asegurando que el flujo continúe a lo largo de la ruta de procesamiento estándar.

Finalmente, crea un mensaje de error personalizado para guiar a los usuarios cuando su tarea no pueda ser guardada, aclarar la razón y proporcionar instrucciones correctivas. Usa la etiqueta `Error - ActivityDate Should Be Sooner` y el API Name `Error_ActivityDate_Should_Be_Sooner`. Asegúrate de agregar una descripción, pero no comprobaremos su texto exacto. Incluye el siguiente mensaje de error: `High Priority cases need to be addressed quickly. Please set the due date no later than {!OneWeek}`. Muestra el mensaje de error como un error en línea en el campo `Due Date Only`.

Tu solución de flujo debe incorporar una lógica clara mientras previene conflictos de programación para tareas críticas. ¡Buen trabajo, Trailblazer!

## Resumen (Sum It Up)
Al completar esta superbadge, has demostrado tu competencia en la gestión de datos. Pudiste mejorar la calidad de los datos de los leads después de analizar un informe, mapear campos faltantes y corregir datos inexactos. Identificaste y resolviste contactos duplicados en la org de Cloud Kicks, y refinaste las reglas para mejorar la detección de duplicados y bloquear la creación de duplicados. Implementaste nuevas medidas de validación para asegurar los datos de oportunidades y campos de fecha precisos. Y en tu desafío final, incorporaste la automatización de flujos, campos de fórmula y filtros de búsqueda para asegurar la consistencia de los datos en casos de alta prioridad. ¡Felicitaciones por este logro de superbadge!

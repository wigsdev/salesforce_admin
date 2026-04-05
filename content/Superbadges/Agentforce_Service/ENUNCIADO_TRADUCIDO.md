# Superbadge: Servicio Agentforce

## Lo que tendrá que hacer para ganar esta Superbadge
* Configurar la Biblioteca de Datos de Agentforce.
* Configurar el Agente de Servicio.
* Construir y probar acciones de agente personalizadas.
* Añadir y configurar temas estándar y personalizados.
* Configurar flujos de enrutamiento y escalamiento.

## Conceptos puestos a prueba en esta Superbadge
* Configuración del Agente de Servicio
* Biblioteca de Datos de Agentforce
* Temas Personalizados y Estándar
* Acciones del Agente
* Enrutamiento de Conversaciones

### Actualización
Gracias por su paciencia mientras un problema del producto impactó temporalmente la finalización de esta superbadge. Nos alegra informar que el problema del recuperador de artículos de Knowledge ya ha sido resuelto.

Si tiene una organización existente que estaba bloqueada en el Desafío 3 debido a este problema, puede intentar eliminar la biblioteca de datos de Knowledge existente y luego volver a crearla con la misma etiqueta, esperando a que el Estado sea "En Progreso" (In Progress) o "Listo" (Ready) antes de construir el Desafío 3. Si aún experimenta errores, recomendamos comenzar de nuevo con una organización nueva desde la página de registro y usarla para completar los desafíos. (Tenga en cuenta que si ya ha pasado los Desafíos 1 y 2, solo necesitará reconstruir el Desafío 1 en su nueva organización antes de construir y pasar el Desafío 3, pero tenga en cuenta que esto podría afectar la funcionalidad de su agente). Pedimos disculpas por los inconvenientes.

## Introducción a las Superbadges
¡Atención! Una superbadge es diferente a otros aprendizajes en Trailhead. Es una evaluación de habilidades técnicas prácticas donde toma requisitos de negocio y aplica sus habilidades para construir algo increíble, sin la guía paso a paso. Hemos proporcionado aprendizaje recomendado y artículos de Ayuda llenos de recursos para ayudarle en su viaje. El tiempo estimado de finalización asume experiencia previa con los conceptos de la superbadge y la finalización del aprendizaje recomendado. ¡Su arduo trabajo valdrá la pena!

## Trabajo Previo y Notas
**Regístrese para una Organización Developer Edition con Configuración Especial**
Para completar esta superbadge, necesita una organización Developer Edition especial que contenga configuración y datos de muestra especiales. Tenga en cuenta que esta organización Developer Edition está diseñada para funcionar con los desafíos de esta superbadge.

1. Regístrese para obtener una organización Developer Edition gratuita de 4 días con configuración especial y Data 360.
2. Complete el formulario. Para la dirección de correo electrónico, ingrese una dirección activa donde pueda recibir el correo electrónico de confirmación de la nueva cuenta.
3. Después de llenar el formulario, haga clic en *Submit* (Enviar). Aparecerá un mensaje de confirmación.
4. Cuando reciba el correo electrónico de activación (esto podría tardar hasta una hora), ábralo y haga clic en el enlace para restablecer su contraseña.
5. Complete su registro configurando su contraseña y pregunta de seguridad. **Sugerencia:** Guarde su nombre de usuario, contraseña y URL de inicio de sesión en un lugar seguro —como un administrador de contraseñas— para acceder fácilmente más tarde.
6. Ha iniciado sesión en su organización Developer Edition de la superbadge.

Ahora, conecte su nueva organización Developer Edition a Trailhead.
1. Asegúrese de haber iniciado sesión en su cuenta de Trailhead.
2. En la sección Desafío al final de esta página, seleccione **Connect Org** (Conectar organización) en la lista desplegable.
3. En la pantalla de inicio de sesión, ingrese el nombre de usuario y la contraseña de la organización Developer Edition que acaba de configurar.
4. En la página *¿Permitir acceso?*, haga clic en **Allow** (Permitir).
5. En la página *¿Desea conectar esta organización para desafíos prácticos?*, haga clic en **¡Sí! Guárdalo.** Será redirigido de vuelta a la página del Desafío y estará listo para usar su nueva organización Developer Edition para ganar esta superbadge.

Ahora que tiene una organización de Salesforce con configuración especial para esta superbadge, está listo para continuar.

Esta superbadge requiere acceso a una organización Developer Edition especial que incluye Einstein Generative AI y Data 360. Estas organizaciones Developer Edition solo están disponibles por un período de 4 días, así que asegúrese de completar esta superbadge antes de que su organización expire.

**Nota**
Antes de comenzar los desafíos, revise la Ayuda del Desafío de la Superbadge de Servicio de Agentforce.

Asegúrese de estar usando una nueva organización Developer Edition de este enlace de registro para completar los desafíos en esta superbadge. Si usa una organización que ha sido utilizada para otro trabajo, no pasará los desafíos de esta superbadge.

## Caso de Uso
Coral Cloud Resorts, un destino de playa de lujo, es conocido por sus ofertas estacionales y su dedicación a brindar experiencias a los huéspedes de alta calidad y personalizadas. Típicamente, el resort tiene su temporada más ocupada en verano, con meses más tranquilos fuera de temporada. Sin embargo, este año, el resort se enfrenta a un desafío emocionante pero complejo: se llevará a cabo un festival de cine independiente en las cercanías durante la temporada baja. Se espera que este evento atraiga a un gran volumen de huéspedes nuevos y recurrentes.

Sumado a la emoción, Coral Cloud Resorts acogerá varios eventos exclusivos de encuentro (*meet-and-greet*) del festival en el lugar. Estas actividades de alto perfil, combinadas con la mayor demanda de los huéspedes, crean presiones operativas únicas para el resort.

Para satisfacer estas demandas, Coral Cloud Resorts está expandiendo sus horas de servicio, ofreciendo actividades exclusivas relacionadas con el festival de cine, y lanzando nuevas opciones de eventos, todo mientras mantiene altos estándares de servicio a los huéspedes. Para lograr esto sin aumentar significativamente la cantidad de personal, el resort está recurriendo a soluciones de servicio al cliente impulsadas por inteligencia artificial (IA) y automatización.

## Requisitos del Negocio
El Agente de Experiencia de Coral Cloud (*Coral Cloud Experience Agent*) actúa como un conserje virtual, manejando las consultas de los huéspedes y ayudando con reservas, recomendaciones del festival y otros servicios. Su tarea es configurar y optimizar el agente para cumplir con las siguientes necesidades comerciales.

1. **Configurar el agente de experiencia de Coral Cloud:** Configure el agente para brindar respuestas personalizadas y precisas utilizando fuentes de datos confiables como la Biblioteca de Datos de Agentforce y artículos de Knowledge.
2. **Administrar reservas eficientemente:** Equipe al agente con acciones para modificar las reservas de los huéspedes, como agregar o cancelar reservas, y proporcione información de reserva en tiempo real.
3. **Expandir el servicio con temas estándar y personalizados:** Use temas estándar como General FAQs para manejar preguntas comunes y cree temas personalizados para resaltar las ofertas relacionadas con el festival.
4. **Manejar consultas complejas con escalamientos:** Configure flujos de enrutamiento para transferir consultas de huéspedes complejas o no resueltas a representantes de servicio para obtener más asistencia.

Con su experiencia en configuración, el Agente de Experiencia de Coral Cloud puede ayudar al resort a mantener un servicio excepcional para los huéspedes durante la ajetreada temporada de festivales al tiempo que optimiza las cargas de trabajo del personal.

---

## Configurar el Agente y la Biblioteca de Datos de Agentforce
Configure el agente y establezca las bibliotecas de datos para ofrecer respuestas precisas y consistentes. La organización ya tiene un Agente de Servicio de Agentforce llamado *Coral Cloud Experience Agent*.

* Active Einstein y Agentforce si aún no están habilitados.

**Definir el Rol y el Contexto del Agente**
| Campo | Valor |
| --- | --- |
| **Description** | `This is Coral Cloud Resorts' AI agent, designed to help customers discover resort experiences and book sessions seamlessly, particularly during the film festival.` |
| **Role** | `You're an AI concierge at Coral Cloud Resorts. Your role is to assist customers with booking and managing services during the film festival by providing accurate information and resolving inquiries swiftly.` |
| **Company** | `Coral Cloud Resorts offers destination experiences that blend unique, premium activities with unmatched customer care. Our discerning customers value effortless, quality reservation services, where every interaction enhances their journey.` |

**Integrar Artículos de Knowledge en Agentforce Builder**
Para integrar artículos de Knowledge en Agentforce Builder y asegurar que el agente esté fundamentado en información relevante, comience gestionando las fuentes de datos para proporcionar acceso a estos artículos. Cree una biblioteca de datos llamada `Coral Cloud Experience Agent Library`, incluyendo los campos identificativos `Title` y `Summary` y los campos de contenido `Answer` y `Question`. Aunque no evaluaremos esta configuración como parte del desafío, es esencial para fundamentar al agente en el conocimiento preciso de los artículos relevantes.

**Integrar el Archivo de Código de Conducta y Acuerdo de Usuario**
Ahora, cree una nueva biblioteca de datos con el nombre `Code of Conduct Agreement` y nombre de API `Code_of_Conduct_Agreement` y cargue el Código de Conducta y Acuerdo de Usuario del resort. *Consejo: No cambie el nombre del archivo; debe llamarse `CC_User_Agreement.pdf`*. Este recurso fundamenta las respuestas del agente en datos confiables y conformes.

*Nota:* Dado que una biblioteca de datos solo puede tener un tipo de datos, necesita dos bibliotecas de datos: una para artículos de Knowledge y otra para cargar el archivo.

Asegúrese de que el rol, la descripción y el contexto de la empresa del agente reflejen la misión y los servicios de Coral Cloud Resorts. Confirme que el *Coral Cloud Experience Agent* está vinculado a la biblioteca de datos de Knowledge. Confirme que el Código de Conducta se cargó en la biblioteca de datos. Usamos estas dos fuentes de datos en el desafío 3.

---

## Crear el Tema de Gestión de Reservas (Booking Management Topic)
El Agente de Experiencia de Coral Cloud debe administrar de manera eficiente todas las interacciones relacionadas con las reservas. Para lograr esto, configure el Tema de Gestión de Reservas de la siguiente manera.

**Tema de Gestión de Reservas y Acciones de Agente**
Incluya una descripción clara, un alcance definido e instrucciones específicas para manejar las reservas de los huéspedes. Asegúrese de que el tema esté alineado con el compromiso del resort con un servicio fluido para los huéspedes.

| Campo | Valor |
| --- | --- |
| **Topic Label** | `Booking Management` |
| **Classification Description** | `This topic handles customer inquiries about booking experiences at Coral Cloud Resorts. It includes making new reservations, modifying existing bookings, and addressing questions about experience details to ensure a smooth and satisfying customer journey.` |
| **Scope** | `Your job is to assist customers with managing their bookings for Coral Cloud Resorts experiences. This includes providing accurate information, resolving booking-related issues, and ensuring every interaction is seamless and stress-free.` |
| **1st Instruction** | `Always request the Booking Record Number, which begins with 'B-', before accessing booking details. Use the 'Get Booking' action to retrieve and share the relevant information with the customer.` |
| **2nd Instruction** | `Prompt the user to specify the action they’d like to take on their booking. Available options include adding and removing guests or canceling the booking.` |
| **3rd Instruction** | `For booking cancellations, confirm the action with the user by displaying the Experience Name. Then call the 'Cancel Booking' action.` |
| **4th Instruction** | `To add guests to a confirmed booking, ask the user for the total number of guests, including the contact, who plan to attend the session. Use the previously provided Booking Record Number (starting with 'B-') to call the 'Adjust Booking' action.` |

Ahora que tiene las instrucciones establecidas, agregará acciones para admitir modificaciones de reserva utilizando el flujo `Adjust Booking`, cancelaciones utilizando el flujo `Cancel Booking` y recuperación de información utilizando el flujo `Get Booking`. Asegúrese de que las acciones soliciten las entradas requeridas, como el Número de Registro de Reserva, y muestren las salidas (outputs) correctamente.

*Consejo: Eche un vistazo a los registros de reserva en la aplicación Coral Cloud Resorts antes de escribir instrucciones de acciones del agente.*

El agente debe recuperar y compartir información de reserva relevante con el cliente. Revise la segunda instrucción, que implica pedir al usuario que especifique la acción que le gustaría tomar, como agregar huéspedes o cancelar una reserva. Cree las siguientes acciones en Agentforce Builder y agréguelas al tema de Gestión de Reservas.
- Get Booking
- Adjust Booking
- Cancel Booking

Configure la acción `Cancel Booking` para que el agente confirme con el usuario antes de cancelar la reserva. Agregue instrucciones adicionales al tema de Gestión de Reservas para llamar a las acciones de agente anteriores.

*Nota:* No estamos comprobando el texto de carga de espera y las configuraciones de entrada/salida de las acciones del agente más allá de lo descrito anteriormente.

Asegúrese de que el tema de Gestión de Reservas (*Booking Management*) incluya la descripción de clasificación correcta, el alcance y las instrucciones según lo especificado, y las acciones de agente requeridas asociadas. Pruebe el agente con escenarios de reserva para garantizar que solicite, procese y muestre correctamente las acciones y detalles de la reserva.

**Nota**
Cuando se implementan cambios en los registros a través de IA, la mejor práctica es incluir medidas de seguridad como la verificación de identidad del usuario. Este paso no es obligatorio para este desafío, pero se alienta para escenarios del mundo real. Consulte la documentación *Maintain Trust with Agentforce Actions* para obtener más información.

---

## Añadir Temas Estándar: Preguntas Frecuentes (General FAQ) y Escalación (Escalation)
Coral Cloud Resorts necesita que su conserje virtual ofrezca información precisa sobre los detalles del evento, políticas y otras consultas. Su tarea es garantizar que el agente utilice fuentes de datos confiables, como artículos de Knowledge y el PDF del Código de Conducta, para obtener respuestas precisas. Además, se asegurará de que el agente pueda escalar consultas complejas a un representante de servicio cuando sea necesario. En este desafío, configurará temas estándar e integrará recuperadores de bibliotecas de datos para fuentes de datos confiables.

Para completar este desafío, configure el *Coral Cloud Experience Agent* para satisfacer las siguientes necesidades.

1. **Añadir el tema estándar de Preguntas Frecuentes (General FAQ Topic) y personalizarlo:** Use una acción de agente para invocar la plantilla de solicitud (prompt template) `Film_Festival_Related_Answers`. La plantilla de solicitud genera una respuesta a la pregunta del usuario basada en la información relevante de los artículos de Knowledge y el archivo del Código de Conducta.
2. **Añadir el Tema de Escalación (Escalation Topic):** Permita al agente transferir las consultas no resueltas a un representante de servicio.

Revise la solicitud (prompt) en la plantilla `Film_Festival_Related_Answers` y agregue la etiqueta del usuario `Input: Question` en el texto del marcador de posición: `[Input the customer's question]`.

Agregue los Retrievers (que tendrán nombres similares a `File_Code_of_Conduct...` y `KA_Coral_Cloud_Experience...`) en el texto de los marcadores de posición indicados con corchetes. Además, configure el Texto de Búsqueda (*Search Text*) para ambos recuperadores con la entrada de usuario, `Input: Question`. Guarde, pruebe y active la plantilla de solicitud.

*Consejo: Si no puede obtener la respuesta esperada desde la plantilla de solicitud, asegúrese de haber reconstruido el índice de búsqueda para los artículos de Knowledge. Consulte el artículo de Ayuda para conocer los pasos detallados sobre cómo reconstruir el índice de búsqueda.*

Establezca las recomendaciones (*guardrails*) para obtener respuestas a partir de la respuesta de la plantilla de prompt `Film_Festival_Related_Answers`. Cree una nueva acción para invocar la plantilla de mensaje. Asocie esta nueva acción al tema *General FAQ*. Asegúrese de que haya solo un tema *General FAQ* y de que esté personalizado con la nueva acción.

Confirme que el tema *General FAQ* implemente una anulación (*override*) para llamar a la nueva acción. Asegúrese de que recupere resultados desde los artículos de Knowledge y del Código de Conducta. Verifique que las respuestas tengan un formato adecuado para los chats del cliente. Asegúrese de que la acción asociada esté configurada correctamente.

Por último, verifique que el agente esté configurado para escalar las conversaciones a un representante en vivo.

---

## Implementar el Agente y Transferir Conversaciones
Coral Cloud Resorts desea agregar el canal de servicio de Mensajería a su sitio de Experience Cloud para que los huéspedes puedan interactuar con el *Coral Cloud Experience Agent*. Para garantizar una experiencia de huésped excepcional, el resort necesita que configure el agente en el sitio `coral-cloud`. La configuración debe permitir que el huésped interactúe con el agente en el sitio de Experience Cloud. Esto incluye asegurar que estén configurados los flujos necesarios, publicar las actualizaciones y habilitar los componentes requeridos.

Confirme que el agente esté activado y actualizado con las configuraciones más recientes. Para transferir la conversación desde los huéspedes en el sitio hacia el *Coral Cloud Experience Agent*, el resort requiere que configure el flujo omnicanal entrante: `Route to ESA`. Guarde y active el flujo actualizado.

En situaciones donde los huéspedes requieran asistencia de un representante de servicio, la organización está equipada con el flujo omnicanal saliente: `ESA - Route to Queue`. El *Coral Cloud Experience Agent* utiliza este flujo para enrutar los escalamientos hacia una cola de Mensajería. Opcionalmente incluya un mensaje para informar a los huéspedes sobre la transferencia de la conversación a un representante de servicio.

*Nota:* Antes de agregar el componente de la ventana de chat (*Embedded Messaging*) al sitio Experience Cloud de coral-cloud, asegúrese de publicar el sitio y la implementación web `ESA Web Deployment`. No verificamos esto en el desafío, pero es crítico completar estos pasos antes de probar el agente en el sitio.

---

## Resumen de los Desafíos
1. **Set Up the Agent and Einstein Data Library**
Configure el Agente de Experiencia Coral Cloud y cree Bibliotecas de Datos de Agentforce como fuentes de datos para el agente.
2. **Create the Booking Management Topic**
Configure un tema personalizado para administrar las reservas iniciando los flujos: Get Booking, Adjust Booking y Cancel Booking.
3. **Add Standard Topics**
Modifique el prompt proporcionado con los recuperadores de la fuente de datos. Reemplace (override) el tema de Preguntas Frecuentes (General FAQ) con una acción personalizada a la plantilla del prompt. Configure el agente para escalar las conversaciones a un representante de servicio.
4. **Deploy Agent and Transfer Conversations**
Ajuste el flujo Route to ESA para desplegar de manera exitosa el Coral Cloud Experience Agent en el sitio de Experience Cloud.

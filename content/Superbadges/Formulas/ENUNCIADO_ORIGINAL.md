# Superbadge: Fórmulas - Enunciado Original

**Traducción literal del enunciado oficial de Trailhead**

---

## Lo que tendrá que hacer para ganar esta Superbadge

- Construir campos de fórmula dinámicos para cumplir requerimientos de negocio.
- Configurar fórmulas para uso dentro de un reporte.
- Describir mejores prácticas de fórmulas.

## Conceptos probados en esta Superbadge

- Fórmulas

## Preparación y Notas

### Registrarse en una Developer Edition Org con Configuración Especial

Para completar este superbadge, necesitas una Developer Edition org especial que contiene configuración especial y datos de muestra. Nota que esta Developer Edition org está diseñada para trabajar con los desafíos en este superbadge.

Regístrate para una Developer Edition org gratuita con configuración especial.

Llena el formulario. Para dirección de Email, ingresa una dirección de email activa.

Después de llenar el formulario, haz clic en Sign me up.

Cuando recibas el email de activación (esto puede tomar algunos minutos), ábrelo y haz clic en Verify Account.

Completa tu registro estableciendo tu contraseña y pregunta de desafío. Consejo: Guarda tu nombre de usuario, contraseña y URL de inicio de sesión en un lugar seguro—como un administrador de contraseñas—para acceso fácil después.

Has iniciado sesión en tu superbadge Developer Edition org.

Ahora, conecta tu nueva Developer Edition org a Trailhead.

Asegúrate de estar conectado a tu cuenta de Trailhead.

En la sección Challenge en la parte inferior de esta página, selecciona Connect Org de la lista de selección.

En la pantalla de inicio de sesión, ingresa el nombre de usuario y contraseña para la Developer Edition org que acabas de configurar.

En la página Allow Access?, haz clic en Allow.

En la página Want to connect this org for hands-on challenges?, haz clic en Yes! Save it. Eres redirigido de vuelta a la página Challenge y listo para usar tu nueva Developer Edition org para ganar este superbadge.

Ahora que tienes una org de Salesforce con configuración especial para este superbadge, estás listo para comenzar.

### Nota

Antes de comenzar los desafíos, por favor revisa Data Model Optimization Superbadges: Trailhead Challenge Help.

Asegúrate de estar usando una nueva Developer Edition org de este enlace de registro para completar los desafíos en este superbadge. Si usas una org que ha sido usada para otro trabajo, no pasarás los desafíos en este superbadge.

Donde sea posible, cambiamos términos no inclusivos para alinearnos con nuestro valor de compañía de Igualdad. Mantuvimos ciertos términos para evitar cualquier efecto en implementaciones de clientes.

### Consejos

- Toma un bolígrafo y papel. Puede que quieras anotar notas mientras lees los requerimientos.
- Parte de la terminología usada en este superbadge es descriptiva y puede no coincidir con el nombre como aparece en la interfaz de usuario (UI). Esto es para probar tu conocimiento de características de Salesforce y habilidad para seleccionar la característica correcta para satisfacer una necesidad de negocio.
- Field-Level Security for Permission Sets during Field Creation ha sido habilitado en la Developer Edition org especial de Salesforce para este superbadge.
- Donde sea posible, las fórmulas serán evaluadas basándose en el resultado esperado en lugar de sintaxis de fórmula específica. Recomendamos usar datos de muestra para probar y validar tus fórmulas.
- Aunque es requerido poblar texto de ayuda para completar muchos de los desafíos en este superbadge, texto de ayuda excesivo puede afectar negativamente la experiencia del usuario, especialmente para usuarios de lectores de pantalla y personas con trastornos de atención. En el mundo real, los admins etiquetan campos claramente y sucintamente y usan texto de ayuda solo cuando el usuario necesita más información sobre los datos alojados allí.

---

## Caso de Uso

Rambunctious Armadillo Socks (RAS) es un gran minorista con procesos complejos de ventas y servicio. La organización tiene un gran volumen de leads y casos en su base de datos de Salesforce y está buscando formas de obtener más de los datos.

Como un admin de Salesforce en RAS, te han pedido usar funcionalidad out-of-the-box para aumentar precisión y eficiencia, mejorar visibilidad, y mejorar toma de decisiones para usuarios para enfocar los recursos de la compañía en los lugares correctos.

---

## Requerimientos de Negocio

Esta sección representa los requerimientos que has reunido para construir la nueva funcionalidad en tu org de Salesforce. Tu solución debe adherirse a mejores prácticas como definidas por el RAS Salesforce Center of Excellence (CoE).

- Los nuevos campos de fórmula deben contener tanto una descripción como texto de ayuda para describir los datos contenidos en el campo.
- Todos los datos almacenados en Salesforce deben seguir el principio de menor privilegio: Los usuarios deben tener el nivel mínimo de acceso requerido para hacer sus trabajos.

> [!NOTE]
> **Interpretación**: El CoE requiere que todos los campos de fórmula tengan Description y Help Text, y que uses Permission Sets para controlar visibilidad de campos (menor privilegio). Además, todas las imágenes deben tener texto alternativo para accesibilidad.

Ahora, ¡manos a la obra!

---

## Puntuar y Calificar Leads para Aumentar Productividad de Ventas

Después de una campaña de marketing tremendamente exitosa, RAS ha visto leads entrantes aumentar diez veces en el último trimestre. Mientras el equipo de marketing está complacido con los frutos de su labor, el proceso actual usado para calificar leads ha sido lento con tal gran cantidad de prospectos, y el equipo de ventas está ansioso por ver nuevas oportunidades en su pipeline. Si solo hubiera una forma de puntuar automáticamente leads entrantes y reducir el tiempo necesario para calificar un lead...

Afortunadamente, RAS tiene un as de lógica de negocio bajo la manga (¡te estamos mirando a ti, Trailblazer!). Este no es tu primer rodeo. Estás bien versado en el lenguaje de la lógica y sabes que puedes usar el poder de las fórmulas para puntuar leads basándose en un conjunto de parámetros.

Primero, te reúnes con el equipo de liderazgo de ventas para aprender sobre su proceso actual de calificación de leads. Después de recopilación y análisis exhaustivos de requerimientos, el equipo del proyecto ha identificado los siguientes factores y puntuaciones relativas que deben ser incluidos en el nuevo campo Lead Score.

| Campo Lead | Criterio | Puntuación | Más Información |
|------------|----------|------------|-----------------|
| Lead Status | EQUALS 'Closed - Not Converted' | 0 | La puntuación del lead siempre debe igualar 0 (cero) para este Lead Status. Ningún otro criterio debe ser evaluado o incluido en la puntuación. |
| Do Not Call | EQUALS TRUE | −25 | Si Do Not Call no está marcado (FALSE), la fórmula debe asignar 0 (cero) para este criterio. |
| Email | Poblado | +15 | Si el campo email está en blanco, la puntuación es 0 (cero) para este criterio. |
| Lead Source | EQUALS 'Web' | +20 | Todas las otras fuentes de lead, actuales y futuras, deben resultar en un 0 (cero) para este conjunto de criterios. |
| | EQUALS 'Phone Inquiry' | +35 | |
| | EQUALS 'Partner Referral' | +25 | |
| | EQUALS 'Purchased List' | +10 | |

Crea un nuevo campo con la etiqueta Lead Score y nombre Lead_Score que suma los valores delineados arriba y muestra la puntuación de cada registro como un entero. Solo usuarios con el permission set Sales Representative existente deben poder ver el nuevo campo.

> [!NOTE]
> **Interpretación**: Crear campo de fórmula numérica (Number, 0 decimales) en objeto Lead. Usar IF y CASE para calcular puntuación. Configurar Field-Level Security para Permission Set "Sales Representative".

### Lead Rating

¡El nuevo campo Lead Score es un éxito! Los representantes de ventas aman poder calificar rápidamente leads entrantes basándose en una variedad de factores importantes. Pero un nuevo desafío ha emergido: Los representantes de ventas no pueden ponerse de acuerdo en qué cuenta como una puntuación de lead "buena".

Después de una verificación rápida con el equipo de liderazgo de ventas, has acordado construir un segundo campo que muestra una calificación visual basada en el Lead Score del registro. Este campo usará el sistema de calificación de estrellas para proporcionar una forma aún más rápida de calificar leads antes de convertir a oportunidades.

Usa los rangos de puntuación abajo para construir el segundo campo con la etiqueta Lead Rating y nombre Lead_Rating. Similar al campo Lead Score, este campo solo debe ser visible para usuarios con el permission set Sales Representative. La accesibilidad para usuarios de lectores de pantalla es un requerimiento en RAS. Tu solución debe incluir texto alternativo para cada imagen mostrada.

| Rango de Lead Score | Texto Alternativo | URL de Imagen* |
|---------------------|-------------------|----------------|
| < 10 | 0 Star | /img/samples/stars_000.gif |
| 10 - 19 | 1 Star | /img/samples/stars_100.gif |
| 20 - 29 | 2 Star | /img/samples/stars_200.gif |
| 30 - 39 | 3 Star | /img/samples/stars_300.gif |
| 40 - 49 | 4 Star | /img/samples/stars_400.gif |
| ≥ 50 | 5 Star | /img/samples/stars_500.gif |

*Las URLs de imagen proporcionadas se relacionan con imágenes de muestra que están disponibles para uso en cada org de Salesforce.

> [!NOTE]
> **Interpretación**: Crear campo de fórmula de texto en objeto Lead. Usar función IMAGE() con CASE anidado para mostrar estrellas según Lead Score. El segundo parámetro de IMAGE() es el texto alternativo (accesibilidad).

---

## Aumentar Visibilidad y Mejorar Toma de Decisiones para Equipos de Servicio

Ahora que has trabajado tu magia de lógica para los equipos de ventas y marketing, el equipo de servicio quiere entrar en acción.

Los agentes de servicio en RAS gestionan un gran volumen de casos y se enorgullecen de su servicio al cliente galardonado. Los agentes revisan regularmente registros de activos de clientes para ver qué productos han sido comprados además de otra información importante para informar la forma en que gestionan el caso. El equipo de liderazgo de servicio quisiera que los agentes de servicio puedan ver el monto de oportunidad asociado con cada registro de activo. El monto de oportunidad es importante para propósitos de toma de decisiones y acuerdos de nivel de servicio.

Construye una solución que permita a usuarios con el permission set Service Agent existente ver el monto del registro de oportunidad relacionado sin otorgar acceso al objeto Opportunity. Etiqueta tu solución Opportunity Value con el nombre Opportunity_Value y agrégala al page layout de activo. El valor mostrado debe coincidir con el monto en el registro de oportunidad relacionado exactamente.

> [!NOTE]
> **Interpretación**: Crear campo de fórmula Currency en objeto Asset. Usar cross-object formula (Opportunity.Amount) para mostrar el monto sin dar acceso al objeto Opportunity. Agregar al Asset Page Layout.

A continuación, el equipo de liderazgo indicó que la severidad del caso es un nuevo indicador clave de rendimiento (KPI) que el equipo revisará a menudo. El equipo acordó que el KPI de severidad del caso necesitará ser mostrado en múltiples reportes y dashboards y necesitará ser usado en una variedad de cálculos.

El picklist Severity existente contiene valores 0 - 5, donde 0 es el más severo y 5 es el menos severo. Este campo no ha sido requerido en el pasado así que registros más antiguos pueden tener un valor en blanco. Basándose en este picklist, construye una solución reutilizable para cumplir este requerimiento. Solo usuarios con el permission set Service Agent deben poder ver la solución y debe ser etiquetada Severity (Number) con el nombre resultante de Severity_Number. Para probar tu solución, modifica el reporte Case Severity by Month Last Year existente para mostrar la severidad promedio. Tu solución debe usar la herramienta de reporte más simple y eficiente para calcular la severidad promedio.

> [!NOTE]
> **Interpretación**: Crear campo de fórmula Number en objeto Case que convierta el picklist Severity a número. Usar VALUE(TEXT(Severity)). Modificar reporte para agregar columna Severity (Number) con función Average.

### Reporte de Casos

Ahora echemos un vistazo a algunas necesidades de reporte adicionales identificadas por el equipo de liderazgo de servicio.

También te han pedido ayudar al equipo a estructurar el reporte Case Severity by Month Last Year para que el promedio para cada cuenta sea agrupado basándose en cuándo el caso fue cerrado. El equipo necesita este reporte único para propósitos de cumplimiento y necesitará exportarlo y ordenar los datos basándose en el mes de cierre en un archivo de valores separados por comas (CSV).

Crea una solución con el título Close Month que agrupará casos basándose en el mes en que el caso fue cerrado. Después de hablar con stakeholders, has confirmado que no hay necesidad de negocio para que cada registro de caso individual muestre el mes de cierre y la solución solo es necesaria para este reporte. Abajo hay una maqueta de cómo el equipo quisiera que el reporte esté estructurado. Tu reporte debe incluir todos los 12 meses del calendario en inglés.

| Close Month | Account Name* | Average Severity (Number) |
|-------------|---------------|---------------------------|
| 01 - January | GenePoint | 1 |
| | Grand Hotels | 5 |
| | Express | 3 |
| 02 - February | Grand Hotels | 2 |
| | United | 4 |

*Los nombres de cuenta son solo para propósitos de ejemplo. Las cuentas mostradas en el reporte real pueden diferir.

> [!NOTE]
> **Interpretación**: Crear Row-Level Formula en el reporte (no en el objeto Case). Formato: "01 - January", "02 - February", etc. Usar TEXT(MONTH(ClosedDate)) concatenado con CASE para nombres de meses en inglés.

### Nota

No necesitas crear ningún reporte nuevo para resolver este desafío. Usa el reporte existente como se instruyó. Si necesitas una nueva copia, asegúrate de que el nuevo reporte tenga el mismo título y que elimines o renombres el reporte anterior antes de verificar el desafío.

---

**Grupo**: 3 - VISIONARY ADMINS  
**Fecha**: 17 Enero 2026

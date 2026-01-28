# Superbadge: Object Relationships - Enunciado Original

**Traducción literal del enunciado oficial de Trailhead**

---

## Lo que tendrá que hacer para ganar esta Superbadge

- Determinar el modelo de datos apropiado para objetos estándar y personalizados.
- Configurar relaciones de objetos con objetos estándar y personalizados.
- Explicar relaciones únicas de objetos estándar.
- Construir una app en App Builder.

## Conceptos probados en esta Superbadge

- Optimización del Modelo de Datos
- Relaciones de objetos
- Schema
- App Builder

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

- Toma un bolígrafo y papel. Puede que quieras anotar notas y mapear el modelo de datos mientras lees los requerimientos.
- Ingresa todas las etiquetas exactamente como se describe en las instrucciones. Las etiquetas son sensibles a mayúsculas y la ortografía cuenta.
- Cuando sea posible, copia y pega los nombres de etiquetas de las instrucciones del superbadge en lugar de escribirlos.
- Asegúrate de guardar tu trabajo antes de ejecutar la verificación del desafío.
- Construye tu solución de acuerdo con los requerimientos; agregar más configuraciones puede causar que las verificaciones de desafío fallen.
- Recomendamos seguir mejores prácticas y siempre incluir descripciones para configuraciones. Sin embargo, no estamos verificando descripciones en este superbadge.

---

## Caso de Uso

Art Tenor ha gestionado algunas de las bandas más exitosas en los últimos 25 años, incluyendo Run SFMC, the Feed Fighters, y Metadatallica. Su banda más reciente, Flow & the Low Codes, lanzó su primer álbum, "A Momentary Lapse of Memory" hace cuatro meses. El álbum y su canción hit "No More Mr. Wi-Fi" ha subido al número uno en las listas de rock alternativo, y el equipo en Tenor Management está armando la primera gira mundial de la banda.

Como el admin de Salesforce para Tenor Management, eres responsable de cargar y rastrear todas las canciones de la banda, información de álbumes, datos de giras, y más, en una sola app World Tour Manager que estarás creando. Prepárate porque se te pedirá hacer cambios regulares, actualizaciones, y reportes para el equipo de gestión, la banda, y otras partes según se solicite.

## Objetos Estándar

La app World Tour Manager usará estos objetos estándar.

- **Account**: Venues para shows, proveedores, servicios de streaming, estudios, y fans.
- **Contact**: Fans, personal de venues, agentes, productor, o manager.
- **Campaign**: Tours (o grupos de presentaciones) por una banda particular o una combinación de bandas (como un festival de música). Ejemplos: World Tour, Errors Tour, y el Trailblazer Tour.
- **Campaign member**: Estos son registros de contacto relacionados a una campaña.

## Objetos Personalizados

Como el admin de Salesforce, eres responsable de mantener los objetos personalizados que interactúan con objetos estándar para mantener registro de todos los elementos que entran en una gira. Estos objetos personalizados representan detalles como nuevas canciones, listas de canciones, e incluso artistas invitados que pueden ser actualizados y compartidos con stakeholders. Los objetos personalizados incluyen:

- **Song**: Incluye campos como Written by, Duration, Album, y así sucesivamente.
- **Album**: Una colección de canciones lanzadas juntas con información de banda y producción, arte, y pistas bonus.
- **Track list**: Una lista de canciones para un show en vivo.
- **Artist**: Estos son los cantantes, escritores, y performers involucrados con las canciones, álbumes, e incluso tours si es un artista invitado actuando con la banda en una noche particular.
- **Performs On**: Este objeto se usa para conectar Artists a Songs, en el futuro Art quiere poder conectar Artists a Albums también, sin embargo, eso está fuera de alcance por ahora.

## Diagrama de Relaciones de Entidades (ERD)

Revisa el modelo actual en Schema Builder y el diagrama abajo para entender cómo la banda está usando objetos estándar y personalizados.

El diagrama de relaciones de entidades muestra las siguientes relaciones:
- El objeto Account tiene una relación master-detail del objeto Contact.
- El objeto Play Tracker tiene lookups requeridos con los objetos Account y Song.
- El objeto Campaign tiene una relación many-to-many con los objetos Campaign y Contact a través del objeto Campaign Member.
- Los objetos Campaign y Song tienen una relación many-to-many con el objeto Track List.
- Los objetos Song y Artist tienen relaciones many-to-many con el objeto Performs On.
- El objeto Account tiene una relación lookup del objeto Campaign.
- El objeto Account tiene una relación lookup del objeto Contact.
- El objeto Album tiene una relación lookup al objeto Song.

---

## Requerimientos de Negocio

Como la compañía de gestión líder en la industria musical, Tenor Management necesita una org de Salesforce altamente eficiente y organizada para mantener registro de todos sus artistas, álbumes, canciones, tours, mercancía, sesiones de grabación, y proveedores de terceros. Todos asociados con la banda y sus actividades dependen de esta información.

### Configurar Objetos Estándar

Un mes en su gira, Flow & the Low Codes están agotando shows a través del país. Art Tenor te llama para tocar base sobre cómo medir las necesidades del equipo de seguridad en los próximos venues de shows. Art pide ver Capacity y Security Provided solo cuando el tipo de cuenta es Concert Venue.

> [!NOTE]
> **Interpretación**: Usar Dynamic Forms en Lightning Record Page para Account. Configurar visibilidad condicional de campos Capacity y Security Provided basándose en Type = "Concert Venue".

Adicionalmente, Art pide que Security Percent solo se muestre cuando Security Provided esté marcado. Menciona que está teniendo problemas sabiendo qué tours, shows, venues, entrevistas, y otras obligaciones de estrella de rock están relacionadas juntas. Necesitarás crear una relación entre Venues (Account) y los Tours (Campaign). Envía un texto con una lista de los tipos de tours y qué campos quiere ver en la página.

> [!NOTE]
> **Interpretación**: Configurar visibilidad de Security Percent solo cuando Security Provided = True. Crear campo Lookup Relationship en Campaign que apunte a Account.

#### Tipos de Tours

- Tour
- Show
- Digital Show
- Interview
- Venue
- Other

#### Campos de Tour a Mostrar en la Página

- Campaign Owner
- Parent Campaign
- Campaign Name
- Active
- Account
- Type
- Status
- Start Date
- End Date
- Contacts in Campaign
- Responses in Campaign

#### Agregar Registros de Tour

Ahora que has agregado los tipos de tours e hiciste la página personalizada a los deseos de Art, agrega la lista actual de tours que Art envió para que Art pueda revisar. No necesitas hacer activo o agregar fechas, Art hará eso después.

| Tour (Campaign) Name | Type | Parent Tour (Parent Campaign) | Status |
|----------------------|------|-------------------------------|--------|
| Errors Tour | Tour | | Planned |
| Camp Success | Interview | Errors Tour | Planned |
| Demo Jam | Digital Show | Camp Success | Planned |
| The Trailblazer Tour | Tour | | Planned |

### Construir Relaciones de Objetos

La cantante principal Appy le dice a Art Tenor que quiere agregar una Track List de canciones a cada tour. Appy quiere todas las canciones que la banda toca en cada tour. Las relaciones correctas entre objetos aseguran que Flow & the Low Codes puede rastrear qué canciones han tocado en qué tours. Revisa el schema para establecer relaciones para un objeto Track List a objetos Tour (Campaign) y Song. Una relación many-to-many entre Tour (Campaign) y Song conectará los objetos y construirá una lista para la banda.

> [!NOTE]
> **Interpretación**: Crear objeto personalizado Track List como Junction Object con dos relaciones Master-Detail: una a Campaign y otra a Song. Esto crea la relación many-to-many.

Durante la fiesta de lanzamiento de la banda para su nuevo single, el guitarrista Cody Shredder se encontró con la superestrella pop Lady Java y le pidió que se uniera a la banda en el escenario como artista invitada durante su show en el Sandbox Arena en Seattle. Lady Java acepta unirse a Cody en su nuevo single "No More Mr. Wi-Fi" como un remix Song en A Momentary Lapse of Memory Album. Tocarán dos de las canciones hit de Lady Java, Poker Interface y 404 (Error Code). Actualiza el modelo de datos para permitir conectar Song a hasta un Album a la vez.

> [!NOTE]
> **Interpretación**: Crear campo Lookup Relationship en objeto Song que apunte a Album. Usar Lookup (no Master-Detail) porque una canción puede existir sin álbum.

### Crear la App World Tour Manager

Flow & the Low Codes acaba de completar su gira, agotando cada uno de sus shows de costa a costa. Con el resto del mundo clamando por verlos, la banda ha acordado una World Tour que comenzará en dos meses cortos. Las ciudades y venues han sido seleccionados, y la track list ha sido revisada con varias canciones nuevas escritas para su nuevo álbum, que será grabado al concluir la gira.

Art Tenor te llama una vez más para hacer esta gira mundial tan épica como siempre. Crea una nueva app Lightning, llamada World Tour Manager para que Art la use para rastrear todas las giras que Flow & the Low Codes tienen próximamente.

| Propiedad | Valor |
|-----------|-------|
| App Name | World Tour Manager |
| Image | Asigna cualquier imagen de tu elección que fomente rockstardom. |
| Navigation Style | Console navigation |
| Selected Items | Accounts, Albums, Artists, Campaigns, Contacts, Songs, Reports |
| Selected Profiles | System Administrator, Standard User |

> [!NOTE]
> **Interpretación**: Crear Lightning App desde App Manager con navegación estilo consola. Agregar los 7 objetos especificados como Navigation Items y asignar a los 2 perfiles indicados.

---

**Grupo**: 3 - VISIONARY ADMINS  
**Fecha**: 17 Enero 2026

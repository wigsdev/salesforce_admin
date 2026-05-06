# Preguntas y Respuestas: Panel de Evaluación (Sprint 3)

Este documento contiene las preguntas más probables que te hará el panel evaluador (Team Leaders técnicos y representantes de Recursos Humanos) tras finalizar tu presentación y demo de Lumina Tech.

---

## 💻 SECCIÓN 1: PREGUNTAS TÉCNICAS (Team Leaders / Arquitectos)
*El objetivo de estas preguntas es validar que no solo seguiste un tutorial, sino que entiendes la arquitectura y la seguridad detrás de la plataforma.*

**1. "Veo que tienes un formulario público para captar Leads. ¿Cómo te aseguraste de que un usuario anónimo no pueda vulnerar la base de datos de Salesforce?"**
*   **Respuesta Ideal:** "Aplicamos el principio de privilegio mínimo usando el *Guest User Profile* de la comunidad. Le dimos permisos estrictamente de 'Lectura' y 'Creación' únicamente al objeto Lead, y habilitamos el acceso exclusivo al Screen Flow de captación. De esta forma, el visitante anónimo puede insertar datos, pero es arquitectónicamente imposible que extraiga o modifique registros existentes."

**2. "En el formulario privado de trámites, ¿cómo sabe el sistema a qué alumno asociar el Caso sin pedirle que escriba su ID?"**
*   **Respuesta Ideal:** "Aprovechamos que el alumno ya está autenticado en el portal mediante su licencia de *Customer Community*. Dentro del Screen Flow, utilicé la variable global `{!$User.ContactId}`. Esto extrae el ID del contacto asociado al usuario activo y lo vincula directamente al nuevo Caso. Esto no solo mejora la experiencia del usuario al no pedirle datos repetidos, sino que previene el fraude o la suplantación de identidad."

**3. "Configuraste una Base de Conocimiento (Knowledge). ¿Cómo controlaste qué artículos son públicos y cuáles son exclusivos para alumnos logueados?"**
*   **Respuesta Ideal:** "Lo manejamos a través de dos mecanismos: primero, la estructura de *Data Categories* para organizar el contenido. Segundo, la visibilidad a nivel de registro. Al publicar un artículo, marcábamos la casilla 'Visible in Public Knowledge Base' si era para visitantes, o exclusivamente 'Visible to Customer' si contenía políticas internas o trámites que solo un alumno autenticado debe ver."

**4. "Implementaste Omni-Channel y Einstein Bot (LuminaBot). ¿Cuál fue el mayor reto técnico de esta configuración?"**
*   **Respuesta Ideal:** "El mayor reto fue la orquestación. Omni-Channel no es solo prender un interruptor; requiere configurar Canales de Servicio, Colas de Enrutamiento y Estados de Presencia para los agentes. Además, integrar el Bot como primer nivel de contención requirió mapear correctamente las transferencias para que, cuando el bot no pudiera resolver la duda, el agente recibiera el caso en su Service Console junto con la transcripción completa del chat, garantizando una transición sin fricciones."

---

## 🤝 SECCIÓN 2: PREGUNTAS DE RECURSOS HUMANOS / SOFT SKILLS
*El objetivo es evaluar tu proactividad, trabajo en equipo y capacidad de resolución de problemas.*

**5. "El Team Lead inicialmente catalogó la implementación del Chat y el Bot como 'laborioso' y sugirió dejarlo fuera del alcance. ¿Por qué decidiste implementarlo de todas formas?"**
*   **Respuesta Ideal:** "Como equipo, analizamos el problema raíz de la Rectora Vance: el cuello de botella en la atención. Si bien un formulario asíncrono (Casos) ayudaba, sabíamos que en época de exámenes la demanda en tiempo real iba a colapsar al equipo de soporte. Decidimos invertir tiempo extra en investigar y configurar el Bot y el Omni-Channel porque entendimos que aportaba un valor de negocio inmenso. Logramos superar las expectativas entregando una solución robusta y escalable."

**6. "Mencionas que este proyecto de Lumina Tech se realizó en un entorno simulado. ¿Cómo te asegura eso estar listo para un cliente real como nosotros?"**
*   **Respuesta Ideal:** "Aunque Lumina Tech es un caso de estudio, la implementación fue 100% real. Trabajamos bajo metodologías ágiles, enfrentamos límites reales de licencias (Developer Edition), lidiamos con el modelo de seguridad de Salesforce y respondimos a requerimientos de negocio ambiguos que tuvimos que refinar. Los problemas técnicos de permisos, visibilidad de datos y flujos que resolví aquí son exactamente los mismos que enfrentan las empresas reales en producción."

**7. "¿Cómo te aseguraste de que la solución técnica realmente resolviera el problema del negocio?"**
*   **Respuesta Ideal:** "Mi enfoque siempre es *Business-First*. Antes de configurar nada en Salesforce, traducimos los dolores de la Rectora (altos tiempos de respuesta, procesos manuales) en Historias de Usuario claras. Por ejemplo, no implementamos 'Experience Cloud' porque sí; implementamos un 'Campus Virtual' porque el negocio necesitaba descentralizar la atención hacia el autoservicio. Esa alineación entre negocio y tecnología fue la clave del éxito del Sprint."

---

## 💡 TIPS PARA EL PANEL
*   Si te hacen una pregunta técnica que no sabes o no recuerdas, **nunca inventes**. Di: *"Ese detalle técnico específico tendría que revisarlo en la documentación de Salesforce o en mi entorno de configuración, pero la lógica de negocio detrás de eso la manejamos de [tal forma]..."*
*   Usa siempre la palabra **"Nosotros"** o **"El equipo"** cuando hables de decisiones de diseño, y **"Yo"** cuando te pregunten sobre qué componente específico configuraste tú.

# Nota Informativa del Tech Lead — Sprint 3

¡Hola, Equipo! Como su Tech Lead, he definido los objetivos y el alcance para este Sprint 3. Entramos en una etapa clave donde dejamos de mirar Salesforce solo "hacia adentro" y empezamos a conectarlo con el mundo exterior. Aquí tienen los requerimientos técnicos y la visión funcional que espero ver implementada:

---

## 1. El Objetivo del Sprint: Expandiendo las fronteras del CRM

Este sprint gira en torno a una herramienta fundamental: **Experience Cloud**. El objetivo es que dejen de ver a Salesforce como una base de datos interna y lo transformen en un portal interactivo.

Deben ser capaces de exponer datos del CRM de forma segura, habilitar el autoservicio mediante bases de conocimiento (**Knowledge**) y ofrecer soporte en tiempo real. Todo esto manteniendo la identidad visual de la marca a través de los **Themes** del sitio.

---

## 2. Casos de Uso por Proyecto (Viabilidad)

He validado que esta implementación es el paso lógico para los tres modelos de negocio en los que están trabajando:

| Proyecto | Aplicación en el Portal (Experience Cloud) |
|:---|:---|
| **Lumina Tech** | Partner Central / Help Desk: Registro de leads por parte de distribuidores o levantamiento de tickets técnicos cuando el software reporta fallas. |

---

## 3. Estrategia Técnica: Screen Flows como Interfaz Web

Una de las soluciones más potentes que vamos a implementar es el uso de **Screen Flows** como formularios dentro del sitio. Para esto, quiero que sigan este orden de arquitectura:

1. **Diseño del Flujo (Backend):** Construyan el Screen Flow dentro de Salesforce con las pantallas necesarias (ej: Datos de contacto, motivos, carga de archivos). Asegúrense de que la lógica final cree el registro correspondiente (Lead, Caso o el Objeto Personalizado que definieron).

2. **Definición de Audiencia y Seguridad:** Este es el punto crítico. Deben decidir si el formulario es **Público** (ej: un "Contáctenos" para prospectos) o **Privado** (solo para usuarios logueados). Si es público, recuerden configurar los permisos del **Guest User Profile** para que tenga acceso a ejecutar el Flow y crear registros.

3. **Implementación Visual (Experience Builder):** Una vez que el flujo es seguro y funcional, su publicación en el sitio es simple. Usen el componente estándar de **"Flow"** en el Builder, arrástrenlo a la página y selecciónenlo del menú.

---

Equipo, este sprint es el que le da "vida" al sistema para el usuario final. Quedo atento a sus dudas sobre la configuración de los perfiles de invitados, que suele ser el mayor reto de seguridad aquí.

¿Cómo ven el desafío? Si necesitan, podemos profundizar en cómo mapear los campos del Screen Flow para que la creación de registros sea limpia y sin errores de validación.

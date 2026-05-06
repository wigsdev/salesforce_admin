# Preparación para Entrevistas
## Wilmer Gulcochía — Aura Renewable Solutions | Admin Salesforce + BA

---

# PARTE 1: ENTREVISTA CON RECURSOS HUMANOS

---

## P1: "Cuéntame sobre ti."

**Respuesta sugerida (60-90 segundos):**

> "Soy Administrador Salesforce con perfil híbrido Admin/BA. Recientemente culminé
> un intensivo de 4 Sprints como parte del equipo que implementó la solución para Lumina
> Tech University. Aporté en todo el ciclo, y particularmente durante los Sprints 2 y 3 
> asumí responsabilidades de guía funcional: redactando Historias de Usuario, proponiendo 
> soluciones y apoyando la configuración técnica. El trabajo en equipo fue evolutivo: en 
> el Sprint 1 consolidamos el modelo de datos; en el Sprint 2 automatizamos procesos 
> con Flow Builder; y actualmente en el Sprint 3 estamos escalando la solución con 
> Experience Cloud y Omni-Channel. Me postulo a Aura porque quiero aplicar esta 
> capacidad de trabajo colaborativo en una empresa con impacto real."

**Puntos clave a no olvidar:**
- Menciona el proyecto Lumina Tech por nombre
- Cierra siempre conectando con por qué Aura

---

## P2: "¿Por qué quieres trabajar en Aura Renewable Solutions?"

> "Aura trabaja en energía limpia con alcance global, y Salesforce es su motor
> operativo. Eso significa que el trabajo del Administrador tiene impacto directo
> en la eficiencia de los equipos de Ventas, Operaciones y Finanzas. No es
> mantenimiento rutinario, es estrategia. Eso es exactamente el tipo de rol híbrido
> Admin/BA donde quiero crecer."

---

## P3: "No tienes certificación ADM-201 activa. ¿Cómo lo justificas?"

> "Es un proceso en marcha. Lo que puedo mostrar hoy son 17 Superbadges en
> Trailhead, incluyendo la suite completa de Flow Builder, 5 Superbadges de
> Seguridad y Gobernanza, y el Superbadge de Agentforce Service. Eso no es
> teoría, son evaluaciones prácticas que Salesforce aplica en escenarios reales.
> La certificación formal está programada y es el siguiente paso natural."

---

## P4: "No tienes 3 años de experiencia formal. ¿Por qué deberíamos contratarte?"

*Aplicar la táctica 'Portafolio + Mentalidad + Plan 30/60/90' de la clase 23.2*

> "Tienes razón, pero mi formación técnica no fue teórica, fue un simulador
> de entornos de producción estructurado en Sprints ágiles. Puedo mostrar una
> implementación Salesforce real de Lumina Tech en video — modelo de seguridad
> validado, automatizaciones complejas, portal en Experience Cloud y un bot activo.
> Ejecuté el ciclo completo de vida del software que muchos candidatos con 3 años
> de experiencia fragmentada no dominan porque solo ven una pequeña parte de la Org.
> En los primeros 30 días mi objetivo sería auditar su instancia actual. En los 60,
> ya estaría entregando mejoras usando este mismo rigor metodológico."

---

## P5: "¿Cómo manejas trabajar de forma remota e independiente?"

> "Tengo formación específica en productividad, gestión del tiempo y autogestión.
> Durante el proyecto Lumina Tech trabajé de forma asíncrona con mi equipo usando
> Trello para gestionar el backlog, documentación técnica en cada entrega y
> comunicación estructurada con el cliente. No necesito supervisión constante:
> necesito contexto claro y criterios de éxito definidos."

---

## P6: "¿Cuál fue tu mayor desafío técnico y cómo lo resolviste?" (Método STAR)

**Situación:** En el Sprint 3 del proyecto, el Einstein Bot mostraba el mensaje "No hay
agentes disponibles" al intentar regresar al menú principal después de ver una carrera.

**Tarea:** El bot debía permitir la navegación circular sin bloqueos.

**Acción:** Identifiqué que la variable de la pregunta estática estaba configurada como
"Omitir si ya tiene valor", lo que hacía que el bot saltara la pregunta y ejecutara la
última acción registrada. Cambié la configuración a "Sobrescribir valor" y verifiqué que
el texto de los botones coincidiera exactamente con las condiciones de las reglas
(sensibilidad a mayúsculas).

**Resultado:** El flujo de navegación quedó circular y funcional: el alumno puede consultar
carreras, volver al menú y transferirse a un agente en una sola sesión sin interrupciones.

---

## P7: "¿Dónde te ves en 2 años?"

> "Con la certificación ADM-201 activa y avanzando hacia Advanced Administrator
> o Service Cloud Consultant. Quiero crecer hacia un rol donde pueda diseñar la
> arquitectura de soluciones escalables, no solo implementarlas. Aura tiene el
> contexto perfecto para eso."

---

---

# PARTE 2: ENTREVISTA TÉCNICA

---

## BLOQUE A — Flow Builder (el tema más evaluado)

### P1: "¿Cuándo usarías un Record-Triggered Flow vs un Screen Flow?"

> "Un Record-Triggered Flow se ejecuta automáticamente cuando un registro se crea,
> actualiza o elimina — sin intervención del usuario. Lo uso para automatización de
> fondo: actualizar campos relacionados, crear registros hijos, enviar notificaciones.
> Durante el Sprint 2 en Lumina Tech lo usé para disparar la creación automática de
> registros de caso cuando un alumno completaba un requisito en el backend.
> Un Screen Flow requiere interacción activa del usuario — tiene pantallas e inputs.
> En el Sprint 3 lo desplegué en el portal de Experience Cloud para que el alumno
> inicie trámites paso a paso. La regla es simple: si el usuario no necesita ver
> nada, uso Triggered. Si hay entrada de datos manual, uso Screen."

---

### P2: "¿Qué es un Before-Save vs After-Save Flow?"

> "Before-Save se ejecuta antes de que el registro se grabe en la base de datos —
> es más eficiente en rendimiento porque no consume una operación DML adicional.
> Lo uso para actualizar campos en el mismo registro. After-Save se ejecuta después
> del commit — lo uso cuando necesito crear o modificar otros registros relacionados,
> porque en ese punto el ID del registro ya existe. La Salesforce Best Practice es
> siempre preferir Before-Save para evitar problemas de Governor Limits."

---

### P3: "¿Cómo aseguras la calidad de los datos antes de hacer una carga masiva?"

> "La carga masiva es un proceso crítico y muy común en el rol. En Lumina Tech,
> antes de subir los registros históricos con Data Loader durante el Sprint 2,
> seguí un protocolo estricto: primero limpié y desdupliqué la data en Excel
> (usando VLOOKUP y estandarizando textos); luego me aseguré de que los valores
> coincidieran exactamente con los campos picklist de Salesforce. Finalmente,
> Regla de Validación o Flow se rompiera antes de impactar Producción. Un buen
> Administrador nunca inserta datos directamente a ciegas."

---

### P4: "Al ganar una Oportunidad, debemos crear 5 registros hijos y enviar un email. ¿Cómo evitas romper los límites (Governor Limits) en el Flow?"

> "Este es un escenario clásico de **Bulkification**. Como es una acción que ocurre al ganar una
> Oportunidad, usaría un **Record-Triggered Flow - After Save**. Para no romper los límites DML
> al crear múltiples registros, **nunca** coloco el elemento 'Create Records' dentro de un Loop.
> La estructura correcta y optimizada es: usar un **Loop** para iterar, un **Assignment** para
> asignar los valores de cada nuevo registro, agregarlos a una **Collection Variable**, y
> colocar un único elemento **Create Records** *fuera del Loop*, pasándole la colección completa."

---

### P5: "¿Cómo depuras un Flow y evitas que los errores afecten al usuario?"

> "Utilizo dos herramientas clave de Salesforce. Primero, antes de activar cualquier Flow, uso el botón **Debug** en modo *Rollback* (Reversión). Esto me permite ver el paso a paso y evaluar los criterios en tiempo real sin modificar datos reales en la base de datos.
> Segundo, utilizo **Fault Paths** (Rutas de Fallo) en todos los elementos rosas (Create/Update). Si un elemento de base de datos falla, el Fault Path captura el error, le muestra una pantalla amigable al usuario (evitando el error de sistema rojo) y me envía un correo a mí como Administrador con el detalle exacto para solucionarlo rápido."

---

## BLOQUE B — Modelo de Seguridad

### P6: "Explícame OWD y cuándo usarías Private vs Public Read Only."

> "OWD — Organization-Wide Default — define el acceso base a los registros antes
> de aplicar cualquier otra regla. Es el 'piso' de seguridad.
> Private significa que solo el dueño del registro y usuarios en posiciones
> superiores en la jerarquía pueden verlo. Lo uso cuando los datos son sensibles
> y no deben compartirse entre equipos — por ejemplo, datos de salario o
> información médica.
> Public Read Only significa que todos pueden ver el registro pero solo el dueño
> puede editarlo. Lo uso para catálogos de productos o artículos de Knowledge
> donde todos necesitan leer pero solo ciertos roles deben modificar.
> En el Sprint 1 de Lumina Tech establecimos las bases de seguridad usando Private
> para los registros académicos y configuré Sharing Rules para abrir el acceso a
> roles específicos de docentes, garantizando el principio de privilegio mínimo."

---

### P7: "¿Diferencia entre Perfil, Permission Set y Permission Set Group?"

> "**Perfil:** Es obligatorio y define el 'piso' o acceso base del usuario (aplicaciones, objetos, permisos del sistema). Un usuario solo puede tener un Perfil.
> **Permission Set:** Son 'capas' individuales de permisos que se agregan encima del Perfil. Los uso para dar accesos específicos sin crear perfiles redundantes. Por ejemplo, en Lumina Tech di acceso a analíticas a los supervisores con un Permission Set, sin tocar el perfil base de 'Docente'.
> **Permission Set Group:** Es un paquete que agrupa MÚLTIPLES Permission Sets. Si tengo un rol que necesita 5 accesos distintos, en lugar de asignarle los 5 Permission Sets individualmente (propenso a errores), los agrupo en un 'Group' y le asigno solo eso. Esto permite escalar la seguridad basada en 'Personas' (Roles de Trabajo) mucho más rápido."

---

### P8: "Escenario: Finanzas pide ver solo Oportunidades mayores a $50K. El gerente de Ventas debe editarlas, pero el resto no. ¿Cómo lo configuras?"

> "Antes de tocar el sistema, pregunto por el organigrama exacto (Roles) para saber la
> jerarquía. Luego, aplico este diseño en 4 niveles:
> 1. **OWD (Organization-Wide Default)** de Oportunidad en **Privado** (nadie ve nada de otros).
> 2. **Jerarquía de Roles** para asegurar que el gerente de Ventas pueda ver y editar las de su equipo.
> 3. **Sharing Rule** basada en criterios (Monto > $50K) para otorgar acceso de Lectura al rol de Finanzas.
> 4. Validar si Finanzas tiene permisos a nivel de **Perfil / Permission Set** para leer el objeto Oportunidad."

---

## BLOQUE C — Business Analysis

### P9: "¿Cómo levantarías requerimientos con un stakeholder que no sabe qué quiere?"

> "Primero escucho sin interrumpir para entender cuál es el dolor real, no la
> solución que ellos proponen. Luego hago preguntas abiertas: ¿Qué está pasando
> hoy que no debería pasar? ¿Qué tiene que ser verdad para que este proceso
> funcione bien? ¿Cómo sabremos que lo logramos?
> Con esas respuestas redacto la Historia de Usuario: Como [rol], quiero [acción],
> para [beneficio]. Luego defino los Criterios de Aceptación —condiciones mínimas
> que deben cumplirse para que la historia esté completa— y los valido con el
> stakeholder antes de configurar nada. Eso evita retrabajo."

---

### P10: "¿Cuándo NO configurarías una solución personalizada y usarías estándar?"

> "Siempre evalúo primero si Salesforce ya resuelve el problema out-of-the-box.
> Las razones para preferir estándar son mantenibilidad, actualizaciones automáticas
> con cada release, y menor deuda técnica.
> Solo voy a personalización cuando el estándar no cubre el caso de negocio
> específico del cliente, o cuando el workaround estándar sería más complejo de
> mantener que una solución declarativa limpia. Y dentro de personalización, siempre
> prefiero declarativo (Flows) sobre código (Apex) — menos riesgo, más fácil de
> mantener por otros Admins."

---

## BLOQUE D — Experience Cloud / Service Cloud

### P11: "¿Cómo funciona el Guest User Profile en Experience Cloud?"

> "El Guest User es el perfil que usan los visitantes no autenticados del portal.
> Por defecto tiene permisos muy restrictivos. En el Sprint 3 de Lumina Tech, al
> lanzar el portal, lo configuré para que los visitantes vieran artículos públicos de
> Knowledge, pero bloqueé la creación o edición de registros. Para trámites reales,
> forzamos la autenticación. La seguridad comienza verificando que el OWD permita
> Guest Access y que el perfil Guest solo tenga acceso de Lectura — nunca modificar."

---

### P12: "¿Qué es Omni-Channel y cómo lo configuraste?"

> "Omni-Channel es el motor de enrutamiento de Salesforce para Service Cloud.
> Permite distribuir trabajo — Casos, Chats, Llamadas — hacia los agentes
> disponibles basándose en su capacidad y habilidades.
> En Lumina Tech configuré: una Service Channel para Chat, una Queue donde
> los agentes se registraban, una Routing Configuration con capacidad máxima
> de 3 chats por agente, y el Presence Status. Cuando el Einstein Bot
> transfería al agente, Omni-Channel enrutaba el chat a la cola y el agente
> recibía el ping en la Service Console. Validé el flujo completo en modo
> Sneak Peek antes de activarlo."

---

## BLOQUE E — Analítica (Informes y Dashboards)

### P13: "¿Qué diferencia hay entre un Reporte y un Dashboard?"

> "Un **Reporte** es el conjunto de datos tabulados o agrupados que extrae el sistema basado en los criterios y filtros definidos; muestra la información pura. Un **Dashboard** (Cuadro de Mando) es la representación visual y gráfica de esos datos.
> La clave operativa es que el Dashboard se alimenta de los Reportes subyacentes. Como Administrador/BA, diseño Reportes robustos para que el equipo operativo audite la data, y configuro Dashboards para que los directores de Ventas o Finanzas puedan consumir esa información de un solo vistazo y tomar decisiones estratégicas."

---

## BLOQUE F — Preguntas trampa que debes anticipar

### P14: "¿Cuál es la diferencia entre Workflow Rules, Process Builder y Flows?"

> "Workflow Rules y Process Builder están en modo legacy — Salesforce los
> deprecó y migra todo a Flow. No los configuraría en proyectos nuevos.
> Flows son el estándar actual: más potentes, más flexibles, soportan lógica
> compleja, pueden hacer todo lo que Workflow y Process Builder hacían y mucho
> más. Si me encuentro una org con Workflow Rules activos, los analizo y
> migro a Flows como parte de la gestión de deuda técnica."

---

### P15: "¿Desarrollarías con Apex o LWC para resolver este problema?"

*(Pregunta trampa — están evaluando si conoces el límite del rol Admin)*

> "Esa es una pregunta importante porque define el límite del rol Administrador.
> Si el problema se puede resolver con Flows, objetos personalizados, reglas de
> validación o Experience Cloud — lo resuelvo declarativamente. Ese es mi
> dominio y donde tengo más valor.
> Si requiere lógica de negocio compleja que supera las capacidades declarativas,
> o integraciones técnicas vía API, es el momento de involucrar a un Developer.
> Un buen Admin sabe exactamente cuándo escalar y no intenta codificar lo que no
> corresponde a su rol."

---

## TIPS FINALES PARA AMBAS ENTREVISTAS

- **Regla de oro:** Responde siempre desde el negocio antes que desde la técnica.
- **Método STAR:** Toda respuesta de experiencia debe tener Situación, Tarea, Acción y Resultado.
- **Usa el nombre del proyecto:** "En Lumina Tech..." da credibilidad inmediata.
- **No improvises debilidades:** Si no sabes algo, di: "No lo he implementado directamente, pero sé cómo abordarlo y tengo el Superbadge / la formación que lo cubre."
- **Prepara dos preguntas para el entrevistador:**
  - ¿Cuáles son los dos procesos más críticos que Salesforce soporta hoy en Aura?
  - ¿Cómo es el proceso de priorización de nuevas funcionalidades en la plataforma?

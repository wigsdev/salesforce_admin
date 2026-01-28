# Salesforce Admin + Agent Force (Teoría Clase 10)

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

## Aspectos Básicos de la Seguridad
*vamos a ver la segunda parte de modelado de datos…*

### La Muralla Exterior (Políticas de Acceso y MFA)
**Perfil**:
1.  **Horario de Inicio de Sesión (Login Hours)**: Si su turno termina a las 6 PM, a las 6:01 PM el sistema los bloquea.
2.  **Rangos de IP (IP Ranges)**: Aquí hay una distinción vital para el examen y la vida real...
    *   Si configuran IPs en **'Network Access'** (Confianza), el usuario recibe un código por email si está fuera de rango. Puede entrar.
    *   Si configuran IPs en el **Perfil**, el usuario es **BLOQUEADO** totalmente si está fuera de rango. No hay código que valga.
    *   *En el proyecto: Usen rangos de perfil para Call Centers o empleados que solo deben trabajar desde la oficina".*

### El Chequeo Médico (Health Check)
Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:
*   La **Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
*   La **Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

### Auditoría y Comportamiento (Login History)
Para el proyecto: La seguridad son capas.
*   **MFA y Contraseñas fuertes** para verificar identidad.
*   **IP y Horarios** para restringir el contexto.
*   **Health Check** para mantener la configuración óptima.
*   **Login History** para resolver problemas y detectar ataques (como 50 intentos fallidos en un minuto). Si dominan esto, su Org será una fortaleza".

**¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
Usamos la herramienta de **Merge (Fusionar)**. Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
*Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## Posibles Preguntas

### 1. La trampa del examen: Network Access vs. Profile IPs
**Alumno**: "Profe, configuré una IP en 'Acceso a la Red' (Network Access) y aún así me pidió un código de verificación. ¿Para qué sirve entonces? ¿No es igual a restringir por Perfil?"
**Respuesta**: "Esta es la pregunta más importante del examen. ¡No son lo mismo!
*   **Network Access (Confianza)**: Es una lista blanca. Si entras desde aquí, Salesforce no te pide código de verificación. Si entras desde fuera, te deja pasar PERO te pide un código. Nunca bloquea.
*   **Profile IP Ranges (Restricción)**: Es una lista estricta. Si entras desde aquí, pasas. Si entras desde fuera, Salesforce te bloquea totalmente. Ni código, ni nada. Acceso denegado".

### 2. El drama del Horario de Inicio de Sesión
**Alumno**: "Si configuro que el horario de trabajo termina a las 18:00, y estoy escribiendo un email larguísimo a un cliente a las 17:59... ¿Qué pasa a las 18:01?"
**Respuesta**: "Prepárate para llorar un poco. A las 18:01, la sesión muere. Puedes seguir mirando la pantalla que ya tenías abierta, pero en el momento en que hagas clic en 'Guardar' o intentes navegar a otra página, te saldrá un error de acceso y perderás lo que no hayas guardado. **Tip**: Por eso siempre damos un margen de 15-30 minutos extra al configurar horarios".

> "¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path. No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'. Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

### 3. ¿Por qué me pide código cada vez?
**Alumno**: "Cada vez que entro a Salesforce me manda un código al email. Es molesto. ¿Cómo lo quito?"
**Respuesta**: "Eso pasa porque Salesforce no reconoce tu navegador o tu IP. Tienes dos soluciones:
1.  Agrega tu IP actual a la lista de Network Access.
2.  O bien, dale al botón de 'Recordarme' o 'No volver a preguntar' en el navegador. (Nota: Esto usa cookies, si borras cookies, te volverá a preguntar)".

### 4. El miedo al "Fix All" (Arreglar todo)
**Alumno**: "En el Health Check me sale que la seguridad es 'Baja'. ¿Puedo darle a 'Fix All' en la empresa de mi cliente para impresionarlos?"
**Respuesta**: "¡ALTO! No lo hagas sin analizar. Si le das a 'Fix All', Salesforce podría cambiar la política de contraseñas de 'Caduca en 90 días' a 'Caduca en 30 días'. Resultado: Mañana por la mañana, 500 empleados intentarán entrar y el sistema les obligará a cambiar su contraseña al mismo tiempo. Colapsarás el soporte técnico. **Regla**: Cambia las configuraciones una por una y avisa a los usuarios antes".

### 5. Usuario bloqueado misteriosamente
**Alumno**: "Un usuario jura que está poniendo bien su contraseña, pero dice 'Cuenta Bloqueada'. ¿Qué pasó?"
**Respuesta**: "Seguramente excedió el número máximo de intentos fallidos (usualmente 3 o 5). Salesforce bloquea la cuenta temporalmente (por 15 min) o indefinidamente según la configuración. Tu trabajo: Ve al usuario y busca el botón 'Desbloquear' (Unlock). Luego, dile que respire hondo y escriba despacio".

### 6. ¿Es obligatorio usar el celular?
**Alumno**: "Tengo un cliente que prohíbe el uso de celulares personales en la oficina. ¿Cómo hacen MFA?"
**Respuesta**: "Buena pregunta de mundo real. Si no pueden usar la App 'Salesforce Authenticator' en el móvil, tienen opciones:
*   Llaves de seguridad físicas (YubiKey): Se conectan al puerto USB de la computadora.
*   Apps de escritorio: Autenticadores que se instalan en la PC (aunque son menos comunes por seguridad).
*   Lo que NO cuenta como MFA seguro para Salesforce es recibir el código por Email o SMS. Eso es solo 'Verificación de Identidad', no MFA fuerte".

### 7. Perdí mi teléfono
**Alumno**: "Profe, el usuario perdió su celular con el Authenticator. ¿Perdió su cuenta para siempre?"
**Respuesta**: "No, para eso estás tú como Admin.
1.  Vas a su registro de Usuario en Configuración.
2.  Haces clic en 'Desconectar' (Disconnect) al lado del campo 'App Registration: Salesforce Authenticator'.
3.  La próxima vez que inicie sesión, Salesforce le pedirá configurar un nuevo teléfono".

---

**Guia**: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol.

---

## ¡Manos a la obra!
Avanzamos con los trails.

**LEER CON ATENCIÓN**
Las prácticas previas al challenge son importantes para entender el challenge. **NO DEJARLAS PASAR**.

### Errores / Consultas
*   Agotar herramientas.
*   Consultar con su grupo.
*   Hacer una nueva ORG.
*   Recién consultar a los profesores.
*   Contexto: **SB-Jueves**.

### Pair Programming
*   Compartir pantalla.
*   Hablar sobre el proceso del Trailhead.
*   Ir rotando.
*   No se puede estar en silencio.
*   El trabajo individual es fuera de la cursada.

### Seguridad
*   LINK

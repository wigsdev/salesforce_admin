# Salesforce Admin + Agent Force (Teoría Clase 9)

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
*   **Jueves**: Preguntas al final de la clase Teórica.

### Para una buena clase…
*   **Autonomía**: Utilizar las herramientas
*   **Guia**: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol

---

## Seguridad de Datos en Salesforce: El Modelo de Capas
*vamos a ver la segunda parte de modelado de datos…*

### Los Cimientos: ¿Qué puedes ver? (Organización, Objetos y Campos)
> "¿Qué puedes ver? Tres niveles de control: Org > Objeto > Campo."

El acceso funciona por capas: si no entras al Objeto, no puedes ver sus Campos.

### La Regla de Oro del Registro: Valores Predeterminados (OWD)
**¿Qué registros específicos pueden ver?**
La base de todo son los Valores Predeterminados de Toda la Organización (OWD - Org-Wide Defaults).
Los OWD son la única herramienta en Salesforce que sirve para **restringir** el acceso.

**Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:**
*   La **Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
*   La **Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

---

### Abriendo las Puertas: Jerarquía y Reglas de Uso Compartido
1.  **La Jerarquía de Roles** (Acceso Vertical)
2.  **Las Reglas de Uso Compartido / Sharing Rules** (Acceso Horizontal)

**¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
Usamos la herramienta de **Merge (Fusionar)**. Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.

> *Nunca eliminen un duplicado sin revisar qué información histórica tiene.*

---

## Conjunto de Permisos

### El Cambio de Paradigma: De Perfiles a Capas

#### 1. Principio de Privilegio Mínimo (La Estrategia)
Es la filosofía de seguridad base. Significa darle al usuario el acceso más restrictivo posible al empezar.
*En resumen: "Dale solo lo necesario para hacer su trabajo, ni un permiso más". Empezamos con un Perfil básico y vamos sumando permisos extra solo si hacen falta.*

#### 2. Conjuntos de Permisos / Permission Sets (La Herramienta)
Son las "llaves extra" que le das a usuarios específicos para extender lo que pueden hacer. Como los Perfiles deben ser restrictivos (por el punto 1), los Permission Sets se usan para ampliar el acceso.
*   **Diferencia**: El Perfil define quién eres (ej. Ventas Estándar), el Permission Set define qué más puedes hacer (ej. "Permiso para Exportar Reportes").
*   **Nota**: Un usuario tiene 1 Perfil, pero puede tener muchos Permission Sets.

#### 3. Grupos de Conjuntos de Permisos / Permission Set Groups (El Agrupador)
Es una forma de organizar los Permission Sets para no tener que asignarlos uno por uno. Se agrupan según el rol de trabajo del usuario.
*   **Diferencia**: En lugar de asignarle a un usuario 5 Permission Sets sueltos (uno para importar, otro para borrar, otro para ver campos ocultos), creas un Grupo llamado "Gerente de Ventas" que contiene esos 5, y asignas solo el Grupo. Ahorra tiempo y evita errores.

> **El error #1 es tratar a todo el mundo como 'Cliente'.**
> Imaginen que van a una feria y recolectan 100 tarjetas. ¿Esos 100 van a comprar? No. Esos son Leads.
> Solo cuando llaman y verifican que tienen presupuesto y necesidad, los convierten en Contactos.
> Si mezclan todo, sus reportes de 'Clientes Activos' serán falsos. El Lead es el 'quizás', el Contacto es el 'confirmado'.

### Modelando la Realidad: El Grupo como "Rol de Trabajo"
El Grupo lo que hace es empaquetar estos tres conjuntos distintos en una sola unidad asignable.

> "Presten atención aquí: La Conversión es irreversible. Salesforce toma los datos del Lead y los reparte. El nombre va al Contacto, la empresa va a la Cuenta, y el interés de compra va a la Oportunidad. Como Admins, su trabajo es asegurar que si crearon un campo 'Preferencia de Color' en el Lead, ese dato viaje a la Oportunidad. Si no configuran el Field Mapping, ese dato se pierde en el limbo al convertir."

### El Superpoder: Silenciamiento (Muting Permission)
El Conjunto de Permisos de Silenciamiento (**Muting Permission Set**).
Esto nos permite decir: *'Quiero este grupo completo, pero voy a apagar este permiso específico solo dentro de este grupo'.*

> "¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path. No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'. Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso."

---

## Posibles Preguntas

### 1. La confusión clásica: Perfil vs. Rol
**Alumno**: "Profe, no entiendo bien la diferencia entre el Perfil y el Rol. ¿Los dos no dicen lo que puedo hacer?"
**Respuesta**: "Piénsalo así:
*   El **Perfil** es tu Licencia de Conducir. Dice qué puedes hacer (conducir un auto, editar un campo, borrar una cuenta).
*   El **Rol** es Tu lugar en el organigrama. Dice qué datos puedes ver basados en quién está debajo de ti.
*   Ejemplo: Tu perfil dice que sabes leer (tienes permiso de 'Leer'), pero tu rol determina qué libros de la biblioteca te dejan sacar".

### 2. El conflicto: Perfil vs. OWD
**Alumno**: "Si en mi Perfil tengo el permiso de 'Ver Todo' (View All) en Cuentas, ¿importa si el OWD es Privado?"
**Respuesta**: "¡Sí importa, pero cuidado! Normalmente, el OWD (Privado) restringe.
PERO, los permisos administrativos del Perfil llamados 'View All' (Ver Todo) y 'Modify All' (Modificar Todo) son como **'Superpoderes'** que rompen las reglas. Si tienes 'View All' en el Perfil, ignoras el OWD y ves todo. Por eso, nunca le den esos permisos a usuarios normales, solo a Admins".

### 3. FLS vs. Perfil (¿Quién gana?)
**Alumno**: "Si mi Perfil dice que puedo 'Editar' el objeto Oportunidad, pero el FLS (Seguridad de Campo) dice que el campo 'Monto' es de Solo Lectura, ¿puedo editar el monto?"
**Respuesta**: "No. La restricción más fuerte siempre gana. Imagina que el Perfil te da la llave para entrar a la casa (el Objeto), pero el FLS le pone un candado a la heladera (el Campo). Entras a la casa, pero no tocas la comida".

### 4. ¿Por qué no poner todo Público y ya?
**Alumno**: "¿No es más fácil poner el OWD en 'Público Escritura/Lectura' y nos ahorramos configurar Roles y Reglas?"
**Respuesta**: "Es más fácil hoy, pero fatal para mañana. En un proyecto real, si pones todo público:
*   Un vendedor podría robarse los clientes de otro antes de cerrar el trato.
*   Si alguien borra un dato por error, no sabrás quién fue o por qué tenía acceso.
*   Violarías leyes de protección de datos si todos ven los datos sensibles de los clientes. **Regla de oro: Siempre empieza restrictivo (Privado) y abre poco a poco**".

### 5. Perfiles vs. Permission Sets
**Alumno**: "Si ya tengo el Perfil, ¿para qué necesito los Permission Sets? ¿Por qué hacer dos cosas?"
**Respuesta**: "Por escalabilidad. Imagina que tienes 50 vendedores. Todos tienen el Perfil 'Ventas'. De repente, solo a 3 de ellos quieres dejarles borrar registros.
*   A la antigua (Solo Perfiles): Tendrías que clonar el perfil, llamarlo 'Ventas con Borrado' y mover a los usuarios. Acabas con 50 perfiles.
*   La forma moderna: Todos mantienen el mismo perfil básico. Creas un Permission Set llamado 'Permiso de Borrar' y se lo asignas solo a esos 3. Es mucho más limpio".

### 6. Restringir con Permission Sets
**Alumno**: "¿Puedo crear un Permission Set para impedir que alguien vea algo?"
**Respuesta**: "No directamente. Los Permission Sets son **Aditivos** (siempre SUMAN permisos, nunca restan). La única excepción es cuando usas un **Muting Permission Set** dentro de un Grupo. Ahí sí puedes 'silenciar' o restar un permiso específico de ese grupo".

### 7. ¿Cuándo usar un Grupo y cuándo uno suelto?
**Alumno**: "¿Cuándo debo crear un Permission Set Group en lugar de asignar los sets uno por uno?"
**Respuesta**: "Usa Grupos cuando tengas roles de trabajo definidos.
*   Si solo vas a dar un permiso temporal (ej: 'Acceso a importar datos por esta semana'), usa un Permission Set suelto.
*   Si es algo permanente del puesto (ej: 'Todo lo que necesita un Agente de Soporte Nivel 2'), crea un Grupo. Así, si contratas a otro Agente, le asignas el Grupo y listo, no tienes que recordar los 5 o 6 permisos individuales que lleva el puesto".

---

## ¡Manos a la obra!
Avanzamos con los trails.

**LEER CON ATENCIÓN**
Las prácticas previas al challenge son importantes para entender el challenge. **NO DEJARLAS PASAR**.

### Errores Comunes
*   Agotar herramientas.
*   Consultar con su grupo.
*   Hacer una nueva ORG.
*   **Recién consultar a los profesores** (tras agotar instancias).

### Contexto
*   **SB-Jueves**: Herramientas extra.
*   **Pair Programming**:
    *   Compartir pantalla.
    *   Hablar sobre el proceso del Trailhead.
    *   Ir rotando.
    *   No se puede estar en silencio.
    *   El trabajo individual es fuera de la cursada.

### Seguridad
*   LINK (Pendiente).

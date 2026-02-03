# Salesforce Admin + Agent Force

### Daily
- **Del 1 al 10 cómo te sentís?**
- **Qué te proponés para hoy?**

---

> [!NOTE]
> **Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN**

### Skills Técnicas (El "Qué" haces)
- **Gestión de Usuarios y Seguridad**: El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
- **Gestión de Datos (Data Management)**: Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
- **Automatización Básica (Flows)**: Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
- **Reportes y Dashboards**: Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.
- **AgentForce**: puedas familiarizarte con la configuración de agentes dentro de Salesforce.

> [!NOTE]
> **Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN**

### Skills Blandas (El "Cómo" lo haces)
- **Comunicación Traducida**: Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
- **Resolución de Problemas (Google-Fu)**: No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
- **Mentalidad de Aprendiz (Learner's Mindset)**: Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
- **Atención al Detalle**: Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.

> [!NOTE]
> **Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN**

---

### Colaboración
- Aprender con y de otras personas

### Ausencias
- Seguir con la planilla y actividades 

### Mic o Chat
- Comunicación
- **ERRORES**
- **Atrasados**

### Jueves
- **PREGUNTAS** (Al final de la clase Teórica)

### Para una buena clase…
- **AUTONOMÍA**: Utilizar las herramientas

---

**Vamos a ver la segunda parte de modelado de datos…**

---

## ¿Qué es Flow Builder?
**Definición simple**: Es la herramienta más potente de Salesforce para "programar sin código". Si Salesforce fuera una casa, Flow es la electricidad y la domótica.

**Analogía**: Es como dibujar un diagrama de flujo en una pizarra, pero cuando terminas, el diagrama funciona de verdad.

---

## Los 3 Tipos de Flows Esenciales
1. **Record-Triggered Flow (El "Automático")**: Se dispara cuando algo pasa en un registro (Crear, Actualizar, Borrar). Ejemplo: Al cerrar una venta, se crea una tarea.
2. **Screen Flow (El "Interactivo")**: Requiere que un humano haga clic e introduzca datos. Son pantallas guiadas. Ejemplo: Un formulario paso a paso para dar de alta un reclamo.
3. **Schedule-Triggered Flow (El "Programado")**: Se ejecuta en una fecha/hora específica. Ejemplo: Todos los lunes a las 9 AM, revisar tareas vencidas.

---

### Manejo de Duplicados (Escenario de Examen)
Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:
- **La Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
- **La Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

---

## Aplicación en un Proyecto Real

### El Escenario:
El cliente (Gerente de Ventas) te dice: *"Mis vendedores se olvidan de contactar a los clientes nuevos. Quiero que cuando un Lead se marque como 'Muy Interesado' (Hot), el sistema avise al vendedor automáticamente."*

### La Solución con Flow (Paso a Paso Lógico):
1. **Disparador (Trigger)**: Elegimos Record-Triggered Flow. Objeto: Lead. Condición: Rating equals Hot.
2. **Acción Inmediata**: Usamos el elemento Action para "Enviar Email" o el elemento Create Records para crear una "Tarea de seguimiento" asignada al dueño del Lead.
3. **Resultado**: El vendedor ya no tiene que "acordarse". El sistema trabaja por él.

**¿Por qué Flow y no otra cosa?**
Porque permite lógica condicional compleja (ej: "Si es Hot Y el presupuesto es > 10k, manda email al Director; si es < 10k, manda email al Vendedor").

---

### Limpieza de Datos
**¿Qué hacemos si ya tenemos 1000 duplicados?** No se borran uno por uno.
Usamos la herramienta de **Merge (Fusionar)**. Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.

> [!IMPORTANT]
> Nunca eliminen un duplicado sin revisar qué información histórica tiene.

---

## 💡 Tips que NO dice Salesforce

### 1. La Regla de Oro del "Bucle de la Muerte":
- **Tip**: NUNCA pongas un elemento rosa (Get, Create, Update, Delete) dentro de un Loop (bucle).
- **Por qué**: Salesforce tiene límites. Si actualizas registros uno por uno dentro de un bucle de 100 registros, el sistema explotará (Límite de SOQL/DML). Siempre haz los cambios en una lista y actualiza la lista completa fuera del bucle.

---

### 2. No "Hardcodear" IDs (Nunca copies y pegues IDs):
- **Tip**: Si necesitas asignar una tarea a un usuario específico o una cola, no copies el ID de la URL y lo pegues en el Flow.
- **Por qué**: Ese ID cambiará cuando pases de Sandbox a Producción y tu flujo se romperá. Usa siempre un "Get Records" para buscar el ID dinámicamente por nombre.

---

### 3. El campo "Descripción" es obligatorio (moralmente):
- **Tip**: Salesforce dice que es opcional. Tú di que es obligatorio.
- **Por qué**: Dentro de 6 meses, cuando el flujo falle, no recordarás qué hace la "Decisión 2". Escribe siempre qué hace cada paso.

---

### 4. Debug (Depurar) es tu mejor amigo:
- **Tip**: Nunca actives un Flow sin haber usado el botón "Debug" primero. Es la única forma de ver "en cámara lenta" qué camino está tomando tu lógica.

---

> [!TIP]
> **¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path.**
> No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'.
> Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso.

---

## ¡Manos a la obra!
Avanzamos con los trails.

**Guia**: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol

---

### LEER CON ATENCIÓN
- **Las prácticas previas al challenge son importantes para entender el challenge**
- **NO DEJARLAS PASAR**

### Atención a Errores
1. Agotar herramientas
2. Consultar con su grupo
3. Hacer una nueva ORG
4. Recién consultar a los profesores

### Consultas
- Haber agotado todas las instancias de herramientas
- Contexto
- SB-Jueves

---

## Pair Programming
- Compartir pantalla
- Hablar sobre el proceso del Trailhead
- Ir rotando
- **No se puede estar en silencio**
- El trabajo individual es fuera de la cursada

---

### FLOWS 1
**[LINK](LINK)**

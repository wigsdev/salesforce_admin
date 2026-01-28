# Salesforce Admin + Agent Force

## Daily
*   Del 1 al 10 cómo te sentís?
*   Qué te proponés para hoy?

> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## Skills Técnicas (El "Qué" haces)

*   **Gestión de Usuarios y Seguridad**: El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
*   **Gestión de Datos (Data Management)**: Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
*   **Automatización Básica (Flows)**: Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
*   **Reportes y Dashboards**: Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.
*   **AgentForce**: puedas familiarizarte con la configuración de agentes dentro de Salesforce.

> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## Skills Blandas (El "Cómo" lo haces)

*   **Comunicación Traducida**: Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
*   **Resolución de Problemas (Google-Fu)**: No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
*   **Mentalidad de Aprendiz (Learner's Mindset)**: Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
*   **Atención al Detalle**: Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.

> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## Normas de Convivencia

*   **COLABORACIÓN**: Aprender con y de otras personas
*   **AUSENCIAS**: Seguir con la planilla y actividades
*   **MIC o CHAT**: Comunicación
*   **ERRORES**: Atrasados
*   **JUEVES**: PREGUNTAS (Al final de la clase Teórica)
*   **AUTONOMÍA**: Utilizar las herramientas

---

# Reportes y Dashboards: Visualizando el Negocio

Vamos a ver la segunda parte de modelado de datos…

## La Base de Todo: Tipos de Informe y Formatos

### El Peligro Oculto: Dashboards y el "Running User"
Aquí es donde se confunden en el examen. Piensen en esto como un aeropuerto:
*   La **Matching Rule** es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
*   La **Duplicate Rule** es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

### Distribución: La Regla de las Carpetas
¿Qué hacemos si ya tenemos 1000 duplicados? No se borran uno por uno.
Usamos la herramienta de **Merge (Fusionar)**. Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.
**Nunca eliminen un duplicado sin revisar qué información histórica tiene.**

---

# Fundamentos de Analytics en Salesforce

## RETO 2: Crear un nuevo PlayGround

### Checklist Técnico para Aprobar el Challenge

#### 1. El Nombre del Reporte (La trampa #1)
*   **Requisito**: El nombre debe ser exactamente `Lead Source Report`.
*   **Error común**: Como el enunciado está traducido, los alumnos suelen nombrarlo "Informe de Fuente de Candidatos" o "Lead Source Reporte".
*   **Solución**: Copiar y pegar el nombre en inglés tal cual aparece en las instrucciones (`Lead Source Report`) en el campo "Report Unique Name" (Nombre único del informe). El validador de Trailhead busca ese string exacto.

#### 2. La Carpeta de Guardado (La trampa #2)
*   **Requisito**: Guardar en "Public Reports" (Informes públicos).
*   **Error común**: Salesforce selecciona por defecto la carpeta "Private Reports" (Mis informes personales). Si lo guardan ahí, el robot de Trailhead no podrá "ver" el reporte y marcará error.
*   **Solución**: Al momento de guardar, deben hacer clic en "Select Folder" (Seleccionar carpeta) y cambiar explícitamente a "Public Reports".

#### 3. Traducción de Campos (Ojo con "Fuente de plomo")
*   **Requisito**: Incluir el campo `Lead Source`.
*   **Aclaración Técnica**: El texto que pegaste dice "Fuente de plomo". Esta es una mala traducción automática. En una Org de Salesforce en español, el campo se llama "Origen del candidato". En inglés es "Lead Source".
*   **Instrucción**: Que no busquen "Plomo". Deben buscar el campo `Lead Source` (si la org está en inglés) u `Origen del candidato` (si está en español) y agregarlo a las columnas.

#### 4. El Filtro de Fecha (Para ver datos)
*   **Requisito**: Rango = `All Time` (Todo el tiempo).
*   **Error común**: Dejar el filtro predeterminado que suele ser "Current Fiscal Quarter" (Trimestre fiscal actual) o "Created Date".
*   **Solución**: Ir a la pestaña de FILTROS (Filters), buscar el filtro de Fecha de Creación (Created Date) y cambiar el rango a "All Time". Aunque el challenge dice "(no lo comprobaremos)", si el alumno no ve datos en la previsualización, pensará que hizo algo mal. Esto asegura que vean la lista de personas.

#### 5. Tipo de Informe Correcto
*   **Requisito**: Seleccionar `Leads` (Candidatos).
*   **Precaución**: No confundir con "Leads with converted lead information" o tipos de reportes personalizados. Deben elegir el estándar simple: `Leads`.

---

## RETO 3

#### 1. La Diferencia entre AND y OR (Expansión vs. Restricción)
*   **OR (O)**: Amplía la lista. Es inclusivo. "Quiero peras O manzanas" (Traeme cualquiera de las dos). En el reto: Queremos clientes de Energía O de Electrónica. Si usaran AND aquí, buscarían una empresa que sea de Energía y Electrónica al mismo tiempo, lo cual daría cero resultados.
*   **AND (Y)**: Reduce la lista. Es restrictivo. "Quiero peras Y que estén maduras". Ambas condiciones deben cumplirse obligatoriamente.

#### 2. El uso de Paréntesis (Agrupación)
*   **Teoría**: Al igual que en matemáticas, lo que está entre paréntesis se resuelve primero.
*   **En el reto**: `(1 OR 2)`
    *   Salesforce primero junta todas las empresas de Energía y todas las de Electrónica en un solo saco.
    *   Luego, a ese saco grande, le aplica el resto de las reglas.
*   **Sin paréntesis**: La lógica se leería de izquierda a derecha y podría mezclar condiciones erróneamente.

#### 3. El Operador NOT (Exclusión)
*   **Teoría**: A veces es más fácil decir lo que no quieres que listar todo lo que sí quieres.
*   **En el reto**: `AND NOT 4` (Y NO el filtro 4).
    *   El filtro 4 busca tipos "Estructurales". Al ponerle un NOT delante en la lógica, le estamos diciendo al reporte: "Si encuentras un caso Estructural, tíralo a la basura". Es un filtro de limpieza.

#### 4. El Orden de los Factores (Los Números)
*   **Teoría**: Los números 1, 2, 3, 4 en la lógica de filtro corresponden al orden en que crearon los filtros en la lista visual.
*   **Advertencia Técnica**: Si un alumno crea primero el filtro de "Estado" y luego el de "Industria", sus números serán diferentes (el Estado será el 1).
*   **Consejo para el alumno**: "Creen los filtros exactamente en el orden que pide la lista del ejercicio para que los números 1, 2, 3 y 4 coincidan con la fórmula lógica".

---

## RETO 4

#### 1. La Metamorfosis: De Tabular a Resumen (Summary)
*   **Teoría**: Por defecto, todo reporte nuevo nace siendo Tabular (una simple lista tipo Excel).
*   **El Reto**: El ejercicio pide explícitamente un "Summary Report" (Informe resumido).
*   **La Clave**: No existe un botón mágico que diga "Convertir a Resumen". Teóricamente, un reporte se convierte en "Resumido" en el momento exacto en que agrupas las filas por algún campo.
*   **Para el alumno**: "Si no agrupan, sigue siendo Tabular y el reto fallará. Agrupar es lo que cambia el formato".

#### 2. El Criterio de Agrupación (Grouping)
*   **Teoría**: Agrupar sirve para organizar datos bajo encabezados comunes.
*   **El Reto**: Roberto quiere ver la diferencia entre casos "Nuevos" y "Cerrados".
*   **La Clave**: Esos valores (New, Closed, Escalated) viven dentro del campo Status (Estado).
*   **Para el alumno**: "Para cumplir el requisito de 'ver rápidamente qué casos son nuevos y cuáles cerrados', deben arrastrar el campo Status a la sección 'Group Rows' (Agrupar filas)".

#### 3. El Alcance Temporal (Data Scope)
*   **Teoría**: Los filtros de fecha son restrictivos por defecto.
*   **El Reto**: Pide rango "All Time" (Todo el tiempo).
*   **La Clave**: Si dejan el filtro por defecto (que suele ser "Este mes fiscal"), es probable que el reporte salga vacío y piensen que hicieron algo mal.
*   **Para el alumno**: "Siempre cambien el filtro de fecha a 'Todo el tiempo' para asegurarse de que el reporte está leyendo toda la base de datos y no solo lo de hoy".

---

## RETO 5

#### 1. La Dependencia "Origen-Destino"
*   **Teoría**: Un Dashboard (Panel) es solo una cáscara vacía. No almacena datos por sí mismo; visualiza datos de un reporte existente.
*   **Aplicación en el Reto**:
    *   Es imposible hacer la segunda parte (Crear el Dashboard "Big Deals") si no han hecho y guardado primero la primera parte (El Reporte "Opportunities in Stages").
    *   El "Source Report" (Informe de origen) es el cimiento.

#### 2. La Regla de la Agrupación (Grouping)
*   **Teoría**: Para crear un gráfico (especialmente un Donut Chart o Gráfico de Anillos), el reporte de origen NO puede ser una lista plana (Tabular). Necesita tener datos resumidos.
*   **Aplicación en el Reto**:
    *   El reto pide un Donut Chart.
    *   Por eso, es obligatorio configurar en el reporte: `Group Rows by Stage` (Agrupar filas por Etapa).
    *   Si el alumno olvida agrupar, cuando intente agregar el gráfico en el Dashboard, Salesforce le dará un error o no le dejará seleccionar el gráfico de anillos.

#### 3. El concepto de "Widget"
*   **Teoría**: En el Generador de Paneles (Dashboard Builder), cada elemento visual (gráfico, número, tabla) se llama Widget (o Componente).
*   **Aplicación en el Reto**:
    *   El paso final no es "pegar" el reporte, sino agregar un Widget.
    *   Deben seleccionar tipo "Chart or Table" (Gráfico o Tabla).
    *   Luego seleccionar el reporte de origen.
    *   Y finalmente elegir el diseño visual: Donut Chart.

---

## Guía: Consultas y Práctica

Consultar si saben que es un administrador de Salesforce, si habian escuchado antes de rol.

### ¡Manos a la obra!
Avanzamos con los trails.

### LEER CON ATENCIÓN
Las prácticas previas al challenge son importantes para entender el challenge. **NO DEJARLAS PASAR.**

### ATENCIÓN

#### ERRORES
1.  Agotar herramientas
2.  Consultar con su grupo
3.  Hacer una nueva ORG
4.  Recién consultar a los profesores

#### CONSULTAS
*   Haber agotado todas las instancias de herramientas

#### Contexto
*   SB-Jueves

#### PAIR PROGRAMING
*   Compartir pantalla
*   Hablar sobre el proceso del Trailhead
*   Ir rotando
*   No se puede estar en silencio
*   El trabajo individual es fuera de la cursada

---

# Reportes y Dashboards - FAQs

[LINK](#)

## POSIBLES PREGUNTAS

**1. El botón gris: "¿Por qué no puedo agregar un gráfico?"**
*   **Alumno**: "Profe, estoy en el Report Builder, quiero poner un gráfico de barras, pero el botón 'Add Chart' está gris (deshabilitado). ¿Se rompió mi Salesforce?"
*   **Respuesta**: "No se rompió, ¡le falta estructura! Salesforce no puede graficar una lista plana de datos. Para activar el botón de gráficos, necesitas agrupar por al menos una columna (ej: Agrupar por 'Fase' o por 'Propietario'). En cuanto conviertes el reporte de 'Tabular' a 'Summary' (agregando un grupo), el botón se enciende mágicamente".

**2. El misterio de los registros faltantes (Tipos de Informe)**
*   **Alumno**: "Mi jefe quiere un reporte de 'Cuentas con Oportunidades'. Lo hice, pero faltan un montón de clientes nuevos que aún no nos han comprado nada. ¿Dónde están?"
*   **Respuesta**: "Elegiste el Report Type estándar 'Accounts with Opportunities'. El estándar hace un filtro estricto (Inner Join): Solo muestra Cuentas SI TIENEN Oportunidades. Para ver todas las cuentas (compren o no), necesitas crear un Custom Report Type que diga: 'Cuentas CON O SIN Oportunidades'. Es la diferencia entre ver solo las ventas cerradas o ver todo tu mercado potencial".

> **¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path.**
> No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'.
> Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso.

**3. Agrupar sin fórmulas (Bucket Fields)**
*   **Alumno**: "Necesito agrupar las ventas en 'Pequeñas', 'Medianas' y 'Grandes' según el monto. ¿Tengo que crear un campo de fórmula complejo en el objeto Oportunidad?"
*   **Respuesta**: "¡No ensucies el objeto para algo que es solo visual! Usa un **Bucket Column** (Campo de Cubo) directamente en el reporte. Es una herramienta del reporte que te permite definir rangos (ej: 0-1000 es 'Pequeña') sin tocar la configuración del objeto ni pedirle nada a un desarrollador. Es rápido y no afecta la base de datos".

**4. El riesgo del "Click-through" (Drill Down)**
*   **Alumno**: "Si configuro el Dashboard para que corra como el Director (Running User), un empleado junior puede ver los números totales de ventas. Pero si hace clic en el gráfico... ¿ve los registros detallados?"
*   **Respuesta**: "Depende, y aquí está la trampa. En el Dashboard ven la foto de los datos del Director (ej: Ventas Totales: $1M). Si hacen clic para ir al reporte fuente (Drill down), Salesforce intenta ejecutar el reporte con el usuario que está haciendo clic. Generalmente, ahí se aplica la seguridad y verán 'Acceso insuficiente' o una lista vacía. Pero el daño ya está hecho: Ya vieron el número total ($1M) que quizás era confidencial. ¡Cuidado con lo que muestran en la foto!"

**5. ¿Por qué no usamos siempre "Dynamic Dashboards"?**
*   **Alumno**: "Si los Dashboards Dinámicos (que se adaptan a quien los mira) son los más seguros, ¿por qué no ponemos todos así y nos olvidamos del problema?"
*   **Respuesta**: "Por los Límites de la Edición. Salesforce es estricto con los recursos. En la edición Enterprise (la más común en empresas grandes), solo te permiten tener 5 Dashboards Dinámicos en toda la organización. Úsalos solo para lo vital (ej: 'Mis Comisiones', 'Mi Rendimiento'). Para cosas generales de la empresa, usa dashboards estáticos".

**6. "Funciona en mi máquina" (Carpetas)**
*   **Alumno**: "Le mandé el link del reporte a mi compañera, ella tiene la misma licencia y perfil que yo, pero le dice 'Privilegios Insuficientes'. ¿Qué pasa?"
*   **Respuesta**: "El 99% de las veces, el problema es la **Carpeta**. Seguro guardaste el reporte en tu carpeta 'Private Reports'. Aunque ella sea Administradora, no puede ver tus cosas privadas fácilmente. Solución: Mueve el reporte a una carpeta Pública (o compartida con su Rol) y el link funcionará al instante".

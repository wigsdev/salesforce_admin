# Salesforce Admin + Agent Force

**Daily**
*   ¿Cuál es tu mayor temor o miedo de este curso?

> "Que tus ganas sean más grandes que tus miedos."

---

## Skills Técnicas y Blandas

### Skills Técnicas (El "Qué" haces)
*   **Gestión de Usuarios y Seguridad**: El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
*   **Gestión de Datos (Data Management)**: Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
*   **Automatización Básica (Flows)**: Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
*   **Reportes y Dashboards**: Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.

### Skills Blandas (El "Cómo" lo haces)
*   **Comunicación Traducida**: Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
*   **Resolución de Problemas**: No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
*   **Mentalidad de Aprendiz (Learner's Mindset)**: Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
*   **Atención al Detalle**: Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.

---

## Dinámica de Clase
*   **ERRORES**: No quedarse atrasados por miedo.
*   **PREGUNTAS**: Al final de la clase Teórica.
*   **COLABORACIÓN**: Aprender con y de otras personas.
*   **MIC o CHAT**: Comunicación activa.
*   **AUSENCIAS**: Seguir con la planilla y actividades.

---

## Quick Data Insights with Formulas
Utilice fórmulas para acceder, comprender y mostrar datos de diferentes maneras.

### Introducción y Concepto

**Definición**: Una fórmula en Salesforce es un campo de **"Solo Lectura"** que deriva su valor de otros campos, expresiones o valores.

**Analogía**: "Piensen en una fórmula de Salesforce como una celda de Excel que se actualiza automáticamente, pero aplicada a cada registro de su base de datos de forma individual".

**El Poder**: Nos permite transformar datos estáticos en información dinámica sin que el usuario tenga que escribir nada.

> "En el ecosistema Salesforce, prohibimos que el usuario use la calculadora del celular. Si tienen el 'Precio' y la 'Cantidad', Salesforce debe calcular el 'Total' solo."

**Concepto Clave (Dinámico)**: Si cambia el 'Precio', el 'Total' cambia solo al instante.

**Cross-Object (Span across relationships)**: Esto es vital. 'Span across relationships'. Permite aplanar la base de datos visualmente para que el usuario no tenga que hacer 3 clics para ver el teléfono del jefe de la empresa.

### Objetivos de Aprendizaje
1.  **Crear Campos de Fórmula** para calcular valores automáticamente (ej. Fechas de vencimiento, descuentos, concatenación de nombres).
2.  **Navegar entre Objetos**: Traer información de un objeto "Padre" al "Hijo" mediante fórmulas (Cross-Object Formulas).
3.  **Dominar las Funciones Lógicas**: Usar `IF`, `AND`, `OR` e `ISBLANK` para tomar decisiones dentro del dato.

### Puntos Teóricos Claves
*   **Tipos de Retorno (Return Type)**: Es vital definir qué tipo de dato va a devolver la fórmula (Check, Moneda, Fecha, Texto). Si la fórmula calcula dinero pero el retorno está en "Texto", no podrán sumar esos valores en un reporte.
*   **Recálculo en Tiempo Real**: Las fórmulas no se guardan en la base de datos como un valor fijo. Se calculan en el momento en que alguien abre el registro o ejecuta un reporte.

> Implicancia: Si cambias un campo que alimenta la fórmula, la fórmula se actualiza instantáneamente.

*   **Fórmulas Cross-Object**:
    *   Pueden "subir" hasta 10 niveles de relaciones (ej. Desde Caso > ver el Manager del Dueño de la Cuenta).
    *   *Limitación*: No pueden "bajar" a ver registros hijos (ej. Desde Cuenta no puedes sumar Oportunidades con una fórmula simple, necesitas Roll-Up Summary).

### Tips "Pro" (Secretos de Consultor)

> Estos tips diferencian a un Admin Junior de un Arquitecto:

1. **El Poder de `BLANKVALUE`**: En lugar de hacer un `IF(ISBLANK(Campo), "Valor", Campo)`, enséñales a usar `BLANKVALUE(Campo, "Valor")`. Ahorra caracteres y procesa más rápido.
2. **Cuidado con los Límites (Compile Size)**: Las fórmulas tienen un límite de tamaño de compilación (5,000 bytes). Si anidan muchos IF dentro de otros IF, explotará.
    *   *Solución*: Usar la función `CASE()` siempre que sea posible en lugar de múltiples IF
*   **El "Truco del Hyperlink"**: Las fórmulas de texto pueden contener imágenes o botones. Pueden crear una fórmula que muestre una bandera roja 🚩 si una cuenta está en riesgo, usando la función `IMAGE()`. Eso a los clientes les encanta visualmente.

### Importancia en el Proyecto Real
- **Calidad de Datos (Single Source of Truth):** Evita errores humanos. Si el descuento depende del volumen de compra, la fórmula lo aplica exacto. Si lo hace una persona, se puede equivocar.
- **Simplificación de Automatizaciones:** Antes de crear un Flow complejo, pregúntate: ¿Puedo hacer esto con una fórmula? Las fórmulas son más ligeras y rápidas para el sistema que los Flows o Triggers.
- **Integraciones:** A menudo los sistemas externos necesitan un ID único o un formato de fecha específico. Creamos fórmulas "puente" para transformar nuestros datos al formato que el otro sistema necesita sin ensuciar el dato original.

---

## Validation Rules

Aprenda a mantener la calidad de los datos en Salesforce implementando la validación de datos.

### Reglas de Validación: Los "Porteros" de nuestra Base de Datos.

El objetivo de hoy no es solo aprender a escribir una fórmula, sino entender cómo garantizar la integridad de los datos desde la entrada. 

Una Regla de Validación es el mecanismo que impide que entre 'basura' al sistema, asegurando que si un dato se guarda, es porque cumple con nuestros estándares de calidad.

### LÓGICA INVERSA

Rojo = TRUE, Verde = FALSE
A diferencia de lo que dice la intuición, en Salesforce la fórmula busca el **ERROR**, no el éxito.
*   Si la fórmula da **TRUE (Verdad)** → Salesforce **DETIENE** al usuario y muestra el error.
*   Si la fórmula da **FALSE (Falso)** → Salesforce **PERMITE** guardar.

> "Piensen en la Validación como un detector de minas. La fórmula busca la mina. Si escribo: `Fecha_Cierre < HOY`. ¿Es error? Sí. Entonces, si es VERDAD, Salesforce grita ERROR."

En el ecosistema Salesforce, prohibimos que el usuario use la calculadora del celular. Si tienen el 'Precio' y la 'Cantidad', Salesforce debe calcular el 'Total' solo.

**Concepto Clave:** Expliquen que la fórmula es **Dinámica**. Si cambia el 'Precio', el 'Total' cambia solo al instante.

**Cross-Object:** Esto es vital. 'Span across relationships'. Permite aplanar la base de datos visualmente para que el usuario no tenga que hacer 3 clics para ver el teléfono del jefe de la empresa.

### Componentes de la Regla
1.  **Condición de Error**: La fórmula lógica (`AND`, `OR`, `NOT`, `ISBLANK`).
2.  **Mensaje de Error**: El texto que ve el usuario (¡Clave para la experiencia de usuario!).
3.  **Ubicación**: ¿Arriba de la página o al lado del campo? (Recomendación: Siempre al lado del campo si es un solo campo; arriba si es una combinación compleja).

### Funciones "Salvavidas"
*   `ISNEW()`: Para reglas que solo apliquen al crear, no al editar.
*   `ISCHANGED()`: Para bloquear cambios en campos sensibles una vez establecidos.
*   `PRIORVALUE()`: Para comparar con lo que había antes (ej. "No puedes bajar el precio si ya estaba aprobado").
*   `VLOOKUP()`: (Menciónala brevemente como "la única regla que busca datos en otros registros", exclusiva de objetos personalizados).

### TIPS
1. **El "Boton de Pánico" (The Bypass Switch):**

- *El problema:* Si creas una regla estricta hoy, mañana cuando quieras cargar 10,000 registros viejos con Data Loader, fallarán todos porque no cumplen la regla nueva.
- *El Tip:* Siempre incluye en tu fórmula una "puerta trasera" para administradores.
    - Fórmula: AND( Condición_Error, $Permission.Bypass_Rules = FALSE )
    - Esto permite que tú, como admin, te saltes las reglas para migraciones de datos o arreglos masivos sin desactivar la regla para todos los usuarios.

2. **Nunca uses IDs fijos (Hardcoding):**

- *El problema:* ProfileId = '00e40000000abc'
- *Por qué falla:* Ese ID cambia entre Sandbox y Producción. Tu regla funcionará en pruebas y romperá todo en vivo.
- *El Tip:* Usa Profile.Name o mejor aún, **Custom Permissions**.

3. **La regla del "Usuario Frustrado":**
- No pongas mensajes de error robóticos como "Error de validación: Datos incorrectos".
- Escribe instrucciones: "El DNI debe tener 8 dígitos y no contener letras". El mensaje de error es parte del entrenamiento del usuario.


### Aplicación en un Proyecto Laboral

**Escenario 1: Calidad de Reportes (Sales & Marketing)**
- "Si no usamos reglas de validación en el campo 'Correo Electrónico' o 'Provincia', nuestros reportes de marketing no servirán. Las reglas aseguran que la segmentación de clientes sea real y no tengamos 5 formas distintas de escribir 'Buenos Aires'."

**Escenario 2: Cumplimiento de Procesos (Service/Soporte)**
- "Podemos usar reglas para obligar a los agentes a llenar ciertos campos solo cuando cambian el estado del caso. Ejemplo: No puedes poner un Caso en 'Cerrado' si el campo 'Solución' está vacío. Esto fuerza el cumplimiento del proceso operativo sin necesidad de un supervisor detrás."

**Escenario 3: Seguridad Financiera**
- "Evitamos pérdidas bloqueando descuentos excesivos. Una regla puede impedir que un vendedor aplique más del 20% de descuento sin que el campo 'Aprobación del Gerente' esté marcado."


---

## Evaluate Report Data with Formulas

**Objetivos de Aprendizaje**:
- Distinguir cuándo usar una fórmula a nivel de fila (registro por registro) vs. una fórmula de resumen (grupo de registros).
- Calcular métricas de negocio complejas (como tasas de conversión o promedios ponderados) sin ensuciar la base de datos con campos nuevos.
- Visualizar estos cálculos numéricos en gráficos de Dashboards.

> - El error número 1 que van a ver en fórmulas es 'Esperaba Texto, recibió Número'. Salesforce es estricto. No pueden sumar 'Manzanas' + 5.
> - La función TEXT() es su traductor. Convierte el número 500 en la palabra '500' para que puedan escribir 'El total es 500'.
> - La función VALUE() es al revés. Si importan datos de un Excel y Salesforce cree que el precio es texto, VALUE() lo vuelve operable matemáticamente.

### Puntos Teóricos Claves
**El Requisito de Oro:** Para activar una Fórmula de Resumen, el reporte DEBE tener al menos una agrupación (filas o columnas). En un reporte tabular simple no existen.

**El Alcance (Scope):**

- *Row-Level:* Calcula A + B en cada línea (Ej: Precio - Costo).
- *Summary Formula:* Calcula el resultado de un grupo entero (Ej: Total Ganado / Total Cerrado).

**Tipos de Datos:** Solo devuelven números, moneda o porcentaje. No devuelven texto ni fechas.

**Visualización:** Puedes elegir dónde se muestra el número: ¿En todas las filas? ¿Solo en el gran total? ¿Solo en el subtotal del vendedor?

> "En matemáticas del colegio, 2.3 se redondea a 2. En los negocios, no siempre.
Imaginen que vendemos pintura. El cálculo dice que el cliente necesita 4.1 latas para pintar su casa. No podemos venderle 0.1 lata. Tenemos que venderle 5 latas completas. Ahí usamos CEILING().
Si usamos ROUND(), le venderíamos 4 y se quedaría sin pintura a la mitad de la pared. Elegir la función incorrecta puede costar dinero real a la empresa."

### Tips "Pro" (Lo que no dice Trailhead)

- **Higiene de Metadata:** "Si el cálculo solo sirve para un reporte mensual, NO crees un campo en el objeto". Enséñales a no crear deuda técnica. Las Fórmulas de Resumen mantienen la org limpia.
- **Limpieza Visual (Display Tab):** Por defecto, la fórmula se repite en cada fila del grupo, lo que hace "ruido". Enséñales a usar la pestaña "Display" dentro del editor de fórmulas para mostrar el resultado solo en el Encabezado o Gran Total.
- **La trampa del NULL:** Si dividen por cero (ej. un vendedor sin oportunidades cerradas), la fórmula puede dar error. Recomienda usar lógica simple o saber que Salesforce suele manejar esto mostrando un guión, pero es vital validar los datos.
- **Límite de 5:** Solo se permiten 5 fórmulas de resumen por reporte. Si necesitan más, es señal de que deben usar CRM Analytics o un Dashboard más complejo.

## Aplicación en un Entorno Laboral Real

**Caso Ventas (Win Rate - El del reto):**
- *Necesidad:* El Director no quiere ver el monto total. Quiere saber quién es más efectivo.
- *Fórmula:* WON:SUM / CLOSED:SUM (Total Ganado entre Total Cerrado).

**Caso Soporte (SLA Breach):**
- *Necesidad:* ¿Qué porcentaje de casos de un agente se cerraron tarde?
- *Fórmula:* (Casos Fuera de SLA / Total de Casos) * 100.

**Caso Calidad de Datos:**
- *Necesidad:* Detectar qué equipos dejan campos vacíos.
- *Fórmula:* Sumar registros con campos vacíos y dividir por el total para sacar un "% de Error".

--- 
### TIPS: Visualizaciones en Reportes

### Outline vs. Filters
1. **OUTLINE (Esquema) = La Estructura (QUÉ y CÓMO)**

- *Concepto:* Define la "forma" y el contenido visible de la tabla.
- *Pregunta clave:* ¿Qué columnas quiero leer? ¿Cómo quiero agruparlas?
- *Acciones:* 
    *   Agregar/Quitar Columnas (Campos).
    *   Agrupar Filas (Para hacer resúmenes).
    *   Agrupar Columnas (Para matrices).

2. **FILTERS (Filtros) = El Criterio (QUIÉN y CUÁNDO)**

- *Concepto:* Define el "alcance" de los datos. Recorta la base de datos.
- *Pregunta clave:* ¿Qué registros cumplen con mis requisitos?
- *Acciones:* 
    *   Rango de Fechas (ej. "Este mes").
    *   Condiciones lógicas (ej. "Estado = Cerrado").
    *   Dueño del registro (ej. "Mis casos").

---

## El Menú de Columna: Control Total en un Clic**

**Puntos clave visuales:**

1. **Orden Inmediato (Sort & Move):** Organiza la data sin perder tiempo.
2. **El Poder de Agrupar (Group Rows):** La función que transforma una "lista" en un "reporte real".
3. **Herramientas Avanzadas (Bucketing):** Crear categorías nuevas sin fórmulas.

---
## OPCIONES

**Puntos Clave:**
1. **Row Counts (Conteo de Filas):** ¿Cuántos registros hay? (El número entre paréntesis).
2. **Detail Rows (Filas de Detalle): EL MÁS IMPORTANTE.** Muestra u oculta los registros individuales.
3. **Subtotals (Subtotales):** La suma parcial de cada grupo.
4. **Grand Total (Total General):** La suma final de todo el reporte.

---

## REFRESH vs UPDATE PREVIEW

1. Update Preview Automatically (El Interruptor)

    - Qué es: El modo "Piloto Automático".
    - Cómo funciona: Cada vez que agregas una columna, un filtro o mueves algo, Salesforce recarga la tabla inmediatamente.
    - Ventaja: Ves el resultado de tus cambios al instante.
    - Desventaja: Si tu internet es lento o el reporte es muy complejo, se "congela" unos segundos cada vez que haces clic.
2. Refresh (La Advertencia Naranja)
    - Qué es: El modo "Manual". Aparece cuando el interruptor de arriba está apagado.
    - Cómo funciona: Puedes hacer 10 cambios seguidos (agregar 5 columnas y 3 filtros) sin que pase nada. Solo cuando terminas, le das a Refresh y se carga todo junto.
    - Ventaja: Es mucho más rápido para construir reportes grandes porque no esperas a que cargue entre cada clic.

---

> "La función MOD parece inútil al principio ('¿A quién le importa el resto de una división?').\
Pero es la base para distribuir trabajo equitativamente.\
Imaginen que tienen 3 vendedores. Toman el número de Lead, aplican MOD(LeadNumber, 3) y el resultado siempre será 0, 1 o 2.
- Si sale 0 → Se lo damos al Vendedor A.
- Si sale 1 → Al Vendedor B.
- Si sale 2 → Al Vendedor C.

Con una simple fórmula matemática, crearon un sistema de reparto de ventas justo."


## ¡Manos a la obra!

**Avanzamos con los trails.**

### ATENCIÓN

#### LEER CON ATENCIÓN

*   Las prácticas previas al challenge son importantes para entender el challenge. **NO DEJARLAS PASAR**.

#### ERRORES
* Agotar herramientas
* Consultar con el grupo
* Hacer una nueva ORG
* Recién consultar a profesores

#### CONSULTAS

* Haber agotado todas las instancias de herramientas
* Contexto
* SB-Jueves

### Fórmulas y Validades [Entrar aquí](https://trailhead.salesforce.com/es-MX/modules/point_click_business_logic)

#### PAIR PROGRAMING
*   Compartir pantalla.
*   Hablar sobre el proceso del Trailhead.
*   Ir rotando.
*   El trabajo individual es fuera del grupo.

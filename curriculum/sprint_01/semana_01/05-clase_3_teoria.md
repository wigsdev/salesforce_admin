# Salesforce Admin + Agent Force

**Daily**
*   ¿Cómo venimos?
*   ¿Algo nos bloquea?
*   ¿Cómo seguimos?

### Dinámica de trabajo
*   **EN PARALELO**: No distraerse con otras tareas.
*   **CONEXIÓN**: Se saca de la reunión a los que no respondan.*   **PREGUNTAS**: Anotar en un cuaderno. Al final de la clase.
*   **MICRÓFONO APAGADO**: Cuando no hablamos.
*   **CÁMARA PRENDIDA**: En los grupos.
*   **COMPROMISO**: Asistencia, atención y puntualidad.

---

## ¡Manos a la obra!
Avanzamos con los trails.

---

## SPRINT 1: Picklist

### Estandarización de Datos (Picklists)

**Concepto**: La base de datos es tan útil como limpios sean sus datos. El texto libre es el enemigo de los reportes.

**Teoría**: Una Lista de Selección (Picklist) no es solo un menú cómodo; es una restricción de integridad. Obliga a que todos hablen el mismo idioma.

### Punto Clave: 
- Global Value Sets (Conjuntos de Valores Globales)
"Reutilización".

    Si tienes una lista de Países en Cuentas y otra en Candidatos, y mañana nace un país nuevo, no quieres editar 20 listas. Creas un Conjunto Global (la "lista maestra") y todos los objetos la heredan. Es eficiencia de mantenimiento.

---

## SPRINT 1: Lógica interfaz condicional

### Dependencias de Campo

**Concepto**: No abrumar al usuario con opciones irrelevantes. La interfaz debe reaccionar a lo que el usuario elige.

**Teoría**: Existe una relación jerárquica entre campos en la interfaz (UI).
*   **Campo de Control (Controlling)**: El que manda (El filtro).
*   **Campo Dependiente**: El que obedece (El resultado filtrado).

**Analogía**: Es como un menú de restaurante. Si eliges "Bebidas" (Control), el submenú solo te muestra "Agua, Coca, Vino", no te muestra "Pizza". Salesforce hace esto para evitar errores lógicos (ej. Elegir Continente: Europa y País: Argentina).

---

## SPRINT 1: Fórmulas

### Datos Derivados (Fórmulas)

**Concepto**: Hay datos que no deberían ingresarse manualmente porque ya existen en otra parte o se pueden calcular matemáticamente.

**Teoría**: Una fórmula es Dinámica y de Solo Lectura.
- No se guarda en la base de datos como un número fijo; se calcula en el momento que abres el registro (On-the-fly).

**El "Superpoder" (Cross-Object Formulas)**: Este es el concepto más importante. Las fórmulas pueden "saltar" de un objeto a otro a través de relaciones.

- **Ejemplo**: Una Oportunidad puede "mirar" a la Cuenta relacionada y traer el campo "Región" sin que el usuario tenga que copiar y pegar. Esto se llama *Span across relationships*.

---

## SPRINT 1: Integridad

### Integridad de Datos e Inversión Lógica (Reglas de Validación)

**Concepto**: "Garbage In, Garbage Out" (Basura entra, basura sale). Necesitamos un "portero" que frene los datos malos antes de que entren a la base de datos.

**Teoría (El obstáculo mental)**: La Lógica Inversa.
- A diferencia de los flujos o procesos donde configuras "Cuándo debe pasar algo", en una Regla de Validación configuras "Qué es un Error".

- Si la fórmula da TRUE (Verdadero), Salesforce DETIENE al usuario.

- **Ejemplo para clase**: "Si quieres bloquear descuentos mayores al 20%, tu fórmula debe buscar el error: Descuento > 0.20. Si esto es verdad, ERROR".

---

## SPRINT 1: VS

### Obligatoriedad Condicional (vs. Page Layouts)

**Concepto**: A veces un campo es obligatorio siempre, pero a veces solo es obligatorio bajo ciertas condiciones.

**Diferenciación Teórica**:
*   **Page Layout (Obligatorio en UI)**: El campo siempre tiene asterisco rojo. No importa qué pase.
*   **Regla de Validación (Obligatorio Lógico)**: El campo es obligatorio solo si se cumple una lógica de negocio (ej. "El DNI es obligatorio solo si el Cliente es una Persona Física, no si es una Empresa").

---

## SPRINT 1: Configuración global

### Company Settings: Definiendo el ADN de tu Salesforce

**Perfil de la Compañía (Company Information)**
*   **Identidad**: Nombre, Dirección y Contacto Principal.
*   **Recursos Críticos**: Espacio de Almacenamiento (Data vs. File) y Licencias de Usuario disponibles.
*   **Identificador Único**: Tu Salesforce Org ID (Vital para soporte).

---

## SPRINT 1: Configuración global

### Configuración Financiera (Fiscal Year & Currencies)

**Año Fiscal**:
*   **Estándar**: Sigue el calendario gregoriano (ej. Ene-Dic).
*   **Personalizado (Custom)**: Estructuras complejas (ej. 4-4-5). ¡Cuidado! Una vez activado, no hay vuelta atrás.

**Monedas**:
*   **Simple**: Una sola moneda para toda la empresa.
*   **Multi-Currency**: Permite vender en USD, EUR, etc. Requiere definir una "Moneda Corporativa" y tablas de conversión.

---

## SPRINT 1: Configuración global

### Localización y Horarios (Locale & Business Hours)

*   **Configuración Regional**: Idioma predeterminado, Zona Horaria y Formato de Fecha/Número (Locale).
    *   *Nota*: Los usuarios pueden anular esto con su configuración personal.
*   **Horarios de Negocio y Feriados**: Define cuándo trabaja tu equipo de soporte. Afecta directamente a los Escalation Rules (Reglas de escalación de casos).

---

## Configuración y uso

[Ingresar aquí](https://trailhead.salesforce.com/es-MX/users/rebecaduran/trailmixes/teoria-modelado-de-datos-ii-calidad)

**¡Buen Comienzo!**

Les señalamos la funcionalidad de renombrarse para llamarlos/as como quieran que se dirijan a ellos/as.
Como son muchas personas, la Encuesta es un buen método para que todo el mundo participe.
*   ¿Dónde viven?, ¿qué es lo que más les gusta hacer?, ¿alguno/a trabaja, de qué?, ¿alguno/a estudia, qué? ¿Qué emoji usan más en Whatsapp?...

Pueden resaltar algunas respuestas e invitar, a quienes se animen, a encender el micrófono y explicar su respuesta, buscando que interactúen entre 4 y 5 estudiantes.

---

## Modelado de datos: Repaso

**Guía**: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol.

"El modelado de datos en Salesforce es el proceso de estructurar y organizar la información de una empresa mediante la definición de objetos, campos y relaciones. Este enfoque permite representar de manera lógica y eficiente los datos dentro de la plataforma, facilitando su gestión y utilización."

### Importancia del modelado de datos
1. **Estructuración de la información:** Al definir objetos y campos, se establece una base sólida para almacenar datos de manera coherente, lo que facilita su acceso y comprensión.
2. **Relaciones entre datos**: El modelado permite establecer conexiones entre diferentes conjuntos de datos, reflejando las interacciones y dependencias reales dentro de la organización.
3. **Personalización y escalabilidad**: Una estructura de datos bien diseñada permite adaptar Salesforce a las necesidades específicas de la empresa y escalar conforme esta crece.
4. **Optimización de procesos**: Al tener datos organizados y relacionados adecuadamente, se mejora la eficiencia en procesos como la generación de informes, automatización de tareas y análisis de información.

---

## Tipos de Objetos en Salesforce

### 1. Objetos Estándar
Estos objetos vienen predefinidos por Salesforce y son comunes para la mayoría de las organizaciones. Se utilizan para registrar información básica que es esencial para los procesos comerciales habituales.

**Ejemplos de objetos estándar**:
*   **Account (Cuenta)**: Registra información sobre las organizaciones con las que haces negocios.
*   **Contact (Contacto)**: Almacena detalles de las personas asociadas con cuentas.
*   **Opportunity (Oportunidad)**: Rastrea posibles ventas o acuerdos.
*   **Lead**: Gestiona prospectos que podrían convertirse en clientes.
*   **Case (Caso)**: Almacena información de solicitudes de soporte o problemas de clientes.

**Características de los objetos estándar**:
*   No puedes eliminarlos ni cambiar su estructura principal, pero puedes personalizarlos con campos adicionales y reglas.
*   Tienen funcionalidades preconfiguradas, como la integración con el sistema CRM de Salesforce.

### 2. Objetos Personalizados
Estos son objetos que los usuarios pueden crear para satisfacer necesidades específicas de su organización. Se utilizan cuando los objetos estándar no son suficientes para gestionar un tipo de datos particular.

**Ejemplos de objetos personalizados**:
*   **Pedido**: Si una empresa necesita gestionar órdenes de compra.
*   **Proyecto**: Para gestionar la información de proyectos internos o externos.
*   **Evento**: Si se requiere registrar información sobre actividades personalizadas.

**Características de los objetos personalizados**:
*   Totalmente configurables: puedes definir los campos, las relaciones y las reglas.
*   Tienen el sufijo `__c` en el código para diferenciarlos de los objetos estándar.
*   Permiten el uso de funcionalidades avanzadas, como páginas Visualforce, Lightning Components y Apex Triggers para personalización adicional.

Diferencias entre objetos Estandar y Custom

| Características | Objetos Estándar | Objetos Personalizados |
| :--- | :--- | :--- |
| **Definición** | Incluidos en Salesforce por defecto (Out-of-the-box). | Creados por el administrador para necesidades específicas. |
| **API Name** | Sin sufijo (ej. `Account`, `Contact`). | Terminan en `__c` (ej. `Inmueble__c`). |
| **Eliminación** | No se pueden borrar. | Sí se pueden borrar (si no tienen dependencias bloqueantes). |
| **Personalización** | Limitada (se pueden agregar campos pero no cambiar su esencia). | Totalmente configurables (Campos, Relaciones, Layouts). |
| **Propósito** | Procesos de negocio comunes (Ventas, Servicio, Marketing). | Procesos únicos de la empresa (ej. Gestión de Flota, Proyectos). |



---

## Campos en Salesforce

Los campos son los componentes básicos de los objetos en Salesforce. Funcionan como las columnas de una tabla en una base de datos, almacenando valores específicos para cada registro en el objeto.

Cada campo tiene un tipo de dato asociado, que determina el tipo de información que puede almacenar (como texto, número, fecha, etc.).

### 1. Campos Estándar
Estos campos vienen predefinidos en los objetos estándar de Salesforce y no se pueden eliminar. Algunos pueden ser personalizados en términos de etiquetas o visibilidad, pero su estructura básica no se puede cambiar.

**Ejemplos en el objeto Cuenta**:
*   **Account Name (Nombre de cuenta)**: Captura el nombre de la empresa.
*   **Industry (Industria)**: Selecciona el sector comercial de la cuenta.
*   **Created Date (Fecha de creación)**: Indica cuándo se creó el registro.
*   **Owner (Propietario)**: Identifica al usuario asignado al registro.

**Características de los Campos Estándar**:
*   No tienen sufijos especiales en su nombre.
*   Están optimizados para usos comunes.
*   Algunos campos estándar están vinculados a funcionalidades del sistema, como el seguimiento de auditoría.

### 2. Campos Personalizados
Son campos creados por los usuarios para satisfacer necesidades específicas de la organización. Estos se añaden a los objetos estándar o personalizados para almacenar datos adicionales.

**Ejemplos**:
*   **Fecha de renovación del contrato**: Campo de tipo fecha.
*   **Estado de aprobación**: Campo de tipo lista de selección.
*   **Notas internas**: Campo de tipo texto largo.

**Características de los Campos Personalizados**:
*   Se identifican con el sufijo `__c`.
*   Pueden configurarse con:
    *   Reglas de validación.
    *   Relaciones con otros objetos.
    *   Ayuda contextual (descripción).

### Diferencias entre campos Estándar y Custom

| Características | Campos Estándar | Campos Personalizados |
| :--- | :--- | :--- |
| **Origen** | Predefinidos por Salesforce. | Creados por la organización. |
| **API Name** | Sin sufijo (ej. `Industry`). | Terminan en `__c` (ej. `Interes__c`). |
| **Eliminación** | No se pueden eliminar. | Se pueden eliminar. |
| **Etiqueta (Label)** | Se puede cambiar. | Se puede cambiar. |
| **Tipo de Dato** | Fijo (no se puede cambiar). | Fijo tras crearse (con algunas excepciones). |

---

## Tipos de datos

En Salesforce, los tipos de datos determinan el formato y el tipo de información que se puede almacenar en un campo. Al configurar un campo, es importante elegir el tipo de dato adecuado para garantizar que los datos se capturen correctamente y se comporten como se espera.

## Principales Tipos de Datos para Campos en Salesforce

| Tipo de Dato | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **Texto** | Almacena cadenas de caracteres. | Nombre, dirección. |
| **Número** | Permite ingresar números. | Cantidad de empleados. |
| **Moneda** | Almacena valores monetarios. | Ventas anuales. |
| **Fecha/Fecha-Hora** | Captura fechas con o sin horas. | Fecha de nacimiento, cita. |
| **Lista de selección** | Campo desplegable con opciones predefinidas. | Industria, estado de aprobación. |
| **Casilla de verificación** | Campo de tipo booleano (verdadero/falso). | Activo (Sí/No). |
| **Fórmula** | Calcula un valor basado en otros campos. | Total = Precio × Cantidad. |
| **Relación** | Vincula registros entre objetos. | Cuenta asociada a Contacto. |


### Datos básicos y numéricos

| Tipo de Dato | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| **Texto (Text)** | Almacena cadenas de caracteres. | Nombre, dirección. |
| **Número (Number)** | Almacena valores numéricos sin decimales. | Cantidad de productos, edad. |
| **Moneda (Currency)** | Valores monetarios con decimales. | Ventas anuales, presupuesto. |
| **Porcentaje (Percent)** | Valores en formato porcentual. | Descuentos, tasas de interés. |


### Fechas, booleanos y selección

| Tipo de Dato | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| **Fecha (Date)** | Almacena solo la fecha. | Fecha de nacimiento. |
| **Fecha/Hora (DateTime)** | Almacena fecha y hora. | Hora de una reunión o cita. |
| **Casilla de Verificación (Checkbox)** | Booleano: verdadero o falso. | Activo/Inactivo. |
| **Lista de Selección (Picklist)** | Desplegable con opciones predefinidas. | Estado de un caso, tipo de industria. |
| **Lista de Selección Multivalor (Multi-Select Picklist)** | Permite elegir varias opciones. | Idiomas hablados. |

### Relacionales y textuales avanzados

| Tipo de Dato | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| **Relación de Búsqueda (Lookup)** | Vincula registros entre objetos. | Contacto asociado a una cuenta. |
| **Relación Maestro-Detalle (Master-Detail)** | Crea una relación jerárquica más estricta. | Oportunidad vinculada a un producto. |
| **Área de Texto (Text Area)** | Permite texto corto (hasta 255 caracteres). | Comentarios, descripciones breves. |
| **Área de Texto Largo (Long Text Area)** | Almacena hasta 131,072 caracteres. | Notas detalladas, descripciones largas. |
| **Área de Texto Enriquecido (Rich Text Area)** | Texto con formato como negritas o enlaces. | Detalles con formato HTML. |

### Especiales y geográficos

| Tipo de Dato | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| **Correo Electrónico (Email)** | Campo para ingresar una dirección válida de correo. | Contacto de un cliente, usuario. |
| **Teléfono (Phone)** | Acepta números de teléfono en varios formatos. | Teléfono de contacto. |
| **URL** | Almacena enlaces web. | Sitio web de la empresa. |
| **Geolocalización (Geolocation)** | Almacena coordenadas geográficas (latitud y longitud). | Ubicación de un cliente. |
| **Archivo (File)** | Permite adjuntar archivos al registro. | Facturas, contratos. |

### Uso Estratégico de Tipos de Datos (Las 4 primeros clases)
1.  **Validez de Datos**: Elegir el tipo adecuado asegura que los datos se capturen en el formato correcto.
    *   *Ejemplo*: Usar Fecha para el nacimiento de un cliente en lugar de un campo de texto. Usar Moneda para valores financieros.
2.  **Optimización de Procesos**: Algunos tipos de datos, como Fórmulas y Relaciones, permiten automatizar cálculos y conexiones entre datos, mejorando la eficiencia.
3.  **Flexibilidad**: Campos como Lista de Selección Multivalor y Área de Texto Enriquecido permiten personalizar la captura de datos según necesidades específicas.
4.  **Visualización y Reportes**: Tipos como Porcentaje o Geolocalización enriquecen los informes y dashboards al proporcionar datos visuales o geográficos.

**Diferencias Clave entre Tipos de Datos**
*   **Campos Numéricos**: Manejan cantidades o valores medibles, ideales para cálculos.
*   **Campos Textuales**: Se utilizan para información descriptiva o identificadores únicos.
*   **Campos de Relación**: Vinculan datos entre objetos para representar conexiones empresariales.
*   **Campos Especiales**: Como Área de Texto Enriquecido o Geolocalización, ofrecen capacidades avanzadas para datos específicos.

> **Recomendación**: Seleccionar el tipo de dato adecuado es esencial para mantener la integridad de los datos, optimizar la entrada y facilitar la generación de reportes precisos. Siempre se debe considerar la naturaleza del dato y cómo será utilizado en los procesos empresariales.

---

## Generador de Esquemas (Schema Builder)
El Generador de Esquemas (Schema Builder) es una herramienta visual en Salesforce que permite a los usuarios ver y gestionar el modelo de datos de su organización de una manera intuitiva y gráfica. Con esta herramienta, es posible configurar objetos, campos y relaciones de manera directa, simplificando el diseño y la comprensión de la estructura de datos.

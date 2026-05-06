Salesforce
Admin +
Agent Force

HOY

EJERCICIO
No pueden cargar el formulario fuera de fecha
Tienen que subir la evidencia que es el resultado de cada ejercicio (Screenshot)
Hay corrección
No es quien termina más rápido es quien lo resuelve en el transcurso del día
Pueden utilizar la IA


Hay premio por participación

Trails al día
Ejercicios al dia

🎁



🎁
Acceso a Focus and Force





TIPOS DE DATOS EN APEX
Tipos Primitivos:
Integer, Double, Long, Date, Datetime, String, Boolean
ID: Identificador de registro de 18 caracteres en la plataforma Lightning.

TIPOS DE DATOS EN APEX
Valores y Referencias:
Todas las variables se inicializan como nulas por defecto.
Las cadenas se tratan como tipos de valor primitivo en Apex, a diferencia de .NET donde son referencias.

RETO:
Crear una clase de Apex que devuelva cuentas
Cree una clase de Apex que devuelva una lista de objetos Account para un estado de usuario especificado.
Cree una clase de Apex que contenga un método estático:
Nombre: AccountUtils
Nombre del método: accountsByState
El método debe devolver el ID y el nombre de todos los objetos Account que coincidan con BillingState para la abreviatura del estado pasado al método
ENVIAR EL DEBUG ONLY COMO SCREEN SHOT

EQUIPOS
SPRINT 3

CHECKLIST SPRINT 3


Proyecto
Aplicación en el Portal (Experience Cloud)
Novabank
Portal de Clientes: Consulta de estado de tarjetas/préstamos, artículos de prevención de fraude y chat de soporte para emergencias financieras.
Vitacore
Portal del Paciente: Gestión de turnos, artículos de bienestar y formularios de autogestión para reintegros o consultas médicas.
Lumina Tech
Partner Central / Help Desk: Registro de leads por parte de distribuidores o levantamiento de tickets técnicos cuando el software reporta fallas.
vamos a ver la segunda parte de modelado de datos… 



Daily
Daily
Daily
Daily


CHECKLIST SPRINT 1


Modelado de Datos
Todos los objetos necesarios declarados en el Sprint 1 
Creación de App
Logo, colores y formatos de diseño
Formularios 
Lightning page, page layouts
Gestión de Usuarios y Permisos
Creación de Usuarios y acceso a la información

vamos a ver la segunda parte de modelado de datos… 



CHECKLIST SPRINT 2


Carga Masiva de Datos
Haber podido subir al menos 500 Registros
Haber limpiado los excel
Tener data concreta
Reportes y Dashboards
Reportes requeridos por el cliente
Dashboards requeridos por el cliente
Automatizaciones
1 Screen Flow
1 Trigger Flow
1 Schedule Flow
vamos a ver la segunda parte de modelado de datos… 



PARTICIPACIÓN
EQUIPO 1
ROBERT
LAURA
KARLA
EQUIPO 2
HECTOR
PATZY
MARIBEL
EQUIPO 3
WILMER
IRAYDA
LINDBERG

EMPIEZAN HOY!

QUÉ HACEMOS HOY?
1-Trabajar en HU
2-Trails atrasados


¡Manos a la obra!
Avanzamos con los trails.



retro




HOY

CHECKLIST SPRINT 1


Modelado de Datos
Todos los objetos necesarios declarados en el Sprint 1 
Creación de App
Logo, colores y formatos de diseño
Formularios 
Lightning page, page layouts
Gestión de Usuarios y Permisos
Creación de Usuarios y acceso a la información

vamos a ver la segunda parte de modelado de datos… 



CHECKLIST SPRINT 2


Carga Masiva de Datos
Haber podido subir al menos 500 Registros
Haber limpiado los excel
Tener data concreta
Reportes y Dashboards
Reportes requeridos por el cliente
Dashboards requeridos por el cliente
Automatizaciones
1 Screen Flow
1 Trigger Flow
1 Schedule Flow
vamos a ver la segunda parte de modelado de datos… 



PRESENTACIÓN DEL SPRINT 3
El Objetivo del Sprint: Expandiendo las fronteras del CRM

Este sprint gira en torno a una herramienta fundamental: Experience Cloud. El objetivo es que dejen de ver a Salesforce como una base de datos interna y lo transformen en un portal interactivo.
vamos a ver la segunda parte de modelado de datos… 



Estrategia Técnica: Screen Flows como Interfaz Web

Una de las soluciones más potentes que vamos a implementar es el uso de Screen Flows como formularios dentro del sitio. Para esto, quiero que sigan este orden de arquitectura:
Diseño del Flujo (Backend): Construyan el Screen Flow dentro de Salesforce con las pantallas necesarias (ej: Datos de contacto, motivos, carga de archivos). Asegúrense de que la lógica final cree el registro correspondiente (Lead, Caso o el Objeto Personalizado que definieron).
Definición de Audiencia y Seguridad: Este es el punto crítico. Deben decidir si el formulario es Público (ej: un "Contáctenos" para prospectos) o Privado (solo para usuarios logueados). Si es público, recuerden configurar los permisos del Guest User Profile para que tenga acceso a ejecutar el Flow y crear registros.
Implementación Visual (Experience Builder): Una vez que el flujo es seguro y funcional, su publicación en el sitio es simple. Usen el componente estándar de "Flow" en el Builder, arrástrenlo a la página y selecciónenlo del menú.
vamos a ver la segunda parte de modelado de datos… 



Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Técnicas (El "Qué" haces)
Gestión de Usuarios y Seguridad: El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
Gestión de Datos (Data Management): Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
Automatización Básica (Flows): Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
Reportes y Dashboards: Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.
AgentForce: puedas familiarizarte con la configuración de agentes dentro de Salesforce.
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Blandas (El "Cómo" lo haces)
Comunicación Traducida: Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
Resolución de Problemas (Google-Fu): No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
Mentalidad de Aprendiz (Learner's Mindset): Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
Atención al Detalle: Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Digitales
Uso de la IA: para resolución, investigación, búsqueda de información
Gestión de Herramientas Ágiles: Uso efectivo de tableros Kanban (Jira, Trello, etc.) para el seguimiento de tareas y Sprints.
Uso de foros, google, documentación: Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
Herramientas de Salesforce: Extensiones y herramientas útiles por fuera de salesforce
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Creativas
Resolución Lateral de Problemas (Workarounds): Capacidad de encontrar caminos alternativos e ingeniosos cuando la plataforma presenta limitaciones nativas.
Diseño Centrado en el Usuario (UX/UI): Creación de Page Layouts y pantallas que sean intuitivas, limpias y agradables para el usuario final.
Storytelling con Datos: Habilidad para construir Dashboards y Reportes que no solo muestren números, sino que cuenten una historia visual y clara.
Ingeniería de Procesos: Imaginar y diseñar el "camino más corto y fácil" para que un usuario complete sus tareas diarias.
Resiliencia Técnica: Ver los errores del sistema o bugs como un rompecabezas creativo a resolver, perdiéndole el miedo a "romper" en entornos de prueba.
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

Skills Estratégicas
Traducción de Negocio (Business Analysis): Capacidad para escuchar lo que pide el cliente y traducirlo en requerimientos técnicos reales (entender el "por qué" detrás del "qué").
Mentalidad Escalable: Construir soluciones pensando no solo en el problema de hoy, sino en cómo funcionará cuando la empresa crezca en 2 o 3 años.
Priorización de Valor (MVP): Saber distinguir entre lo esencial y lo accesorio para entregar valor rápido al cliente (Producto Mínimo Viable).
Gestión de Expectativas (Stakeholders): Aprender a negociar requerimientos y a decir "no" (o "lo dejamos para la fase 2") de manera profesional y fundamentada.
Gobernanza y Documentación: Entender que documentar (diccionarios de datos, descripciones) es una estrategia vital para la supervivencia a largo plazo del proyecto.
Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN





Introducción




¿Qué es APEX?

¿Qué es APEX?
Aspectos destacados del lenguaje Apex
Como ocurre con otros lenguajes de programación orientados a objetos, estos son algunos de los elementos de lenguaje que admite Apex:
Clases, interfaces, propiedades y colecciones (listas, mapas y conjuntos).
Notación de objetos y conjuntos.
Expresiones, variables y constantes.
Declaraciones condicionales (si..., entonces...) y declaraciones de flujo de control (bucles for y bucles while).

¿Qué es APEX?
A diferencia de otros lenguajes de programación orientados a objetos, Apex admite lo siguiente:
Desarrollo en la nube a medida que Apex se almacena, compila y ejecuta en la nube.
Desencadenadores, los cuales son similares a los desencadenadores de sistemas de base de datos.
Declaraciones de base de datos que permiten hacer llamadas directas a la base de datos y lenguajes de consulta para consultar y buscar datos.
Transacciones y reversiones.
El modificador de acceso global, que es más permisivo que el modificador public y permite el acceso a espacios de nombres y aplicaciones.
Control de versiones de código personalizado.
Además, no se aplica la distinción entre mayúsculas y minúsculas al lenguaje Apex.

Estructura Básica
Elementos

public: Acceso público a la clase.

static: Método que puede ser llamado sin instanciar la clase.

System.debug(): Método para imprimir información en el log.

CLASES APEX
Una de las ventajas de las clases de Apex es la reutilización del código. 
Se puede llamar a métodos de clase mediante desencadenadores y otras clases. 

Ejemplo Práctico “Hola Mundo”
Descripción
Creamos una clase SoyEstudiante con un método DigoEsto.

Abrir Developer Console en Salesforce.
Ingresar el código y ejecutarlo.

Resultado Esperado:
Ver el mensaje "Soy un SF Admin!" en el log.

Esto enviar por Formulario

Ejemplo Práctico “Hola Mundo”
Descripción
Creamos una clase HelloWorld con un método sayHello.

Abrir Developer Console en Salesforce.
Ingresar el código y ejecutarlo.

Resultado Esperado:
Ver el mensaje "Hello, World!" en el log.

Ejemplo Práctico “Hola Mundo”
public class HelloWorld {
    public static void sayHello() {
        System.debug('Hello, World!');
    }
}
Ejecución en Developer Console:
Abre la Developer Console en Salesforce.
Ve a File > New > Apex Class.
Copia y pega el código anterior en la nueva clase.
Guarda la clase con un nombre, por ejemplo, HelloWorld.
Luego, abre la Anonymous Window (Ctrl + E o desde el menú Debug > Open Execute Anonymous Window).

Ejemplo Práctico “Hola Mundo”
HelloWorld.sayHello();
Hacer CLICK en EXECUTE
Resultado Esperado:
Verás el mensaje "Hello, World!" en el log. 
Para verlo, ve a la pestaña Logs en la Developer Console y selecciona el log más reciente. 
Busca la línea que dice USER_DEBUG para ver el mensaje.

Estructura de una Clase Apex
public class MyClass {
}
Definición de Clase:
Se utiliza la palabra clave class seguida del nombre de la clase.

Modificadores de Acceso
private:
Descripción: Indica que la clase, método o variable solo es accesible dentro de la misma clase.
Uso: Se utiliza para encapsular la lógica y proteger los datos de ser accedidos o modificados desde fuera de la clase.
private void myPrivateMethod() {
    // Lógica interna
}


Modificadores de Acceso
public:
Descripción: Permite que la clase, método o variable sea accesible desde cualquier otra clase dentro de la misma aplicación.
Uso: Se utiliza cuando se desea que otros componentes de la aplicación puedan acceder a la funcionalidad.
public void myPublicMethod() {
    // Lógica accesible desde otras clases
}



Modificadores de Acceso
global:
Descripción: Permite que la clase, método o variable sea accesible desde cualquier lugar, incluso desde paquetes externos.
Uso: Se utiliza principalmente para clases y métodos que se desean exponer a otros desarrolladores o aplicaciones que puedan estar utilizando tu código.
global class MyGlobalClass {
    global void myGlobalMethod() {
        // Lógica accesible globalmente
    }
}

Cuerpo de la clase
public class MyClass {
    public void myMethod() {

        // Lógica del método
    }
}
Contiene métodos y propiedades.

Métodos de una clase APEX
1. Definición de Métodos:
Los métodos son funciones que realizan acciones.
Ejemplo de un método simple:
public void sayHello() {
    System.debug('Hello, World!');}
2. Tipos de Métodos:
Métodos Estáticos: Se pueden llamar sin crear una instancia de la clase.
public static void staticMethod() {
    System.debug('Static Method Called');}
Métodos de Instancia: Requieren una instancia de la clase para ser llamados.

3. Parámetros y Retornos:
Los métodos pueden aceptar parámetros y devolver valores.
public Integer addNumbers(Integer a, Integer b) {
    return a + b;}

LLAMADO
1. Abrir la Consola Anónima:
Ve a Setup > Developer Console.
Selecciona Debug > Open Execute Anonymous Window.

2. Llamar a un Método:
Para llamar a un método estático:
MyClass.staticMethod();

Para llamar a un método de instancia:
MyClass obj = new MyClass();
obj.sayHello();

3. Ver Resultados:
Usa System.debug() para imprimir resultados en la consola.
Revisa los logs en la pestaña Logs para ver la salida.

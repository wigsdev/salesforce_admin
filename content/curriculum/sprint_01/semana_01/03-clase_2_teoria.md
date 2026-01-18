# Salesforce Admin - Teoría Clase 2

## Check-in Inicial
*   **Daily**: ¿Cómo venimos? ¿Algo nos bloquea? ¿Cómo seguimos?
*   **Mascotas de Salesforce**
*   **PREGUNTAS**: Anotar y ver al final.

### Dinámica de trabajo
* EN PARALELO: No distraerse con otras tareas
* ENFOQUE: Prestar atención Seguir el hilo
* PREGUNTAS: Anotar en un cuaderno Al final de la clase
* MICRÓFONO APAGADO: Cuando no hablamos
* CAMARA PRENDIDA: En los grupos
* COMPROMISO: Asistencia, atención y puntualidad.

---

## 1. Modelo de Datos
**Concepto**:
"Imaginen una hoja de cálculo de Excel gigante. Eso es una base de datos plana. El modelo de datos de Salesforce es como tomar ese Excel, cortar las pestañas y conectarlas entre sí de forma inteligente."
*Por qué importa*: Si el modelo está mal diseñado, todo falla (reportes, seguridad, automatización). Es el cimiento del edificio.

### Bloques de Construcción

### A. Objetos (Las Tablas): Son los contenedores de información.
* Objetos Estándar: Vienen de fábrica con Salesforce (Cuentas, Contactos, Oportunidades, Casos). Ya están ahí, no se pueden borrar, solo ocultar.
* Objetos Personalizados: Los que creamos nosotros para necesidades específicas del negocio (ej. "Inmuebles", "Proyectos", "Vehículos").
* Dato clave: En la API (el código), los personalizados siempre terminan en __c (ej. Inmueble__c).
### B. Campos (Las Columnas): Son los datos específicos dentro de un objeto.
* Identidad (ID): Cada registro tiene un DNI único de 15 o 18 caracteres.
* Sistema: Se llenan solos (Creado por, Última modificación).
* Nombre: El nombre del registro (puede ser texto o autounumérico).
* Personalizados: Los que creamos (Texto, Fecha, Picklist, Checkbox, Moneda).


#### C. Relaciones (El corazón del sistema)
Existen dos formas principales de conectar dos objetos (Padre e Hijo):
* A. Relación de Búsqueda (Lookup Relationship):
    * Definición: Una relación flexible. Como un post-it en un archivo que hace referencia a otro.
    * Comportamiento: Si borras al Padre, el Hijo sobrevive.
    * Seguridad: El hijo puede tener su propia seguridad, independiente del padre.
    * Uso: Cuando los datos están relacionados pero no dependen el uno del otro (ej. Un Contacto asignado a un Proyecto específico).
* B. Relación Maestro-Detalle (Master-Detail Relationship):
    * Definición: Una relación fuerte y estricta. Están pegados con pegamento industrial.
    * Comportamiento: Si borras al Padre (Maestro), los Hijos (Detalle) se borran automáticamente (Efecto cascada).
    * Seguridad: El hijo hereda la seguridad del padre. Si no puedes ver al padre, no ves al hijo.
    * Ventaja: Permite crear Campos de Resumen (Roll-up Summary) en el padre (ej. Sumar el total de precios de todos los productos en una oportunidad).
* C. Relación Muchos a Muchos (Many-to-Many):
    * No existe un botón para esto. Se crea usando un tercer objeto en el medio (Objeto de Unión) con dos relaciones Maestro-Detalle.
    * Ejemplo: Un Alumno puede tener muchas Clases, y una Clase tiene muchos Alumnos. El objeto del medio sería "Inscripción".

### Herramienta Visual: Schema Builder
#### Schema Builder 
*   En lugar de crear campos lista por lista, Salesforce tiene una herramienta llamada Schema Builder (Generador de Esquemas).
*   Permite ver el modelo de datos como un diagrama visual (mapa), arrastrar y soltar cajas para crear objetos y dibujar líneas para crear relaciones. Es vital para visualizar la arquitectura compleja.

---

## 2. Herramientas del Administrador

### Object Manager

#### Descripción

Sección de Salesforce donde los administradores gestionan objetos, campos y relaciones entre ellos.
¿Como se asignan los permisos?
¿Que es la data? ¿Qué es la metadata?

#### Utilidades

Facilita la administración de los datos en la plataforma, permitiendo a los administradores crear objetos personalizados y organizar los datos según los procesos de negocio.

### 3. Perfil y Permisos
Controlan qué ven y hacen los usuarios.

#### Descripción

Controlan qué información pueden ver y modificar los usuarios.

#### Utilidad

Aseguran que cada usuario tenga acceso solo a la información relevante para su rol, mejorando la seguridad de la información y cumpliendo con las políticas de la organización.

### 4. Herramientas de Seguridad

#### Descripción

Incluyen la configuración de roles, permisos y opciones como la autenticación de dos factores

#### Utilidad

Garantizan que sólo los usuarios autorizados accedan a los datos y funcionalidades de Salesforce, protegiendo la información sensible de la organización.

**Niveles:**
1.  **Acceso (Login)**: IP Ranges, Horarios, MFA, SSO.
2.  **Datos**:
    *   **Sharing Models**: Privado, Público, Híbrido.
    *   **Sharing Rules**: Compartir automáticamente.
    *   **Field-Level Security**: Visibilidad de campos.
3.  **Auditoría**: Event Monitoring, Setup Audit Trail.

---

### 5. App Builder

#### Descripción

Herramienta visual que permite a los administradores crear aplicaciones personalizadas, definir el diseño de las páginas y personalizar la experiencia del usuario.

#### Utilidad

Permite la creación de interfaces intuitivas y optimizadas para diferentes roles, mejorando la experiencia de usuario y adaptando las aplicaciones a las necesidades de cada equipo.

### 6. Reports and Dashboards

#### Descripción

Herramientas de análisis que permiten a los usuarios ver, analizar y representar datos de forma visual.

#### Utilidad

Facilitan la toma de decisiones al permitir a los administradores y ejecutivos obtener insights clave y crear reportes personalizados.

## 7. Automatización (Process Builder & Flow Builder)

#### Descripción
Herramientas de automatización que permiten crear flujos de trabajo personalizados y automatizar tareas repetitivas.
#### Utilidad
Reducen el trabajo manual y aseguran la consistencia de los procesos, optimizando el tiempo y recursos de la organización.

## 8. Data Loader

#### Descripción
Herramienta que permite importar, exportar y actualizar grandes volúmenes de datos.

#### Utilidad

Muy útil para migrar datos o realizar actualizaciones masivas, lo que ahorra tiempo y reduce el riesgo de errores manuales.

---

## ¡Manos a la obra!
Avanzamos con los trails.
### Modelado de Datos I -> [Entrar aquí](https://trailhead.salesforce.com/es-MX/users/rebecaduran/trailmixes/modelado-de-datos)

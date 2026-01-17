# Salesforce Admin + Agent Force

**Daily**
*   ¿Cómo venimos?
*   ¿Algo nos bloquea?
*   ¿Cómo seguimos?

---

## Gestión de Usuarios: Las Llaves del Reino

**Guía**: Consultar si Saben que es un administrador de Salesforce, si habían escuchado antes de rol.

**Concepto**: Un usuario en Salesforce es simplemente un Registro en la base de datos (como un Cliente o un Contacto), pero con privilegios de acceso.

### Regla de Oro del Username
Debe tener formato de email y ser globalmente único en todo el universo Salesforce (no solo en tu organización).
*   **Ejemplo**: `juan@miempresa.com.dev01`

> "Chicos, lo primero que deben saber es que el Username es sagrado. Tiene que parecer un email, pero no necesita ser un email real. Lo importante es que sea ÚNICO en todo el mundo. Si alguien en Japón usó `admin@salesforce.com`, ustedes no pueden usarlo. Por eso en los entornos de práctica siempre agregamos algo al final, como `nombre@empresa.com.curso2026`"

### La "Tríada de Acceso" (Lo obligatorio para crear uno)
1.  **Licencia de Usuario (User License)**: Es el "Pasaporte". Define qué funcionalidades básicas puede tener el usuario (Ej. Salesforce, Platform, Chatter Free). Cuestan dinero.
2.  **Perfil (Profile)**: Es el "Rol". Define qué puede hacer y ver (Ej. Admin, Ventas, Soporte). Determina los permisos CRUD (Crear, Leer, Editar, Borrar).
3.  **Rol (Role Hierarchy)**: (Opcional pero vital). Define a quién reporta y qué datos de otros usuarios puede ver.

**Licencia vs. Perfil (La gran confusión)**
> "Imaginen un gimnasio.
> La Licencia es la membresía que pagaron. Les da derecho a entrar al edificio. Sin licencia, no entran.
> El Perfil dice qué máquinas pueden usar. ¿Pueden usar la piscina? ¿Solo las pesas?
> No pueden darle permisos de 'Administrador' a alguien con una Licencia de 'Chatter Free', porque su membresía no cubre eso. La Licencia es el techo de lo que pueden hacer."

### Ciclo de Vida: Prohibido Borrar
**Nunca se elimina un usuario**: Salesforce no permite borrar usuarios para mantener la integridad histórica (auditoría).

*   **Desactivar (Deactivate)**: Libera la licencia para que la use otro. El usuario ya no puede entrar.
*   **Congelar (Freeze)**: Bloquea el acceso temporalmente, pero NO libera la licencia. Se usa cuando necesitas tiempo para limpiar sus responsabilidades antes de desactivarlo.

**Congelar vs. Desactivar**
> "¿Por qué no podemos borrar usuarios? Imaginen que Juan cerró una venta millonaria en 2024 y luego se fue de la empresa. Si borramos a Juan, esa venta queda huérfana. Salesforce guarda todo."

> "Congelar es para emergencias: 'Despidieron a Juan ahora mismo, congélalo para que no entre, luego vemos qué hacemos con sus datos'. Desactivar es el paso final: 'Ya pasamos sus cuentas a María, adiós Juan'. Al desactivar, recuperamos la licencia para dársela a alguien nuevo."

### El Detective: Login History
- Si un usuario dice "No puedo entrar", no le cambies la contraseña a ciegas.
- **Revisa el Historial de Inicios de Sesión (Login History)**. Te dirá exactamente por qué falló: *Password Incorrecto, Restricción de IP, Horario no permitido o Usuario Congelado.*

> "Como Admins, su día a día será: 'No puedo entrar'. Antes de resetear la contraseña, vayan al Login History. Ahí verán si el usuario está poniendo mal la clave (Invalid Password) o si está intentando entrar un sábado y su perfil solo permite de Lunes a Viernes. El Login History es su herramienta de detective."

---

## Autenticación de Usuarios

### 1. MFA (Autenticación Multifactor): Nuevo Estándar
**¿Qué es?** Es un método de seguridad que requiere dos o más pruebas (factores) para iniciar sesión.

**La Fórmula**:
*   Algo que sabes (Tu contraseña).
*   Algo que tienes (Tu celular con la App Salesforce Authenticator o una llave de seguridad física).

**Por qué es obligatorio**: Las contraseñas se roban o adivinan fácilmente (phishing). El segundo factor impide que el hacker entre aunque tenga tu clave.

> "Chicos, la contraseña sola ya murió. Es demasiado insegura. Imaginen el cajero automático: necesitan la Tarjeta (algo que tienen) y el PIN (algo que saben). Si les roban la tarjeta pero no saben el PIN, no sacan plata. MFA es exactamente eso en Salesforce. Hoy en día, activar MFA no es una opción, es una exigencia contractual de Salesforce para proteger los datos."

### 2. My Domain (Personalizado)
**Definición**: Es una URL personalizada para tu organización de Salesforce.
*   **Antes**: `https://na123.salesforce.com` (Genérico).
*   **Con My Domain**: `https://tuempresa.my.salesforce.com` (Profesional).

**Importancia Técnica**: No es solo estético. Es obligatorio para usar componentes Lightning personalizados, Single Sign-On (SSO) y para trabajar mejor con múltiples navegadores.

> "¿Han visto que cuando entran a Facebook es facebook.com y no servidor54.facebook.com? My Domain hace que su Salesforce tenga nombre propio, como dap-creaciones.my.salesforce.com. Más allá de verse bonito y dar confianza, Salesforce lo necesita internamente para que los componentes modernos (Lightning Web Components) funcionen bien. Es el primer paso de configuración en una org nueva."

### 3. Single Sign On (Llave Maestra)
**Concepto**: Permite a los usuarios acceder a múltiples aplicaciones (Salesforce, Gmail, Slack) con un solo inicio de sesión.

**Beneficio**:
*   **Para el usuario**: Menos contraseñas que recordar (menos post-its en el monitor).
*   **Para TI**: Si un empleado se va, bloqueas su acceso en un solo lugar y pierde acceso a todo automáticamente.

> "SSO es lo que pasa cuando usan 'Iniciar sesión con Google'. En las empresas grandes, no quieren que tengas 20 contraseñas diferentes. Usan un proveedor de identidad (como Microsoft Azure o Okta). Tú te logueas en tu computadora en la mañana, y cuando abres Salesforce... ¡bum! Ya estás adentro sin escribir nada. Eso es SSO: seguridad para la empresa y comodidad para el usuario."

---

## ¡Manos a la obra!

Avanzamos con los trails.

**Conceptos de Gestión de Usuarios y Modelado de Datos (Repaso)**.

**Link**: [Ingresar aquí](https://trailhead.salesforce.com/es-MX/users/rebecaduran/trailmixes/teoria-semana-2-gestion-de-usuarios)

---

## REPASO
### Modelado y calidad de datos

### Mejores Prácticas en el Modelado de Datos

### 1. Comprender los Requisitos del Negocio
*   Antes de modelar datos, identifica las necesidades específicas de la organización.
*   Involucra a los usuarios finales para entender los flujos de trabajo, reportes requeridos y datos críticos.

### 2. Usar Objetos y Campos de Manera Estratégica
*   **Objetos Estándar**: Úsalos siempre que sea posible para evitar duplicidad y aprovechar funcionalidades nativas.
*   **Objetos Personalizados**: Crea solo cuando los objetos estándar no cumplan con los requisitos específicos.
*   **Campos Personalizados**: Evita crear demasiados campos innecesarios para mantener un diseño limpio.

### 3. Definir Relaciones Claras
*   Utiliza relaciones **Lookup** cuando los datos sean opcionales o tengan conexiones débiles.
*   Usa relaciones **Master-Detail** para dependencias fuertes entre datos y flujos de datos jerárquicos.
*   Configura reglas de eliminación y visibilidad adecuadas para cada tipo de relación.

### 4. Optimizar el Rendimiento
*   Minimiza el uso de campos de texto largos o campos enriquecidos en consultas frecuentes.
*   Reduce los cálculos innecesarios en campos de fórmulas complejas.
*   Usa índices en campos clave para acelerar búsquedas y reportes.

### 5. Diseñar para Escalabilidad
*   Planifica un modelo de datos que pueda crecer con la organización.
*   Considera el impacto de volúmenes altos de datos en objetos, relaciones y reportes.
*   Implementa partición lógica de datos si se espera un crecimiento significativo.

### 6. Aprovechar el Generador de Esquemas (Schema Builder)
*   Utiliza el Generador de Esquemas para visualizar y revisar conexiones entre objetos.
*   Realiza auditorías periódicas para identificar relaciones o campos innecesarios.

### 7. Establecer Reglas de Nombres Consistentes
*   Usa nombres descriptivos y consistentes para objetos, campos y relaciones.
*   Establece un estándar de nomenclatura para que sea fácilmente entendible por todos los usuarios.

### 8. Aplicar Controles de Seguridad
*   Configura la seguridad a nivel de objeto, campo y registro de acuerdo con los roles de los usuarios.
*   Asegúrate de que los datos sensibles estén protegidos y solo accesibles para usuarios autorizados.

### 9. Documentar el Modelo de Datos
*   Crea una documentación detallada del modelo de datos, incluyendo objetos, campos, relaciones y dependencias.
*   Mantén la documentación actualizada con cada cambio en la estructura.

### 10. Limitar la Duplicación
*   Implementa reglas de duplicación para evitar la creación de datos redundantes.
*   Usa herramientas como **Duplicate Management** para controlar la calidad de los datos.

### 11. Revisar y Mantener Regularmente
*   Programa auditorías periódicas para eliminar campos, relaciones u objetos que ya no sean necesarios.
*   Analiza el uso de campos y objetos para identificar oportunidades de mejora.

---

## Métodos de Importación de datos

### 1. Asistente de Importación de Datos (Data Import Wizard)
El Asistente de Importación de Datos es una herramienta intuitiva y fácil de usar que permite a los usuarios importar datos directamente desde la interfaz de Salesforce. Esta herramienta está diseñada para usuarios con poca experiencia técnica y para operaciones de importación más pequeñas y controladas.

**Características**:
*   **1. Interfaz basada en la web**: Accesible desde la configuración de Salesforce, sin necesidad de descargar ni instalar software adicional.
*   **2. Soporte para múltiples objetos**: Compatible con la mayoría de los objetos estándar (como Contactos, Cuentas, Leads) y objetos personalizados.
*   **3. Personalización de opciones**: Permite configurar criterios de coincidencia para evitar duplicados y seleccionar cómo se manejarán los datos existentes (actualización, inserción o ambas).
*   **4. Validación automática**: El asistente guía a los usuarios paso a paso, asegurándose de que los datos cumplan con los requisitos antes de ser importados.

**Capacidades**:
*   **Cantidad de registros soportados**: Hasta **50,000 registros** por operación.
*   **Uso específico**: Ideal para pequeñas importaciones. Adecuado para usuarios que trabajan con datos básicos y necesitan simplicidad.

**Pasos para usar el Asistente**:
1.  Acceder al asistente desde la configuración (Configuración → Herramientas de Importación de Datos).
2.  Seleccionar el objeto (estándar o personalizado).
3.  Subir el archivo CSV.
4.  Configurar las opciones de coincidencia para evitar duplicados.
5.  Mapear los campos del archivo CSV con los campos en Salesforce.
6.  Revisar y ejecutar la importación.
7.  Monitorear el progreso.

### 2. Data Loader (Cargador de Datos)
El Data Loader es una herramienta más avanzada que permite a los usuarios importar, exportar y eliminar grandes volúmenes de datos en Salesforce. Es ideal para administradores y desarrolladores que necesitan flexibilidad y escalabilidad.

**Características**:
*   **Software descargable**: Aplicación de escritorio (Windows/macOS).
*   **Soporte avanzado**: Permite trabajar con objetos estándar, personalizados, relaciones jerárquicas y grandes volúmenes.
*   **Métodos de uso**: Interfaz de usuario (UI) para cargas manuales o Línea de comandos (CLI) para automatización.
*   **Registros detallados**: Genera archivos de éxito y error para auditoría.

**Capacidades**:
*   **Cantidad de registros soportados**: Hasta **150 millones de registros** por operación.
*   **Uso específico**: Grandes volúmenes, proyectos complejos, automatización, integraciones.

**Pasos para usar Data Loader (UI)**:
1.  Descargar e instalar Data Loader.
2.  Configurar la conexión con Salesforce (OAuth/credenciales).
3.  Seleccionar operación (Insert, Update, Delete, Export).
4.  Subir archivo CSV.
5.  Mapear campos.
6.  Ejecutar la operación y monitorear los resultados.
7.  Revisar archivos de éxito y error generados automaticamente.


**Automatización con la Línea de Comandos (CLI):**
- Configuración inicial: Crear scripts que definan las operaciones y configuren los datos.
- Uso frecuente: Para importaciones periódicas o integración con otros sistemas mediante API.

**Comparacion**



---

## Preparación para la Importación de Datos

La preparación adecuada de los datos es esencial para garantizar que el proceso de importación sea exitoso y que los datos en Salesforce sean precisos, coherentes y útiles para las operaciones empresariales. A continuación, veremos los pasos clave que debes realizar antes de importar datos a Salesforce.

### 1. Creación de un Archivo de Exportación desde el Sistema de Origen
* Para comenzar, es necesario extraer los datos desde el sistema o aplicación de origen. Esto suele hacerse en formato CSV (Comma-Separated Values), que es ampliamente compatible con las herramientas de importación de Salesforce.

* Asegúrate de incluir todos los datos necesarios, como nombres, direcciones, identificadores únicos, y cualquier información relevante para los procesos empresariales.

* Verifica que los datos exportados sean los más recientes y reflejen la información actual.


### 2. Limpieza y Normalización de Datos
Antes de importar los datos, es fundamental realizar una limpieza y normalización para garantizar que sean precisos y consistentes. Los principales pasos incluyen:

* Eliminación de duplicados:
    * Busca registros duplicados utilizando herramientas como Excel, Google Sheets, o software de limpieza de datos.
    * Asegúrate de consolidar los registros duplicados antes de la importación para evitar redundancia en Salesforce.

* Corrección de errores ortográficos:
    * Revisa manualmente o utiliza herramientas automatizadas para corregir errores comunes en nombres, direcciones y otros campos clave.

* Aplicación de convenciones de nomenclatura:
    * Estandariza los valores de los campos para mantener coherencia.
    * Ejemplo: Usar "Estados Unidos" o "EE.UU." de manera uniforme en todos los registros.
    * Formatear nombres en "Nombre Apellido" en lugar de "APELLIDO, Nombre".
    * Aplica formatos consistentes para números de teléfono, direcciones y fechas.


### 3. Comparación y Mapeo de Campos
El mapeo de campos asegura que cada columna del archivo de importación se corresponda con un campo específico en Salesforce.

Pasos clave:
* Revisar campos disponibles en Salesforce:
    * Identifica los campos estándar y personalizados que recibirán los datos.
* Comparar nombres de columnas:
    * Asegúrate de que los nombres de las columnas en el archivo CSV coincidan con los nombres o formatos esperados en Salesforce.
* Ajustar los datos del archivo de importación:
    * Si un campo en Salesforce espera datos numéricos, asegúrate de que la columna correspondiente en el archivo tenga solo 


### 4. Realización de Cambios de Configuración Necesarios en Salesforce
Antes de iniciar la importación, es posible que debas realizar ajustes en Salesforce para garantizar que los datos se importen correctamente.

* Creación de campos personalizados:
    * Si los datos incluyen información no cubierta por los campos estándar, crea campos personalizados en el objeto correspondiente.
    * Ejemplo: Si estás importando datos de empleados, puedes agregar un campo personalizado para "Fecha de contratación".
* Actualización de listas de selección (picklists):
    * Si un campo es una lista de selección, verifica que todos los valores en el archivo de importación estén incluidos en la lista de opciones de Salesforce.
    * Agrega nuevos valores a la lista si es necesario para evitar errores durante la importación.
* Desactivación temporal de reglas de flujo de trabajo y validación:
    * Algunos flujos de trabajo o reglas de validación pueden bloquear la importación o generar errores.
    * Ejemplo: Una regla que exige que el campo "Estado" esté completo podría impedir la importación de datos incompletos.
    * Desactiva temporalmente estas reglas durante la importación y vuelve a activarlas una vez que el proceso haya finalizado.


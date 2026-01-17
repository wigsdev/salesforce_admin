# Reto 1: Configurar Objetos Estándar

Desafío 1 de la Object Relationships Superbadge Unit.

Este reto se enfoca en configurar objetos estándar (Account y Campaign) para gestionar una aplicación de giras de conciertos.

---

## Fase 0: Preparación del Entorno

El video enfatiza que no se puede usar un Playground normal.

Debes registrarte en una Developer Edition especial (con metadatos preinstalados para este Superbadge) usando el enlace que provee Trailhead.

Conectar esa nueva Org a tu cuenta de Trailhead antes de empezar.

---

## Paso 1: Personalización del Objeto Account (Cuentas/Recintos)

El objetivo es crear una interfaz dinámica para gestionar los "Recintos" (Venues).

### Ir al Lightning App Builder

Desde el Object Manager > Account, ve a Lightning Record Pages.

Crea una Nueva Página de tipo "Record Page".

- **Etiqueta**: Concert Venue Layout
- **Plantilla**: Header and Two Equal Regions (Encabezado y dos regiones iguales).

### Configurar Componentes

- Arrastra el Highlights Panel al encabezado.
- Arrastra Record Detail a la columna izquierda.
- Arrastra Activities a la columna derecha.

### Activar Dynamic Forms (Formularios Dinámicos)

Selecciona el componente Record Detail y haz clic en Upgrade Now (Actualizar ahora) en el panel derecho para convertirlo a Dynamic Forms.

Elimina la sección de "Información Adicional" si sobra.

### Aplicar Lógica de Visibilidad (Filtros)

Configura que ciertos campos solo aparezcan bajo condiciones específicas:

- **Campo Capacity (Capacidad)**: Solo visible si Type es igual a "Concert Venue".
- **Campo Security Provided (Seguridad provista)**: Solo visible si Type es igual a "Concert Venue".
- **Campo Security %**: Solo visible si Security Provided es igual a True (Verdadero).

### Activación

Guarda y activa la página como Org Default para escritorio.

---

## Paso 2: Personalización del Objeto Campaign (Giras/Tours)

El objetivo es adaptar las Campañas para que funcionen como "Giras".

### Modificar el Campo "Type" (Tipo)

En Object Manager > Campaign > Fields & Relationships, edita el campo Type.

Actualiza/Reemplaza los valores existentes según la letra del desafío (en el video agrega valores como Tour, Interview, Digital Show).

### Crear Relación con Recintos

Crea un nuevo campo en Campaign.

- **Tipo de dato**: Lookup Relationship (Relación de búsqueda).
- **Relacionado con**: Account (Esto servirá para asignar el Recinto a la Gira).

### Limpiar el Page Layout (Diseño de Página)

Edita el Campaign Layout.

Elimina secciones innecesarias.

Organiza los campos en un orden lógico (ej: Campaign Owner, Parent Campaign, Name, Active, Venue/Account, Type, Status, fechas).

Agrega las listas relacionadas necesarias (Contacts, Responses).

---

## Paso 3: Carga de Datos (Testing)

Para verificar que todo funciona, el video muestra la creación de 4 registros de Campaña específicos con una jerarquía:

### Campaña 1

- **Nombre**: Errors Tour
- **Tipo**: Tour
- **Estado**: Planned

### Campaña 2

- **Nombre**: Camp Success
- **Padre (Parent)**: Errors Tour
- **Tipo**: Interview
- **Estado**: Planned

### Campaña 3

- **Nombre**: Demo Jam
- **Padre**: Camp Success
- **Tipo**: Digital Show

### Campaña 4

- **Nombre**: Trailblazer Tour
- **Tipo**: Tour

---

## Resumen del Objetivo

Has transformado objetos estándar de ventas (Cuentas y Campañas) en una estructura para gestionar Recintos de conciertos y Giras mundiales, usando visibilidad condicional para mejorar la experiencia del usuario.

---

**Grupo**: 3 - VISIONARY ADMINS  
**Última actualización**: 17 Enero 2026

# Reto 2: Crear Objetos Custom y Relaciones

## Objetivo del Reto

Crear la estructura para manejar las "Listas de Canciones" (Setlists) que se tocan en cada Gira, conectando las Giras (Campaigns) con las Canciones (Songs).

---

## Paso 1: Crear el Objeto Personalizado "Track List"

Este será el objeto intermedio que conecta Tours y Canciones.

### En Object Manager

Crear un Custom Object (Objeto Personalizado).

- **Label**: Track List
- **Plural Label**: Track Lists
- **Record Name**: Dejar por defecto (Track List Name, Texto) o según indique la letra (el video lo deja default).

### Características Opcionales

- Marcar Allow Reports (Permitir informes).
- Marcar Allow Activities (Permitir actividades).
- **Search Status**: Marcar Allow Search.

Guardar.

---

## Paso 2: Crear Relaciones en "Track List" (El Puente)

El objeto Track List necesita conectarse con dos padres para funcionar como unión.

### Relación con Campaign (Tour)

En el objeto Track List > Fields & Relationships, crea un nuevo campo.

- **Tipo de Dato**: Master-Detail Relationship (Maestro-Detalle). **Nota**: Esto es vital porque si se borra el Tour, la lista de canciones de ese tour debe desaparecer.
- **Relacionado con**: Campaign.
- **Field Label**: Tour (o dejar por defecto Campaign, ajusta según el requisito del superbadge).

Siguiente, Siguiente, Guardar.

### Relación con Song (Canción)

Crea otro campo nuevo en Track List.

- **Tipo de Dato**: Master-Detail Relationship (Maestro-Detalle).
- **Relacionado con**: Song.

Siguiente, Siguiente, Guardar.

**Resultado**: Has creado una relación "Muchos a Muchos" entre Giras y Canciones usando Track List en el medio.

---

## Paso 3: Conectar Canciones con Álbumes

Ahora necesitas vincular cada canción a su álbum correspondiente.

### Ir al Objeto "Song"

Busca el objeto personalizado Song en el Object Manager.

### Crear Relación de Búsqueda

Ve a Fields & Relationships > Nuevo.

- **Tipo de Dato**: Lookup Relationship (Relación de Búsqueda). **Nota**: Usamos Lookup y no Master-Detail porque una canción podría existir sin estar asignada a un álbum, o si borras el álbum, quizás no quieras borrar la canción.
- **Relacionado con**: Album.

Siguiente, Siguiente, Guardar.

---

## Resumen de la Arquitectura Creada

| Objeto Hijo | Objeto Padre | Tipo de Relación | Lógica de Negocio |
|-------------|--------------|------------------|-------------------|
| Track List | Campaign (Tour) | Master-Detail | La lista pertenece estrictamente a la gira. |
| Track List | Song | Master-Detail | La lista se compone de canciones. |
| Song | Album | Lookup | Una canción "puede" pertenecer a un álbum. |

Este paso es crítico para entender cómo romper una relación "Muchos a Muchos" (Muchos tours tienen muchas canciones) usando un objeto intermedio (Track List) con dos relaciones fuertes (Master-Detail).

---

**Grupo**: 3 - VISIONARY ADMINS  
**Última actualización**: 17 Enero 2026

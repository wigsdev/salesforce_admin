# Reto 3: Crear la Aplicación World Tour Manager

## Objetivo del Reto

Crear la aplicación "World Tour Manager", configurando la navegación estilo consola y asignando los permisos correspondientes.

---

## Paso 1: Crear la Lightning App

### Ir al App Manager

Desde Setup, busca App Manager.

Haz clic en New Lightning App.

### Configuración Básica (App Details)

- **App Name**: World Tour Manager (Copia y pega exacto de la letra para evitar errores).
- **Developer Name**: Se autocompleta.
- **Image**: Opcional (el video no carga ninguna).
- Siguiente.

### Opciones de Navegación (App Options)

- **Navigation Style**: Selecciona Console Navigation (Navegación de Consola).

**Nota Importante**: La letra del desafío pide explícitamente consola. Esto permite abrir múltiples pestañas (subtabs) dentro de una misma ventana, ideal para gestionar giras y datos relacionados.

Siguiente, Siguiente.

---

## Paso 2: Selección de Elementos (Utility Items & Navigation Items)

### Utility Items

El video salta esta parte (clic en Next), lo que indica que no se requieren utilidades específicas (como History o Notes) para este reto.

### Navigation Items (Las Pestañas)

Debes seleccionar los objetos que serán visibles en la barra de navegación. El orden mostrado en el video es:

- Accounts (Cuentas/Recintos)
- Albums (Álbumes - Objeto personalizado)
- Artists (Artistas - Objeto personalizado, probablemente venía en la org o se creó antes)
- Campaigns (Giras)
- Contacts (Contactos)
- Songs (Canciones - Objeto personalizado)
- Reports (Reportes)

**Acción**: Moverlos de la lista "Available" a "Selected Items".

Siguiente.

---

## Paso 3: Asignación de Perfiles (User Profiles)

Debes definir quién tiene permiso para ver esta aplicación.

### Perfiles Seleccionados

- Busca y agrega System Administrator.
- Busca y agrega Standard User.

**Nota**: Si el desafío mencionara un perfil personalizado (ej. "Tenor Management User"), deberías agregarlo aquí.

### Finalizar

Haz clic en Save & Finish.

---

## Paso 4: Verificación (Testing)

### App Launcher

- Haz clic en los 9 puntos (Waffle) arriba a la izquierda.
- Busca World Tour Manager.
- Verifica que la aplicación aparece y se abre en modo consola (con las pestañas de navegación que elegiste).

---

## Resumen del Objetivo

Has empaquetado toda la arquitectura de datos (Recintos, Giras, Canciones, Álbumes) en una Experiencia de Usuario unificada bajo el formato de Salesforce Console, lista para ser entregada al equipo de gestión de la banda.

---

**Grupo**: 3 - VISIONARY ADMINS  
**Última actualización**: 17 Enero 2026

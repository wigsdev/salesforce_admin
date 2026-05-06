# Guía Avanzada: Personalización del Home por Audiencias (Experience Cloud)

## Objetivo
Implementar una arquitectura de **Front-End Bifurcado** mediante *Page Variations* y *Audiences* en Experience Cloud. Esto permite que la misma URL raíz (`/s/`) muestre un diseño y componentes completamente distintos dependiendo de si el usuario es un Visitante Anónimo (Prospecto) o un Usuario Autenticado (Alumno Matriculado).

## ¿Cuándo usar esta técnica?
*   Cuando quieres esconder componentes enteros (como FAQs públicas) de usuarios que ya iniciaron sesión.
*   Cuando la personalización a nivel de componente se vuelve inmanejable.
*   Cuando manejas múltiples roles (Alumnos, Profesores, Administrativos) en el mismo portal y cada uno requiere un *Dashboard* diferente.

---

## PASO 1: Preparar la Página Maestra (La página por defecto)
En Salesforce Experience Cloud, la página original siempre será la página de "rescate" (Fallback). Es la página que verán todos los usuarios que *no cumplan* con ningún criterio de audiencia especial.

1.  En **Experience Builder**, asegúrate de que el menú de control superior indique que estás viendo las páginas de **Inicio (Home)**.
2.  Diseña esta página con todos los componentes que deseas que vean tus **Usuarios Autenticados (Alumnos)**. *(Ej: Dashboards de casos, artículos técnicos, menús de autogestión)*.
3.  Esta será tu "Default Page".

## PASO 2: Crear la Variación de Página para Anónimos (Landing Page)
1.  Haz clic en el ícono de engranaje ⚙️ (Page Properties) al lado del título de la página actual en el menú central.
2.  Selecciona **Page Variations** (Variaciones de página).
3.  Haz clic en el botón **New Page Variation** (Nueva variación de página).
4.  Elige **New Blank Page** si quieres construir el diseño de ventas desde cero, o **Duplicate** si quieres clonar el Home actual y borrar componentes.
5.  Nombra tu variación como: `Página de Captación (Anónimos)`.
6.  *Importante:* Cierra la ventana y asegúrate de cambiar la vista superior en el Builder para empezar a editar esta nueva página en blanco. Inserta aquí tu Formulario de Leads comercial.

## PASO 3: Construir el Criterio (La Audiencia)
Tenemos que decirle al sistema quién califica para ver la nueva página.
1.  En la misma ventana de **Page Variations**, cambia a la pestaña superior **Audiences** (Audiencias).
2.  Haz clic en **Add Audience** (Nueva audiencia).
3.  Escribe como Nombre: `Visitantes No Autenticados`.
4.  Configura las reglas lógicas:
    *   **Tipo (Type):** `User` (Usuario).
    *   **Criterio (Operator):** `Equals` (Es igual a).
    *   **Valor:** `Unauthenticated` (No autenticado).
    > **Alternativa por Perfil:** También puedes apuntar directamente al perfil oculto. *Tipo: Profile, Operador: Equals, Valor: Campus Virtual Lumina Tech Profile*.
5.  Haz clic en **Guardar**.

## PASO 4: Cruzar Variación con Audiencia (El Ensamblaje)
1.  Regresa a la pestaña **Page Variations**.
2.  En la lista, localiza tu nueva variación `Página de Captación (Anónimos)`.
3.  Haz clic en el menú desplegable (▼) a la derecha de ese nombre y selecciona **Assign** (Asignar).
4.  Aparecerá un cuadro de diálogo con tus audiencias. Selecciona `Visitantes No Autenticados` y asígnala.
5.  Activa o Pública (Set to Active) si el sistema lo requiere.

## Verificación Final y Despliegue
*   **En Experience Builder:** Podrás alternar entre vistas usando el menú superior central (Verás que ahora te permite seleccionar entre "Default Page" y "Página de Captación").
*   **En QA:** Abre una ventana de modo incógnito. Debes aterrizar automáticamente en la Variación, diseñada comercialmente. Al iniciar sesión como un alumno de prueba, el sistema purgará la variación e inyectará los componentes privados de la Default Page.

---
**Nota de Arquitectura:** Almacena siempre estos flujos de decisiones (quién ve qué) en tu diagrama de roles para facilitar la escalabilidad del portal en futuros Sprints.

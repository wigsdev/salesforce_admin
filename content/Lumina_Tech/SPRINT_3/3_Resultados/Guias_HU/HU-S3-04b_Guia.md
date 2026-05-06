# 🎯 GUÍA DE IMPLEMENTACIÓN: HU-S3-04b
**Nombre:** Screen Flow Privado — Publicación en el Portal (Parte B)
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce (aprendices)
**Herramienta principal:** Setup → Profiles + Experience Builder

> [!IMPORTANT]
> **Pre-requisito:** La **HU-S3-04a** debe estar completada. El Flow `Lumina EC Reclamos y Tramites Alumno` debe estar en estado **Active** antes de iniciar esta guía.

---

## 🧭 ¿Qué vas a construir en esta parte?

Conectar el Flow ya activado al portal de Experience Cloud:
1. Verificar que el perfil del alumno tiene permisos para crear Cases
2. Crear la página privada `Trámites` en el Builder
3. Publicar el Flow en esa página
4. Agregar el ítem "Hacer una consulta" al menú de navegación
5. Publicar el sitio

---

### Paso 1 (de esta parte): Verificar Permisos del Perfil Customer Community User

El alumno logueado usa el perfil **Customer Community User**. Sin permisos de creación sobre `Case`, el Flow fallará silenciosamente cuando el alumno intente enviar su solicitud.

1. En Setup, escribe `Profiles` en el Quick Find → haz clic en **Profiles**.
2. En la lista de perfiles, haz clic en **Customer Community User**.
3. En la página del perfil, haz clic en el botón **Edit** (arriba a la derecha).
4. Usa `Ctrl+F` en el navegador para buscar `Case` dentro de la página del perfil (es una página larga).
5. En la sección de permisos del objeto **Case**, verifica que estén activas:
   - ✅ **Read**
   - ✅ **Create**
6. Si alguna no está activa, actívala y haz clic en **Save** al final de la página.

> [!WARNING]
> Este paso es crítico. Si `Create` no está activo en el perfil, el Flow ejecutará el Create Records, Salesforce lo rechazará por permisos, y el alumno verá la pantalla de error sin ninguna indicación clara de qué falló.

---

### Paso 2 (de esta parte): Crear la Página Privada "Trámites" en el Experience Builder

1. En Setup, escribe `All Sites` en el Quick Find → haz clic en **All Sites**.
2. En la fila del sitio **Campus Virtual Lumina Tech**, haz clic en el botón **Builder**.
3. En la barra superior del Builder, haz clic sobre el **nombre de la página actual** (dice "Home" o "Inicio"). Se despliega el selector de páginas del sitio.
4. En la parte inferior de ese panel, haz clic en **+ New Page**.
5. Selecciona **Standard Page** en el modal que aparece.
6. Selecciona el layout **Flexible Layout**.
7. Completa los campos:
   - **Page Name:** `Tramites`
   - **URL:** `tramites`
8. Haz clic en **Create**.

**Inmediatamente después de crear la página, configura su acceso:**

9. Con la página **Tramites** activa en el Builder, haz clic en el ícono **⚙️ (Settings)** que aparece en la barra superior junto al nombre de la página.
10. Selecciona **Page Settings** o **Page Access** en el menú desplegable.
11. Cambia el acceso a **`Requires Login`** (o **"Login Required"**).
12. Guarda la configuración.

> [!WARNING]
> **Este paso es obligatorio.** La configuración **"Default"** no siempre redirige al login en todos los templates de Experience Cloud — en algunos casos permite que usuarios anónimos accedan a la página y vean una pantalla en blanco en lugar del formulario. Configurar explícitamente **"Requires Login"** garantiza que los visitantes sin sesión sean redirigidos al login al intentar acceder a `/tramites`.

---

### Paso 3 (de esta parte): Agregar el Flow a la Página Trámites

1. Verifica que estás en la página **Tramites** — el nombre debe aparecer en la barra superior del Builder.
2. En la **barra lateral izquierda** del Builder, haz clic en el primer ícono (⚡ rayo o figura geométrica) — este es el panel de **Components**.
3. En el buscador del panel de componentes, escribe `Flow`.
4. Aparecerá el componente estándar **Flow** — arrástralo al área central de la página y suéltalo.
5. Con el componente Flow seleccionado, en el **panel derecho** de propiedades:
   - En el campo **Flow**, haz clic en el dropdown y selecciona `Lumina EC Reclamos y Tramites Alumno`.
6. El componente mostrará la primera pantalla del Flow en la vista previa del Builder — esto confirma que está correctamente conectado.

---

### Paso 4 (de esta parte): Actualizar el Menú de Navegación

La página "Tramites" ahora existe. Agrega el ítem de menú que quedó pendiente desde la HU-S3-01.

1. En el Builder, haz clic sobre la **barra de navegación** (la franja azul debajo del header donde dice "INICIO").
2. En el panel derecho aparece la propiedad **Navigation Menu** — haz clic en el nombre del menú para editarlo.
3. Se abre el editor **Edit Default Navigation**. Haz clic en **+ Add Menu Item**.
4. Configura el nuevo ítem:
   - **Name:** `Hacer una consulta`
   - **Type:** selecciona **`Site Page`** *(NO uses External URL — requiere URL absoluta con https:// y rechaza rutas relativas)*
   - **Page:** selecciona `Tramites` del dropdown que aparece
   - **Publicly available:** ✅ **YES** — el tab debe ser visible para todos, incluyendo usuarios anónimos
5. Haz clic en **Save Menu**.
6. Verifica que el menú del Builder ahora muestra: `Home | Hacer una consulta` (o `Inicio | Hacer una consulta`).

> [!NOTE]
> **¿Por qué Publicly available: YES si la página es privada?**
> La **seguridad la maneja la página** (Page Access: Requires Login), no el menú. Poner el tab como visible para todos permite que el alumno anónimo **descubra el servicio** antes de loguearse. Al hacer clic → es redirigido al login → después del login llega directamente al formulario. Este es el patrón estándar de UX para contenido privado en portales web.


---

### Paso 5 (de esta parte): Publicar el Sitio

1. En la barra superior del Builder, haz clic en el botón **Publish**.
2. En el modal de confirmación, haz clic en **Publish** nuevamente.
3. Espera el mensaje de confirmación de publicación exitosa.

---

### ✅ Checklist de Resultado Profesional — QA Completo

Ejecuta estas pruebas en orden para validar que la HU-S3-04 (ambas partes) está correctamente implementada:

| # | Prueba | Cómo verificar | Resultado Esperado |
|:---:|:---|:---|:---|
| 1 | **Permisos del perfil** | Setup → Profiles → Customer Community User → Case | Read ✅ y Create ✅ activos |
| 2 | **Página Tramites existe** | Builder → selector de páginas (barra superior) | Aparece `Tramites` en la lista |
| 3 | **Flow conectado a la página** | Builder → página Tramites | El componente Flow muestra la Pantalla 1 en la vista previa |
| 4 | **Menú actualizado** | Sitio publicado → barra de navegación | Muestra: `Inicio \| Hacer una consulta` |
| 5 | **Acceso anónimo bloqueado** | Navegador en incógnito → URL del sitio + `/tramites` | Redirige al login — no muestra el formulario |
| 6 | **Login y formulario visible** | Iniciar sesión como Lucas Martinez → clic en "Hacer una consulta" | Muestra la Pantalla 1 con el Picklist de 5 opciones |
| 7 | **Completar formulario** | Seleccionar `Nota o calificacion` → escribir descripción → enviar | Aparece pantalla de confirmación con el tipo seleccionado |
| 8 | **Case creado en Salesforce** | Admin → App Launcher → Cases | Existe el Case con `Origin = Web`, `Status = New`, `Priority = Medium` |
| 9 | **ContactId automático** | Abrir el Case creado → campo **Contact** | Muestra `Lucas Martinez` sin que él lo haya escrito |

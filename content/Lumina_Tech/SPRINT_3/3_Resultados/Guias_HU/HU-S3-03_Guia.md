# 👥 GUÍA DE IMPLEMENTACIÓN: HU-S3-03
**Nombre:** Habilitación de Alumnos (Community Users)
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce

### Paso 1: Configurar el Login del Portal
1. Ve a **Setup → All Sites** → haz clic en **Workspaces** al lado de tu sitio.
2. Clic en **Administration** → Pestaña **Members**.
3. En la lista desplegable del buscador cambia "Portal" por "All". Pasa el perfil **Customer Community User** a la columna "Selected Profiles". Haz clic en **Save**. *(Si olvidas este paso, los alumnos no podrán loguearse).*

### Paso 2: Convertir al Contacto en Usuario
1. Cierra Setup y abre la aplicación normal Sales. Ve a la pestaña **Contacts**.
2. Abre el registro alumno de "Lucas Martinez".
3. En la esquina superior derecha del registro busca la flecha de opciones y haz clic en **Enable Customer User** (a veces está dentro del menú de botones).
4. El sistema abre la pantalla de creación de usuario:
   - User License: `Customer Community`.
   - Profile: `Customer Community User`.
   - Role (si lo pide): No le des importancia alta o ponlo por defecto.
   - Email: El real de prueba que controles.
   - *Nota:* Asegúrate de que el campo Username (nombre de usuario) sea único (ej: `lucas.mtz@lumina.edu.2024`).
5. **Save.** ¡El alumno ahora puede iniciar sesión!

### Paso 3: Verificar el Acceso al Portal (QA)
1. Vuelve al registro del Contact de **Lucas Martinez** en la aplicación.
2. Despliega el menú de opciones (▼ junto a los botones de acción, arriba a la derecha).
3. Selecciona **"Log in to Experience as User"**. Esto te mete directamente en la sesión del alumno dentro del portal sin necesidad de contraseña ni email de activación.
4. Verifica que el Campus Virtual carga correctamente con el nombre del alumno visible en la esquina superior derecha.

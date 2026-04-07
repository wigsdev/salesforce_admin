# 📚 GUÍA DE IMPLEMENTACIÓN: HU-S3-05
**Nombre:** Gestión de Contenido (Knowledge)
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce

### Paso 1: Armar las carpetas (Data Categories)
1. **Setup** → Quick Find → `Data Category Setup`.
2. Completa los detalles del grupo: Group Name: `Temas Lumina`, Group Unique Name: `Temas_Lumina`. Guarda.
3. Abajo, en Categories, pulsa Actions (Add Child Category) en la de nivel superior ("All"). Crea: `Academico`, `Administrativo`.
4. Arriba del todo, haz clic en **Activate**. *(Si no activas las Data Categories, ningún artículo te las mostrará).*

### Paso 2: Crear el Artículo
1. Ve al **App Launcher** (matriz de puntos a la izquierda) y abre la aplicación normal "Service" o busca **Knowledge**.
2. En la pestaña Knowledge haz clic en **New**.
3. Title: `¿Cuál es la escala de calificaciones?`
4. Escribe la respuesta clara en el cuerpo.
5. **CRÍTICO - Sección de visibilidad:** Busca unas casillas llamadas "Visible In Public Knowledge Base" y "Visible to Customer". **Marca AMBAS.** *(Si omites este check, el portal no mostrará el texto).*
6. Guárdalo y luego a la derecha haz click en **Publish** (¡Publicar!)

### Paso 3: Verlo en el Portal
1. Vuelve al **Experience Builder**.
2. En el panel de componentes (⚡), busca algo llamado "Article List" o "Trending Articles" o "Global Search for Peer-to-Peer Communities". Cualquiera de ellos.
3. Arrástralo a la página de Home. Verás unas barras grises (preview).
4. Dale a **Publish**. ¡Abre el sitio como anónimo y prueba a buscar las FAQ!

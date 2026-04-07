# 🛠️ GUÍA DE IMPLEMENTACIÓN: HU-S3-00
**Nombre:** Activación de la Plataforma de Portal
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce

*El pre-requisito absoluto. Sigue esto antes de hacer cualquier otra cosa.*

### Paso 1: Activar Digital Experiences
1. Ve al ícono del engranaje (⚙️) arriba a la derecha y selecciona **Setup**.
2. En el buscador rápido (Quick Find) de la izquierda, escribe `Digital Experiences` y haz clic en **Settings**.
3. Verás una casilla que dice **Enable Digital Experiences**. Múrcala (Check ✅).
4. El sistema te pedirá establecer un nombre de dominio (si no tienes uno). Ingresa `luminatech-[tus_iniciales]` y haz clic en **Check Availability**.
5. Haz clic en **Save** y luego en **OK**. *(Salesforce podría refrescar o pedirte iniciar sesión de nuevo; es normal).*

### Paso 2: Activar Knowledge
1. En **Setup**, escribe `Knowledge Settings` en el Quick Find.
2. Marca la casilla **Enable Lightning Knowledge**.
3. Haz clic en **Save**. Aparecerá una advertencia diciendo que no se puede deshacer. Acepta.

### Paso 3: Asignarte el permiso de Knowledge User (Crucial)
1. En **Setup**, busca `Users` en el Quick Find y entra.
2. Haz clic en **Edit** junto a tu propio nombre de usuario (el administrador con el que estás logueado).
3. Busca en la columna derecha una casilla llamada **Knowledge User** y márcala (Check ✅).
4. Haz clic en **Save**. *(Si no haces esto, la pestaña de Knowledge jamás te aparecerá).*

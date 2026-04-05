# 🛠️ Solución Técnica: Crear Reporte Independiente de Personas (Custom Report Type)

**Contexto**: Tu Salesforce no muestra el reporte de "Personas" solo, lo que obliga a que cada alumno tenga una Cuenta (Account) para aparecer. Si importaste los alumnos directo a Personas, están ocultos.

---

### Paso único: Crear el "Tipo de Reporte Personalizado"

1.  Ve a **Setup** (Engranaje) > **Report Types**.
2.  Si aparece una pantalla de bienvenida, dale a **Continue**.
3.  Haz clic en el botón **New Custom Report Type**.
4.  **Configuración del Reporte**:
    - **Primary Object**: Selecciona **Personas** (o `Contacts`).
    - **Report Type Label**: Pon `Personas (Standalone)`.
    - **Report Type Name**: Se llena solo.
    - **Description**: `Reporte para ver a todos los alumnos sin requerir cuenta`.
    - **Store in Category**: Elige `Accounts & Personas`.
    - **Deployment Status**: Selecciona **Deployed** (Desplegado) - ¡IMPORTANTE!.
5.  Dale a **Next**.
6.  En la pantalla de "Define Object Relationships", **no toques nada**. Debe decir solo `A: Personas`.
7.  Haz clic en **Save**.

---

### 📦 Paso 2: Asegurar que se vean tus Campos (VITAL)
*A diferencia de los reportes estándar, aquí debes añadir manualmente los campos que creaste (Rol, DNI, etc.) para que aparezcan en la lista de "Columnas".*

1.  En la misma pantalla donde guardaste el Report Type, baja hasta la sección **Fields Available for Reports**.
2.  Haz clic en el botón **Edit Layout**.
3.  En el panel de la derecha, verás una lista de campos. **Busca y arrastra** los campos `Rol`, `Número de Documento`, `DNI`, etc., hacia el cuadro de la izquierda.
4.  Haz clic en **Save**.

---

### ¿Cómo usarlo ahora?
Vuelve a la pestaña de **Reports** > **New Report** y busca el nuevo reporte llamado: **`Personas (Standalone)`**. 

Con este nuevo reporte, al poner el filtro **"All personas"** y **"All Time"**, verás a tus 500 alumnos de golpe. Aplicar la lógica de filtros de la [Guía 23](file:///c:/Users/WIGUSA/Documents/GitHub/admin_salesforce/content/Lumina_Tech/Guias_Implementacion_MOD/23-Tutorial_Reporte_Calidad_Datos_Es_Es.md) será ahora 100% efectivo. 🚀

# 📊 Guía Técnica: Dashboard Académico (Inscripciones) [HU-205A]

**Sprint**: 02 (Analítica y Seguridad)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-205A] Vision Académica

---

## 🎯 Objetivo
Configurar el Tablero de Control estratégico para la Rectora, permitiendo la visualización en tiempo real de la distribución de alumnos por carrera y año, con filtros dinámicos y segregación de acceso por carpetas.

## 🛠️ Procedimiento de Configuración

### Paso 1: Creación de la Carpeta de Seguridad
1.  Ve a la pestaña **Reportes** > **New Folder**.
2.  Nombre: `Reportes Directivos / Rectorado`.
3.  **Folder Sharing**:
    *   Compartir con Perfiles: `Lumina Rectorado` (View).
    *   Compartir con Roles: `CEO / Rectora` y `Gerentes`.
4.  Repite el proceso en la pestaña **Dashboards** con el nombre `Dashboard Directivo`.

### Paso 2: El Reporte Base (Source Report)
1.  **New Report** > **Inscripciones**.
2.  **Filtros**:
    *   `Estado__c` Equals `Activo, Cursando`. (Solo alumnos activos).
    *   `Fecha de Creación` Equals `All Time`.
3.  **Columnas**:
    *   `Alumno: Nombre`
    *   `Alumno: Apellido`
    *   `Numero de Documento`
    *   `ID Importacion`
4.  **Agrupación (Group Rows)**:
    *   **1º**: `Carrera_F__c` (O el nombre que le hayas dado al campo de fórmula de carrera).
    *   **2º**: `Anio_Lectivo__c` (Año).
5.  **Save & Run**: `Alumnos por Carrera y Año`. Guárdalo en la carpeta creada en el Paso 1.

### Paso 3: Configuración del Dashboard
1.  **Dashboards** > **New Dashboard**.
2.  Título: `Alumnos inscritos por Carrera`.
3.  Carpeta: `Dashboard Directivo`.
4.  **Configuración del Widget (Gráfico Torta)**:
    - Haz clic en el botón azul **+ Widget**.
    - Selecciona la opción **Chart or Table**.
    - Ahora busca y selecciona el reporte: `Alumnos por Carrera y Año`.
    - En **Display As**, selecciona el ícono de **Donut Chart** (Gráfico de Dona/Torta).
    - En el panel de la izquierda:
        *   **Chart Type**: Donut Chart.
        *   **Value**: `Record Count`.
        *   **Slice By**: Selecciona el campo de fórmula **`Carrera (F)`**.
    - Clic en **Add**.
5.  **Configuración del Filtro (Filtro Global)**:
    - Haz clic en **+ Filter** (arriba a la derecha).
    - **Field**: Busca y selecciona **`Año Lectivo`** (o `Anio_Lectivo__c`).
    - En **Filter Values**, haz clic en **Add Filter Value** para agregar cada opción:
        *   `2024-1`
        *   `2024-2`
        *   `2025-1`
        *   `2025-2`
    - Clic en **Apply**.

### Paso 4: Validación Relacional (Tabular)
Para cumplir con el requerimiento de validación manual en tiempo real:
1.  Agrega un segundo componente al Dashboard tipo **Table**.
2.  Muestra las columnas de detalle: `Alumno`, `Carrera`, `Estado_Socioeconomico__c` (o el campo que represente el segmento "desfavorecido recesivo").
3.  Esto permitirá a la Rectora comparar el gráfico de torta con la lista individual de alumnos de interés.

## ✅ Verificación de Éxito
1.  Entra como `Lumina Rectorado` y confirma que el Dashboard es visible.
2.  Entra como `Profesor` y confirma que el Dashboard **NO** es visible (Acceso Denegado).
3.  Cambia el filtro de año a `2025-1` y verifica que el gráfico de torta se actualice instantaneamente.

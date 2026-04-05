# 📊 Guía Técnica: Dashboard Gestión de Profesores [HU-206A]

**Sprint**: 02 (Analítica y Seguridad)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-206A] Gestión de Profesores

---

## 🎯 Objetivo
Configurar un tablero de control para monitorear la carga laboral docente (materias por profesor) y el ausentismo estudiantil por materia. Esto permite a Recursos Humanos y Rectoría balancear el trabajo y detectar problemas de asistencia.

---

## 🛠️ Procedimiento de Configuración

### Paso 1: Reporte de Carga Horaria
*Este reporte cuenta cuántas materias tiene asignadas cada profesor.*

1.  **New Report** > **Materias**.
2.  **Filtros (Filters)**:
    - **Show Me**: `All materias`.
    - **Fechas**: `All Time`.
3.  **Agrupación (Outline)**:
    - **Group Rows**: `Materia Owner` (o el campo que represente al Profesor).
4.  **Save & Run**: `Total de Materias por Profesor`. Guárdalo en la carpeta `Reportes Directivos`.

### Paso 2: Reporte de Ausentismo (HU-206B)
*Este reporte calcula el porcentaje de ausentismo por cada materia.*

1.  **New Report** > **Inscripciones**.
2.  **Filtros (Filters)**:
    - **Show Me**: `All inscriptions`.
    - **Año Lectivo**: `2024` o `2025` (según se necesite).
3.  **Columnas (Outline)**:
    - `Nombre de la Materia`.
    - `% Asistencia` (Campo de fórmula de la Guía 04).
4.  **Agrupación**:
    - **Group Rows**: `Materia__r.Name`.
5.  **Resumen de Datos**:
    - En el campo `% Asistencia`, haz clic en la flecha y elige **Summarize** > **Average** (Promedio).
6.  **Save & Run**: `Ausentismo por Materia`.

### Paso 3: Configuración del Dashboard
1.  **Dashboards** > **New Dashboard**.
2.  **Título**: `Gestión de Profesores y Asistencia`.
3.  **Carpeta**: `Dashboard Directivo`.
4.  **Widget 1 (Carga Docente)**:
    - **+ Widget** > **Chart or Table**.
    - Reporte: `Total de Materias por Profesor`.
    - **Display As**: **Horizontal Bar Chart** (Barras Horizontales).
    - **X-Axis**: `Record Count`.
    - **Y-Axis**: `Materia Owner`.
    - Clic en **Add**.
5.  **Widget 2 (Ranking de Ausentismo)**:
    - **+ Widget** > **Chart or Table**.
    - Reporte: `Ausentismo por Materia`.
    - **Display As**: **Lightning Table**.
    - **Values**: Mostrar el promedio de `% Asistencia`.
    - **Sort By**: `% Asistencia` (Ascendente para ver primero las materias con menos asistencia).
    - Clic en **Add**.

---

## ✅ Verificación de Éxito
1.  Busca a un profesor y asígnale una nueva materia.
2.  Refresca el Dashboard.
3.  El gráfico de barras debe mostrar el incremento inmediatamente.
4.  Confirma que solo Rectora y Gerentes pueden ver este Dashboard.

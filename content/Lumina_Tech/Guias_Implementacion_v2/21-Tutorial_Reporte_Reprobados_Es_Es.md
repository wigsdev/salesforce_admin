# 📊 Guía Técnica: Reporte de Alumnos Reprobados [HU-205B]

**Sprint**: 02 (Analítica y Seguridad)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-205B] Visión Académica

---

## 🎯 Objetivo
Configurar un reporte detallado y un widget de dashboard que permita a la Rectora identificar a los alumnos con rendimiento académico insuficiente (Estado = Desaprobado). Como nuestra data es histórica (2024-2025), crearemos una herramienta para filtrar mes a mes con precisión.

---

## 🛠️ Paso 1: Crear el Campo "Mes-Año" (En Object Manager)
*Antes de hacer el reporte, necesitamos un campo que Salesforce pueda usar para filtrar meses del pasado en el Dashboard.*

1.  Ve a **Setup** (Engranaje) > **Object Manager**.
2.  Busca y selecciona el objeto **Evaluación** (`Evaluacion__c`).
3.  Entra en **Fields & Relationships** y haz clic en **New**.
4.  Selecciona **Formula** y haz clic en **Next**.
5.  **Field Label**: `Mes Año (F)`.
6.  **Formula Return Type**: Elige **Text**. Haz clic en **Next**.
7.  En el cuadro de fórmula, pega lo siguiente:
    `TEXT(YEAR(Fecha_de_Examen__c)) & "-" & LPAD(TEXT(MONTH(Fecha_de_Examen__c)), 2, "0")`
8.  Haz clic en **Next**, luego **Next** y finalmente **Save**.

---

## 📊 Paso 2: Crear el Reporte Base
1.  Ve a la pestaña **Reports** y haz clic en **New Report**.
2.  Busca el tipo de reporte **Evaluaciones** y haz clic en **Start Report**.
3.  **Configurar Filtros (Pestaña Filters)**:
    - **Show Me**: Cámbialo a `All evaluations` y dale a **Done**.
    - **Fecha de Examen**: Cámbialo a `All Time` (Para que aparezca 2024 y 2025).
    - **Add Filter**: Busca el campo **Estado** y pon `Equals` `Desaprobado`.
4.  **Configurar Columnas (Pestaña Outline)**:
    - En la sección **Columns**, busca y agrega el campo que creamos: **`Mes Año (F)`**. (¡ESTO ES VITAL para que el Dashboard lo reconozca!).
    - Agrega también: `Alumno (F)`, `Materia (F)`, `Examen Final`.
5.  **Grouping**:
    - En **Group Rows**, agrega `Mes Año (F)` para que el reporte se ordene por meses.
6.  **Save & Run**: Título `Reporte Maestro de Reprobados`. Guárdalo en la carpeta `Reportes Directivos`.

---

## 🍰 Paso 3: Crear el Dashboard Independiente
*Para evitar mezclar la data de inscripciones con la de reprobados, crearemos un tablero nuevo y limpio.*

1.  Ve a la pestaña **Dashboards** y haz clic en **New Dashboard**.
2.  **Título**: `Control de Calidad: Alumnos Reprobados`.
3.  **Carpeta**: `Dashboard Directivo`.
4.  **Añadir el Widget**:
    - Haz clic en el botón azul **+ Widget** > **Chart or Table**.
    - Selecciona el reporte: `Reporte Maestro de Reprobados`.
    - **Display As**: Elige **Lightning Table** (para ver la lista) o **Gauge/Metric** (para ver solo el número total).
    - **Value**: Selecciona **Record Count** (Cuenta de Registros).
    - Haz clic en **Add**.
5.  **Añadir el Filtro de Mes**:
    - Haz clic en **+ Filter** (arriba a la derecha).
    - **Field**: Busca y selecciona tu nuevo campo **`Mes Año (F)`**.
    - Haz clic en **Add Filter Value** para agregar los meses que necesites (ej: `2024-03`, `2024-04`).
    - En **Display Name**, pon el nombre legible (ej: "Marzo 2024").
    - Haz clic en **Apply**.
6.  Haz clic en **Save** y luego en **Done**.

---

## 🔄 Paso 4: Sincronizar Columnas (IMPORTANTE)
*Cuando agregas campos nuevos al reporte (como DNI o Email), Salesforce Lightning **no** los pone automáticamente en el cuadro del Dashboard. Debes hacerlo a mano.*

1.  Ve al Dashboard y haz clic en **Edit**.
2.  Busca el componente (la tabla) de "Alumnos Reprobados" y haz clic en el icono del **Lápiz** (Edit Component).
3.  En el panel de la derecha, busca la sección **Columns**.
4.  Haz clic en **+ Column** y busca el nombre del campo (ej: `DNI` o `Email`).
5.  **Reordenar**: Puedes arrastrar los campos hacia arriba o abajo para que queden en el orden que el cliente pidió (Alumno → DNI → Email → Materia → Nota).
6.  Haz clic en **Update** (en el componente) y luego en **Save** (en el Dashboard).
7.  Haz clic en **Done** y finalmente en el botón **Refresh**.

---

---

## 🆘 ¿Por qué no filtra? (Resolución de Problemas)
Si pones `2024-03` y el Dashboard no cambia, revisa estos 3 puntos en orden:

1.  **Refrescar el Dashboard**:
    - Después de hacer cualquier cambio en el reporte o en el filtro, debes hacer clic en el botón **Refresh** (Actualizar) del Dashboard. Si no, estarás viendo datos viejos.

2.  **Verificar el Mapeo (Equivalent Field)**:
    - Entra en **Edit** en el Dashboard.
    - Haz clic en el icono del **Lápiz** sobre el filtro de `Mes Año (F)`.
    - Asegúrate de que para tu Widget de reprobados, en la columna de la derecha, esté seleccionado el campo `Mes Año (F)`. Si dice "No selection", el filtro no sabe a qué columna del reporte atacar.

3.  **Verificar el Formato en el Reporte**:
    - Ve a tu reporte `Reporte Maestro de Reprobados` y dale a **Run**.
    - Mira la columna `Mes Año (F)`. ¿Dice exactamente `2024-03`? 
    - Si dice `2024-3` (sin el cero), entonces el valor del filtro debe ser `2024-3`. La coincidencia debe ser **exacta**.

## ✅ Verificación Final
Si el reporte muestra `2024-03` y el filtro del Dashboard apunta a esa misma columna, al elegir el valor el gráfico DEBE filtrarse.

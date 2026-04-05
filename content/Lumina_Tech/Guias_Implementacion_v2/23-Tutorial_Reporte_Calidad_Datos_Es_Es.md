# 📊 Guía Técnica: Reporte de Calidad de Datos y Auditoría [HU-207A]

**Sprint**: 02 (Analítica y Auditoría)
**Rol Responsable**: 🛡️ **Salesforce Admin** / **Rectora**
**HUs Relacionadas**: [HU-207A] Calidad de Datos

---

## 🎯 Objetivo
Crear un reporte que identifique registros de alumnos con información de contacto faltante (Email o Teléfonos). Este reporte es crítico para que el equipo administrativo realice limpiezas de datos y mantenga la comunicación fluida con los estudiantes de Lumina Tech.

---

## 🛠️ Paso 1: Configurar el Reporte Base
1.  Ve a la pestaña **Reports** y haz clic en **New Report**.
2.  En el buscador, selecciona **Personas (Standalone)**. (Creado previamente en la [Guía 24](file:///c:/Users/WIGUSA/Documents/GitHub/admin_salesforce/content/Lumina_Tech/Guias_Implementacion_MOD/24-Solucion_Custom_Report_Type_Personas_Es_Es.md)).
3.  Haz clic en **Start Report**.

---

## 🔍 Paso 2: Configuración de Filtros (Lógica OR)
*Este es el paso más importante para capturar solo los alumnos con datos incompletos.*

1.  Ve a la pestaña **Filters**:
    - **Show Me**: Selecciónalo como **`All personas`**.
    - **Created Date**: `All Time`.
    - **Rol**: Busca el campo `Rol` y pon `Equals` `Alumno`.
2.  **Añadir Filtros de Vacío**:
    - Agrega: `Email` `equals` `""` (déjalo en blanco).
    - Agrega: `Phone` `equals` `""` (déjalo en blanco).
    - *Nota: No incluimos Mobile aquí porque es un campo vacío para toda la base por el momento.*
3.  **Configurar Lógica de Filtros**:
    - Haz clic en la flecha pequeña junto a **Filters** y selecciona **Add Filter Logic**.
    - La lógica debe ser: **`1 AND (2 OR 3)`**
    - *Esto significa: Solo Alumnos (1) QUE no tengan email (2) O no tengan teléfono (3).*

---

## 📋 Paso 3: Diseño de Columnas y Agrupación
1.  Ve a la pestaña **Outline**:
    - **Columns**: Deja `First Name`, `Last Name`, `Email`, `Phone`, `Mobile`.
    - **Group Rows**: Busca el campo `Tipo de Documento` y agrégalo como agrupación. *Esto permitirá ver si la falta de datos es frecuente en ciertos tipos de documento.*
2.  Asegúrate de que la opción **Detail Rows** esté activa (abajo) para ver el listado de alumnos.

---

## 📁 Paso 4: Ubicación y Seguridad
1.  Haz clic en **Save & Run**.
2.  **Report Name**: `Alumnos con datos incompletos`.
3.  **Description**: Listado de alumnos con Email o Teléfonos faltantes para auditoría de administración.
4.  **Select Folder**:
    - Si no existe, crea la carpeta **Auditoría y Calidad**.
    - **Compartir (Sharing):** Asegúrate de habilitar el acceso a esta carpeta solo para los Roles: `Rectorado`, `System Administrator` y `Gerentes`.

---

## ✅ Criterios de Aceptación (Checklist)
- [ ] El reporte utiliza el tipo **"Personas (Standalone)"**.
- [ ] El filtro Show Me es **"All personas"**.
- [ ] La lógica de filtros es **`1 AND (2 OR 3)`**.
- [ ] Mobile es visible como columna pero **no** se usa como filtro.
- [ ] Está guardado en la carpeta `Auditoría y Calidad`.

# 🎓 Guía Técnica: Carga de Datos (Data Loader)

**Sprint**: 01 (Fundamentos)
**Día**: 0/1 (Preparación)
**Rol Responsable**: ♾️ **DevOps Specialist**
**HUs Relacionadas**: [HU-General](../../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Carga Inicial)

---

## 🎯 Objetivo
Dejar de cargar alumnos "a mano". Aprenderemos a subir 50 (o 500) registros de golpe desde un Excel.

## 🛠️ Procedimiento

### Paso 1: Preparar el CSV (La parte más importante)
Salesforce no lee tu mente, lee columnas exactas.

1.  Abre Excel o Google Sheets.
2.  Crea un encabezado EXACTO con los nombres de tus campos:
    *   `First Name`
    *   `Last Name`
    *   `National ID`
    *   `Personal Email`
    *   `Phone`
    *   `Date of Birth` (YYYY-MM-DD)
3.  Llena con datos de prueba (Mínimo 5 filas).
    *   *Ejemplo*: Juan, Perez, 111222, juan@lumina.edu, 555-0101, 1990-05-15
4.  **Guardar como**:
    *   Haz clic en **Archivo** > **Guardar como**.
    *   Selecciona formato **CSV (Delimitado por comas)**.
    *   Nombre archivo: `Student_Load_v1.csv`.

> ⚠️ **Advertencia**: Si usas fechas, el formato debe ser `DD/MM/YYYY` o `YYYY-MM-DD` dependiendo de tu configuración regional.

### Paso 2: Ejecutar Data Import Wizard
1.  Ve a **Setup** (Engranaje).
2.  En el buscador rápido (Quick Find), escribe: `Data Import Wizard`.
3.  Selecciona la opción **Data Import Wizard**.
4.  Haz clic en el botón verde **Launch Wizard**.

### Paso 3: Configurar la Importación
1.  **¿Qué tipo de datos?**: Haz clic en la pestaña azul **Custom Objects**.
2.  Selecciona **Students**.
3.  **¿Qué quieres hacer?**: Haz clic en **Add new records**.
4.  **Match by**: Déjalo en `--None--` (o selecciona **National ID** si estuvieras actualizando datos existentes).
5.  **Where is your data?**:
    *   Haz clic en **CSV**.
    *   Haz clic en **Choose File** (o arrastra tu archivo) y selecciona `Student_Load_v1.csv`.
6.  Haz clic en **Next**.

### Paso 4: Mapeo de Campos (Mapping)
*Aquí conectas tu Excel con Salesforce.*

1.  Verás dos columnas: "CSV Header" y "Salesforce Field".
2.  Si los nombres coinciden, Salesforce los mapea automáticamente.
3.  Si alguno dice "Unmapped" (en rojo):
    *   Haz clic en **Map**.
    *   Busca el campo correcto en la lista (ej: Tu Excel dice "Celular" y Salesforce es "Phone").
    *   Haz clic en **Map**.
4.  Cuando todo esté verde (Mapped), haz clic en **Next**.

### Paso 5: Ejecución y Auditoría
1.  Revisa el resumen (Verifica que el número de columnas sea correcto).
2.  Haz clic en **Start Import**.
3.  Haz clic en **OK**.
4.  Serás redirigido a la pantalla de estado. Espera a que la barra de progreso llegue al 100%.
    *   Estado: `Queued` -> `Processing` -> `Completed`.
5.  Si ves **Failures**: Haz clic en **View Result** para descargar el CSV de errores y ver qué pasó.

---

## ✅ Verificación de Éxito
1.  Ve a tu App **Academic Management**.
2.  Haz clic en la pestaña **Students**.
3.  Cambia la vista (arriba a la izquierda) de "Recently Viewed" a **"All"**.
4.  ¡Deberías ver a todos los alumnos nuevos en la lista! 🧙‍♂️

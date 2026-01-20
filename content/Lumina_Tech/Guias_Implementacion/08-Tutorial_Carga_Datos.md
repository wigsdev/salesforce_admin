# 🎓 Guía Paso a Paso: Carga Masiva de Datos (Data Loading)
**Nivel**: Intermedio
**Tiempo Estimado**: 30 minutos
**Herramienta**: Data Import Wizard (Asistente de Importación)

---

## 🎯 Objetivo
Dejar de cargar alumnos "a mano". Aprenderemos a subir 50 (o 500) registros de golpe desde un Excel.

## 🛠️ Procedimiento

### Paso 1: Preparar el CSV (La parte más importante)
Salesforce no lee tu mente, lee columnas exactas.
1.  Abre Excel o Google Sheets.
2.  Crea un encabezado EXACTO con los nombres de tus campos:
    *   `Nombre`
    *   `Apellido`
    *   `DNI`
    *   `Email`
3.  Llena con datos de prueba (Mínimo 5 filas).
    *   *Ejemplo*: Juan, Perez, 111222, juan@lumina.edu
4.  **Guardar como**: Selecciona formato **CSV (Delimitado por comas)**.
    *   Nombre archivo: `Carga_Alumnos_v1.csv`.

> ⚠️ **Advertencia**: Si usas fechas, el formato debe ser `DD/MM/YYYY` o `YYYY-MM-DD` dependiendo de tu configuración regional.

### Paso 2: Ejecutar Data Import Wizard
1.  **Setup**.
2.  En el buscador rápido escribe: **Data Import Wizard** (o Asistente de Importación de Datos).
3.  Click en el botón verde **Launch Wizard**.

### Paso 3: Configurar la Importación
1.  **¿Qué tipo de datos?**: Click en **Custom Objects**.
2.  Selecciona **Alumnos**.
3.  **¿Qué quieres hacer?**: Click en **Add new records**.
4.  **Match by**: Dejar vacío (o seleccionar DNI si estuvieras actualizando).
5.  **Where is your data?**:
    *   Arrastra tu archivo `Carga_Alumnos_v1.csv` a la zona de carga.
    *   Click **Next**.

### Paso 4: Mapeo de Campos (Mapping)
*Aquí conectas tu Excel con Salesforce.*
1.  Verás dos columnas: "CSV Header" y "Salesforce Field".
2.  Si los nombres coinciden, Salesforce los mapea solo.
3.  Si alguno dice "Unmapped" (en rojo):
    *   Click en **Map**.
    *   Busca el campo correcto (ej: Tu Excel dice "Celular" y Salesforce es "Teléfono").
    *   Click **Map**.
4.  Cuando todo esté verde, click **Next**.

### Paso 5: Ejecución y Auditoría
1.  Revisa el resumen (cuántos campos, cuántas columnas).
2.  Click **Start Import**.
3.  Click **OK**.
4.  Serás redirigido a la pantalla de "Bulk Data Load Jobs".
    *   Estado: `Queued` -> `Processing` -> `Completed`.
5.  Si ves **Failures**: Descarga el "Result File" para ver qué fila falló (ej: Email duplicado o DNI faltante).

---

## ✅ Verificación de Éxito
1.  Ve a tu App **Gestión Académica**.
2.  Click en la pestaña **Alumnos**.
3.  Cambia la vista de "Recently Viewed" a **"All"**.
4.  ¡Deberías ver a todo tu ejército de alumnos cargado mágicamente! 🧙‍♂️

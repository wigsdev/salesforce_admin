# 🎓 Guía Técnica: Carga de Datos (Data Import Wizard)

**Sprint**: 01 (Fundamentos)
**Día**: 0/1 (Preparación)
**Rol Responsable**: ♾️ **DevOps Specialist**
**HUs Relacionadas**: [HU-General](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Carga Inicial)

---

## 🎯 Objetivo
Dejar de cargar alumnos "a mano". Aprenderemos a subir 50 (o 500) registros de golpe desde una planilla de cálculo (Excel).

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Paso 1: Preparar el CSV (La parte más importante)
Salesforce no lee tu mente, lee columnas.

1.  Abre Excel o Google Sheets.
2.  Crea un encabezado claro con los nombres de tus campos (pueden ser en español):
    *   `Nombres`
    *   `Apellidos`
    *   `DNI`
    *   `Email Personal`
    *   `Telefono`
    *   `Fecha Nacimiento`
3.  Llena con datos de prueba (Mínimo 5 filas).
    *   *Ejemplo*: Juan, Perez, 11122233, juan@lumina.edu, 555-0101, 15/05/1990
4.  **Guardar como**:
    *   Haz clic en **Archivo** > **Guardar como** (o Descargar).
    *   Selecciona formato **CSV (Delimitado por comas)**.
    *   Nombre archivo: `Carga_Alumnos_v1.csv`.

> ⚠️ **Advertencia**: Si usas fechas, el formato recomendado es `DD/MM/YYYY` (LatAm) o `YYYY-MM-DD` (ISO). Verifica la configuración regional de tu usuario en Salesforce si da error.

### Paso 2: Ejecutar Data Import Wizard
1.  Ve a **Setup** (Engranaje).
2.  En el buscador rápido (Quick Find), escribe: `Data Import Wizard`.
3.  Selecciona la opción **Data Import Wizard**.
4.  Haz clic en el botón verde **Launch Wizard**.

### Paso 3: Configurar la Importación
1.  **¿Qué tipo de datos?**: Haz clic en la pestaña azul **Custom Objects**.
2.  Selecciona **Alumnos** (`Alumno`).
3.  **¿Qué quieres hacer?**: Haz clic en **Add new records** (Agregar nuevos registros).
4.  **Match by**: Déjalo en `--None--` (o selecciona **DNI** si estuvieras actualizando datos existentes para no duplicar).
5.  **Where is your data?**:
    *   Haz clic en **CSV**.
    *   Haz clic en **Choose File** (o arrastra tu archivo) y selecciona `Carga_Alumnos_v1.csv`.
6.  Haz clic en **Next**.

### Paso 4: Mapeo de Campos (Mapping)
*Aquí conectas tu Excel con Salesforce.*

1.  Verás dos columnas: "CSV Header" (Tu Excel) y "Salesforce Field" (La Base de Datos).
2.  Salesforce intentará adivinar. Si no coinciden, verás "Unmapped" (en rojo).
3.  **Mapeo Manual**:
    *   Haz clic en **Map** al lado de cada campo rojo.
    *   Busca el campo correcto en la lista:
        *   `Nombres` -> Mapear a `Nombres`
        *   `Apellidos` -> Mapear a `Apellidos`
        *   `DNI` -> Mapear a `DNI`
        *   `Email Personal` -> Mapear a `Email Personal` (API: `Email_Personal__c`)
    *   Haz clic en **Map**.
4.  Cuando todo esté verde (Mapped), haz clic en **Next**.

### Paso 5: Ejecución y Auditoría
1.  Revisa el resumen (Verifica que el número de columnas sea correcto).
2.  Haz clic en **Start Import**.
3.  Haz clic en **OK**.
4.  Serás redirigido a la pantalla de estado. Espera a que la barra de progreso llegue al 100%.
    *   Estado: `Queued` -> `Processing` -> `Completed`.
5.  Si ves **Failures**: Haz clic en **View Result** para descargar el CSV de errores y ver qué pasó (ej: un DNI duplicado o formato incorrecto).

---

## ✅ Verificación de Éxito
1.  Ve a tu App **Gestión Académica Lumina**.
2.  Haz clic en la pestaña **Alumnos**.
3.  Cambia la vista (arriba a la izquierda) de "Recently Viewed" a **"All"** (Todos).
4.  ¡Deberías ver a todos los alumnos nuevos de tu Excel en la lista! 🧙‍♂️

# 🎓 Guía Técnica: Objeto Carrera (Master Data)

**Sprint**: 01 (Fundamentos)
**Día**: 1 (Modelado de Datos)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-003 (Soporte a Estructura)

---

## 🎯 Objetivo
Crear el objeto `Carrera__c` que almacenará los planes de estudio de la universidad. Este será un objeto "Padre".

## 🛠️ Procedimiento

### Paso 1: Configuración Inicial
1.  Haz clic en el ícono de engranaje ⚙️ (arriba a la derecha) y selecciona **Setup**.
2.  En la barra superior, haz clic en la pestaña **Object Manager**.
3.  Haz clic en el botón **Create** (arriba a la derecha) y selecciona **Custom Object**.

### Paso 2: Definición del Objeto
Complete los campos con EXACTITUD:

1.  **Label**: Escribe `Carrera`.
2.  **Plural Label**: Escribe `Carreras`.
3.  **Object Name**: `Carrera` (Se llena automático).
4.  **Record Name**: Escribe `Código de Carrera`.
5.  **Data Type**: Selecciona **Auto Number** en el menú desplegable.
6.  **Display Format**: Escribe `CAR-{0000}`.
7.  **Starting Number**: Escribe `1`.
8.  En la sección "Optional Features", marca la casilla: ☑️ **Track Field History**.
9.  En la sección "Search Status", marca la casilla: ☑️ **Allow Search**.
10. Haz clic en **Save**.

### Paso 3: Crear Campos (Duración)
1.  En el menú izquierdo del objeto Carrera, haz clic en **Fields & Relationships**.
2.  Haz clic en el botón **New**.
3.  Selecciona Data Type: **Number**. Haz clic en **Next**.
4.  Completa los detalles:
    *   **Field Label**: `Duración (Años)`
    *   **Length**: `2`
    *   **Decimal Places**: `0` (Enteros)
    *   Marca la casilla: ☑️ **Required**.
5.  Haz clic en **Next**.
6.  Haz clic en **Next** (Add to Page Layout).
7.  Haz clic en **Save**.

---

## ✅ Verificación de Éxito
1.  Haz clic en el **App Launcher** (9 puntos).
2.  Escribe y selecciona "Carreras".
3.  Haz clic en **New**.
4.  Completa la duración (ej: 5) y **Save**.
5.  Verifica que se generó un código como `CAR-0001`.

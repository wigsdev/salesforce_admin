# 🎓 Guía Paso a Paso: Creación de Objeto Carrera
**Nivel**: Principiante
**Tiempo Estimado**: 10 minutos
**Rol**: Salesforce Admin

---

## 🎯 Objetivo
Crear el objeto `Carrera__c` que almacenará los planes de estudio de la universidad. Este será un objeto "Padre".

## 🛠️ Procedimiento

### Paso 1: Configuración Inicial
1.  Haga clic en el ícono de engranaje ⚙️ y seleccione **Setup**.
2.  En la barra superior, haga clic en la pestaña **Object Manager**.
3.  Haga clic en el botón **Create** (arriba a la derecha) > **Custom Object**.

### Paso 2: Definición del Objeto
Complete los campos con EXACTITUD:

*   **Label**: `Carrera`
*   **Plural Label**: `Carreras`
*   **Object Name**: `Carrera` (Automático)
*   **Record Name**: `Código de Carrera`
*   **Data Type**: Seleccione **Auto Number**
*   **Display Format**: `CAR-{0000}`
*   **Starting Number**: `1`

> ⚠️ **Audit Features**: Marque la casilla **Track Field History**.

*   **Deployment Status**: Deje en **Deployed**.
*   **Search Status**: Marque **Allow Search**.

Haga clic en **Save**.

### Paso 3: Crear Campos (Duración)
1.  En el menú izquierdo, vaya a **Fields & Relationships**.
2.  Haga clic en **New**.
3.  Seleccione Data Type: **Number**. Next.
4.  Complete:
    *   **Field Label**: `Duración (Años)`
    *   **Length**: `2`
    *   **Decimal Places**: `0` (Enteros)
    *   **Required**: ☑️ Marcado.
5.  **Next** > **Next** (Visible a todos) > **Save**.

---

## ✅ Verificación de Éxito
1.  Vaya al **App Launcher** (9 puntos).
2.  Busque "Carreras".
3.  Intente crear una nueva.
4.  Debería ver el campo "Duración" y el Código debería generarse solo (ej: CAR-0001) al guardar.

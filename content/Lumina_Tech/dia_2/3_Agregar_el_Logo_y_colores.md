# 🖌️ Agregar el Logo y colores

**Rol Responsable**: 🛡️ **Salesforce Admin**
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../Gestor_de_Versiones/03-Salesforce_Admin.md) (UI & Branding)

## Implementación de Themes & Branding

### 1. Preparación de Assets
*   **Logo**: Archivo `.png` con fondo transparente. Max 600x120px.
*   **Brand Color**: `#005A9C` (Lumina Blue).

### 2. Configuración en Salesforce (Click-Path)
1.  Ir a **Setup** > **Themes and Branding**.
2.  Click en **New Theme**.
3.  **Details**:
    *   Theme Name: `Lumina Official`.
    *   API Name: `Lumina_Official`.
4.  **Branding**:
    *   **Brand Image**: Subir `logo_lumina.png`.
    *   **Brand Color**: Ingresar `#005A9C`.
    *   **Page Background Color**: Ingresar `#F4F6F9` (Soft Grey).
5.  **Save** y luego **Activate**.

### 3. Creación de la App "Gestión Académica Lumina"
El tema por sí solo no basta; necesitamos una "App" (contenedor de pestañas).
1.  Ir a **Setup** > **App Manager** > **New Lightning App**.
2.  **App Details**:
    *   Name: `Gestión Académica Lumina`.
    *   Developer Name: `Gestion_Academica_Lumina`.
    *   Color: `#005A9C`.
3.  **Navigation Items**:
    *   Agregar: `Home`, `Alumnos`, `Carreras`, `Materias`, `Inscripciones`, `Exámenes`.
4.  **User Profiles**:
    *   Asignar a: `System Administrator`, `Lumina Administrativo`, `Lumina Profesor`.

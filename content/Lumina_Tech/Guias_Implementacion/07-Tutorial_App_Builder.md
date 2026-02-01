# 🎓 Guía Técnica: Lightning App (Branding & Navigation)

**Sprint**: 01 (Fundamentos)
**Día**: 2 (App Building)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: HU-004 (Dominio), HU-005 (Theme), HU-006 (App)

---

## 🎯 Objetivo
Transformar una lista de objetos aburridos en una **Aplicación Profesional**.

## 🛠️ Procedimiento

### Paso 1: My Domain (Identidad - HU-004)
*Requisito obligatorio para componentes modernos.*
1.  **Setup > My Domain**.
2.  En "My Domain Details", click **Edit**.
3.  Cambia el nombre a algo como: `lumina-university-[tunombre]`.
4.  Click **Save**.
5.  Espera 2 minutos y refresca la página.
6.  Click **Deploy to Users**. (¡Crucial!).

### Paso 2: Configurar Temas y Marca (Theming - HU-005)
1.  **Setup > User Interface > Themes and Branding**.
2.  Click **New Theme**.
3.  **Theme Details**:
    *   Theme Name: `Lumina Official`.
4.  **Branding**:
    *   **Brand Color**: `#005A9C` (Lumina Blue).
    *   **Brand Image (Logo)**: Sube el logo corporativo.
5.  **Save** > **Activate**.

### Paso 3: Crear la Lightning App (HU-006)
1.  **Setup > App Manager**.
2.  Click **New Lightning App**.
3.  **App Details**:
    *   Name: `Gestión Académica Lumina`.
    *   Color: `#005A9C`.
4.  **Navigation Items** (Mueve a la derecha):
    *   Home, Alumnos, Carreras, Materias, Inscripciones.
5.  **User Profiles**:
    *   System Administrator, Lumina Profesor, Lumina Bedel.
6.  **Save & Finish**.

---

## ✅ Verificación de Éxito
1.  Mira la URL de tu navegador. ¿Dice `lumina-university...`? ✅
2.  Abre el App Launcher. ¿Ves "Gestión Académica Lumina"? ✅
3.  ¿El sistema es Azul Lumina en lugar del Azul Salesforce default? ✅

¡Transformación Digital completada! 🏛️

# 🎓 Guía Técnica: Lightning App (Identidad & Navegación)

**Sprint**: 01 (Fundamentos)
**Día**: 2 (App Building)
**Rol Responsable**: 🛡️ **Salesforce Admin**
**HUs Relacionadas**: [HU-004](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Dominio), [HU-005](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (Theme), [HU-006](../../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES.md) (App)

---

## 🎯 Objetivo
Transformar una lista de objetos aburridos en una **Aplicación Profesional** que la Rectora pueda usar. Aplicaremos los colores institucionales y configuraremos el dominio propio.

> **⚠️ Nota de Localización**
> Todos los nombres técnicos (API Names) se definirán en **Español** siguiendo la convención:
> *   Sin tildes (`á` -> `a`).
> *   `ñ` -> `ni` (Ej: `Año` -> `Anio`).

## 🛠️ Procedimiento

### Paso 1: My Domain (Identidad - HU-004)
*Requisito obligatorio para que funcionen los componentes modernos.*

1.  Ve a **Setup** y busca **My Domain** en la barra Quick Find.
2.  En la sección "My Domain Details", haz clic en **Edit**.
3.  En el campo "My Domain Name", escribe: `lumina-tech-university`.
    *   *URL Resultante*: `https://lumina-tech-university-dev-ed.trailblaze.my.salesforce.com/`
4.  Haz clic en **Save**.
5.  **ESPERA**: Salesforce mostrará un mensaje de "Provisioning". Espera unos 2 minutos.
6.  Refresca la página del navegador (F5).
7.  **¡IMPORTANTE!**: Verás un botón nuevo que dice **Deploy to Users**. Haz clic en él.
8.  Haz clic en **OK** en el mensaje de confirmación.

### Paso 2: Configurar Temas y Marca (Theming - HU-005)
1.  Busca **Themes and Branding** en Setup.
2.  Haz clic en **New Theme**.
3.  **Theme Details**:
    *   **Theme Name**: `Lumina Oficial`.
    *   **API Name**: `Lumina_Oficial`.
4.  **Branding** (Colores Institucionales):
    *   **Brand Color**: `#005A9C` (Lumina Blue).
    *   **Page Background Color**: `#F4F6F9` (Soft Grey).
    *   **Global Header Background Color**: `#00477D` (Deep Blue).
    *   **Link Color**: Desmarca la casilla "Use brand color". **Si no aparece el cuadro de color**, vuelve a marcarla y continúa (usaremos el azul por defecto).
    *   **Brand Image**: Sube el archivo `lumina_logo_header.png` (tiene fondo azul para integrarse).
    
    > **⚠️ Nota de Diseño (Colores Semánticos)**
    > Los colores **Tech Gold** (`#F2A900`) y **Growth Green** (`#4BCA81`) definidos en la identidad se reservarán para indicadores de estado (Path) y gráficos de éxito en futuras configuraciones. No se aplican en esta pantalla global.

5.  Haz clic en **Save**.

#### Paso 2.1: Imágenes Avanzadas (Opción Completa)
*Para completar la identidad visual al 100% (Banners y Avatares).*
1.  En la misma pantalla del Tema, haz clic en la pestaña **Images** (junto a Branding).
2.  Los archivos se encuentran en tu carpeta del proyecto:
    `content/Lumina_Tech/Recursos_Graficos/Theme/`
3.  Sube los archivos correspondientes:
    *   **Page Background Image**: `lumina_banner.png`
    *   **Default Group Banner**: `lumina_banner.png`
    *   **Default User Profile Banner**: `lumina_banner.png`
    *   **Default Group Avatar**: `lumina_avatar_group.png`
    *   **Default User Profile Avatar**: `lumina_avatar_user.png`
4.  Haz clic en **Save**.
5.  Haz clic en **Activate** (arriba a la derecha) si no lo has hecho.
6.  Una vez guardado, haz clic en el botón **Activate** (arriba a la derecha) para aplicarlo.

### Paso 3: Crear la Lightning App (HU-006)
1.  Busca **App Manager** en Setup.
2.  Haz clic en el botón **New Lightning App** (arriba a la derecha).
3.  **App Details & Branding**:
    *   **App Name**: `Gestión Académica Lumina` (Lumina Academic Management).
    *   **Developer Name**: `Gestion_Academica_Lumina` (Validado por Req. Identidad).
    *   **Description**: *Plataforma integral para la gestión de alumnos, inscripciones y notas de la Universidad Lumina Tech.*
    *   **Image**: Haz clic en **Upload** y selecciona el logo de tu organización.
    *   **Primary Color Hex Value**: Escribe `#005A9C` (Azul Lumina).
    *   Haz clic en **Next**.
4.  **App Options**:
    *   **Navigation Style**: Selecciona **Standard Navigation**.
    *   **Supported Form Factors**: Selecciona **Desktop and Phone**.
    *   **Setup Experience**: Selecciona **Setup**.
    *   Haz clic en **Next**.
5.  **Utility Items (Utility Bar)**:
    *   No agregaremos elementos por ahora.
    *   Haz clic en **Next**.
6.  **Navigation Items** (El menú de la app):
    *(Si no encuentras los objetos, sigue el PASO 6.0 abajo primero).*
    *   En la lista **Available Items** (izquierda), usa el buscador o desplázate.
    *   Selecciona y agrega en este orden exacto:
        1.  **Home** (Inicio)
        2.  **Contactos** (El objeto estándar que gestiona a los Alumnos)
        3.  **Carreras**
        4.  **Materias**
        5.  **Inscripciones**
        6.  **Asistencias**
        7.  **Evaluaciones** (Gestión de Notas)
        8.  **Cobros** (Gestión de Tesorería)
    *   Haz clic en **Next**.

#### ⚠️ Paso 6.0: Recuperación - Crear Pestañas (Si no aparecen)
*Si no ves Carreras/Materias/etc en la lista, es porque no creamos sus "Tabs" al definir los objetos.*
1.  **Guarda** tu progreso en el App Builder (botón **Save** arriba > **Activate later** si pregunta).
2.  Vuelve al **Setup** principal en otra pestaña del navegador.
3.  Busca **Tabs** en el Quick Find.
4.  En "Custom Object Tabs", haz clic en **New**.
5.  **Object**: Selecciona `Carrera`. **Tab Style**: Elige cualquiera (ej: "Building"). **Next**.
6.  **Profiles**: "Apply one tab visibility to all profiles" > **Default On**. **Next**.
7.  **Apps**: Desmarca "Include Tab". **Save**.
8.  **Repite** para `Materia`, `Inscripción`, `Asistencia`, `Evaluación` y `Cobro`. *(Nota: Contactos ya existe por ser objeto estándar).*
9.  Vuelve al App Manager y retoma la edición de tu App. Ahora sí aparecerán.

7.  **User Profiles** (Quién puede ver la app):
    *   Mueve a la derecha: `System Administrator` (Administrador del Sistema).
    *   Mueve a la derecha: `Lumina Professor`.
    *   Mueve a la derecha: `Lumina Registrar`.
    *   Haz clic en **Save & Finish**.

---

## ✅ Verificación de Éxito
1.  Mira la URL de tu navegador. ¿Dice `lumina-tech...`? ✅
2.  Haz clic en el **App Launcher** (los 9 puntos arriba a la izquierda).
3.  Escribe "Gestión" en el buscador. Haz clic en **Gestión Académica Lumina**.
4.  ¿Ves el logo que subiste? ¿El color de fondo es azul `#005A9C`? ✅
5.  Verifica que las pestañas (Tabs: Alumnos, Materias, etc.) funcionan correctamente.

¡Has creado una App Corporativa Real! 🏛️

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
3.  En el campo "My Domain Name", escribe un nombre único.
    *   *Ejemplo*: `lumina-tech-[tu-apellido]`. (Si dice "Available", procede).
4.  Haz clic en **Save**.
5.  **ESPERA**: Salesforce mostrará un mensaje de "Provisioning". Espera unos 2 minutos.
6.  Refresca la página del navegador (F5).
7.  **¡IMPORTANTE!**: Verás un botón nuevo que dice **Deploy to Users**. Haz clic en él.
8.  Haz clic en **OK** en el mensaje de confirmación.
    *   *Resultado*: Ahora la URL de tu navegador cambiará para mostrar tu nuevo dominio.

### Paso 2: Configurar Temas y Marca (Theming - HU-005)
1.  Busca **Themes and Branding** en Setup.
2.  Haz clic en **New Theme**.
3.  **Theme Details**:
    *   Theme Name: `Lumina Oficial`.
4.  **Branding**:
    *   Haz clic en el recuadro de **Brand Color** y escribe: `#005A9C` (Azul Lumina).
    *   Haz clic en **Brand Image** y sube el logo de Lumina (o una imagen cualquiera de prueba).
5.  Haz clic en **Save**.
6.  Una vez guardado, haz clic en el botón **Activate** (arriba a la derecha) para aplicarlo.

### Paso 3: Crear la Lightning App (HU-006)
1.  Busca **App Manager** en Setup.
2.  Haz clic en el botón **New Lightning App** (arriba a la derecha).
3.  **App Details**:
    *   App Name: `Gestión Académica Lumina` (Lumina Academic Management).
    *   Developer Name: `Gestion_Academica` (Automático, sin tildes).
    *   Haz clic en **Next**.
4.  **App Options**: Deja todo por defecto (Standard Navigation). Haz clic en **Next**.
5.  **Utility Items**: Haz clic en **Next** (Saltar).
6.  **Navigation Items** (El menú de la app):
    *   En la lista izquierda ("Available Items"), busca `Alumnos`.
    *   Selecciónalo y haz clic en la flecha derecha (▶) para moverlo a "Selected Items".
    *   Repite para: `Carreras`, `Materias`, `Inscripciones`.
    *   Haz clic en **Next**.
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

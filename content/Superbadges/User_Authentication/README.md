# User Authentication Settings Superbadge 🔐

**Estado**: ✅ COMPLETADO


Este directorio contiene todos los recursos necesarios para completar el Superbadge de **User Authentication Settings**. Este reto valida tu capacidad para proteger el acceso a una organización de Salesforce mediante políticas de contraseñas, restricciones de red y seguridad de aplicaciones conectadas.

## � Contenido del Directorio

*   **[ENUNCIADO_ORIGINAL.md](ENUNCIADO_ORIGINAL.md)**: El escenario de negocio de "Cirrus Cash Flow" y los requisitos detallados del reto.
*   **[GUIA_SB_SOLUCION.md](GUIA_SB_SOLUCION.md)**: Guía paso a paso para configurar las políticas de seguridad y resolver los desafíos.

---

## 🎯 Objetivos de Aprendizaje

Al completar este Superbadge, demostrarás competencia en:
1.  **Políticas de Contraseña**: Configurar vencimientos, complejidad y bloqueos tanto a nivel de Organización como de Perfil.
2.  **Restricciones de Red**: Implementar rangos de IP de confianza (Network Access) y rangos de IP estrictos por perfil.
3.  **Gestión de Sesiones**: Configurar tiempos de espera y cierres de sesión forzados.
4.  **Seguridad de Apps**: Controlar qué Aplicaciones Conectadas (Connected Apps) pueden acceder a los datos.
5.  **Autenticación**: Habilitar y requerir autenticación multifactor (MFA) para accesos sensibles.

## 📝 Prerrequisitos (¡Muy Importante!)

Para este Superbadge **NO** puedes usar una Playground estándar. Debes registrarte en una **Developer Edition especial** con datos pre-cargados.

*   🔗 **Link de Registro**: [Sign up for a special Developer Edition org with configuration data](https://trailhead.salesforce.com/promo/orgs/superbadge-user-authentication-settings)
*   **Nota**: Conecta esta org a tu Trailhead ANTES de empezar a configurar, especialmente antes de tocar las Connected Apps.

## 💡 Consejos Clave
*   **Orden de Factores**: Configura primero las políticas generales (OWD, Password Policies) antes de ir a los perfiles específicos.
*   **IPs y Bloqueos**: Ten cuidado al configurar los rangos de IP en tu propio perfil de Administrador; podrías bloquearte a ti mismo. Asegúrate de tener acceso.
*   **Usuarios Ficticios**: El reto usa usuarios como "Sonia" o "Adil". Asegúrate de probar las configuraciones logueándote como ellos (Incognito Mode) para verificar que las restricciones funcionen.

---
*¡Mantén segura la fortaleza, Admin!* 🛡️

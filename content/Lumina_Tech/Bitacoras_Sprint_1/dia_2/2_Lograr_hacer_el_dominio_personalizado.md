# 🌐 Lograr hacer el dominio personalizado

**Rol Responsable**: 🛡️ **Salesforce Admin**
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../../Gestor_de_Versiones/03-Salesforce_Admin.md) (Configuración Básica)

## Guía de Configuración: My Domain

### ¿Por qué personalizar el dominio?
Transformar `na123.salesforce.com` en `luminatech.my.salesforce.com`.
1.  **Seguridad**: Requisito obligatorio para componentes Lightning personalizados.
2.  **Identidad**: Refuerza la marca ante los usuarios.
3.  **SSO**: Facilita futuras integraciones de Single Sign-On.

### Pasos de Implementación (Click-Path)
1.  Ir a **Setup** > **My Domain**.
2.  En "My Domain Name", ingresar `lumina-university-[TU_APELLIDO]`.
    *   *Nota*: Debe ser único mundialmente.
3.  Click en **Check Availability**.
4.  Click en **Register Domain**.
5.  ❌ **ESPERAR**: Puede tardar de 2 a 20 minutos. El admin recibirá un email.
6.  Una vez activo, click en **Deploy to Users**.

> ⚠️ **Advertencia**: Una vez desplegado, cambiarlo es disruptivo. Verificar bien el nombre antes de aceptar.

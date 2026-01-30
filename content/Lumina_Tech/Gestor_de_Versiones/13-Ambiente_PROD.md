# 13-Ambiente_PROD.md - Bitácora de Producción
**Org ID**: `00D_PROD_LUMINA`
**Dominio**: `lumina.my.salesforce.com`
**Estado**: 🔒 Locked (Solo Deployments)

---

## 🛑 Política de Acceso (Governance)

*   **Regla #1**: Nadie configura "a mano" en Producción.
*   **Regla #2**: Todo cambio debe venir de un Change Set aprobado en QA.
*   **Excepción**: Reportes y Dashboards pueden crearse directamente en PROD por usuarios Power Users.

---

## 📦 Historial de Versiones (Changelog)

### v1.0.0 - "Genesis" (Sprint 1)
**Fecha**: 25/01/2026
**Release Manager**: WIGUSA

**Contenido**:
*   Core Académico Completo (Objetos, Campos, Tabs).
*   Seguridad Inicial (Perfiles Profesor y Admin).
*   Aplicación Lightning "Gestión Académica".

**Incidentes Post-Deploy**:
*   *Ninguno reportado en las primeras 24hs.*

---

## 📞 Soporte Post-Go-Live

Si un usuario reporta un error crítico:
1.  Crear ticket en Jira/Trello (Etiqueta 🔴 Producción).
2.  Reproducir el error en SANDBOX FULL (UAT).
3.  **Nunca** depurar con datos reales de alumnos (PII).

# 13-Ambiente_PROD.md - Entorno de Producción

## 📋 Información del Ambiente

**Proyecto**: Lumina Tech
**Tipo de Ambiente**: Production Org (Developer Edition actuando como PROD)
**Propósito**: Uso final por la Rectora y Profesores reales.
**Equipo**: Grupo de Trabajo (Estudiantes)
**Responsables**: Todo el equipo (Custodia compartida)
**Estado**: 🔴 Protegido (Solo lectura hasta Deploy)

---

## 🔗 Acceso al Ambiente

### URL de Login
**URL**: [https://login.salesforce.com](https://login.salesforce.com)
**My Domain**: `https://lumina-tech.my.salesforce.com` (Definitivo)

---

## 👥 Administradores de Producción (Grupo de Trabajo)

⚠ **Política de Acceso**: Solo 2 personas tienen la contraseña de Admin en PROD para evitar errores accidentales.

### Gatekeeper 1 (Release Manager)
**Responsable**: Estudiante 1
**Usuario**: `admin@lumina.edu`
**Función**: Aprobar y ejecutar deployments finales.

### Gatekeeper 2 (Backup)
**Responsable**: Estudiante 2
**Usuario**: `backup@lumina.edu`
**Función**: Acceso de emergencia.

---

## ⚠️ Protocolo de Seguridad (Reglas de Oro)

1.  **NUNCA probar en PROD**: Las pruebas se hacen en QA.
2.  **Backup Obligatorio**: Antes de cualquier deploy, exportar datos (Data Export).
3.  **Ventana de Mantenimiento**: Los deploys se hacen Viernes 18:00hs (simulado).

---

## 📦 Registro de Deployments (Release History)

| Versión | Fecha | Contenido (Log) | Resultado |
|---|---|---|---|
| **v1.0 (MVP)** | 30/01 | Objetos Core, Seguridad OWD, App Lightning. | ⏳ Pendiente |
| **v1.1** | 15/02 | Reportes Avanzados y Dashboard Rectoría. | ⚪ Planificado |

---

## 🔄 Plan de Rollback

Si el deployment v1.0 rompe el sistema:
1.  **Desactivar**: Flows y Reglas de Validación problemáticas.
2.  **Restaurar**: Borrar campos custom nuevos si corrompen datos.
3.  **Comunicar**: Enviar email a soporte@lumina.edu avisando del incidente.

# 14-DevOPS.md - Estrategia de Despliegue y CI/CD
**Proyecto**: Universidad Lumina Tech
**Rol**: DevOps Engineer / Release Manager
**Ciclo**: Sprint 1

---

## 🔁 Estrategia de Ramificación (Environment Strategy)

Para este proyecto, utilizamos un modelo de **Salesforce Org-Based Development**.

| Ambiente | Tipo | Propósito | Refresh |
|---|---|---|---|
| **DEV** | Developer Edition | Construcción día a día. Configuración sucia. | N/A (Org persistente) |
| **QA** | Sandbox (Partial Copy) | Pruebas de integración y QA formal. | Mensual (Post-Release) |
| **UAT** | Sandbox (Full Copy) | Pruebas de aceptación de usuario final (Rectora). | Trimestral |
| **PROD** | Production | Ambiente vivo. Datos reales. | N/A |

---

## 📦 Protocolo de Despliegue (Change Sets)

### Naming Convention
Los Change Sets deben seguir el formato: `[SPRINT]_[TICKET]_[DESCRIPCION]`.
*   *Ejemplo*: `S1_HU001_OWD_Alumno`

### Checklist Pre-Deploy
1.  **Dependencias**: ¿Has incluido los campos nuevos antes de los Page Layouts?
2.  **Perfiles**: Recuerda que los Change Sets **NO** llevan la asignación de usuarios estándar, solo los permisos del perfil custom.
3.  **Tests**: ¿Tienes al menos 75% de cobertura en Apex? (N/A para Sprint 1 config-only).

### Pasos de Despliegue (Outbound -> Inbound)
1.  **En DEV**: Ir a Setup -> Outbound Change Sets -> New.
2.  Agregar componentes (Custom Objects, Fields, Validation Rules).
3.  **Upload** a la organización target (QA).
4.  **En QA**: Ir a Setup -> Inbound Change Sets.
5.  **Validate**: Ejecutar "Default Tests".
6.  **Deploy**: Si verde, desplegar.

---

## 🛡️ Plan de Rollback

Si el despliegue rompe la Org destino:

### Escenario A: Configuración (Metadata)
*   **Acción**: Desactivar manualmente los componentes fallidos (e.g., desactivar la Validation Rule errónea).
*   **No borrar**: Borrar campos en PROD causa pérdida de datos. Renombrar a `OBSOLETE_NombreCampo` hasta confirmar backup.

### Escenario B: Datos (Data Loader)
*   **Prevención**: Exportar CSV de la tabla afectada ANTES del deploy.
*   **Restauración**: Usar Data Loader en modo "Update" con el CSV de backup.

---

## 📅 Calendario de Release (Sprint 1)

| Hito | Día | Hora | Responsable |
|---|---|---|---|
| **Freeze** | Jueves | 18:00 | Admin |
| **Validation** | Viernes | 09:00 | DevOps |
| **Deploy QA** | Viernes | 14:00 | DevOps |
| **Deploy PROD** | Viernes | 17:00 | Release Manager |

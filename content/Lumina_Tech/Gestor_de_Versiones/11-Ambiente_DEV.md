# 11-Ambiente_DEV.md - Entorno de Desarrollo

## 📋 Información del Ambiente

**Proyecto**: Lumina Tech
**Tipo de Ambiente**: Developer Edition (Simulando Sandbox)
**Propósito**: Desarrollo y configuración inicial del MVP
**Equipo**: Grupo de Trabajo (Estudiantes)
**Admins Principales**: Estudiante 1 y Estudiante 2
**Estado**: 🟢 Activo

---

## 🔗 Acceso al Ambiente

### URL de Login
**URL**: [https://login.salesforce.com](https://login.salesforce.com) (Para Developer Edition)
**My Domain**: `https://lumina-tech-dev-ed.my.salesforce.com` (Simulado)

---

## 👥 Credenciales de Administradores (Grupo de Trabajo)

Todos los administradores **son miembros del equipo**. No compartimos credenciales con externos.

### Admin 1: Arquitecto de Datos
**Responsable**: Estudiante 1
**Username**: `admin1@lumina.dev`
**Función**: Responsable de Objetos (`Carrera`, `Materia`, `Alumno`) y Relaciones.

### Admin 2: Responsable de Seguridad
**Responsable**: Estudiante 2
**Username**: `admin2@lumina.dev`
**Función**: Configuración de Perfiles, Roles y Sharing Settings (OWD).

---

## 📝 Registro de Cambios (Audit Log)

| Fecha | Cambio realizado | Responsable | Estado Migración |
|-------|------------------|-------------|------------------|
| 19/01 | Creación de Objetos Core (`Carrera`, `Materia`) | Estudiante 1 | ⏳ Pendiente |
| 20/01 | Creación Junction Object `Inscripción__c` | Estudiante 1 | ⏳ Pendiente |
| 21/01 | Clonación de Perfiles (`Lumina_Profesor`) | Estudiante 2 | ⏳ Pendiente |
| 21/01 | Configuración de OWD Private en `Alumno__c` | Estudiante 2 | ⏳ Pendiente |

---

## 🔧 Checklist de Configuración
- [x] My Domain configurado (`lumina-tech...`)
- [x] Usuarios Admin activos
- [x] Moneda configurada (USD/Local)
- [ ] Idioma Español activado
- [ ] Timezone ajustado a local

## 🚫 Reglas de Oro en DEV
1.  **NO usar datos reales**: Usar nombres ficticios ("Juan Pérez").
2.  **Documentar todo**: Si creas un campo, añádelo al `03-Salesforce_Admin.md`.
3.  **Comunicación**: Avisar al compañero si vas a modificar un objeto compartido.

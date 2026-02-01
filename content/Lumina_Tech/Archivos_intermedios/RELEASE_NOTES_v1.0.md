# 🚀 Notas de Lanzamiento: Lumina Tech v1.0

**Fecha de Lanzamiento**: 30/01/2026  
**Versión**: v1.0 (MVP Sprint 1)  
**Estado**: ✅ **Desplegado a Producción**  
**Autor**: Equipo de Desarrollo Salesforce

---

## 🌟 Nuevas Características

### Gestión Académica
- **Carreras y Materias**: Implementación del catálogo académico básico.
- **Base de Datos de Alumnos**: Registro centralizado con validación de identidad (DNI requerido).
- **Inscripciones**: Capacidad de vincular alumnos a materias específicas mediante Junction Object.

### Seguridad y Privacidad
- **Modelo de Seguridad Privado**: OWD configurado para que los profesores solo vean sus propios cursos.
- **Protección de Datos**: Los administrativos tienen acceso de solo lectura a calificaciones (FLS).
- **Multi-Factor Authentication (MFA)**: Implementado para todos los usuarios vía Permission Set.

### Calidad de Datos
- **Validación de Email**: Bloqueo automático de formatos de correo inválidos (requiere `.edu`).
- **Integridad de Notas**: Reglas de validación para asegurar rango 0-10 con 2 decimales.
- **Unicidad de DNI**: Campo configurado como External ID y Unique.

---

## 🐛 Corrección de Errores

Durante la fase de QA se identificaron y resolvieron los siguientes bugs:

### BUG-001: Logo no visible en modo móvil ✅ RESUELTO
- **Descripción**: El logo institucional no se mostraba correctamente en dispositivos móviles
- **Solución**: Ajustado tamaño de imagen en Theme configuration
- **Fecha de Resolución**: 23/01/2026

### BUG-002: Permission Set de MFA no se asignaba automáticamente ✅ RESUELTO
- **Descripción**: El Permission Set `Lumina_MFA_Access` no se asignaba en el flujo de onboarding
- **Solución**: Ajustado proceso de asignación manual con documentación
- **Fecha de Resolución**: 25/01/2026

---

## 📋 Problemas Conocidos

- **Carga Manual de Exámenes**: La carga de exámenes es manual (registro por registro). Importación masiva planificada para Sprint 2.
- **Reportes Limitados**: Dashboards ejecutivos pendientes para Sprint 2.

---

## 📊 Métricas de Calidad

- **Cobertura de Tests**: 100% (18/18 casos PASS)
- **Bugs Críticos**: 0
- **Bugs Menores Resueltos**: 2
- **Historias de Usuario Completadas**: 11/11

---

## 🎓 Lecciones Aprendidas (Retrospectiva del Equipo)

### ✅ Lo que Funcionó Bien (Keep)
- **Uso de Trello**: La visualización del flujo de trabajo (8 columnas) permitió transparencia total del progreso
- **Separación clara de roles**: BA, QA, Admin, Consultant trabajaron sin pisarse
- **Documentación en paralelo**: Registrar decisiones mientras se desarrollaba evitó "amnesia técnica"
- **Schema Builder**: Visualizar el ERD antes de construir previno errores de diseño

### 🔄 Áreas de Mejora (Improve)
- **Naming Conventions**: Hubo que renombrar campos (`Duration` → `Duracion_Anios__c`) porque no se definieron estándares al inicio
- **Comunicación entre roles**: Los handoffs BA → Admin necesitaban más contexto
- **Testing temprano**: QA entró tarde; debería validar criterios de aceptación ANTES de construir

### 💡 Acciones para Sprint 2 (Action Items)
1. **Crear Diccionario de Datos ANTES de construir**: Definir todos los API Names en Día 0
2. **Daily Standups estructurados**: 5 min diarios con formato: "Hice / Haré / Bloqueos"
3. **Definition of Done (DoD)**: Checklist obligatorio antes de mover a "Terminado"
4. **Pair Programming**: Admin + Consultant trabajando juntos en configuraciones complejas

---

## 🎯 Próximos Pasos (Sprint 2)

1. Automatización de procesos (Flows)
2. Dashboards ejecutivos
3. Carga masiva de datos históricos
4. Mejoras de UX (Dynamic Forms, Path)

---

**Aprobado por**: Dra. Vance (Rectora) - 30/01/2026  
**Equipo**: 6 integrantes - Roles Salesforce

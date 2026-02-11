# 🚀 Notas de Lanzamiento: Lumina Tech v1.0

**Fecha de Lanzamiento**: 06/02/2026
**Versión**: v1.0 (MVP Sprint 1 - Argentina)
**Estado**: ✅ **Desplegado a Producción**
**Autor**: Equipo de Desarrollo Salesforce (Localización)

---

## 🌟 Nuevas Características

### Gestión Metodológica y Documentación
- **Documentación Gold Standard**: Guías de implementación detalladas con controles de calidad por rol.
- **Backlog Gherkin**: Historias de Usuario con Criterios de Aceptación verificables y narrativa clara.
- **Roles Definidos**: Guías específicas para Admins, QA y DevOps.

### Gestión Académica (Core)
- **Careers & Subjects**: Implementación del catálogo académico básico (`Careers` y `Subjects`).
- **Student Database**: Registro centralizado con `First Name` y `Last Name` separados, y validación de `National ID` (8 dígitos).
- **Enrollments**: Capacidad de vincular `Students` a `Subjects`.
- **Exams**: Carga de notas parciales y finales con escala 0-10 (`Score`).

### Seguridad y Privacidad
- **Modelo "Zero Trust"**: OWD Privado. Los profesores solo ven sus propias `Subjects`.
- **Perfiles Especializados**:
    - `Lumina Professor`: Carga notas, ve solo sus cursos.
    - `Lumina Registrar`: Inscribe alumnos (`Enrollments`), pero no puede modificar notas históricas (Read Only).
- **MFA (Multi-Factor Authentication)**: Implementado para usuarios clave.

### Calidad de Datos
- **Validación de Email**: Formato de correo validado (acepta Gmail, Hotmail, etc., pero con estructura correcta).
- **Integridad de Notas**: Validation Rules para asegurar rango 0-10 (`Score`).
- **Unicidad de National ID**: Campo `National ID` configurado como Unique para evitar duplicados.

### Experiencia de Usuario (UX)
- **App "Lumina Academic Management"**: Branding institucional y navegación personalizada.
- **Terminología**: Interfaz mantiene los términos estándar en inglés (`Students`, `Careers`) para alineación con el Backend.

---

## 🐛 Corrección de Errores

Durante la fase de QA se identificaron y resolvieron los siguientes bugs:

### BUG-001: Validación de Email Restrictiva ✅ RESUELTO
- **Descripción**: El sistema rechazaba emails personales (Gmail), exigiendo `@lumina.edu`.
- **Solución**: Se relajó la regla a `Valid_Email_Format` (Regex genérico).
- **Fecha de Resolución**: 06/02/2026

### BUG-002: Formato de Nombres ⚠️ AJUSTADO
- **Descripción**: Confusión sobre dónde cargar segundo nombre o apellido materno.
- **Solución**: Se aclaró en las guías el uso de `First Name` para nombres completos y `Last Name` para ambos apellidos.
- **Fecha de Resolución**: 06/02/2026

---

## 📋 Problemas Conocidos (Known Issues)

- **Carga Manual de Exams**: Actualmente se hace registro por registro. Importación masiva (Bulk Import) planificada para Sprint 2.
- **Reportes**: Aún no hay dashboards gráficos de rendimiento académico.

---

## 📊 Métricas del Sprint 1

- **Guías de Implementación**: 10 Documentos Localizados (100%).
- **Historias de Usuario**: 12/12 Completadas.
- **Índice de Adopción**: User Guide creada con Tips de Productividad.

---

## 🎓 Lecciones Aprendidas (Retrospectiva del Equipo)

### ✅ Lo que Funcionó Bien (Keep)
- **Transparencia en Trello**: El flujo de 11 columnas permitió visibilidad total.
- **Separación de Roles**: BA, QA, Admin y Consultant trabajaron sin bloqueos.
- **Schema Builder**: Validar el ERD visualmente antes de construir previno errores de diseño.

### 🔄 Áreas de Mejora (Improve)
- **Naming Convention**: Hubo que refactorizar `First Name` y `Last Name` tardíamente por falta de definición inicial sobre el manejo de apellidos compuestos.
- **Testing Temprano**: QA debería validar criterios de aceptación antes de la construcción.

### 💡 Acciones para el Futuro
1. **Data Dictionary**: Definir API Names antes del Día 0.
2. **Definition of Done (DoD)**: Checklist obligatorio antes de cerrar la tarea.

---

## 🎯 Próximos Pasos (Sprint 2)

1.  Automatización de procesos (Flows de Email, Alertas).
2.  Dashboards Ejecutivos para Rectoría.
3.  Migración masiva de notas históricas.
4.  Dynamic Forms según el estado del `Student`.

---

**Aprobado por**: Product Owner (Usuario)
**Equipo**: Visionary Admins Grupo 03

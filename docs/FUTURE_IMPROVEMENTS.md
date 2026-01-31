# 🚀 Manual de Mejoras y Evolución del Producto

**Rol**: Product Manager (PM)  
**Proyecto**: Salesforce Admin Learning Platform  
**Fecha**: 31 Enero 2026

---

## 🎯 Visión Estratégica
Este documento describe el "Roadmap de Excelencia" para transformar el MVP actual en una plataforma de educación de clase mundial. Las mejoras se priorizan por impacto en el usuario y viabilidad técnica.

---

## 1. Panel de Administración (Superuser) 🛡️

**Prioridad**: Alta  
**Justificación**: Actualmente, la gestión de usuarios y contenidos requiere intervención manual en base de datos. Un panel visual democratiza la administración.

### Especificaciones Funcionales
*   **Gestión de Usuarios**: CRUD completo (Crear, Editar, Desactivar) para estudiantes y profesores.
*   **Asignación de Roles**: Interfaz simple para promover usuarios de "Student" a "Consultant" o "Admin".
*   **Moderación de Progreso**: Capacidad de visualizar y corregir el avance de un estudiante si reporta errores.

### Implementación Técnica Recomendada
*   **Opción A (Rápida - "Low Code")**: Integrar [`sqladmin`](https://github.com/aminalaee/sqladmin). Es una librería para FastAPI que genera un panel admin automático basado en tus modelos SQLAlchemy.
*   **Opción B (Custom - "High Control")**: Crear una ruta `/admin` protegida para usuarios con `role='superuser'`, usando componentes de Tailwind existentes.

---

## 2. Motor de Búsqueda Inteligente (Full-Text Search) 🔍

**Prioridad**: Media-Alta  
**Justificación**: A medida que crece la documentación (Markdown), encontrar un concepto específico ("Validation Rules", "Flow Builder") se vuelve difícil navegando carpeta por carpeta.

### Solución
*   **Frontend**: Barra de búsqueda global en el header (Cmd+K).
*   **Backend**: Indexar los títulos y contenidos de los archivos Markdown al inicio (`startup_event`).
*   **UX**: Resultados instantáneos con resaltado de coincidencias.

---

## 3. Gamificación y Engagement 🏆

**Prioridad**: Media  
**Justificación**: Aumentar la retención y motivación del estudiante.

### Features
*   **Medallas (Badges)**: "Rookie Admin", "Flow Master", "Security Guard". Se otorgan al completar Sprints específicos.
*   **Leaderboard**: Tabla de clasificación semanal basada en tareas completadas de Lumina Tech.
*   **Streaks**: Contador de días consecutivos estudiando.

---

## 4. Funcionalidades Sociales y Colaborativas 💬

**Prioridad**: Baja (Futuro)  
**Justificación**: Transformar el estudio solitario en aprendizaje comunitario.

### Features
*   **Comentarios en Lecciones**: Permitir dudas al pie de cada documento Markdown.
*   **Reacciones**: Emojis (👍, 💡, ❤️) en los párrafos para feedback rápido.
*   **User Profiles**: Páginas públicas con el portafolio de logros del estudiante.

---

## 5. Aplicación Progresiva (PWA) 📱

**Prioridad**: Media (Mejora Mobile)  
**Justificación**: Permitir estudio offline o en transporte público.

### Implementación
*   **Service Workers**: Cachear el contenido estático (CSS, JS) y los Markdowns visitados recientemente.
*   **Manifest.json**: Permitir "Instalar" la web como app nativa en Android/iOS.

---

**Nota del PM**: Recomiendo comenzar con el **Panel de Administración** (Opción A: `sqladmin`) en el próximo Sprint Técnico, ya que libera al equipo de desarrollo de tareas operativas manuales.

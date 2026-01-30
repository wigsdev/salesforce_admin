# 08-SPRINT_2.md - Planificación Futura (Reportes)
**Estado**: 🔜 Backlog Priorizado
**Tema**: "Inteligencia de Negocio y Migración"

---

## 🎯 Objetivos del Sprint 2
1.  **Migración Masiva**: Cargar los 500 alumnos actuales desde Excel (CSV).
2.  **Reportes Operativos**: Listados de asistencia y actas de examen.
3.  **Dashboards**: Visualización para la Rectora (KPIs).

## 📝 Historias de Usuario Candidatas

### HU-020: Importación de Legajos
*   **Como**: Admin.
*   **Quiero**: Usar Data Loader para importar alumnos.
*   **Para**: No cargarlos manualmente uno por uno.

### HU-021: Reporte de Deserción
*   **Como**: Director Académico.
*   **Quiero**: Un reporte de alumnos con "Estado = Libre" en más de 2 materias.
*   **Para**: Contactarlos y ofrecer tutorías.

### HU-022: Dashboard de Rectoría
*   **Componentes**:
    *   Gráfico de Barras: Inscritos por Carrera.
    *   Velocímetro: Promedio general de notas de la universidad.

---

## 🛠️ Tareas Técnicas
*   [ ] Mapeo de campos Excel -> Salesforce.
*   [ ] Limpieza de datos (Deduplicación de DNIs).
*   [ ] Configuración de carpetas de Reportes (Públicos vs Privados).

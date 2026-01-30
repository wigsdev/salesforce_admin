# 12-Ambiente_QA.md - Bitácora de Calidad
**Org ID**: N/A (Simulado en Dev Sandbox con sufijo .qa)
**Login**: `tester@lumina.qa.com`
**Estado**: 🟡 En Pruebas

---

## 🧪 Datos de Prueba (Seed Data)

Para validar el Sprint 1, se ha cargado el siguiente set de datos ("Data Factory"):

### Carreras (Padres)
1.  **Ingeniería en Sistemas** (Duración: 5 años).
2.  **Administración de Empresas** (Duración: 4 años).

### Materias (Hijos)
*   `MAT-001` Programación I (Sistemas).
*   `MAT-002` Contabilidad Básica (Admin).

### Alumnos (Actores)
*   **Juan Perez (Legajo 100)**: Caso feliz.
*   **Maria Error (Legajo 999)**: Usada para pruebas de validación (notas negativas).

---

## 🔍 Resultados de Smoke Tests

| Fecha | Versión | Pass Rate | Bloqueantes |
|---|---|---|---|
| 20/01 | v0.1 (Alpha) | 40% | Sí (No se podía crear Inscripción). |
| 22/01 | v0.5 (Beta) | 85% | No. |
| 24/01 | v1.0 (RC) | 100% | Ready for Prod. |

---

## 🐛 Bugs Recurrentes (Known Issues)
*   A veces el Lightning App Builder tarda en refrescar el cache y no muestra los campos nuevos. Solución: Hard Refresh (Ctrl+F5).

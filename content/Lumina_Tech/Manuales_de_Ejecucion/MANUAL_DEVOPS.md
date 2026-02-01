# ♾️ Manual de Ejecución: DevOps Specialist

**Tu Misión**: Eres el Mecánico. Preparas el terreno (Datos y Ambientes) para que los pilotos (Admin/QA) puedan volar.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Entrada** | QA necesita probar, pero el sistema está vacío (sin alumnos, sin materias). |
| 💿 **DATA** | **Tu Turno** | Cargas datos masivos (Seed Data) para simular un entorno real. |
| ♻️ **REFRESH** | **Mantenimiento** | Sincronizas los cambios entre Sandboxes si hay desvaríos. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN

### Día 1: Preparación del Terreno
*   🛑 **PRE-REQ**: Admin creó los objetos `Carrera` y `Materia`.

1.  **Carga de Datos Maestros (Seed)**
    *   💿 **DATA**:
        *   Usa Data Import Wizard o Inspector para cargar 5 Carreras (Ingeniería, Derecho, etc.).
        *   Carga 20 Materias vinculadas.
    *   *Por qué*: Para que el QA no tenga que crear datos manuales uno por uno.
    *   📘 **Guía**: [09-Rol_DevOps_Specialist.md](../../Tutoriales_por_Rol/09-Rol_DevOps_Specialist.md)

*   👋 **HANDOFF**: Avisa al QA: "Datos de prueba listos. Hay 20 materias para jugar".

### Día 4: Stress Testing (Soporte)
*   🛑 **PRE-REQ**: QA quiere probar seguridad masiva.

1.  **Creación de Usuarios Fake**
    *   💿 **DATA**:
        *   Crea 3 usuarios "Student" ficticios.
        *   Crea 2 usuarios "Professor" ficticios.
    *   *Objetivo*: Que QA pruebe los permisos de login.

*   👋 **HANDOFF**: "Usuarios de prueba creados. Credenciales en el documento compartido".

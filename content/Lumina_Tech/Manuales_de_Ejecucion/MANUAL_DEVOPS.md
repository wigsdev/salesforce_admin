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

### Día 0: Preparación de Ambientes
*   🛑 **PRE-REQ**: Acceso a la Org y Sandboxes asignados.

1.  **Verificación de Ambientes**
    *   💿 **DATA**: Confirma que tienes acceso a DEV, QA y PROD.
    *   *Acción*: Documenta las credenciales y URLs de cada ambiente.

*   👋 **HANDOFF**: "Ambientes verificados y listos para el equipo".

---

### Día 1: Preparación del Terreno
*   🛑 **PRE-REQ**: Admin creó los objetos `Carrera` y `Materia`.

1.  **Carga de Datos Maestros (Seed)**
    *   💿 **DATA**:
        *   Usa Data Import Wizard o Inspector para cargar 5 Carreras (Ingeniería, Derecho, etc.).
        *   Carga 20 Materias vinculadas.
    *   *Por qué*: Para que el QA no tenga que crear datos manuales uno por uno.
    *   📘 **Guía**: [09-Rol_DevOps_Specialist.md](../Tutoriales_por_Rol/09-Rol_DevOps_Specialist.md)

*   👋 **HANDOFF**: Avisa al QA: "Datos de prueba listos. Hay 20 materias para jugar".

---

## 📚 Recursos Relacionados

- 📘 **Tutorial de Rol**: [09-Rol_DevOps_Specialist.md](../Tutoriales_por_Rol/09-Rol_DevOps_Specialist.md)
- 📘 **Glosario**: [GLOSARIO.md](../GLOSARIO.md)

---

### Día 2: Soporte a Branding
*   🛑 **PRE-REQ**: Admin está configurando My Domain y Themes.

1.  **Monitoreo Pasivo**
    *   ♻️ **REFRESH**: El DevOps no tiene tareas activas este día.
    *   *Rol*: Disponible para resolver problemas técnicos si el Admin tiene bloqueos.

*   👋 **HANDOFF**: "Día de construcción. DevOps en standby".

---

### Día 3: Soporte a Validaciones
*   🛑 **PRE-REQ**: Admin está creando Validation Rules.

1.  **Backup Preventivo**
    *   💿 **DATA**: Exporta los datos actuales de DEV como respaldo antes de las validaciones.
    *   *Por qué*: Las validaciones pueden bloquear datos existentes.

*   👋 **HANDOFF**: "Backup completado. Admin puede proceder con validaciones".

---

### Día 4: Stress Testing (Soporte)
*   🛑 **PRE-REQ**: QA quiere probar seguridad masiva.

1.  **Creación de Usuarios Fake**
    *   💿 **DATA**:
        *   Crea 3 usuarios "Student" ficticios.
        *   Crea 2 usuarios "Professor" ficticios.
    *   *Objetivo*: Que QA pruebe los permisos de login.

*   👋 **HANDOFF**: "Usuarios de prueba creados. Credenciales en el documento compartido".


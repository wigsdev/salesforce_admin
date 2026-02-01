# 🚀 Manual de Ejecución: Release Manager

**Tu Misión**: Despliegue. Eres el dueño de las columnas **7. SF Producción** y **8. Terminado**.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **7. SF Producción** | El TL aprobó técnicamente. La tarjeta espera deploy. |
| 📦 **DEPLOY** | **(Proceso)** | Ejecutas Change Sets / Metadata API hacia Prod. |
| 🏁 **DONE** | **8. Terminado** | Está vivo en Producción. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN

> **Nota**: El Release Manager tiene dos responsabilidades principales:
> 1. **Documentación Continua**: Registrar cambios en el Gestor de Versiones (días 1-4)
> 2. **Despliegue a Producción**: Ejecutar releases al final del Sprint (día 4)

### Día 1: Registro de Modelo de Datos
*   🛑 **PRE-REQ**: Admin ha creado objetos y campos.

1.  **Registrar en Gestor**
    *   📦 **ACCIÓN**: Documenta en el Gestor los objetos creados (Carrera, Materia, Alumno, Inscripción).
    *   📘 **Guía**: [4_Registrar_en_el_Doc_gestor_de_versiones.md](../Bitacoras_Sprint_1/dia_1/4_Registrar_en_el_Doc_gestor_de_versiones.md)

*   👋 **HANDOFF**: "Baseline del modelo de datos registrado".

---

### Día 2: Registro de Branding
*   🛑 **PRE-REQ**: Admin ha configurado My Domain, Logo y App.

1.  **Registrar en Gestor**
    *   📦 **ACCIÓN**: Documenta la configuración de branding (URL del dominio, colores, nombre de la App).
    *   📘 **Guía**: [4_Registrar_en_el_Doc_gestor_de_versiones.md](../Bitacoras_Sprint_1/dia_2/4_Registrar_en_el_Doc_gestor_de_versiones.md)

*   👋 **HANDOFF**: "Configuración de branding registrada".

---

### Día 3: Registro de Validaciones
*   🛑 **PRE-REQ**: Admin ha creado Validation Rules y campos fórmula.

1.  **Registrar en Gestor**
    *   📦 **ACCIÓN**: Documenta las reglas de validación y fórmulas implementadas.
    *   📘 **Guía**: [3_Registrar_en_el_Doc_gestor_de_versiones.md](../Bitacoras_Sprint_1/dia_3/3_Registrar_en_el_Doc_gestor_de_versiones.md)

*   👋 **HANDOFF**: "Reglas de negocio registradas".

---

### Día 4: Registro de Seguridad y Despliegue
*   🛑 **PRE-REQ**: Admin ha configurado Permission Sets y perfiles.

1.  **Registrar en Gestor**
    *   📦 **ACCIÓN**: Documenta la configuración de seguridad (Permission Sets, OWD, FLS).
    *   📘 **Guía**: [4_Registrar_Gestor_Versiones.md](../Bitacoras_Sprint_1/dia_4/4_Registrar_Gestor_Versiones.md)

2.  **Preparar Release**
    *   **Contexto**: Acumula tarjetas en **7. SF Producción** que ya fueron aprobadas por el TL.
    *   📘 **Guía**: [04-Rol_Release_Manager.md](../Tutoriales_por_Rol/04-Rol_Release_Manager.md)

3.  **Ejecutar Deploy**
    *   📦 **Acción**: Sube los cambios de Sandbox a Producción.

4.  **Cierre de Tarea**
    *   **Movimiento (7 -> 8)**: Mueve las tarjetas desplegadas a **8. Terminado**.
    *   🏁 **Celebración**: Avisa al equipo: "La funcionalidad X está en vivo".

*   👋 **HANDOFF**: "Sprint 1 completado y desplegado a producción".

---

## 📚 Recursos Relacionados

- 📘 **Tutorial de Rol**: [04-Rol_Release_Manager.md](../Tutoriales_por_Rol/04-Rol_Release_Manager.md)
- 📘 **Glosario**: [GLOSARIO.md](../GLOSARIO.md)
- 🔄 **Diagrama Trello**: [DIAGRAMA_FLUJO_TRELLO.md](../DIAGRAMA_FLUJO_TRELLO.md)

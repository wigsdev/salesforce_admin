# 🎓 Guía Metodológica para el Alumno
**Proyecto**: Universidad Lumina Tech
**Rol**: Consultor Salesforce (Business Analyst + Implementador)

Esta guía establece el **Estándar de Calidad** que esperamos de tu trabajo en este proyecto. No solo vas a "configurar", vas a **consultar**.

---

## 🕵️ Fase 1: La Indagación (Consultativa)

Tu primer trabajo NO es abrir Salesforce. Es **entender el dolor del cliente**.
Antes de escribir una sola línea en Trello, debes hacerte estas preguntas sobre el enunciado de la Dra. Vance:

### Sobre la Seguridad ("Nuestra Gente")
*   *"La Rectora dice que 'tienen un problema legal'. ¿Qué significa eso técnicamente?"*
    *   **Pregunta de Consultor**: ¿Basta con ocultar la pestaña o necesitamos bloquear el campo a nivel de base de datos (FLS)?
    *   **Respuesta Esperada**: FLS es obligatorio. La UI no es suficiente seguridad.

### Sobre la Estructura ("Materias y Alumnos")
*   *"Ella menciona que un alumno cursa muchas materias."*
    *   **Pregunta de Consultor**: ¿Qué pasa si un alumno recursa? ¿Necesitamos un registro histórico por cada intento?
    *   **Respuesta Esperada**: Sí, por eso usamos un objeto intermedio (Inscripción), no una relación directa.

---

## 📝 Fase 2: Traducción a Ágil (User Stories)

No copies y pegues el texto del cliente. Tradúcelo a valor.

### ❌ Mal Ejemplo (Técnico)
> "Crear objeto Alumno con campo DNI y validación de número."

### ✅ Buen Ejemplo (Funcional)
> **Título**: HU-007 - Garantía de Identidad Única
>
> **Como** Administrativo de Inscripciones,
> **Quiero** que el sistema impida guardar un alumno si no he cargado su DNI,
> **Para** asegurar que cumplimos con la normativa legal de matriculación y evitar duplicados.
>
> **Criterios de Aceptación**:
> - [ ] El campo DNI es obligatorio (Required) en el Page Layout y en el Object Manager.
> - [ ] Intentar guardar un registro sin DNI arroja el error: "Este campo es necesario".

---

## 🏗️ Fase 3: Gestión del Tablero (Workflow)

Para simular un entorno real de consultoría Salesforce, tu Trello debe tener este flujo riguroso:

| Columna | Significado | Quién actúa |
|---|---|---|
| **1. Backlog** | Todas las historias identificadas ([HISTORIAS_DE_USUARIO.md](HISTORIAS_DE_USUARIO.md)). | Product Owner |
| **2. Sprint Backlog** | Lo que te comprometes a hacer ESTA semana. | Equipo |
| **3. En Progreso** | Tarea activa (Máximo 2 por persona). | Admin / Dev |
| **4. SF Desarrollo** | Ya configurado en Sandbox, falta probar. | Admin / Dev |
| **5. SF QA** | El Tester verifica los Criterios de Aceptación. | QA Lead |
| **6. Aprobación TL** | Revisión de Código/Config por el Team Lead. | Arquitecto |
| **7. Terminado** | Listo para desplegar a Producción. | Todos |

---

## 💡 Consejos de Oro (Pro-Tips)

1.  **Piensa en Escalabilidad**: Hoy son 5 carreras, mañana pueden ser 50. No uses Picklists para "Nombre de Carrera", usa un Objeto.
2.  **Defensa en Profundidad**: Si la Rectora pide privacidad, usa OWD Privado + Sharing Rules. No confíes solo en ocultar menús.
3.  **Evidencia**: Una tarea no está terminada hasta que hay una captura de pantalla en Trello demostrando que funciona.

---
**Siguiente Paso**: Revisa la [00-Guia_Trello_Paso_a_Paso.md](00-Guia_Trello_Paso_a_Paso.md) para configurar tu tablero.

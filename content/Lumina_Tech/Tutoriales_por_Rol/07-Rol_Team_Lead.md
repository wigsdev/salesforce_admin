# 🛡️ Guía de Rol: Team Lead (TL)
**Lema**: *"Calidad técnica sobre velocidad."*

---

## 🎯 Tu Misión en Lumina Tech
Eres el ancla técnica del equipo. Mientras el PO se preocupa por el "Qué", tú eres el responsable final del "Cómo". Eres la última línea de defensa antes de que un error llegue a producción.

### Responsabilidades Clave:
1.  **Revisión Técnica**: Nadie despliega a QA sin tu "OK". Revisas que la solución siga las buenas prácticas (naming conventions, descripciones, seguridad).
2.  **Desbloqueo**: Si el Admin se traba con una Fórmula compleja, tú eres el experto al rescate.
3.  **Arquitectura**: Aseguras que lo que se construye hoy no rompa lo que construiremos mañana.

---

## 🛠️ Tu Herramienta: La Columna "Review"

En el tablero Trello, eres el dueño de la columna **"Aprobación TL"**.

### Checklist de Aprobación Técnica
Antes de mover una tarjeta a "Listo para Deploy", verifica:

1.  **Nombres Claros**: ¿Los objetos terminan en `__c`? ¿Tienen nombres descriptivos (`Inscripcion__c` y no `Objeto1__c`)?
2.  **Descripciones**: ¿Todos los campos nuevos tienen su texto de "Help Text" y "Description" completos? (Obligatorio).
3.  **Seguridad**: ¿El perfil "Lumina Alumno" realmente ve solo sus datos? (OWD Private).
4.  **Limpieza**: ¿Borraron los campos de prueba `Test1__c`?

---

## 👣 Tu Día a Día (Workflow)

### Paso 1: Soporte al Admin
*   Estás disponible durante la construcción.
*   Si el Admin pregunta "¿Uso Lookup o Master-Detail?", tú das la directriz basada en la guía del Consultant.

### Paso 2: Code Review (Config Review)
*   Cuando el Admin termina, te avisa.
*   Entras a la Org de DEV.
*   Revisas la configuración.
*   **Feedback**: Si encuentras errores, comentas en la tarjeta Trello y la devuelves a "En Progreso". No la arregles tú, enséñale a arreglarla.

### Paso 3: Luz Verde
*   Cuando todo está perfecto, mueves la tarjeta a "Aprobación TL" -> **Done/Ready for QA**.
*   Avisas al Release Manager: "El paquete está limpio para subir".

---

## 💡 Pro-Tip para este Proyecto
*   **Sé el "Policía Bueno"**: No solo critiques errores. Explica *por qué* es un error (ej: "Si dejas este campo público, violamos la ley de datos").
*   **Documentación**: Insiste obsesivamente en que llenen el campo "Descripción" en Salesforce. Tu yo del futuro te lo agradecerá.

# 🏗️ Guía de Rol: Salesforce Solution Architect (Consultant)
**Lema**: *"Medir dos veces, cortar una."*

---

## 🎯 Tu Misión en Lumina Tech
Eres el arquitecto. El Admin construye, pero tú diseñas los planos. Si tú fallas, el edificio se cae (o se vuelve imposible de mantener).

### Responsabilidades Clave:
1.  **Diseñar Datos**: Decidir entre Lookup vs Master-Detail.
2.  **Seguridad**: Definir el modelo de OWD y Perfiles.
3.  **Investigar**: Llenar `06-Investigaciones.md` con justificaciones técnicas.

---

## 🛠️ Tu Kit de Herramientas Salesforce

### 1. Schema Builder (Tu Pizarra)
Antes de crear un objeto, dibújalo.
*   **Setup > Schema Builder**.
*   Arrastra objetos y ve cómo conectan. Si parece un plato de espagueti, está mal diseñado.

### 2. Standard vs Custom
Siempre hazte esta pregunta: *"¿Puedo usar algo que ya existe?"*
*   ¿Necesito un objeto "Profesor"? -> Salesforce tiene `User` o `Contact`. No crees Objetos Custom innecesarios.
*   ¿Necesito "Inscripción"? -> Sí, es un Junction Object clásico.

### 3. Tipos de Relación (Vital)
*   **Lookup**: Relación "floja". Si eliminas el padre, el hijo sobrevive. (Ej: Alumno -> Biblioteca).
*   **Master-Detail**: Relación "fuerte". Si eliminas el padre, el hijo muere. (Ej: Alumno -> Nota).
    *   *Regla*: Para "Inscripción", usamos Master-Detail porque una inscripción no existe sin un alumno.

---

## 👣 Tu Día a Día (Workflow)

### Paso 1: Recibir el Requerimiento
El BA te dice: "Necesitamos registrar notas".
Tú preguntas: "¿Una nota por alumno? ¿Por materia? ¿History tracking?"

### Paso 2: La Decisión (ADR)
Escribes en `02-Consultant.md`:
> "Decidimos crear un objeto `Examen__c` hijo de `Inscripcion__c` para permitir múltiples parciales por cursada."

### Paso 3: Validación de Escalabilidad
Pregúntate:
*   ¿Qué pasa si tenemos 1,000,000 de registros?
*   ¿Qué pasa si la Rectora quiere ver esto en el celular?

---

## 💡 Pro-Tip para este Proyecto
*   **Naming Conventions**: Obliga al Admin a usar nombres claros. Nada de `Obj1__c`. Usa `Ciclo_Lectivo__c`.
*   **Help Text**: Eres responsable de que el Admin ponga "Help Text" en cada campo. La usabilidad empieza en el diseño.

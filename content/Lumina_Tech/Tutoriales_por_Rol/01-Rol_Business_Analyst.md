# 🕵️ Guía de Rol: Business Analyst (BA)
**Lema**: *"El puente entre el Negocio (Rectora) y la Tecnología (Salesforce)."*

---

## 🎯 Tu Misión en Lumina Tech
No eres un "tomador de pedidos". Eres un investigador. Tu trabajo es evitar que el equipo construya lo incorrecto.

### Responsabilidades Clave:
1.  **Entender**: Leer `SPRINT 1.md` y detectar qué duele realmente.
2.  **Traducir**: Convertir "quejas" en **Historias de Usuario**.
3.  **Gestionar**: Ser el dueño del Trello (`00-INTEGRACION_TRELLO.md`).

---

## 🛠️ Tu Kit de Herramientas Salesforce

Aunque no configuras, necesitas saber qué pedir.

### 1. Entiende el "Standard Box"
Antes de pedir algo nuevo, verifica si Salesforce ya lo tiene.
*   *Cliente dice*: "Quiero guardar empresas". -> *Tú piensas*: **Accounts**.
*   *Cliente dice*: "Quiero gente". -> *Tú piensas*: **Contacts**.
*   *Cliente dice*: "Quiero alumnos". -> *Tú piensas*: **¿Contact o Custom Object?** (Aquí hablas con el Arquitecto).

### 2. Criterios de Aceptación (Tu Arma Secreta)
Una Historia de Usuario sin Criterios de Aceptación es solo un deseo.
Usa este formato para que el Admin no te odie:

> **HU-003: Inscripción de Alumnos**
> ...
> **Criterios de Aceptación (Definition of Done):**
> 1. [ ] El sistema debe impedir inscribir si falta el DNI.
> 2. [ ] El sistema debe permitir elegir una Materia existente (Lookup).
> 3. [ ] Debe haber un campo de "Estado" por defecto en "Cursando".

---

## 👣 Tu Día a Día (Workflow)

### Paso 1: El Refinamiento (Grooming)
Antes de que el Admin toque una tecla:
1.  Abre `SPRINT 1.md`.
2.  Identifica un requerimiento (ej: "Privacidad de notas").
3.  Abre `01-Business_Analyst.md`.
4.  Escribe la traducción técnica ("Requerimos Field Level Security").

### Paso 2: Creación de Tickets
1.  Ve a Trello.
2.  Crea la tarjeta.
3.  **Vital**: Ponele Etiquetas (🔴 Seguridad, 🔵 Funcionalidad).
4.  Asigna los Story Points (¿Es un 2 o un 8?).

### Paso 3: Aceptación (UAT)
Cuando el QA dice que "Pasó", tú eres el juez final.
1.  Mira la evidencia.
2.  ¿Cumple lo que pidió la Rectora?
3.  Si Sí -> Aprueba.
4.  Si No -> Rechaza (aunque el código funcione, si no cumple la necesidad, no sirve).

---

## 💡 Pro-Tip para este Proyecto
*   **En la duda, pregunta**: Usa `05-Preguntas_y_Dudas.md`.
*   **No asumas**: Si la Rectora no dijo "Quiero foto del alumno", no pidas un campo de Foto. Mantenlo MVP.

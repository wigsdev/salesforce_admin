# 🏗️ Guía de Rol: Salesforce Administrator (Admin)
**Lema**: *"Tú lo sueñas, yo lo construyo."*

---

## 🎯 Tu Misión en Lumina Tech
Eres el constructor. El BA trae los planos, el Arquitecto verifica los cimientos, y tú pones los ladrillos.
Eres el responsable de que "la idea" se convierta en "software".

### Responsabilidades Clave:
1.  **Configurar**: Crear objetos, campos y reglas en Salesforce (Setup).
2.  **Documentar**: Mantener actualizado el "Diccionario de Datos" (`Gestor_de_Versiones/03-Salesforce_Admin.md`).
3.  **Mantener**: Asegurar que nadie rompa la seguridad.

---

## 🛠️ Tu Kit de Herramientas (Tutoriales Técnicos)

A diferencia de los otros roles que usan Trello o Documentos, tú usas **Salesforce Setup**.
Para guiarte en la construcción, hemos preparado manuales paso a paso:

### 🧱 Fase de Construcción (Objetos)
*   **Si tienes que crear Objetos**: [Ir a Tutoriales 01-04](../Guias_Implementacion/).
    *   `01-Carrera`: Tu primer objeto.
    *   `02-Materia`: Relaciones Master-Detail.
    *   `03-Alumno`: Validaciones de Unicidad.
    *   `04-Inscripción`: El reto del Junction Object.

### 🛡️ Fase de Seguridad y Lógica
*   **Si tienes que asegurar datos**: [Ir a Tutoriales 05-06](../Guias_Implementacion/).
    *   `05-Validaciones`: Fórmulas Regex.
    *   `06-Seguridad`: Perfiles y OWD.

### 🎨 Fase de Visualización
*   **Si tienes que armar la App**: [Ir a Tutorial 07](../Guias_Implementacion/07-Tutorial_App_Builder.md).

### 💾 Fase de Datos
*   **Si tienes que cargar Excel**: [Ir a Tutorial 08](../Guias_Implementacion/08-Tutorial_Carga_Datos.md).

---

## 👣 Tu Día a Día (Workflow)

### Paso 1: Recibir Ticket de Trello
Tomas una tarjeta de "En Progreso" (ej: "Crear Objeto Alumno").
Lees los "Criterios de Aceptación" que escribió el BA.

### Paso 2: Construir en DEV
Abres tu Org de Desarrollo (`11-Ambiente_DEV.md`).
Sigues el Tutorial correspondiente.

### Paso 3: Documentar (Tu Entregable)
Una vez creado el objeto, vas al archivo **`Gestor_de_Versiones/03-Salesforce_Admin.md`**.
Anotas allí el API Name (`Alumno__c`) y los campos que creaste.
> *Nota*: `03-Salesforce_Admin.md` es tu "Cuaderno de Bitácora".

### Paso 4: Avisar al QA
Mueves la tarjeta a "QA Testing" o "Code Review".
Le dices al Arquitecto: "Ya está listo el objeto Alumno".

---

## 💡 Pro-Tip para este Proyecto
*   **Setup Audit Trail**: Todo lo que haces queda grabado.
*   **Description Field**: Siempre llena el campo "Description" en Salesforce. El Admin del futuro te lo agradecerá.

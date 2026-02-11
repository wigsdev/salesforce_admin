# 📘 Manual de Usuario: Gestión Académica Lumina (v1.0)
**Destinatarios**: Personal Administrativo y Docente Proyecto Lumina Tech.

---

## 🏢 1. Para Personal Administrativo (Bedelía/Admisión)

### 📌 Alta de Alumnos
Para inscribir un nuevo estudiante, la **Calidad del Dato** es prioridad.
1.  Abra la App **Lumina Academic Management** desde el App Launcher.
2.  Vaya a la pestaña **Students**.
3.  Presione **New**.
4.  **Campos Críticos**:
    *   `First Name`: Ingrese primer y segundo nombre si aplica.
    *   `Last Name`: Ingrese apellido paterno y materno.
    *   `National ID`: Es obligatorio y debe tener **exactamente 8 dígitos numéricos**. (Sin puntos).
    *   `Personal Email`: Formato estándar (ej: `alumno@gmail.com`).
5.  Guarde el registro (**Save**).

### 📌 Inscripción a Materias
Una vez creado el Alumno:
1.  Vaya a la pestaña **Related > Enrollments**.
2.  Haga clic en **New**.
3.  Seleccione la **Subject** (Materia), la **Career** (Carrera) y el Ciclo Lectivo.
4.  Guarde.

> ⚠️ **Nota Legal**: Usted puede crear la inscripción, pero NO puede modificar calificaciones de exámenes cerrados ni la `Final Grade` si no tiene permisos superiores.

---

## 🎓 2. Para Profesores (Académico)

### 📝 Carga de Exámenes y Notas
Como docente, usted es responsable de la integridad de la evaluación.
1.  Ingrese a la **Subject** (Materia) y busque al alumno en la lista.
2.  Vaya a la pestaña **Related > Exams**.
3.  Haga clic en **New**.
4.  Complete los datos:
    *   `Exam Date`: Día de la evaluación.
    *   `Score`: Escala numérica **0.00 a 10.00**.
    *   `Type`: Parcial, Final, TP, etc.
    *   `Attended`: Marque o desmarque según corresponda.
5.  Guarde (**Save**).
    *   ⛔ **Bloqueo**: Notas menores a 0 o mayores a 10 serán rechazadas automáticamente.

### 🔒 Privacidad de Datos
El sistema opera bajo el modelo "Zero Trust":
*   Solo verá las materias y alumnos que **usted dicta**.
*   No tendrá acceso a datos sensibles (National ID, Phone) de alumnos que no sean suyos (según configuración de seguridad).

---

## 🚀 3. Trucos de Productividad Diaria

### 📌 Dominando las Vistas (List Views)
¿Entra a la pestaña **Students** y no ve nada?
1.  Por defecto, Salesforce muestra "Recently Viewed" (Vistos Recientemente).
2.  Haga clic en la flecha ▼ al lado del título de la lista.
3.  Seleccione **All** (Todos).
4.  📌 **Tip Experto**: Haga clic en el **Pin** (Chincheta) al lado del nombre de la vista para dejarla fija. ¡Nunca más verá la lista vacía!

### 🔍 Buscador Global
No pierda tiempo navegando. Use la barra superior para buscar por:
*   **National ID**: Encuentre un alumno al instante.
*   **Email**: Útil si no recuerda el apellido exacto.
*   **Record ID**: Si copió el ID del registro.

### ⭐ Favoritos
¿Trabaja siempre con la misma Materia o Lista?
1.  Navegue a la página que usa frecuentemente.
2.  Haga clic en la **Estrella** ⭐ (Arriba a la derecha).
3.  Ahora podrá acceder con un solo clic desde cualquier parte del sistema.

---

## 🆘 Mesa de Ayuda
Para reportar bloqueos o errores de sistema:
*   🔑 **Acceso Bloqueado**: Si el sistema pide "Código de Verificación", use la app **Salesforce Authenticator** (MFA) en su celular.
*   📧 **Soporte**: Contacte a `soporte@lumina.edu`.
*   **Tickets**: Indique siempre el **National ID** del Alumno y adjunte captura de pantalla del error.

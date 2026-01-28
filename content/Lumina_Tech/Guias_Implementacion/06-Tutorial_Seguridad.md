# 🎓 Guía Paso a Paso: Seguridad y Accesos (The Vault)
**Nivel**: Avanzado
**Tiempo Estimado**: 25 minutos
**Rol**: Security Admin

---

## 🎯 Objetivo
Configurar el modelo de seguridad "Zero Trust". Por defecto nadie ve nada, a menos que se le de permiso.

## 🛠️ Procedimiento

### Parte 1: Organization-Wide Defaults (OWD)
*Define el nivel base de acceso. "El piso".*

1.  **Setup > Sharing Settings**.
2.  Click **Edit** (Botón gris arriba).
3.  Busca el objeto **Alumno**.
4.  Cambia "Default Internal Access" a **Private**.
    *   *Significado*: Yo solo veo mis propios registros. No veo los de otros.
5.  Busca **Carrera** y **Materia**.
6.  Cambia a **Public Read Only**.
    *   *Significado*: Todos pueden ver las carreras, pero solo el Admin puede editarlas.
7.  **Save**. (Salesforce tardará unos minutos recálculando).

### Parte 2: Perfiles (Profiles)
*Define qué puede hacer un rol específico.*

1.  **Setup > Profiles**.
2.  Busca **Standard User** (o Usuario Estándar).
3.  Click en la flecha o botón **Clone**.
4.  **Profile Name**: `Lumina Profesor`. Save.
5.  Click en el nombre `Lumina Profesor` para editarlo.
6.  Click **Object Settings**.
7.  Busca **Alumno**. Click Edit.
    *   **Tab Settings**: Default On.
    *   **Object Permissions**: ☑️ Read. (Desmarcar Create, Edit, Delete).
    *   **Save**.
8.  Busca **Inscripción**. Click Edit.
    *   **Object Permissions**: ☑️ Read, ☑️ Create, ☑️ Edit. (Desmarcar Delete).
    *   *Lógica*: El profesor carga notas (Edit), pero no puede borrar al alumno de la materia.

### Parte 3: Crear un Usuario de Prueba
1.  **Setup > Users**.
2.  **New User**.
3.  Nombre: "Profesor Test".
4.  **Profile**: Selecciona `Lumina Profesor`.
5.  **Save**.

---

## ✅ Verificación de Éxito (Login As)
1.  En la lista de Users, busca "Profesor Test".
2.  Click **Login** (al lado del nombre). *Ahora ves Salesforce como él*.
3.  Intenta borrar una Inscripción.
    *   **Resultado**: El botón Delete no existe o da error.
4.  Intenta editar una Carrera.
    *   **Resultado**: Error de permisos insuficientes.

¡Sistema seguro activado! 🔐

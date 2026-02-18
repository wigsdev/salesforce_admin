# 🚀 Manual de Ejecución: Release Manager

**Tu Misión**: Llevar la carga a puerto seguro. Eres el único que toca Producción.
**Responsabilidad**: Integridad de los Ambientes. Que lo que funcionó en QA, funcione igual en PROD.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Input** | El TL ha dado el "OK Técnico" (Columna 7). |
| 📦 **BUNDLE** | **Tu Turno** | Armas el paquete (Change Set / Package.xml). |
| 🏁 **DEPLOY** | **Salida** | Ejecutas el deploy y realizas los pasos manuales. |

---

## 📅 ESTRATEGIA DE DESPLIEGUE (Sprint 1)

Tu trabajo es preparar el paquete `Release_1.0_Foundation`.

### 1. Inventario del Change Set
Asegúrate de incluir TODO esto. Si falta uno, el deploy falla.

*   **Custom Objects**:
    *   `Carrera__c`, `Materia__c`, `Alumno__c`, `Inscripcion__c`, `Nota__c`, `Asistencia__c`.
*   **Custom Fields**:
    *   Todos los campos de los objetos anteriores.
    *   *Ojo*: Incluir `Carrera__c.Estado__c` (Picklist) y `Alumno__c.DNI__c`.
*   **Validation Rules**:
    *   `Alumno__c.Formato_Email_Valido`.
    *   `Inscripcion__c.Rango_Nota_Valida`.
*   **Apps**:
    *   `Gestion_Academica_Lumina` (Lightning App).
*   **Permission Sets**:
    *   `Lumina_MFA_Required`.
*   **Profiles** (¡Cuidado con esto!):
    *   `Lumina_Professor`, `Lumina_Registrar`.
    *   *Nota*: A veces los perfiles no pasan bien por Change Set. Prepárate para ajustar a mano.

### 2. Pasos Pre-Despliegue (En PROD)
*   [ ] Verificar que el dominio `lumina-tech-university` esté activado y desplegado.

### 3. Pasos Post-Despliegue (Manual Steps)
No todo viaja por la API. Esto lo haces a mano en Producción:

*   [ ] **Organización**: Ir a *Company Information* y verificar licencias.
*   [ ] **Seguridad**:
    *   Ir a *Sharing Settings* y poner `Alumno` en **Private**. (A veces se resetea a Public).
*   [ ] **Datos Base (Seed Data)**:
    *   Tu compañero (DevOps) te dará el CSV. Cárgalo con Data Loader.

---

## 🛑 Gestión de Errores de Deploy

### Error A: "Missing Dependency"
*   **Mensaje**: `Dependent class is invalid and needs recompilation`.
*   **Solución**: Te olvidaste de agregar un campo que es referenciado por una fórmula. Búscalo y agrégalo al Change Set.

### Error B: "Test Coverage Failure"
*   **Mensaje**: `Code coverage is 0%`.
*   **Solución**: En este Sprint no hicimos Apex, así que selecciona **Run Local Tests** (o **No Test Run** si es Sandbox->Sandbox, aunque NO recomendado para Prod).

---

## 📚 Recursos Relacionados
- 📘 **Tutorial de Rol**: [04-Rol_Release_Manager.md](../Tutoriales_por_Rol/04-Rol_Release_Manager.md)
- 📘 **Lista de Componentes**: [HISTORIAS_DE_USUARIO_ES_ES.md](../Archivos_intermedios/HISTORIAS_DE_USUARIO_ES_ES.md) (Tu checklist de qué incluir).
- 🔄 **Diagrama Trello**: [DIAGRAMA_FLUJO_TRELLO.md](../DIAGRAMA_FLUJO_TRELLO.md)

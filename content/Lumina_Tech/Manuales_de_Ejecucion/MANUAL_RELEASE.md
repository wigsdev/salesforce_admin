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
    *   `Career__c`, `Subject__c`, `Student__c`, `Enrollment__c`.
*   **Custom Fields**:
    *   Todos los campos de los objetos anteriores.
    *   *Ojo*: Incluir `Career__c.Status__c` (Picklist).
*   **Validation Rules**:
    *   `Student__c.Valid_Institutional_Email`.
    *   `Enrollment__c.Grade_Range_1_10`.
*   **Apps**:
    *   `Lumina_Academic` (Lightning App).
*   **Permission Sets**:
    *   `Lumina_MFA_Access`.
*   **Profiles** (¡Cuidado con esto!):
    *   `Lumina Professor`, `Lumina Registrar`.
    *   *Nota*: A veces los perfiles no pasan bien por Change Set. Prepárate para ajustar a mano.

### 2. Pasos Pre-Despliegue (En PROD)
*   [ ] Verificar que el dominio `lumina-university` esté activado y desplegado.

### 3. Pasos Post-Despliegue (Manual Steps)
No todo viaja por la API. Esto lo haces a mano en Producción:

*   [ ] **Organización**: Ir a *Company Information* y verificar licencias.
*   [ ] **Seguridad**:
    *   Ir a *Sharing Settings* y poner `Student` en **Private**. (A veces se resetea a Public).
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
- 📘 **Lista de Componentes**: [HISTORIAS_DE_USUARIO.md](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md) (Tu checklist de qué incluir).
- 🔄 **Diagrama Trello**: [DIAGRAMA_FLUJO_TRELLO.md](../DIAGRAMA_FLUJO_TRELLO.md)

# 🏗️ Manual de Ejecución: Team Lead (TL)

**Tu Misión**: Calidad Técnica y Gobernanza. Eres el portero. Nada entra a Producción si está "sucio".
**Responsabilidad**: Garantizar que lo construido coincida con lo diseñado (`MANUAL_CONSULTANT.md`).

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **5. SF QA** | QA ha validado que "funciona" funcionalmente. |
| 🔍 **REVIEW** | **Tu Turno** | Revisas las tripas: Naming Conventions, Seguridad, Performance. |
| 👋 **HANDOFF** | **7. SF Producción** | Das el "Golden Ticket". Autorizas el Merge/Deploy. |

---

## 📅 RUTINA DE AUDITORÍA (Definition of Done)

Cuando una tarjeta llega a tu escritorio, ejecuta este checklist implacable.

### 1. Auditoría de Naming Conventions
*   **Contexto**: El Admin puede haber creado `Career` como `Carrera__c` por error.
*   **Checklist**:
    *   [ ] Objetos Custom: PascalCase en Español (`Inscripcion__c`, `Alumno__c`).
    *   [ ] Campos Custom: Snake_case en Español (`DNI__c`, `Nota_Final__c`).
    *   [ ] ¿Hay campos "Test1", "Prueba" o basura? -> **RECHAZAR**.

### 2. Auditoría de Seguridad (Security Review)
*   **Contexto**: Un campo abierto es una brecha de seguridad.
*   **Checklist**:
    *   [ ] **OWD**: Confirmar que `Alumno` esté en **Private**.
    *   [ ] **FLS**: Verificar que el perfil `Lumina_Professor` NO tenga Read Access a `DNI__c`.
    *   [ ] **MFA**: Verificar que el Permission Set `Lumina_MFA_Required` no esté asignado a "Guest Users" por error.

### 3. Auditoría de Calidad (Best Practices)
*   **Contexto**: Evitar deuda técnica.
*   **Checklist**:
    *   [ ] **Validaciones**: ¿Tienen mensajes de error amigables? (No "Formula Error").
    *   [ ] **Descripciones**: ¿Todos los campos nuevos tienen el campo `Description` lleno?
    *   [ ] **Deprecación**: ¿Se borraron los campos temporales?

---

## 🛑 Gestión de Bloqueos (Troubleshooting)

### Caso A: "El Admin dice que no puede cumplir el requisito"
*   **Acción**: Revisa el `MANUAL_CONSULTANT.md`.
*   *Solución*: Si el diseño era imposible, autoriza un cambio de alcance (Change Request) y actualiza la HU.

### Caso B: "QA encontró un bug crítico el último día"
*   **Acción**: Evaluar severidad.
*   *Solución*: Si rompe el Core (Inscripción), se detiene el Release. Si es cosmético (Color incorrecto), se crea un "Bug Ticket" para Sprint 2.

---

## 📚 Recursos Relacionados
- 📘 **Tutorial de Rol**: [07-Rol_Team_Lead.md](../Tutoriales_por_Rol/07-Rol_Team_Lead.md)
- 📘 **Manual Consultor**: [MANUAL_CONSULTANT.md](MANUAL_CONSULTANT.md) (Tu referencia de verdad)
- 🛡️ **Diagrama Seguridad**: [DIAGRAMA_SEGURIDAD.md](../DIAGRAMA_SEGURIDAD.md)

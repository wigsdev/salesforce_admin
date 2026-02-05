# 📝 Tarea: Relación entre Objetos

**Rol Responsable**: 🏗️ **Salesforce Consultant**
**Referencia**: HU-003, HU-004
**Destino en Gestor**: [`02-Salesforce_Consultant.md`](../../Gestor_de_Versiones/02-Salesforce_Consultant.md)

## Diseño de Arquitectura de Datos (ERD)

Mi trabajo es asegurar que los objetos "hablen" entre sí para cumplir con **[REQ-DATA-002] Historial Académico**.

### 📊 Esquema Relacional

*Nota: Se adjunta diagrama lógico y versión texto por compatibilidad.*

#### Opción A: Código Mermaid (Requiere Extension)
```mermaid
erDiagram
    %% Relaciones
    CAREER ||--o{ SUBJECT : "Contiene"
    SUBJECT ||--o{ ENROLLMENT : "Tiene"
    STUDENT ||--o{ ENROLLMENT : "Realiza"
    ENROLLMENT ||--o{ EXAM : "Genera"

    %% Definición de Entidades y Atributos
    CAREER {
        string Name
    }
    
    SUBJECT {
        string Name
        lookup Career
    }
    
    STUDENT {
        string RecordName
        string National_ID
    }
    
    ENROLLMENT {
        picklist Cycle
        picklist Status
    }
    
    EXAM {
        number Final_Grade
        date Date
    }
```

#### Opción B: Diagrama Lógico (Texto)
Si no visualizas el gráfico de arriba, esta es la jerarquía:

```text
[ CAREER ]
     |
     +---<tiene>---( SUBJECT )
                        |
                        +---<tiene>---( ENROLLMENT )---<realiza>---[ STUDENT ]
                                            |
                                            +---<genera>---( EXAM )
```

**Explicación de Cardinalidad:**
1.  **Career --(1:N)--> Subject**: Una carrera tiene muchas materias.
2.  **Subject --(1:N)--> Enrollment**: Una materia tiene muchos inscritos.
3.  **Student --(1:N)--> Enrollment**: Un alumno tiene muchas inscripciones.
4.  **Enrollment --(1:N)--> Exam**: Una inscripción tiene varios exámenes (Parciales/Finales).

---

### 1. Modelo de Inscripción (Junction Object)
El requerimiento [REQ-DATA-002] dice: *"Un alumno cursa muchas materias, una materia tiene muchos alumnos e historial"*.
*   **Solución**: Relación `Many-to-Many`.
*   **Objeto Intermedio**: `Enrollment__c`.
*   **Relaciones**:
    1.  `Enrollment__c` ➡️ **Master-Detail** ➡️ `Student__c`.
    2.  `Enrollment__c` ➡️ **Master-Detail** ➡️ `Subject__c`.

### 2. Modelo de Exámenes (Evaluación Continua)
Responde a **[REQ-FUNC-001] Ciclo de Exámenes**.
*   **Relación**: `Exam__c` ➡️ **Master-Detail** ➡️ `Enrollment__c`.
*   **Justificación**: Un examen no existe sin una inscripción activa.

### 3. Career - Subject
*   **Relación**: `Subject__c` ➡️ **Lookup** ➡️ `Career__c`.
*   **Justificación**: Facilita [REQ-SEC-002], permitiendo reasignar materias sin perder integridad.

---
**Validación**: Esquema 100% compliant con REQ-DATA-002.

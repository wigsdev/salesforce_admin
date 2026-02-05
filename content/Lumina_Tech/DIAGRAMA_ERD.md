# 🗂️ Diagrama ERD: Modelo de Datos Lumina Tech

```mermaid
erDiagram
    CAREER ||--o{ SUBJECT : "offers"
    SUBJECT ||--o{ ENROLLMENT : "is_studied_in"
    STUDENT ||--o{ ENROLLMENT : "enrolls_in"
    ENROLLMENT ||--o{ EXAM : "has_evaluation"
    
    CAREER {
        string Name
        string Career__c
        number Duration_Years__c
        picklist Type__c
        date CreatedDate
    }
    
    SUBJECT {
        string Name
        string Subject__c
        number Credits__c
        lookup Career__c FK
        number Max_Capacity__c
    }
    
    STUDENT {
        string Name
        string Student__c
        number National_ID__c UK "External ID"
        string First_Name__c
        string Last_Name__c
        email Email__c UK
        phone Phone__c
        textarea Address__c
    }
    
    ENROLLMENT {
        string Name
        string Enrollment__c
        lookup Student__c FK
        lookup Subject__c FK
        picklist Status__c "Enrolled, Passed, Failed"
        number Final_Grade__c "0-10"
        formula Subject_Display__c
        date Enrollment_Date__c
    }
    
    EXAM {
        string Name
        string Exam__c
        lookup Enrollment__c FK "Master-Detail"
        number Score__c
        date Exam_Date__c
        checkbox Attended__c
    }
```

## Leyenda de Relaciones

| Relación | Tipo | Descripción |
|----------|------|-------------|
| **Career → Subject** | Master-Detail | A Subject belongs to a Career |
| **Student → Enrollment** | Master-Detail | Enrollment depends on Student |
| **Subject → Enrollment** | Master-Detail | Enrollment depends on Subject |
| **Enrollment → Exam** | Master-Detail | Exams are part of an Enrollment |

## Leyenda de Tipos de Campo

- **string**: Texto
- **number**: Número
- **picklist**: Lista de valores
- **date**: Fecha
- **email**: Email
- **phone**: Teléfono
- **text**: Texto largo
- **lookup**: Relación (FK = Foreign Key)
- **formula**: Campo calculado
- **UK**: Unique Key (campo único)

## Validaciones Clave

1. **National ID**: Unique in the system
2. **Email**: Unique and strictly formatted as `@lumina.edu`
3. **Final Grade**: Strictly between 0.00 and 10.00
4. **Status**: Picklist based (Enrolled, Passed, Failed) - No auto-calculation yet (Sprint 2)

## Referencias

- **Guía de Objetos**: [01-Tutorial_Carrera.md](../Guias_Implementacion/01-Tutorial_Carrera.md)
- **Guía de Relaciones**: [04-Tutorial_Inscripcion.md](../Guias_Implementacion/04-Tutorial_Inscripcion.md)
- **Schema Builder**: [09-Tutorial_Schema_Builder.md](../Guias_Implementacion/09-Tutorial_Schema_Builder.md)

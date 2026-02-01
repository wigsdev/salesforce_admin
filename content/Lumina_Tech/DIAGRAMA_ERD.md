# 🗂️ Diagrama ERD: Modelo de Datos Lumina Tech

```mermaid
erDiagram
    CARRERA ||--o{ MATERIA : "tiene"
    MATERIA ||--o{ INSCRIPCION : "recibe"
    ALUMNO ||--o{ INSCRIPCION : "se_inscribe_en"
    
    CARRERA {
        string Nombre_Carrera__c
        number Duracion_Anios__c
        picklist Tipo__c
        date Fecha_Creacion__c
    }
    
    MATERIA {
        string Nombre_Materia__c
        number Creditos__c
        lookup Carrera__c FK
        number Cupo_Maximo__c
    }
    
    ALUMNO {
        string DNI__c UK
        string Nombre__c
        string Apellido__c
        email Email_Institucional__c UK
        phone Telefono__c
        text Direccion__c
        formula Nombre_Completo__c
    }
    
    INSCRIPCION {
        lookup Alumno__c FK
        lookup Materia__c FK
        picklist Estado__c
        number Nota_Final__c
        formula Estado_Cursada__c
        formula Semaforo__c
        date Fecha_Inscripcion__c
    }
```

## Leyenda de Relaciones

| Relación | Tipo | Descripción |
|----------|------|-------------|
| **Carrera → Materia** | Master-Detail | Una materia pertenece a una carrera |
| **Alumno → Inscripción** | Master-Detail | Inscripción depende del alumno |
| **Materia → Inscripción** | Master-Detail | Inscripción depende de la materia |

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

1. **DNI**: Único en todo el sistema
2. **Email Institucional**: Único y formato `@lumina.edu`
3. **Nota Final**: Entre 0 y 10
4. **Estado Cursada**: Automático (Aprobado si Nota >= 6)

## Referencias

- **Guía de Objetos**: [01-Tutorial_Carrera.md](../Guias_Implementacion/01-Tutorial_Carrera.md)
- **Guía de Relaciones**: [04-Tutorial_Inscripcion.md](../Guias_Implementacion/04-Tutorial_Inscripcion.md)
- **Schema Builder**: [09-Tutorial_Schema_Builder.md](../Guias_Implementacion/09-Tutorial_Schema_Builder.md)

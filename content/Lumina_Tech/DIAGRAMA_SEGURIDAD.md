# 🛡️ Diagrama de Arquitectura de Seguridad

```mermaid
graph TB
    subgraph "Organization-Wide Defaults (OWD)"
        OWD1["Carrera: Public Read Only"]
        OWD2["Materia: Public Read Only"]
        OWD3["Alumno: Private"]
        OWD4["Inscripción: Controlled by Parent"]
    end
    
    subgraph "Perfiles"
        P1["👔 Bedel<br/>CRUD: Alumno, Inscripción<br/>FLS: Nota = Read-Only"]
        P2["👨‍🏫 Profesor<br/>Read: Alumno (solo sus materias)<br/>FLS: Nota = Edit"]
    end
    
    subgraph "Permission Sets"
        PS1["🔐 Lumina_MFA_Access<br/>MFA Habilitado"]
        PS2["📊 Dashboard_Rectoria<br/>Acceso a reportes ejecutivos"]
    end
    
    subgraph "Field-Level Security (FLS)"
        FLS1["DNI: Read-Only para Profesor"]
        FLS2["Nota_Final: Edit para Profesor"]
        FLS3["Nota_Final: Read-Only para Bedel"]
        FLS4["Email: Edit para Bedel"]
    end
    
    OWD3 --> P1
    OWD3 --> P2
    P1 --> FLS3
    P1 --> FLS4
    P2 --> FLS1
    P2 --> FLS2
    P1 -.-> PS1
    P2 -.-> PS1
    
    style OWD1 fill:#e3f2fd
    style OWD2 fill:#e3f2fd
    style OWD3 fill:#ffebee
    style OWD4 fill:#fff3e0
    style P1 fill:#c8e6c9
    style P2 fill:#c8e6c9
    style PS1 fill:#f8bbd0
    style PS2 fill:#f8bbd0
```

## Matriz de Permisos

| Objeto | Bedel | Profesor | Justificación |
|--------|-------|----------|---------------|
| **Carrera** | Read | Read | Información pública |
| **Materia** | Read | Read | Información pública |
| **Alumno** | CRUD | Read* | Bedel gestiona, Profesor solo ve sus alumnos |
| **Inscripción** | CRUD | Read* | Bedel inscribe, Profesor ve sus inscripciones |
| **Campo: DNI** | Edit | Read-Only | Solo Bedel actualiza datos personales |
| **Campo: Nota_Final** | Read-Only | Edit | Solo Profesor califica |

*\*Read limitado por OWD: Profesor solo ve alumnos de sus materias*

## Principios de Seguridad Aplicados

### 1. **Zero Trust** (Confianza Cero)
- OWD = Private por defecto
- Acceso explícito mediante Sharing Rules o Perfiles

### 2. **Least Privilege** (Mínimo Privilegio)
- Cada perfil tiene solo los permisos necesarios
- Permission Sets para casos especiales (MFA)

### 3. **Segregation of Duties (SoD)**
- Bedel NO puede calificar
- Profesor NO puede modificar datos personales

### 4. **Defense in Depth** (Defensa en Profundidad)
- Capa 1: OWD (nivel objeto)
- Capa 2: Perfil (CRUD)
- Capa 3: FLS (nivel campo)
- Capa 4: Validation Rules (lógica de negocio)
- Capa 5: MFA (autenticación)

## Referencias

- **Guía de Seguridad**: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md)
- **Manual Consultant**: [MANUAL_CONSULTANT.md](../Manuales_de_Ejecucion/MANUAL_CONSULTANT.md)
- **Bitácora Día 4**: [dia_4/](../Bitacoras_Sprint_1/dia_4/)

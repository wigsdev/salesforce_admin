# 🛡️ Diagrama de Arquitectura de Seguridad

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#fff','primaryTextColor':'#000','primaryBorderColor':'#000','lineColor':'#000','fontSize':'13px'}}}%%
graph TB
    subgraph OWD["<b>Organization-Wide Defaults (OWD)</b>"]
        OWD1["Carrera:<br/>Public Read Only"]
        OWD2["Materia:<br/>Public Read Only"]
        OWD3["Alumno:<br/>Private"]
        OWD4["Inscripción:<br/>Controlled by Parent"]
    end
    
    subgraph PROF["<b>Perfiles</b>"]
        P1["👔 Bedel<br/>CRUD: Alumno, Inscripción<br/>FLS: Nota = Read-Only"]
        P2["👨‍🏫 Profesor<br/>Read: Alumno (solo sus materias)<br/>FLS: Nota = Edit"]
    end
    
    subgraph PS["<b>Permission Sets</b>"]
        PS1["🔐 Lumina_MFA_Access<br/>MFA Habilitado"]
        PS2["📊 Dashboard_Rectoria<br/>Acceso a reportes ejecutivos"]
    end
    
    subgraph FLS["<b>Field-Level Security (FLS)</b>"]
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
    
    classDef owdStyle fill:#fff,stroke:#000,stroke-width:2px,color:#000
    classDef profileStyle fill:#f5f5f5,stroke:#000,stroke-width:2px,color:#000
    classDef psStyle fill:#e0e0e0,stroke:#000,stroke-width:2px,color:#000,stroke-dasharray: 5 5
    
    class OWD1,OWD2,OWD3,OWD4 owdStyle
    class P1,P2 profileStyle
    class PS1,PS2,FLS1,FLS2,FLS3,FLS4 psStyle
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

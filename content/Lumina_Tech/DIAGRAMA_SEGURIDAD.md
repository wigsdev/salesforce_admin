# 🛡️ Diagrama de Arquitectura de Seguridad

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#fff','primaryTextColor':'#000','primaryBorderColor':'#000','lineColor':'#000','fontSize':'13px'}}}%%
graph TB
    subgraph OWD["<b>Organization-Wide Defaults (OWD)</b>"]
        OWD1["Career:<br/>Public Read Only"]
        OWD2["Subject:<br/>Public Read Only"]
        OWD3["Student:<br/>Private"]
        OWD4["Enrollment:<br/>Controlled by Parent"]
    end
    
    subgraph PROF["<b>Profiles / PSG</b>"]
        P1["👔 Registrar (Bedel)<br/>CRUD: Student, Enrollment<br/>FLS: Final_Grade = Read-Only"]
        P2["👨‍🏫 Professor<br/>Read: Student (My Students)<br/>FLS: Final_Grade = Edit"]
    end
    
    subgraph PS["<b>Permission Sets</b>"]
        PS1["🔐 Lumina_MFA_Access<br/>MFA Enabled"]
        PS2["📊 Lumina_Registrar_Access<br/>Admin Capabilities"]
    end
    
    subgraph FLS["<b>Field-Level Security (FLS)</b>"]
        FLS1["National_ID: Read-Only for Professor"]
        FLS2["Final_Grade: Edit for Professor"]
        FLS3["Final_Grade: Read-Only for Registrar"]
        FLS4["Email: Edit for Registrar"]
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

| Objeto | Registrar (Bedel) | Professor | Justificación |
|--------|-------------------|-----------|---------------|
| **Career** | Read | Read | Información pública |
| **Subject** | Read | Read | Información pública |
| **Student** | CRUD | Read* | Bedel gestiona, Professor solo ve sus alumnos |
| **Enrollment** | CRUD | Read* | Bedel inscribe, Professor ve sus inscripciones |
| **Campo: National_ID** | Edit | Read-Only | Solo Bedel actualiza datos personales |
| **Campo: Final_Grade** | Read-Only | Edit | Solo Professor califica |

*\*Read limitado por OWD: Professor solo ve alumnos de sus materias*

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

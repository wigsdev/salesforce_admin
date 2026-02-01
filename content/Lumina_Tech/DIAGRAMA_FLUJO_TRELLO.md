# 🔄 Diagrama de Flujo: Proceso Trello (8 Columnas)

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#fff','primaryTextColor':'#000','primaryBorderColor':'#000','lineColor':'#000','secondaryColor':'#f5f5f5','tertiaryColor':'#e0e0e0','fontSize':'14px'}}}%%
graph LR
    A["<b>1. Backlog</b><br/>(PO + BA)"] --> B["<b>2. Sprint Backlog</b><br/>(PO)"]
    B --> C["<b>3. En Progreso</b><br/>(Admin)"]
    C --> D["<b>4. SF Desarrollo</b><br/>(Admin)"]
    D --> E["<b>5. SF QA</b><br/>(QA Tester)"]
    E -->|"❌ Falla"| C
    E -->|"✅ Pasa"| F["<b>6. Aprobación TL</b><br/>(Team Lead)"]
    F -->|"❌ Rechaza"| C
    F -->|"✅ Aprueba"| G["<b>7. SF Producción</b><br/>(Release Manager)"]
    G --> H["<b>8. Terminado</b><br/>(Done)"]
    
    classDef defaultStyle fill:#fff,stroke:#000,stroke-width:3px,color:#000
    classDef progressStyle fill:#f5f5f5,stroke:#000,stroke-width:3px,color:#000
    classDef doneStyle fill:#e0e0e0,stroke:#000,stroke-width:3px,color:#000
    
    class A,B defaultStyle
    class C,D,E,F,G progressStyle
    class H doneStyle
```

## Leyenda de Responsables

| Columna | Responsable | Acción Principal |
|---------|-------------|------------------|
| **1. Backlog** | PO + BA | Crear y refinar HUs |
| **2. Sprint Backlog** | PO | Priorizar para el Sprint |
| **3. En Progreso** | Admin | Construir en Sandbox |
| **4. SF Desarrollo** | Admin | Entregar para testing |
| **5. SF QA** | QA Tester | Probar funcionalidad |
| **6. Aprobación TL** | Team Lead | Revisar calidad técnica |
| **7. SF Producción** | Release Manager | Desplegar a PROD |
| **8. Terminado** | Release Manager | Cerrar tarea |

## Flujos de Retroceso

- **QA Falla** (5 → 3): Bug encontrado, vuelve a desarrollo
- **TL Rechaza** (6 → 3): Problema de calidad técnica (naming, seguridad)

## Referencias

- **Manual Maestro**: [MANUAL_MAESTRO.md](../Manuales_de_Ejecucion/MANUAL_MAESTRO.md)
- **Tutorial Scrum Master**: [08-Rol_Scrum_Master.md](../Tutoriales_por_Rol/08-Rol_Scrum_Master.md)

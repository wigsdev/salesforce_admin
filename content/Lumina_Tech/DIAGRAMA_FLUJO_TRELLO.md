# 🔄 Diagrama de Flujo: Proceso Trello (8 Columnas)

```mermaid
graph LR
    A["1. Backlog<br/>(PO + BA)"] --> B["2. Sprint Backlog<br/>(PO)"]
    B --> C["3. En Progreso<br/>(Admin)"]
    C --> D["4. SF Desarrollo<br/>(Admin)"]
    D --> E["5. SF QA<br/>(QA Tester)"]
    E -->|❌ Falla| C
    E -->|✅ Pasa| F["6. Aprobación TL<br/>(Team Lead)"]
    F -->|❌ Rechaza| C
    F -->|✅ Aprueba| G["7. SF Producción<br/>(Release Manager)"]
    G --> H["8. Terminado<br/>(Done)"]
    
    style A fill:#e3f2fd
    style B fill:#fff3e0
    style C fill:#fff9c4
    style D fill:#f0f4c3
    style E fill:#ffe0b2
    style F fill:#ffccbc
    style G fill:#d1c4e9
    style H fill:#c8e6c9
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

# 🎨 Tener en cuenta el diseño

**Rol Responsable**: 🏗️ **Salesforce Architect** / 🎨 **UX Specialist**
**Destino en Gestor**: [`02-Salesforce_Consultant.md`](../Gestor_de_Versiones/02-Salesforce_Consultant.md) (ADR Branding)

## Definición de Identidad Visual (Day 2)

### 1. El Problema de la "Org en Blanco"
Salesforce, por defecto, se ve corporativo y genérico (azul standard). Para **Lumina Tech**, la experiencia debe sentirse universitaria, moderna y acogedora desde el primer login.

### 2. Estrategia de Branding
No se trata solo de ser "bonito", sino de **usabilidad** y **sentido de pertenencia**.

*   **Paleta de Colores**:
    *   **Primary**: `#005A9C` (Lumina Blue) - Usado en Header y Botones.
    *   **Secondary**: `#F2A900` (Tech Gold) - Acentos y Call-to-Action.
    *   **Background**: `#F4F6F9` (Soft Grey) - Fondos de página.
*   **Logo**: Distintivo "Lumina Tech" con iconografía de educación (birrete/libro).
*   **Temas**: Uso de `Salesforce Lightning Themes & Branding` para aplicar estos cambios sin código CSS complejo.

### 3. Consideraciones de UX
*   **Contraste**: Asegurar que el texto blanco sobre fondo azul sea legible (WCAG AA).
*   **Densidad**: Configurar la densidad de pantalla en "Comfy" para administrativos (muchos datos) vs "Compact" para listas largas.

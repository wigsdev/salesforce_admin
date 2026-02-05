# 🕵️ Manual de Ejecución: Business Analyst (BA)

**Tu Misión**: Eres el Estratega. Defines QUÉ se va a construir antes de que nadie escriba una línea de código. Transformas necesidades vagas en Requerimientos de Acero.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Entrada** | Recibes el "Dolor del Cliente" (ej. "Perdemos datos de alumnos"). |
| 📝 **SPEC** | **Tu Turno** | Escribes Historias de Usuario (HU) en `HISTORIAS_DE_USUARIO.md` y Trello. |
| 👋 **HANDOFF** | **Salida** | Mueves tarjeta a "Ready for Dev" y avisas al Salesforce Admin. |

---

## 📅 CRONOGRAMA DE ESTRATEGIA (Sprint 1: Fundamentos)

### 📅 DÍA 0: Discovery & Entendimiento
*Objetivo: Entender el negocio antes de proponer soluciones.*

1.  **Analizar el Caso Lumina Tech**
    *   **Acción**: Identifica actores (Rector, Bedelía, Profesores).
    *   **Producto**: Mapa de Actores.

2.  **Refinar el Backlog Maestro**
    *   **Acción**: Revisa el documento [HISTORIAS_DE_USUARIO.md](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md).
    *   **Validación**: Asegura que las 12 HUs cubran el alcance del MVP.

---

### 📅 DÍA 1: Datos Core (Modelado)
*Definir la estructura de la información.*

#### 📝 Misión: Especificar el Modelo Académico
*   **HUs a Definir**:
    *   [HU-001](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Inscripciones (Many-to-Many).
    *   [HU-002](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Identidad (`National ID`).
    *   [HU-003](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Notas (`Final Grade`).
*   **Criterios Clave**:
    *   Especifica tipos de datos exactos (Picklist vs Texto).
    *   Define unicidad (DNI 8 dígitos).

---

### 📅 DÍA 2: Identidad & UX
*Definir cómo se ve y se siente el sistema.*

#### 📝 Misión: Especificar Branding
*   **HUs a Definir**:
    *   [HU-004](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): My Domain.
    *   [HU-005](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Look & Feel.
    *   [HU-006](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Lightning App.
*   **Criterios Clave**:
    *   Colores Hexadecimales exactos.
    *   Navegación (Tabs) requerida.

---

### 📅 DÍA 3: Calidad & Reglas de Negocio
*Blindar la base de datos.*

#### 📝 Misión: Especificar Validaciones
*   **HUs a Definir**:
    *   [HU-007](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Email (`.edu`).
    *   [HU-008](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Rango Notas (1-10).
    *   [HU-009](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Asistencia (<75% Libre).
*   **Criterios Clave**:
    *   Redactar el "Mensaje de Error" exacto que debe ver el usuario.
    *   Proveer la fórmula lógica (Regex/And/Or) al Admin.

---

### 📅 DÍA 4: Seguridad Zero Trust
*Proteger los activos de información.*

#### 📝 Misión: Matriz de Permisos
*   **HUs a Definir**:
    *   [HU-010](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Visibilidad (OWD Private).
    *   [HU-011](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): MFA (2FA).
    *   [HU-012](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md): Segregación (SoD).
*   **Criterios Clave**:
    *   Definir Perfiles: `Lumina Professor` vs `Lumina Registrar`.
    *   Especificar qué campos son Read-Only para quién.

---

## 🃏 Herramienta: Planning Poker (Estimación)
*Tu responsabilidad es liderar la sesión de estimación.*

1.  Reúne al equipo (Admin + QA).
2.  Lee la HU.
3.  Voten Story Points (1, 3, 5).
4.  **Referencia**: [2_Votar_Dificultad.md](../Bitacoras_Sprint_1/dia_5/2_Votar_Dificultad.md).

---

## 📚 Recursos Relacionados
- 📘 **Tutorial de Rol**: [01-Rol_Business_Analyst.md](../Tutoriales_por_Rol/01-Rol_Business_Analyst.md)
- 📘 **Backlog Maestro**: [HISTORIAS_DE_USUARIO.md](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
- 📘 **Glosario**: [GLOSARIO.md](../GLOSARIO.md)
- 🔄 **Diagrama Trello**: [DIAGRAMA_FLUJO_TRELLO.md](../DIAGRAMA_FLUJO_TRELLO.md)

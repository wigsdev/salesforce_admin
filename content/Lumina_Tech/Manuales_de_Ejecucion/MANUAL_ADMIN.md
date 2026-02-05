# 🛡️ Manual de Ejecución: Salesforce Admin

**Tu Misión**: Construir. Transformas Historias de Usuario (Tarjetas) en Soluciones.
**Territorio**: Columnas **3. En Progreso** y **4. SF Desarrollo**.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **2. Sprint Backlog** | Buscas la tarjeta específica (ej. HU-001). |
| 🔨 **BUILD** | **3. En Progreso** | La mueves aquí mientras trabajas en Salesforce. |
| 👋 **HANDOFF** | **4. SF Desarrollo** | La mueves aquí al terminar. El QA toma el relevo. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN (Sprint 1: Las 12 Historias)

### 📅 DÍA 1: Cimientos de Datos (Modelado)
*Crea los objetos donde vivirá la información.*

#### 🏷️ Misión 1: El Modelo Académico (HU-001)
*   **Backlog**: [HU-001: Gestión de Inscripciones](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Crear objetos `Career`, `Subject` e `Enrollment`.
    *   🔨 Usa: [01-Tutorial_Carrera.md](../Guias_Implementacion/01-Tutorial_Carrera.md)
    *   🔨 Usa: [02-Tutorial_Materia.md](../Guias_Implementacion/02-Tutorial_Materia.md)
    *   🔨 Usa: [04-Tutorial_Inscripcion.md](../Guias_Implementacion/04-Tutorial_Inscripcion.md)

#### 🏷️ Misión 2: Identidad del Alumno (HU-002)
*   **Backlog**: [HU-002: Identidad Única](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Configurar `Student` con `National ID` único y ID automático.
    *   🔨 Usa: [03-Tutorial_Alumno.md](../Guias_Implementacion/03-Tutorial_Alumno.md)
    *   🔨 Usa: [05-Tutorial_Validaciones.md](../Guias_Implementacion/05-Tutorial_Validaciones.md) (Caso D: Validación DNI)

#### 🏷️ Misión 3: Integridad de Notas (HU-003)
*   **Backlog**: [HU-003: Notas y Auditoría](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Crear campo `Final Grade` (Number 4,2) y activar Field History.
    *   🔨 Usa: [04-Tutorial_Inscripcion.md](../Guias_Implementacion/04-Tutorial_Inscripcion.md) (Paso 5)

---

### 📅 DÍA 2: Identidad Visual (Branding)
*Que la app se sienta profesional.*

#### 🏷️ Misión 4: Tu Propio Dominio (HU-004)
*   **Backlog**: [HU-004: Dominio Seguro](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Configura My Domain (`lumina-university`).
    *   🔨 Usa: [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md) (Sección Dominio)

#### 🏷️ Misión 5: Colores y Logo (HU-005)
*   **Backlog**: [HU-005: Identidad Institucional](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Sube el logo y activa el Theme corporativo.
    *   🔨 Usa: [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md) (Sección Temas)

#### 🏷️ Misión 6: La App Central (HU-006)
*   **Backlog**: [HU-006: App de Gestión](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Crea la Lightning App "Gestión Académica".
    *   🔨 Usa: [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md) (Sección App)

---

### 📅 DÍA 3: Calidad de Datos (Reglas)
*Evitar basura en la base de datos.*

#### 🏷️ Misión 7: Email Limpio (HU-007)
*   **Backlog**: [HU-007: Validación Email](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Regex para `@lumina.edu`.
    *   🔨 Usa: [05-Tutorial_Validaciones.md](../Guias_Implementacion/05-Tutorial_Validaciones.md) (Caso A)

#### 🏷️ Misión 8: Notas Lógicas (HU-008)
*   **Backlog**: [HU-008: Integridad Numérica](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Validation Rule `1..10`.
    *   🔨 Usa: [05-Tutorial_Validaciones.md](../Guias_Implementacion/05-Tutorial_Validaciones.md) (Caso B)

#### 🏷️ Misión 9: Automatización Asistencia (HU-009)
*   **Backlog**: [HU-009: Control de Asistencia](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Fórmulas de Porcentaje y Condición Académica.
    *   🔨 Usa: [04-Tutorial_Inscripcion.md](../Guias_Implementacion/04-Tutorial_Inscripcion.md) (Paso 6)

---

### 📅 DÍA 4: Seguridad (Zero Trust)
*Protege la información.*

#### 🏷️ Misión 10: Matriz de Visibilidad (HU-010)
*   **Backlog**: [HU-010: Visibilidad](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: OWD Private + Sharing Rules.
    *   🔨 Usa: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md) (Parte 1 y 5)

#### 🏷️ Misión 11: Doble Factor (HU-011)
*   **Backlog**: [HU-011: MFA](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Permission Set MFA.
    *   🔨 Usa: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md) (Parte 3)

#### 🏷️ Misión 12: Segregación de Roles (HU-012)
*   **Backlog**: [HU-012: SoD](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
*   **Ejecución**: Perfiles Professor vs Registrar.
    *   🔨 Usa: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md) (Parte 2)

---

## 🎁 Misiones Bonus (Tools de Poder)

#### 💾 Misión Data: Carga Masiva
*   **Objetivo**: Cargar alumnos desde Excel sin teclear.
    *   🔨 Usa: [08-Tutorial_Carga_Datos.md](../Guias_Implementacion/08-Tutorial_Carga_Datos.md)

#### �️ Misión Architect: Vista de Pájaro
*   **Objetivo**: Ver el diagrama de la base de datos en vivo.
    *   🔨 Usa: [09-Tutorial_Schema_Builder.md](../Guias_Implementacion/09-Tutorial_Schema_Builder.md)

---

## 📚 Recursos Relacionados
- 📘 **Guías Técnicas**: [Guias_Implementacion](../Guias_Implementacion/)
- 📘 **Backlog Detallado**: [HISTORIAS_DE_USUARIO.md](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
- � **Glosario**: [GLOSARIO.md](../GLOSARIO.md)
- � **Diagrama ERD**: [DIAGRAMA_ERD.md](../DIAGRAMA_ERD.md)

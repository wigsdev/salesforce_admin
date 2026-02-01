# 🛡️ Manual de Ejecución: Salesforce Admin

**Tu Misión**: Construir. Transformas Tarjetas en Soluciones.
**Territorio**: Columnas **3. En Progreso** y **4. SF Desarrollo**.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Columna Trello | Significado |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **2. Sprint Backlog** | Buscas la tarjeta específica (ej. HU-001). |
| 🔨 **BUILD** | **3. En Progreso** | La mueves aquí mientras trabajas en Salesforce. |
| 👋 **HANDOFF** | **4. SF Desarrollo** | La mueves aquí al terminar. El QA toma el relevo. |

---

## 📅 CRONOGRAMA DE EJECUCIÓN (Sprint 1: Las 11 Historias)

### 📅 DÍA 1: Cimientos de Datos (Modelado)
*Crea los objetos donde vivirá la información.*

#### 🏷️ Misión 1: El Modelo Académico (HU-001)
1.  **Trello**: Busca la tarjeta **HU-001: Gestión de Inscripciones**.
2.  **Acción**: Muévela a **3. En Progreso**.
3.  **Ejecución**: Para cumplir esto, necesitas crear `Carrera`, `Materia` e `Inscripción`.
    *   🔨 Usa: [01-Tutorial_Carrera.md](../Guias_Implementacion/01-Tutorial_Carrera.md)
    *   🔨 Usa: [02-Tutorial_Materia.md](../Guias_Implementacion/02-Tutorial_Materia.md)
    *   🔨 Usa: [04-Tutorial_Inscripcion.md](../Guias_Implementacion/04-Tutorial_Inscripcion.md)
4.  **Cierre**: Muévela a **4. SF Desarrollo**.

#### 🏷️ Misión 2: Identidad del Alumno (HU-002)
1.  **Trello**: Busca **HU-002: Unicidad de Identidad**. -> Mueve a **En Progreso**.
2.  **Ejecución**: Configura el campo DNI como único en el objeto Alumno.
    *   🔨 Usa: [03-Tutorial_Alumno.md](../Guias_Implementacion/03-Tutorial_Alumno.md)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

#### 🏷️ Misión 3: Precisión de Notas (HU-003)
1.  **Trello**: Busca **HU-003: Integridad de Notas**. -> Mueve a **En Progreso**.
2.  **Ejecución**: Crea el campo `Nota__c` (Number 2,2) en Inscripción.
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

---

### 📅 DÍA 2: Identidad Visual (Branding)
*Que la app se sienta profesional.*

#### 🏷️ Misión 4: Tu Propio Dominio (HU-004)
1.  **Trello**: Mueve **HU-004: Dominio Institucional** a **En Progreso**.
2.  **Ejecución**: Configura My Domain (`lumina-tech.my.salesforce...`).
    *   🔨 Usa: [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md) (Sección Dominio)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

#### 🏷️ Misión 5: Colores y Logo (HU-005)
1.  **Trello**: Mueve **HU-005: Look & Feel** a **En Progreso**.
2.  **Ejecución**: Sube el logo y activa el Theme corporativo.
    *   🔨 Usa: [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md) (Sección Temas)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

#### 🏷️ Misión 6: La App Central (HU-006)
1.  **Trello**: Mueve **HU-006: App Central** a **En Progreso**.
2.  **Ejecución**: Crea la Lightning App "Gestión Académica" con sus Tabs.
    *   🔨 Usa: [07-Tutorial_App_Builder.md](../Guias_Implementacion/07-Tutorial_App_Builder.md) (Sección App)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

---

### 📅 DÍA 3: Calidad de Datos (Reglas)
*Evitar basura en la base de datos.*

#### 🏷️ Misión 7: Email Limpio (HU-007)
1.  **Trello**: Mueve **HU-007: Validación de Email** a **En Progreso**.
2.  **Ejecución**: Aplica la Regex en el campo Email.
    *   🔨 Usa: [05-Tutorial_Validaciones.md](../Guias_Implementacion/05-Tutorial_Validaciones.md)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

#### 🏷️ Misión 8: Notas Lógicas (HU-008)
1.  **Trello**: Mueve **HU-008: Lógica de Notas** a **En Progreso**.
2.  **Ejecución**: Validation Rule `Nota >= 0 && Nota <= 10`.
    *   🔨 Usa: [05-Tutorial_Validaciones.md](../Guias_Implementacion/05-Tutorial_Validaciones.md)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

---

### 📅 DÍA 4: Seguridad (Zero Trust)
*Protege la información.*

#### 🏷️ Misión 9: Privacidad por Defecto (HU-009)
1.  **Trello**: Mueve **HU-009: Matriz de Privacidad** a **En Progreso**.
2.  **Ejecución**: Configura OWD de Alumno a "Private".
    *   🔨 Usa: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

#### 🏷️ Misión 10: Doble Factor (HU-010)
1.  **Trello**: Mueve **HU-010: Acceso MFA** a **En Progreso**.
2.  **Ejecución**: Crea Permission Set para MFA.
    *   🔨 Usa: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

#### 🏷️ Misión 11: Segregación (HU-011)
1.  **Trello**: Mueve **HU-011: Segregación de Perfiles** a **En Progreso**.
2.  **Ejecución**: Configura Perfiles (Bedelía vs Profesor).
    *   🔨 Usa: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md)
3.  **Cierre**: Mueve a **4. SF Desarrollo**.

---

> **¡Felicidades!** Has completado las 11 misiones del Sprint 1. Tu trabajo aquí ha terminado.

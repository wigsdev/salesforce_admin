# ♾️ Manual de Ejecución: DevOps Specialist

**Tu Misión**: Eres el Mecánico. Preparas el terreno (Datos y Ambientes) para que los pilotos (Admin y QA) puedan volar sin estrellarse.
**Territorio**: Data Loader, Schema Builder y Sandboxes.

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Bloqueo** | QA necesita probar, pero el sistema está vacío (sin alumnos). |
| 💿 **DATA** | **Tu Turno** | Inyectas datos masivos (Seed Data) para simular realidad. |
| 🗺️ **AUDIT** | **Mantenimiento** | Verificas que la BD no tenga objetos basura o huérfanos. |

---

## 📅 CRONOGRAMA DE OPERACIONES (Sprint 1)

### 📅 DÍA 0: Preparación del Hangar
*Antes de que empiece el desarrollo.*

1.  **Sanidad de Ambientes**
    *   **Acción**: Verifica acceso a DEV y QA Sandboxes.
    *   **Health Check**: Confirma que el `Company Information` tenga las licencias disponibles.

---

### 📅 DÍA 1: Inyección de Datos (Data Seeding)
*Admin ha creado los objetos, pero están vacíos.*

#### 💿 Misión: Carga Masiva de Alumnos
*   **Contexto**: QA necesita 50 alumnos para probar filtros y reportes.
*   **Ejecución**:
    1.  Prepara el CSV `Student_Load_v1.csv` con columnas: `First Name`, `Last Name`, `National ID`, `Email`.
    2.  Ejecuta **Data Import Wizard**.
    3.  **Validación**: Verifica que los 8 dígitos del DNI respeten la regla del Admin.
    *   🔨 Usa: [08-Tutorial_Carga_Datos.md](../Guias_Implementacion/08-Tutorial_Carga_Datos.md)

---

### 📅 DÍA 2: Soporte a Branding
*El Admin despliega My Domain.*

#### 🔄 Misión: Verificación de DNS
*   **Acción**: Verifica que la URL `lumina-university.my.salesforce.com` resuelva correctamente desde fuera de la red (simulando acceso público).

---

### 📅 DÍA 3: Calidad de Datos (Smoke Test)
*Admin implementó reglas de validación.*

#### 🧪 Misión: Prueba de Estrés de Datos
*   **Acción**: Intenta cargar un CSV con datos sucios (Emails sin @, Notas > 10).
*   **Resultado Esperado**: El Data Loader debe devolver `FAILED` para esas filas.
*   **Reporte**: Entrega el archivo de errores al Admin como evidencia de que sus reglas funcionan.

---

### 📅 DÍA 4: Auditoría de Arquitectura
*El Sprint termina. ¿Qué basura quedó?*

#### 🗺️ Misión: Limpieza de Esquema
*   **Contexto**: A veces se crean campos de prueba que luego se borran pero quedan "soft deleted".
*   **Ejecución**:
    1.  Entra al **Schema Builder**.
    2.  Visualiza `Student`, `Subject`, `Enrollment`.
    3.  **Audit**: Confirma que las relaciones sean Master-Detail (Líneas rojas) y no Lookup (Líneas azules).
    4.  **Limpieza**: Identifica campos no usados o desconectados.
    *   🔨 Usa: [09-Tutorial_Schema_Builder.md](../Guias_Implementacion/09-Tutorial_Schema_Builder.md)

---

## 🚀 Despliegue (Deployment Strategy)

Cuando el QA apruebe todo, tu trabajo es moverlo a Producción.

1.  **Change Set**: Crea un Change Set saliente en DEV.
2.  **Add Components**:
    *   Custom Objects: `Student`, `Subject`, `Career`, `Enrollment`.
    *   Profiles: `Lumina Professor`, `Lumina Registrar`.
    *   Permission Set: `Lumina_MFA_Access`.
    *   Apps: `Lumina_Academic`.
3.  **Upload & Deploy**: Sube a PROD y valida.

---

## 📚 Recursos Relacionados
- 📘 **Tutorial de Rol**: [09-Rol_DevOps_Specialist.md](../Tutoriales_por_Rol/09-Rol_DevOps_Specialist.md)
- 📘 **Guía Data Loader**: [08-Tutorial_Carga_Datos.md](../Guias_Implementacion/08-Tutorial_Carga_Datos.md)
- 📘 **Guía Schema**: [09-Tutorial_Schema_Builder.md](../Guias_Implementacion/09-Tutorial_Schema_Builder.md)
- 📊 **Diagrama ERD**: [DIAGRAMA_ERD.md](../DIAGRAMA_ERD.md)

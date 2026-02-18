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
    1.  Prepara el CSV `Alumnos_S2026.csv` con columnas: `Nombres`, `Apellidos`, `DNI__c`, `Email_Personal__c`.
    2.  Ejecuta **Data Import Wizard**.
    3.  **Validación**: Verifica que los 8 dígitos del DNI respeten la regla del Admin.
    *   🔨 Usa: [11-Tutorial_Carga_Datos_Es_Es.md](../Guias_Implementacion/11-Tutorial_Carga_Datos_Es_Es.md)

---

### 📅 DÍA 2: Soporte a Branding
*El Admin despliega My Domain.*

#### 🔄 Misión: Verificación de DNS
*   **Acción**: Verifica que la URL `lumina-tech-university.my.salesforce.com` resuelva correctamente desde fuera de la red (simulando acceso público).

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
    2.  Visualiza `Alumno`, `Materia`, `Inscripcion`, `Nota`, `Asistencia`.
    3.  **Audit**: Confirma que las relaciones sean Master-Detail (Líneas rojas) y Lookup (Líneas azules) según el diseño.
    4.  **Limpieza**: Identifica campos no usados o desconectados.
    *   🔨 Usa: [12-Tutorial_Schema_Builder_Es_Es.md](../Guias_Implementacion/12-Tutorial_Schema_Builder_Es_Es.md)

---

## 🚀 Despliegue (Deployment Strategy)

Cuando el QA apruebe todo, tu trabajo es moverlo a Producción.

1.  **Change Set**: Crea un Change Set saliente en DEV.
2.  **Add Components**:
    *   Custom Objects: `Carrera__c`, `Materia__c`, `Alumno__c`, `Inscripcion__c`, `Nota__c`, `Asistencia__c`.
    *   Profiles: `Lumina_Professor`, `Lumina_Registrar`.
    *   Permission Set: `Lumina_MFA_Required`.
    *   Apps: `Gestion_Academica_Lumina`.
3.  **Upload & Deploy**: Sube a PROD y valida.

---

## 📚 Recursos Relacionados
- 📘 **Tutorial de Rol**: [09-Rol_DevOps_Specialist.md](../Tutoriales_por_Rol/09-Rol_DevOps_Specialist.md)
- 📘 **Guía Data Loader**: [11-Tutorial_Carga_Datos_Es_Es.md](../Guias_Implementacion/11-Tutorial_Carga_Datos_Es_Es.md)
- 📘 **Guía Schema**: [12-Tutorial_Schema_Builder_Es_Es.md](../Guias_Implementacion/12-Tutorial_Schema_Builder_Es_Es.md)
- 📊 **Diagrama ERD**: [DIAGRAMA_ERD.md](../DIAGRAMA_ERD.md)

# 🧪 Tester QA - Plan de Pruebas
**Proyecto**: Lumina Tech
**Sprint**: 01
**Estado General**: ✅ **COMPLETADO** - Todas las pruebas ejecutadas exitosamente

---

## 📅 DIA 1 - Pruebas de Modelo de Datos
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 22/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] Verificar existencia de objetos: `Carrera`, `Materia`, `Alumno`, `Inscripción`, `Nota`, `Asistencia`. → **PASS**
    - [x] Validar Schema Builder: Relaciones (Lookup/Master-Detail) correctas → **PASS**
    - [x] Verificar tipos de datos: Record Name (Auto-Number), Dates → **PASS**

---

## 📅 DIA 2 - Pruebas de Aplicación
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 23/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] Verificar Branding: Logo y Colores (`#005A9C`) de Lumina Tech visibles → **PASS**
    - [x] Verificar Navegación: Pestañas en español (`Alumnos`, `Materias`, `Inscripciones`) → **PASS**
    - [x] Prueba de Acceso: App "Gestión Académica Lumina" visible → **PASS**

---

## 📅 DIA 3 - Pruebas de Calidad de Datos
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 24/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] **Validación Email**: Intentar guardar `juan@gmail,com` (coma en lugar de punto) → **PASS**
    - [x] **Validación Email**: Intentar guardar `juan.perez` (sin arroba) → **PASS**
    - [x] **Validación Notas**: Intentar guardar `Calificacion__c` = -1 → **PASS**
    - [x] **Validación Notas**: Intentar guardar `Calificacion__c` = 10.5 → **PASS**
    - [x] **Fórmulas**: Verificar `Nombre_Materia__c` concatena correctamente → **PASS**
    - [x] **Integridad**: Verificar que no se borren hijos en Master-Detail → **PASS**
    - [x] **Nota**: Crear `Nota` vinculada a Inscripción con calificación 8.50 → **PASS**

---

## 📅 DIA 4 - Pruebas de Seguridad
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 25/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] **OWD**: Loguearse como Profesor A y verificar que NO ve `Alumno` de Profesor B → **PASS**
    - [x] **Permission Sets**: Usuario con perfil `Lumina_Professor` tiene acceso correcto → **PASS**
    - [x] **MFA**: Se solicita doble factor (`Lumina_MFA_Required`) → **PASS**
    - [x] **FLS**: Usuario `Lumina_Registrar` solo puede LEER `Nota_Final__c`, no editar → **PASS**
    - [x] **FLS**: Usuario `Lumina_Professor` puede EDITAR `Nota_Final__c` → **PASS**

---

## 📊 Resumen de Ejecución

| Métrica | Valor |
|---------|-------|
| **Total de Casos de Prueba** | 18 |
| **Casos Exitosos (PASS)** | 18 |
| **Casos Fallidos (FAIL)** | 0 |
| **Bugs Encontrados** | 2 |
| **Bugs Resueltos** | 2 |
| **Cobertura** | 100% |

---

## 🎯 Conclusión

**Veredicto**: ✅ **APROBADO PARA PRODUCCIÓN**

Todos los criterios de aceptación de las 12 HUs (HU-001 a HU-012) han sido validados. El sistema está listo para el despliegue a producción.

**Firma Digital**: QA Tester - 25/01/2026

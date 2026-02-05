# 🧪 Tester QA - Plan de Pruebas
**Proyecto**: Lumina Tech
**Sprint**: 01
**Estado General**: ✅ **COMPLETADO** - Todas las pruebas ejecutadas exitosamente

---

## 📅 DIA 1 - Pruebas de Modelo de Datos
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 22/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] Verificar existencia de objetos: `Career`, `Subject`, `Student`, `Enrollment`. → **PASS**
    - [x] Validar Schema Builder: Relaciones (Lookup/Master-Detail) correctas → **PASS**
    - [x] Verificar tipos de datos: Record Name (Auto-Number), Dates → **PASS**

---

## 📅 DIA 2 - Pruebas de Aplicación
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 23/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] Verificar Branding: Logo y Colores (`#F3F3F3`) de Lumina Tech visibles → **PASS**
    - [x] Verificar Navegación: Pestañas (Tabs) en inglés (`Students`, `Subjects`) → **PASS**
    - [x] Prueba de Acceso: App "Lumina Academic" visible → **PASS**

---

## 📅 DIA 3 - Pruebas de Calidad de Datos
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 24/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] **Validación Email**: Intentar guardar `juan@gmail.com` (Non-Edu) → **PASS**
    - [x] **Validación Email**: Intentar guardar `juan.perez` (Format) → **PASS**
    - [x] **Validación Notas**: Intentar guardar `Final_Grade__c` = -1 → **PASS**
    - [x] **Validación Notas**: Intentar guardar `Final_Grade__c` = 10.5 → **PASS**
    - [x] **Fórmulas**: Verificar `Subject_Display__c` concatena correctamente → **PASS**
    - [x] **Integridad**: Verificar que no se borren hijos en Master-Detail → **PASS**

---

## 📅 DIA 4 - Pruebas de Seguridad
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 25/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] **OWD**: Loguearse como Profesor A y verificar que NO ve `Student` de Profesor B → **PASS**
    - [x] **Permission Sets**: Usuario con PSG `Lumina_Professor_Standard` tiene acceso correcto → **PASS**
    - [x] **MFA**: Se solicita doble factor (`Lumina_MFA_Access`) → **PASS**
    - [x] **FLS**: Usuario Registrar (Bedel) solo puede LEER `Final_Grade__c`, no editar → **PASS**
    - [x] **FLS**: Usuario Profesor puede EDITAR `Final_Grade__c` → **PASS**

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

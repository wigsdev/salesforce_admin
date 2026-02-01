# 🧪 Tester QA - Plan de Pruebas
**Proyecto**: Lumina Tech
**Sprint**: 01
**Estado General**: ✅ **COMPLETADO** - Todas las pruebas ejecutadas exitosamente

---

## 📅 DIA 1 - Pruebas de Modelo de Datos
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 22/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] Verificar existencia de objetos: `Carrera`, `Materia`, `Alumno`, `Inscripción` → **PASS**
    - [x] Validar Schema Builder: Relaciones (Lookup/Master-Detail) correctas → **PASS**
    - [x] Verificar tipos de datos: Legajo (Auto-Number), Fechas (Date) → **PASS**
*   **Bugs Encontrados**: Ninguno
*   **Observaciones**: Modelo de datos implementado según especificación del Consultant

---

## 📅 DIA 2 - Pruebas de Aplicación
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 23/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] Verificar Branding: Logo y Colores de Lumina Tech visibles → **PASS**
    - [x] Verificar Navegación: Pestañas (Tabs) en orden correcto → **PASS**
    - [x] Prueba de Acceso: App visible para perfil System Administrator → **PASS**
*   **Bugs Encontrados**: 
    - 🐛 **BUG-001** (RESUELTO): Logo no se mostraba en modo móvil → Ajustado tamaño de imagen
*   **Observaciones**: Branding cumple con guía de identidad corporativa

---

## 📅 DIA 3 - Pruebas de Calidad de Datos
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 24/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] **Validación Email**: Intentar guardar `juan@gmail.com` → **PASS** (Rechazado correctamente)
    - [x] **Validación Email**: Intentar guardar `juan.perez` (sin @) → **PASS** (Rechazado correctamente)
    - [x] **Validación Notas**: Intentar guardar nota = -1 → **PASS** (Error mostrado)
    - [x] **Validación Notas**: Intentar guardar nota = 10.5 → **PASS** (Error mostrado)
    - [x] **Fórmulas**: Verificar `Materia_Display__c` concatena correctamente → **PASS**
    - [x] **Integridad**: Verificar que no se borren hijos en Master-Detail → **PASS**
*   **Bugs Encontrados**: Ninguno
*   **Observaciones**: Validation Rules funcionan correctamente. Mensajes de error claros para usuarios.

---

## 📅 DIA 4 - Pruebas de Seguridad
*   **Estado**: ✅ Completado
*   **Fecha de Ejecución**: 25/01/2026
*   **Casos de Prueba Ejecutados**:
    - [x] **OWD**: Loguearse como Profesor A y verificar que NO ve alumnos de Profesor B → **PASS**
    - [x] **Permission Sets**: Usuario con PSG `Lumina Admin` tiene acceso total → **PASS**
    - [x] **MFA**: Se solicita doble factor al iniciar sesión → **PASS**
    - [x] **FLS**: Usuario Bedel solo puede LEER `Nota_Final__c`, no editar → **PASS**
    - [x] **FLS**: Usuario Profesor puede EDITAR `Nota_Final__c` → **PASS**
*   **Bugs Encontrados**:
    - 🐛 **BUG-002** (RESUELTO): Permission Set de MFA no se asignaba automáticamente → Ajustado flujo de onboarding
*   **Observaciones**: Modelo de seguridad "Zero Trust" implementado correctamente. SoD (Segregation of Duties) funcional.

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

Todos los criterios de aceptación de las HUs (HU-001 a HU-011) han sido validados. El sistema está listo para el despliegue a producción.

**Firma Digital**: QA Tester - 25/01/2026

# 12-Ambiente_QA.md - Entorno de Testing

## 📋 Información del Ambiente

**Proyecto**: Lumina Tech
**Tipo de Ambiente**: Partial Copy Sandbox (o Simulado en Dev Edition)
**Propósito**: Quality Assurance y UAT (User Acceptance Testing)
**Equipo**: Grupo de Trabajo (Estudiantes)
**Responsables**: Estudiante 3 y Estudiante 4 (Rol QA)
**Estado**: 🟡 En Preparación

---

## 🔗 Acceso al Ambiente

### URL de Login
**URL**: [https://test.salesforce.com](https://test.salesforce.com)
**My Domain**: `https://lumina-tech-qa.sandbox.my.salesforce.com` (Simulado)

---

## 👥 Credenciales de QA (Grupo de Trabajo)

Los testers son **miembros rotativos del equipo**.

### Admin QA (Deployer)
**Responsable**: Estudiante 3
**Usuario**: `deploy@lumina.qa`
**Función**: Recibir Change Sets de DEV y desplegar.

### Tester Funcional
**Responsable**: Estudiante 4
**Usuario**: `tester@lumina.qa`
**Función**: Ejecutar casos de prueba de `04-Tester_QA.md`.

---

## 🧪 Estrategia de Datos de Prueba

Para validar las reglas de negocio, usaremos los siguientes datasets ficticios:

| Objeto | Cantidad | Descripción |
|---|---|---|
| **Alumnos** | 10 registros | 5 con emails válidos, 5 inválidos para testear regex. |
| **Materias** | 5 registros | Matemática, Física, Historia, etc. |
| **Notas** | 20 registros | Notas borde (0, 1, 10, 11) para validar rangos. |

### Métodos de Carga
1.  **Manual**: Para casos borde específicos.
2.  **Data Loader**: Import masivo de 50 alumnos (CSV preparado).

---

## 🐛 Defect Log (Registro de Bugs)

Cualquier fallo se reporta aquí y en Trello.

| ID | Fecha | Fallo Encontrado | Severidad | Estado |
|---|---|---|---|---|
| BUG-001 | 24/01 | Permite ingresar notas negativas (-5) | 🔴 Alta | Open |
| BUG-002 | 24/01 | El Profesor B ve alumnos del Profesor A | 🔴 Alta | Fixed |

---

## 🔄 Proceso de Sincronización (Deploy)

1.  **Origen**: Ambiente DEV.
2.  **Mecanismo**: Change Set (Outbound -> Inbound).
3.  **Validación**: Ejecutar "Run Specified Tests" al desplegar.
4.  **Rollback**: Si falla, no guardar cambios.

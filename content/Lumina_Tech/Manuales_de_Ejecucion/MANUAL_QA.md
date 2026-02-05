# 🧪 Manual de Ejecución: QA Tester

**Tu Misión**: Romper cosas. Eres el Guardián de la Calidad. Nada pasa a Producción si tú no das el OK.
**Herramientas**: `HISTORIAS_DE_USUARIO.md` (Tu Biblia) y Sandbox (Tu Patio de Juegos).

---

## 🚦 Tus Banderas (Reglas de Juego)

| Bandera | Significado | Acción |
| :--- | :--- | :--- |
| 🛑 **PRE-REQ** | **Bloqueo** | El Admin dice "Terminado" (Columna 4). Tú dices "Vamos a ver". |
| 💥 **TEST** | **Tu Turno** | Ejecutas los **QA Checks** definidos en la Historia de Usuario. |
| 👋 **HANDOFF** | **Salida** | Apruebas (Pasa a Done) o Rechazas (Vuelve a In Progress). |

---

## 📅 ESTRATEGIA DE PRUEBAS (Sprint 1)

Tu trabajo no es adivinar. Tienes un guion estricto.

### 1. El Checklist de Oro (Backlog)
Para cada HU, consulta la sección **✅ Criterios de Aceptación (QA Check)** en `HISTORIAS_DE_USUARIO.md`.

*   **Ejemplo (HU-002 - Identidad)**:
    *   [ ] ¿Se generó el ID automático?
    *   [ ] ¿El sistema explotó cuando metí un DNI duplicado? (Debe explotar).
    *   [ ] ¿El sistema rechazó mi DNI de 7 dígitos con un mensaje claro?

### 2. Pruebas de Seguridad (Personas)
No pruebes todo como "Admin". Usa los usuarios ficticios.
*   🔨 Referencia: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md) (Parte 6: Estrategia de Testing).

| Actor | Rol | Prueba Clave |
| :--- | :--- | :--- |
| **Severus S.** | Profesor | Intentar ver materias de otros. (Debe fallar). |
| **Dolores U.** | Registrar | Intentar cambiar una nota final. (Debe fallar). |
| **Alumno Fake** | Estudiante | Intentar ver datos de otro alumno. (Debe fallar). |

---

## 🐛 Cómo Reportar Bugs (Bug Tracking)

Si encuentras un error, no digas "no anda". Sé profesional.

**Plantilla de Bug:**
> **Título**: [HU-008] Permite ingresar notas negativas (-5)
> **Pasos para reproducir**:
> 1. Loguearse como Profesor.
> 2. Ir al alumno X.
> 3. En la nota, poner "-5".
> 4. Guardar.
> **Resultado Esperado**: Error "Invalid Grade".
> **Resultado Obtenido**: Se guardó con éxito.
> **Severidad**: Alta.

---

## 📅 RUTINA DIARIA

### Días 1-2: Pruebas Funcionales (Caja Negra)
*   Verifica que los objetos existan.
*   Crea registros de prueba manualmente.
*   Valida los "Required Fields".

### Días 3-4: Pruebas de Reglas y Seguridad
*   **Data Quality**: Intenta ensuciar la base de datos (emails falsos, DNIs letras).
*   **Security**: Logueate como Severus y Dolores. Intenta violar la privacidad.

---

## 📚 Recursos Relacionados
- 📘 **Backlog con QA Checks**: [HISTORIAS_DE_USUARIO.md](../Archivos_intermedios/HISTORIAS_DE_USUARIO.md)
- 📘 **Guía de Seguridad**: [06-Tutorial_Seguridad.md](../Guias_Implementacion/06-Tutorial_Seguridad.md)
- 📘 **Tutorial de Rol**: [03-Rol_QA_Tester.md](../Tutoriales_por_Rol/03-Rol_QA_Tester.md)

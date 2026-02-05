# 🦅 MANUAL MAESTRO: Centro de Comando Lumina Tech

**Bienvenido, Arquitecto.**
Este repositorio no es solo código; es una **Simulación de Agencia Salesforce**.
Para tener éxito, debes saber qué sombrero llevas puesto.

---

## 🚦 ¿Quién Eres Hoy? (Select your Player)

### 🧠 FASE 1: ESTRATEGIA (Planning)
*Define qué construir y por qué.*
1.  👔 **[PRODUCT OWNER (PO)](MANUAL_PO.md)**: "Priorizo el Valor". (Dueño del Backlog).
2.  🕵️ **[BUSINESS ANALYST (BA)](MANUAL_BA.md)**: "Escribo las Historias". (Dueño de los Requisitos).
3.  🏗️ **[CONSULTANT (ARCH)](MANUAL_CONSULTANT.md)**: "Diseño la Solución". (Dueño del Modelo de Datos).

### 🔨 FASE 2: CONSTRUCCIÓN (Build)
*Configura la plataforma.*
4.  🛡️ **[ADMINISTRATOR](MANUAL_ADMIN.md)**: "Hago los Clicks". (Constructor).
5.  ♾️ **[DEVOPS](MANUAL_DEVOPS.md)**: "Cargo los Datos". (Mecánico de Ambientes).

### 🧪 FASE 3: CALIDAD (Verify)
*Rompe la plataforma.*
6.  🧪 **[QA TESTER](MANUAL_QA.md)**: "Encuentro los Bugs". (Guardián de Calidad).
7.  👮‍♂️ **[TEAM LEAD (TL)](MANUAL_TL.md)**: "Reviso el Código". (Guardián Técnico).

### 🚀 FASE 4: DESPLIEGUE (Release)
*Llévalo al mundo real.*
8.  ⏱️ **[SCRUM MASTER](MANUAL_SCRUM.md)**: "Desbloqueo al Equipo". (Facilitador).
9.  🚀 **[RELEASE MANAGER](MANUAL_RELEASE.md)**: "Despliego a Producción". (Piloto de Salida).

---

## 🌊 El Flujo del Trello (The Pipeline)

Sigue la tarjeta de izquierda a derecha. **Nunca** saltes una columna.

| Paso | Columna | Dueño | Acción Clave |
| :--- | :--- | :--- | :--- |
| **1** | **Backlog** | PO/BA | Escribir la HU (As a... I want...). |
| **2** | **Sprint Backlog** | PO | Decidir: "Esto entra hoy". |
| **3** | **En Progreso** | Admin | Crear Objetos, Campos, Flows. |
| **4** | **SF Desarrollo** | Admin | Auto-Test básico. Mover a QA. |
| **5** | **SF QA** | QA | Ejecutar **Quick Scripts** (Backlog Check). |
| **6** | **Aprobación TL** | TL | Revisar Naming Conventions & Seguridad. |
| **7** | **SF Producción** | Release | Deploy (Change Set) & Pasos Manuales. |
| **8** | **Terminado** | Todos | ¡Celebrar! 🎉 |

---

## 💡 ¿Cómo usar estos manuales? (Simulación)

Este proyecto está diseñado para que **TÚ** rotes por los roles.
*   **Mañana (Día 1)**: Ponte la gorra de **Consultant** y diseña. Luego la de **Admin** y construye.
*   **Tarde (Día 1)**: Ponte la gorra de **DevOps** y carga datos. Luego la de **QA** y prueba lo que hiciste en la mañana.

**¡Buena suerte, equipo!** (O sea, tú).

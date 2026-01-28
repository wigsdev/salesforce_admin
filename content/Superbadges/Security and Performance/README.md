# Security and Performance Superbadge 🚀

**Estado**: ✅ COMPLETADO


Este directorio contiene todos los recursos necesarios para completar el Superbadge de **Security and Performance**. Este reto valida tu capacidad para optimizar el almacenamiento de datos, integrar sistemas externos y proteger información sensible.

## 📂 Contenido del Directorio

*   **[ENUNCIADO_ORIGINAL.md](ENUNCIADO_ORIGINAL.md)**: El escenario de negocio de "Flow and the Low Codes" (la banda de música) y los requisitos detallados.
*   **[GUIA_SB_SOLUCION.md](GUIA_SB_SOLUCION.md)**: Guía paso a paso para configurar Big Objects, External Objects y Encriptación.

---

## 🎯 Objetivos de Aprendizaje

Al completar este Superbadge, demostrarás competencia en:
1.  **Big Objects**: Manejar grandes volúmenes de datos (hasta millones de registros) sin sacrificar rendimiento.
2.  **External Objects**: Conectar Salesforce con APIs externas (OData) para ver datos sin importarlos ("Salesforce Connect").
3.  **Data Classification**: Clasificar campos sensibles (PII) por niveles de cumplimiento y confidencialidad.
4.  **Field Encryption**: Implementar Classic Encryption para datos críticos como números de identificación de fans.
5.  **Índices Personalizados**: Crear índices compuestos para optimizar consultas en Big Objects.

## 📝 Prerrequisitos (¡Muy Importante!)

Para este Superbadge **NO** puedes usar una Playground estándar. Debes registrarte en una **Developer Edition especial** con datos pre-cargados.

*   **Requisito**: Busca el enlace "Sign up for a free Developer Edition org with special configuration" en la página oficial del Superbadge en Trailhead.
*   **Nota**: Esta org incluye la configuración necesaria para el reto de External Services y los datos de muestra.

## 💡 Consejos Clave
*   **Big Objects & Índices**: El orden de los campos en el índice es CRÍTICO. Si te equivocas en el orden (`Song` > `Account` > `Play Date`), no podrás editarlo después; tendrás que borrar el objeto y empezar de nuevo. ¡Atención al detalle!
*   **External Data**: Asegúrate de desmarcar "Request Row Counts" al configurar la fuente de datos externa, o la validación fallará.
*   **PII & Confidencialidad**: No olvides clasificar TODOS los campos solicitados (`Email`, `Birthdate`, `Gender`, `Pronouns`) con el nivel de sensibilidad correcto.

---
*¡Optimiza y protege, Admin! Que la música no pare.* 🎸

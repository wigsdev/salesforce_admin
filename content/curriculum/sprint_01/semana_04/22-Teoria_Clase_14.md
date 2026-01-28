# Salesforce Admin + Agent Force

## Daily
*   Del 1 al 10 cómo te sentís?
*   Qué te proponés para hoy?

> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## Skills Técnicas (El "Qué" haces)

*   **Gestión de Usuarios y Seguridad**: El pan de cada día. Crear usuarios, resetear contraseñas, asignar Perfiles y Roles sin abrir brechas de seguridad.
*   **Gestión de Datos (Data Management)**: Limpieza, carga masiva (Data Loader/Import Wizard) y prevención de duplicados. Saber que "datos sucios = reportes inútiles".
*   **Automatización Básica (Flows)**: Capacidad de crear flujos sencillos (Record-Triggered) para reemplazar tareas manuales repetitivas.
*   **Reportes y Dashboards**: Crear visibilidad para los jefes. Saber traducir preguntas de negocio ("¿Cuánto vendimos?") en gráficos.
*   **AgentForce**: puedas familiarizarte con la configuración de agentes dentro de Salesforce.

> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## Skills Blandas (El "Cómo" lo haces)

*   **Comunicación Traducida**: Habilidad para hablar con un vendedor sin usar jerga técnica ("Objeto", "API"). Explicar el por qué, no solo el cómo.
*   **Resolución de Problemas (Google-Fu)**: No saberlo todo, pero saber cómo buscarlo. Diagnosticar errores antes de escalar.
*   **Mentalidad de Aprendiz (Learner's Mindset)**: Salesforce cambia 3 veces al año. La curiosidad vale más que la memoria.
*   **Atención al Detalle**: Probar antes de desplegar. Un pequeño error en un Flow puede detener a toda la empresa.

> Reemplazar imagen con foto propia seleccionando la forma y usando REEMPLAZAR IMAGEN

## Normas de Convivencia

*   **COLABORACIÓN**: Aprender con y de otras personas
*   **AUSENCIAS**: Seguir con la planilla y actividades
*   **MIC o CHAT**: Comunicación
*   **ERRORES**: Atrasados
*   **JUEVES**: PREGUNTAS (Al final de la clase Teórica)
*   **AUTONOMÍA**: Utilizar las herramientas

---

# GESTIÓN DE DATOS

Vamos a ver la segunda parte de modelado de datos…

## La Operación Maestra: UPSERT y los IDs

La Matching Rule es el escáner de rayos X. Dice: '¡Atención! Esta maleta se parece a esta otra'. Solo identifica.
La Duplicate Rule es el guardia de seguridad. El escáner avisa, pero el guardia decide: ¿Te dejo pasar con advertencia? ¿O te bloqueo la entrada y te mando a casa?

Ustedes configuran ambas cosas por separado. Primero definen la coincidencia, luego definen el castigo.

### La Red de Seguridad: Exportación y Backups

¿Qué hacemos si ya tenemos 1000 duplicados? No se borran uno por uno.
Usamos la herramienta de **Merge (Fusionar)**. Salesforce les permite tomar 3 registros duplicados y convertirlos en uno solo, eligiendo el mejor teléfono de uno, el mejor email del otro y conservando toda la historia (casos, ventas) de los tres.

> **Nunca eliminen un duplicado sin revisar qué información histórica tiene.**

---

## POSIBLES PREGUNTAS

**1. El pánico del "Undo"**
*   **Alumno**: "Profe, cargué 5,000 registros con Data Loader y me di cuenta de que mapeé mal el campo de Teléfono en el de Email. ¿Cómo hago 'Deshacer'?"
*   **Respuesta**: "No hay botón 'Deshacer'. Tienes que arreglarlo con otra carga.
    1.  Exporta los registros que acabas de crear (necesitas sus IDs).
    2.  Arregla el Excel.
    3.  Haz un 'Update' con los datos correctos.
    *   **Lección**: ¡Siempre prueba con 1 o 5 registros antes de cargar los 5,000!"

**2. Import Wizard y Oportunidades**
*   **Alumno**: "Estoy tratando de subir Oportunidades con el Import Wizard pero no encuentro el objeto en la lista. ¿Por qué?"
*   **Respuesta**: "¡Trampa clásica! El Data Import Wizard NO soporta el objeto Oportunidades (ni Casos, ni Productos). Aunque sea una carga pequeña, para Oportunidades estás obligado a usar el Data Loader".

**3. ¿Qué es un archivo CSV?**
*   **Alumno**: "Tengo mi base de datos en un Excel bonito con colores y fórmulas. ¿Lo subo así?"
*   **Respuesta**: "No. Salesforce solo lee CSV (Valores Separados por Comas). Debes hacer 'Guardar como' en Excel y elegir formato .csv. Los colores, negritas y fórmulas se perderán; solo importan los datos planos".

> **¿Ven esa barra verde arriba en las Oportunidades? Eso es el Path.**
> No es solo un dibujo. Ustedes pueden configurar que cuando el vendedor llegue a la etapa 'Negociación', aparezca un cartel que diga: 'Recuerda pedir el RUT de la empresa y no ofrecer más del 10% de descuento'.
> Es como tener al gerente de ventas susurrándole al oído al vendedor qué hacer en cada paso.

**4. IDs de 15 vs 18 caracteres**
*   **Alumno**: "Al exportar veo IDs que terminan distinto. Unos tienen 15 letras y otros 18. ¿Cuál uso?"
*   **Respuesta**: "El ID de 15 caracteres distingue mayúsculas de minúsculas (Case-sensitive). El ID de 18 caracteres NO distingue (Case-insensitive) y es el seguro para trabajar en Excel (porque Excel a veces confunde 'Id' con 'ID'). Tip: Data Loader siempre usa 18. En reportes, intenta usar 15 a menos que uses una fórmula para convertirlo".

**5. Validaciones vs. Carga de Datos**
*   **Alumno**: "Tengo una Regla de Validación que impide guardar contactos sin email. Si subo 100 contactos sin email por Data Loader, ¿se saltan la regla?"
*   **Respuesta**: "No. Las Reglas de Validación se ejecutan siempre, incluso en cargas masivas. Esos registros fallarán y Data Loader te generará un archivo de 'Errores' explicando por qué no entraron".

**6. El Link Caducado**
*   **Alumno**: "Me llegó el email del Data Export semanal el viernes, pero intenté bajarlo el lunes y el link no funciona."
*   **Respuesta**: "Los links de descarga del Data Export Service duran solo 48 horas por seguridad. Si no lo bajaste, perdiste ese backup y tendrás que esperar a la semana siguiente (o hacer uno manual)".

---

## ¡Manos a la obra!
Avanzamos con los trails.

### LEER CON ATENCIÓN
Las prácticas previas al challenge son importantes para entender el challenge. **NO DEJARLAS PASAR.**

### ATENCIÓN

#### ERRORES
1.  Agotar herramientas
2.  Consultar con su grupo
3.  Hacer una nueva ORG
4.  Recién consultar a los profesores

#### CONSULTAS
*   Haber agotado todas las instancias de herramientas

#### Contexto
*   SB-Jueves

#### PAIR PROGRAMING
*   Compartir pantalla
*   Hablar sobre el proceso del Trailhead
*   Ir rotando
*   No se puede estar en silencio
*   El trabajo individual es fuera de la cursada

---

### IMPORTAR DATA
[LINK](#)

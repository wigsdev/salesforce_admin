# Guía SB - Fórmulas

## Reto 1: Build Lead Score and Rating Fields (Puntuación de Candidatos)

El objetivo aquí es calificar automáticamente a los Leads para que ventas sepa a quién llamar primero.

### Paso 1: Crear el campo de Puntuación (Lead Score)

El negocio quiere una fórmula numérica que sume puntos si el Lead tiene ciertos datos completos.

**Objeto**: Lead (Candidato).  
**Tipo de Campo**: Fórmula (Número, 0 decimales).  
**Nombre API Sugerido**: `Lead_Score__c`

#### La Lógica (Pseudo-código):

Tienes que sumar bloques usando IF.

- Si tiene Teléfono (Phone) → Suma puntos.
- Si tiene Email (Email) → Suma puntos.
- Si tiene Título (Title) → Suma puntos.
- Si la Empresa (Company) no está vacía → Suma puntos.

**Tip**: Usa `NOT(ISBLANK(Campo))` para verificar si tiene datos. La fórmula se verá como una suma: `IF(Condicion1, 1, 0) + IF(Condicion2, 1, 0)...`

---

### Paso 2: Crear el campo de Clasificación Visual (Lead Rating)

Ahora quieren una imagen o texto que interprete ese número.

**Objeto**: Lead.  
**Tipo de Campo**: Fórmula (Texto).  
**Nombre API Sugerido**: `Lead_Rating__c` (o lo que pida la letra exacta).

#### La Lógica:

- Si el `Lead_Score__c` es alto (ej. >= 3) → Muestra imagen de "Hot" (Fuego/Verde).
- Si es medio → Muestra imagen "Warm" (Amarillo).
- Si es bajo → Muestra imagen "Cold" (Azul/Hielo).

**Tip**: Usa la función `IMAGE("/img/samples/flag_green.gif", "Hot")` dentro de una función CASE o IF anidados.

---

## Reto 2: Support Visibility and Decision-Making (Equipo de Servicio)

Aquí nos movemos al objeto Case (Caso). El objetivo es asegurar que los casos urgentes se traten correctamente y dar visibilidad visual.

### Paso 1: Validación de Integridad (Validation Rule)

El negocio quiere evitar que alguien marque un caso como "Escalado" si no tiene la información necesaria.

**Objeto**: Case.  
**Herramienta**: Validation Rule.  
**Escenario Típico**: No permitir que el Status cambie a "Escalated" si la Priority no es "High".

#### La Lógica del Error:

(Recuerda, definimos el error).

SI el Status es "Escalated" Y la Prioridad NO es "High" → ERROR.

**Tip**: Usa `AND(ISPICKVAL(Status, "Escalated"), NOT(ISPICKVAL(Priority, "High")))`.

---

### Paso 2: Semáforo de Antigüedad (Fórmula de Visibilidad)

Necesitan ver visualmente si un caso es crítico.

**Objeto**: Case.  
**Tipo de Campo**: Fórmula (Texto/Imagen).  
**Nombre**: Probablemente algo como `Case_Urgency__c` o `Traffic_Light__c`.

#### La Lógica:

- Si Priority es High Y el caso está abierto (`IsClosed = False`) → Muestra ROJO.
- Si es Medium → AMARILLO.
- Si es Low → VERDE.

**Tip**: Asegúrate de verificar que el caso no esté cerrado antes de mostrar la alerta roja, o el reporte se verá mal históricamente.

---

## Reto 3: Enhance Reporting with Business Logic (Reportes Avanzados)

Aquí no creas campos en el objeto, sino fórmulas dentro del Reporte.

### Paso 1: Ubicar el Reporte

- Ve a la pestaña Reports.
- Busca el reporte pre-creado llamado "Case Severity by Month Last Year" (o similar).
- Dale a Edit.

---

### Paso 2: Crear una Fórmula de Fila (Row-Level Formula)

Quieren saber cuánto tiempo tardó en cerrarse cada caso individualmente.

- En el constructor de reportes, busca la flecha en la columna de campos y elige "Add Row-Level Formula".
- **Nombre**: Days to Close.
- **Tipo**: Número.
- **Fórmula**: `CloseDate - CreatedDate` (Fecha de Cierre menos Fecha de Creación).

---

### Paso 3: Validar y Ejecutar

- Asegúrate de que el reporte esté filtrado correctamente (ej. solo casos cerrados, solo del año pasado).
- Guarda y Ejecuta (Save & Run).

---

**Grupo**: 3 - VISIONARY ADMINS  
**Última actualización**: 16 Enero 2026

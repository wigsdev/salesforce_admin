# 📋 Guía Paso a Paso: Trasladar Historias de Usuario a Trello

Esta guía te llevará desde cero hasta tener un tablero de Trello completamente configurado con las 3 Historias de Usuario de Financiera Horizonte S.A.

---

## 🎯 Objetivo

Al finalizar esta guía tendrás:
- ✅ Un tablero de Trello configurado con columnas Agile
- ✅ 3 tarjetas (HU-001, HU-002, HU-003) con toda la información
- ✅ Etiquetas de Épicas y Story Points asignados
- ✅ Criterios de aceptación como checklist

**Tiempo estimado**: 20-30 minutos

---

## 📝 PARTE 1: Crear y Configurar el Tablero

### Paso 1.1: Crear cuenta en Trello (si no tienes)

1. Ve a [https://trello.com](https://trello.com)
2. Haz clic en **"Registrarse"**
3. Usa tu email o cuenta de Google
4. Verifica tu email

### Paso 1.2: Crear el tablero

1. En la página principal de Trello, haz clic en **"Crear nuevo tablero"**
2. **Nombre del tablero**: `Financiera Horizonte S.A. - Sprint 1`
3. **Fondo**: Elige el color azul o una imagen profesional
4. **Visibilidad**: Selecciona **"Equipo"** o **"Público"** (para compartir con mentores)
5. Haz clic en **"Crear"**

### Paso 1.3: Configurar columnas (Listas)

Elimina las listas por defecto y crea estas 8 columnas en orden:

1. **Backlog** (Historias de Usuario)
2. **Sprint Backlog** (Por Hacer)
3. **En Progreso**
4. **SF Desarrollo**
5. **SF QA**
6. **Aprobación TL**
7. **SF Producción**
8. **Terminado**

**Cómo crear una lista**:
- Haz clic en **"+ Añadir otra lista"**
- Escribe el nombre
- Presiona Enter

---

## 🏷️ PARTE 2: Crear Etiquetas (Épicas y Prioridades)

### Paso 2.1: Configurar Épicas

1. Haz clic en **"Mostrar menú"** (esquina superior derecha)
2. Selecciona **"Etiquetas"**
3. Crea las siguientes etiquetas:

| Color | Nombre | Uso |
|-------|--------|-----|
| 🔵 Azul | Gestión de Clientes | Para HU-001 |
| 🔴 Rojo | Seguridad y Permisos | Para HU-002 |
| 🟢 Verde | Automatización de Procesos | Para HU-003 |

### Paso 2.2: Configurar Prioridades (Opcional)

| Color | Nombre |
|-------|--------|
| 🟠 Naranja | Prioridad: Alta |
| 🟡 Amarillo | Prioridad: Media |
| ⚫ Negro | Prioridad: Crítica |

---

## 📌 PARTE 3: Crear las Tarjetas (Historias de Usuario)

### 🔵 HU-001: Gestión de Garantes en Préstamos

#### Paso 3.1: Crear la tarjeta

1. En la columna **"Backlog"**, haz clic en **"+ Añadir una tarjeta"**
2. **Título**: `(5) HU-001 - Gestión de Garantes en Préstamos`
   - El `(5)` representa los Story Points
3. Presiona Enter para crear la tarjeta
4. Haz clic en la tarjeta para abrirla

#### Paso 3.2: Completar la descripción

En el campo **"Descripción"**, copia y pega:

```
**Como**: Ejecutivo de Créditos
**Quiero**: Registrar múltiples garantes asociados a un préstamo con sus datos completos
**Para**: Poder contactarlos cuando sea necesario y tener trazabilidad de quiénes respaldan cada crédito

---

## 🔧 Solución Técnica

**Objeto**: Opportunity (Oportunidad = Préstamo)
**Funcionalidad**: Contact Roles (Roles de Contacto)

### Configuración:
- Usar Contact Roles nativo de Salesforce
- Agregar valor "Garante" al picklist de roles
- Crear Page Layout personalizado para mostrar Contact Roles

---

## 📊 Notas Adicionales

**Alternativa Custom**: Objeto Junction `Loan_Contact__c` si se necesita más flexibilidad
**Campos adicionales**: Role, Guarantee_Percentage
```

#### Paso 3.3: Agregar Checklist (Criterios de Aceptación)

1. Haz clic en **"Checklist"** en el menú lateral
2. **Nombre**: `Criterios de Aceptación`
3. Agrega estos ítems uno por uno:

```
☐ Puedo agregar uno o más garantes a una oportunidad de préstamo
☐ Cada garante tiene su ficha de contacto completa (teléfono, email, dirección)
☐ Puedo diferenciar visualmente quién es el cliente principal y quién es garante
☐ Los garantes aparecen en la vista de la oportunidad sin necesidad de buscarlos
☐ Puedo generar reportes de "Préstamos con Garantes" vs "Préstamos sin Garantes"
```

#### Paso 3.4: Asignar etiquetas

1. Haz clic en **"Etiquetas"**
2. Selecciona: 🔵 **Gestión de Clientes**
3. Selecciona: 🟠 **Prioridad: Alta**

#### Paso 3.5: Agregar fecha de vencimiento (opcional)

1. Haz clic en **"Fechas"**
2. Selecciona la fecha de fin del Sprint 1
3. Marca **"Recordatorio"** si deseas notificaciones

---

### 🔴 HU-002: Restricción de Acceso a Datos Financieros Sensibles

#### Paso 3.6: Crear la tarjeta

1. En **"Backlog"**, añade nueva tarjeta
2. **Título**: `(3) HU-002 - Restricción de Acceso a Datos Financieros`

#### Paso 3.7: Completar la descripción

```
**Como**: Gerente de Finanzas
**Quiero**: Que solo los vendedores y gerentes puedan ver el salario de los clientes
**Para**: Proteger la privacidad de la información financiera y cumplir con políticas de seguridad

---

## 🔧 Solución Técnica

**Funcionalidad**: Field-Level Security (FLS)
**Objeto**: Contact
**Campo**: Monthly_Salary__c

### Configuración:
1. Setup → Object Manager → Contact → Fields → Monthly_Salary__c
2. Configurar FLS por perfil:
   - ✅ Visible: "Ejecutivo de Créditos", "Gerente de Finanzas"
   - ❌ No Visible: "Atención al Cliente"
3. Crear Permission Set "Financial_Data_Access"

---

## ⚠️ Validación

- Probar con usuarios de diferentes perfiles
- Verificar que reportes respeten FLS
```

#### Paso 3.8: Agregar Checklist

**Nombre**: `Criterios de Aceptación`

```
☐ El perfil "Atención al Cliente" NO puede ver el campo Monthly_Salary__c
☐ El perfil "Ejecutivo de Créditos" SÍ puede ver y editar el campo
☐ El perfil "Gerente de Finanzas" SÍ puede ver y editar el campo
☐ Los usuarios de Atención al Cliente no ven el campo en reportes ni vistas
☐ Se documenta qué perfiles tienen acceso a datos financieros
```

#### Paso 3.9: Asignar etiquetas

- 🔴 **Seguridad y Permisos**
- ⚫ **Prioridad: Crítica**

---

### 🟢 HU-003: Gestión de Múltiples Cuentas Bancarias

#### Paso 3.10: Crear la tarjeta

1. En **"Backlog"**, añade nueva tarjeta
2. **Título**: `(8) HU-003 - Gestión de Múltiples Cuentas Bancarias`

#### Paso 3.11: Completar la descripción

```
**Como**: Analista de Desembolsos
**Quiero**: Registrar todas las cuentas bancarias de un cliente y marcar cuál es la activa
**Para**: Tener historial completo de cuentas y saber a cuál transferir sin perder información

---

## 🔧 Solución Técnica

**Objeto Custom**: Bank_Account__c (Cuenta Bancaria)
**Relación**: Master-Detail con Contact

### Campos del objeto:
- Contact__c (Master-Detail)
- Bank_Name__c (Picklist) - Banco
- Account_Number__c (Text Encrypted) - Número de cuenta
- CBU__c (Text 22) - Clave Bancaria Uniforme
- Account_Type__c (Picklist) - "Caja de Ahorro", "Cuenta Corriente"
- Is_Primary__c (Checkbox) - Cuenta preferida
- Status__c (Picklist) - "Activa", "Inactiva", "Cerrada"

### Validation Rule:
Solo una cuenta puede estar marcada como Is_Primary__c = TRUE por contacto

### Flow:
Auto-desmarcar cuentas anteriores al marcar nueva como primaria
```

#### Paso 3.12: Agregar Checklist

**Nombre**: `Criterios de Aceptación`

```
☐ Puedo agregar múltiples cuentas bancarias a un cliente
☐ Cada cuenta tiene: Banco, CBU, Tipo de cuenta, Estado
☐ Solo UNA cuenta puede estar marcada como "Preferida" a la vez
☐ Puedo ver el historial completo de cuentas (activas e inactivas)
☐ Al marcar nueva cuenta como preferida, la anterior se desmarca automáticamente
☐ Puedo generar reportes de "Clientes con múltiples cuentas"
☐ El CBU está encriptado por seguridad
```

#### Paso 3.13: Asignar etiquetas

- 🟢 **Automatización de Procesos**
- 🟠 **Prioridad: Alta**

---

## 🎨 PARTE 4: Personalización Avanzada (Opcional)

### Opción A: Activar Power-Up "Custom Fields"

1. Menú → **"Power-Ups"**
2. Busca **"Custom Fields"**
3. Activa el Power-Up
4. Crea un campo personalizado **"Story Points"** (Número)
5. Asigna valores: 5, 3, 8 a cada tarjeta

### Opción B: Usar descripción corta

1. Abre cada tarjeta
2. Haz clic en el ícono de lápiz junto al título
3. En **"Descripción corta"** escribe:
   - HU-001: `Épica: Gestión de Clientes | SP: 5`
   - HU-002: `Épica: Seguridad | SP: 3`
   - HU-003: `Épica: Automatización | SP: 8`

### Opción C: Agregar miembros del equipo

1. Haz clic en **"Miembros"** en cada tarjeta
2. Asigna responsables según roles:
   - **HU-001**: Administrador Salesforce
   - **HU-002**: Administrador + Arquitecto
   - **HU-003**: Desarrollador Salesforce

---

## 📊 PARTE 5: Organizar el Sprint

### Paso 5.1: Mover tarjetas a Sprint Backlog

Para simular el inicio del Sprint 1:

1. Arrastra las 3 tarjetas de **"Backlog"** a **"Sprint Backlog"**
2. Ordénalas por prioridad:
   - 1º: HU-002 (Crítica - Seguridad)
   - 2º: HU-001 (Alta - Garantes)
   - 3º: HU-003 (Alta - Cuentas Bancarias)

### Paso 5.2: Crear tarjeta de Sprint Goal (Opcional)

En la columna **"Sprint Backlog"**, crea una tarjeta especial:

**Título**: `🎯 SPRINT 1 GOAL`

**Descripción**:
```
Implementar funcionalidades críticas de seguridad y gestión de clientes para Financiera Horizonte S.A.

## Objetivos:
- ✅ Proteger datos financieros sensibles (HU-002)
- ✅ Habilitar gestión de garantes (HU-001)
- ✅ Implementar historial de cuentas bancarias (HU-003)

## Métricas:
- Total Story Points: 16
- Duración: 2 semanas
- Fecha inicio: [Tu fecha]
- Fecha fin: [Tu fecha]
```

---

## 🔍 PARTE 6: Filtros y Vistas

### Crear filtros rápidos

1. Presiona la tecla **`F`** en el teclado
2. Selecciona una etiqueta para filtrar (ej: 🔴 Seguridad)
3. Verás solo las tarjetas con esa épica

### Atajos de teclado útiles

| Tecla | Acción |
|-------|--------|
| `Q` | Mostrar solo mis tarjetas |
| `F` | Filtrar por etiqueta |
| `D` | Agregar fecha de vencimiento |
| `L` | Abrir menú de etiquetas |
| `Espacio` | Asignarme la tarjeta |

---

## ✅ PARTE 7: Verificación Final

Revisa que tu tablero tenga:

- [ ] 8 columnas configuradas correctamente
- [ ] 3 etiquetas de Épicas (Azul, Rojo, Verde)
- [ ] 3 tarjetas con formato `(SP) HU-00X - Título`
- [ ] Cada tarjeta tiene descripción completa
- [ ] Cada tarjeta tiene checklist de Criterios de Aceptación
- [ ] Etiquetas asignadas correctamente
- [ ] Tarjetas en la columna "Sprint Backlog" u ordenadas por prioridad

---

## 📸 PARTE 8: Compartir con el Equipo

### Paso 8.1: Hacer el tablero público

1. Haz clic en **"Compartir"** (esquina superior derecha)
2. Cambia la visibilidad a **"Público"** o **"Equipo"**
3. Copia el enlace del tablero

### Paso 8.2: Invitar a mentores/facilitadores

1. Haz clic en **"Invitar"**
2. Ingresa los emails de tus mentores
3. Asigna rol **"Observador"** o **"Miembro"**

### Paso 8.3: Exportar como evidencia (Opcional)

1. Menú → **"Más"** → **"Imprimir y exportar"**
2. Selecciona **"Exportar como JSON"** (backup completo)
3. O toma capturas de pantalla del tablero completo

---

## 🎓 PARTE 9: Buenas Prácticas

### Durante el Sprint

1. **Actualiza diariamente**: Mueve las tarjetas según avances
2. **Marca checklist**: Completa criterios de aceptación uno por uno
3. **Comenta en tarjetas**: Documenta decisiones técnicas
4. **Adjunta evidencia**: Screenshots de Salesforce, diagramas

### Regla de Oro

> **"Nunca muevas una tarjeta hacia atrás"**
> 
> Si algo falla en QA, crea una nueva tarjeta de Bug o marca la tarjeta con etiqueta roja "Bloqueado", pero no la devuelvas a columnas anteriores.

### WIP Limit (Work In Progress)

- Máximo **1-2 tarjetas** en "En Progreso" por persona
- Mejor terminar una tarea que empezar muchas

---

## 🚀 ¡Listo!

Tu tablero de Trello está completamente configurado y listo para gestionar el Sprint 1 de Financiera Horizonte S.A.

**Próximos pasos**:
1. Comienza a trabajar en HU-002 (Prioridad Crítica)
2. Mueve la tarjeta a "En Progreso"
3. Configura Field-Level Security en tu Sandbox
4. Marca los criterios de aceptación conforme avances
5. Mueve a "SF QA" para pruebas

---

## 📚 Recursos Adicionales

- [Guía oficial de Trello](https://trello.com/guide)
- [Atajos de teclado completos](https://trello.com/shortcuts)
- [Power-Ups recomendados](https://trello.com/power-ups)

---

**Creado para**: Salesforce Admin + Agent Force  
**Sprint**: 1 | **Clase**: 3 - Práctica  
**Caso**: Financiera Horizonte S.A.

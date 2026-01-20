# Ambiente QA

## 📋 Información del Ambiente

**Tipo de Ambiente**: Partial Copy Sandbox (o Developer si no hay Partial disponible)  
**Propósito**: Testing y Quality Assurance  
**Creado el**: [Fecha de creación]  
**Última actualización**: [Fecha]

---

## 🔗 Acceso al Ambiente

### URL de Login

**URL**: [https://test.salesforce.com](https://test.salesforce.com)  
**My Domain**: [https://[nombre-org]--qa.sandbox.my.salesforce.com](https://[nombre-org]--qa.sandbox.my.salesforce.com)

---

## 👥 Credenciales de Usuarios Admin

### Usuario Admin 1

**Nombre**: [Nombre del equipo]  
**Username**: `[nombre].[apellido]@equipo[numero].com.qa`  
**Email**: [email del responsable]  
**Perfil**: System Administrator  
**Responsable**: [Nombre del Tester QA]

---

### Usuario Admin 2

**Nombre**: [Nombre del equipo]  
**Username**: `[nombre].[apellido]@equipo[numero].com.qa`  
**Email**: [email del responsable]  
**Perfil**: System Administrator  
**Responsable**: [Nombre del miembro del equipo]

---

## 📝 Instrucciones para Crear el Ambiente QA

### Paso 1: Crear Sandbox QA

1. Login en PROD con credenciales del instructor
2. Setup → Environments → Sandboxes
3. Click "New Sandbox"
4. Seleccionar tipo: **Partial Copy** (o Developer si no está disponible)
5. Nombre: `QA` o `Equipo[X]_QA`
6. Descripción: "Ambiente de testing para Equipo [X]"
7. Si es Partial Copy, seleccionar objetos a copiar:
   - Accounts
   - Contacts
   - Opportunities
   - (Otros objetos relevantes)
8. Click "Create"
9. Esperar ~30-60 minutos para Partial Copy (recibirás email)

---

### Paso 2: Crear Usuarios de Testing

Además de los 2 Admin, crear usuarios de diferentes perfiles para testing:

#### Usuario Ejecutivo de Créditos

**Username**: `ejecutivo.qa@equipo[numero].com.qa`  
**Perfil**: Ejecutivo de Créditos (o Standard User)  
**Propósito**: Testing de funcionalidades de ventas

#### Usuario Atención al Cliente

**Username**: `atencion.cliente@equipo[numero].com.qa`  
**Perfil**: Atención al Cliente (o Standard User)  
**Propósito**: Testing de restricciones de seguridad

#### Usuario Gerente

**Username**: `gerente.qa@equipo[numero].com.qa`  
**Perfil**: Gerente de Finanzas (o Standard User)  
**Propósito**: Testing de permisos gerenciales

---

## 🔧 Configuración Inicial del Ambiente QA

### Checklist de Configuración

- [ ] Sandbox QA creado
- [ ] My Domain configurado (opcional)
- [ ] 2 usuarios Admin creados
- [ ] 3+ usuarios de testing creados (diferentes perfiles)
- [ ] Credenciales documentadas
- [ ] Datos de prueba cargados
- [ ] Timezone y Language configurados

---

## 📊 Datos de Prueba

### Estrategia de Datos

**Opción A**: Usar datos de PROD (si es Partial Copy)
- ✅ Datos realistas
- ⚠️ Anonimizar información sensible

**Opción B**: Crear datos ficticios
- ✅ Sin riesgos de privacidad
- ⚠️ Requiere tiempo de creación

### Datos Mínimos Requeridos

| Objeto | Cantidad Mínima | Propósito |
|--------|-----------------|-----------|
| Accounts | 20 | Testing de búsquedas y reportes |
| Contacts | 50 | Testing de relaciones y seguridad |
| Opportunities | 30 | Testing de Contact Roles y garantes |
| Bank Accounts (custom) | 60 | Testing de múltiples cuentas |

---

### Cómo Cargar Datos de Prueba

#### Opción 1: Data Loader

1. Descargar Data Loader
2. Login en QA
3. Preparar CSV con datos ficticios
4. Insert → Seleccionar objeto → Mapear campos
5. Finish

#### Opción 2: Data Import Wizard

1. Setup → Data Import Wizard
2. Seleccionar objeto (Accounts, Contacts, etc.)
3. Upload CSV
4. Map fields
5. Start Import

#### Opción 3: Apex Anonymous (para pocos registros)

```apex
// Crear 10 Contacts de prueba
List<Contact> contacts = new List<Contact>();
for(Integer i = 1; i <= 10; i++) {
    contacts.add(new Contact(
        FirstName = 'Test',
        LastName = 'Contact ' + i,
        Email = 'test' + i + '@example.com'
    ));
}
insert contacts;
```

---

## 🧪 Uso del Ambiente QA

### ¿Cuándo usar QA?

- ✅ Testing de funcionalidades antes de PROD
- ✅ Validación de Criterios de Aceptación
- ✅ Testing de seguridad (FLS, permisos)
- ✅ Testing de integración
- ✅ User Acceptance Testing (UAT)
- ✅ Demos internas al equipo

### ¿Qué NO hacer en QA?

- ❌ Desarrollar nuevas funcionalidades (usar DEV)
- ❌ Hacer cambios sin documentar
- ❌ Borrar datos de prueba sin avisar al equipo
- ❌ Demos al cliente (usar PROD)

---

## 📋 Proceso de Testing en QA

### Flujo de Trabajo

1. **Desarrollo en DEV** → Funcionalidad completada
2. **Deployment a QA** → Via Change Set o Metadata API
3. **Testing en QA** → Ejecutar test cases
4. **Aprobación** → Si pasa todos los tests
5. **Deployment a PROD** → Funcionalidad lista para producción

---

### Registro de Testing

| Fecha | HU Testeada | Tester | Resultado | Bugs Encontrados |
|-------|-------------|--------|-----------|------------------|
| [Fecha] | HU-XXX | [Nombre] | ✅ PASS / ❌ FAIL | [Link a bugs] |

**Ejemplo**:
| Fecha | HU Testeada | Tester | Resultado | Bugs Encontrados |
|-------|-------------|--------|-----------|------------------|
| 22 Enero 2026 | HU-001 Garantes | Ana QA | ✅ PASS | Ninguno |
| 28 Enero 2026 | HU-002 Seguridad | Carlos QA | ✅ PASS | Ninguno |

---

## 🔄 Sincronización con DEV

### Cuándo Sincronizar

- Después de cada Sprint
- Cuando hay cambios mayores en DEV
- Antes de UAT

### Cómo Sincronizar

**Método 1: Change Sets**
1. En DEV: Setup → Outbound Change Sets
2. Crear Change Set con componentes
3. Upload a QA
4. En QA: Setup → Inbound Change Sets
5. Deploy

**Método 2: Metadata API (SFDX)**
```bash
# Retrieve from DEV
sfdx force:source:retrieve -u dev-org

# Deploy to QA
sfdx force:source:deploy -u qa-org
```

---

## 🐛 Gestión de Bugs

### Cuando Encuentres un Bug

1. Documentar en archivo `04-Tester_QA.md`
2. Crear tarjeta en Trello con etiqueta "BUG"
3. Asignar al desarrollador
4. Mover HU de vuelta a "En Progreso" o "Backlog"

### Formato de Reporte de Bug

**Título**: [BUG] [Descripción breve]

**Descripción**:
- **Pasos para reproducir**: [1, 2, 3...]
- **Resultado esperado**: [Qué debería pasar]
- **Resultado obtenido**: [Qué pasó realmente]
- **Severidad**: Crítica / Alta / Media / Baja
- **Screenshot**: [Adjuntar si aplica]

---

## 🔐 Seguridad en QA

### Datos Sensibles

- ⚠️ **NO** usar datos reales de clientes
- ⚠️ **NO** usar emails reales en testing
- ✅ Usar datos ficticios o anonimizados
- ✅ Usar emails de prueba (@example.com, @test.com)

### Permisos

- ✅ Solo el equipo debe tener acceso a QA
- ✅ No compartir credenciales fuera del equipo
- ✅ Revocar acceso al finalizar el proyecto

---

## ✅ Verificación de QA

### Checklist Antes de Aprobar para PROD

- [ ] Todos los test cases pasaron
- [ ] No hay bugs críticos o altos
- [ ] Criterios de aceptación verificados
- [ ] Testing de seguridad completado
- [ ] Testing de performance aceptable
- [ ] Documentación actualizada
- [ ] Cliente/Product Owner aprobó (si aplica)

---

## 📞 Soporte

### Problemas Comunes

**P: Los datos de prueba se borraron**
- R: Recargar datos usando Data Loader o scripts

**P: El Change Set falló al deployar**
- R: Verificar dependencias (ej: campos custom antes de validation rules)
- R: Revisar errores en Deployment Status

**P: Un test case falla pero en DEV funciona**
- R: Verificar que QA tiene la última versión de DEV
- R: Verificar datos de prueba (pueden ser diferentes)

---

**Última actualización**: [Fecha]  
**Próxima revisión**: [Fecha]  
**Responsable del ambiente**: [Nombre del QA Lead]

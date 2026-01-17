# Ambiente PROD

## 📋 Información del Ambiente

**Tipo de Ambiente**: Producción  
**Propósito**: Ambiente real de trabajo del cliente  
**Creado el**: [Fecha de creación de la org]  
**Última actualización**: [Fecha]

---

## 🔗 Acceso al Ambiente

### URL de Login

**URL**: [https://login.salesforce.com](https://login.salesforce.com)  
**My Domain**: [https://[nombre-org].my.salesforce.com](https://[nombre-org].my.salesforce.com)

⚠️ **IMPORTANTE**: Este es el ambiente REAL del cliente. Todos los cambios afectan a usuarios reales.

---

## 👥 Credenciales de Usuarios Admin

### Usuario Admin 1

**Nombre**: [Nombre del equipo]  
**Username**: `[nombre].[apellido]@equipo[numero].com.prod`  
**Email**: [email del responsable]  
**Perfil**: System Administrator  
**Responsable**: [Nombre del líder técnico]

---

### Usuario Admin 2

**Nombre**: [Nombre del equipo]  
**Username**: `[nombre].[apellido]@equipo[numero].com.prod`  
**Email**: [email del responsable]  
**Perfil**: System Administrator  
**Responsable**: [Nombre del miembro del equipo]

---

## ⚠️ REGLAS CRÍTICAS PARA PROD

### 🛑 NUNCA hacer en PROD:

- ❌ **NUNCA** experimentar o probar configuraciones nuevas
- ❌ **NUNCA** borrar datos sin backup
- ❌ **NUNCA** hacer cambios sin aprobar en QA primero
- ❌ **NUNCA** trabajar directamente en PROD (siempre DEV → QA → PROD)
- ❌ **NUNCA** hacer deployment un viernes o antes de feriados
- ❌ **NUNCA** hacer cambios sin documentar
- ❌ **NUNCA** compartir credenciales de PROD por email o chat

### ✅ SIEMPRE hacer en PROD:

- ✅ **SIEMPRE** hacer backup antes de cambios mayores
- ✅ **SIEMPRE** tener plan de rollback
- ✅ **SIEMPRE** comunicar a usuarios antes de deployment
- ✅ **SIEMPRE** hacer deployment en horario de baja actividad
- ✅ **SIEMPRE** verificar en QA antes de PROD
- ✅ **SIEMPRE** documentar cada cambio
- ✅ **SIEMPRE** tener a alguien más revisando (4 ojos)

---

## 📝 Instrucciones para Configurar Acceso a PROD

### Opción A: Org del Instructor (Proyecto Académico)

Si el instructor provee una org de PROD:

1. Instructor crea usuarios para cada equipo
2. Username format: `equipo[X].admin@[org].com`
3. Instructor envía credenciales por canal seguro
4. Equipo documenta credenciales en este archivo
5. Cambiar password en primer login

---

### Opción B: Trailhead Playground como "PROD"

Si usan Trailhead Playground:

1. Crear Playground específico para PROD
2. Nombre: `Equipo [X] - PROD`
3. **NO** usar el mismo Playground que DEV
4. Configurar My Domain
5. Cargar datos de demostración

---

### Opción C: Developer Edition como PROD

1. Registrarse en [https://developer.salesforce.com/signup](https://developer.salesforce.com/signup)
2. Usar email del equipo
3. Username: `equipo[X].admin@[dominio].com`
4. Completar registro
5. Verificar email
6. Login y documentar credenciales

---

## 🔧 Configuración Inicial de PROD

### Checklist de Configuración

- [ ] Org de PROD identificada
- [ ] My Domain configurado
- [ ] 2 usuarios Admin creados
- [ ] Credenciales documentadas (de forma segura)
- [ ] Timezone configurado
- [ ] Language configurado
- [ ] Currency configurado
- [ ] Company Information completada
- [ ] Logo de la empresa cargado (opcional)

---

## 📊 Uso del Ambiente PROD

### ¿Cuándo usar PROD?

- ✅ Demos al cliente
- ✅ User Acceptance Testing (UAT) final
- ✅ Deployment de funcionalidades aprobadas
- ✅ Capacitación de usuarios finales
- ✅ Trabajo real del negocio

### ¿Qué NO hacer en PROD?

- ❌ Desarrollo de nuevas funcionalidades
- ❌ Testing experimental
- ❌ Cargar datos de prueba ficticios
- ❌ Cambios sin aprobar

---

## 🚀 Proceso de Deployment a PROD

### Pre-Deployment Checklist

- [ ] Funcionalidad testeada y aprobada en QA
- [ ] Todos los test cases pasaron (100%)
- [ ] Cliente/Product Owner aprobó
- [ ] Documentación actualizada
- [ ] Change Set o package preparado
- [ ] Backup de PROD realizado
- [ ] Plan de rollback documentado
- [ ] Usuarios notificados del deployment
- [ ] Horario de deployment acordado (fuera de horas pico)

---

### Pasos de Deployment

#### Método 1: Change Sets

1. **En QA**: Setup → Outbound Change Sets
2. Crear Change Set con nombre descriptivo: `Sprint[X]_[Fecha]_[Descripción]`
3. Agregar componentes:
   - Custom Objects
   - Custom Fields
   - Flows
   - Validation Rules
   - Page Layouts
   - Permission Sets
   - Reports
4. Upload a PROD
5. **En PROD**: Setup → Inbound Change Sets
6. Validar Change Set (sin deployar aún)
7. Revisar errores si los hay
8. Si validación OK → Deploy
9. Seleccionar opciones:
   - ✅ Run All Tests (si hay Apex)
   - ✅ Rollback on Error
10. Click "Deploy"
11. Monitorear Deployment Status

---

#### Método 2: Metadata API (SFDX)

```bash
# 1. Retrieve from QA
sfdx force:source:retrieve -u qa-org -m CustomObject,CustomField,Flow

# 2. Validate in PROD (dry run)
sfdx force:source:deploy -u prod-org --checkonly --testlevel RunLocalTests

# 3. If validation passes, deploy
sfdx force:source:deploy -u prod-org --testlevel RunLocalTests
```

---

### Post-Deployment Checklist

- [ ] Deployment completado sin errores
- [ ] Smoke testing realizado (verificar funcionalidades básicas)
- [ ] Usuarios notificados que deployment terminó
- [ ] Documentar deployment en este archivo
- [ ] Actualizar versión en documentación
- [ ] Monitorear por 24-48 horas para bugs

---

## 📋 Registro de Deployments a PROD

### Historial de Deployments

| Fecha | Sprint | Componentes | Responsable | Estado | Rollback |
|-------|--------|-------------|-------------|--------|----------|
| [Fecha] | Sprint X | [Lista] | [Nombre] | ✅ Exitoso / ❌ Fallido | ✅/❌ |

**Ejemplo**:
| Fecha | Sprint | Componentes | Responsable | Estado | Rollback |
|-------|--------|-------------|-------------|--------|----------|
| 2026-01-30 | Sprint 1 | Bank_Account__c, Contact Roles, FLS | Juan Admin | ✅ Exitoso | ❌ No necesario |

---

### Detalles del Último Deployment

**Fecha**: [Fecha]  
**Sprint**: [Número]  
**Change Set ID**: [ID del Change Set]

**Componentes Deployados**:
- [Componente 1]
- [Componente 2]
- [Componente 3]

**Tiempo de Deployment**: [X minutos]  
**Tests Ejecutados**: [X/X pasaron]  
**Errores**: [Ninguno / Descripción]

---

## 🔄 Plan de Rollback

### Cuándo Hacer Rollback

- ❌ Deployment causó errores críticos
- ❌ Funcionalidad no trabaja como esperado
- ❌ Usuarios reportan problemas masivos
- ❌ Tests en PROD fallan

### Cómo Hacer Rollback

#### Opción 1: Destructive Changes

1. Crear Change Set con componentes a remover
2. Usar Destructive Changes XML
3. Deploy a PROD

#### Opción 2: Restaurar Backup

1. Si tienes backup de metadata
2. Deploy versión anterior

#### Opción 3: Desactivar Manualmente

1. Desactivar Flows
2. Desactivar Validation Rules
3. Ocultar campos en Page Layouts
4. Revocar Permission Sets

---

## 💾 Backup de PROD

### Estrategia de Backup

**Frecuencia**: Antes de cada deployment mayor

**Qué respaldar**:
- [ ] Metadata (Change Set de toda la configuración)
- [ ] Datos críticos (Data Loader export)
- [ ] Configuración de usuarios y permisos
- [ ] Reports y Dashboards

### Herramientas de Backup

**Opción 1**: Weekly Data Export (nativo de Salesforce)
- Setup → Data Export → Schedule Export

**Opción 2**: Data Loader
- Export manual de objetos críticos

**Opción 3**: Herramientas de terceros
- OwnBackup
- Spanning Backup
- Odaseva

---

## 🔐 Seguridad en PROD

### Control de Acceso

- ✅ Solo 2-3 personas deben tener acceso Admin a PROD
- ✅ Activar MFA (Multi-Factor Authentication)
- ✅ Configurar Login Hours (horario de trabajo)
- ✅ Configurar IP Restrictions (si aplica)
- ✅ Revisar Setup Audit Trail regularmente

### Auditoría

**Revisar mensualmente**:
- Setup Audit Trail (quién hizo qué cambios)
- Login History (accesos sospechosos)
- Field History Tracking (cambios en datos sensibles)

---

## 📞 Soporte y Escalación

### Contactos de Emergencia

**Administrador Principal**: [Nombre] - [Email] - [Teléfono]  
**Administrador Backup**: [Nombre] - [Email] - [Teléfono]  
**Instructor/Mentor**: [Nombre] - [Email]

### Proceso de Escalación

1. **Nivel 1**: Equipo intenta resolver (30 min)
2. **Nivel 2**: Consultar documentación y comunidad (1 hora)
3. **Nivel 3**: Contactar a instructor/mentor
4. **Nivel 4**: Salesforce Support (si org tiene contrato)

---

## 📊 Monitoreo de PROD

### Métricas a Monitorear

- **Performance**: Tiempo de carga de páginas
- **Errores**: Apex errors, Flow errors
- **Uso**: Número de usuarios activos
- **Storage**: Data storage, File storage

### Herramientas de Monitoreo

- Setup → System Overview
- Setup → Apex Jobs
- Setup → Debug Logs
- Reports de uso

---

## ✅ Verificación de PROD

### Checklist de Salud de PROD

Verificar semanalmente:

- [ ] Todos los usuarios pueden hacer login
- [ ] No hay errores críticos en logs
- [ ] Storage está dentro de límites (< 80%)
- [ ] Backups están actualizados
- [ ] No hay Flows o Processes fallando
- [ ] Permisos están correctos

---

## 📝 Notas Importantes

### Limitaciones de PROD

**Developer Edition**:
- Límite de 2 usuarios
- Límite de storage reducido
- No tiene Sandboxes

**Trailhead Playground**:
- Se puede eliminar automáticamente si no se usa
- No para uso productivo real
- Solo para aprendizaje

### Recomendaciones

- ✅ Documentar TODO lo que se hace en PROD
- ✅ Nunca trabajar solo en PROD (siempre con revisión)
- ✅ Comunicar cambios al equipo
- ✅ Mantener este archivo actualizado

---

**Última actualización**: [Fecha]  
**Próxima revisión**: [Fecha]  
**Responsable del ambiente**: [Nombre del líder técnico]

---

## 🎓 Recursos de Aprendizaje

- [Salesforce Deployment Best Practices](https://help.salesforce.com/s/articleView?id=sf.deploy_best_practices.htm)
- [Change Sets Guide](https://help.salesforce.com/s/articleView?id=sf.changesets.htm)
- [Backup and Recovery](https://help.salesforce.com/s/articleView?id=sf.admin_data_backup.htm)

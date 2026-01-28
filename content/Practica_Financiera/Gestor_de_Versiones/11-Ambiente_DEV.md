# Ambiente DEV

## 📋 Información del Ambiente

**Tipo de Ambiente**: Developer Sandbox  
**Propósito**: Desarrollo y configuración inicial  
**Equipo**: 9 personas (6 Admins + 3 Roles Funcionales)  
**Admins de este ambiente**: 2 personas (Estudiantes 1-2)  
**Creado el**: [Fecha de creación]  
**Última actualización**: [Fecha]

---

## 🔗 Acceso al Ambiente

### URL de Login

**URL**: [https://test.salesforce.com](https://test.salesforce.com)  
**My Domain**: [https://[nombre-org]--dev.sandbox.my.salesforce.com](https://[nombre-org]--dev.sandbox.my.salesforce.com)

---

## 👥 Credenciales de Usuarios Admin

### Usuario Admin 1

**Nombre**: [Nombre del equipo]  
**Username**: `[nombre].[apellido]@equipo[numero].com.dev`  
**Email**: [email del responsable]  
**Perfil**: System Administrator  
**Responsable**: [Nombre del miembro del equipo]

**Ejemplo**:
- Username: `juan.perez@equipo1.com.dev`
- Email: juan.perez@gmail.com
- Responsable: Juan Pérez

---

### Usuario Admin 2

**Nombre**: [Nombre del equipo]  
**Username**: `[nombre].[apellido]@equipo[numero].com.dev`  
**Email**: [email del responsable]  
**Perfil**: System Administrator  
**Responsable**: [Nombre del miembro del equipo]

---

## 📝 Instrucciones para Crear el Ambiente DEV

### Paso 1: Crear Developer Sandbox

1. Login en PROD con credenciales del instructor
2. Setup → Environments → Sandboxes
3. Click "New Sandbox"
4. Seleccionar tipo: **Developer**
5. Nombre: `DEV` o `Equipo[X]_DEV`
6. Descripción: "Ambiente de desarrollo para Equipo [X]"
7. Click "Create"
8. Esperar ~10-15 minutos (recibirás email cuando esté listo)

---

### Paso 2: Crear Usuarios Admin

#### Opción A: Desde Setup

1. Setup → Users → Users
2. Click "New User"
3. Completar:
   - First Name: [Nombre]
   - Last Name: [Apellido]
   - Email: [Email real del miembro]
   - Username: `[nombre].[apellido]@equipo[numero].com.dev`
   - Nickname: [Apodo único]
   - Profile: System Administrator
   - User License: Salesforce
4. Desmarcar "Generate new password and notify user immediately"
5. Click "Save"
6. Establecer password manualmente

#### Opción B: Desde Trailhead Playground

Si usas Trailhead Playground como DEV:
1. Ir a [https://trailhead.salesforce.com/es/users/profiles/orgs](https://trailhead.salesforce.com/es/users/profiles/orgs)
2. Click "Create a Playground"
3. Nombre: `Equipo [X] - DEV`
4. Click "Create"
5. Anotar credenciales automáticas

---

### Paso 3: Configurar My Domain (Opcional pero Recomendado)

1. Setup → Company Settings → My Domain
2. Ingresar nombre: `equipo[X]dev` (ejemplo: `equipo1dev`)
3. Click "Check Availability"
4. Click "Register Domain"
5. Esperar email de confirmación
6. Click "Log in" en el email
7. Setup → My Domain → Click "Deploy to Users"

**My Domain resultante**: `https://equipo1dev.my.salesforce.com`

---

## 🔧 Configuración Inicial del Ambiente

### Checklist de Configuración

- [ ] My Domain configurado
- [ ] 2 usuarios Admin creados
- [ ] Credenciales documentadas en este archivo
- [ ] Password compartido con el equipo (de forma segura)
- [ ] Timezone configurado (Setup → Company Information)
- [ ] Language configurado a Español (si aplica)
- [ ] Currency configurado (USD o moneda local)

---

## 📊 Uso del Ambiente DEV

### ¿Cuándo usar DEV?

- ✅ Crear objetos custom
- ✅ Crear campos custom
- ✅ Configurar Flows
- ✅ Crear Validation Rules
- ✅ Experimentar con configuraciones
- ✅ Probar ideas antes de implementar

### ¿Qué NO hacer en DEV?

- ❌ Cargar datos de producción reales
- ❌ Compartir credenciales fuera del equipo
- ❌ Hacer demos al cliente (usar QA o PROD)
- ❌ Borrar objetos estándar

---

## 🔄 Refresh del Sandbox

### Cuándo hacer Refresh

- Cuando DEV esté muy desincronizado con PROD
- Cuando necesites datos actualizados de PROD
- Cuando quieras empezar "limpio"

### Cómo hacer Refresh

1. Setup → Sandboxes
2. Buscar tu sandbox "DEV"
3. Click "Refresh"
4. Confirmar (⚠️ esto borrará todos los datos actuales)
5. Esperar ~10-15 minutos

**⚠️ ADVERTENCIA**: Refresh borra TODOS los datos y configuraciones del sandbox. Hacer backup antes.

---

## 📝 Registro de Cambios en DEV

### Cambios Realizados

| Fecha | Cambio | Responsable | Estado |
|-------|--------|-------------|--------|
| [Fecha] | [Descripción del cambio] | [Nombre] | ✅ Migrado a QA / ⏳ Pendiente |

**Ejemplo**:
| Fecha | Cambio | Responsable | Estado |
|-------|--------|-------------|--------|
| 2026-01-16 | Crear objeto Bank_Account__c | Juan Pérez | ✅ Migrado a QA |
| 2026-01-17 | Configurar FLS en Monthly_Salary__c | María García | ✅ Migrado a QA |

---

## 🔐 Seguridad

### Buenas Prácticas

- ✅ Cambiar password cada 90 días
- ✅ No compartir credenciales por email
- ✅ Usar password manager (LastPass, 1Password, etc.)
- ✅ Activar MFA si es posible
- ✅ No usar passwords simples

### Password Sugerido

Formato: `[Equipo][Numero][Simbolo][Palabra]`

Ejemplo: `Equipo1$Salesforce2026`

---

## 📞 Soporte

### Problemas Comunes

**P: No puedo hacer login**
- R: Verificar que estás usando la URL correcta (test.salesforce.com o My Domain)
- R: Verificar username completo (debe terminar en .dev)
- R: Resetear password desde la pantalla de login

**P: El sandbox no está disponible**
- R: Verificar que la creación se completó (revisar email)
- R: Esperar 15-20 minutos después de crear

**P: Olvidé mi password**
- R: Click "Forgot Password" en login
- R: O pedir a otro admin que lo resetee desde Setup → Users

---

## ✅ Verificación

### Checklist de Verificación

Antes de empezar a trabajar, verificar:

- [ ] Puedo hacer login exitosamente
- [ ] Veo el ambiente correcto (debe decir "DEV" o nombre del sandbox)
- [ ] Tengo permisos de System Administrator
- [ ] Puedo crear objetos custom (Setup → Object Manager → Create)
- [ ] My Domain funciona (si lo configuraste)

---

**Última actualización**: [Fecha]  
**Próxima revisión**: [Fecha]  
**Responsable del ambiente**: [Nombre]

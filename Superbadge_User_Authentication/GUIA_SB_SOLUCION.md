# Guía SB - Autenticación de Usuario

## ⚠️ AVISO IMPORTANTE ANTES DE EMPEZAR

Para este Superbadge NO puedes usar un Playground normal.

Debes haberte registrado en el enlace específico que aparece en la sección "Prework and Notes" (Sign up for a free Developer Edition org with special configuration).

Si usas tu organización "EQUIPO 7 - Academico" asegúrate de que esa sea la que creaste específicamente para este reto. Si es una org vieja, los retos fallarán.

---

## Reto 1: Políticas de Contraseña (Password Policies)

**Objetivo**: Configurar las reglas de contraseñas generales y endurecerlas para los Administradores.

### Paso 1: Políticas para toda la organización

Ve a Setup (Configuración).

En el buscador rápido escribe: Password Policies (Políticas de contraseñas).

Configura lo siguiente:

- **User passwords expire in**: 90 days (o lo que esté por defecto, no lo especifican, pero lo importante son los siguientes).
- **Enforce password history**: 3 passwords remembered (estándar).
- **Minimum password length**: 12 characters.
- **Password complexity requirement**: Must include alpha, numeric, and special characters.
- **Password question requirement**: Cannot contain password.
- **Maximum invalid login attempts**: 3.
- **Lockout effective period**: 30 minutes.
- **Require a minimum 1 day password lifetime**: Check (Marcado) (Esto cumple el requisito de "no resetear más de una vez en 24h").
- **Obscure secret answer for password resets**: Check (Marcado).

Clic en Save.

---

### Paso 2: Políticas para System Administrator

Ve a Setup > Profiles.

Busca y haz clic en System Administrator (Administrador del Sistema).

Desplázate hacia abajo hasta la sección Password Policies (si no lo ves, busca el botón o enlace que dice "View Password Policies" o similar, a veces está en la parte superior dependiendo de la interfaz). Clic en Edit.

Configura lo siguiente para este perfil:

- **Minimum password length**: 15 characters.
- **Password complexity requirement**: Must include numbers, uppercase and lowercase letters, and special characters.

Clic en Save.

---

## Reto 2: Requisitos y Límites de Inicio de Sesión

**Objetivo**: Restringir desde DÓNDE y CUÁNDO pueden entrar los usuarios de Ventas y Call Center.

### Paso 1: Configurar perfil Inside Sales

Ve a Setup > Profiles.

Entra al perfil Inside Sales (o Inside Sales Representative).

Busca la sección Login IP Ranges (Rangos de IP de inicio de sesión). Clic en New.

**Corporate IP**:
- Start IP: `13.108.0.0`
- End IP: `13.108.0.0`
- Description: `Corporate Office`

Clic Save & New.

**VPN IP**:
- Start IP: `22.0.0.1`
- End IP: `22.0.255.0`
- Description: `VPN`

Clic Save.

Verifica Login Hours. Como el requisito dice "No time restrictions", asegúrate de que la lista de horas esté vacía (o sea, 24/7).

---

### Paso 2: Configurar perfil Call Center

Ve a Setup > Profiles.

Entra al perfil Call Center (o Call Center Agent).

Busca Login IP Ranges. Clic en New.

- Start IP: `13.108.0.0`
- End IP: `13.108.0.0`
- Description: `Corporate Office`

Clic Save.

Busca la sección Login Hours. Clic en Edit.

Configura de Lunes a Viernes (Monday - Friday).

- Start Time: `8:00 AM`.
- End Time: `5:00 PM (17:00)`.

Deja Sábado y Domingo vacíos.

Clic Save.

---

## Reto 3: Acceso API para Apps Conectadas

**Objetivo**: Bloquear el acceso libre a apps y permitir solo la App de iOS para el equipo de Inside Sales.

Ve a Setup.

Busca Manage Connected Apps (Gestionar aplicaciones conectadas).

**Nota**: Asegúrate de entrar en "Manage Connected Apps" y no en "App Manager".

En la lista, busca Salesforce for iOS. Haz clic en el nombre (letras azules).

Clic en el botón Edit Policies.

En la sección OAuth Policies:

- Cambia **Permitted Users** a: **Admin approved users are pre-authorized** (Los usuarios aprobados por el administrador están preautorizados).
- Te saldrá una alerta advirtiendo que los usuarios actuales serán bloqueados. Acepta.

Clic en Save.

Ahora volverás a la página de detalles de la App. Desplázate hacia abajo hasta la sección Profiles.

Clic en Manage Profiles.

Selecciona únicamente el perfil Inside Sales.

Clic en Save.

**Nota**: El enunciado dice "lock down ALL connected apps", pero técnicamente el validador del Superbadge suele revisar específicamente la configuración de "Salesforce for iOS" y que hayas cambiado la política de permisos. Si quieres ser exhaustivo, deberías revisar otras apps, pero NO toques la app llamada "Trailhead Connected App".

---

## Reto 4: IP de Confianza (Trusted IP)

**Objetivo**: Evitar que pidan código de verificación (OTP) cuando se está en la oficina. Ojo: Esto es diferente a los rangos de IP del perfil.

Ve a Setup.

En el buscador escribe Network Access (Acceso a la red).

Clic en New.

Ingresa los datos de la oficina corporativa:

- Start IP Address: `13.108.0.0`
- End IP Address: `13.108.0.0`
- Description: `Corporate Office`

Clic en Save.

---

## Validación Final

Ahora regresa a la página del Superbadge en Trailhead y haz clic en Check Challenge para cada paso.

- **Si falla el paso 3**: Asegúrate de haber editado la política de "Salesforce for iOS" a "Admin approved users" antes de intentar agregar el perfil.
- **Si falla el paso 1**: Revisa que hayas marcado la casilla "Require a minimum 1 day password lifetime".

---

**Grupo**: 3 - VISIONARY ADMINS  
**Última actualización**: 17 Enero 2026

# 🛠️ Guía de Mantenimiento y Operaciones

**Proyecto**: Salesforce Admin Learning Platform  
**Versión**: 1.0  
**Última Actualización**: 31 Enero 2026

---

## 🎯 Objetivo
Este documento define los procedimientos estándar para mantener la salud, seguridad y actualización de la plataforma en producción.

---

## 1. 📦 Gestión de Dependencias

Mantener las librerías al día es vital para la seguridad y performance.

### 1.1 Protocolo de Actualización
1.  **Crear Rama**: `git checkout -b chore/update-deps`
2.  **Verificar obsoletos**: Ejecutar `pip list --outdated`
3.  **Actualizar**: Modificar `requirements.txt` o usar `pip install -U [paquete]`
4.  **Congelar**: `pip freeze > requirements.txt`
5.  **Validar**: Ejecutar `pytest`. **Si los tests fallan, NO actualizar.**
6.  **Commit**: `chore(deps): update [paquete] to [version]`

### 1.2 Regla de Oro
> "Si funciona, no lo toques... a menos que sea un parche de seguridad o toque mantenimiento programado."

### 1.3 Calendario de Actualizaciones (Estrategia)
Para evitar la obsolescencia ("Bit Rot") sin sacrificar la estabilidad, adoptamos este calendario:

| Tipo | Frecuencia | Ejemplo | Acción |
| :--- | :--- | :--- | :--- |
| **🛡️ Crítica** | **Inmediata** | `CVE-202X` (Vulnerabilidad) | Crear Hotfix. Actualizar SOLO la librería afectada. |
| **🛠️ Rutina** | **Mensual** | `v1.2.3` -> `v1.2.9` (Patch) | Revisar `pip list --outdated`. Aplicar actualizaciones *minor/patch*. |
| **🏗️ Mayor** | **Trimestral** | `v1.x` -> `v2.x` (Major) | Planificar como Tarea de Desarrollo. Requiere refactorización. |

**Nota sobre Estabilidad**: No perseguimos siempre la versión "Latest" (última), sino la versión "Stable" (probada). Esperar 2-3 semanas después de un lanzamiento mayor antes de adoptarlo permite que la comunidad detecte los bugs primero.

---

## 2. 🛡️ Estrategia de Backups

### 2.1 Backup Automático (Script)
Usamos el script `scripts/backup_db.py` que genera un dump SQL completo.
*   **Comando**: `python scripts/backup_db.py`
*   **Destino**: Carpeta `backups/` (Ignorada por Git por seguridad)
*   **Frecuencia Recomendada**: Semanal (o antes de un deploy crítico).

### 2.2 Restauración (Disaster Recovery)
En caso de fallo catastrófico:
```bash
# Restaurar desde archivo SQL (Local o Prod)
psql -U [usuario] -d [nombre_db] -f backups/backup_file.sql
```

---

## 3. 🚨 Monitoreo y Observabilidad

### 3.1 Uptime (Disponibilidad)
*   **Herramienta**: UptimeRobot
*   **Endpoint**: `https://[app].onrender.com/health`
*   **Acción**: Si recibes alerta de "DOWN", verifica los logs de Render inmediatamente.

### 3.2 Errores (Sentry)
*   **Herramienta**: Sentry.io
*   **Flujo**:
    1.  Alerta llega al correo.
    2.  Clic en el enlace para ver el "Stack Trace".
    3.  Crear ticket/bug en GitHub con la info.
    4.  Crear rama `fix/...` para resolverlo.

---

## 4. 🧹 Limpieza y Salud

### 4.1 Base de Datos
*   **Migrations**: Nunca modificar tablas manualmente. Usar siempre `alembic`.
*   **Seed Data**: El script `seed_data.py` es idempotente (seguro de correr múltiples veces). Úsalo para actualizar contenidos curriculares sin borrar progreso de usuarios.

### 4.2 Logs
*   Revisar logs en Render ocasionalmente para detectar "Warnings" que no son errores pero indican problemas latentes (ej. "Database connection pool full").

---

**Responsable de Mantenimiento**: DevOps Lead

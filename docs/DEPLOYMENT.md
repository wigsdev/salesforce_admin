# 🚀 Guía de Despliegue (Deployment)

Este proyecto está configurado para desplegarse automáticamente en **Render** utilizando "Infrastructure as Code" (Blueprints).

## Prerrequisitos
- Cuenta en [Render.com](https://render.com).
- Repositorio conectado a GitHub.

## Archivos Clave
- `render.yaml`: Define la infraestructura (Web Service + Postgres DB).
- `scripts/build.sh`: Script que ejecuta Render para construir la app (`pip install` + `npm build` + `alembic upgrade`).

## Instrucciones de Despliegue (Paso a Paso)

1. **Dashboard de Render**:
   - Ve a [dashboard.render.com](https://dashboard.render.com).
   - Click en **New +** -> **Blueprint**.

2. **Conectar Repositorio**:
   - Selecciona el repositorio `admin_salesforce`.
   - Render detectará automáticamente el archivo `render.yaml`.

3. **Revisar Configuración**:
   - Verás dos servicios listados: `admin-salesforce` (Web) y `admin-salesforce-db` (Database).
   - Render te pedirá confirmar el Plan (selecciona "Free" si estás probando).

4. **Deploy**:
   - Click en **Apply**.
   - Render:
     1. Creará la Base de Datos PostgreSQL.
     2. Inyectará la `DATABASE_URL` automáticamente en la Web App.
     3. Ejecutar el `buildCommand` (`scripts/build.sh`).
     4. Iniciará el servidor Uvicorn.

## Variables de Entorno
Las siguientes variables se configuran automáticamente vía `render.yaml`:
- `DATABASE_URL`: Connection string (Manejado por Render).
- `SECRET_KEY`: Generado automáticamente.
- `ENVIRONMENT`: `production`.

Si necesitas agregar más (ej. API Keys), hazlo desde el Dashboard de Render -> Environment.

## Troubleshooting

### Error: "Table not found"
- Significa que las migraciones fallaron. Revisa los logs de "Build".
- Asegurate que `alembic upgrade head` se esté ejecutando en `build.sh`.

### Error: CSS no carga
- Tailwind no se compiló. Verifica que `npm run build:css` esté en el script de build.

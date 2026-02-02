# Setup PostgreSQL Database
# Run AFTER fix_postgresql.ps1

$psql = "C:\Program Files\PostgreSQL\18\bin\psql.exe"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "🗄️ Configurando Base de Datos Local" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# SQL commands
$sqlCommands = @"
-- Create database
CREATE DATABASE salesforce_admin_dev;

-- Create user
CREATE USER admin WITH PASSWORD 'dev_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE salesforce_admin_dev TO admin;

-- Connect to database
\c salesforce_admin_dev

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO admin;
"@

# Save to temp file
$tempSqlFile = "$env:TEMP\setup_db.sql"
$sqlCommands | Out-File -FilePath $tempSqlFile -Encoding UTF8

Write-Host "📝 Ejecutando comandos SQL..." -ForegroundColor Yellow
Write-Host "   (Te pedirá la contraseña de postgres)`n" -ForegroundColor Gray

# Execute
& $psql -U postgres -f $tempSqlFile

# Cleanup
Remove-Item $tempSqlFile -Force

Write-Host "`n✅ Base de datos configurada`n" -ForegroundColor Green

Write-Host "📝 Próximos pasos:" -ForegroundColor Yellow
Write-Host "1. Ejecutar migraciones: alembic upgrade head" -ForegroundColor White
Write-Host "2. Seed data: python scripts/seed_data.py" -ForegroundColor White
Write-Host "3. Verificar: python scripts/check_local_db.py`n" -ForegroundColor White

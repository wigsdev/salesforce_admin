# Fix PostgreSQL Local Connection
# Run as Administrator

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "🔧 Configurando PostgreSQL Local" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$postgresqlConf = "C:\Program Files\PostgreSQL\18\data\postgresql.conf"
$pgHbaConf = "C:\Program Files\PostgreSQL\18\data\pg_hba.conf"

# Backup files
Write-Host "📦 Creando backups..." -ForegroundColor Yellow
Copy-Item $postgresqlConf "$postgresqlConf.backup" -Force
Copy-Item $pgHbaConf "$pgHbaConf.backup" -Force
Write-Host "✅ Backups creados`n" -ForegroundColor Green

# Fix postgresql.conf
Write-Host "📝 Configurando postgresql.conf..." -ForegroundColor Yellow
$content = Get-Content $postgresqlConf
$newContent = $content | ForEach-Object {
    if ($_ -match "^#?listen_addresses\s*=") {
        "listen_addresses = '*'		# Modified by fix script"
    } elseif ($_ -match "^#?port\s*=") {
        "port = 5432				# Modified by fix script"
    } else {
        $_
    }
}
$newContent | Set-Content $postgresqlConf -Force
Write-Host "✅ postgresql.conf configurado`n" -ForegroundColor Green

# Fix pg_hba.conf
Write-Host "📝 Configurando pg_hba.conf..." -ForegroundColor Yellow
$hbaContent = Get-Content $pgHbaConf

# Check if our rules already exist
if ($hbaContent -notmatch "# Added by fix script") {
    Add-Content $pgHbaConf "`n# Added by fix script"
    Add-Content $pgHbaConf "host    all             all             127.0.0.1/32            scram-sha-256"
    Add-Content $pgHbaConf "host    all             all             ::1/128                 scram-sha-256"
}
Write-Host "✅ pg_hba.conf configurado`n" -ForegroundColor Green

# Restart PostgreSQL
Write-Host "🔄 Reiniciando PostgreSQL..." -ForegroundColor Yellow
Restart-Service postgresql-x64-18
Start-Sleep -Seconds 3
Write-Host "✅ PostgreSQL reiniciado`n" -ForegroundColor Green

# Verify
Write-Host "🔍 Verificando conexión..." -ForegroundColor Yellow
$listening = netstat -an | Select-String ":5432"
if ($listening) {
    Write-Host "✅ PostgreSQL escuchando en puerto 5432`n" -ForegroundColor Green
    Write-Host $listening
} else {
    Write-Host "❌ PostgreSQL NO está escuchando en puerto 5432`n" -ForegroundColor Red
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "✅ Configuración completada" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "📝 Próximos pasos:" -ForegroundColor Yellow
Write-Host "1. Crear base de datos: psql -U postgres" -ForegroundColor White
Write-Host "2. Ejecutar: CREATE DATABASE salesforce_admin_dev;" -ForegroundColor White
Write-Host "3. Ejecutar: CREATE USER admin WITH PASSWORD 'dev_password';" -ForegroundColor White
Write-Host "4. Ejecutar: GRANT ALL PRIVILEGES ON DATABASE salesforce_admin_dev TO admin;" -ForegroundColor White
Write-Host "5. Ejecutar migraciones: alembic upgrade head`n" -ForegroundColor White

# List PostgreSQL Databases
# Run this to see all databases

$psql = "C:\Program Files\PostgreSQL\18\bin\psql.exe"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "📊 Listando Bases de Datos PostgreSQL" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Conectando a PostgreSQL..." -ForegroundColor Yellow
Write-Host "(Te pedirá la contraseña de postgres)`n" -ForegroundColor Gray

& $psql -U postgres -c "\l"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Bases de datos listadas arriba" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "📝 Busca bases de datos con nombres como:" -ForegroundColor Yellow
Write-Host "  - salesforce_admin" -ForegroundColor White
Write-Host "  - salesforce_admin_dev" -ForegroundColor White
Write-Host "  - admin_salesforce" -ForegroundColor White
Write-Host "  - salesforce" -ForegroundColor White
Write-Host "`nLa que NO sea 'salesforce_admin_dev' es probablemente la original.`n" -ForegroundColor Gray

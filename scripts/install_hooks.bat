@echo off
echo Instalando Git Hooks...

copy "scripts\pre-commit" ".git\hooks\pre-commit"
echo.

echo Permisos de ejecucion...
REM En Windows, git bash suele manejar esto, pero nos aseguramos que el archivo exista.
if exist ".git\hooks\pre-commit" (
    echo ✅ Hook 'pre-commit' instalado correctamente en .git/hooks/
    echo Ahora cada 'git commit' ejecutara los tests automaticamente.
) else (
    echo ❌ Hubo un error al copiar el archivo. Verifica permisos.
)

pause

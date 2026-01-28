@echo off
echo ==========================================
echo 🧪 EJECUTANDO VERIFICACION PRE-COMMIT
echo ==========================================

echo.
echo [1/3] Verificando Estilo de Codigo (Linting)...
REM Aqui podriamos agregar ruff o flake8 en el futuro
echo (Saltado - No configurado aun)

echo.
echo [2/3] Ejecutando Tests Unitarios...
python -m pytest tests/unit/ -q
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ FALLO EN TESTS UNITARIOS
    exit /b 1
)

echo.
echo [3/3] Ejecutando Tests de Integracion...
python -m pytest tests/e2e/ -q
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ FALLO EN TESTS E2E
    exit /b 1
)

echo.
echo ==========================================
echo ✅ TODO OK. LISTO PARA COMMIT/PUSH.
echo ==========================================
exit /b 0

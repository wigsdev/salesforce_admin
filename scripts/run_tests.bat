@echo off
echo ==========================================
echo 🧪 EJECUTANDO VERIFICACION DE CALIDAD TOTAL
echo ==========================================

echo.
echo [1/3] Verificando Estilo y Formato (Linting)...

REM 1. Auto-Formateo con Black
echo    - Ejecutando Black (Auto-Format)...
python -m black .
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ FALLO EN BLACK
    exit /b 1
)

REM 2. Linting rapido con Ruff
echo    - Ejecutando Ruff (Linter)...
python -m ruff check . --fix
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ FALLO EN RUFF
    exit /b 1
)

echo ✅ Codigo Limpio y Formateado.

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
echo ✅ CALIDAD EXCELENTE. LISTO PARA COMMIT.
echo ==========================================
exit /b 0

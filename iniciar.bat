@echo off
title Barcode Ticket Generator
echo ============================================
echo   Barcode Ticket Generator
echo ============================================
echo.

REM Verificar si Python esta instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado.
    echo Descarga Python desde: https://www.python.org/downloads/
    echo Asegurate de marcar "Add Python to PATH" al instalar.
    echo.
    pause
    exit /b 1
)

REM Instalar dependencias si no existe el entorno
if not exist "venv" (
    echo [1/3] Creando entorno virtual...
    python -m venv venv
)

echo [2/3] Instalando dependencias...
call venv\Scripts\activate.bat
pip install -r requirements.txt --quiet

echo [3/3] Iniciando servidor...
echo.
echo ============================================
echo   Abre en tu navegador: http://127.0.0.1:8005
echo   Para cerrar: presiona Ctrl+C en esta ventana
echo ============================================
echo.
python main.py
pause

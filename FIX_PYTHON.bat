@echo off
echo ========================================
echo OpenClaw Agent - Python Repair Tool
echo ========================================
echo.

echo [1/3] Checking Python...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python is not recognized.
    echo Please REINSTALL Python from python.org and check "Add Python to PATH".
    pause
    exit /b
)

echo.
echo [2/3] Checking pip...
python -m pip --version
if %errorlevel% neq 0 (
    echo [ERROR] pip is missing or broken.
    echo Attempting to install pip...
    python -m ensurepip --default-pip
    if %errorlevel% neq 0 (
        echo [FATAL] Could not install pip automatically.
        echo Please REINSTALL Python and ensure "pip" feature is selected.
        pause
        exit /b
    )
)

echo.
echo [3/3] Installing Dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% == 0 (
    echo.
    echo [SUCCESS] All dependencies installed!
    echo You can now run the agent:
    echo   python agent.py --once --agent0
) else (
    echo.
    echo [ERROR] Failed to install dependencies.
    echo Please check your internet connection or try running as Administrator.
)

echo.
pause

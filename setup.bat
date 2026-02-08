@echo off
echo ========================================
echo OpenClaw Agent - Python Setup Checker
echo ========================================
echo.

echo [1/3] Checking for Python installation...
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo [OK] Python is installed!
    python --version
    echo.
    echo [2/3] Checking pip...
    python -m pip --version
    if %errorlevel% == 0 (
        echo [OK] pip is working!
        echo.
        echo [3/3] Installing dependencies...
        python -m pip install web3==6.15.1 eth-account==0.11.0 python-dotenv==1.0.0 requests==2.31.0 requests-oauthlib==1.3.1
        echo.
        echo ========================================
        echo Setup Complete! You can now run:
        echo   python agent.py --once --agent0
        echo ========================================
    ) else (
        echo [ERROR] pip is not working
        echo Please reinstall Python and check "Add to PATH"
    )
) else (
    echo [X] Python is NOT installed
    echo.
    echo Please follow these steps:
    echo 1. Go to: https://www.python.org/downloads/
    echo 2. Download Python 3.11 or later
    echo 3. RUN the installer
    echo 4. CHECK the box: "Add Python to PATH"
    echo 5. Click "Install Now"
    echo 6. After installation, run this script again
    echo.
    echo Opening Python download page in your browser...
    start https://www.python.org/downloads/
)

echo.
pause

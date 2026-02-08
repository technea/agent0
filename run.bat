@echo off
echo ========================================
echo OpenClaw Agent - Quick Start
echo ========================================
echo.

if not exist .env (
    echo [SETUP NEEDED] Creating .env file...
    copy .env.example .env
    echo.
    echo Please edit .env file and add:
    echo   - RPC_URL
    echo   - PRIVATE_KEY
    echo.
    echo Opening .env in Notepad...
    notepad .env
    echo.
    echo After saving .env, run this script again.
    pause
    exit
)

echo [OK] .env file exists
echo.
echo Choose your option:
echo   1. Test once (basic mode)
echo   2. Test once (with Agent0/ERC-8004) [RECOMMENDED]
echo   3. Run continuously (every 20 minutes)
echo   4. Run continuously with Agent0
echo   5. Custom interval
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo Running: python agent.py --once
    python agent.py --once
) else if "%choice%"=="2" (
    echo.
    echo Running: python agent.py --once --agent0
    python agent.py --once --agent0
) else if "%choice%"=="3" (
    echo.
    echo Running: python agent.py
    python agent.py
) else if "%choice%"=="4" (
    echo.
    echo Running: python agent.py --agent0
    python agent.py --agent0
) else if "%choice%"=="5" (
    set /p interval="Enter interval in minutes: "
    echo.
    echo Running: python agent.py --agent0 --interval %interval%
    python agent.py --agent0 --interval %interval%
) else (
    echo Invalid choice!
)

echo.
pause

@echo off
REM Build script for Windows
REM This creates the executable and optionally the installer

echo ================================================
echo Genre-Based File Organizer - Build Script
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo PyInstaller is not installed. Installing...
    pip install pyinstaller
    if errorlevel 1 (
        echo Failed to install PyInstaller
        pause
        exit /b 1
    )
)

echo.
echo Building executable...
echo This may take several minutes...
echo.

REM Run the build script
python build_exe.py

if errorlevel 1 (
    echo.
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo ================================================
echo Build completed successfully!
echo ================================================
echo.
echo Executable location: dist\GenreFileOrganizer.exe
echo.
echo Next steps:
echo   1. Test the executable: dist\GenreFileOrganizer.exe
echo   2. Create installer (optional):
echo      - Install Inno Setup from https://jrsoftware.org/isdl.php
echo      - Compile installer.iss with Inno Setup
echo   3. Distribute the setup file or the exe directly
echo.

pause

@echo off
REM Build script for Windows - Creates Self-Contained Executable
REM No Python or dependencies needed for end users!

echo ========================================================
echo Genre-Based File Organizer - Professional Build System
echo ========================================================
echo.
echo Creating SELF-CONTAINED executable (Chrome/VS Code style)
echo   - ONE FILE with everything bundled
echo   - NO Python installation required for users
echo   - NO dependency installations needed
echo.
echo ========================================================
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
echo ========================================================
echo SUCCESS! Self-Contained Executable Created
echo ========================================================
echo.
echo Executable location: dist\GenreFileOrganizer.exe
echo.
echo *** THIS .EXE IS COMPLETELY STANDALONE ***
echo   - Users can run it WITHOUT installing Python
echo   - All dependencies are BUNDLED INSIDE
echo   - Just like downloading Chrome or VS Code!
echo.
echo Next steps:
echo   1. Test on a clean machine (without Python)
echo   2. Create installer (optional):
echo      - Install Inno Setup from https://jrsoftware.org/isdl.php
echo      - Compile installer.iss with Inno Setup
echo   3. Distribute the setup file to users
echo.

pause

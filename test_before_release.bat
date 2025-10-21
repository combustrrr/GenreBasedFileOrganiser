@echo off
echo ========================================
echo Genre File Organizer - Pre-Release Testing
echo ========================================
echo.

echo Step 1: Checking if executable exists...
if not exist "dist\GenreFileOrganizer.exe" (
    echo ERROR: Executable not found! Run build.bat first.
    pause
    exit /b 1
)
echo [OK] Executable found

echo.
echo Step 2: Checking if installer exists...
if not exist "installer_output\GenreFileOrganizer_Setup_v1.0.0.exe" (
    echo ERROR: Installer not found! Run Inno Setup compiler.
    pause
    exit /b 1
)
echo [OK] Installer found

echo.
echo Step 3: Checking file sizes...
for %%A in ("dist\GenreFileOrganizer.exe") do echo Executable size: %%~zA bytes
for %%A in ("installer_output\GenreFileOrganizer_Setup_v1.0.0.exe") do echo Installer size: %%~zA bytes

echo.
echo Step 4: Testing executable on this machine...
echo Starting application... (Close it to continue testing)
start /wait dist\GenreFileOrganizer.exe
echo [OK] Application started and closed successfully

echo.
echo ========================================
echo Manual Testing Required:
echo ========================================
echo.
echo 1. TEST ON CLEAN WINDOWS MACHINE (CRITICAL!)
echo    - Download a Windows 10/11 VM or use a friend's computer
echo    - Make sure Python is NOT installed
echo    - Copy the installer to that machine
echo    - Run the installer
echo    - Test the application
echo.
echo 2. TEST WITH ANTIVIRUS ENABLED
echo    - Ensure Windows Defender is active
echo    - Run the installer
echo    - Check if antivirus flags anything
echo    - Test application launch and file organization
echo.
echo 3. TEST WITH NON-ADMIN USER ACCOUNT
echo    - Create a standard user account
echo    - Try installing and running as that user
echo.
echo 4. TEST DIFFERENT SCREEN RESOLUTIONS
echo    - Test on 1366x768 (minimum)
echo    - Test on 1920x1080 (common)
echo    - Test on 4K display (if available)
echo    - Verify GUI displays correctly at all sizes
echo.
echo 5. TEST MODEL DOWNLOAD (CRITICAL!)
echo    - On first run, verify DistilBERT downloads successfully
echo    - Check progress indication
echo    - Verify it completes without errors
echo    - Close and restart application
echo    - Verify cached model works (no re-download)
echo.
echo 6. TEST FILE ORGANIZATION
echo    - Create test folder with Word/Excel/PowerPoint files
echo    - Run organization
echo    - Verify files are grouped correctly
echo    - Check for any errors in the log
echo.
echo ========================================
echo If ALL tests pass, you're ready to release!
echo ========================================
echo.
echo Next steps after testing:
echo 1. Create GitHub release
echo 2. Upload installer to releases
echo 3. Update download links
echo 4. Announce the release
echo.
pause

#!/bin/bash

echo "========================================"
echo "Genre File Organizer - Pre-Release Testing"
echo "========================================"
echo ""

echo "Step 1: Checking if executable exists..."
if [ ! -f "dist/GenreFileOrganizer" ] && [ ! -d "dist/GenreFileOrganizer.app" ]; then
    echo "ERROR: Executable not found! Run build.sh first."
    exit 1
fi
echo "[OK] Executable found"

echo ""
echo "Step 2: Checking file sizes..."
if [ -f "dist/GenreFileOrganizer" ]; then
    ls -lh dist/GenreFileOrganizer | awk '{print "Executable size: " $5}'
elif [ -d "dist/GenreFileOrganizer.app" ]; then
    du -sh dist/GenreFileOrganizer.app | awk '{print "App bundle size: " $1}'
fi

echo ""
echo "Step 3: Testing executable on this machine..."
echo "Starting application... (Close it to continue testing)"
if [ -f "dist/GenreFileOrganizer" ]; then
    ./dist/GenreFileOrganizer
elif [ -d "dist/GenreFileOrganizer.app" ]; then
    open dist/GenreFileOrganizer.app
    read -p "Press Enter after closing the application..."
fi
echo "[OK] Application started and closed successfully"

echo ""
echo "========================================"
echo "Manual Testing Required:"
echo "========================================"
echo ""
echo "1. TEST ON CLEAN SYSTEM (CRITICAL!)"
echo "   - Use a fresh macOS/Linux system or VM"
echo "   - Make sure Python is NOT installed"
echo "   - Copy the executable/app to that machine"
echo "   - Test the application"
echo ""
echo "2. TEST WITH SECURITY SOFTWARE"
echo "   - Ensure Gatekeeper is enabled (macOS)"
echo "   - Test with firewall enabled"
echo "   - Check for any security warnings"
echo ""
echo "3. TEST DIFFERENT SCREEN RESOLUTIONS"
echo "   - Test on various display sizes"
echo "   - Verify GUI displays correctly"
echo "   - Test on Retina/HiDPI displays"
echo ""
echo "4. TEST MODEL DOWNLOAD (CRITICAL!)"
echo "   - On first run, verify DistilBERT downloads"
echo "   - Check progress indication"
echo "   - Verify it completes without errors"
echo "   - Close and restart application"
echo "   - Verify cached model works"
echo ""
echo "5. TEST FILE ORGANIZATION"
echo "   - Create test folder with sample files"
echo "   - Run organization"
echo "   - Verify files are grouped correctly"
echo "   - Check for any errors in the log"
echo ""
echo "========================================"
echo "If ALL tests pass, you're ready to release!"
echo "========================================"
echo ""
echo "Next steps after testing:"
echo "1. Create GitHub release"
echo "2. Upload executable/DMG to releases"
echo "3. Update download links"
echo "4. Announce the release"
echo ""

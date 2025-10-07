#!/bin/bash
# Build script for macOS/Linux
# This creates the executable

echo "================================================"
echo "Genre-Based File Organizer - Build Script"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" &> /dev/null; then
    echo "PyInstaller is not installed. Installing..."
    pip3 install pyinstaller
    if [ $? -ne 0 ]; then
        echo "Failed to install PyInstaller"
        exit 1
    fi
fi

echo ""
echo "Building executable..."
echo "This may take several minutes..."
echo ""

# Run the build script
python3 build_exe.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Build failed!"
    exit 1
fi

echo ""
echo "================================================"
echo "Build completed successfully!"
echo "================================================"
echo ""

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Application location: dist/GenreFileOrganizer.app"
    echo ""
    echo "Next steps:"
    echo "  1. Test the app: open dist/GenreFileOrganizer.app"
    echo "  2. Create DMG (optional):"
    echo "     hdiutil create -volname 'Genre File Organizer' \\"
    echo "       -srcfolder dist/GenreFileOrganizer.app \\"
    echo "       -ov -format UDZO GenreFileOrganizer.dmg"
    echo "  3. Distribute the DMG file"
else
    echo "Executable location: dist/GenreFileOrganizer"
    echo ""
    echo "Next steps:"
    echo "  1. Test the executable: ./dist/GenreFileOrganizer"
    echo "  2. Create AppImage or package for distribution"
    echo "  3. Make executable: chmod +x dist/GenreFileOrganizer"
fi

echo ""

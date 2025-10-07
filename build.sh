#!/bin/bash
# Build script for macOS/Linux - Creates Self-Contained Executable
# No Python or dependencies needed for end users!

echo "========================================================"
echo "Genre-Based File Organizer - Professional Build System"
echo "========================================================"
echo ""
echo "Creating SELF-CONTAINED executable (Chrome/VS Code style)"
echo "  - ONE FILE with everything bundled"
echo "  - NO Python installation required for users"
echo "  - NO dependency installations needed"
echo ""
echo "========================================================"
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
echo "========================================================"
echo "SUCCESS! Self-Contained Executable Created"
echo "========================================================"
echo ""

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Application location: dist/GenreFileOrganizer.app"
    echo ""
    echo "*** THIS .APP IS COMPLETELY STANDALONE ***"
    echo "  - Users can run it WITHOUT installing Python"
    echo "  - All dependencies are BUNDLED INSIDE"
    echo "  - Just like downloading Chrome or VS Code!"
    echo ""
    echo "Next steps:"
    echo "  1. Test the app: open dist/GenreFileOrganizer.app"
    echo "  2. Create DMG (optional):"
    echo "     hdiutil create -volname 'Genre File Organizer' \\"
    echo "       -srcfolder dist/GenreFileOrganizer.app \\"
    echo "       -ov -format UDZO GenreFileOrganizer.dmg"
    echo "  3. Distribute the DMG file to users"
else
    echo "Executable location: dist/GenreFileOrganizer"
    echo ""
    echo "*** THIS BINARY IS COMPLETELY STANDALONE ***"
    echo "  - Users can run it WITHOUT installing Python"
    echo "  - All dependencies are BUNDLED INSIDE"
    echo "  - Just like downloading Chrome or VS Code!"
    echo ""
    echo "Next steps:"
    echo "  1. Make executable: chmod +x dist/GenreFileOrganizer"
    echo "  2. Test the executable: ./dist/GenreFileOrganizer"
    echo "  3. Create AppImage or package for distribution"
fi

echo ""

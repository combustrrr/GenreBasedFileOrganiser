# Building Standalone Executable

This document explains how to build and distribute a standalone executable (.exe) file for the Genre-Based File Organizer.

## Prerequisites

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Building the Executable

### Method 1: Using the Build Script (Recommended)

Simply run the build script:

```bash
python build_exe.py
```

This will:
- Create a standalone executable in the `dist/` folder
- Bundle all required dependencies
- Create a single file that can be distributed

**Output:**
- Windows: `dist/GenreFileOrganizer.exe`
- macOS: `dist/GenreFileOrganizer.app`
- Linux: `dist/GenreFileOrganizer`

### Method 2: Manual PyInstaller Command

For Windows:
```bash
pyinstaller --name=GenreFileOrganizer --onefile --windowed ^
  --collect-all=transformers --collect-all=torch ^
  --hidden-import=sklearn.utils._weight_vector ^
  --hidden-import=sklearn.neighbors._typedefs ^
  --hidden-import=sklearn.tree._utils ^
  main.py
```

For macOS/Linux:
```bash
pyinstaller --name=GenreFileOrganizer --onefile --windowed \
  --collect-all=transformers --collect-all=torch \
  --hidden-import=sklearn.utils._weight_vector \
  --hidden-import=sklearn.neighbors._typedefs \
  --hidden-import=sklearn.tree._utils \
  main.py
```

## Distribution

### For Windows Users

1. Build the executable using the instructions above
2. The file `GenreFileOrganizer.exe` will be in the `dist/` folder
3. Distribute this single .exe file
4. Users can double-click to run (no Python installation needed)

**Important Notes:**
- First run will download DistilBERT model (~250MB from internet)
- Executable size: ~100-200MB (includes Python + dependencies)
- Windows may show security warning (normal for unsigned executables)

### For macOS Users

1. Build using the build script
2. Distribute `GenreFileOrganizer.app` from the `dist/` folder
3. Users can drag to Applications folder
4. May need to allow in Security & Privacy settings

### For Linux Users

1. Build the executable
2. Distribute the `GenreFileOrganizer` file from `dist/`
3. Users need to make it executable: `chmod +x GenreFileOrganizer`
4. Run with: `./GenreFileOrganizer`

## File Size Reduction

The executable can be large (~100-200MB). To reduce size:

1. **Use UPX compression** (optional):
```bash
pip install pyinstaller[encryption]
```

Add `--upx-dir=/path/to/upx` to PyInstaller command

2. **Exclude unnecessary modules**:
Already done in build script (excludes matplotlib, pandas)

3. **Consider installer package**:
Use NSIS (Windows), DMG (macOS), or AppImage (Linux) for better compression

## Creating an Installer (Advanced)

### Windows Installer (NSIS)

1. Install NSIS: https://nsis.sourceforge.io/
2. Create installer script (see `installer.nsi` example below)
3. Compile with NSIS

Example `installer.nsi`:
```nsis
!define APPNAME "Genre File Organizer"
!define COMPANYNAME "GenreOrganizer"
!define DESCRIPTION "Intelligent document organizer using semantic clustering"
!define VERSIONMAJOR 1
!define VERSIONMINOR 0
!define VERSIONBUILD 0

OutFile "GenreFileOrganizer_Setup.exe"
InstallDir "$PROGRAMFILES\${APPNAME}"

Page directory
Page instfiles

Section "Install"
    SetOutPath $INSTDIR
    File "dist\GenreFileOrganizer.exe"
    WriteUninstaller "$INSTDIR\uninstall.exe"
    
    CreateShortCut "$DESKTOP\Genre File Organizer.lnk" "$INSTDIR\GenreFileOrganizer.exe"
    CreateShortCut "$SMPROGRAMS\Genre File Organizer.lnk" "$INSTDIR\GenreFileOrganizer.exe"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\GenreFileOrganizer.exe"
    Delete "$INSTDIR\uninstall.exe"
    Delete "$DESKTOP\Genre File Organizer.lnk"
    Delete "$SMPROGRAMS\Genre File Organizer.lnk"
    RMDir "$INSTDIR"
SectionEnd
```

### macOS DMG

```bash
# Create DMG file
hdiutil create -volname "Genre File Organizer" \
  -srcfolder dist/GenreFileOrganizer.app \
  -ov -format UDZO GenreFileOrganizer.dmg
```

### Linux AppImage

Use `pyinstaller-appimage` or create manually with `appimagetool`

## Troubleshooting

### "Failed to execute script" error
- Make sure all dependencies are included
- Check `--hidden-import` flags for missing modules
- Run executable from command line to see error details

### Large file size
- Executable includes Python interpreter and all dependencies
- Normal size: 100-200MB
- Use compression or installer for distribution

### Anti-virus false positives
- Common with PyInstaller executables
- Consider code signing certificate (Windows)
- Submit to anti-virus vendors for whitelisting

### Model download on first run
- Executable needs internet connection on first run
- Downloads DistilBERT model (~250MB)
- Cached for subsequent runs

## Pre-built Executables

If you don't want to build yourself, request pre-built executables:

1. Check the Releases page on GitHub
2. Download for your platform:
   - Windows: `GenreFileOrganizer_Windows.exe`
   - macOS: `GenreFileOrganizer_macOS.dmg`
   - Linux: `GenreFileOrganizer_Linux.AppImage`

## Testing the Executable

Before distribution:

1. Test on a clean machine without Python
2. Test with different file types
3. Test with various folder sizes
4. Verify model download works
5. Check logging functionality

## Support

For build issues:
- Ensure PyInstaller version: `pip install --upgrade pyinstaller`
- Check PyInstaller docs: https://pyinstaller.readthedocs.io/
- Review build logs in `build/` folder

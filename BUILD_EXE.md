# Building Standalone Executable

This document explains how to build and distribute a standalone executable (.exe) file for the Genre-Based File Organizer, following professional software development practices.

## Quick Start

### Windows
```batch
build.bat
```

### macOS/Linux
```bash
chmod +x build.sh
./build.sh
```

## Method 1: Using PyInstaller with Spec File (Recommended)

This method uses a pre-configured spec file for professional builds.

### Prerequisites

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Building

**Option A: Using build script (Recommended)**
```bash
python build_exe.py
```

**Option B: Using spec file directly**
```bash
pyinstaller GenreFileOrganizer.spec
```

**Option C: Simple build**
```bash
python build_exe.py --simple
```

### Output
- Windows: `dist/GenreFileOrganizer.exe`
- macOS: `dist/GenreFileOrganizer.app`
- Linux: `dist/GenreFileOrganizer`

## Method 2: Using auto-py-to-exe (GUI Interface)

For users who prefer a graphical interface:

### Installation
```bash
pip install auto-py-to-exe
```

### Launch GUI
```bash
python build_exe.py --auto-gui
# OR
auto-py-to-exe
```

### Configuration in GUI
1. **Script Location**: Browse to `main.py`
2. **One File**: Select "One File"
3. **Console Window**: Select "Window Based (hide the console)"
4. **Icon**: (Optional) Add an icon file
5. **Additional Files**: Add `README.md`
6. **Hidden Imports**: Add:
   - `sklearn.utils._weight_vector`
   - `sklearn.neighbors._typedefs`
   - `sklearn.tree._utils`
7. Click **"CONVERT .PY TO .EXE"**

## Method 3: Creating a Windows Installer (Inno Setup)

After building the executable, create a professional installer.

### Prerequisites
1. Build the executable first (see Method 1)
2. Download and install Inno Setup: https://jrsoftware.org/isdl.php

### Creating Installer

1. **Compile the installer script:**
   - Open Inno Setup Compiler
   - Open `installer.iss`
   - Click Build → Compile
   - OR use command line:
     ```bash
     "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
     ```

2. **Output:**
   - `installer_output/GenreFileOrganizer_Setup_v1.0.0.exe`

3. **Features:**
   - Professional installation wizard
   - Desktop shortcut creation
   - Start menu integration
   - Uninstaller included
   - Version information
   - License agreement

### Customizing the Installer

Edit `installer.iss` to customize:
- Application name and version
- Installation directory
- File associations
- Registry entries
- Custom icons

## Advanced Configuration

### Spec File Customization

Edit `GenreFileOrganizer.spec` to:

**Add data files:**
```python
datas=[
    ('README.md', '.'),
    ('config.ini', '.'),
    ('icons/*', 'icons'),
],
```

**Add hidden imports:**
```python
hiddenimports=[
    'your.module.here',
],
```

**Add/remove exclusions:**
```python
excludes=[
    'matplotlib',
    'pandas',
],
```

**Add an icon:**
```python
icon='app.ico',
```

### Version Information

The `version_info.txt` file contains Windows version metadata:
- File version
- Product version
- Company name
- File description
- Copyright

Edit this file to update version information.

## Building for Different Platforms

### Windows (.exe)

```bash
# On Windows machine
python build_exe.py
```

Creates: `dist/GenreFileOrganizer.exe`

**Installer (Inno Setup):**
```bash
# After building .exe
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
```

Creates: `installer_output/GenreFileOrganizer_Setup_v1.0.0.exe`

### macOS (.app)

```bash
# On macOS machine
python build_exe.py
```

Creates: `dist/GenreFileOrganizer.app`

**DMG Creation:**
```bash
hdiutil create -volname "Genre File Organizer" \
  -srcfolder dist/GenreFileOrganizer.app \
  -ov -format UDZO GenreFileOrganizer.dmg
```

### Linux (Binary)

```bash
# On Linux machine
python build_exe.py
```

Creates: `dist/GenreFileOrganizer`

**AppImage Creation:**
Use `appimagetool` or create a package for your distribution.

## File Size Optimization

### Basic Optimization (Already Applied)
- Excluded matplotlib, pandas, IPython
- Using --onefile for single executable
- UPX compression enabled

### Additional Optimization

**1. Exclude more unused modules:**
Edit spec file, add to `excludes`:
```python
excludes=[
    'matplotlib',
    'pandas',
    'IPython',
    'jupyter',
    'PIL',
],
```

**2. Use UPX compression:**
Already enabled in spec file. For manual control:
```bash
pip install pyinstaller[encryption]
```

**3. Exclude unnecessary torch components:**
If file size is too large, consider using CPU-only torch:
```bash
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

## Distribution Guide

### For Windows Users

**Option 1: Installer (Recommended)**
1. Build exe: `python build_exe.py`
2. Create installer: Compile `installer.iss`
3. Distribute: `GenreFileOrganizer_Setup_v1.0.0.exe`
4. Users run installer → application installs

**Option 2: Standalone EXE**
1. Build exe: `python build_exe.py`
2. Zip the exe if needed
3. Distribute: `GenreFileOrganizer.exe`
4. Users extract and run

### For macOS Users

**Option 1: DMG (Recommended)**
1. Build app: `python build_exe.py`
2. Create DMG: `hdiutil create ...`
3. Distribute: `GenreFileOrganizer.dmg`
4. Users open DMG → drag to Applications

**Option 2: App Bundle**
1. Build app: `python build_exe.py`
2. Zip: `zip -r GenreFileOrganizer.zip dist/GenreFileOrganizer.app`
3. Distribute zip file

### For Linux Users

**Option 1: AppImage**
1. Build binary
2. Create AppImage with `appimagetool`
3. Distribute AppImage
4. Users make executable and run

**Option 2: Distribution Package**
1. Create .deb or .rpm package
2. Distribute package
3. Users install via package manager

## Testing the Build

### Pre-Distribution Checklist

- [ ] Test on clean machine without Python
- [ ] Test with different file types (.docx, .xlsx, .pptx)
- [ ] Test with various folder sizes (10, 100, 1000 files)
- [ ] Verify model download works on first run
- [ ] Check logging functionality
- [ ] Test GUI responsiveness
- [ ] Verify error handling
- [ ] Check file organization accuracy

### Clean Machine Testing

**Windows:**
1. Create Windows VM or use clean Windows PC
2. Do NOT install Python
3. Run the installer or .exe
4. Test all functionality

**macOS:**
1. Create macOS VM or use clean Mac
2. Do NOT install Python
3. Install .app or open DMG
4. Test all functionality

**Linux:**
1. Use Docker or VM
2. Do NOT install Python
3. Run binary or AppImage
4. Test all functionality

## Troubleshooting

### Common Build Errors

**"Failed to execute script" error:**
```bash
# Solution: Add hidden imports
# Edit GenreFileOrganizer.spec, add to hiddenimports list
```

**"Module not found" during build:**
```bash
# Solution: Add to hidden imports or collect-all
# Edit spec file
```

**Large file size (>500MB):**
```bash
# Solution 1: Exclude unused modules
# Solution 2: Use CPU-only torch
# Solution 3: Remove transformers cache before building
```

### Runtime Errors

**"Model download failed":**
```bash
# Ensure internet connection on first run
# Model will be cached: ~/.cache/huggingface/
```

**"Permission denied":**
```bash
# Windows: Run as Administrator
# macOS/Linux: chmod +x GenreFileOrganizer
```

**Anti-virus false positive:**
```bash
# Common with PyInstaller executables
# Solution: Code signing (Windows) or submit to AV vendors
```

## Code Signing (Optional but Recommended)

### Windows Code Signing
1. Obtain code signing certificate
2. Sign exe: `signtool sign /f cert.pfx /p password GenreFileOrganizer.exe`
3. Benefits: Removes security warnings, trusted by Windows

### macOS Code Signing
1. Enroll in Apple Developer Program
2. Get certificate from Apple
3. Sign app: `codesign --deep --force --verify --verbose --sign "Developer ID" GenreFileOrganizer.app`
4. Notarize for macOS 10.15+

## Continuous Integration

### GitHub Actions Example

```yaml
name: Build Executables

on: [push, release]

jobs:
  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: pip install pyinstaller
      - run: python build_exe.py
      - uses: actions/upload-artifact@v2
        with:
          name: windows-exe
          path: dist/GenreFileOrganizer.exe
  
  build-macos:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: pip install pyinstaller
      - run: python build_exe.py
      - uses: actions/upload-artifact@v2
        with:
          name: macos-app
          path: dist/GenreFileOrganizer.app
```

## Support

For build issues:
- Check PyInstaller documentation: https://pyinstaller.readthedocs.io/
- Review build logs in `build/` folder
- Test with `--simple` flag first
- Check hidden imports for missing modules

## Summary

**Quick Build Commands:**
```bash
# Standard build
python build_exe.py

# Simple build
python build_exe.py --simple

# GUI build tool
python build_exe.py --auto-gui

# Using spec file directly
pyinstaller GenreFileOrganizer.spec

# Create Windows installer
# (After building exe)
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
```

**Output Locations:**
- Executable: `dist/GenreFileOrganizer.exe` (Windows)
- Installer: `installer_output/GenreFileOrganizer_Setup_v1.0.0.exe`
- Build files: `build/` (can be deleted)
- Spec file: `GenreFileOrganizer.spec` (keep for rebuilds)

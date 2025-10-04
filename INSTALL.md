# Installation Guide

This guide provides step-by-step instructions for installing the Genre-Based File Organizer as a standalone application.

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 500MB for models and dependencies

## Installation Methods

### Method 1: Install from Source (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/combustrrr/GenreBasedFileOrganiser.git
   cd GenreBasedFileOrganiser
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the application:**
   ```bash
   pip install -e .
   ```

4. **Verify installation:**
   ```bash
   python check_deps.py
   ```

### Method 2: Install using pip

```bash
pip install -e git+https://github.com/combustrrr/GenreBasedFileOrganiser.git#egg=genre-based-file-organizer
```

## Running the Application

### GUI Mode (Default)

**Option 1: Using the installed command**
```bash
file-organizer-gui
```

**Option 2: Using Python directly**
```bash
python main.py
```

### CLI Mode (Command Line)

For advanced users who prefer command-line interface:
```bash
python organize.py /path/to/files
```

## First Time Setup

When you run the application for the first time:

1. The application will download the DistilBERT model (~250MB)
2. This is a one-time download and will be cached for future use
3. The download may take a few minutes depending on your internet connection

## Creating Desktop Shortcuts

### Windows

1. Create a batch file `file-organizer.bat`:
   ```batch
   @echo off
   cd C:\path\to\GenreBasedFileOrganiser
   call venv\Scripts\activate
   python main.py
   pause
   ```

2. Right-click the batch file → Create shortcut
3. Move the shortcut to your Desktop
4. (Optional) Right-click shortcut → Properties → Change Icon

### macOS

1. Create a script `file-organizer.command`:
   ```bash
   #!/bin/bash
   cd /path/to/GenreBasedFileOrganiser
   source venv/bin/activate
   python main.py
   ```

2. Make it executable:
   ```bash
   chmod +x file-organizer.command
   ```

3. Double-click to run or drag to Desktop/Dock

### Linux

1. Create a desktop entry file `~/.local/share/applications/file-organizer.desktop`:
   ```ini
   [Desktop Entry]
   Type=Application
   Name=Genre-Based File Organizer
   Comment=AI-powered document organizer
   Exec=/path/to/venv/bin/python /path/to/GenreBasedFileOrganiser/main.py
   Terminal=false
   Categories=Utility;Office;
   ```

2. Make it executable:
   ```bash
   chmod +x ~/.local/share/applications/file-organizer.desktop
   ```

## Building Standalone Executable (Optional)

For users who want a standalone executable without Python installation:

### Using PyInstaller

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable:**
   ```bash
   pyinstaller --onefile --windowed --name="FileOrganizer" main.py
   ```

3. **Find the executable:**
   - Windows: `dist\FileOrganizer.exe`
   - macOS: `dist/FileOrganizer.app`
   - Linux: `dist/FileOrganizer`

### Using cx_Freeze

1. **Install cx_Freeze:**
   ```bash
   pip install cx_Freeze
   ```

2. **Create a build script `build.py`:**
   ```python
   from cx_Freeze import setup, Executable
   
   setup(
       name="FileOrganizer",
       version="1.0",
       description="Genre-Based File Organizer",
       executables=[Executable("main.py", base="Win32GUI")]
   )
   ```

3. **Build:**
   ```bash
   python build.py build
   ```

## Troubleshooting

### Common Issues

**Issue: "Module not found" errors**
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

**Issue: "Model download failed"**
```bash
# Solution: Manual model download
python -c "from transformers import DistilBertModel; DistilBertModel.from_pretrained('distilbert-base-uncased')"
```

**Issue: GUI doesn't start**
```bash
# Check if tkinter is installed
python -m tkinter

# If not, install it:
# Ubuntu/Debian: sudo apt-get install python3-tk
# macOS: brew install python-tk
# Windows: tkinter is included with Python
```

**Issue: "Permission denied" errors**
```bash
# Run with appropriate permissions
# On Windows: Run as Administrator
# On macOS/Linux: Check folder permissions
```

### Getting Help

1. Check the logs in the `logs/` folder
2. Review the [USAGE.md](USAGE.md) documentation
3. Visit the [GitHub Issues](https://github.com/combustrrr/GenreBasedFileOrganiser/issues) page

## Uninstallation

To uninstall the application:

```bash
pip uninstall genre-based-file-organizer
```

To completely remove all files:
```bash
rm -rf GenreBasedFileOrganiser  # or delete the folder manually
```

## Updating

To update to the latest version:

```bash
cd GenreBasedFileOrganiser
git pull origin master
pip install -e . --upgrade
```

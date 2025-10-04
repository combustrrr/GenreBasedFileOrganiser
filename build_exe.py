"""
Build script for creating standalone executable using PyInstaller.
Run this script to create a standalone .exe file for Windows.
"""

import PyInstaller.__main__
import os
import sys

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# PyInstaller arguments
args = [
    'main.py',  # Entry point
    '--name=GenreFileOrganizer',  # Name of the executable
    '--onefile',  # Create a single executable file
    '--windowed',  # Don't show console window (GUI app)
    '--add-data=README.md;.',  # Include README
    '--hidden-import=sklearn.utils._weight_vector',  # Include hidden imports
    '--hidden-import=sklearn.neighbors._typedefs',
    '--hidden-import=sklearn.tree._utils',
    '--collect-all=transformers',  # Collect all transformers data
    '--collect-all=torch',  # Collect all torch data
    '--exclude-module=matplotlib',  # Exclude unnecessary modules
    '--exclude-module=pandas',
    '--icon=NONE',  # No icon (can be added later)
]

# Add platform-specific arguments
if sys.platform == 'win32':
    print("Building for Windows...")
elif sys.platform == 'darwin':
    print("Building for macOS...")
    args.append('--osx-bundle-identifier=com.genreorganizer.app')
elif sys.platform.startswith('linux'):
    print("Building for Linux...")

print("Starting build process...")
print("This may take several minutes...")
print("=" * 60)

try:
    PyInstaller.__main__.run(args)
    print("\n" + "=" * 60)
    print("Build completed successfully!")
    print(f"\nExecutable location:")
    if sys.platform == 'win32':
        print(f"  {os.path.join(script_dir, 'dist', 'GenreFileOrganizer.exe')}")
    elif sys.platform == 'darwin':
        print(f"  {os.path.join(script_dir, 'dist', 'GenreFileOrganizer.app')}")
    else:
        print(f"  {os.path.join(script_dir, 'dist', 'GenreFileOrganizer')}")
    print("\nYou can distribute this file to users.")
    print("Note: First run will download DistilBERT model (~250MB)")
    print("=" * 60)
except Exception as e:
    print(f"\nBuild failed: {e}")
    print("\nMake sure PyInstaller is installed:")
    print("  pip install pyinstaller")
    sys.exit(1)

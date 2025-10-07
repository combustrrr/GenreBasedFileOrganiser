"""
Build script for creating standalone executable using PyInstaller.
Run this script to create a standalone .exe file for Windows.

Usage:
    python build_exe.py              # Build using spec file
    python build_exe.py --simple     # Build using simple command
    python build_exe.py --auto-gui   # Launch auto-py-to-exe GUI
"""

import sys
import os
import subprocess

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))


def build_with_spec():
    """Build using the spec file for advanced configuration."""
    print("=" * 60)
    print("Building with spec file (recommended)")
    print("=" * 60)
    
    spec_file = os.path.join(script_dir, 'GenreFileOrganizer.spec')
    
    if not os.path.exists(spec_file):
        print(f"Error: Spec file not found: {spec_file}")
        print("Creating spec file...")
        create_spec_file()
        return
    
    try:
        import PyInstaller.__main__
        PyInstaller.__main__.run([spec_file])
        print_success()
    except Exception as e:
        print(f"\nBuild failed: {e}")
        print("\nMake sure PyInstaller is installed:")
        print("  pip install pyinstaller")
        sys.exit(1)


def build_simple():
    """Build using simple PyInstaller command."""
    print("=" * 60)
    print("Building with simple command")
    print("=" * 60)
    
    try:
        import PyInstaller.__main__
        
        args = [
            'main.py',
            '--name=GenreFileOrganizer',
            '--onefile',
            '--windowed',
            '--add-data=README.md;.' if sys.platform == 'win32' else '--add-data=README.md:.',
            '--hidden-import=sklearn.utils._weight_vector',
            '--hidden-import=sklearn.neighbors._typedefs',
            '--hidden-import=sklearn.tree._utils',
            '--collect-all=transformers',
            '--collect-all=torch',
            '--exclude-module=matplotlib',
            '--exclude-module=pandas',
        ]
        
        # Add platform-specific arguments
        if sys.platform == 'win32':
            print("Building for Windows...")
        elif sys.platform == 'darwin':
            print("Building for macOS...")
            args.append('--osx-bundle-identifier=com.genreorganizer.app')
        elif sys.platform.startswith('linux'):
            print("Building for Linux...")
        
        print("\nStarting build process...")
        print("This may take several minutes...\n")
        
        PyInstaller.__main__.run(args)
        print_success()
        
    except Exception as e:
        print(f"\nBuild failed: {e}")
        print("\nMake sure PyInstaller is installed:")
        print("  pip install pyinstaller")
        sys.exit(1)


def launch_auto_gui():
    """Launch auto-py-to-exe GUI."""
    print("=" * 60)
    print("Launching auto-py-to-exe GUI")
    print("=" * 60)
    
    try:
        subprocess.run(['auto-py-to-exe'], check=True)
    except FileNotFoundError:
        print("\nauto-py-to-exe is not installed.")
        print("Install it with:")
        print("  pip install auto-py-to-exe")
        print("\nThen run:")
        print("  auto-py-to-exe")
        sys.exit(1)
    except Exception as e:
        print(f"\nFailed to launch auto-py-to-exe: {e}")
        sys.exit(1)


def create_spec_file():
    """Create a basic spec file if it doesn't exist."""
    print("Generating spec file...")
    
    try:
        import PyInstaller.__main__
        PyInstaller.__main__.run([
            'main.py',
            '--name=GenreFileOrganizer',
            '--onefile',
            '--windowed',
        ])
        print("\nSpec file created: GenreFileOrganizer.spec")
        print("You can now edit it and run: pyinstaller GenreFileOrganizer.spec")
    except Exception as e:
        print(f"Failed to create spec file: {e}")


def print_success():
    """Print success message."""
    print("\n" + "=" * 60)
    print("Build completed successfully!")
    print("=" * 60)
    print(f"\nExecutable location:")
    
    if sys.platform == 'win32':
        exe_path = os.path.join(script_dir, 'dist', 'GenreFileOrganizer.exe')
        print(f"  {exe_path}")
        print("\nNext steps:")
        print("  1. Test the executable")
        print("  2. Create installer with Inno Setup (see installer.iss)")
        print("  3. Distribute GenreFileOrganizer_Setup.exe")
    elif sys.platform == 'darwin':
        app_path = os.path.join(script_dir, 'dist', 'GenreFileOrganizer.app')
        print(f"  {app_path}")
        print("\nNext steps:")
        print("  1. Test the app")
        print("  2. Create DMG: hdiutil create -volname 'Genre File Organizer' \\")
        print("              -srcfolder dist/GenreFileOrganizer.app \\")
        print("              -ov -format UDZO GenreFileOrganizer.dmg")
    else:
        exe_path = os.path.join(script_dir, 'dist', 'GenreFileOrganizer')
        print(f"  {exe_path}")
        print("\nNext steps:")
        print("  1. Test the executable: ./dist/GenreFileOrganizer")
        print("  2. Create AppImage or package for distribution")
    
    print("\nNote: First run will download DistilBERT model (~250MB)")
    print("=" * 60)


def print_usage():
    """Print usage information."""
    print(__doc__)
    print("\nOptions:")
    print("  (no args)    Build using spec file (recommended)")
    print("  --simple     Build using simple PyInstaller command")
    print("  --auto-gui   Launch auto-py-to-exe GUI")
    print("  --help       Show this help message")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '--help':
            print_usage()
        elif arg == '--simple':
            build_simple()
        elif arg == '--auto-gui':
            launch_auto_gui()
        else:
            print(f"Unknown argument: {arg}")
            print_usage()
            sys.exit(1)
    else:
        # Default: build with spec file
        build_with_spec()


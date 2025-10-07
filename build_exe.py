"""
Build script for creating a SINGLE, SELF-CONTAINED executable.

Creates a professional executable just like Chrome or VS Code:
- ONE FILE with everything bundled inside
- NO Python installation required
- NO separate dependency installations
- ALL libraries embedded (PyTorch, Transformers, FAISS, etc.)

Users simply download and run the .exe - that's it!

Usage:
    python build_exe.py              # Build using spec file (recommended)
    python build_exe.py --simple     # Quick build
    python build_exe.py --auto-gui   # Launch GUI build tool
"""

import sys
import os
import subprocess

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))


def build_with_spec():
    """Build using the spec file for advanced configuration."""
    print("=" * 70)
    print("Building Self-Contained Executable (Chrome/VS Code style)")
    print("=" * 70)
    print("\n📦 Creating ONE file with everything bundled:")
    print("   ✓ Python interpreter")
    print("   ✓ All dependencies (PyTorch, Transformers, FAISS, etc.)")
    print("   ✓ Application code")
    print("   ✓ GUI framework")
    print("\n👤 Users will NOT need to install:")
    print("   ✗ Python")
    print("   ✗ pip packages")
    print("   ✗ Any dependencies")
    print("\n" + "=" * 70)
    
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
    print("=" * 70)
    print("Building Self-Contained Executable (Quick Build)")
    print("=" * 70)
    print("\n📦 Creating ONE file with everything bundled inside")
    print("=" * 70)
    
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
    print("\n" + "=" * 70)
    print("✅ BUILD SUCCESSFUL - Self-Contained Executable Created!")
    print("=" * 70)
    print("\n🎉 You now have a SINGLE FILE with EVERYTHING bundled:")
    print("   • Python interpreter")
    print("   • All libraries (PyTorch, Transformers, FAISS, etc.)")
    print("   • Your application code")
    print("   • GUI framework")
    print("\n📍 Executable location:")
    
    if sys.platform == 'win32':
        exe_path = os.path.join(script_dir, 'dist', 'GenreFileOrganizer.exe')
        print(f"  {exe_path}")
        print("\n🚀 Distribution Ready:")
        print("  • This .exe is COMPLETELY STANDALONE")
        print("  • Users can run it without installing Python")
        print("  • No dependencies needed - everything is inside!")
        print("\n📋 Next steps:")
        print("  1. Test the executable on a clean machine (no Python)")
        print("  2. Create installer with Inno Setup (see installer.iss)")
        print("  3. Distribute GenreFileOrganizer_Setup.exe to users")
    elif sys.platform == 'darwin':
        app_path = os.path.join(script_dir, 'dist', 'GenreFileOrganizer.app')
        print(f"  {app_path}")
        print("\n🚀 Distribution Ready:")
        print("  • This .app is COMPLETELY STANDALONE")
        print("  • Users can run it without installing Python")
        print("  • No dependencies needed - everything is inside!")
        print("\n📋 Next steps:")
        print("  1. Test the app")
        print("  2. Create DMG: hdiutil create -volname 'Genre File Organizer' \\")
        print("              -srcfolder dist/GenreFileOrganizer.app \\")
        print("              -ov -format UDZO GenreFileOrganizer.dmg")
    else:
        exe_path = os.path.join(script_dir, 'dist', 'GenreFileOrganizer')
        print(f"  {exe_path}")
        print("\n🚀 Distribution Ready:")
        print("  • This binary is COMPLETELY STANDALONE")
        print("  • Users can run it without installing Python")
        print("  • No dependencies needed - everything is inside!")
        print("\n📋 Next steps:")
        print("  1. Test the executable: ./dist/GenreFileOrganizer")
        print("  2. Create AppImage or package for distribution")
    
    print("\n💡 Note: First run downloads DistilBERT model (~250MB)")
    print("   After that, model is cached - no downloads needed!")
    print("=" * 70)


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


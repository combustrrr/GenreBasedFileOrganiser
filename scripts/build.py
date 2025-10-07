#!/usr/bin/env python3
"""
Corporate Build Script - Industry Standard Build System
Follows professional software development practices for building executables.
"""
import os
import sys
import shutil
import subprocess
import platform
from pathlib import Path
from datetime import datetime

class BuildSystem:
    """Professional build system for Genre-Based File Organizer."""
    
    def __init__(self):
        self.version = "1.0.0"
        self.build_dir = Path("build")
        self.dist_dir = Path("dist")
        self.installer_output_dir = Path("installer_output")
        self.platform = platform.system()
        
    def print_header(self, message: str):
        """Print formatted header message."""
        print("\n" + "=" * 70)
        print(f"  {message}")
        print("=" * 70 + "\n")
        
    def print_step(self, step_num: int, message: str):
        """Print formatted step message."""
        print(f"[{step_num}/6] {message}...")
        
    def print_success(self, message: str):
        """Print success message."""
        print(f"✓ {message}")
        
    def print_error(self, message: str):
        """Print error message."""
        print(f"✗ ERROR: {message}", file=sys.stderr)
        
    def clean_previous_builds(self):
        """Clean build artifacts from previous builds."""
        self.print_step(1, "Cleaning previous builds")
        
        dirs_to_clean = [self.build_dir, self.dist_dir, Path("__pycache__")]
        
        for dir_path in dirs_to_clean:
            if dir_path.exists():
                shutil.rmtree(dir_path)
                self.print_success(f"Removed {dir_path}")
                
        # Clean .spec file artifacts
        spec_files = list(Path(".").glob("*.spec.bak"))
        for spec_file in spec_files:
            spec_file.unlink()
            
        self.print_success("Build environment cleaned")
        
    def check_dependencies(self):
        """Verify all required dependencies are installed."""
        self.print_step(2, "Checking dependencies")
        
        required_packages = [
            "pyinstaller",
            "torch",
            "transformers",
            "faiss",
            "docx",
            "openpyxl",
            "pptx",
        ]
        
        missing = []
        for package in required_packages:
            try:
                __import__(package)
                self.print_success(f"{package} ✓")
            except ImportError:
                missing.append(package)
                self.print_error(f"{package} NOT FOUND")
                
        if missing:
            self.print_error(f"Missing packages: {', '.join(missing)}")
            self.print_error("Run: pip install -e .[dev,build]")
            return False
            
        self.print_success("All dependencies satisfied")
        return True
        
    def run_tests(self):
        """Run test suite before building."""
        self.print_step(3, "Running tests")
        
        if not Path("test_organizer.py").exists():
            self.print_success("No tests found (skipping)")
            return True
            
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "-v"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                self.print_success("All tests passed")
                return True
            else:
                self.print_error("Tests failed!")
                print(result.stdout)
                print(result.stderr)
                return False
                
        except subprocess.TimeoutExpired:
            self.print_error("Tests timed out")
            return False
        except FileNotFoundError:
            self.print_success("pytest not found (skipping tests)")
            return True
            
    def build_executable(self):
        """Build standalone executable using PyInstaller."""
        self.print_step(4, "Building executable")
        
        # Determine which spec file or script to use
        if Path("GenreFileOrganizer.spec").exists():
            build_command = [
                sys.executable, "-m", "PyInstaller",
                "--clean",
                "--noconfirm",
                "GenreFileOrganizer.spec"
            ]
            self.print_success("Using spec file for build")
        else:
            build_command = [
                sys.executable, "-m", "PyInstaller",
                "--onefile",
                "--windowed",
                "--name=GenreFileOrganizer",
                "main.py"
            ]
            self.print_success("Using simple build (no spec file)")
            
        try:
            result = subprocess.run(
                build_command,
                capture_output=True,
                text=True,
                timeout=600
            )
            
            if result.returncode == 0:
                self.print_success("Executable built successfully")
                return True
            else:
                self.print_error("Build failed!")
                print(result.stdout)
                print(result.stderr)
                return False
                
        except subprocess.TimeoutExpired:
            self.print_error("Build timed out")
            return False
        except Exception as e:
            self.print_error(f"Build error: {e}")
            return False
            
    def verify_build(self):
        """Verify the built executable exists and is valid."""
        self.print_step(5, "Verifying build")
        
        if self.platform == "Windows":
            exe_path = self.dist_dir / "GenreFileOrganizer.exe"
        elif self.platform == "Darwin":
            exe_path = self.dist_dir / "GenreFileOrganizer.app"
        else:
            exe_path = self.dist_dir / "GenreFileOrganizer"
            
        if not exe_path.exists():
            self.print_error(f"Executable not found at {exe_path}")
            return False
            
        # Check file size
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        self.print_success(f"Executable found: {exe_path}")
        self.print_success(f"Size: {size_mb:.1f} MB")
        
        if size_mb < 1:
            self.print_error("Executable seems too small - may be corrupted")
            return False
            
        return True
        
    def create_installer(self):
        """Create professional installer package (Windows only)."""
        self.print_step(6, "Creating installer")
        
        if self.platform != "Windows":
            self.print_success(f"Installer creation not available on {self.platform}")
            self.print_success("Use DMG (macOS) or AppImage (Linux) manually")
            return True
            
        if not Path("installer.iss").exists():
            self.print_success("No installer script found (skipping)")
            return True
            
        # Check for Inno Setup
        inno_paths = [
            r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
            r"C:\Program Files\Inno Setup 6\ISCC.exe",
        ]
        
        iscc_exe = None
        for path in inno_paths:
            if Path(path).exists():
                iscc_exe = path
                break
                
        if not iscc_exe:
            self.print_success("Inno Setup not found (skipping installer)")
            self.print_success("Install from: https://jrsoftware.org/isdl.php")
            return True
            
        try:
            result = subprocess.run(
                [iscc_exe, "installer.iss"],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                self.print_success("Installer created successfully")
                return True
            else:
                self.print_error("Installer creation failed")
                print(result.stdout)
                return False
                
        except subprocess.TimeoutExpired:
            self.print_error("Installer creation timed out")
            return False
        except Exception as e:
            self.print_error(f"Installer creation error: {e}")
            return False
            
    def print_build_summary(self):
        """Print summary of build artifacts."""
        self.print_header("Build Complete!")
        
        print("📦 Build Artifacts:")
        print(f"   Executable:  {self.dist_dir}/")
        
        if self.installer_output_dir.exists():
            print(f"   Installer:   {self.installer_output_dir}/")
            
        print("\n📋 Next Steps:")
        print("   1. Test the executable on a clean system")
        print("   2. Run test_before_release script")
        print("   3. Create GitHub release")
        print("   4. Upload installer for distribution")
        
        print("\n💡 Distribution:")
        print("   See DISTRIBUTION.md for publishing guide")
        
    def build(self):
        """Execute complete build process."""
        self.print_header(f"Genre File Organizer v{self.version} - Professional Build")
        
        print(f"Platform: {self.platform}")
        print(f"Python: {sys.version.split()[0]}")
        print(f"Build Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Step 1: Clean
        self.clean_previous_builds()
        
        # Step 2: Check dependencies
        if not self.check_dependencies():
            sys.exit(1)
            
        # Step 3: Run tests
        if not self.run_tests():
            response = input("\n⚠️  Tests failed. Continue anyway? (y/N): ")
            if response.lower() != 'y':
                sys.exit(1)
                
        # Step 4: Build executable
        if not self.build_executable():
            sys.exit(1)
            
        # Step 5: Verify build
        if not self.verify_build():
            sys.exit(1)
            
        # Step 6: Create installer
        self.create_installer()
        
        # Summary
        self.print_build_summary()
        

def main():
    """Main entry point."""
    builder = BuildSystem()
    
    try:
        builder.build()
    except KeyboardInterrupt:
        print("\n\n⚠️  Build cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

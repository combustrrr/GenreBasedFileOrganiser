#!/usr/bin/env python3
"""
Check if all required dependencies are installed.
"""

import sys

def check_dependencies():
    """Check if all dependencies are installed."""
    missing = []
    
    dependencies = [
        ('torch', 'torch'),
        ('transformers', 'transformers'),
        ('faiss', 'faiss-cpu'),
        ('docx', 'python-docx'),
        ('openpyxl', 'openpyxl'),
        ('pptx', 'python-pptx'),
        ('numpy', 'numpy'),
        ('sklearn', 'scikit-learn'),
    ]
    
    print("Checking dependencies...\n")
    
    for module_name, package_name in dependencies:
        try:
            __import__(module_name)
            print(f"✓ {package_name}")
        except ImportError:
            print(f"✗ {package_name} (missing)")
            missing.append(package_name)
    
    print()
    
    if missing:
        print("Missing dependencies:")
        for pkg in missing:
            print(f"  - {pkg}")
        print("\nInstall with:")
        print(f"  pip install {' '.join(missing)}")
        return False
    else:
        print("✓ All dependencies installed!")
        return True


if __name__ == "__main__":
    success = check_dependencies()
    sys.exit(0 if success else 1)

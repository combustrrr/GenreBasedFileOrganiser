# Contributing to Genre-Based File Organizer

Thank you for your interest in contributing to Genre-Based File Organizer! This document provides guidelines and instructions for contributing to the project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Release Process](#release-process)

## Code of Conduct

We expect all contributors to:
- Be respectful and inclusive
- Focus on constructive feedback
- Prioritize project goals over personal preferences
- Help create a welcoming environment for newcomers

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/GenreBasedFileOrganiser.git
   cd GenreBasedFileOrganiser
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/combustrrr/GenreBasedFileOrganiser.git
   ```

4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git version control

### Installation

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

3. **Verify installation**:
   ```bash
   python check_deps.py
   ```

### Development Tools

Install development dependencies:
```bash
pip install -e ".[dev,build]"
```

This includes:
- `pytest` - Testing framework
- `pytest-cov` - Code coverage
- `black` - Code formatter
- `flake8` - Linter
- `mypy` - Type checker
- `pylint` - Code analysis
- `pyinstaller` - Executable builder

## Project Structure

```
GenreBasedFileOrganiser/
├── .github/
│   └── workflows/           # CI/CD pipelines (future)
├── docs/                    # Documentation (if separated)
├── tests/                   # Test files
│   └── test_organizer.py
├── scripts/                 # Build and utility scripts
│   ├── build.bat
│   ├── build.sh
│   ├── build_exe.py
│   ├── test_before_release.bat
│   └── test_before_release.sh
│
├── Core Modules:
│   ├── main.py             # GUI entry point
│   ├── gui.py              # Tkinter GUI
│   ├── file_organizer.py   # Main orchestration
│   ├── text_extractor.py   # Document text extraction
│   ├── embedding_generator.py  # DistilBERT embeddings
│   ├── clusterer.py        # FAISS clustering
│   ├── organize.py         # CLI interface
│   └── logger.py           # Logging system
│
├── Configuration:
│   ├── pyproject.toml      # Modern Python config
│   ├── setup.py            # Package setup
│   ├── requirements.txt    # Dependencies
│   ├── GenreFileOrganizer.spec  # PyInstaller config
│   ├── installer.iss       # Inno Setup script
│   └── version_info.txt    # Windows version info
│
├── Documentation:
│   ├── README.md
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── BUILD_EXE.md
│   ├── DISTRIBUTION.md
│   ├── USER_EXPERIENCE.md
│   ├── GUI_OVERVIEW.md
│   ├── ARCHITECTURE.md
│   ├── USAGE.md
│   ├── QUICKREF.md
│   ├── INSTALL.md
│   └── TEST_CHECKLIST.md
│
└── Other:
    ├── .gitignore
    ├── LICENSE.txt
    ├── example.py
    └── check_deps.py
```

## Coding Standards

### Python Style Guide

We follow **PEP 8** with these specific guidelines:

1. **Line Length**: Maximum 88 characters (Black default)
2. **Imports**: Organized in groups (standard library, third-party, local)
3. **Naming Conventions**:
   - `snake_case` for functions and variables
   - `PascalCase` for classes
   - `UPPER_CASE` for constants

### Code Formatting

Run Black formatter before committing:
```bash
black .
```

### Linting

Check code quality:
```bash
flake8 .
pylint *.py
```

### Type Hints

Add type hints where appropriate:
```python
def process_file(file_path: str, output_dir: str) -> dict:
    """Process a single file and return results."""
    pass
```

### Docstrings

Use clear docstrings for all public functions:
```python
def extract_text(file_path: str) -> str:
    """
    Extract text content from a document file.
    
    Args:
        file_path: Absolute path to the document file
        
    Returns:
        Extracted text content as a string
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format is unsupported
    """
    pass
```

## Testing

### Running Tests

Run all tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=. --cov-report=html
```

### Writing Tests

1. **Create test files** in `tests/` directory
2. **Name test files** with `test_` prefix
3. **Name test functions** with `test_` prefix

Example:
```python
# tests/test_extractor.py
import pytest
from text_extractor import TextExtractor

def test_extract_from_docx():
    """Test Word document text extraction."""
    extractor = TextExtractor()
    text = extractor.extract("sample.docx")
    assert isinstance(text, str)
    assert len(text) > 0

def test_invalid_file():
    """Test handling of invalid file."""
    extractor = TextExtractor()
    with pytest.raises(ValueError):
        extractor.extract("invalid.xyz")
```

### Test Requirements

- **Unit tests** for all new functions
- **Integration tests** for workflows
- **Edge case coverage** for error handling
- **Minimum 80% code coverage**

## Submitting Changes

### Commit Messages

Follow conventional commit format:

```
type(scope): brief description

Detailed explanation of what changed and why.

- Additional details
- As bullet points
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no functionality change)
- `refactor`: Code restructuring (no functionality change)
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat(clustering): add support for hierarchical clustering

Implemented hierarchical clustering algorithm as an alternative
to K-means. Users can now choose clustering method via GUI dropdown.

- Added HierarchicalClusterer class
- Updated GUI with method selection
- Added tests for hierarchical clustering
```

### Pull Request Process

1. **Update documentation** for any changed functionality
2. **Add/update tests** for new code
3. **Run full test suite** and ensure all tests pass
4. **Update CHANGELOG.md** with your changes
5. **Create pull request** with clear description:
   - What changed
   - Why it changed
   - How to test it

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] All existing tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No breaking changes (or documented if yes)
```

## Release Process

### Versioning

We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Creating a Release

1. **Update version** in:
   - `pyproject.toml`
   - `version_info.txt`
   - `installer.iss`

2. **Update CHANGELOG.md**:
   - Move unreleased changes to new version section
   - Add release date

3. **Create release commit**:
   ```bash
   git commit -m "chore: bump version to X.Y.Z"
   ```

4. **Tag the release**:
   ```bash
   git tag -a vX.Y.Z -m "Release version X.Y.Z"
   git push origin vX.Y.Z
   ```

5. **Build distribution**:
   ```bash
   python build_exe.py
   ```

6. **Create GitHub release** with:
   - Release notes from CHANGELOG
   - Compiled executables
   - Installer packages

## Questions or Issues?

- **Questions**: Open a GitHub Discussion
- **Bug Reports**: Open a GitHub Issue with:
  - Clear description
  - Steps to reproduce
  - Expected vs actual behavior
  - System information
- **Feature Requests**: Open a GitHub Issue with:
  - Use case description
  - Proposed solution
  - Alternative approaches considered

---

**Thank you for contributing to Genre-Based File Organizer!**

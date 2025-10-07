# Changelog

All notable changes to the Genre-Based File Organizer will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-15

### Added
- **GUI Application**: Professional Tkinter-based graphical interface
  - Browse dialog for folder selection
  - Configurable cluster count (Auto or 2-10 groups)
  - Real-time progress log with detailed status updates
  - Animated progress bar
  - Copy/Move operation toggle
  - Multi-threaded architecture for responsive UI

- **Core Features**:
  - Multi-format text extraction (Word .docx, Excel .xlsx, PowerPoint .pptx)
  - DistilBERT transformer model for semantic embeddings
  - FAISS-based similarity search and clustering
  - K-means clustering algorithm
  - Automatic cluster count determination
  - Intelligent file organization into semantic groups

- **Build System**:
  - PyInstaller spec file for advanced configuration
  - Windows version information file
  - Inno Setup installer script
  - Automated build scripts (build.bat, build.sh)
  - Self-contained executable with all dependencies embedded
  - Cross-platform support (Windows, macOS, Linux)

- **Documentation**:
  - Comprehensive README with quick start guide
  - BUILD_EXE.md - Complete build system documentation
  - DISTRIBUTION.md - Professional distribution guide
  - USER_EXPERIENCE.md - End-user journey documentation
  - GUI_OVERVIEW.md - GUI features and design
  - ARCHITECTURE.md - Technical architecture
  - USAGE.md - Comprehensive usage guide
  - QUICKREF.md - Quick reference for common tasks
  - INSTALL.md - Installation guide
  - TEST_CHECKLIST.md - Complete testing checklist

- **Testing**:
  - Unit tests for core functionality
  - Pre-release testing scripts
  - Comprehensive test checklist
  - CI/CD ready structure

- **Packaging**:
  - Modern pyproject.toml configuration
  - MIT License
  - Professional setup.py
  - Entry points for GUI and CLI

### Changed
- Terminology updated to emphasize technical components (DistilBERT, FAISS, K-means) instead of generic "AI" buzzwords

### Security
- All dependencies pinned to minimum secure versions
- Input validation for file paths
- Safe file operations with duplicate handling

## [Unreleased]

### Planned
- Additional file format support (PDF, TXT, CSV)
- Hierarchical clustering for multi-level organization
- Custom cluster naming/labeling
- Drag-and-drop folder selection
- Theme customization
- Multi-language support
- Cloud storage integration
- Automatic update checker
- Code signing for trusted distribution

---

## Release Notes

### Version 1.0.0 - Initial Release

This is the first production-ready release of Genre-Based File Organizer. The application provides:

**For End Users:**
- Simple installation via downloadable installer
- No Python or technical knowledge required
- Professional GUI interface
- Automatic semantic document organization
- Works with Word, Excel, and PowerPoint files

**For Developers:**
- Clean, modular architecture
- Comprehensive documentation
- Modern Python packaging
- Professional build system
- Easy to extend and customize

**System Requirements:**
- **Minimum**: Windows 10, 4 GB RAM, 2 GB disk space
- **Recommended**: Windows 11, 8 GB RAM, 5 GB disk space, GPU support

**Known Limitations:**
- First launch requires ~250 MB DistilBERT model download
- Large documents (>10,000 words) may take longer to process
- GPU acceleration requires CUDA-compatible graphics card

**Upgrade Notes:**
- This is the initial release - no upgrade path needed

---

**Contributors:** Genre File Organizer Team
**License:** MIT License
**Support:** GitHub Issues

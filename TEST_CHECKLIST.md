# Pre-Release Testing Checklist

Use this checklist before releasing any new version to ensure quality and reliability.

## Build Verification

- [ ] Executable builds without errors
- [ ] Installer builds successfully (Windows)
- [ ] File size is reasonable (~500 MB expected)
- [ ] Version information displays correctly in file properties
- [ ] All version numbers match across files (setup.py, installer.iss, version_info.txt)

---

## Clean System Tests (CRITICAL!)

### Windows
- [ ] Windows 10 (fresh install, no Python)
- [ ] Windows 11 (fresh install, no Python)
- [ ] Windows 10 with Windows Defender enabled
- [ ] Windows 10 with third-party antivirus (Norton/McAfee/Avast)

### macOS
- [ ] macOS 11 Big Sur or later (no Python)
- [ ] macOS with Gatekeeper enabled
- [ ] macOS with FileVault enabled

### Linux
- [ ] Ubuntu 20.04 LTS or later (no Python)
- [ ] Fedora or other distribution (no Python)

---

## User Account Tests

- [ ] Administrator/root account
- [ ] Standard user account
- [ ] User with limited permissions
- [ ] Non-English username/path

---

## Functionality Tests

### Application Launch
- [ ] Application launches successfully
- [ ] GUI displays correctly
- [ ] Window can be moved and resized
- [ ] Application appears in taskbar/dock

### Core Features
- [ ] Folder browse dialog works
- [ ] File selection and validation works
- [ ] Cluster count dropdown works
- [ ] Copy/Move toggle functions
- [ ] Organize button triggers processing
- [ ] Cancel button stops processing
- [ ] Clear log button works

### File Processing
- [ ] Organizes Word documents correctly
- [ ] Organizes Excel spreadsheets correctly
- [ ] Organizes PowerPoint presentations correctly
- [ ] Handles mixed file types
- [ ] Creates proper folder structure (Sorted, Cluster_X)
- [ ] Moves unsupported files to Unsorted folder
- [ ] Handles duplicate filenames correctly

### Progress and Feedback
- [ ] Progress bar updates during processing
- [ ] Log shows detailed status messages
- [ ] Success dialog appears on completion
- [ ] Error dialogs show for invalid inputs
- [ ] Application remains responsive during processing

### Error Handling
- [ ] Handles invalid folder paths
- [ ] Handles empty folders
- [ ] Handles folders with no supported files
- [ ] Handles permission denied errors
- [ ] Handles disk space issues
- [ ] Provides clear error messages

### Model Download (CRITICAL!)
- [ ] Model downloads successfully on first run
- [ ] Progress indication shows during download
- [ ] Download completes without errors
- [ ] Model is cached correctly
- [ ] Subsequent runs use cached model (no re-download)
- [ ] Works with slow internet connection
- [ ] Handles download interruptions gracefully
- [ ] Provides clear error if download fails

---

## Installation Tests (Windows)

- [ ] Installer welcome screen displays
- [ ] License agreement shows correctly
- [ ] Install location can be changed
- [ ] Default location is appropriate
- [ ] Desktop shortcut created (if selected)
- [ ] Start Menu shortcut created
- [ ] Application launches from shortcuts
- [ ] Application launches from Start Menu
- [ ] Uninstaller works correctly
- [ ] Uninstaller removes all files
- [ ] Uninstaller removes shortcuts
- [ ] Registry entries cleaned up (if any)

---

## Edge Cases

### System Conditions
- [ ] Low disk space (< 1 GB)
- [ ] Low memory (4 GB RAM)
- [ ] Running on system with Python installed
- [ ] Running on system without Python installed
- [ ] Multiple concurrent instances
- [ ] Application minimized during processing
- [ ] System sleep/hibernation during processing

### Display
- [ ] Different screen resolutions (1366x768, 1920x1080, 4K)
- [ ] Multiple monitors
- [ ] High DPI displays (150%, 200% scaling)
- [ ] Low resolution (1024x768)
- [ ] Ultra-wide monitors

### File System
- [ ] Files with special characters in names
- [ ] Very long file paths
- [ ] Files on network drives
- [ ] Files on external drives
- [ ] Read-only files
- [ ] Files in use by other programs

---

## Security Tests

- [ ] Windows SmartScreen doesn't block (or shows expected warning)
- [ ] Antivirus doesn't flag as malware
- [ ] Firewall doesn't block model download
- [ ] No code injection vulnerabilities
- [ ] No privilege escalation issues
- [ ] User data stays private (no telemetry)

---

## Performance Tests

- [ ] Small folder (< 10 files) processes quickly
- [ ] Medium folder (10-100 files) completes reasonably
- [ ] Large folder (100-1000 files) completes without crash
- [ ] Very large folder (1000+ files) handled appropriately
- [ ] Memory usage stays reasonable
- [ ] CPU usage is acceptable
- [ ] No memory leaks during extended use

---

## Documentation Tests

- [ ] README.md is up to date
- [ ] INSTALL.md instructions work
- [ ] BUILD_EXE.md builds successfully
- [ ] USER_EXPERIENCE.md matches actual experience
- [ ] DISTRIBUTION.md is accurate
- [ ] All screenshots in docs are current
- [ ] Links in documentation work

---

## Platform-Specific Tests

### Windows
- [ ] Works on Windows 10 Home
- [ ] Works on Windows 10 Pro
- [ ] Works on Windows 11
- [ ] UAC prompts are appropriate
- [ ] File associations work (if implemented)

### macOS
- [ ] Works on Intel Macs
- [ ] Works on Apple Silicon (M1/M2) Macs
- [ ] Gatekeeper warning is acceptable
- [ ] Notarization works (if signed)
- [ ] DMG mounts correctly

### Linux
- [ ] Works on Ubuntu/Debian
- [ ] Works on Fedora/RHEL
- [ ] Works on Arch Linux
- [ ] AppImage runs correctly
- [ ] Desktop file works

---

## Pre-Release Final Checks

- [ ] All critical bugs fixed
- [ ] All known issues documented
- [ ] CHANGELOG.md updated
- [ ] Version number incremented
- [ ] Git tag created
- [ ] Release notes written
- [ ] Screenshots updated
- [ ] Download links prepared

---

## Post-Release Monitoring

After release, monitor for:

- [ ] Download counts
- [ ] GitHub issues/bug reports
- [ ] User feedback and reviews
- [ ] Antivirus false positives
- [ ] Performance issues
- [ ] Feature requests

---

## Testing Tools

### Virtual Machines
- VMware Workstation/Fusion
- VirtualBox
- Parallels Desktop
- Windows Sandbox (Windows 10/11 Pro)

### Testing Services
- VirusTotal (antivirus scan)
- BrowserStack (cross-platform testing)
- Any.run (malware analysis sandbox)

### Utilities
- Process Explorer (monitor resources)
- Wireshark (network traffic)
- Dependency Walker (check DLL dependencies)

---

## Sign-Off

**Tested by:** ___________________

**Date:** ___________________

**Version:** ___________________

**Test Environment:**
- OS: ___________________
- RAM: ___________________
- Storage: ___________________

**Critical Issues Found:** ___________________

**Ready for Release:** ☐ Yes  ☐ No

---

## Notes

Use this space to record any observations, issues, or recommendations:

```
[Add notes here]
```

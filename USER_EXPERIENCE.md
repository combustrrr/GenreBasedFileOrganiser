# User Experience Guide

This document describes the complete user experience from downloading to using the Genre-Based File Organizer software.

## Download & Installation (Windows)

### Step 1: Download the Installer

Users download `GenreFileOrganizer_Setup_v1.0.0.exe` from:
- GitHub Releases page
- Your website
- Shared network location

**File size:** ~100-200 MB (includes all dependencies)

### Step 2: Run the Setup

**User Experience:**

1. **Double-click** `GenreFileOrganizer_Setup_v1.0.0.exe`

2. **Windows SmartScreen** may appear (first time)
   - Shows: "Windows protected your PC"
   - User clicks: "More info" → "Run anyway"
   - *Note: Code signing eliminates this (see BUILD_EXE.md)*

3. **Welcome Screen**
   ```
   ╔════════════════════════════════════════════╗
   ║  Welcome to Genre-Based File Organizer     ║
   ║  Setup Wizard                              ║
   ║                                            ║
   ║  This will install Genre-Based File        ║
   ║  Organizer on your computer.               ║
   ║                                            ║
   ║                                            ║
   ║                [Next]  [Cancel]            ║
   ╚════════════════════════════════════════════╝
   ```

4. **License Agreement**
   ```
   ╔════════════════════════════════════════════╗
   ║  Please review the license terms           ║
   ║                                            ║
   ║  MIT License                               ║
   ║  Copyright (c) 2024                        ║
   ║  [License text displayed here...]          ║
   ║                                            ║
   ║  ☑ I accept the agreement                 ║
   ║                                            ║
   ║  [Back]            [Next]  [Cancel]        ║
   ╚════════════════════════════════════════════╝
   ```

5. **Select Destination Location**
   ```
   ╔════════════════════════════════════════════╗
   ║  Where should we install?                  ║
   ║                                            ║
   ║  C:\Program Files\Genre-Based File         ║
   ║  Organizer                    [Browse...]  ║
   ║                                            ║
   ║  Space required: 200 MB                    ║
   ║  Space available: 50 GB                    ║
   ║                                            ║
   ║  [Back]            [Next]  [Cancel]        ║
   ╚════════════════════════════════════════════╝
   ```

6. **Select Start Menu Folder**
   ```
   ╔════════════════════════════════════════════╗
   ║  Select Start Menu folder                  ║
   ║                                            ║
   ║  Genre-Based File Organizer                ║
   ║                                            ║
   ║  ☐ Don't create a Start Menu folder       ║
   ║                                            ║
   ║  [Back]            [Next]  [Cancel]        ║
   ╚════════════════════════════════════════════╝
   ```

7. **Select Additional Tasks**
   ```
   ╔════════════════════════════════════════════╗
   ║  Which additional tasks should be          ║
   ║  performed?                                ║
   ║                                            ║
   ║  Additional icons:                         ║
   ║  ☐ Create a desktop icon                  ║
   ║  ☐ Create a Quick Launch icon             ║
   ║                                            ║
   ║  [Back]            [Next]  [Cancel]        ║
   ╚════════════════════════════════════════════╝
   ```

8. **Ready to Install**
   ```
   ╔════════════════════════════════════════════╗
   ║  Ready to Install                          ║
   ║                                            ║
   ║  Setup is now ready to begin installing   ║
   ║  Genre-Based File Organizer on your        ║
   ║  computer.                                 ║
   ║                                            ║
   ║  Destination:                              ║
   ║  C:\Program Files\Genre-Based File...      ║
   ║                                            ║
   ║  [Back]          [Install]  [Cancel]       ║
   ╚════════════════════════════════════════════╝
   ```

9. **Installing**
   ```
   ╔════════════════════════════════════════════╗
   ║  Installing                                ║
   ║                                            ║
   ║  Please wait while Setup installs         ║
   ║  Genre-Based File Organizer on your        ║
   ║  computer.                                 ║
   ║                                            ║
   ║  [████████████████░░░░░░░░░░] 60%         ║
   ║                                            ║
   ║  Extracting files...                       ║
   ║                                            ║
   ║                            [Cancel]        ║
   ╚════════════════════════════════════════════╝
   ```

10. **Completing Setup**
    ```
    ╔════════════════════════════════════════════╗
    ║  Completing the Setup Wizard               ║
    ║                                            ║
    ║  Setup has finished installing             ║
    ║  Genre-Based File Organizer on your        ║
    ║  computer.                                 ║
    ║                                            ║
    ║  ☑ Launch Genre-Based File Organizer      ║
    ║                                            ║
    ║  Click Finish to exit Setup.               ║
    ║                                            ║
    ║                          [Finish]          ║
    ╚════════════════════════════════════════════╝
    ```

### Step 3: Installation Complete

**What Gets Installed:**

1. **Program Files:**
   - `C:\Program Files\Genre-Based File Organizer\`
     - `GenreFileOrganizer.exe` (main executable)
     - `README.md` (documentation)
     - `BUILD_EXE.md` (build guide)
     - `INSTALL.md` (installation guide)
     - `unins000.exe` (uninstaller)
     - `unins000.dat` (uninstaller data)

2. **Start Menu:**
   - `Start → Programs → Genre-Based File Organizer`
     - Genre-Based File Organizer (launches app)
     - Uninstall Genre-Based File Organizer

3. **Desktop (if selected):**
   - `Genre-Based File Organizer` shortcut icon

4. **Quick Launch (if selected):**
   - Quick Launch toolbar icon

## First Launch

### Initial Model Download

When users first launch the application:

1. **Application opens** with GUI interface

2. **First-time setup** (happens automatically):
   ```
   ╔════════════════════════════════════════════╗
   ║  First-Time Setup                          ║
   ║                                            ║
   ║  Downloading DistilBERT model...           ║
   ║                                            ║
   ║  [████████████░░░░░░░░░░░░░░░] 50%        ║
   ║                                            ║
   ║  150 MB / 250 MB                           ║
   ║                                            ║
   ║  This only happens once.                   ║
   ║  Please wait...                            ║
   ╚════════════════════════════════════════════╝
   ```

3. **Model cached** in:
   - `C:\Users\[Username]\.cache\huggingface\`
   - Subsequent launches use cached model (instant start)

### Main Application Interface

```
╔═══════════════════════════════════════════════════════════════╗
║  Genre-Based File Organizer                                   ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Source Folder:                                               ║
║  [C:\Users\John\Documents\MyFiles        ] [Browse...]       ║
║                                                               ║
║  Output Folder:                                               ║
║  [C:\Users\John\Documents\MyFiles        ] [Browse...]       ║
║                                                               ║
║  Number of Clusters: [Auto ▼]                                ║
║                                                               ║
║  ☑ Copy files (keep originals)                               ║
║  ☐ Move files (remove originals)                             ║
║                                                               ║
║  [Organize Files]  [Cancel]  [Clear Log]                     ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ Progress Log:                                           │ ║
║  │                                                         │ ║
║  │ Ready to organize files...                             │ ║
║  │                                                         │ ║
║  │                                                         │ ║
║  │                                                         │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
║  [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0%               ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

## Using the Software

### Basic Workflow

1. **Select Source Folder**
   - Click "Browse..." next to Source Folder
   - Navigate to folder containing documents
   - Click "Select Folder"

2. **Configure Settings** (optional)
   - Choose number of clusters or use Auto
   - Select Copy or Move operation

3. **Organize Files**
   - Click "Organize Files" button
   - Watch progress in real-time:
     ```
     Progress Log:
     
     Scanning folder: C:\Users\John\Documents\MyFiles
     Found 47 supported files
     Extracting text from: report.docx
     Extracting text from: budget.xlsx
     Extracting text from: presentation.pptx
     ...
     Generating embeddings (this may take a moment)...
     Processing batch 1/3...
     Clustering documents into 3 groups...
     Creating Cluster_0 folder...
     Copying ml_basics.docx to Cluster_0
     Copying ai_models.xlsx to Cluster_0
     ...
     
     ✓ Organization complete!
     Files organized into 3 clusters
     ```

4. **View Results**
   - Success dialog appears:
     ```
     ╔════════════════════════════════════════════╗
     ║  Success!                                  ║
     ║                                            ║
     ║  47 files organized into 3 clusters        ║
     ║                                            ║
     ║  Output location:                          ║
     ║  C:\Users\John\Documents\MyFiles\Sorted    ║
     ║                                            ║
     ║                    [OK]                    ║
     ╚════════════════════════════════════════════╝
     ```

5. **Check Organized Files**
   - Navigate to: `[Source Folder]\Sorted\`
   - Find clustered folders:
     - `Cluster_0\` (ML/AI documents)
     - `Cluster_1\` (Food/cooking documents)
     - `Cluster_2\` (Business/finance documents)

## Uninstalling

### Using Control Panel

1. **Open Control Panel**
   - Windows 10: Start → Settings → Apps
   - Windows 11: Start → Settings → Apps → Installed apps

2. **Find Application**
   - Search for "Genre-Based File Organizer"

3. **Uninstall**
   - Click "Uninstall" button
   - Confirm when prompted

4. **Uninstaller Wizard**
   ```
   ╔════════════════════════════════════════════╗
   ║  Uninstall Genre-Based File Organizer      ║
   ║                                            ║
   ║  Are you sure you want to completely       ║
   ║  remove Genre-Based File Organizer and     ║
   ║  all of its components?                    ║
   ║                                            ║
   ║                                            ║
   ║            [Yes]          [No]             ║
   ╚════════════════════════════════════════════╝
   ```

5. **Uninstalling**
   ```
   ╔════════════════════════════════════════════╗
   ║  Uninstalling                              ║
   ║                                            ║
   ║  [████████████████████████████] 100%       ║
   ║                                            ║
   ║  Removing files...                         ║
   ╚════════════════════════════════════════════╝
   ```

6. **Complete**
   ```
   ╔════════════════════════════════════════════╗
   ║  Uninstall Complete                        ║
   ║                                            ║
   ║  Genre-Based File Organizer has been       ║
   ║  successfully removed from your            ║
   ║  computer.                                 ║
   ║                                            ║
   ║                    [OK]                    ║
   ╚════════════════════════════════════════════╝
   ```

### Using Start Menu

Alternative method:
- Start → Programs → Genre-Based File Organizer
- Click "Uninstall Genre-Based File Organizer"
- Follow uninstaller wizard

### What Gets Removed

**Automatically removed:**
- Program files in `C:\Program Files\Genre-Based File Organizer\`
- Start Menu shortcuts
- Desktop shortcut (if created)
- Quick Launch icon (if created)
- Uninstaller files

**User data preserved** (by design):
- Downloaded DistilBERT model in `.cache\huggingface\`
- Log files in user AppData
- Organized files created by the application

**To manually remove user data** (optional):
1. Delete: `C:\Users\[Username]\.cache\huggingface\`
2. Delete: `C:\Users\[Username]\AppData\Roaming\GenreFileOrganizer\`

## macOS Experience

### Download & Installation

1. **Download**: `GenreFileOrganizer.dmg`
2. **Open DMG**: Double-click to mount
3. **Install**: Drag `GenreFileOrganizer.app` to Applications folder
4. **First Launch**: 
   - Right-click → Open (first time only)
   - Allow in System Preferences if prompted
5. **Use**: Launch from Applications or Spotlight

### Uninstall

1. Open Applications folder
2. Drag `GenreFileOrganizer.app` to Trash
3. Empty Trash

## Linux Experience

### Installation

**Option 1: AppImage**
```bash
chmod +x GenreFileOrganizer.AppImage
./GenreFileOrganizer.AppImage
```

**Option 2: Binary**
```bash
chmod +x GenreFileOrganizer
./GenreFileOrganizer
```

**Option 3: Package Manager** (if .deb/.rpm created)
```bash
# Debian/Ubuntu
sudo dpkg -i genrefileorganizer_1.0.0_amd64.deb

# Fedora/RHEL
sudo rpm -i genrefileorganizer-1.0.0.x86_64.rpm
```

### Uninstall

**AppImage/Binary:**
- Simply delete the file

**Package:**
```bash
# Debian/Ubuntu
sudo apt remove genrefileorganizer

# Fedora/RHEL
sudo rpm -e genrefileorganizer
```

## Troubleshooting Common Issues

### Windows SmartScreen Warning

**Issue:** "Windows protected your PC" warning

**Solution:**
- Click "More info" → "Run anyway"
- Or: Get code signing certificate (see BUILD_EXE.md)

### Antivirus False Positive

**Issue:** Antivirus blocks or quarantines the installer

**Solution:**
- Whitelist the file in antivirus settings
- Or: Submit to antivirus vendor for review
- Or: Get code signing certificate

### Model Download Fails

**Issue:** DistilBERT model download error on first run

**Solution:**
- Check internet connection
- Check firewall settings
- Try again later (HuggingFace servers may be busy)

### Out of Memory

**Issue:** Application crashes with large file sets

**Solution:**
- Process fewer files at once
- Close other applications
- Use a computer with more RAM (8GB+ recommended)

### Files Not Organizing Correctly

**Issue:** Files grouped unexpectedly

**Solution:**
- Ensure files contain actual text content
- Try adjusting number of clusters
- Check that files are .docx, .xlsx, or .pptx format

## System Requirements

**Minimum:**
- Windows 10 / macOS 10.14 / Ubuntu 18.04 or later
- 4 GB RAM
- 500 MB disk space (+ 250 MB for model on first run)
- Internet connection (first run only)

**Recommended:**
- Windows 11 / macOS 12 / Ubuntu 22.04 or later
- 8 GB RAM or more
- 1 GB disk space
- GPU with CUDA support (optional, for faster processing)

## Support

For help and support:
- Documentation: See README.md, USAGE.md, QUICKREF.md
- Issues: https://github.com/combustrrr/GenreBasedFileOrganiser/issues
- Logs: Check `file_organizer.log` in application directory

## Updates

**Checking for updates:**
- Currently: Manual check on GitHub Releases
- Future: Automatic update checker (planned)

**Installing updates:**
1. Download new installer
2. Run new installer (will upgrade existing installation)
3. Keep your organized files (they're not affected)

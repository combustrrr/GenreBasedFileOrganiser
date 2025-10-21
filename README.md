# GenreBasedFileOrganiser

An intelligent file organizer with a user-friendly GUI that reads and understands document content using Natural Language Processing. It extracts text from Word, Excel, and PowerPoint files, converts meaning into embeddings via DistilBERT transformer model, and clusters similar files using FAISS. This enables automatic genre-based organization—grouping related documents by semantic similarity without relying on filenames or manual sorting.

## Features

- **🖥️ User-Friendly GUI**: Beautiful graphical interface for easy file organization
- **🧠 Semantic Analysis**: Uses DistilBERT transformer model for deep content understanding
- **📄 Multi-Format Support**: Extracts text from `.docx`, `.xlsx`, and `.pptx` files
- **🎯 FAISS Clustering**: Groups similar documents using Facebook AI Similarity Search
- **⚡ Efficient Processing**: Fast embedding generation and clustering even for large document sets
- **🔍 Similar File Search**: Find documents similar to a given file
- **🎨 Flexible Organization**: Auto-determine optimal clusters or specify custom number
- **📦 Easy Installation**: Install as a standalone application

## Installation

### For End Users (No Python Required)

**Download the standalone executable** - Just like Chrome or VS Code!

1. Download `GenreFileOrganizer_Setup.exe` (Windows), `.dmg` (macOS), or `.AppImage` (Linux)
2. Run the installer
3. Launch the application
4. **Done!** No Python or dependencies needed

The standalone version includes:
- ✅ Python interpreter (bundled inside)
- ✅ All libraries (PyTorch, Transformers, FAISS, etc.)
- ✅ Complete application
- ✅ Everything in ONE file

**[Download releases](#)** | **[Build instructions](BUILD_EXE.md)**

### For Developers (Python Required)

#### Prerequisites

- Python 3.8 or higher
- pip package manager
- 2GB+ RAM for AI models

### Quick Install

1. Clone the repository:
```bash
git clone https://github.com/combustrrr/GenreBasedFileOrganiser.git
cd GenreBasedFileOrganiser
```

2. Install the application:
```bash
pip install -e .
```

3. Verify installation:
```bash
python check_deps.py
```

For detailed installation instructions, including creating desktop shortcuts and building standalone executables, see [INSTALL.md](INSTALL.md).

The first time you run the organizer, it will download the DistilBERT model (~250MB).

## Usage

### GUI Application (Recommended)

Launch the graphical interface:

```bash
python main.py
```

Or use the installed command:
```bash
file-organizer-gui
```

**Using the GUI:**
1. Click "Browse..." to select a folder containing your documents
2. Choose the number of groups (or leave as "Auto")
3. Select whether to copy or move files
4. Click "Organize Files" to start
5. Watch the progress in real-time
6. View results in the "Sorted" folder

### Command Line Interface

For advanced users or automation:

Basic usage:
```bash
python organize.py /path/to/your/files
```

Specify output directory:
```bash
python organize.py /path/to/files -o /path/to/organized
```

Set specific number of clusters:
```bash
python organize.py /path/to/files -n 5
```

Move files instead of copying:
```bash
python organize.py /path/to/files --move
```

Find similar files:
```bash
python organize.py /path/to/files --similar example.docx -k 10
```

### Python API

```python
from file_organizer import GenreBasedFileOrganizer

# Initialize the organizer
organizer = GenreBasedFileOrganizer()

# Organize files
cluster_map = organizer.organize_files(
    source_dir="./my_files",
    output_dir="./organized",
    n_clusters=None,  # Auto-determine
    copy_files=True   # Copy instead of move
)

# Find similar files
similar = organizer.find_similar_files("example.docx", k=5)
```

## How It Works

1. **Text Extraction**: Extracts text content from Word, Excel, and PowerPoint files
   - Word: Paragraphs and tables
   - Excel: All cells across all sheets
   - PowerPoint: All text shapes in all slides

2. **Embedding Generation**: Converts text to semantic embeddings using DistilBERT
   - Uses the `[CLS]` token representation for document-level embeddings
   - 768-dimensional vectors capture semantic meaning

3. **FAISS Clustering**: Groups similar documents using FAISS and K-means
   - FAISS index enables efficient similarity search
   - K-means algorithm clusters documents into semantic groups
   - Auto-determines optimal cluster count or accepts custom value

4. **Organization**: Moves/copies files into cluster folders
   - Creates folders named `Cluster_0`, `Cluster_1`, etc.
   - Each folder contains semantically similar documents

## Building Standalone Executable

Create a **single, self-contained executable** - just like Chrome or VS Code!

### Quick Build

**Windows:**
```batch
build.bat
```

**macOS/Linux:**
```bash
chmod +x build.sh
./build.sh
```

### What You Get

- **ONE FILE** with everything bundled inside
- **NO Python** installation required for users
- **ALL dependencies** embedded (PyTorch, Transformers, FAISS, etc.)
- **Ready to distribute** to anyone

### Output Locations

- Windows: `dist/GenreFileOrganizer.exe`
- macOS: `dist/GenreFileOrganizer.app`
- Linux: `dist/GenreFileOrganizer`

### Creating Professional Installer

**Windows (Inno Setup):**
```bash
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
```
Output: `installer_output/GenreFileOrganizer_Setup_v1.0.0.exe`

For complete build instructions, see [BUILD_EXE.md](BUILD_EXE.md).

## Architecture

```
┌─────────────────┐
│  Office Files   │
│ (.docx, .xlsx,  │
│     .pptx)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Text Extractor  │ (text_extractor.py)
│  - python-docx  │
│  - openpyxl     │
│  - python-pptx  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   DistilBERT    │ (embedding_generator.py)
│ Transformer Model│
│  (768-dim)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ FAISS Clustering│ (clusterer.py)
│   + K-means     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  File Organizer │ (file_organizer.py)
│ Cluster folders │
└─────────────────┘
```

## Examples

See `example.py` for detailed usage examples:

```bash
python example.py
```

## Requirements

- torch >= 2.0.0
- transformers >= 4.30.0
- faiss-cpu >= 1.7.4
- python-docx >= 0.8.11
- openpyxl >= 3.0.10
- python-pptx >= 0.6.21
- numpy >= 1.24.0
- scikit-learn >= 1.3.0

## Performance

- **Speed**: Processes ~10-20 documents per minute (depends on document size and hardware)
- **Accuracy**: DistilBERT transformer model provides high-quality semantic understanding
- **Scalability**: FAISS enables efficient clustering even with thousands of documents

## Limitations

- Only supports `.docx`, `.xlsx`, and `.pptx` files (not older `.doc`, `.xls`, `.ppt` formats)
- Requires sufficient RAM for loading transformer model (~1-2GB)
- Processing time increases with document count and size

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Documentation

### For Users
- **[USER_EXPERIENCE.md](USER_EXPERIENCE.md)**: End-user installation and usage experience
- **[QUICKREF.md](QUICKREF.md)**: Quick reference guide for common tasks
- **[USAGE.md](USAGE.md)**: Comprehensive usage guide with examples

### For Developers
- **[BUILD_EXE.md](BUILD_EXE.md)**: Building standalone executables
- **[DISTRIBUTION.md](DISTRIBUTION.md)**: Distribution, testing, and release guide
- **[TEST_CHECKLIST.md](TEST_CHECKLIST.md)**: Pre-release testing checklist
- **[INSTALL.md](INSTALL.md)**: Developer installation guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Technical architecture documentation
- **[GUI_OVERVIEW.md](GUI_OVERVIEW.md)**: GUI design and features

## License

This project is open source and available under the MIT License.

## Technical Components

- **DistilBERT**: Hugging Face transformer model for text embeddings
- **FAISS**: Facebook AI Similarity Search for efficient clustering
- **Document Libraries**: python-docx, openpyxl, python-pptx for text extraction
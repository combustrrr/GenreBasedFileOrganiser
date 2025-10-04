# Quick Reference Guide

## Installation

```bash
git clone https://github.com/combustrrr/GenreBasedFileOrganiser.git
cd GenreBasedFileOrganiser
pip install -r requirements.txt
python check_deps.py
```

## Basic Usage

```bash
# Organize files in a directory
python organize.py /path/to/files

# Organize to specific output
python organize.py /path/to/files -o /path/to/output

# Move files instead of copying
python organize.py /path/to/files --move

# Find similar files
python organize.py /path/to/files --similar example.docx
```

## Python API

```python
from file_organizer import GenreBasedFileOrganizer

organizer = GenreBasedFileOrganizer()
cluster_map = organizer.organize_files(
    source_dir="./files",
    output_dir="./organized",
    n_clusters=None,
    copy_files=True
)
```

## Supported File Types

- `.docx` - Microsoft Word documents
- `.xlsx` - Microsoft Excel spreadsheets
- `.pptx` - Microsoft PowerPoint presentations

## Output Structure

```
organized/
├── group_0/          # Cluster 0 (e.g., AI/ML documents)
│   ├── file1.docx
│   └── file2.xlsx
├── group_1/          # Cluster 1 (e.g., recipes)
│   └── file3.pptx
└── group_2/          # Cluster 2 (e.g., business reports)
    └── file4.docx
```

## Components

| Module | Purpose |
|--------|---------|
| `text_extractor.py` | Extract text from Office files |
| `embedding_generator.py` | Generate DistilBERT embeddings |
| `clusterer.py` | FAISS-based clustering |
| `file_organizer.py` | Main orchestration |
| `organize.py` | CLI interface |
| `example.py` | Usage examples |
| `check_deps.py` | Dependency checker |
| `test_organizer.py` | Unit tests |

## Documentation

- **README.md** - Overview and quick start
- **USAGE.md** - Comprehensive usage guide
- **ARCHITECTURE.md** - Technical architecture
- **QUICKREF.md** - This file

## Common Commands

```bash
# Check dependencies
python check_deps.py

# Run examples
python example.py

# Run tests
python test_organizer.py

# Get help
python organize.py --help
```

## Key Features

- 🤖 AI-powered semantic understanding (DistilBERT)
- 📄 Multi-format support (Word, Excel, PowerPoint)
- 🎯 Smart clustering (FAISS + K-means)
- ⚡ Efficient batch processing
- 🔍 Similarity search
- 🎨 Auto or manual cluster count

## Requirements

- Python 3.8+
- 2GB+ RAM
- 500MB+ disk space (for model)

## Performance

- Text extraction: ~100-500 files/min
- Embedding (CPU): ~10-20 files/min
- Embedding (GPU): ~100-200 files/min
- Clustering: ~1000 files/sec

## Troubleshooting

**Missing dependencies:**
```bash
pip install -r requirements.txt
```

**Import errors:**
```bash
python check_deps.py
```

**Slow processing:**
- Normal on CPU (~10-20 files/min)
- Use GPU for 10x speedup

**Empty clusters:**
- Documents may have too little text
- Try manual cluster count: `-n 3`

## Examples

**Example 1: Basic organization**
```bash
python organize.py ~/Documents/Reports
```

**Example 2: Custom clusters**
```bash
python organize.py ~/Documents -n 5 -o ~/Organized
```

**Example 3: Similarity search**
```bash
python organize.py ~/Documents --similar template.docx -k 10
```

**Example 4: Python API**
```python
from file_organizer import GenreBasedFileOrganizer

org = GenreBasedFileOrganizer()
org.organize_files("./docs", "./sorted", n_clusters=3)
```

## Support

- Issues: https://github.com/combustrrr/GenreBasedFileOrganiser/issues
- Documentation: See USAGE.md and ARCHITECTURE.md

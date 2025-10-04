# GenreBasedFileOrganiser

An AI-powered file organizer that reads and understands document content using NLP. It extracts text from Word, Excel, and PowerPoint files, converts meaning into embeddings via DistilBERT, and clusters similar files using FAISS. This enables automatic genre-based organization—grouping related documents intelligently without relying on filenames or manual sorting.

## Features

- **🤖 AI-Powered Analysis**: Uses DistilBERT transformer model for deep semantic understanding
- **📄 Multi-Format Support**: Extracts text from `.docx`, `.xlsx`, and `.pptx` files
- **🎯 Smart Clustering**: Groups similar documents using FAISS-based similarity search
- **⚡ Efficient Processing**: Fast embedding generation and clustering even for large document sets
- **🔍 Similar File Search**: Find documents similar to a given file
- **🎨 Flexible Organization**: Auto-determine optimal clusters or specify custom number

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/combustrrr/GenreBasedFileOrganiser.git
cd GenreBasedFileOrganiser
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Verify installation:
```bash
python check_deps.py
```

The first time you run the organizer, it will download the DistilBERT model (~250MB).

## Usage

### Command Line Interface

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

3. **Clustering**: Groups similar documents using FAISS and K-means
   - FAISS index enables efficient similarity search
   - K-means clusters documents into semantic groups
   - Auto-determines optimal cluster count or accepts custom value

4. **Organization**: Moves/copies files into group folders
   - Creates folders named `group_0`, `group_1`, etc.
   - Each folder contains semantically similar documents

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
│  Embedding Gen  │
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
│  Group folders  │
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
- **Accuracy**: DistilBERT provides high-quality semantic understanding
- **Scalability**: FAISS enables efficient clustering even with thousands of documents

## Limitations

- Only supports `.docx`, `.xlsx`, and `.pptx` files (not older `.doc`, `.xls`, `.ppt` formats)
- Requires sufficient RAM for loading transformer model (~1-2GB)
- Processing time increases with document count and size

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Documentation

- **[USAGE.md](USAGE.md)**: Comprehensive usage guide with examples
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Detailed architecture and design documentation

## License

This project is open source and available under the MIT License.

## Acknowledgments

- **DistilBERT**: Hugging Face transformers library
- **FAISS**: Facebook AI Similarity Search
- **Document Libraries**: python-docx, openpyxl, python-pptx